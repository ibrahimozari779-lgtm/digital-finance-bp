"""CFO & Senior Auditor Hardening Tests.

Verifies that the 11 mathematical, consistency, and data-binding flaws
flagged during the CFO audit cannot silently regress:
1. TMS 7 reconciliation: A + B + C == Net Cash Change with 0.0 difference.
2. Cash realization metric: operating profit vs net profit distinction and labels.
3. Executive summary narrative alignment with profit base.
4. Tax strategy: current tax expense context, legal caveats on VUK 323, advisory framing.
5. Product profitability margin tolerance (near-average products not flagged as dragging).
6. Frontend template contract: CFO PDF variables, 13w projection, runway binding, no 0 || 45 fallback.
"""
from __future__ import annotations

import os
import re
import pytest

from finance_engine.cash_flow_engine import build_cash_flow_engine
from finance_engine.cash_bridge_engine import build_cash_bridge
from finance_engine.executive_summary_engine import build_executive_summary
from finance_engine.tax_strategy_engine import build_tax_strategy_analysis
from finance_engine.product_profitability_engine import build_product_profitability_analysis


def test_tms7_mathematical_reconciliation_zero_diff():
    """Verify TMS 7 mathematical identity A + B + C == Net Cash Change with 0 diff."""
    statements = {
        "profit_and_loss": {"Net sales": 10_800_000.0, "Net profit": 72_000.0, "Finance costs": 750_000.0, "Operating profit": 800_000.0},
        "balance_sheet": {
            "Total assets": 6_650_000.0,
            "Current assets": 4_550_000.0,
            "Non-current assets": 2_100_000.0,
            "Total equity incl. current result": 2_000_000.0,
            "Current liabilities": 3_150_000.0,
            "Non-current liabilities": 1_500_000.0,
        },
        "kpis": {"receivables": 2_400_000.0, "inventory": 1_900_000.0, "payables": 850_000.0, "cash": 250_000.0, "financial_debt": 2_200_000.0},
    }
    prior_statements = {
        "profit_and_loss": {"Net sales": 9_000_000.0, "Net profit": 500_000.0, "Finance costs": 200_000.0, "Operating profit": 750_000.0},
        "balance_sheet": {
            "Total assets": 5_000_000.0,
            "Current assets": 3_300_000.0,
            "Non-current assets": 1_700_000.0,
            "Total equity incl. current result": 2_000_000.0,
            "Current liabilities": 2_000_000.0,
            "Non-current liabilities": 1_000_000.0,
        },
        "kpis": {"receivables": 1_400_000.0, "inventory": 1_000_000.0, "payables": 900_000.0, "cash": 800_000.0, "financial_debt": 1_000_000.0},
    }
    cf = build_cash_flow_engine(statements, previous_statement=prior_statements)
    assert cf["available"] is True
    tms7 = cf["tms7_statement"]
    op_cf = tms7["operating_activities"]["net_operating_cash_flow"]
    inv_cf = tms7["investing_activities"]["net_investing_cash_flow"]
    fin_cf = tms7["financing_activities"]["net_financing_cash_flow"]
    net_change = tms7["summary"]["net_cash_change"]

    assert round(op_cf + inv_cf + fin_cf, 2) == round(net_change, 2)
    assert tms7["summary"]["reconciliation_difference"] == 0.0


def test_cash_realization_metrics_and_labels():
    """Verify operating profit vs net profit cash realization metrics."""
    ck = {"cash": 250_000.0, "receivables": 2_400_000.0, "inventory": 1_900_000.0, "payables": 850_000.0, "financial_debt": 2_200_000.0}
    pk = {"cash": 800_000.0, "receivables": 1_400_000.0, "inventory": 1_000_000.0, "payables": 900_000.0, "financial_debt": 1_000_000.0}
    c_pl = {"Operating profit": 800_000.0, "Net profit": 72_000.0, "Finance costs": 750_000.0}
    p_pl = {"Operating profit": 750_000.0, "Net profit": 500_000.0}
    bridge = build_cash_bridge({"kpis": ck, "profit_and_loss": c_pl}, {"kpis": pk, "profit_and_loss": p_pl})

    assert bridge["available"] is True
    assert "Faaliyet Kârı" in bridge["profit_base_label"]
    assert bridge["operating_profit_cash_realization_pct"] is not None
    assert bridge["net_profit_cash_realization_pct"] is not None
    assert bridge["operating_profit_cash_realization_pct"] == pytest.approx(-143.8, rel=1e-2)
    assert bridge["net_profit_cash_realization_pct"] == pytest.approx(-1597.2, rel=1e-2)


def test_executive_summary_cash_realization_wording():
    """Verify executive summary uses profit_base_label and does not misattribute to net profit."""
    bridge = {
        "available": True,
        "cash_realization_pct": -144.0,
        "profit_base_label": "Faaliyet Kârı (EBIT)",
    }
    stm = {
        "profit_and_loss": {"Net sales": 10_000_000.0, "Operating profit": 800_000.0, "Net profit": 72_000.0},
        "balance_sheet": {"Total assets": 5_000_000.0, "Total equity incl. current result": 2_000_000.0},
        "kpis": {"receivables": 2_000_000.0, "inventory": 1_000_000.0, "payables": 500_000.0, "cash": 200_000.0},
    }
    res = build_executive_summary(70.0, "Dengeli", [], [], {}, {}, {}, {}, {}, management_actions=[], cash_bridge=bridge, statements=stm)
    narrative = res["text"]
    assert "Faaliyet Kârı (EBIT) nakde dönüşmüyor" in narrative
    assert "Net kâr nakde dönüşmüyor (dönüşüm: %-144" not in narrative


def test_tax_strategy_caveats_and_current_tax():
    """Verify tax strategy engine has SMMM/YMM caveats and current_tax_expense."""
    stm = {
        "profit_and_loss": {"Net sales": 10_000_000.0, "Finance costs": 500_000.0, "Tax expense": 18_000.0},
        "balance_sheet": {
            "Total assets": 10_000_000.0,
            "Current assets": 7_000_000.0,
            "Total equity incl. current result": 3_000_000.0,
            "Current liabilities": 5_000_000.0,
            "Non-current liabilities": 2_000_000.0,
        },
        "kpis": {"financial_debt": 4_000_000.0, "receivables": 2_500_000.0},
    }
    data_hub = {
        "analysis_ar": {
            "overdue": 600_000.0,
            "top_overdue_parties": [{"name": "Debtor A", "amount": 600_000.0, "avg_days_overdue": 90.0}],
        }
    }
    res = build_tax_strategy_analysis(stm, data_hub=data_hub)
    assert res["status"] == "PASS"
    assert res["current_tax_expense"] == 18_000.0
    assert "disclaimer" in res
    assert "SMMM" in res["disclaimer"] or "YMM" in res["disclaimer"]
    s2 = next(s for s in res["strategies"] if s["code"] == "TAX-002")
    assert "legal_note" in s2
    assert "dava veya icra safhasına" in s2["legal_note"]


def test_product_profitability_margin_tolerance():
    """Verify product with margin close to company average is not labeled as profit-eroding."""
    sales_analysis = {
        "net_sales": 10_000_000.0,
        "gross_margin": 0.324,
        "product_profitability": [
            {"name": "Ürün A", "sales": 4_000_000.0, "cogs": 2_400_000.0, "gross_profit": 1_600_000.0, "gross_margin_pct": 40.0},
            {"name": "Ürün B", "sales": 3_500_000.0, "cogs": 2_450_000.0, "gross_profit": 1_050_000.0, "gross_margin_pct": 30.0},
            {"name": "Ürün C", "sales": 2_500_000.0, "cogs": 1_690_000.0, "gross_profit": 810_000.0, "gross_margin_pct": 32.4},
        ],
    }
    res = build_product_profitability_analysis(sales_analysis)
    p_c = next(p for p in res["products"] if p["name"] == "Ürün C")
    assert p_c["category"] == "Lokomotif Kârlı"
    assert "Kârı Aşağı Çeken" not in p_c["category"]


def test_frontend_template_contract():
    """Verify frontend_template.py has correct bindings and no problematic fallbacks."""
    tpl_path = os.path.join(os.path.dirname(__file__), "..", "frontend_template.py")
    with open(tpl_path, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. CFO Report Modal binds cb to cash_bridge_engine
    assert "const cb = bp.cash_bridge_engine || {};" in code

    # 2. CFO Report Modal binds cf13 to thirteen_week_projection
    assert "cfe.thirteen_week_projection || bp.cash_flow_13w" in code

    # 3. CFO Report Modal does not fall back to 45 days on 0 stressed runway
    assert "stress.runway_days_stressed || 45" not in code

    # 4. No internal consulting marketing language in report methodology
    assert "satılabilir danışmanlık standardında" not in code

    # 5. Electronic signature wording is professional
    assert "Sistem Raporu · İmza ve Mütalaa Bekliyor" in code
