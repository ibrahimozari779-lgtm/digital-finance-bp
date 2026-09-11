from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import pandas as pd
from finance_engine.data_classifier import classify_dataframe
from finance_engine.sales_intelligence_engine import analyze_sales
from finance_engine.receivables_payables_engine import analyze_ar, analyze_ap
from finance_engine.inventory_intelligence_engine import analyze_inventory

def test_classification_and_sales():
    df=pd.DataFrame({'Invoice':['1','2'],'Customer':['A','B'],'Product':['X','Y'],'Date':['01.01.2026','02.01.2026'],'Net Sales':['1.000,00','2.000,00']})
    role,conf,m=classify_dataframe(df,'sales.xlsx')
    assert role=='sales' and conf>0.9
    r=analyze_sales(df,m)
    assert r['net_sales']==3000
    assert r['customer_count']==2

def test_ar_ap_inventory():
    ardf=pd.DataFrame({'Customer':['A','B'],'Invoice':['1','2'],'Due Date':['01.01.2026','01.08.2026'],'Outstanding':['1.000,00','2.000,00']})
    role,_,m=classify_dataframe(ardf,'ar.xlsx'); assert role=='ar_aging'
    ar=analyze_ar(ardf,m,net_sales=10000,period_days=365); assert ar['outstanding']==3000
    apdf=pd.DataFrame({'Vendor':['V1'],'Invoice':['3'],'Due Date':['01.01.2026'],'Outstanding':['1.500,00']})
    role,_,m2=classify_dataframe(apdf,'ap.xlsx'); assert role=='ap_aging'
    ap=analyze_ap(apdf,m2,cogs=10000,period_days=365); assert ap['outstanding']==1500
    invdf=pd.DataFrame({'SKU':['X','Y'],'Quantity':['10','5'],'Unit Cost':['100,00','200,00']})
    role,_,m3=classify_dataframe(invdf,'inventory.xlsx'); assert role=='inventory'
    inv=analyze_inventory(invdf,m3,cogs=10000,period_days=365); assert inv['value']==2000


def test_detailed_sales_headers_are_detected():
    df=pd.DataFrame({
        'Müşteri Adı':['A','B'],
        'Fatura Tarihi':['01.01.2026','02.01.2026'],
        'Fatura No':['1','2'],
        'Ürün Adı':['X','Y'],
        'Net Satış Tutarı':['1.000,00','2.000,00'],
    })
    role,conf,m=classify_dataframe(df,'Controller Satis Verileri.xlsx')
    assert role=='sales' and conf>=0.9
    assert 'net_sales' in m and 'customer' in m
