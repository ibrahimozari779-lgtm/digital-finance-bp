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

    # 1. Sürdürülebilir Kâr vs. Tek Seferlik Gelir Ayrımı (64 / 67 Hesaplar)
    non_core_income = other
    non_core_share_of_profit = round((other / max(1.0, abs(pbt))) * 100, 1) if pbt > 0 else 0.0
    sustainable_operating_profit = round(op, 2)
    is_non_core_dominated = bool(other > 0 and (non_core_share_of_profit > 30.0 or (op > 0 and other > op * 0.4)))
    non_core_warning = None
    if is_non_core_dominated:
        non_core_warning = (
            f"⚠️ Kârınızın %{non_core_share_of_profit:.0f}'i ana işinizden gelmiyor; "
            f"tek seferlik/faaliyet dışı gelirler (₺{other:,.0f}) arındırıldığında operasyonel kârlılık risk altındadır."
        ).replace(",", ".")

    # 2. Fiktif Stok Kârı İllüzyonu Filtresi (Enflasyonist Stok İkame Maliyeti)
    bs = statements.get('balance_sheet') or {}
    inventories = float(bs.get('Inventories') or 0.0)
    dio = float(k.get('dio') or 60.0)
    cogs = float(pl.get('Cost of sales') or pl.get('COGS') or 0.0)
    inflation_rate = 0.45  # Yıllık enflasyon varsayımı / stok yenileme farkı
    fictitious_stock_profit = 0.0
    real_operating_profit = op
    fictitious_stock_pct = 0.0
    stock_illusion_warning = None

    if inventories > 0 and cogs > 0 and op > 0:
        replacement_drag = round(inventories * (inflation_rate * (min(180.0, max(15.0, dio)) / 365.0)), 2)
        fictitious_stock_profit = round(min(op, max(0.0, replacement_drag)), 2)
        real_operating_profit = round(op - fictitious_stock_profit, 2)
        fictitious_stock_pct = round((fictitious_stock_profit / op * 100), 1)
        if fictitious_stock_pct >= 20.0:
            stock_illusion_warning = (
                f"📦 Fiktif Stok Kârı İllüzyonu: Yüksek enflasyon ortamında kâğıt üzerinde görünen kârın "
                f"₺{fictitious_stock_profit:,.0f}'lik kısmı satılan malı aynı fiyattan depoya yerine koymaya "
                f"(stok ikame maliyetine) gidecektir. Şirketin Reel Operasyonel Kârı ₺{real_operating_profit:,.0f} seviyesindedir."
            ).replace(",", ".")

    # A single, additive quality score (0-100, higher = better quality)
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
    if fictitious_stock_pct > 20:
        quality_points -= min(20.0, (fictitious_stock_pct - 20) * 0.4)
    quality_score = round(max(0.0, min(100.0, quality_points)), 1)
    quality_label = 'Yüksek' if quality_score >= 75 else 'Orta' if quality_score >= 50 else 'Düşük'
    qoe_grade = 'A (Çok Güçlü)' if quality_score >= 80 else 'B (Yeterli)' if quality_score >= 65 else 'C (Kırılgan)' if quality_score >= 50 else 'D (Yüksek Risk)'

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
        'qoe_grade': qoe_grade,
        'sustainable_operating_profit': sustainable_operating_profit,
        'non_core_income': non_core_income,
        'non_core_share_of_profit': non_core_share_of_profit,
        'is_non_core_dominated': is_non_core_dominated,
        'non_core_warning': non_core_warning,
        'fictitious_stock_profit': fictitious_stock_profit,
        'fictitious_stock_pct': fictitious_stock_pct,
        'real_operating_profit': real_operating_profit,
        'stock_illusion_warning': stock_illusion_warning,
        'flags': flags,
        'cross_references': cross_references,
        'note': 'Kâr Kalitesi Skoru (QoE), kâğıt üzerindeki kârın ne kadarının sürdürülebilir ana faaliyetlerden, ne kadarının tek seferlik veya enflasyonist stok kârından kaynaklandığını ölçer.',
    }
