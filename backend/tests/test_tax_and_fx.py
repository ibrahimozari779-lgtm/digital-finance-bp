from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pytest
from finance_engine.fx_rates_provider import resolve_fx_rates
from finance_engine.tax_strategy_engine import build_tax_strategy_analysis


def test_tcmb_fx_rates_resolution():
    # 2024 Year-End
    fx24 = resolve_fx_rates('2024-12-31')
    assert fx24['effective_date'] == '31.12.2024'
    assert fx24['rates']['EUR'] == 36.7215
    assert fx24['rates']['USD'] == 35.2803
    assert 'TCMB' in fx24['source']
    assert '31.12.2024' in fx24['badge_text']
    assert fx24['multipliers']['EUR'] == pytest.approx(1.0 / 36.7215)

    # 2025 Year-End
    fx25 = resolve_fx_rates('2025-12-31')
    assert fx25['effective_date'] == '31.12.2025'
    assert fx25['rates']['EUR'] == 38.1250
    assert fx25['rates']['USD'] == 36.4520

    # Fiscal year fallback
    fxfy = resolve_fx_rates(fiscal_year=2023)
    assert fxfy['effective_date'] == '31.12.2023'
    assert fxfy['rates']['USD'] == 29.4382

    # Default fallback
    fxdef = resolve_fx_rates(None)
    assert 'effective_date' in fxdef
    assert fxdef['rates']['TRY'] == 1.0


def test_tax_strategy_tailored_calculations():
    statements = {
        'profit_and_loss': {
            'Net sales': 10_000_000.0,
            'Finance costs': 500_000.0,
            'Pre-tax profit': 1_200_000.0,
        },
        'balance_sheet': {
            'Total assets': 10_000_000.0,
            'Current assets': 7_000_000.0,
            'Total equity incl. current result': 3_000_000.0,
            'Current liabilities': 5_000_000.0,
            'Non-current liabilities': 2_000_000.0,
        },
        'kpis': {
            'financial_debt': 4_000_000.0,
            'receivables': 2_500_000.0,
        }
    }
    data_hub = {
        'analysis_ar': {
            'overdue': 600_000.0,
            'top_overdue_parties': [
                {'name': 'Test Debtor A', 'amount': 400_000.0, 'avg_days_overdue': 120.0},
                {'name': 'Test Debtor B', 'amount': 200_000.0, 'avg_days_overdue': 75.0},
            ]
        }
    }
    result = build_tax_strategy_analysis(statements, data_hub, corporate_tax_rate=0.25)
    assert result['status'] == 'PASS'
    assert result['total_estimated_tax_saving'] > 0
    assert len(result['strategies']) >= 5

    # Check TAX-001 (Finansman Gider Kısıtlaması)
    s1 = next(s for s in result['strategies'] if s['code'] == 'TAX-001')
    assert 'KVK Md. 11/1-i' in s1['legal_basis']
    assert len(s1['calculation_steps']) == 6
    # Total Liab = 7M, Equity = 3M, excess = 4M, excess ratio = 4/7 = 57.14%
    # finance costs = 500k -> KKEG = 500k * (4/7) * 0.10 = 28,571.43 TL
    # tax penalty = 28,571.43 * 0.25 = 7,142.86 TL
    assert s1['potential_saving'] == pytest.approx(7142.86, rel=1e-2)

    # Check TAX-002 (Şüpheli Alacak Karşılığı with real parties)
    s2 = next(s for s in result['strategies'] if s['code'] == 'TAX-002')
    assert 'VUK Md. 323' in s2['legal_basis']
    assert s2['potential_saving'] == 600_000.0 * 0.25  # 150,000 TL
    assert 'Test Debtor A' in s2['current_state']
    assert len(s2['delinquent_debtors']) == 2

    # Check TAX-003 (Hızlandırılmış Amortisman)
    s3 = next(s for s in result['strategies'] if s['code'] == 'TAX-003')
    assert 'VUK Md. 315' in s3['legal_basis']
    # Fixed assets = 10M - 7M = 3M
    # Additional depr = 3M * 20% = 600k
    # saving = 600k * 0.25 = 150k
    assert s3['potential_saving'] == 150_000.0
