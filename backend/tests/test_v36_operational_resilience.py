from pathlib import Path
import sys
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from finance_engine.sales_intelligence_engine import analyze_sales
from finance_engine.multi_source_intelligence import _canonicalize
from finance_engine.operational_finance_engine import build_operational_finance
from finance_engine.ai_critic import critique_ai_response


def test_sales_profitability_and_safe_mixed_dates():
    df=pd.DataFrame({'Customer':['A','B'], 'Product':['X','Y'], 'Date':['01.01.2026','not-a-date'], 'Net Sales':['100,00','200,00'], 'Cost':['40,00','150,00']})
    result=analyze_sales(df, {'customer':'Customer','product':'Product','date':'Date','net_sales':'Net Sales','cost':'Cost'})
    assert round(result['gross_margin'], 4) == 0.3667
    assert result['customer_profitability'][0]['name'] == 'A'
    assert result['monthly_series'][0]['period'] == '2026-01'


def test_multi_file_mapping_is_semantic_not_first_file_header():
    items=[
        {'df':pd.DataFrame({'Customer':['A'],'Net Sales':[10]}),'mapping':{'customer':'Customer','net_sales':'Net Sales'}},
        {'df':pd.DataFrame({'Müşteri':['B'],'Net Satış':[20]}),'mapping':{'customer':'Müşteri','net_sales':'Net Satış'}},
    ]
    frame,mapping=_canonicalize(items)
    assert mapping['customer']=='__customer'
    assert list(frame['__customer']) == ['A','B']
    assert list(frame['__net_sales']) == [10,20]


def test_operational_finance_and_ai_critic_are_evidence_aware():
    hub={'analysis':{'ar_aging':{'overdue':40},'inventory':{'stale_180_amount':30},'sales':{},'ap_aging':{}}}
    operational=build_operational_finance(hub,{})
    assert operational['cash_release_proxy']==70
    critic=critique_ai_response({'message':'Observed 40 TL and 999 TL'}, {'overdue':40})
    assert critic['status']=='review_required'




