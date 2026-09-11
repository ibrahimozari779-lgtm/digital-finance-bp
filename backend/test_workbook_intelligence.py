from pathlib import Path
from app import read_workbook_all_sheets, merge_workbook_statement_sheets, aggregate_statements

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'sample_three_sheet_financials.xlsx'
sheets = read_workbook_all_sheets(SOURCE.read_bytes(), SOURCE.name)
tb, meta, mode, findings, _ = merge_workbook_statement_sheets(sheets)
assert mode == 'multi_sheet'
assert [x['role'] for x in meta] == ['assets','liabilities_equity','profit_and_loss']
assert len(meta) == 3
assert tb.account_code.nunique() >= 200
st = aggregate_statements(tb)
pl=st['profit_and_loss']; bs=st['balance_sheet']; k=st['kpis']
assert abs(pl['Net sales'] - 54547431.90) < 0.01
assert abs(pl['Gross profit'] - 10903590.34) < 0.01
assert abs(pl['Operating profit'] - 7917889.30) < 0.01
assert abs(pl['Pre-tax profit'] - 2903102.36) < 0.01
assert abs(pl['Net profit'] - 2261441.01) < 0.01
assert abs(bs['Total assets'] - 68568773.62) < 0.01
assert abs(bs['Current liabilities'] - 59322957.91) < 0.01
assert abs(bs['Total equity incl. current result'] - 9245815.71) < 0.01
assert abs(bs['Balance check difference']) < 0.01
assert abs(k['financial_debt'] - 57506100.21) < 0.01
assert abs(k['net_debt'] - 25931418.80) < 0.01
assert abs(k['debt_to_equity'] - 6.2196892101) < 0.0001
print('PASS: multi-sheet workbook intelligence')
