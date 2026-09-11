import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import _process_workbook
from finance_engine import build_finance_business_partner_analysis

SAMPLE=Path(__file__).resolve().parents[2]/'sample_three_sheet_financials.xlsx'

def get():
    r=_process_workbook(SAMPLE.read_bytes(),'Bilanco_31.12.2019.xlsx')
    bp=build_finance_business_partner_analysis(r['statements'],r['quality'])
    return r,bp

def test_core_regression():
    r,bp=get(); p=r['statements']['profit_and_loss']; b=r['statements']['balance_sheet']; k=r['statements']['kpis']
    assert round(p['Net sales'],2)==54547431.90
    assert round(p['Gross profit'],2)==10903590.34
    assert round(p['Operating profit'],2)==7917889.30
    assert round(p['Pre-tax profit'],2)==2903102.36
    assert round(p['Net profit'],2)==2261441.01
    assert round(b['Total assets'],2)==68568773.62
    assert round(b['Balance check difference'],2)==0
    assert round(k['financial_debt'],2)==57506100.21
    assert round(k['net_debt'],2)==25931418.80

def test_audit_and_data_quality():
    r,bp=get()
    assert bp['calculation_audit']['status']=='PASS'
    assert r['quality']['advanced']['score']>=90

def test_new_engines():
    _,bp=get()
    assert len(bp['scenario_engine']['scenarios'])>=5
    assert bp['profit_quality_engine']['finance_cost_to_operating_profit_pct']>60
    assert len(bp['management_actions'])>=3
    assert bp['cash_bridge_engine']['available'] is False

def test_two_period_cash_bridge():
    r1,_=get()
    r2,_=get()
    bp=build_finance_business_partner_analysis(r2['statements'],r2['quality'],previous_periods=[{'label':'prior','statements':r1['statements']}])
    assert bp['cash_bridge_engine']['available'] is True
