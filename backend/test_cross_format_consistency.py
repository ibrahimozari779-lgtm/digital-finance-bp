from pathlib import Path
from app import read_workbook_all_sheets, merge_workbook_statement_sheets, aggregate_statements

SINGLE = Path('/mnt/data/ÖRNEK MİZAN.xlsx')
MULTI = Path('/mnt/data/Bilanço ve Gelir Tablosu 31.12.2019 . (1) (2) (1).xlsx')
EXPECTED = {
    'net_sales': 54547431.90,
    'gross_profit': 10903590.34,
    'operating_profit': 7917889.30,
    'pre_tax_profit': 2903102.36,
    'net_profit': 2261441.01,
    'total_assets': 68568773.62,
    'current_liabilities': 59322957.91,
    'equity': 9245815.71,
    'financial_debt': 57506100.21,
    'net_debt': 25931418.80,
}

def run(path):
    sheets = read_workbook_all_sheets(path.read_bytes(), path.name)
    tb, meta, mode, findings, _ = merge_workbook_statement_sheets(sheets)
    st = aggregate_statements(tb)
    return st, tb, meta, findings, mode

st1,tb1,meta1,find1,mode1=run(SINGLE)
st2,tb2,meta2,find2,mode2=run(MULTI)

for label, st in [('single',st1),('multi',st2)]:
    pl=st['profit_and_loss']; bs=st['balance_sheet']; k=st['kpis']
    actual={
        'net_sales':pl['Net sales'], 'gross_profit':pl['Gross profit'], 'operating_profit':pl['Operating profit'],
        'pre_tax_profit':pl['Pre-tax profit'], 'net_profit':pl['Net profit'], 'total_assets':bs['Total assets'],
        'current_liabilities':bs['Current liabilities'], 'equity':bs['Total equity incl. current result'],
        'financial_debt':k['financial_debt'], 'net_debt':k['net_debt']}
    for k1,v in EXPECTED.items():
        assert abs(actual[k1]-v) < 0.01, (label,k1,actual[k1],v)
    assert abs(bs['Balance check difference'])<0.01

pl1=st1['profit_and_loss']; pl2=st2['profit_and_loss']
bs1=st1['balance_sheet']; bs2=st2['balance_sheet']; k1=st1['kpis']; k2=st2['kpis']
for key in ['Net sales','Gross profit','Operating profit','Pre-tax profit','Net profit','COGS','Operating expenses','Finance costs']:
    assert abs(pl1[key]-pl2[key])<0.01,(key,pl1[key],pl2[key])
for key in ['Total assets','Current liabilities','Total equity incl. current result','Balance check difference']:
    assert abs(bs1[key]-bs2[key])<0.01,(key,bs1[key],bs2[key])
for key in ['financial_debt','net_debt','debt_to_equity']:
    assert abs(k1[key]-k2[key])<0.0001,(key,k1[key],k2[key])

# The single-sheet source contains one explicit reconciliation finding; the 3-sheet
# source does not carry that supporting reconciliation column. Both still reconcile financially.
assert len(find1)==1
assert len(find2)==0
print('PASS: single-sheet and 3-sheet formats produce identical canonical financial results')
