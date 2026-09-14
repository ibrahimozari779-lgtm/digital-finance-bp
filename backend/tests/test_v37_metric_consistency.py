from __future__ import annotations
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from finance_engine.core_metrics import build_core_metrics
from finance_engine.cash_conversion_engine import build_cash_conversion_cycle
from finance_engine.trend_engine import build_trend_analysis, _clean_period_label
from finance_engine.decision_engine import build_finance_business_partner_analysis


def test_core_metrics_deterministic_ssot():
    statements = {
        "profit_and_loss": {
            "Net sales": 9880000.0,
            "COGS": 7410000.0,
            "Gross profit": 2470000.0,
            "Operating profit": 988000.0,
            "Net profit": 494000.0,
        },
        "balance_sheet": {
            "Total assets": 12000000.0,
            "Current assets": 6000000.0,
            "Current liabilities": 4000000.0,
            "Total equity incl. current result": 5000000.0,
        },
        "kpis": {
            "receivables": 1400000.0,
            "inventory": 1200000.0,
            "payables": 1000000.0,
            "gross_margin_pct": 25.0,
            "operating_margin_pct": 10.0,
            "net_margin_pct": 5.0,
        },
        "period_metadata": {"period_days": 365, "label": "2025/12"},
        "controls": {"result_control": {}},
    }
    quality = {"score": 95.0, "status": "Trusted", "internal_consistency_status": "Trusted"}
    ccc = build_cash_conversion_cycle(statements, period_days=365)

    cm = build_core_metrics(
        statements=statements,
        quality=quality,
        ccc=ccc,
        health_score=85.0,
        health_label="Güçlü",
        data_hub=None,
    )

    # 1. Verify exact SSOT values
    assert cm["canonical_net_sales"] == 9880000.0
    assert cm["gross_profit"] == 2470000.0
    assert cm["operating_profit"] == 988000.0
    assert cm["net_profit"] == 494000.0
    assert cm["gross_margin_pct"] == 25.0
    assert cm["operating_margin_pct"] == 10.0
    assert cm["net_margin_pct"] == 5.0

    # 2. Verify DSO, DIO, DPO, CCC identity
    assert cm["dso_days"] == ccc["dso_days"]
    assert cm["dio_days"] == ccc["dio_days"]
    assert cm["dpo_days"] == ccc["dpo_days"]
    assert cm["ccc_days"] == ccc["cash_conversion_cycle_days"]

    # 3. Verify math: DSO = 1.4M / 9.88M * 365 = 51.7 or 51.9 days
    assert abs(cm["dso_days"] - (1400000.0 / 9880000.0 * 365)) < 0.1
    # CCC = DSO + DIO - DPO
    expected_ccc = round(cm["dso_days"] + cm["dio_days"] - cm["dpo_days"], 1)
    assert abs(cm["ccc_days"] - expected_ccc) < 0.2

    # 4. Canonical source attribution
    assert cm["dso_source"] == "mizan_120"
    assert "Mizan 120" in cm["dso_source_label"]


def test_core_metrics_two_layer_audit_and_conditional_score():
    statements = {
        "profit_and_loss": {"Net sales": 10000000.0, "Gross profit": 2500000.0},
        "balance_sheet": {"Total assets": 10000000.0},
        "kpis": {"receivables": 1400000.0},
        "period_metadata": {"period_days": 365},
        "controls": {"result_control": {}},
    }
    quality = {"score": 65.0, "status": "Caution", "internal_consistency_status": "Trusted"}
    ccc = {"dso_days": 51.9, "dio_days": 40.0, "dpo_days": 34.0, "cash_conversion_cycle_days": 57.8}

    # Simulate data hub with 71.4% mismatch in receivables (GL 1.4M vs AR 2.4M)
    data_hub = {
        "analysis_ar": {"dso_days": 88.9, "outstanding": 2400001.0},
        "reconciliation": {
            "checks": [
                {
                    "name": "Trade Receivables vs AR Aging",
                    "status": "material_difference",
                    "difference_pct": 71.4,
                    "gl_value": 1400000.0,
                    "source_value": 2400001.0,
                }
            ]
        },
    }

    cm = build_core_metrics(
        statements=statements,
        quality=quality,
        ccc=ccc,
        health_score=91.0,
        health_label="Güçlü",
        data_hub=data_hub,
    )

    # Katman 1: Mizan içi denklik tam
    assert cm["audit_layer_a_internal_equation"] == "Trusted"
    # Katman 2: Alt defter farkı var
    assert cm["audit_layer_b_subledger_reconciliation"] == "review"
    assert cm["is_conditional_score"] is True
    assert "Şartlı" in cm["health_label"]
    assert cm["conditional_badge"] is not None
    assert "%71.4" in cm["conditional_badge"]["warning_text"]
    assert cm["subledger_ar_dso_days"] == 88.9
    assert "AR Yaşlandırma" in cm["subledger_ar_source_label"]


def test_trend_engine_period_days_and_label_cleaning():
    stmt1 = {
        "profit_and_loss": {"Net sales": 8000000.0, "Gross profit": 2000000.0, "Operating profit": 800000.0, "Net profit": 400000.0},
        "balance_sheet": {"Total assets": 10000000.0, "Total equity incl. current result": 4000000.0},
        "kpis": {"receivables": 1000000.0, "inventory": 800000.0, "payables": 600000.0, "financial_debt": 2000000.0},
        "period_metadata": {"period_days": 365, "label": "2024/12"},
    }
    stmt2 = {
        "profit_and_loss": {"Net sales": 10000000.0, "Gross profit": 2500000.0, "Operating profit": 1000000.0, "Net profit": 500000.0},
        "balance_sheet": {"Total assets": 12000000.0, "Total equity incl. current result": 5000000.0},
        "kpis": {"receivables": 1400000.0, "inventory": 1200000.0, "payables": 1000000.0, "financial_debt": 2500000.0},
        "period_metadata": {"period_days": 365, "label": "2025/12"},
    }

    trend = build_trend_analysis(
        current_statements=stmt2,
        previous_periods=[{"label": "demo_data/sample_mizan_2024_donem1.xlsx", "statements": stmt1}],
        current_label="demo_data/sample_mizan_2025_donem2.xlsx",
    )

    assert trend["available"] is True
    # Test label cleaning: filenames must be converted to user-friendly titles
    labels = trend["period_labels"]
    assert "Önceki Dönem (2024)" in labels[0] or "2024" in labels[0]
    assert "Cari Dönem (2025)" in labels[1] or "2025" in labels[1]

    # Test unit helper
    assert _clean_period_label("hub_mizan_prior.xlsx", "Dönem 1") == "Önceki Dönem (2024)"
    assert _clean_period_label("hub_mizan.xlsx", "Dönem 2") == "Cari Dönem (2025)"
