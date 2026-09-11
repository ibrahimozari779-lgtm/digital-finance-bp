from pathlib import Path
from app import read_workbook_all_sheets, detect_special_layout, build_special_trial_balance, aggregate_statements, quality_checks

SOURCE = Path('/mnt/data/ÖRNEK MİZAN(2).xlsx')
EXPECTED = {
    '600': -54655059.91,
    '610': 107628.01,
    '621': 43394674.67,
    '622': 249166.89,
    '631': 570409.03,
    '632': 2415292.01,
    '642': -495285.46,
    '646': -48310.46,
    '660': 5054946.86,
    '679': -402.82,
    '689': 451967.08,
    '691': 641661.35,
    '690': -2903102.36,
    '692': -2261441.01,
}

sheets = read_workbook_all_sheets(SOURCE.read_bytes(), SOURCE.name)
raw = sheets[next(iter(sheets))]
det = detect_special_layout(raw)
assert det == (1, 2, 4, 8), det

tb, meta = build_special_trial_balance(raw, det)
assert meta['amount_column'] == 'Column 5'

for code, expected in EXPECTED.items():
    row = tb[tb.account_code == code]
    assert not row.empty, code
    actual = float(row.iloc[0].balance)
    assert abs(actual - expected) < 0.01, (code, actual, expected)

st = aggregate_statements(tb)
pl = st['profit_and_loss']
bs = st['balance_sheet']
assert abs(pl['Net sales'] - 54547431.90) < 0.01, pl['Net sales']
assert abs(pl['Gross profit'] - 10903590.34) < 0.01, pl['Gross profit']
assert abs(pl['Operating expenses'] - 2985701.04) < 0.01, pl['Operating expenses']
assert abs(pl['Finance costs'] - 5054946.86) < 0.01, pl['Finance costs']
assert abs(pl['Pre-tax profit'] - 2903102.36) < 0.01, pl['Pre-tax profit']
assert abs(pl['Tax expense'] - 641661.35) < 0.01, pl['Tax expense']
assert abs(pl['Net profit'] - 2261441.01) < 0.01, pl['Net profit']
assert abs(bs['Balance check difference']) < 0.01, bs['Balance check difference']
q=quality_checks(raw, {}, tb, meta, st)
assert 0 <= q['score'] <= 100
assert any(x['name']=='Source reconciliation findings' and x['value']==1 and x['status']=='warning' for x in q['checks'])
assert abs(next(x['value'] for x in q['checks'] if x['name']=='Source reconciliation difference (absolute total)')-45658.27) < 0.01
assert meta['code_column']=='Column 2' and meta['name_column']=='Column 3' and meta['amount_column']=='Column 5'
print('PASS')
print('Mode:', meta['mode'])
print('Net Sales:', pl['Net sales'])
print('Gross Profit:', pl['Gross profit'])
print('Operating Profit:', pl['Gross profit'] - pl['Operating expenses'])
print('Pre-tax Profit:', pl['Pre-tax profit'])
print('Net Profit:', pl['Net profit'])
print('Balance Difference:', bs['Balance check difference'])
