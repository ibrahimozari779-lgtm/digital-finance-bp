"""Tests for edge cases audited: negative equity (TTK 376) and operating loss with finance costs."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pytest
from finance_engine.decision_engine import build_finance_business_partner_analysis
from finance_engine.dupont_engine import build_dupont_analysis


def test_negative_equity_decision_engine():
    statements = {
        'profit_and_loss': {
            'Operating profit': 500000.0,
            'Operating margin': 10.0,
            'Net profit': 100000.0,
            'Finance costs': 50000.0,
        },
        'balance_sheet': {
            'Total equity incl. current result': -200000.0,
            'Financial debt': 1000000.0,
            'Current ratio': 1.2,
            'Cash ratio': 0.3,
        },
        'kpis': {
            'debt_to_equity': -5.0,
            'finance_cost_to_operating_profit': 0.10,
            'operating_margin_pct': 10.0,
            'net_margin_pct': 2.0,
            'asset_turnover': 1.0,
            'equity_ratio': -0.2,
            'current_ratio': 1.2,
            'cash_ratio': 0.3,
        }
    }
    res = build_finance_business_partner_analysis(statements, {'score': 95, 'status': 'PASS'})
    findings = {f['code']: f for f in res['findings']}
    assert 'L002' in findings
    assert findings['L002']['severity'] == 'critical'
    assert 'Negatif Özkaynak' in findings['L002']['title']
    assert 'TTK 376' in findings['L002']['title']


def test_operating_loss_with_finance_costs():
    statements = {
        'profit_and_loss': {
            'Operating profit': -300000.0,
            'Operating margin': -6.0,
            'Net profit': -450000.0,
            'Finance costs': 150000.0,
        },
        'balance_sheet': {
            'Total equity incl. current result': 500000.0,
            'Financial debt': 400000.0,
            'Current ratio': 0.9,
            'Cash ratio': 0.1,
        },
        'kpis': {
            'debt_to_equity': 0.8,
            'finance_cost_to_operating_profit': -0.5,
            'operating_margin_pct': -6.0,
            'net_margin_pct': -9.0,
            'asset_turnover': 0.8,
            'equity_ratio': 0.3,
            'current_ratio': 0.9,
            'cash_ratio': 0.1,
        }
    }
    res = build_finance_business_partner_analysis(statements, {'score': 95, 'status': 'PASS'})
    findings = {f['code']: f for f in res['findings']}
    assert 'L001' in findings
    assert findings['L001']['severity'] == 'critical'
    assert 'Faaliyet zararı' in findings['L001']['title']


def test_dupont_negative_equity():
    statements = {
        'profit_and_loss': {
            'Net sales': 1000000.0,
            'Operating profit': 100000.0,
            'Pre-tax profit': 80000.0,
            'Net profit': 60000.0,
        },
        'balance_sheet': {
            'Total assets': 2000000.0,
            'Total equity incl. current result': -100000.0,
        }
    }
    dupont = build_dupont_analysis(statements)
    diag_str = ' '.join(dupont['diagnosis'])
    assert 'Negatif özkaynak' in diag_str
    assert 'Muhafazakar sermaye' not in diag_str
