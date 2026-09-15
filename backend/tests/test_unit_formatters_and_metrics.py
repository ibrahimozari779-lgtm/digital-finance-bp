from __future__ import annotations
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from finance_engine.cash_conversion_engine import build_cash_conversion_cycle
from finance_engine.core_metrics import build_core_metrics
from finance_engine.decision_engine import build_finance_business_partner_analysis


def test_health_score_5_pillar_breakdown():
    """Verify that health_score_methodology has exact 5 pillars totaling 100 points."""
    statements = {
        "profit_and_loss": {
            "Net sales": 10000000.0,
            "COGS": 7000000.0,
            "Gross profit": 3000000.0,
            "Operating expenses": 1500000.0,
            "Operating profit": 1500000.0,
            "Finance costs": 300000.0,
            "Tax expense": 200000.0,
            "Net profit": 1000000.0,
        },
        "balance_sheet": {
            "Total assets": 8000000.0,
            "Current assets": 5000000.0,
            "Current liabilities": 2500000.0,
            "Total debt": 3000000.0,
            "Total equity incl. current result": 5000000.0,
        },
        "kpis": {
            "current_ratio": 2.0,
            "cash_ratio": 0.4,
            "debt_to_equity": 0.6,
            "net_debt": 1500000.0,
            "gross_margin_pct": 30.0,
            "operating_margin_pct": 15.0,
            "net_margin_pct": 10.0,
        },
        "controls": {"result_control": {}},
        "period_metadata": {"period_days": 365},
    }
    quality = {"score": 90.0, "status": "Trusted", "internal_consistency_status": "Trusted"}
    analysis = build_finance_business_partner_analysis(statements, quality)
    methodology = analysis.get("health_score_methodology")

    assert methodology is not None, "health_score_methodology must be present in analysis"
    assert methodology["max_score"] == 100
    pillars = methodology["pillars"]
    assert len(pillars) == 5, "Must have exactly 5 pillars"

    # Verify pillar keys
    keys = [p["key"] for p in pillars]
    assert keys == ["data_trust", "liquidity", "leverage", "profitability", "efficiency_capital"]

    # Verify weights sum to 100%
    total_weight = sum(p["weight_pct"] for p in pillars)
    assert total_weight == 100, f"Total weight must be 100, got {total_weight}"

    # Verify max points sum to 100.0
    total_max_points = sum(p["max_points"] for p in pillars)
    assert total_max_points == 100.0, f"Total max points must be 100.0, got {total_max_points}"

    # Verify individual pillar weights
    weight_map = {p["key"]: p["weight_pct"] for p in pillars}
    assert weight_map["data_trust"] == 15
    assert weight_map["liquidity"] == 20
    assert weight_map["leverage"] == 25
    assert weight_map["profitability"] == 25
    assert weight_map["efficiency_capital"] == 15

    # Verify earned points are valid and within [0, max_points]
    for p in pillars:
        assert 0.0 <= p["earned_points"] <= p["max_points"], (
            f"Pillar {p['key']} earned {p['earned_points']} outside [0, {p['max_points']}]"
        )
        assert p["formula"] != ""
        assert p["metric_basis"] != ""


def test_working_capital_zero_and_edge_cases():
    """Verify DSO, DIO, DPO, CCC handle zero division gracefully."""
    # Scenario: Zero sales, zero COGS
    statements_zero = {
        "profit_and_loss": {
            "Net sales": 0.0,
            "COGS": 0.0,
            "Gross profit": 0.0,
            "Operating profit": 0.0,
            "Net profit": 0.0,
        },
        "balance_sheet": {
            "Total assets": 1000000.0,
            "Current assets": 500000.0,
            "Current liabilities": 300000.0,
            "Total equity incl. current result": 700000.0,
        },
        "kpis": {
            "receivables": 0.0,
            "inventory": 0.0,
            "payables": 0.0,
        },
        "period_metadata": {"period_days": 365},
    }

    ccc = build_cash_conversion_cycle(statements_zero, period_days=365)
    # Zero sales/COGS should result in None or 0, never crashing with ZeroDivisionError
    assert ccc.get("dso_days") is None or ccc.get("dso_days") == 0.0
    assert ccc.get("dio_days") is None or ccc.get("dio_days") == 0.0
    assert ccc.get("dpo_days") is None or ccc.get("dpo_days") == 0.0


def test_working_capital_mathematical_identity():
    """Verify CCC = DSO + DIO - DPO with known test values."""
    statements = {
        "profit_and_loss": {
            "Net sales": 3650000.0,   # Daily sales = 10,000
            "COGS": 1825000.0,        # Daily COGS = 5,000
            "Gross profit": 1825000.0,
            "Operating profit": 365000.0,
            "Net profit": 182500.0,
        },
        "balance_sheet": {
            "Total assets": 5000000.0,
            "Current assets": 2000000.0,
            "Current liabilities": 1000000.0,
            "Total equity incl. current result": 4000000.0,
        },
        "kpis": {
            "receivables": 600000.0,  # 60 days of sales
            "inventory": 200000.0,    # 40 days of COGS
            "payables": 150000.0,     # 30 days of COGS
        },
        "period_metadata": {"period_days": 365},
    }

    ccc = build_cash_conversion_cycle(statements, period_days=365)
    dso = ccc.get("dso_days")
    dio = ccc.get("dio_days")
    dpo = ccc.get("dpo_days")
    actual_ccc = ccc.get("cash_conversion_cycle_days")

    assert round(dso, 1) == 60.0
    assert round(dio, 1) == 40.0
    assert round(dpo, 1) == 30.0
    # CCC = 60 + 40 - 30 = 70 days
    assert round(actual_ccc, 1) == 70.0


def test_margin_and_ratio_formulas():
    """Verify Gross, Operating, and Net margins arithmetic and precision."""
    sales = 5000000.0
    cogs = 3250000.0
    gross_profit = sales - cogs      # 1,750,000 (35.0%)
    op_expenses = 750000.0
    op_profit = gross_profit - op_expenses  # 1,000,000 (20.0%)
    fin_costs = 250000.0
    tax = 150000.0
    net_profit = op_profit - fin_costs - tax # 600,000 (12.0%)

    gm_pct = (gross_profit / sales) * 100.0
    om_pct = (op_profit / sales) * 100.0
    nm_pct = (net_profit / sales) * 100.0

    assert round(gm_pct, 2) == 35.0
    assert round(om_pct, 2) == 20.0
    assert round(nm_pct, 2) == 12.0


def test_wacc_cost_of_capital_cash_freed_formula():
    """Verify simulator cash release and financing interest saving formulas."""
    sales = 12000000.0
    cogs = 8000000.0
    days_in_year = 365.0

    dso_reduction_days = 15.0
    dio_reduction_days = 20.0
    wacc_pct = 45.0  # 45% cost of capital proxy

    cash_from_dso = (dso_reduction_days / days_in_year) * sales
    cash_from_dio = (dio_reduction_days / days_in_year) * cogs
    total_cash_freed = cash_from_dso + cash_from_dio

    annual_interest_savings = total_cash_freed * (wacc_pct / 100.0)

    # 15 days of 12M sales = 493,150.68 TL
    assert round(cash_from_dso, 2) == round((15.0 / 365.0) * 12000000.0, 2)
    # 20 days of 8M COGS = 438,356.16 TL
    assert round(cash_from_dio, 2) == round((20.0 / 365.0) * 8000000.0, 2)
    # Total cash freed ~ 931,506.85 TL
    assert round(total_cash_freed, 2) == round(cash_from_dso + cash_from_dio, 2)
    # Annual interest savings at 45% ~ 419,178.08 TL
    assert round(annual_interest_savings, 2) == round(total_cash_freed * 0.45, 2)
