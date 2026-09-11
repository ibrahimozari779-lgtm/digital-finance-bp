from pathlib import Path
from app import read_workbook_all_sheets, merge_workbook_statement_sheets, aggregate_statements, quality_checks
from finance_engine import build_finance_business_partner_analysis

SOURCE = Path('../sample_three_sheet_financials.xlsx')
sheets = read_workbook_all_sheets(SOURCE.read_bytes(), SOURCE.name)
tb, sheet_meta, mode, findings, _ = merge_workbook_statement_sheets(sheets)
st = aggregate_statements(tb)
q = quality_checks(None, {}, tb, {'mode': mode, 'sheets': sheet_meta, 'reconciliation_findings': findings}, st)
bp = build_finance_business_partner_analysis(st, q)

assert bp['health_score'] == 54.0, bp['health_score']
assert any(x['code'] == 'L001' and x['severity'] == 'critical' for x in bp['findings'])
assert any(x['code'] == 'L002' and x['severity'] == 'critical' for x in bp['findings'])
assert abs(bp['derived_metrics']['finance_cost_to_operating_profit_pct'] - 63.84) < 0.1
assert abs(next(x for x in bp['opportunities'] if x['code']=='O001')['estimated_impact'] - 545474.319) < 0.1
assert abs(next(x for x in bp['opportunities'] if x['code']=='O002')['estimated_impact'] - 505494.686) < 0.1
print('PASS: Finance Business Partner decision engine')
print('Health:', bp['health_score'], bp['health_label'])
print('Top finding:', bp['findings'][0]['title'])
print('Summary:', bp['executive_summary'])
