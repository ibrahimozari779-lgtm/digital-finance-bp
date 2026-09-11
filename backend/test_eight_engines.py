"""Regression tests for the v1.3 Finance Business Partner engine set:
Root Cause, Business Impact, Executive Summary, Risk Ranking, Opportunity,
Cash Conversion Cycle, Trend Analysis and Benchmarking.

Run: python3 test_eight_engines.py
"""
from pathlib import Path

from app import read_workbook_all_sheets, merge_workbook_statement_sheets, aggregate_statements, quality_checks
from finance_engine import build_finance_business_partner_analysis

SOURCE = Path('../sample_three_sheet_financials.xlsx')
sheets = read_workbook_all_sheets(SOURCE.read_bytes(), SOURCE.name)
tb, sheet_meta, mode, findings, _ = merge_workbook_statement_sheets(sheets)
st = aggregate_statements(tb)
q = quality_checks(None, {}, tb, {'mode': mode, 'sheets': sheet_meta, 'reconciliation_findings': findings}, st)

# ---- Single-period run: engine version + all 8 sections present ----
bp = build_finance_business_partner_analysis(st, q, sector='Üretim / Sanayi')
assert bp['engine_version'] == '1.9'
for key in [
    'root_cause_engine', 'business_impact_engine', 'executive_summary_engine',
    'risk_ranking_engine', 'opportunity_engine', 'cash_conversion_cycle',
    'trend_analysis', 'benchmarking',
]:
    assert key in bp, f'missing section: {key}'
print('PASS: all 8 engine sections present')

# ---- Backward-compat regression (frozen from v1.2) ----
assert bp['health_score'] == 54.0, bp['health_score']
assert any(x['code'] == 'L001' and x['severity'] == 'critical' for x in bp['findings'])
assert abs(next(x for x in bp['opportunities'] if x['code'] == 'O001')['estimated_impact'] - 545474.319) < 0.1
assert abs(next(x for x in bp['opportunities'] if x['code'] == 'O002')['estimated_impact'] - 505494.686) < 0.1
print('PASS: v1.2 backward compatibility preserved')

# ---- 1. Root Cause Engine ----
rc = bp['root_cause_engine']
assert len(rc['margin_bridge']) > 0
assert rc['primary_margin_driver'] is not None
assert rc['primary_margin_driver']['label'] == 'Satışların maliyeti (COGS)'
assert any(f.get('root_cause') for f in bp['findings']), 'expected at least one finding to carry a root_cause chain'
assert rc['findings_driven'] is True, 'root cause should be findings-driven when findings_sorted is passed in'
print('PASS: Root Cause Engine (margin bridge + causal chains)')

# ---- 2. Business Impact Engine ----
bi = bp['business_impact_engine']
assert bi['total_quantifiable_risk_exposure'] > 0
assert bi['total_opportunity_value'] > 0
assert len(bi['findings_impact']) == len([f for f in bp['findings'] if f['severity'] != 'positive'])
print('PASS: Business Impact Engine (quantified exposure + opportunity value)')

# ---- 3. Executive Summary Engine ----
exec_summary = bp['executive_summary_engine']
assert isinstance(bp['executive_summary'], str) and len(bp['executive_summary']) > 20
assert len(exec_summary['key_points']) >= 3
print('PASS: Executive Summary Engine (narrative + key points)')

# ---- 4. Risk Ranking Engine ----
rr = bp['risk_ranking_engine']
assert len(rr['ranked_risks']) > 0
scores = [r['risk_score'] for r in rr['ranked_risks']]
assert scores == sorted(scores, reverse=True), 'ranked_risks must be sorted by risk_score desc'
assert all(r['risk_tier'] in {'Kritik', 'Yüksek', 'Orta', 'Düşük'} for r in rr['ranked_risks'])
print('PASS: Risk Ranking Engine (composite score, sorted, tiered)')

# ---- 5. Opportunity Engine ----
opp = bp['opportunities']
codes = {o['code'] for o in opp}
assert {'O001', 'O002', 'O003'}.issubset(codes)
impacts = [o['estimated_impact'] for o in opp]
assert impacts == sorted(impacts, reverse=True)
print('PASS: Opportunity Engine (extended opportunity set, sorted by impact)')

# ---- 6. Cash Conversion Cycle ----
ccc = bp['cash_conversion_cycle']
assert ccc['available'] is True
assert ccc['dso_days'] is not None and ccc['dpo_days'] is not None
assert ccc['cash_conversion_cycle_days'] == round(ccc['dso_days'] + ccc['dio_days'] - ccc['dpo_days'], 1)
print('PASS: Cash Conversion Cycle Engine (DSO/DIO/DPO/CCC computed)')

# ---- 7. Trend Analysis (single period -> unavailable, graceful) ----
trend_single = bp['trend_analysis']
assert trend_single['available'] is False
assert trend_single['periods_analyzed'] == 1

# ---- 7b. Trend Analysis (with a fabricated prior period) ----
prev_pl = {k: (v * 0.85 if isinstance(v, (int, float)) else v) for k, v in st['profit_and_loss'].items()}
prev_bs = {k: (v * 0.9 if isinstance(v, (int, float)) else v) for k, v in st['balance_sheet'].items()}
prev_kpis = dict(st['kpis'])
prev_statements = {'profit_and_loss': prev_pl, 'balance_sheet': prev_bs, 'kpis': prev_kpis, 'controls': {}}
bp_trend = build_finance_business_partner_analysis(
    st, q, previous_periods=[{'label': 'Önceki Dönem', 'statements': prev_statements}]
)
trend = bp_trend['trend_analysis']
assert trend['available'] is True
assert trend['periods_analyzed'] == 2
assert trend['metric_trends']['net_sales']['period_over_period_change_pct'][0] is not None
print('PASS: Trend Analysis Engine (unavailable on single period, works with prior periods)')

# ---- 8. Benchmarking ----
bm = bp['benchmarking']
assert bm['sector'] == 'Üretim / Sanayi'
assert bm['overall_score'] is not None
assert len(bm['metrics']) > 0
bm_default = build_finance_business_partner_analysis(st, q)['benchmarking']
assert bm_default['sector'] == 'Genel'
print('PASS: Benchmarking Engine (sector selection + default fallback)')

print()
print('ALL 8 ENGINES PASS')

# ---- Regression tests for issues found reviewing real-world PDF output ----

# 1. Business Impact Engine: de-duplicated total must be <= raw total, and
#    strictly less when the same driver (e.g. financial_debt) backs 2+ findings.
assert bi['total_quantifiable_risk_exposure_unique'] <= bi['total_quantifiable_risk_exposure']
driver_counts = {}
for x in bi['findings_impact']:
    if x['driver_key']:
        driver_counts[x['driver_key']] = driver_counts.get(x['driver_key'], 0) + 1
if any(c >= 2 for c in driver_counts.values()):
    assert bi['total_quantifiable_risk_exposure_unique'] < bi['total_quantifiable_risk_exposure'], \
        'expected de-duplication to reduce the total when a driver repeats'
    assert bi['overlap_amount'] > 0
print('PASS: Business Impact Engine de-duplicates overlapping exposure drivers')

# 2. Risk Ranking: impact bonus must not saturate at the same value for very
#    different exposure/net_sales ratios (regression for the old hard-cap bug).
import finance_engine.risk_ranking_engine as rr_mod
net_sales_probe = 100.0
findings_probe = [
    {"code": "X1", "title": "t1", "category": "c", "severity": "critical", "confidence": "high", "recommendation": "r"},
    {"code": "X2", "title": "t2", "category": "c", "severity": "critical", "confidence": "high", "recommendation": "r"},
]
bi_probe_low = {"findings_impact": [{"code": "X1", "estimated_exposure": 100.0}, {"code": "X2", "estimated_exposure": 100.0}]}  # 100% of sales
bi_probe_high = {"findings_impact": [{"code": "X1", "estimated_exposure": 500.0}, {"code": "X2", "estimated_exposure": 500.0}]}  # 500% of sales
statements_probe = {"profit_and_loss": {"Net sales": net_sales_probe}}
rank_low = rr_mod.build_risk_ranking(findings_probe, bi_probe_low, statements_probe)
rank_high = rr_mod.build_risk_ranking(findings_probe, bi_probe_high, statements_probe)
score_low = rank_low['ranked_risks'][0]['risk_score']
score_high = rank_high['ranked_risks'][0]['risk_score']
assert score_high > score_low, f'expected a 500%-of-sales exposure to score higher than a 100%-of-sales one, got {score_high} <= {score_low}'
print(f'PASS: Risk Ranking no longer saturates ({score_low} at 100% ratio vs {score_high} at 500% ratio)')

# 3. Benchmarking: a "lower is better" metric (debt/equity) that is far above
#    its band must be scored/labeled as unfavorable, not favorable, and every
#    metric row must carry a machine-readable favorability tag distinct from
#    the raw band position text.
de_metric = next(m for m in bm['metrics'] if m['metric'] == 'debt_to_equity')
assert de_metric['favorability'] == 'olumsuz', de_metric
assert de_metric['score'] is not None and de_metric['score'] < 35
roe_metric = next(m for m in bm['metrics'] if m['metric'] == 'return_on_equity_pct')
assert roe_metric['position'] == de_metric['position'] == 'Bandın üzerinde', 'raw position text should be direction-agnostic'
assert roe_metric['favorability'] != de_metric['favorability'], 'favorability must differ for a higher-is-better vs lower-is-better metric both above their band'
print('PASS: Benchmarking favorability is direction-aware and decoupled from raw band position text')

# 4. Master Decision Hub (Faz 1): Management Actions must be ordered by the
#    same Priority Score as Risk Ranking, not by an independently computed
#    severity label - this is the concrete, testable proof that Action is
#    now downstream of Priority Score rather than a parallel, disconnected
#    engine.
ma = bp['management_actions']
priority_by_code_from_risk = {
    code: r['risk_score']
    for r in rr['ranked_risks']
    for code in r['contributing_codes']
}
ma_scores = [a['priority_score'] for a in ma if a.get('finding_id') in priority_by_code_from_risk]
assert ma_scores == sorted(ma_scores, reverse=True), 'management_actions must be ordered by Priority Score (Risk Ranking risk_score)'
for a in ma:
    fid = a.get('finding_id')
    if fid in priority_by_code_from_risk:
        assert abs(a['priority_score'] - priority_by_code_from_risk[fid]) < 1e-6, \
            f"action {a['action_id']} priority_score should equal its Risk Ranking risk_score"
print('PASS: Master Decision Hub — Management Actions follow the Priority Score from Risk Ranking')

# 5. CFO Narrative Engine (revised Sprint 2): the driver-bullet + projection
#    logic must be category-general, not hardcoded to one scenario. Prove it
#    fires correctly for two DIFFERENT categories using synthetic trend data.
from finance_engine.executive_summary_engine import _quantified_driver_facts, _forward_looking_projection

karlilik_trend = {"available": True, "metric_trends": {
    "net_margin_pct": {"label": "Net Marj %", "series": [6.0, 4.0, 2.0]},
    "gross_margin_pct": {"label": "Brüt Marj %", "series": [22.0, 20.0, 19.0], "period_over_period_change_pp": [None, -2.0, -1.0]},
}}
karlilik_facts = _quantified_driver_facts("Kârlılık", karlilik_trend)
assert any(f["metric"] == "gross_margin_pct" for f in karlilik_facts)
karlilik_proj = _forward_looking_projection("Kârlılık", karlilik_trend)
assert karlilik_proj is not None and karlilik_proj["metric"] == "net_margin_pct" and karlilik_proj["periods_projected"] >= 1

borcluluk_trend = {"available": True, "metric_trends": {
    "debt_to_equity": {"label": "Borç/Özkaynak", "series": [2.0, 3.0, 3.8]},
    "financial_debt": {"label": "Finansal Borç", "series": [1000000, 1300000, 1600000], "period_over_period_change_pct": [None, 30.0, 23.1]},
}}
borcluluk_facts = _quantified_driver_facts("Borçluluk", borcluluk_trend)
assert any(f["metric"] == "financial_debt" for f in borcluluk_facts)
borcluluk_proj = _forward_looking_projection("Borçluluk", borcluluk_trend)
assert borcluluk_proj is not None and borcluluk_proj["metric"] == "debt_to_equity"

# A metric that has already crossed its critical threshold must NOT get a
# forward "N periods until" projection - it's already there, projecting
# forward would be nonsensical, not merely imprecise.
already_crossed = {"available": True, "metric_trends": {
    "net_margin_pct": {"label": "Net Marj %", "series": [6.0, 3.0, 1.0, -1.0]},
}}
assert _forward_looking_projection("Kârlılık", already_crossed) is None
print('PASS: CFO Narrative Engine — driver bullets + projection generalize across categories, not one hardcoded scenario')

# 6. narrative_story: the explicit KPI -> Neden -> Etki -> Risk -> Aksiyon
#    structure must be populated end-to-end for the top finding, and its
#    TL-quantified driver figures must use the real formula (days x daily
#    sales / cogs, or margin points x net sales) - not scripted text.
story = exec_summary['narrative_story']
assert story is not None
assert story['finding_code'] is not None
assert story['risk'] is not None and story['risk']['risk_tier'] in {'Kritik', 'Yüksek', 'Orta', 'Düşük'}
assert story['financial_impact'] is None or story['financial_impact']['currency'] == 'TRY'

dso_trend = {"available": True, "metric_trends": {
    "dso_days": {"label": "Alacak Tahsilat Süresi / DSO (gün)", "series": [58.0, 70.0, 82.0], "period_over_period_change_abs": [None, 12.0, 12.0]},
}}
dso_statements = {"profit_and_loss": {"Net sales": 188_500_000, "COGS": 150_000_000}}
dso_facts = _quantified_driver_facts("İşletme Sermayesi", dso_trend, dso_statements)
assert dso_facts and abs(dso_facts[0]['tl_impact'] - round(12.0 * 188_500_000 / 365.0, 2)) < 0.01, \
    'DSO TL impact must equal days_changed x daily net sales'
print('PASS: CFO Narrative Engine — narrative_story (KPI/Neden/Etki/Risk/Aksiyon) populated with real TL-quantified drivers')

