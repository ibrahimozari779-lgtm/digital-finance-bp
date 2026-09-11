from pathlib import Path
import sys
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import _process_workbook


def test_headerless_financial_workbook_end_to_end(tmp_path):
    raw = pd.DataFrame([
        [100, 100000], [120, 250000], [153, 200000], [320, -180000],
        [500, -300000], [600, -1000000], [610, 20000], [620, 500000], [660, 25000],
    ])
    path = tmp_path / 'headerless.xlsx'
    raw.to_excel(path, index=False, header=False)
    r = _process_workbook(path.read_bytes(), path.name)
    assert not r['tb'].empty
    assert r['tb']['account_code'].nunique() == 9
    assert r['meta']['sheets'][0]['mode'] == 'headerless_financial_inference'
    assert r['statements']['profit_and_loss']['Net sales'] > 0
