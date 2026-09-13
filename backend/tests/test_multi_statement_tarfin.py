import os
from pathlib import Path
import sys
import pytest
import pandas as pd
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import app, is_special_financial_statement_layout, classify_sheet, safe_extract_texts

def test_safe_extract_texts():
    df = pd.DataFrame({
        'Date': ['2019-01-01 10:00:00', None],
        'Text': ['Tarfin Tarım A.Ş.', None],
        'Amount': [15000.5, 25000.0]
    })
    text = safe_extract_texts(df, max_rows=5)
    assert 'tarfin tarim' in text
    assert '15000' in text

def test_classify_sheet_statements():
    df_empty = pd.DataFrame()
    assert classify_sheet('BALANCE SHEET - ASSETS', df_empty) == 'assets'
    assert classify_sheet('BS ASSET', df_empty) == 'assets'
    assert classify_sheet('Aktif Bilanço', df_empty) == 'assets'
    
    assert classify_sheet('BALANCE SHEET - LIABILITIES', df_empty) == 'liabilities_equity'
    assert classify_sheet('BS LIAB', df_empty) == 'liabilities_equity'
    assert classify_sheet('Pasif Bilanço', df_empty) == 'liabilities_equity'
    
    assert classify_sheet('INCOME STATEMENT', df_empty) == 'profit_and_loss'
    assert classify_sheet('PL', df_empty) == 'profit_and_loss'
    assert classify_sheet('P&L', df_empty) == 'profit_and_loss'
    assert classify_sheet('Gelir Tablosu', df_empty) == 'profit_and_loss'

    # Operational subledgers must be recognized and not treated as trial balance
    assert classify_sheet('SALES RAW DATA', df_empty) == 'sales'
    assert classify_sheet('SALES_PIVOT', df_empty) == 'sales'
    assert classify_sheet('profit analyze', df_empty) == 'sales'
    assert classify_sheet('Q1', df_empty) == 'notes_or_other'
    assert classify_sheet('Kontrol Notları', df_empty) == 'notes_or_other'

def test_is_special_financial_statement_layout_with_sheet_name():
    df = pd.DataFrame([[None, None, 100, 'Kasa', None, 5000]])
    assert is_special_financial_statement_layout(df, 'BS ASSET') is True
    assert is_special_financial_statement_layout(df, 'BS LIAB') is True
    assert is_special_financial_statement_layout(df, 'PL') is True

def test_tarfin_real_file_end_to_end():
    tarfin_path = '/Users/ibrahimozari/Documents/Tarfin_Q1_Q2.xlsx'
    if not os.path.exists(tarfin_path):
        pytest.skip('Tarfin_Q1_Q2.xlsx not present on disk')
    
    with open(tarfin_path, 'rb') as f:
        content = f.read()

    client = TestClient(app)
    
    # 1. Pre-flight inspect
    resp_inspect = client.post('/api/inspect', files={'files': ('Tarfin_Q1_Q2.xlsx', content, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')})
    assert resp_inspect.status_code == 200
    d_inspect = resp_inspect.json()
    assert d_inspect['detected_erp'] == 'multi_statement'
    assert 'Çoklu Finansal Tablo' in d_inspect['erp_badge']
    assert d_inspect['role'] == 'finance'
    assert len(d_inspect['files'][0]['sheets']) == 9

    # 2. Full 33 decision engines analysis
    resp_analyze = client.post('/api/mizan/analyze', files={'file': ('Tarfin_Q1_Q2.xlsx', content, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')})
    assert resp_analyze.status_code == 200
    d_analyze = resp_analyze.json()
    assert d_analyze['source']['mode'] == 'multi_statement_financial_workbook'
    assert d_analyze['account_count'] >= 150
    assert d_analyze['business_partner']['health_score'] > 0
    assert d_analyze['statements']['profit_and_loss']['Gross profit'] > 0
    assert d_analyze['statements']['balance_sheet']['Total assets'] > 0
