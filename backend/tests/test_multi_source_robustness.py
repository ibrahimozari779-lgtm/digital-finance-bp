from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import pandas as pd
from finance_engine.multi_source_ingestion import _read_one, ingest_sources
from finance_engine.data_classifier import classify_dataframe
from finance_engine.sales_intelligence_engine import analyze_sales
from finance_engine.receivables_payables_engine import analyze_ar

def test_number_formats():
    df=pd.DataFrame({'Müşteri':['A','B'],'Vadeli Fiyat':['1.234.567,89','500.000,00'],'Peşin Fiyat':['1.000.000,00','450.000,00']})
    role,conf,m=classify_dataframe(df,'sales.xlsx')
    assert role=='sales' and conf>=0.95
    r=analyze_sales(df,m)
    assert abs(r['term_price_total']-1734567.89)<0.01

def test_ar_uses_as_of_date_not_today():
    df=pd.DataFrame({'Customer':['A'],'Due Date':['31.12.2019'],'Outstanding':['1000']})
    _,_,m=classify_dataframe(df,'ar_aging.xlsx')
    r=analyze_ar(df,m,net_sales=10000,period_days=365,as_of_date='2019-12-31')
    assert r['overdue']==0

def test_headerless_finance():
    raw=pd.DataFrame([[100,'Kasa','1.000.000'],[120,'Alıcılar','2.000.000'],[320,'Satıcılar','-500.000'],[600,'Satışlar','5.000.000'],[620,'Maliyet','-3.500.000'],[660,'Finansman','-200.000']])
    sheets={'Sheet1':raw}
    from finance_engine.multi_source_ingestion import _promote_header
    df,meta=_promote_header(raw)
    assert meta['mode']=='headerless_financial_inference'
    assert len(df)==6


def test_finance_plus_sales_data_hub_integration():
    from io import BytesIO
    from fastapi.testclient import TestClient
    from app import app
    mizan=Path(__file__).resolve().parents[2] / 'sample_three_sheet_financials.xlsx'
    sales=pd.DataFrame({'Customer':['A','B'],'Peşin Fiyat':['900,00','1.800,00'],'Vadeli Fiyat':['1000,00','2000,00'],'Satış Tarihi':['01.01.2020','02.01.2020']})
    buf=BytesIO(); sales.to_excel(buf,index=False)
    with open(mizan,'rb') as mf:
        r=TestClient(app).post('/api/data-hub/analyze',files=[('files',(mizan.name,mf,'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')),('files',('sales.xlsx',buf.getvalue(),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))])
    assert r.status_code==200
    hub=r.json()['data_hub']
    assert hub['summary']['finance_core_available'] is True
    assert hub['summary']['sales_loaded'] is True
    assert hub['errors']==[]
