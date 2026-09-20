from __future__ import annotations
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from finance_engine.cash_flow_engine import build_cash_flow_engine
from finance_engine.decision_engine import build_finance_business_partner_analysis


def _sample_statements():
    return {
        "kpis": {
            "cash": 42000.0,
            "receivables": 1850000.0,
            "inventory": 1400000.0,
            "payables": 800000.0,
            "financial_debt": 2050000.0,
            "financial_expense": 240000.0,
        },
        "profit_and_loss": {
            "Net sales": 10800000.0,
            "COGS": 7500000.0,
            "Gross profit": 3300000.0,
            "Operating expenses": 2500000.0,
            "Operating profit": 800000.0,
            "Finance costs": 240000.0,
            "Pre-tax profit": 560000.0,
            "Tax expense": 120000.0,
            "Net profit": 440000.0,
        },
        "balance_sheet": {
            "Current assets": 3800000.0,
            "Non-current assets": 2200000.0,
            "Total assets": 6000000.0,
            "Current liabilities": 2500000.0,
            "Long-term liabilities": 1500000.0,
            "Total liabilities": 4000000.0,
            "Total equity incl. current result": 2000000.0,
        },
        "cash_conversion_cycle": {
            "dso_days": 85.0,
            "dpo_days": 38.0,
            "dio_days": 68.0,
            "ccc_days": 115.0,
        },
    }


def _prior_statements():
    s = _sample_statements()
    s["kpis"]["cash"] = 80000.0
    s["kpis"]["receivables"] = 1400000.0
    s["kpis"]["inventory"] = 1100000.0
    s["kpis"]["payables"] = 700000.0
    s["kpis"]["financial_debt"] = 1800000.0
    s["balance_sheet"]["Non-current assets"] = 2100000.0
    return s


def test_cash_flow_engine_single_period_generates_all_components():
    statements = _sample_statements()
    out = build_cash_flow_engine(statements)

    assert out["available"] is True
    assert "tms7_statement" in out
    assert "thirteen_week_projection" in out
    assert "patron_cockpit" in out

    # TMS 7 structure
    tms7 = out["tms7_statement"]
    assert "operating_activities" in tms7
    assert "investing_activities" in tms7
    assert "financing_activities" in tms7
    assert "summary" in tms7

    # 13-week projection structure
    proj = out["thirteen_week_projection"]
    weeks = proj["weeks"]
    assert len(weeks) == 13
    assert weeks[0]["week"] == 1
    assert weeks[-1]["week"] == 13
    for w in weeks:
        assert "beginning_cash" in w
        assert "inflows" in w
        assert "outflows" in w
        assert "net_cash_flow" in w
        assert "ending_cash" in w
        assert w["status"] in ("HEALTHY", "WARNING", "DEFICIT")

    summary = proj["summary"]
    assert summary["opening_cash"] == 42000.0
    assert summary["runway_weeks"] is not None

    # Patron cockpit
    cockpit = out["patron_cockpit"]
    assert "where_is_the_money" in cockpit
    assert "anomalies" in cockpit
    assert "actions" in cockpit
    assert len(cockpit["actions"]) == 3
    for act in cockpit["actions"]:
        assert "task" in act
        assert "owner" in act
        assert "deadline" in act
        assert "kpi" in act
        assert "cash_impact_tl" in act
        assert "whatsapp_template" in act
        assert "Sayın" in act["whatsapp_template"] or "Ekibine" in act["whatsapp_template"]


def test_cash_flow_engine_two_period_reconciles_tms7():
    curr = _sample_statements()
    prior = _prior_statements()
    out = build_cash_flow_engine(curr, previous_statement=prior)

    tms7 = out["tms7_statement"]
    assert tms7["is_two_period"] is True
    summary = tms7["summary"]
    assert summary["opening_cash"] == 80000.0
    assert summary["closing_cash"] == 42000.0


def test_cash_flow_engine_deficit_detection():
    # Low cash with huge burn produces deficit weeks
    statements = _sample_statements()
    statements["kpis"]["cash"] = 5000.0  # almost zero cash
    out = build_cash_flow_engine(statements)

    cockpit = out["patron_cockpit"]
    assert cockpit["lowest_cash_point"] < 50000.0
    # There should be an anomaly flagged for deficit or low buffer
    codes = [a["code"] for a in cockpit["anomalies"]]
    assert any(c in ("ALM-NAKIT-ACIGI", "ALM-DUSUK-TAMPON") for c in codes)


def test_decision_engine_integration_includes_cash_flow_engine():
    statements = _sample_statements()
    quality = {"score": 100, "status": "Trusted", "checks": []}
    analysis = build_finance_business_partner_analysis(statements, quality)
    assert "cash_flow_engine" in analysis
    cfe = analysis["cash_flow_engine"]
    assert cfe["available"] is True
    assert "patron_cockpit" in cfe
    assert "thirteen_week_projection" in cfe
    assert "tms7_statement" in cfe


@pytest.mark.anyio
async def test_cash_flow_engine_zero_discrepancy_with_data_hub_demo():
    from app import _SAMPLE_FILES, _PROJECT_ROOT, _analyze_data_hub_raw, DATA_HUB_SAMPLE_KEYS

    raw_files = []
    for k in DATA_HUB_SAMPLE_KEYS:
        fn = _SAMPLE_FILES[k][0]
        fpath = os.path.join(_PROJECT_ROOT, fn)
        with open(fpath, "rb") as f:
            raw_files.append((fn, f.read()))

    res = await _analyze_data_hub_raw(raw_files, sector="Genel")
    bp = res.get("business_partner", {})

    cb = bp.get("cash_bridge_engine", {})
    ra = bp.get("resource_allocation_engine", {})
    ma = bp.get("management_actions", [])
    cfe = bp.get("cash_flow_engine", {})

    assert cfe.get("available") is True

    # 1. TMS 7 vs Cash Bridge reconciliation (exact match)
    tms7_op = cfe["tms7_statement"]["operating_activities"]
    assert tms7_op["net_operating_cash_flow"] == cb["operating_cash_flow_proxy"]
    assert tms7_op["receivables_change"] == cb["working_capital_components"]["receivables_effect"]
    assert tms7_op["inventory_change"] == cb["working_capital_components"]["inventory_effect"]
    assert tms7_op["payables_change"] == cb["working_capital_components"]["payables_effect"]
    assert cfe["tms7_statement"]["summary"]["reconciliation_difference"] == 0.0

    # 2. "Para Nerede?" vs Resource Allocation reconciliation
    where = cfe["patron_cockpit"]["where_is_the_money"]
    ra_money = ra["where_is_money"]
    assert where["headline"] == ra_money["summary_narrative"]
    assert where["cash_amount"] == ra_money["free_cash"]
    assert where["receivables_amount"] == ra_money["breakdown"][0]["amount"]

    # 3. Actions vs Management Actions (action specificity)
    cockpit_actions = cfe["patron_cockpit"]["actions"]
    assert len(cockpit_actions) > 0
    # The top cockpit action matches the top prioritized management action
    assert cockpit_actions[0]["id"] == ma[0]["action_id"]
    assert cockpit_actions[0]["owner"] == ma[0]["owner"]
    assert cockpit_actions[0]["task"] == ma[0]["action"]
    assert "whatsapp_template" in cockpit_actions[0]
    assert cockpit_actions[0]["whatsapp_template"] != ""

