from pathlib import Path
import pytest
import sys
sys.path.insert(0, str(Path(__file__).parents[1]))
from finance_engine.multi_source_ingestion import _read_one, ingest_sources
from finance_engine.sales_intelligence_engine import analyze_sales
from finance_engine.data_classifier import classify_dataframe

SALES = Path('/mnt/data/satış tarfin.xlsx')

def test_real_tarfin_sales_file_classifies_and_extracts():
    if not SALES.exists(): pytest.skip('Tarfin sample is not bundled in this environment')
    content = SALES.read_bytes()
    sheets = _read_one(content, SALES.name)
    df = sheets['SALES RAW DATA']
    role, conf, mapping = classify_dataframe(df, SALES.name, 'SALES RAW DATA')
    assert role == 'sales'
    assert conf >= 0.95
    assert mapping['cash_price'] == 'Peşin Fiyat'
    assert mapping['term_price'] == 'Vadeli Fiyat'
    assert mapping['paid'] == 'Ödenen Tutar'
    assert mapping['outstanding'] == 'Outstanding Balance as of 31122019'

    result = analyze_sales(df, mapping)
    assert result['rows'] == 7800
    assert abs(result['cash_price_total'] - 44716234.52) < 0.01
    assert abs(result['term_price_total'] - 54392386.49) < 0.01
    assert abs(result['term_premium'] - 9676151.97) < 0.01
    assert abs(result['term_premium_pct'] - 21.6390133782) < 1e-6
    assert result['customer_count'] == 4737
    assert len(result['product_mix']) == 7
    assert result['product_mix'][0]['name'] == 'Gübre'
    assert result['overdue_row_count'] == 27
    assert result['overdue_amount_by_status'] is not None

def test_real_tarfin_is_not_misclassified_as_ar_only():
    if not SALES.exists(): pytest.skip('Tarfin sample is not bundled in this environment')
    bundle = ingest_sources([(SALES.name, SALES.read_bytes())])
    assert bundle['errors'] == []
    assert bundle['files'][0]['roles'][0]['role'] == 'sales'
    assert bundle['files'][0]['roles'][0]['confidence'] >= 0.95
