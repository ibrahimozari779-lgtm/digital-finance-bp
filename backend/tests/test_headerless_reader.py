from pathlib import Path
import sys
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from finance_engine.multi_source_ingestion import _promote_header, ingest_sources
from finance_engine.data_classifier import classify_dataframe


def test_headerless_code_and_balance_only():
    raw = pd.DataFrame([
        [100, 100000], [120, 250000], [153, 200000], [320, -180000],
        [500, -300000], [600, -1000000], [620, 500000], [660, 25000],
    ])
    df, meta = _promote_header(raw)
    assert meta['mode'] == 'headerless_financial_inference'
    assert 'account_code' in df.columns
    assert 'balance' in df.columns
    role, conf, mapping = classify_dataframe(df, 'headerless.xlsx')
    assert role == 'finance'
    assert conf > 0.9
    assert len(df) == 8


def test_headerless_code_name_debit_credit():
    raw = pd.DataFrame([
        [100, 'Kasa', 100000, 0], [120, 'Alıcılar', 250000, 0],
        [320, 'Satıcılar', 0, 180000], [500, 'Sermaye', 0, 300000],
        [600, 'Yurtiçi Satışlar', 0, 1000000], [620, 'Satışların Maliyeti', 500000, 0],
    ])
    df, meta = _promote_header(raw)
    assert meta['mode'] == 'headerless_financial_inference'
    assert df['account_name'].iloc[0] == 'Kasa'
    assert {'debit_turnover','credit_turnover','balance'}.issubset(df.columns)


def test_real_tarfin_sales_is_not_corrupted():
    path = Path('/mnt/data/satış tarfin.xlsx')
    if not path.exists():
        return
    content = path.read_bytes()
    out = ingest_sources([('satış tarfin.xlsx', content)])
    assert not out['errors']
    sales = [s for s in out['sources'] if s['role'] == 'sales']
    assert sales, out
    assert sales[0]['rows'] > 7000
    mapping = sales[0]['mapping']
    assert mapping.get('cash_price')
    assert mapping.get('term_price')
    assert mapping.get('customer')
