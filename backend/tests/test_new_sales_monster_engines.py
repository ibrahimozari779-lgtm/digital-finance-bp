import pytest
from finance_engine.benchmarking_engine import build_benchmark_analysis
from finance_engine.inflation_adjustment_engine import build_inflation_adjustment_analysis
from finance_engine.liquidity_stress_testing_engine import build_liquidity_stress_test


def test_benchmarking_working_capital_leakage():
    statements = {
        "profit_and_loss": {"Net sales": 36500000.0, "COGS": 20000000.0},
        "kpis": {
            "receivables": 10000000.0,  # 100 days DSO (sector Genel median is 65 days -> 35 days gap)
            "inventory": 5000000.0,     # 91.25 days DIO (sector Genel median is 50 days -> 41.25 days gap)
            "payables": 2000000.0,
            "gross_margin_pct": 45.2,
            "operating_margin_pct": 12.0,
            "net_margin_pct": 8.0,
            "current_ratio": 1.5,
            "quick_ratio": 1.1,
            "debt_to_equity": 1.0,
            "asset_turnover": 1.1,
            "return_on_equity_pct": 18.0,
        },
    }
    bench = build_benchmark_analysis(statements, sector="Genel")
    leak = bench.get("working_capital_leakage")
    assert leak is not None
    assert leak["dso"]["gap_days"] > 30.0
    assert leak["annual_interest_leakage"] > 0
    assert "gizli finansman yükü" in leak["executive_summary"]


def test_inflation_adjustment_engine():
    statements = {
        "profit_and_loss": {"Net sales": 10000000.0, "COGS": 6000000.0, "Gross profit": 4000000.0, "Operating profit": 1000000.0, "Net profit": 500000.0},
        "balance_sheet": {"Total equity incl. current result": 2000000.0, "Current liabilities": 3000000.0},
        "kpis": {"inventory": 2000000.0, "cash": 500000.0, "receivables": 1500000.0},
    }
    inf = build_inflation_adjustment_analysis(statements, annual_inflation_rate=0.50)
    assert inf is not None
    assert inf["nominal_net_profit"] == 500000.0
    assert inf["phantom_inventory_profit"] > 0
    # Equity preservation threshold: 2M * 50% = 1M > 500k net profit -> capital is eroding
    assert inf["is_capital_eroding"] is True
    assert "Sermaye" in inf["executive_assessment"] or "İllüzyon" in inf["executive_assessment"]


def test_liquidity_stress_testing_engine():
    statements = {
        "profit_and_loss": {"Net sales": 12000000.0, "COGS": 7200000.0},
        "balance_sheet": {"Current liabilities": 3000000.0},
        "kpis": {"cash": 400000.0, "receivables": 3000000.0, "financial_debt": 1000000.0},
    }
    stress = build_liquidity_stress_test(statements)
    assert stress is not None
    # 35% of 3M = 1.05M shock. 60d shock = 1.05M > 400k cash -> Deficit!
    assert stress["scenario_60d"]["is_deficit"] is True
    assert stress["scenario_60d"]["net_cash_after_shock"] < 0
    assert "KRİTİK" in stress["stress_status"]
