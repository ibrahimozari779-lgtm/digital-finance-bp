from __future__ import annotations

from typing import Any

from .opportunity_engine import build_opportunities
from .root_cause_engine import build_root_cause_analysis
from .business_impact_engine import build_business_impact
from .risk_ranking_engine import build_risk_ranking
from .cash_conversion_engine import build_cash_conversion_cycle
from .trend_engine import build_trend_analysis
from .benchmarking_engine import build_benchmark_analysis
from .executive_summary_engine import build_executive_summary
from .cash_bridge_engine import build_cash_bridge
from .cash_flow_engine import build_cash_flow_engine
from .profit_quality_engine import build_profit_quality
from .action_engine import build_management_actions
from .validation_engine import build_calculation_audit
from .scenario_engine import build_scenarios
from .gap_detection_engine import build_gap_detection, build_extended_root_cause
from .operational_finance_engine import build_operational_finance
from .finding_registry import build_finding_registry
from .strategy_playbook import build_strategy_playbook
from .narrative_engine import build_narrative_engine
from .dupont_engine import build_dupont_analysis
from .profit_improvement_engine import build_profit_improvement_analysis
from .resource_allocation_engine import build_resource_allocation_analysis
from .core_metrics import build_core_metrics


def _safe_div(a: float | None, b: float | None) -> float | None:
    if a is None or b in (None, 0):
        return None
    return float(a) / float(b)


def _clamp(v: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, v))


def _score_band(value: float | None, bands: list[tuple[float, float]], default: float = 0.0) -> float:
    if value is None:
        return default
    for threshold, score in bands:
        if value >= threshold:
            return score
    return default


def _severity_rank(severity: str) -> int:
    return {"critical": 4, "high": 3, "medium": 2, "low": 1, "positive": 0}.get(severity, 0)


def build_finance_business_partner_analysis(
    statements: dict[str, Any],
    quality: dict[str, Any],
    sector: str | None = None,
    previous_periods: list[dict[str, Any]] | None = None,
    data_hub: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Deterministic first-generation Finance Business Partner decision engine.

    This engine does not ask an LLM to invent financial facts. It derives evidence,
    risks, opportunities and impact estimates from the canonical financial model.
    Thresholds are general-purpose financial guardrails, not industry benchmarks.
    """
    pl = statements["profit_and_loss"]
    bs = statements["balance_sheet"]
    k = statements["kpis"]

    net_sales = float(pl.get("Net sales") or 0.0)
    gross_profit = float(pl.get("Gross profit") or 0.0)
    operating_profit = float(pl.get("Operating profit") or 0.0)
    net_profit = float(pl.get("Net profit") or 0.0)
    finance_costs = float(pl.get("Finance costs") or 0.0)
    other_operating_income = float(pl.get("Other operating income") or 0.0)
    other_non_operating_income = float(pl.get("Other non-operating income") or 0.0)
    total_assets = float(bs.get("Total assets") or 0.0)
    current_assets = float(bs.get("Current assets") or 0.0)
    current_liabilities = float(bs.get("Current liabilities") or 0.0)
    total_equity = float(bs.get("Total equity incl. current result") or 0.0)

    financial_debt = float(k.get("financial_debt") or 0.0)
    net_debt = float(k.get("net_debt") or 0.0)
    cash = float(k.get("cash") or 0.0)
    receivables = float(k.get("receivables") or 0.0)
    inventory = float(k.get("inventory") or 0.0)
    payables = float(k.get("payables") or 0.0)
    dso = k.get("dso")
    dio = k.get("dio")
    dpo = k.get("dpo")

    gross_margin = k.get("gross_margin_pct")
    operating_margin = k.get("operating_margin_pct")
    net_margin = k.get("net_margin_pct")
    current_ratio = k.get("current_ratio")
    quick_ratio = k.get("quick_ratio")
    cash_ratio = k.get("cash_ratio")
    debt_to_equity = k.get("debt_to_equity")
    roa = k.get("return_on_assets_pct")
    roe = k.get("return_on_equity_pct")
    asset_turnover = k.get("asset_turnover")

    raw_opex = pl.get("Operating expenses")
    opex_abs = abs(float(raw_opex)) if raw_opex is not None else max(0.0, gross_profit - operating_profit)
    opex_to_sales = _safe_div(opex_abs, net_sales) if opex_abs > 0 else None
    inventory_to_current_assets = _safe_div(inventory, current_assets) if inventory > 0 else None

    finance_cost_to_op = _safe_div(finance_costs, operating_profit)
    interest_coverage_proxy = _safe_div(operating_profit, finance_costs)
    debt_to_assets = _safe_div(financial_debt, total_assets)
    equity_ratio = _safe_div(total_equity, total_assets)
    cash_to_debt = _safe_div(cash, financial_debt)
    receivables_to_sales = _safe_div(receivables, net_sales)
    non_core_income = other_operating_income + other_non_operating_income
    non_core_income_to_pbt = _safe_div(non_core_income, float(pl.get("Pre-tax profit") or 0.0))

    # ----- Health score -----
    data_score = float(quality.get("score") or 0.0)
    data_component = _clamp(data_score) * 0.15

    liquidity_points = 0.0
    if current_ratio is not None:
        liquidity_points += _score_band(current_ratio, [(1.50, 10), (1.20, 8), (1.00, 6), (0.80, 3)], 0)
    if cash_ratio is not None:
        liquidity_points += _score_band(cash_ratio, [(0.50, 10), (0.30, 8), (0.15, 5), (0.05, 2)], 0)

    leverage_points = 0.0
    if total_equity is not None and total_equity <= 0:
        # Technical insolvency / negative equity: no positive leverage points
        leverage_points += 0.0
    elif debt_to_equity is not None and debt_to_equity >= 0:
        if debt_to_equity <= 1.0: leverage_points += 12
        elif debt_to_equity <= 2.0: leverage_points += 9
        elif debt_to_equity <= 3.0: leverage_points += 6
        elif debt_to_equity <= 5.0: leverage_points += 3

    if operating_profit is not None and operating_profit <= 0 and finance_costs is not None and finance_costs > 0:
        # Operating loss with finance costs: no leverage points
        pass
    elif finance_cost_to_op is not None and finance_cost_to_op >= 0:
        if finance_cost_to_op <= 0.20: leverage_points += 13
        elif finance_cost_to_op <= 0.35: leverage_points += 10
        elif finance_cost_to_op <= 0.50: leverage_points += 6
        elif finance_cost_to_op <= 0.75: leverage_points += 3

    profitability_points = 0.0
    if operating_margin is not None:
        profitability_points += _score_band(operating_margin, [(15, 13), (10, 10), (5, 6), (0, 3)], 0)
    if net_margin is not None:
        profitability_points += _score_band(net_margin, [(10, 12), (5, 9), (2, 5), (0, 2)], 0)

    efficiency_points = 0.0
    if asset_turnover is not None:
        efficiency_points += _score_band(asset_turnover, [(1.5, 8), (1.0, 6), (0.7, 4), (0.4, 2)], 0)
    if equity_ratio is not None:
        efficiency_points += _score_band(equity_ratio, [(0.40, 7), (0.30, 5), (0.20, 3), (0.10, 1)], 0)

    health_score = round(_clamp(data_component + liquidity_points + leverage_points + profitability_points + efficiency_points), 1)
    health_label = "Güçlü" if health_score >= 80 else "Dengeli" if health_score >= 65 else "Dikkat Gerektiriyor" if health_score >= 50 else "Yüksek Risk"

    findings: list[dict[str, Any]] = []

    def _tr_cur(v: float | None) -> str:
        if v is None: return "0 TL"
        return f"{v:,.0f}".replace(",", ".") + " TL"

    def _tr_pct(v: float | None, decimals: int = 1) -> str:
        if v is None: return "%0"
        fmt = f"%.{decimals}f" % v
        return "%" + fmt.replace(".", ",")

    def _tr_ratio(v: float | None, decimals: int = 2) -> str:
        if v is None: return "0x"
        fmt = f"%.{decimals}f" % v
        return fmt.replace(".", ",") + "x"

    def add_finding(code: str, category: str, severity: str, title: str, evidence: list[str], interpretation: str, recommendation: str, confidence: str = "high"):
        findings.append({
            "code": code,
            "category": category,
            "severity": severity,
            "title": title,
            "evidence": [e for e in evidence if e],
            "interpretation": interpretation,
            "recommendation": recommendation,
            "confidence": confidence,
        })

    # Profitability
    if operating_margin is not None:
        if operating_margin >= 12:
            add_finding("P001", "Kârlılık", "positive", "Faaliyet kârlılığı güçlü", [f"Faaliyet kâr marjı {_tr_pct(operating_margin)}", f"Faaliyet kârı {_tr_cur(operating_profit)}"], "Ana faaliyetler güçlü bir kâr marjı üretiyor; şirket operasyonel olarak değer yaratıyor.", "Faaliyet marjını korurken bu kârın alacak/stokta kilitlenmeden kasaya dönüşmesine odaklan.")
        elif operating_margin < 5:
            add_finding("P002", "Kârlılık", "high", "Faaliyet marjı zayıf", [f"Faaliyet kâr marjı {_tr_pct(operating_margin)}"], "Satışlar faaliyet seviyesinde çok sınırlı kâra dönüşüyor; maliyet veya gider artışına karşı hata payı kalmamış.", "Brüt marj, fiyatlama, iskonto disiplini ve faaliyet giderlerini (760/770) ayrıştırarak kârsız ürün/müşterileri ayıkla.")
        else:
            add_finding("P005", "Kârlılık", "positive", "Faaliyet marjı dengeli ancak koruma gerektiriyor", [f"Faaliyet kâr marjı {_tr_pct(operating_margin)}", f"Faaliyet kârı {_tr_cur(operating_profit)}"], "Şirket esas faaliyetlerinden pozitif kâr üretiyor ancak marj tamponu orta seviyede; faiz veya maliyet şoklarına karşı disiplin şart.", "Maliyet artışlarını satış fiyatlarına gecikmesiz yansıt ve sabit gider artışını ciro büyümesinin altında tut.")

    if gross_margin is not None and gross_margin < 15:
        add_finding("P003", "Kârlılık", "medium", "Brüt marj sınırlı", [f"Brüt marj {_tr_pct(gross_margin)}"], "Satış maliyeti veya fiyatlama baskısı, genel yönetim ve pazarlama giderlerini karşılamak için dar bir tampon bırakıyor.", "Müşteri/ürün bazında iskonto tavanı belirle ve hammadde/tedarik maliyetlerini yeniden müzakere et.")

    if gross_margin is not None and gross_margin >= 18 and opex_to_sales is not None and opex_to_sales > 0.16 and (operating_margin is None or operating_margin < 10):
        opex_sev = "high" if opex_to_sales > 0.22 else "medium"
        add_finding(
            "P004", "Kârlılık", opex_sev,
            "Brüt kâr faaliyet giderlerinde (OPEX) eriyor",
            [f"Brüt marj {_tr_pct(gross_margin)}", f"Faaliyet gideri / Satış {_tr_pct(opex_to_sales * 100)}", f"Faaliyet gideri {_tr_cur(opex_abs)}"],
            "Üretim/ticaret brüt marjı sağlıklı olmasına rağmen pazarlama ve genel yönetim giderleri (760/770) kazanılan kârın önemli kısmını tüketiyor.",
            "760 ve 770 hesap kırılımlarında ciro üretmeyen sabit giderleri denetle; departman bazlı sıfır tabanlı bütçe disiplinine geç.",
        )

    # Financing pressure
    if operating_profit is not None and operating_profit <= 0 and finance_costs is not None and finance_costs > 0:
        add_finding(
            "L001", "Borçluluk", "critical",
            "Faaliyet zararı & finansman gider yükü",
            [f"Faaliyet zararı {_tr_cur(operating_profit)}", f"Finansman gideri {_tr_cur(finance_costs)}"],
            "Şirket ana faaliyetlerinden kâr üretemezken üstüne faiz yükü taşıyor; borç servisi doğrudan özkaynak ve kasayı eritiyor.",
            "Kısa vadeli pahalı kredileri yapılandır ve nakit tüketen zararlı operasyonları derhal durdur.",
        )
    elif finance_cost_to_op is not None and finance_cost_to_op >= 0:
        pct = finance_cost_to_op * 100
        if finance_cost_to_op > 0.60:
            sev = "critical"
        elif finance_cost_to_op > 0.40:
            sev = "high"
        elif finance_cost_to_op > 0.25:
            sev = "medium"
        else:
            sev = "positive"
        add_finding(
            "L001", "Borçluluk", sev,
            "Finansman gider baskısı" if sev != "positive" else "Finansman gider yükü kontrollü",
            [f"Finansman gideri / Faaliyet kârı {_tr_pct(pct)}", f"Finansman gideri {_tr_cur(finance_costs)}", f"Faaliyet kârı {_tr_cur(operating_profit)}"],
            "Operasyonda kazanılan faaliyet kârının büyük bölümü bankalara ve finansman maliyetine gidiyor." if sev != "positive" else "Faaliyet kârının büyük kısmı finansman giderlerinden sonra şirket içinde korunuyor.",
            "Rotatif/spot kredileri kapat veya vadesini uzat; alacak tahsilatını hızlandırarak kredi kullanım ihtiyacını düşür." if sev != "positive" else "Mevcut finansman disiplinini koru.",
        )

    if total_equity is not None and total_equity <= 0:
        add_finding(
            "L002", "Borçluluk", "critical",
            "Negatif Özkaynak / Borca Batıklık Riski (TTK 376)",
            [f"Özkaynak {_tr_cur(total_equity)}", f"Finansal borç {_tr_cur(financial_debt)}" if financial_debt is not None else ""],
            "Şirket özkaynakları negatife düşmüştür; borç/özkaynak oranı matematiksel olarak tanımsızdır ve TTK 376 kapsamında teknik iflas / borca batıklık riski bulunmaktadır.",
            "TTK 376 kapsamında genel kurul çağrısı, sermaye tamamlama, ortak alacaklarının sermayeye ilavesi veya nakdi sermaye artırımı önlemleri acilen alınmalıdır.",
        )
    elif debt_to_equity is not None and debt_to_equity >= 0:
        if debt_to_equity > 5:
            sev = "critical"
        elif debt_to_equity > 3:
            sev = "high"
        elif debt_to_equity > 2:
            sev = "medium"
        else:
            sev = "positive"
        add_finding(
            "L002", "Borçluluk", sev,
            "Finansal kaldıraç yüksek" if sev != "positive" else "Finansal kaldıraç makul",
            [f"Finansal borç / Özkaynak {_tr_ratio(debt_to_equity)}", f"Finansal borç {_tr_cur(financial_debt)}", f"Özkaynak {_tr_cur(total_equity)}"],
            "Borç seviyesi özkaynak tabanına göre yüksek; faiz artışlarına ve banka limit daralmalarına karşı kırılganlık artıyor." if sev != "positive" else "Borç/özkaynak dengesi güvenli eşiklerde ve yönetilebilir seviyede.",
            "Kısa vadeli borç azaltımı, kârın şirkette bırakılması ve KVK 10/1-ı vergi kalkanlı nakdi sermaye güçlendirme seçeneklerini değerlendir." if sev != "positive" else "Borçluluk seviyesini yeni yatırımlarda disiplinli izle.",
        )

    if financial_debt > 0 and cash > 0 and cash_to_debt is not None and cash_to_debt >= 0.35 and finance_cost_to_op is not None and finance_cost_to_op > 0.25:
        add_finding(
            "L003", "Borçluluk", "medium",
            "Kasada nakit tutulurken yüksek faizli kredi taşınıyor",
            [f"Kasa & Banka {_tr_cur(cash)}", f"Finansal borç {_tr_cur(financial_debt)}", f"Finansman gideri {_tr_cur(finance_costs)}"],
            "Şirket bir yandan önemli miktarda hazır değer taşırken diğer yandan yüksek finansman gideri ödüyor; negatif faiz taşıma maliyeti (negative carry) oluşuyor.",
            "13 haftalık zorunlu likidite tamponu dışındaki atıl nakitle en pahalı rotatif/TKM kredi dilimlerini erken kapat.",
        )

    # Liquidity
    if current_ratio is not None:
        if current_ratio < 1.0:
            add_finding("Q001", "Likidite", "critical", "Kısa vadeli likidite açığı", [f"Cari oran {_tr_ratio(current_ratio)}"], "Dönen varlıklar (kasa, alacak, stok) 1 yıl içinde ödenecek kısa vadeli borçları karşılamaya yetmiyor.", "13 haftalık nakit akış planı kur, vadesi geçmiş alacakları hızla tahsil et ve kısa vadeli banka borçlarını uzun vadeye yay.")
        elif current_ratio < 1.2:
            add_finding("Q002", "Likidite", "medium", "Likidite tamponu sınırlı", [f"Cari oran {_tr_ratio(current_ratio)}", f"Nakit oranı {_tr_ratio(cash_ratio)}" if cash_ratio is not None else ""], "Kısa vadeli yükümlülükler kağıt üzerinde karşılanabiliyor ancak tahsilat gecikmesine karşı hata payı düşük.", "Nakit tamponunu güçlendir ve haftalık tahsilat/ödeme takvimini stres senaryolarıyla yönet.")
        elif current_ratio >= 1.5:
            add_finding("Q004", "Likidite", "positive", "Kısa vadeli likidite tamponu güçlü", [f"Cari oran {_tr_ratio(current_ratio)}", f"Nakit oranı {_tr_ratio(cash_ratio)}" if cash_ratio is not None else ""], "Dönen varlıklar kısa vadeli yükümlülükleri güvenli bir marjla karşılıyor; kısa vadeli ödeme sıkışıklığı riski düşük.", "Fazla likiditenin atıl alacak/stokta değil, yüksek getirili veya borç azaltıcı alanlarda değerlendirildiğinden emin ol.")

    # Cash vs debt
    if cash_to_debt is not None and cash_to_debt < 0.5:
        add_finding("Q003", "Likidite", "high", "Nakit finansal borcu sınırlı karşılıyor", [f"Kasa / Finansal borç {_tr_pct(cash_to_debt*100)}", f"Net borç {_tr_cur(net_debt)}"], "Mevcut hazır değerler finansal borcun yarısından azını karşılıyor; borç çevrimi operasyonel nakit üretimine bağımlı.", "Serbest nakit yaratımı ve kredi anapara azaltım takvimini birlikte planla.")

    # Receivables concentration at statement level
    if receivables_to_sales is not None and receivables_to_sales > 0.50:
        add_finding("W001", "İşletme Sermayesi", "high", "Alacak bakiyesi satışlara göre yüksek", [f"Alacak / Net satış {_tr_pct(receivables_to_sales*100)}", f"Ticari alacaklar {_tr_cur(receivables)}"], "Satışların önemli bölümü henüz kasaya girmemiş ve müşteri vadelerinde bekliyor.", "120 Alacak yaşlandırma (AR aging) listesini çıkar, geciken müşterilere vade/teminat sınırı koy ve erken ödeme iskontosu uygula.", confidence="medium")

    # Inventory lockup at statement level
    if (dio is not None and float(dio) > 75) or (inventory_to_current_assets is not None and inventory_to_current_assets > 0.45 and inventory > 0):
        inv_sev = "high" if (dio is not None and float(dio) > 110) else "medium"
        inv_ev = [f"Stoklar {_tr_cur(inventory)}"]
        if dio is not None:
            inv_ev.insert(0, f"Stokta kalma süresi (DIO) {round(float(dio))} gün")
        if inventory_to_current_assets is not None:
            inv_ev.append(f"Stok / Dönen varlıklar {_tr_pct(inventory_to_current_assets * 100)}")
        add_finding(
            "W002", "İşletme Sermayesi", inv_sev,
            "Stok devir hızı yavaş / depoda nakit kilitli",
            inv_ev,
            "Şirketin nakdi depodaki stoklarda uzun süre bekliyor; yavaş dönen envanter işletme sermayesi ve finansman ihtiyacını büyütüyor.",
            "90 günü aşan hareketsiz (dead/slow-moving) stokları kampanya ile nakde çevir ve emniyet stok/sipariş seviyelerini düşür.",
        )

    # Negative Receivable-Payable Term Spread (Financing customers while paying suppliers early)
    if dso is not None and dpo is not None and (float(dso) - float(dpo)) > 25 and receivables > payables:
        spread_days = round(float(dso) - float(dpo))
        spread_sev = "high" if spread_days > 45 else "medium"
        add_finding(
            "W003", "İşletme Sermayesi", spread_sev,
            "Alacak-borç vade makası aleyhte (Müşteriyi finanse etme riski)",
            [f"Tahsilat süresi (DSO) {round(float(dso))} gün", f"Tedarikçi ödeme süresi (DPO) {round(float(dpo))} gün", f"Net vade açığı {spread_days} gün"],
            f"Tedarikçilere ortalama {round(float(dpo))} günde ödeme yapılırken müşterilerden {round(float(dso))} günde tahsilat yapılıyor; aradaki {spread_days} günlük boşluğu şirket kendi kasasından veya banka kredisiyle finanse ediyor.",
            "Müşteri satış vadelerini kısaltırken ana tedarikçilerle vade uzatımı veya DBS/Tedarikçi Finansmanı anlaşması yap.",
        )

    # Excessive Payable Stretch (Supplier Continuity Risk)
    if dpo is not None and float(dpo) > 95 and payables > 0:
        add_finding(
            "W005", "İşletme Sermayesi", "medium",
            "Tedarikçi ödeme vadesi (DPO) kritik eşiği aşıyor",
            [f"Tedarikçi ödeme süresi (DPO) {round(float(dpo))} gün", f"Ticari borçlar (320) {_tr_cur(payables)}"],
            "Tedarikçi ödemelerinin 95 günün üzerine çıkması peşin alım iskontolarının kaçırılmasına, fiyatların içine gizli vade farkı gömülmesine veya tedarik kesintisine yol açabilir.",
            "Kritik tedarikçilerle ödeme planını mutabık kal ve yüksek iskonto sunan tedarikçilerde erken ödeme (dinamik iskonto) fırsatlarını hesapla.",
        )

    # Earnings quality
    if non_core_income_to_pbt is not None and non_core_income_to_pbt > 0.30:
        add_finding("E001", "Kazanç Kalitesi", "medium", "Faaliyet dışı/ikincil gelirlerin kâra katkısı yüksek", [f"Faaliyet dışı gelir / VÖK {_tr_pct(non_core_income_to_pbt*100)}", f"Faaliyet dışı gelir {_tr_cur(non_core_income)}"], "Vergi öncesi kârın önemli bir bölümü ana faaliyet dışındaki tek seferlik veya ikincil gelirlerden geliyor.", "Sürdürülebilir esas faaliyet kârlılığını (QoE) tek seferlik kur/faiz/diğer gelirlerden ayırarak bütçele.")

    # Profit locked in working capital ("Kâr var ama para nerede?")
    net_wc_lock = receivables + inventory - payables
    if operating_profit > 0 and net_wc_lock > operating_profit * 1.5 and (financial_debt == 0 or cash < financial_debt * 0.30) and (receivables_to_sales is not None and receivables_to_sales > 0.30):
        add_finding(
            "E002", "Kazanç Kalitesi", "high",
            "Kağıt üzerinde kâr var ancak nakit işletme sermayesinde kilitli",
            [f"Faaliyet kârı {_tr_cur(operating_profit)}", f"Net işletme sermayesi yükü {_tr_cur(net_wc_lock)}", f"Kasa {_tr_cur(cash)}"],
            "Gelir tablosu kâr göstermesine rağmen kazanılan para kasaya girmemiş; alacak ve stok büyümesini finanse etmek için sahada kilitlenmiş durumda.",
            "Kâr dağıtımı veya yeni yatırım kararı almadan önce tahsilat ve stok eritme aksiyonlarıyla kağıt üzerindeki kârı nakde çevir.",
        )

    # Efficiency
    if asset_turnover is not None and asset_turnover < 0.6:
        add_finding("A001", "Verimlilik", "medium", "Varlık devir hızı düşük", [f"Aktif devir hızı {_tr_ratio(asset_turnover)}"], "Şirketin taşıdığı toplam varlık büyüklüğü, ürettiği ciroya göre ağır kalıyor.", "Ciro üretmeyen atıl varlıkları, yavaş dönen stokları ve tahsil edilemeyen alacakları bilançodan temizle.")


    # Advanced Risk Rules V1.3

    if debt_to_assets is not None:
        if debt_to_assets > 0.70:
            add_finding("D004","Borçluluk","critical","Borç yükü kritik seviyede",
                        [f"Toplam borç / Aktif {_tr_pct(debt_to_assets*100)}"],
                        "Varlıkların önemli bölümü borç ile finanse edilmektedir.",
                        "Borç azaltımı ve sermaye güçlendirme seçenekleri değerlendirilmelidir.")
        elif debt_to_assets > 0.50:
            add_finding("D005","Borçluluk","high","Borç yoğunluğu yüksek",
                        [f"Toplam borç / Aktif {_tr_pct(debt_to_assets*100)}"],
                        "Borç seviyesi finansal esnekliği azaltabilir.",
                        "Borç yapısı yakından izlenmelidir.")

    if interest_coverage_proxy is not None:
        if interest_coverage_proxy < 1.5:
            add_finding("D006","Borçluluk","critical","Faiz karşılama seviyesi kritik",
                        [f"Faiz karşılama oranı {_tr_ratio(interest_coverage_proxy)}"],
                        "Faaliyet karı faiz yükünü taşımakta zorlanıyor.",
                        "Borç maliyetleri ve finansman yapısı gözden geçirilmelidir.")
        elif interest_coverage_proxy < 3:
            add_finding("D007","Borçluluk","high","Faiz karşılama seviyesi zayıf",
                        [f"Faiz karşılama oranı {_tr_ratio(interest_coverage_proxy)}"],
                        "Faiz giderleri karlılığı baskılıyor.",
                        "Faiz maliyetlerini azaltacak aksiyonlar değerlendirilmelidir.")

    if total_equity < 0:
        add_finding("D008","Borçluluk","critical","Negatif özkaynak",
                    [f"Özkaynak {_tr_cur(total_equity)}"],
                    "Şirket sermaye erozyonu yaşamaktadır.",
                    "Özkaynak yapısı acilen güçlendirilmelidir.")

    if receivables_to_sales is not None and debt_to_equity is not None:
        if receivables_to_sales > 0.40 and debt_to_equity > 2:
            add_finding("WC004","İşletme Sermayesi","high",
                        "İşletme sermayesi finansman baskısı",
                        [f"Alacak / Satış {_tr_pct(receivables_to_sales*100)}",
                         f"Borç / Özkaynak {_tr_ratio(debt_to_equity)}"],
                        "Yüksek alacak seviyesi kredi ihtiyacını artırıyor olabilir.",
                        "Tahsilat performansı ve müşteri vadeleri analiz edilmelidir.")

    # Priority = severity/financial impact/actionability proxy.
    findings_sorted = sorted(findings, key=lambda x: (_severity_rank(x["severity"]), len(x["evidence"])), reverse=True)

    # ----- 5. Opportunity Engine -----
    opportunities_sorted = build_opportunities(statements)

    # ----- 1. Root Cause Engine -----
    # Master Decision Hub (Faz 1): Root Cause now consumes the Findings list
    # itself instead of independently re-deriving its own threshold checks -
    # see root_cause_engine.build_root_cause_analysis docstring for why that
    # matters (threshold drift risk between two copies of "the same" rule).
    root_cause = build_root_cause_analysis(statements, findings=findings_sorted)
    gap_detection = build_gap_detection(statements, quality, data_hub) if data_hub is not None else build_gap_detection(statements, quality, None)
    root_cause = build_extended_root_cause(statements, root_cause, data_hub or {}, gap_detection)
    operational_finance = build_operational_finance(data_hub, statements)
    chain_by_finding_code: dict[str, str] = {}
    for chain in root_cause["causal_chains"]:
        for code in chain.get("related_findings", []):
            chain_by_finding_code[code] = " → ".join(chain["chain"])
    for f in findings_sorted:
        if f["code"] in chain_by_finding_code:
            f["root_cause"] = chain_by_finding_code[f["code"]]

    # ----- 2. Business Impact Engine -----
    business_impact = build_business_impact(statements, findings_sorted, opportunities_sorted)

    # ----- 4. Risk Ranking Engine -----
    risk_ranking = build_risk_ranking(findings_sorted, business_impact, statements)

    # ----- Priority Score (Master Decision Hub, Faz 1) -----
    # Risk Ranking's composite risk_score (severity x confidence x financial
    # exposure, see risk_ranking_engine.py) IS the Priority Score in the
    # Finding -> Root Cause -> Business Impact -> Priority Score -> Action
    # pipeline. Before this, Management Actions ordered its own groups by a
    # bare severity_rank computed independently of Risk Ranking, so two
    # findings tied on severity could be prioritized differently by the
    # Risk list and the Action list. This map is the one thing that carries
    # the Priority Score forward into Action Engine's own ordering.
    priority_by_code: dict[str, float] = {
        code: r["risk_score"]
        for r in risk_ranking.get("ranked_risks", [])
        for code in r.get("contributing_codes", [r.get("code")])
    }

    # ----- 6. Cash Conversion Cycle Engine -----
    period_days = None
    if isinstance(statements.get("period_metadata"), dict):
        period_days = statements["period_metadata"].get("period_days")
    ccc = build_cash_conversion_cycle(statements, period_days=period_days)

    # ----- 7. Trend Analysis Engine -----
    trend = build_trend_analysis(statements, previous_periods)

    # ----- 8. Benchmarking Engine -----
    benchmark = build_benchmark_analysis(statements, sector)

    actions = []
    for f in findings_sorted:
        if f["severity"] in {"critical", "high", "medium"}:
            actions.append({
                "priority": len(actions) + 1,
                "title": f["recommendation"],
                "reason": f["title"],
                "severity": f["severity"],
                "area": f["category"],
            })
        if len(actions) >= 5:
            break

    previous_statement = previous_periods[-1].get("statements") if previous_periods else None
    cash_bridge = build_cash_bridge(statements, previous_statement)
    profit_quality = build_profit_quality(statements, findings=findings_sorted)
    management_actions = build_management_actions(
        findings_sorted, opportunities_sorted, statements,
        causal_chains=root_cause.get('causal_chains'), gap_detection=gap_detection,
        priority_by_code=priority_by_code,
    )
    calculation_audit = build_calculation_audit(statements)

    # ----- 3. Executive Summary Engine -----
    # Built after management_actions/cash_bridge so the narrative can close
    # with a concrete "what should the manager do" decision paragraph and a
    # net-profit-to-cash sentence, instead of stopping at diagnosis.
    executive_summary = build_executive_summary(
        health_score, health_label, findings_sorted, opportunities_sorted,
        root_cause, business_impact, ccc, trend, benchmark,
        management_actions=management_actions, cash_bridge=cash_bridge,
        risk_ranking=risk_ranking, statements=statements,
        data_hub=data_hub,
    )
    scenarios = build_scenarios(statements)

    finding_registry = build_finding_registry(
        findings_sorted, gap_detection, root_cause, risk_ranking, business_impact,
        opportunities=opportunities_sorted, management_actions=management_actions,
    )
    gap_detection_for_report = finding_registry["gap_detection_deduplicated"]
    strategy_playbook = build_strategy_playbook(opportunities_sorted, scenarios)

    # ----- Narrative Engine (multi-scenario Ne oldu/Neden/Maliyet/Ne yapmalı) -----
    # Runs AFTER every input engine it reads from is available. Deliberately
    # separate from executive_summary_engine's top-1 narrative_story: this
    # produces one card PER independently-triggered scenario (margin
    # erosion, DSO risk, inventory bloat, cash runway...), not just the
    # single most severe finding.
    narrative_engine = build_narrative_engine(
        statements, trend, root_cause, business_impact, ccc, cash_bridge=cash_bridge,
        benchmark=benchmark, profit_quality=profit_quality,
        sales_intelligence=(data_hub or {}).get("analysis_sales"),
    )

    # New: DuPont 3 and 5-stage value driver tree decomposition
    dupont = build_dupont_analysis(statements)

    # New: Profit Improvement Sensitivity and Resource Allocation ("Para Nerede?")
    profit_improvement = build_profit_improvement_analysis(statements, (data_hub or {}).get("analysis_sales"))
    resource_allocation = build_resource_allocation_analysis(statements, data_hub)
    cust_prof = (data_hub or {}).get("customer_profitability") or {"status": "DATA_MISSING_EXPECTED", "reason": "Müşteri kârlılığı analizi için Satış Defteri (Sales Ledger) yüklenmedi."}
    prod_prof = (data_hub or {}).get("product_profitability") or {"status": "DATA_MISSING_EXPECTED", "reason": "Ürün kârlılığı analizi için Satış Defteri (Sales Ledger) yüklenmedi."}
    pricing_opp = (data_hub or {}).get("pricing_opportunity") or {"status": "DATA_MISSING_EXPECTED", "reason": "Fiyatlama fırsat analizi için Satış Defteri (Sales Ledger) yüklenmedi."}
    from .tax_strategy_engine import build_tax_strategy_analysis
    tax_strategy = build_tax_strategy_analysis(statements, data_hub)

    from .inflation_adjustment_engine import build_inflation_adjustment_analysis
    inflation_adjustment = build_inflation_adjustment_analysis(statements)

    from .liquidity_stress_testing_engine import build_liquidity_stress_test
    liquidity_stress_test = build_liquidity_stress_test(statements, data_hub)

    cash_flow = build_cash_flow_engine(
        statements,
        previous_statement=previous_statement,
        ccc=ccc,
        data_hub=data_hub,
        cash_bridge=cash_bridge,
        management_actions=management_actions,
        resource_allocation=resource_allocation,
        liquidity_stress_test=liquidity_stress_test,
    )

    from .fx_rates_provider import resolve_fx_rates
    period_meta = statements.get("period_metadata") or {}
    fx_rates = resolve_fx_rates(
        period_end_date=period_meta.get("period_end"),
        fiscal_year=period_meta.get("label"),
        raw_text_hint=str(period_meta),
    )
    statements["tax_strategy"] = tax_strategy
    statements["fx_rates"] = fx_rates

    from .kobi_patron_engine import build_kobi_patron_analysis
    kobi_patron = build_kobi_patron_analysis(
        statements=statements,
        sector=sector,
        data_hub=data_hub,
        kpis=statements.get("kpis"),
        bp={"health_score": health_score, "health_label": health_label, "cash_conversion": ccc},
    )

    core_metrics = build_core_metrics(
        statements=statements,
        quality=quality,
        ccc=ccc,
        health_score=health_score,
        health_label=health_label,
        data_hub=data_hub,
    )

    return {
        "engine_version": "2.0",
        "core_metrics": core_metrics,
        "health_score": health_score,
        "health_label": health_label,
        "score_components": {
            "data_trust": round(data_component, 1),
            "liquidity": round(liquidity_points, 1),
            "leverage": round(leverage_points, 1),
            "profitability": round(profitability_points, 1),
            "efficiency_capital": round(efficiency_points, 1),
        },
        "health_score_methodology": {
            "title": "Finansal Sağlık Skoru Metodolojisi & Ağırlık Dağılımı",
            "total_score": health_score,
            "max_score": 100,
            "label": health_label,
            "description": "Finansal Sağlık Skoru bir kara kutu veya sübjektif AI tahmini değildir; 5 temel kurumsal finans boyutunu ölçen kural tabanlı, deterministik bir kompozit skorlama modelidir.",
            "pillars": [
                {
                    "key": "data_trust",
                    "name": "Veri Güvenilirliği & Bilanço Denkliği",
                    "weight_pct": 15,
                    "max_points": 15.0,
                    "earned_points": round(data_component, 1),
                    "metric_basis": f"Veri Kalite Skoru: {data_score:.0f}/100",
                    "formula": "Veri Güvenilirlik Skoru × %15",
                    "evaluation": "Bilanço eşitliği, aktif/pasif mutabakatı ve hesap planı tutarlılığı."
                },
                {
                    "key": "liquidity",
                    "name": "Likidite & Kısa Vadeli Ödeme Gücü",
                    "weight_pct": 20,
                    "max_points": 20.0,
                    "earned_points": round(liquidity_points, 1),
                    "metric_basis": f"Cari Oran: {current_ratio if current_ratio is not None else 0.0:.2f} · Nakit Oranı: {cash_ratio if cash_ratio is not None else 0.0:.2f}",
                    "formula": "Cari Oran bandı (max 10p) + Nakit Oranı bandı (max 10p)",
                    "evaluation": "Vadesi gelen kısa vadeli borçların dönen ve nakit varlıklarla karşılanabilme gücü."
                },
                {
                    "key": "leverage",
                    "name": "Kaldıraç & Finansman Yükü",
                    "weight_pct": 25,
                    "max_points": 25.0,
                    "earned_points": round(leverage_points, 1),
                    "metric_basis": f"Borç/Özkaynak: {debt_to_equity if debt_to_equity is not None else 0.0:.2f}x · Fin. Gider/FVÖK: %{((finance_cost_to_op or 0.0)*100):.1f}",
                    "formula": "Borç/Özkaynak bandı (max 12p) + Finansman Gideri/Faaliyet Kârı bandı (max 13p)",
                    "evaluation": "Faaliyet kârının finansman giderlerini karşılama kapasitesi ve özkaynak emniyet marjı."
                },
                {
                    "key": "profitability",
                    "name": "Faaliyet & Net Kârlılık",
                    "weight_pct": 25,
                    "max_points": 25.0,
                    "earned_points": round(profitability_points, 1),
                    "metric_basis": f"Faaliyet Marjı: %{operating_margin if operating_margin is not None else 0.0:.1f} · Net Marj: %{net_margin if net_margin is not None else 0.0:.1f}",
                    "formula": "Faaliyet Kâr Marjı bandı (max 13p) + Net Kâr Marjı bandı (max 12p)",
                    "evaluation": "Satışların faaliyet seviyesinde ve net dönem seviyesinde kâra dönüşüm başarısı."
                },
                {
                    "key": "efficiency_capital",
                    "name": "Varlık Verimliliği & Sermaye Gücü",
                    "weight_pct": 15,
                    "max_points": 15.0,
                    "earned_points": round(efficiency_points, 1),
                    "metric_basis": f"Aktif Devir Hızı: {asset_turnover if asset_turnover is not None else 0.0:.2f}x · Özkaynak Oranı: %{((equity_ratio or 0.0)*100):.1f}",
                    "formula": "Aktif Devir Hızı bandı (max 8p) + Özkaynak/Aktif bandı (max 7p)",
                    "evaluation": "Bağlı aktiflerin ciro üretme hızı ve şirketin varlıklarını finanse eden özkaynak payı."
                }
            ]
        },
        "derived_metrics": {
            "finance_cost_to_operating_profit_pct": None if finance_cost_to_op is None else finance_cost_to_op * 100,
            "interest_coverage_proxy": interest_coverage_proxy,
            "debt_to_assets_pct": None if debt_to_assets is None else debt_to_assets * 100,
            "equity_ratio_pct": None if equity_ratio is None else equity_ratio * 100,
            "cash_to_financial_debt_pct": None if cash_to_debt is None else cash_to_debt * 100,
            "receivables_to_sales_pct": None if receivables_to_sales is None else receivables_to_sales * 100,
            "other_income_to_pbt_pct": None if non_core_income_to_pbt is None else non_core_income_to_pbt * 100,
        },
        # Legacy / backward-compatible fields (existing frontend + tests rely on these).
        "findings": findings_sorted,
        "opportunities": opportunities_sorted,
        "actions": actions,
        "executive_summary": executive_summary["text"],
        "methodology_note": "Skor ve kurallar genel finansal eşiklere dayanır; resmi sektör benchmarkı değildir. Trend analizi çok dönemli veri, gerçek DSO/DPO/DIO ise açılış bakiyesi/subledger verisi gerektirir; bu motorlar mevcut verinin izin verdiği ölçüde çalışır ve sınırlarını açıkça belirtir.",
        # Explicit Decision Engines
        "root_cause_engine": root_cause,
        "business_impact_engine": business_impact,
        "executive_summary_engine": executive_summary,
        "risk_ranking_engine": risk_ranking,
        "opportunity_engine": {"opportunities": opportunities_sorted},
        "cash_conversion_cycle": ccc,
        "trend_analysis": trend,
        "benchmarking": benchmark,
        "cash_bridge_engine": cash_bridge,
        "cash_flow_engine": cash_flow,
        "profit_quality_engine": profit_quality,
        "management_actions": management_actions,
        "calculation_audit": calculation_audit,
        "scenario_engine": {"scenarios": scenarios},
        "gap_detection_engine": gap_detection_for_report,
        "operational_finance_engine": operational_finance,
        "finding_registry": finding_registry,
        "strategy_playbook": strategy_playbook,
        "narrative_engine": narrative_engine,
        "dupont_analysis": dupont,
        "profit_improvement_engine": profit_improvement,
        "resource_allocation_engine": resource_allocation,
        "customer_profitability_engine": cust_prof,
        "product_profitability_engine": prod_prof,
        "pricing_opportunity_engine": pricing_opp,
        "tax_strategy_engine": tax_strategy,
        "inflation_adjustment_engine": inflation_adjustment,
        "liquidity_stress_testing_engine": liquidity_stress_test,
        "fx_rates": fx_rates,
        "kobi_patron_engine": kobi_patron,
    }
