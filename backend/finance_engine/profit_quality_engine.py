from __future__ import annotations
from typing import Any


def build_profit_quality(statements: dict[str, Any], findings: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """Profit Quality Engine.

    Flags mechanical drivers of profit quality (finance-cost burden, non-core
    income dependency, operating-to-net conversion). To avoid restating the
    same underlying condition that the main Findings/Risk Ranking sections
    already report (e.g. finance-cost pressure is L001 there), any flag whose
    driver matches an existing non-positive finding is cross-referenced by
    code instead of being narrated a second time - this is what previously
    produced duplicate commentary between the Findings list and Profit
    Quality section for the same underlying ratio.
    """
    findings = findings or []
    # Only non-positive findings represent an already-reported problem; a
    # "positive" finding for the same metric means the condition being
    # checked here has NOT been raised elsewhere, so it should still surface.
    active_finding_codes = {f["code"] for f in findings if f.get("severity") != "positive"}

    pl = statements['profit_and_loss']; k = statements['kpis']
    sales = float(pl.get('Net sales') or 0)
    op = float(pl.get('Operating profit') or 0)
    fin = float(pl.get('Finance costs') or 0)
    net_profit = float(pl.get('Net profit') or 0)
    other = float(pl.get('Other income') or 0)
    pbt = float(pl.get('Pre-tax profit') or 0)

    finance_burden = (fin / op * 100) if op else None
    other_dependency = (other / pbt * 100) if pbt > 0 else None
    op_to_net_ratio = (net_profit / op) if op else None

    flags: list[dict[str, Any]] = []
    cross_references: list[dict[str, Any]] = []
    seen_titles: set[str] = set()

    def add_flag(severity: str, title: str, detail: str, related_code: str | None = None):
        # Defensive de-duplication: never emit the exact same headline twice
        # within this engine's own output, regardless of the reason it fired.
        if title in seen_titles:
            return
        seen_titles.add(title)
        if related_code and related_code in active_finding_codes:
            cross_references.append({"title": title, "detail": detail, "related_finding_code": related_code})
            return
        flags.append({'severity': severity, 'title': title, 'detail': detail, 'related_finding_code': related_code})

    if finance_burden is not None and finance_burden > 50:
        add_flag('high', 'Finansman maliyeti kâr kalitesini zayıflatıyor',
                  f'Finansman giderleri faaliyet kârının %{finance_burden:.1f} kadarına ulaşıyor.',
                  related_code='L001')
    if op > 0 and net_profit < op * 0.5:
        add_flag('medium', 'Faaliyet kârı net kâra sınırlı dönüşüyor',
                  'Finansman, diğer kalemler ve vergi etkisi belirgin.',
                  related_code=None)
    if other_dependency is not None and other_dependency > 30:
        add_flag('medium', 'Diğer gelir bağımlılığı yüksek',
                  f'Diğer gelirler vergi öncesi kârın yaklaşık %{other_dependency:.1f} kadarını oluşturuyor.',
                  related_code='E001')
    if op < 0 < net_profit:
        add_flag('high', 'Net kâr faaliyet zararına rağmen pozitif',
                  'Net kâr, faaliyet dışı/tek seferlik kalemler tarafından taşınıyor olabilir; sürdürülebilirliği düşük.',
                  related_code=None)

    # A single, additive quality score (0-100, higher = better quality) so the
    # section has one headline number instead of only a bag of flags. This is
    # new information, not a restatement of any individual flag above.
    quality_points = 100.0
    if finance_burden is not None:
        quality_points -= min(35.0, max(0.0, finance_burden - 20) * 0.5)
    if other_dependency is not None:
        quality_points -= min(25.0, max(0.0, other_dependency - 10) * 0.6)
    if op_to_net_ratio is not None and op > 0:
        shortfall = max(0.0, 1.0 - op_to_net_ratio)
        quality_points -= min(25.0, shortfall * 40)
    if op <= 0:
        quality_points -= 20.0
    quality_score = round(max(0.0, min(100.0, quality_points)), 1)
    quality_label = 'Yüksek' if quality_score >= 75 else 'Orta' if quality_score >= 50 else 'Düşük'

    return {
        'available': True,
        'gross_margin_pct': k.get('gross_margin_pct'),
        'operating_margin_pct': k.get('operating_margin_pct'),
        'net_margin_pct': k.get('net_margin_pct'),
        'finance_cost_to_operating_profit_pct': finance_burden,
        'other_income_to_pbt_pct': other_dependency,
        'operating_to_net_profit_ratio': op_to_net_ratio,
        'quality_score': quality_score,
        'quality_label': quality_label,
        'flags': flags,
        'cross_references': cross_references,
        'note': 'EBITDA yalnızca amortisman/faiz öncesi veri güvenilir biçimde ayrıştırılabildiğinde ayrıca hesaplanmalıdır. Bu bölümde, ana Bulgular listesinde zaten raporlanan bir koşulla örtüşen kalemler tekrar anlatılmaz; ilgili bulgu koduna çapraz referans verilir (bkz. cross_references).',
    }
