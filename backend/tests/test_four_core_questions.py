from __future__ import annotations
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import _SAMPLE_FILES, _PROJECT_ROOT, _analyze_data_hub_raw, DATA_HUB_SAMPLE_KEYS

@pytest.mark.anyio
async def test_data_hub_demo_answers_all_four_business_questions():
    # 1. Verify DATA_HUB_SAMPLE_KEYS contains the 2-period mizan set + operational subledgers
    assert 'hub_mizan_prior' in DATA_HUB_SAMPLE_KEYS
    assert 'hub_mizan' in DATA_HUB_SAMPLE_KEYS
    assert 'ar_aging' in DATA_HUB_SAMPLE_KEYS
    assert 'ap_aging' in DATA_HUB_SAMPLE_KEYS
    assert 'inventory' in DATA_HUB_SAMPLE_KEYS
    assert 'sales_ledger' in DATA_HUB_SAMPLE_KEYS
    assert len(DATA_HUB_SAMPLE_KEYS) == 6

    # 2. Ingest the 6 files into _analyze_data_hub_raw
    raw_files = []
    for k in DATA_HUB_SAMPLE_KEYS:
        fn = _SAMPLE_FILES[k][0]
        fpath = os.path.join(_PROJECT_ROOT, fn)
        assert os.path.isfile(fpath), f"Sample file not found: {fpath}"
        with open(fpath, 'rb') as f:
            raw_files.append((fn, f.read()))

    res = await _analyze_data_hub_raw(raw_files, sector='Genel')
    bp = res.get('business_partner', {})

    # QUESTION 1: "Kâğıt üzerinde kâr görünüyor ama kasada para nerede?"
    # -> Cash Bridge & Cash Realization Engine
    cb = bp.get('cash_bridge_engine', {})
    assert cb.get('available') is True, "Cash bridge must be available when multi-period mizan is present"
    assert cb.get('cash_realization_pct') is not None, "Cash realization % must be computed"
    assert 'working_capital_components' in cb
    wcc = cb['working_capital_components']
    assert 'receivables_effect' in wcc
    assert 'inventory_effect' in wcc
    assert 'payables_effect' in wcc
    # In the demo dataset, net profit is positive (72k) but working capital drag (-1.95M) makes operating cash flow negative (-1.15M)
    assert cb.get('net_profit') > 0
    assert cb.get('operating_cash_flow_proxy') < 0

    # QUESTION 2: "Cirosu en yüksek müşterim bana gerçekten para kazandırıyor mu?"
    # -> 4-Quadrant Customer Profitability Matrix
    ms = res.get('data_hub', {})
    an = ms.get('analysis', {})
    cp = an.get('customer_profitability')
    assert cp is not None, "Customer profitability analysis must be present"
    assert cp.get('status') == 'PASS'
    assert 'stars' in cp
    assert 'volume_chasers' in cp
    assert 'niche_profit' in cp
    assert 'low_value' in cp

    # QUESTION 3: "Depodaki stok nakdimi ne kadar boğuyor?"
    # -> Inventory Intelligence & Aging
    inv = res.get('inventory_aging')
    assert inv is not None, "Inventory aging must be present"
    assert inv.get('dio_days') is not None
    assert inv.get('stale_180_amount') is not None
    assert inv.get('value') is not None

    # QUESTION 4: "Fiyatlarımızı %3 artırsak veya vadeyi 15 gün çeksek nakit ne olur?"
    # -> KPI and P&L baseline for Interactive What-If Simulator
    pl = res.get('statements', {}).get('profit_and_loss', {})
    kpis = res.get('statements', {}).get('kpis', {})
    assert pl.get('Net sales') is not None and pl.get('Net sales') > 0
    assert pl.get('Operating expenses') is not None
    assert kpis.get('financial_debt') is not None
