from __future__ import annotations

import os, sys, asyncio
import pandas as pd
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from finance_engine.gap_detection_engine import build_gap_detection, build_extended_root_cause
from finance_engine.scenario_engine import build_scenarios


def sample_statements():
    return {
        'profit_and_loss': {'Net sales': 1000.0,'COGS':800.0,'Gross profit':200.0,'Operating expenses':50.0,'Operating profit':150.0,'Finance costs':90.0,'Pre-tax profit':60.0,'Tax expense':12.0,'Net profit':48.0},
        'balance_sheet': {'Current assets':500.0,'Current liabilities':450.0,'Total assets':600.0,'Total equity incl. current result':80.0},
        'kpis': {'debt_to_equity':6.0,'financial_debt':480.0,'cash':100.0,'receivables':500.0,'inventory':0.0,'payables':50.0,'current_ratio':1.11,'net_debt':380.0,'gross_margin_pct':20.0},
        'period_metadata': {'available': True, 'period_days':365}
    }


def test_gap_detector_flags_missing_sources_and_leverage():
    d=build_gap_detection(sample_statements(), {'score':100}, {'summary':{'sales_loaded':False,'ar_aging_loaded':False,'ap_aging_loaded':False,'inventory_loaded':False},'analysis':{}})
    codes={x['code'] for x in d['gaps']}
    assert 'GAP-CAP-01' in codes
    assert 'MISS-SALES' in {x['code'] for x in d['missing_intelligence']}


def test_root_cause_keeps_data_gap_first_class():
    g=build_gap_detection(sample_statements(), {'score':100}, {'summary':{'sales_loaded':False,'ar_aging_loaded':False,'ap_aging_loaded':False,'inventory_loaded':False},'analysis':{}})
    rc=build_extended_root_cause(sample_statements(), {'causal_chains':[]}, {}, g)
    assert any(x['code']=='RC-DATA' and x['causal_status']=='data_gap' for x in rc['causal_chains'])


def test_scenario_tax_aware_and_debt_proxy_not_zero():
    sc=build_scenarios(sample_statements())
    gross=next(x for x in sc if x['scenario_id']=='S003')
    # NOTE: scenario_engine.S003 margin_pp is band-adaptive (wider gap to the
    # 30% reference band -> larger, but still modest, uplift shown). For this
    # fixture gross_margin_pct=20 -> margin_gap=10 -> band (5.0, 0.015) ->
    # uplift = sales(1000) * 0.015 = 15.0. This was a stale fixed-1pp
    # assumption from before the band-adaptive logic was introduced; the
    # underlying engine behavior is intentional (see scenario_engine.py S003
    # comment) and is NOT part of the Faz 0 trust-hardening scope.
    assert gross['gross_profit_impact']==15.0
    assert gross['pbt_impact']==15.0
    assert gross['tax_impact']>0
    assert gross['net_profit_impact']<15.0
    debt=next(x for x in sc if x['scenario_id']=='S002')
    assert debt['pbt_impact']>0
    assert debt['confidence']=='low'


def test_customer_and_product_profitability_segmentation():
    from finance_engine.customer_profitability_engine import build_customer_profitability_analysis
    from finance_engine.product_profitability_engine import build_product_profitability_analysis

    sales_data = {
        'net_sales': 100000.0,
        'gross_margin': 0.25,
        'customer_profitability': [
            {'name': 'Zarar Eden Müşteri A', 'sales': 20000.0, 'cogs': 25000.0, 'gross_profit': -5000.0, 'gross_margin_pct': -25.0},
            {'name': 'Altın Müşteri B', 'sales': 50000.0, 'cogs': 30000.0, 'gross_profit': 20000.0, 'gross_margin_pct': 40.0},
            {'name': 'Hacimli Düşük Marj C', 'sales': 30000.0, 'cogs': 27000.0, 'gross_profit': 3000.0, 'gross_margin_pct': 10.0},
        ],
        'product_profitability': [
            {'name': 'Zararlı Ürün X', 'sales': 15000.0, 'cogs': 18000.0, 'gross_profit': -3000.0, 'gross_margin_pct': -20.0},
            {'name': 'Lokomotif Ürün Y', 'sales': 60000.0, 'cogs': 35000.0, 'gross_profit': 25000.0, 'gross_margin_pct': 41.7},
        ]
    }
    ar_data = {
        'top_parties': [{'name': 'Altın Müşteri B', 'amount': 10000.0}],
        'overdue_by_party': {'Altın Müşteri B': 0.0},
        'weighted_overdue_days_by_party': {'Altın Müşteri B': 0.0}
    }

    cp = build_customer_profitability_analysis(sales_data, ar_data)
    assert cp['status'] == 'PASS'
    assert len(cp['loss_making_customers']) == 1
    assert cp['loss_making_customers'][0]['name'] == 'Zarar Eden Müşteri A'
    assert len(cp['high_quality_customers']) >= 1
    assert any(c['name'] == 'Altın Müşteri B' for c in cp['high_quality_customers'])
    assert any(f['code'] == 'CP-000' for f in cp['findings'])

    pp = build_product_profitability_analysis(sales_data)
    assert pp['status'] == 'PASS'
    assert len(pp['loss_making_products']) == 1
    assert pp['loss_making_products'][0]['name'] == 'Zararlı Ürün X'
    assert any(f['code'] == 'PP-000' for f in pp['findings'])

