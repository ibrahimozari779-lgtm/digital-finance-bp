from __future__ import annotations
from typing import Any

def build_data_quality_report(tb, statements: dict[str, Any], quality: dict[str, Any], period: dict[str, Any]) -> dict[str, Any]:
    checks=[]; critical=[]; warnings=[]
    unmapped=int((tb.statement_bucket=='UNMAPPED').sum()) if 'statement_bucket' in tb else 0
    duplicate_conflicts=[x for x in quality.get('reconciliation_findings',[]) if x.get('type')=='duplicate_conflict']
    bs_diff=float(statements['balance_sheet'].get('Balance check difference') or 0)
    rc=statements['controls']['result_control']
    def chk(name, ok, value=None, note=''):
        checks.append({'name':name,'status':'passed' if ok else 'failed','value':value,'note':note})
        if not ok: critical.append({'name':name,'value':value,'note':note})
    chk('Balance sheet equation', abs(bs_diff)<0.01, round(bs_diff,2))
    chk('690 / PBT reconciliation', rc.get('pre_tax_difference') is None or abs(rc['pre_tax_difference'])<0.01, rc.get('pre_tax_difference'))
    chk('691 / tax reconciliation', rc.get('tax_difference') is None or abs(rc['tax_difference'])<0.01, rc.get('tax_difference'))
    chk('692 / net profit reconciliation', rc.get('net_profit_difference') is None or abs(rc['net_profit_difference'])<0.01, rc.get('net_profit_difference'))
    if unmapped: warnings.append({'name':'Unmapped accounts','count':unmapped})
    if duplicate_conflicts: critical.append({'name':'Conflicting duplicate accounts','count':len(duplicate_conflicts)})
    if not period.get('available'): warnings.append({'name':'Period metadata unavailable','note':'Days-based metrics use explicit fallback assumptions.'})
    required={'cash':statements['kpis'].get('cash'),'receivables':statements['kpis'].get('receivables'),'inventory':statements['kpis'].get('inventory'),'payables':statements['kpis'].get('payables'),'financial_debt':statements['kpis'].get('financial_debt')}
    missing=[k for k,v in required.items() if v is None]
    if missing: warnings.append({'name':'Missing management balance','fields':missing})
    base=float(quality.get('score') or 0)
    penalty=min(40, len(critical)*15 + unmapped*0.5 + len(warnings)*2)
    score=round(max(0,min(100,base-penalty)),1)
    status='Trusted' if score>=90 else 'Review' if score>=75 else 'Caution' if score>=55 else 'Critical'
    return {'score':score,'status':status,'checks':checks,'critical_issues':critical,'warnings':warnings,'unmapped_accounts':unmapped,'period':period,
            'internal_consistency_score':score,'internal_consistency_status':status,
            'note':'Bu skor yalnızca mizan-içi tutarlılığı (bilanço eşitliği, 690/691/692 mutabakatı) ölçer. GL ile satış/AR/AP dosyaları arasındaki çapraz kaynak farkları buraya dahil değildir — ayrıca "Kaynak Mutabakatı" bölümüne bakın.'}


def apply_cross_source_reconciliation(quality_advanced: dict[str, Any], reconciliation: dict[str, Any] | None) -> dict[str, Any]:
    """FIX (customer-trust bug): a mizan-only quality score of 100/100 "Trusted"
    was being shown to the user even when GL vs Sales/AR/AP reconciliation had
    open warnings (e.g. a 262K TL revenue gap). A buyer evaluating this tool
    will not trust a headline "100/100 Trusted" badge that visibly contradicts
    unresolved reconciliation warnings elsewhere on the same page. This blends
    the two signals into one combined, honest headline score while preserving
    the original internal-consistency number for transparency.
    """
    if not reconciliation:
        return quality_advanced
    warning_count = int(reconciliation.get('warning_count') or 0)
    material_count = int(reconciliation.get('material_difference_count') or 0)
    if warning_count == 0 and material_count == 0:
        return quality_advanced
    internal_score = float(quality_advanced.get('score') or 0)
    recon_penalty = min(35, warning_count * 6 + material_count * 15)
    combined = round(max(0, internal_score - recon_penalty), 1)
    combined_status = 'Trusted' if combined>=90 else 'Review' if combined>=75 else 'Caution' if combined>=55 else 'Critical'
    out = dict(quality_advanced)
    out['score'] = combined
    out['status'] = combined_status
    out['internal_consistency_score'] = internal_score
    out['internal_consistency_status'] = quality_advanced.get('status')
    out['cross_source_warning_count'] = warning_count
    out['cross_source_material_difference_count'] = material_count
    out['note'] = (
        f"Genel Güven Skoru = mizan-içi tutarlılık ({internal_score:.0f}/100) ile "
        f"kaynaklar-arası mutabakat sonucunun birleşimidir. {warning_count} adet "
        "mutabakat uyarısı bu skoru düşürmüştür; ayrıntı için 'Kaynak Mutabakatı' bölümüne bakın."
    )
    return out
