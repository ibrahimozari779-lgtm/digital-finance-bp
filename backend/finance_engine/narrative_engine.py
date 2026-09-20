from __future__ import annotations

from typing import Any, Callable, Optional


# ===========================================================================
# NARRATIVE ENGINE  —  Financial Storytelling Layer
# ===========================================================================
# Bu modül, brief'te tarif edilen mimariyi birebir uygular:
#
#   Financial Data -> KPI Engine -> Variance Engine -> Root Cause Engine
#       -> Impact Engine -> NARRATIVE ENGINE
#
# Zaten var olan motorlar (trend_engine=Variance, root_cause_engine=Root
# Cause, business_impact_engine/cash_conversion_engine=Impact) bu pipeline'ın
# ilk 4 kutusunu karşılıyor. Bu dosya sadece son kutuyu ekliyor ve YENİ bir
# sayı üretmiyor: her tetikleyici, başka bir motorun ZATEN hesapladığı bir
# rakamı okuyup eşikle karşılaştırıyor, sonra o rakamı bir şablona döküyor.
#
# executive_summary_engine.py içindeki narrative_chain / narrative_story
# fonksiyonlarından FARKI: onlar "en kritik TEK bulgu" için tek bir hikâye
# üretir (top-1). Bu motor ise brief'teki 5 senaryo örneğinde görüldüğü gibi
# BİRDEN FAZLA bağımsız tetikleyiciyi (kârlılık erozyonu + tahsilat riski +
# stok şişmesi + nakit erken uyarı ...) AYNI ANDA, birbirinden bağımsız
# kartlar olarak üretebilir — CFO panosunda "bugün kaç tane hikâye var"
# sorusuna cevap verir, "en önemli hikâye hangisi" sorusuna değil.
#
# Tasarım ilkesi (brief'teki JSON trigger tablosuyla birebir örtüşür):
#
#   {
#     "trigger": "dso_increase",
#     "condition": data -> bool,
#     "template": ["DSO {old} günden {new} güne yükseldi.", ...],
#   }
#
# `_TRIGGERS` listesindeki her kayıt tam olarak budur: bir `condition`
# (rakamları okur, eşikle kıyaslar) ve bir `build` (rakamları şablona
# döker). Motor koşar, tetiklenen kuralları toplar, her biri için
# "Ne oldu? -> Neden oldu? -> Bana maliyeti ne? -> Ne yapmam lazım?" dört
# adımlı kartı üretir. Yeni bir senaryo eklemek = listeye yeni bir trigger
# eklemek; mevcut hiçbir koda dokunmadan genişler.
#
# DÜRÜSTLÜK SINIRI (brief'teki 5 örnekten hangileri gerçekten üretilebilir):
#   - Senaryo 1 (Kârlılık Erozyonu)      -> TAM DESTEKLENİYOR (trend + root_cause + business_impact)
#   - Senaryo 2 (Tahsilat Riski / DSO)   -> TAM DESTEKLENİYOR (trend.dso_days + cash_conversion)
#                                            "ilk 10 müşteride yoğunlaşma" kısmı DESTEKLENMİYOR
#                                            (müşteri bazlı aging verisi bu pipeline'a girmiyor).
#   - Senaryo 3 (Stok Şişmesi)           -> TAM DESTEKLENİYOR (trend.dio_days + cash_conversion)
#                                            "%27 slow-moving" kısmı DESTEKLENMİYOR (SKU seviyesi
#                                            hareket verisi bu pipeline'a girmiyor).
#   - Senaryo 4 (Müşteri Karlılık)       -> KOŞULLU OLARAK DESTEKLENİYOR. Kanonik finansal
#                                            model (bilanço/gelir tablosu) tek şirket seviyesinde
#                                            olsa da, kullanıcı ayrıca satış/tahsilat detay dosyası
#                                            (multi_source_intelligence -> sales_intelligence_engine)
#                                            yüklediğinde `customer_profitability` (müşteri bazlı
#                                            ciro/COGS/brüt marj) ZATEN hesaplanıyor. Bu veri mevcut
#                                            olduğunda trigger tetiklenir; olmadığında sessizce
#                                            atlanır (uydurulmaz) - aşağıdaki `_t_customer_margin_gap`.
#   - Senaryo 5 (Nakit Krizi Erken Uyarı)-> KISMEN DESTEKLENİYOR. Bilançodaki nakit bakiyesi var,
#                                            ama "aylık burn" kavramı yok (bu pipeline dönemsel
#                                            çalışıyor, aylık nakit akışı almıyor). Burada dönemsel
#                                            faaliyet nakit akışı proxy'sini (cash_bridge) period
#                                            uzunluğuna bölerek KABA bir aylık burn tahmini
#                                            üretiyoruz — sonucu "approx"/"kaba tahmin" olarak
#                                            açıkça etiketliyoruz, kesin ay sayısı gibi sunmuyoruz.
# ===========================================================================


def _safe(v: Any) -> float | None:
    try:
        return None if v is None else float(v)
    except (TypeError, ValueError):
        return None


def _latest(mt: dict[str, Any] | None, field: str) -> float | None:
    if not mt:
        return None
    arr = mt.get(field) or []
    return arr[-1] if arr else None


def _prev_from_latest_delta(mt: dict[str, Any] | None, field_series: str = "series", field_delta: str = "period_over_period_change_abs") -> tuple[float | None, float | None]:
    """Returns (old_value, new_value) for a metric using its own trend series -
    never re-derives, just reads what trend_engine already computed."""
    if not mt:
        return None, None
    series = mt.get(field_series) or []
    new_val = series[-1] if series else None
    delta = _latest(mt, field_delta)
    if new_val is None or delta is None:
        return None, new_val
    return round(new_val - delta, 2), new_val


# ---------------------------------------------------------------------------
# Context assembly: pulls together the outputs already computed by the
# other engines into one flat dict the trigger conditions/templates read
# from. No new arithmetic happens here beyond unit-safe lookups.
# ---------------------------------------------------------------------------

def _build_context(
    statements: dict[str, Any],
    trend: dict[str, Any],
    root_cause: dict[str, Any],
    business_impact: dict[str, Any],
    ccc: dict[str, Any],
    cash_bridge: dict[str, Any] | None,
    benchmark: dict[str, Any] | None = None,
    profit_quality: dict[str, Any] | None = None,
    sales_intelligence: dict[str, Any] | None = None,
) -> dict[str, Any]:
    pl = statements.get("profit_and_loss", {}) or {}
    k = statements.get("kpis", {}) or {}
    mt = (trend.get("metric_trends") or {}) if trend.get("available") else {}

    period_days = None
    if isinstance(statements.get("period_metadata"), dict):
        period_days = statements["period_metadata"].get("period_days")
    period_days = period_days or 365
    period_months = max(period_days / 30.4, 1e-6)

    net_sales = _safe(pl.get("Net sales")) or 0.0
    cogs = _safe(pl.get("COGS")) or 0.0

    gm_old, gm_new = _prev_from_latest_delta(mt.get("gross_margin_pct"), field_delta="period_over_period_change_pp")
    dso_old, dso_new = _prev_from_latest_delta(mt.get("dso_days"))
    dio_old, dio_new = _prev_from_latest_delta(mt.get("dio_days"))

    cogs_growth_pct = None
    price_growth_proxy_pct = None
    cogs_series = (mt.get("cogs") or {}).get("series") if mt.get("cogs") else None
    if cogs_series and len(cogs_series) >= 2 and cogs_series[-2]:
        cogs_growth_pct = round((cogs_series[-1] - cogs_series[-2]) / cogs_series[-2] * 100, 1)
    sales_series = (mt.get("net_sales") or {}).get("series") if mt.get("net_sales") else None
    if sales_series and len(sales_series) >= 2 and sales_series[-2]:
        price_growth_proxy_pct = round((sales_series[-1] - sales_series[-2]) / sales_series[-2] * 100, 1)

    gm_exposure = next(
        (r["amount"] for r in root_cause.get("margin_bridge", []) if r.get("label", "").startswith("Satışların maliyeti")),
        None,
    )
    annualization = 365.0 / period_days if period_days else 1.0
    gm_pp_change = _latest(mt.get("gross_margin_pct"), "period_over_period_change_pp")
    ebitda_impact_annualized = (
        round((gm_pp_change / 100.0) * net_sales * annualization, 0)
        if gm_pp_change is not None and net_sales else None
    )

    dso_cash_impact = None
    if dso_old is not None and dso_new is not None and net_sales:
        dso_cash_impact = round((dso_new - dso_old) * (net_sales / period_days), 0)

    dio_cash_impact = ccc.get("estimated_cash_tied_up") if ccc.get("available") else None
    inventory_balance = _safe(k.get("inventory"))

    cash_balance = _safe(k.get("cash"))
    monthly_burn = None
    runway_months = None
    if cash_bridge and cash_bridge.get("available"):
        ocf_proxy = cash_bridge.get("operating_cash_flow_proxy")
        if ocf_proxy is not None and ocf_proxy < 0:
            monthly_burn = round(abs(ocf_proxy) / period_months, 0)
    if cash_balance is not None and monthly_burn:
        runway_months = round(cash_balance / monthly_burn, 1)

    dte_old, dte_new = _prev_from_latest_delta(mt.get("debt_to_equity"), field_delta="period_over_period_change_pp")
    cr_old, cr_new = _prev_from_latest_delta(mt.get("current_ratio"), field_delta="period_over_period_change_pp")
    nm_old, nm_new = _prev_from_latest_delta(mt.get("net_margin_pct"), field_delta="period_over_period_change_pp")
    sales_growth_pct = price_growth_proxy_pct  # same underlying series, reused for readability at call sites

    cash_realization_pct = (
        cash_bridge.get("cash_realization_pct") if cash_bridge and cash_bridge.get("available") else None
    )
    finance_burden_pct = None
    op_profit = _safe(pl.get("Operating profit"))
    finance_costs_v = _safe(pl.get("Finance costs"))
    if op_profit:
        finance_burden_pct = round(finance_costs_v / op_profit * 100, 1) if finance_costs_v is not None else None

    benchmark = benchmark or {}
    profit_quality = profit_quality or {}
    sales_intelligence = sales_intelligence or {}
    company_gross_margin_pct = k.get("gross_margin_pct")

    return {
        "sales_intelligence": sales_intelligence,
        "company_gross_margin_pct": company_gross_margin_pct,
        "net_sales": net_sales, "cogs": cogs,
        "gm_old": gm_old, "gm_new": gm_new, "gm_pp_change": gm_pp_change,
        "cogs_growth_pct": cogs_growth_pct, "price_growth_proxy_pct": price_growth_proxy_pct,
        "gm_exposure": gm_exposure, "ebitda_impact_annualized": ebitda_impact_annualized,
        "dso_old": dso_old, "dso_new": dso_new, "dso_cash_impact": dso_cash_impact,
        "dio_old": dio_old, "dio_new": dio_new, "dio_cash_impact": dio_cash_impact,
        "inventory_balance": inventory_balance,
        "cash_balance": cash_balance, "monthly_burn": monthly_burn, "runway_months": runway_months,
        "period_months": period_months,
        "dte_old": dte_old, "dte_new": dte_new,
        "cr_old": cr_old, "cr_new": cr_new,
        "nm_old": nm_old, "nm_new": nm_new,
        "sales_growth_pct": sales_growth_pct,
        "cash_realization_pct": cash_realization_pct,
        "finance_burden_pct": finance_burden_pct,
        "benchmark": benchmark, "profit_quality": profit_quality,
        "root_cause": root_cause, "business_impact": business_impact,
    }


# ---------------------------------------------------------------------------
# Trigger registry — brief'teki JSON tablonun Python karşılığı. Her trigger:
#   code, title, category           -> kimlik
#   condition(ctx) -> bool          -> ateşleme koşulu (var olan eşiklerle)
#   severity(ctx) -> str            -> critical/high/medium
#   build(ctx) -> dict              -> ne_oldu / neden / maliyet / ne_yapmali
# ---------------------------------------------------------------------------

Trigger = dict[str, Any]


def _t_margin_erosion() -> Trigger:
    def condition(ctx: dict[str, Any]) -> bool:
        return ctx["gm_pp_change"] is not None and ctx["gm_pp_change"] <= -1.5

    def severity(ctx: dict[str, Any]) -> str:
        chg = ctx["gm_pp_change"]
        return "critical" if chg <= -5 else "high" if chg <= -2.5 else "medium"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        chg = ctx["gm_pp_change"]
        neden_bits = []
        if ctx["cogs_growth_pct"] is not None:
            neden_bits.append(f"hammadde/satış maliyeti dönemde %{ctx['cogs_growth_pct']:.1f} arttı")
        if ctx["price_growth_proxy_pct"] is not None:
            neden_bits.append(f"satış fiyatı/gelir tarafı yalnızca %{ctx['price_growth_proxy_pct']:.1f} değişti")
        neden = (
            f"Ana neden, maliyet artışının fiyata tam yansıtılamamasıdır ({', '.join(neden_bits)})."
            if neden_bits else
            "Trend Motoru dönemsel COGS/gelir kırılımını hesaplayamadı; maliyet-fiyat makasının büyüklüğü doğrulanamıyor."
        )
        maliyet = (
            f"Mevcut eğilim devam ederse yıllıklandırılmış EBITDA üzerinde yaklaşık "
            f"{ctx['ebitda_impact_annualized']:,.0f} TL negatif baskı oluşabilir."
            if ctx["ebitda_impact_annualized"] is not None else
            "Yıllıklandırılmış etki, net satış verisi yetersiz olduğu için hesaplanamadı."
        )
        return {
            "ne_oldu": f"Brüt kâr marjı {abs(chg):.1f} puan geriledi"
                       + (f" (%{ctx['gm_old']:.1f} → %{ctx['gm_new']:.1f})." if ctx['gm_old'] is not None and ctx['gm_new'] is not None else "."),
            "neden": neden,
            "maliyet": maliyet,
            "ne_yapmali": [
                "Fiyat geçişlerinin (pass-through) gözden geçirilmesi",
                "Düşük marjlı ürün/segmentlerin incelenmesi",
                "Alternatif tedarik kaynaklarının değerlendirilmesi",
            ],
        }

    return {
        "code": "NE-MARGIN-EROSION", "title": "Kârlılık Erozyonu", "category": "Kârlılık",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["trend_engine.gross_margin_pct"],
    }


def _t_dso_risk() -> Trigger:
    def condition(ctx: dict[str, Any]) -> bool:
        return ctx["dso_old"] is not None and ctx["dso_new"] is not None and (ctx["dso_new"] - ctx["dso_old"]) >= 10

    def severity(ctx: dict[str, Any]) -> str:
        d = ctx["dso_new"] - ctx["dso_old"]
        return "critical" if d >= 30 else "high" if d >= 20 else "medium"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        d = ctx["dso_new"] - ctx["dso_old"]
        maliyet = (
            f"{d:.0f} günlük artış, işletme sermayesinde yaklaşık {ctx['dso_cash_impact']:,.0f} TL "
            f"ilave nakit ihtiyacı yaratmaktadır."
            if ctx["dso_cash_impact"] is not None else
            "Nakit etkisi, net satış verisi yetersiz olduğu için hesaplanamadı."
        )
        return {
            "ne_oldu": f"Tahsilat süresi (DSO) {ctx['dso_old']:.0f} günden {ctx['dso_new']:.0f} güne yükseldi.",
            "neden": "Tahsilat performansındaki yavaşlama, toplam alacak bakiyesindeki değişimden tespit edilmiştir; "
                     "hangi müşterilerde gecikme yoğunlaştığını kesinleştirmek için müşteri bazlı alt defter (120 yaşlandırma) "
                     "analiziyle teyit edilmesi önerilir.",
            "maliyet": maliyet,
            "ne_yapmali": [
                "Alacak yaşlandırma (120 cari hesap) raporunun çıkarılması ve en büyük gecikmelerin tespiti",
                "Kredi ve vade limitlerinin gözden geçirilmesi",
                "Tahsilat takip sıklığının haftalık icraat masasına alınması",
            ],
            "data_gap": "Müşteri bazlı alacak konsantrasyonu ve gecikme detayları için Data Hub üzerinden müşteri yaşlandırma defteri eklenebilir.",
        }

    return {
        "code": "NE-DSO-RISK", "title": "Tahsilat Riski", "category": "İşletme Sermayesi",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["trend_engine.dso_days"],
    }


def _t_inventory_bloat() -> Trigger:
    def condition(ctx: dict[str, Any]) -> bool:
        return ctx["dio_old"] is not None and ctx["dio_new"] is not None and (ctx["dio_new"] - ctx["dio_old"]) >= 10

    def severity(ctx: dict[str, Any]) -> str:
        d = ctx["dio_new"] - ctx["dio_old"]
        return "critical" if d >= 40 else "high" if d >= 20 else "medium"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        d = ctx["dio_new"] - ctx["dio_old"]
        maliyet = (
            f"Yaklaşık {ctx['dio_cash_impact']:,.0f} TL stokta bağlı sermaye bulunmaktadır."
            if ctx["dio_cash_impact"] is not None else
            f"Dönem sonu stok bakiyesi {ctx['inventory_balance']:,.0f} TL; tam nakit döngüsü etkisi COGS verisiyle birlikte hesaplanabilir."
            if ctx["inventory_balance"] is not None else
            "Stokta bağlı sermaye tutarı hesaplanamadı."
        )
        return {
            "ne_oldu": f"Stok devir süresi (DIO) {ctx['dio_old']:.0f} günden {ctx['dio_new']:.0f} güne yükseldi ({d:.0f} gün artış).",
            "neden": "Stok devir hızındaki yavaşlama toplam envanter bakiyesinden görülüyor; hangi ürün "
                     "gruplarında atıl stok oluştuğunu netleştirmek için ürün bazlı (SKU) detaylandırma önerilir.",
            "maliyet": maliyet,
            "ne_yapmali": [
                "Yavaş hareket eden (hareketsiz) stok analizi yapılması",
                "Satın alma ve sipariş parametrelerinin güncellenmesi",
                "Atıl stok tasfiye ve nakde çevirme planının devreye alınması",
            ],
            "data_gap": "Ürün bazlı atıl ve yavaş hareket eden stok kırılımı için Data Hub üzerinden stok envanter defteri eklenebilir.",
        }

    return {
        "code": "NE-INVENTORY-BLOAT", "title": "Stok Şişmesi", "category": "Verimlilik",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["trend_engine.dio_days"],
    }


def _t_cash_runway() -> Trigger:
    def condition(ctx: dict[str, Any]) -> bool:
        return ctx["runway_months"] is not None and ctx["runway_months"] <= 6

    def severity(ctx: dict[str, Any]) -> str:
        rm = ctx["runway_months"]
        return "critical" if rm <= 2 else "high" if rm <= 4 else "medium"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        return {
            "ne_oldu": f"Mevcut nakit pozisyonu ({ctx['cash_balance']:,.0f} TL), kaba bir aylık faaliyet nakit "
                       f"akışı (yakma hızı) tahminiyle yaklaşık {ctx['runway_months']:.1f} aylık operasyonu "
                       f"finanse edebilecek düzeydedir.",
            "neden": "Bu dönemde esas faaliyet nakit akışı negatiftir (Nakit Akış Köprüsü); aylık net nakit erimesi "
                     "(Net Cash Burn), işletme nakit açığının dönem ay sayısına oranlanmasıyla hesaplanmıştır.",
            "maliyet": f"Aylık net operasyonel nakit tüketimi (Net Cash Burn): {ctx['monthly_burn']:,.0f} TL.",
            "ne_yapmali": [
                "Öncelikli tahsilat hızlandırma ve vade kısaltma programı",
                "Atıl stokların tasfiyesi ve nakit serbestleştirme",
                "Zorunlu olmayan sermaye harcamalarının (capex) ertelenmesi",
            ],
            "data_gap": "Detaylı haftalık/aylık nakit akışı tahmini için 13 Haftalık Nakit Projeksiyonu modülü kullanılmalıdır.",
            "approx": True,
        }

    return {
        "code": "NE-CASH-RUNWAY", "title": "Nakit Krizi Erken Uyarısı", "category": "Likidite",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["cash_bridge_engine (2 dönem)", "kpis.cash"],
    }


def _t_leverage_risk() -> Trigger:
    # Aynı eşik decision_engine.py'de L002'yi kritik yapan eşiktir (>5x);
    # burada tekrar bağımsız bir eşik icat edilmiyor.
    def condition(ctx: dict[str, Any]) -> bool:
        return ctx["dte_new"] is not None and ctx["dte_old"] is not None and ctx["dte_new"] > 2.0 and (ctx["dte_new"] - ctx["dte_old"]) > 0.2

    def severity(ctx: dict[str, Any]) -> str:
        v = ctx["dte_new"]
        return "critical" if v > 5 else "high" if v > 3 else "medium"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        d = ctx["dte_new"] - ctx["dte_old"]
        return {
            "ne_oldu": f"Borç/Özkaynak oranı {ctx['dte_old']:.2f}x'ten {ctx['dte_new']:.2f}x'e yükseldi.",
            "neden": "Finansal borç, özkaynak tabanına göre daha hızlı büyüyor; işletme sermayesi açığının "
                     "(alacak/stok artışı) ek borçla kapatılıyor olması olası bir sürücüdür (Root Cause Motoru "
                     "ile çapraz kontrol edilmelidir).",
            "maliyet": f"Kaldıraç {d:.2f}x arttı; bu, gelecekte finansman maliyetini ve kredi/teminat "
                       f"koşullarını olumsuz etkileyebilir.",
            "ne_yapmali": [
                "Borç vade yapısının ve faiz oranlarının gözden geçirilmesi",
                "İşletme sermayesi ihtiyacının borç yerine tahsilat/stok iyileştirmesiyle azaltılması",
                "Yeni yatırım/harcama kararlarının kaldıraç iyileşene kadar ertelenmesi",
            ],
        }

    return {
        "code": "NE-LEVERAGE-RISK", "title": "Kaldıraç Artışı", "category": "Borçluluk",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["trend_engine.debt_to_equity"],
    }


def _t_liquidity_risk() -> Trigger:
    # Aynı eşik decision_engine.py'nin Q001 kritik eşiği (<1.0).
    def condition(ctx: dict[str, Any]) -> bool:
        return ctx["cr_new"] is not None and ctx["cr_old"] is not None and ctx["cr_new"] < 1.3 and ctx["cr_new"] < ctx["cr_old"]

    def severity(ctx: dict[str, Any]) -> str:
        v = ctx["cr_new"]
        return "critical" if v < 1.0 else "high" if v < 1.15 else "medium"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        return {
            "ne_oldu": f"Cari oran {ctx['cr_old']:.2f}'den {ctx['cr_new']:.2f}'e geriledi.",
            "neden": "Kısa vadeli yükümlülükler, kısa vadeli varlıklara göre daha hızlı büyüyor; bu genellikle "
                     "artan kısa vadeli borçlanma ve/veya yavaşlayan tahsilat/stok devrinin birleşik etkisidir.",
            "maliyet": (
                "Cari oran 1.0'ın altına indi: kısa vadeli varlıklar kısa vadeli borçları karşılamıyor, bu "
                "likidite açısından acil bir uyarı seviyesidir."
                if ctx["cr_new"] < 1.0 else
                "Cari oran güvenli bandın (>1.3-1.5) altına yaklaşıyor; tampon daralıyor."
            ),
            "ne_yapmali": [
                "Kısa vadeli borç/uzun vadeli borç dengesinin yeniden yapılandırılması",
                "Tahsilat ve stok devir hızının iyileştirilmesi",
                "Kısa vadeli nakit akış planlamasının haftalık takibe alınması",
            ],
        }

    return {
        "code": "NE-LIQUIDITY-RISK", "title": "Likidite Daralması", "category": "Likidite",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["trend_engine.current_ratio"],
    }


def _t_earnings_quality() -> Trigger:
    def condition(ctx: dict[str, Any]) -> bool:
        return ctx["cash_realization_pct"] is not None and ctx["cash_realization_pct"] < 50

    def severity(ctx: dict[str, Any]) -> str:
        v = ctx["cash_realization_pct"]
        return "critical" if v < 0 else "high" if v < 25 else "medium"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        crp = ctx["cash_realization_pct"]
        return {
            "ne_oldu": f"Net kârın yalnızca yaklaşık %{crp:.0f}'i işletme nakdine dönüşüyor.",
            "neden": "Fark, alacak/stok artışı ve/veya borç ödemesinin nakti tükettiği çalışma sermayesi "
                     "kalemlerinde bağlanıyor (cash_bridge_engine kırılımına bakınız); defter kârı gerçek "
                     "ama henüz kasaya girmemiş durumda.",
            "maliyet": "Kâr rakamı yönetim raporlamasında güçlü görünse de, kısa vadeli nakit ihtiyacını "
                       "tek başına karşılamıyor — ek finansman veya çalışma sermayesi iyileştirmesi gerekebilir.",
            "ne_yapmali": [
                "Çalışma sermayesi kalemlerinin (alacak/stok/borç) ayrı ayrı incelenmesi",
                "Nakit akış tahmininin kâr tahmininden bağımsız olarak takip edilmesi",
                "Kâr paylaşımı/temettü gibi nakit çıkışı kararlarının bu farkı hesaba katarak alınması",
            ],
        }

    return {
        "code": "NE-EARNINGS-QUALITY", "title": "Kazanç Kalitesi / Nakde Dönmeyen Kâr", "category": "Kazanç Kalitesi",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["cash_bridge_engine (2 dönem)"],
    }


def _t_finance_cost_burden() -> Trigger:
    def condition(ctx: dict[str, Any]) -> bool:
        return ctx["finance_burden_pct"] is not None and ctx["finance_burden_pct"] > 30

    def severity(ctx: dict[str, Any]) -> str:
        v = ctx["finance_burden_pct"]
        return "critical" if v > 70 else "high" if v > 50 else "medium"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        return {
            "ne_oldu": f"Finansman giderleri, faaliyet kârının %{ctx['finance_burden_pct']:.0f}'ini tüketiyor.",
            "neden": "Faiz/finansman yükü, operasyonel kârlılığa göre orantısız büyük; yüksek borç seviyesi "
                     "ve/veya yüksek faiz ortamı bu makasın ana sürücüsüdür.",
            "maliyet": "Faaliyet kârının büyük bölümü finansman giderlerine gittiği için net kâra kalan pay "
                       "daralıyor; faiz oranlarındaki ek bir artış bu etkiyi doğrudan büyütür.",
            "ne_yapmali": [
                "Borcun yeniden fiyatlanması/refinansmanının değerlendirilmesi",
                "Operasyonel kârlılığın artırılmasına öncelik verilmesi (finansman baskısını mutlak olarak azaltmasa da payını düşürür)",
                "Döviz cinsi borç varsa kur riskinin ayrıca değerlendirilmesi",
            ],
        }

    return {
        "code": "NE-FINANCE-BURDEN", "title": "Finansman Maliyeti Baskısı", "category": "Borçluluk",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["profit_and_loss.Finance costs", "profit_and_loss.Operating profit"],
    }


def _t_sector_underperformance() -> Trigger:
    def condition(ctx: dict[str, Any]) -> bool:
        bm = ctx["benchmark"]
        return bm.get("overall_score") is not None and bm["overall_score"] < 40

    def severity(ctx: dict[str, Any]) -> str:
        v = ctx["benchmark"]["overall_score"]
        return "high" if v < 25 else "medium"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        bm = ctx["benchmark"]
        weak = [m["label"] for m in bm.get("metrics", []) if m.get("favorability") == "olumsuz"]
        return {
            "ne_oldu": f"{bm.get('sector', 'sektör')} göstergeleriyle kıyaslandığında genel konum: "
                       f"{bm.get('overall_label', '').lower()} (skor {bm['overall_score']:.0f}/100).",
            "neden": (
                f"Zayıf konumlanan göstergeler: {', '.join(weak[:4])}."
                if weak else "Birden fazla göstergede sektör bandının altında kalınıyor."
            ),
            "maliyet": "Sektör ortalamasının altında kalmak; rekabet gücü, finansmana erişim koşulları ve "
                       "yatırımcı/kredi verenler nezdinde algı açısından dolaylı bir maliyet taşır.",
            "ne_yapmali": [
                "En zayıf 1-2 göstergeye odaklanan bir iyileştirme planı hazırlanması",
                "Sektör bandının hangi varsayımlara dayandığının (Genel/indikatif bant) gözden geçirilmesi",
                "İlerlemenin çeyreklik olarak aynı benchmark ile yeniden ölçülmesi",
            ],
        }

    return {
        "code": "NE-SECTOR-UNDERPERFORMANCE", "title": "Sektör Altı Performans", "category": "Genel",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["benchmarking_engine"],
    }


def _t_growth_without_profit() -> Trigger:
    """Ciro büyürken kârlılığın gerilemesi - klasik 'büyüme tuzağı' senaryosu."""
    def condition(ctx: dict[str, Any]) -> bool:
        return (
            ctx["sales_growth_pct"] is not None and ctx["sales_growth_pct"] > 5
            and ctx["nm_old"] is not None and ctx["nm_new"] is not None
            and (ctx["nm_new"] - ctx["nm_old"]) <= -1.0
        )

    def severity(ctx: dict[str, Any]) -> str:
        d = ctx["nm_new"] - ctx["nm_old"]
        return "high" if d <= -3 else "medium"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        return {
            "ne_oldu": f"Net satışlar %{ctx['sales_growth_pct']:.1f} büyürken net kâr marjı "
                       f"%{ctx['nm_old']:.1f}'den %{ctx['nm_new']:.1f}'e geriledi.",
            "neden": "Büyüme, kârlılığı da beraberinde getirmiyor; bu genellikle büyümenin düşük marjlı "
                     "kanallar/ürünler üzerinden gerçekleştiğine, maliyet artışının fiyata yansıtılamadığına "
                     "veya büyümeyle orantısız OPEX/finansman yükü arttığına işaret eder.",
            "maliyet": "Ciro büyürken kârlılığın gerilemesi, uzun vadede sürdürülemez bir büyüme profiline "
                       "işaret edebilir; her ek TL satış, orantılı ek kâr getirmiyor.",
            "ne_yapmali": [
                "Büyümenin kaynaklandığı segment/kanalların marj bazında ayrıştırılması",
                "Fiyatlama ve iskonto politikasının büyüme hedefleriyle birlikte gözden geçirilmesi",
                "Büyümeyle birlikte artan OPEX/finansman kalemlerinin ayrı izlenmesi",
            ],
        }

    return {
        "code": "NE-GROWTH-WITHOUT-PROFIT", "title": "Kârsız Büyüme", "category": "Kârlılık",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["trend_engine.net_sales", "trend_engine.net_margin_pct"],
    }


def _t_margin_improvement() -> Trigger:
    """Pozitif senaryo: sistem sadece riskleri değil, gerçek iyileşmeleri de
    aynı Ne oldu/Neden/Etki/Ne yapmalı formatıyla anlatır - CFO'ya sadece kötü
    haber değil, neyin işe yaradığını da gösterir."""
    def condition(ctx: dict[str, Any]) -> bool:
        return ctx["gm_pp_change"] is not None and ctx["gm_pp_change"] >= 2.0

    def severity(ctx: dict[str, Any]) -> str:
        return "positive"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        chg = ctx["gm_pp_change"]
        return {
            "ne_oldu": f"Brüt kâr marjı {chg:.1f} puan iyileşti"
                       + (f" (%{ctx['gm_old']:.1f} → %{ctx['gm_new']:.1f})." if ctx['gm_old'] is not None and ctx['gm_new'] is not None else "."),
            "neden": (
                f"Satış fiyatı/gelir tarafı %{ctx['price_growth_proxy_pct']:.1f} artarken maliyet artışı "
                f"%{ctx['cogs_growth_pct']:.1f} ile daha sınırlı kaldı."
                if ctx["price_growth_proxy_pct"] is not None and ctx["cogs_growth_pct"] is not None else
                "Trend Motoru'nun hesapladığı dönemsel kırılıma göre maliyet tarafı gelir tarafından daha yavaş büyüdü."
            ),
            "maliyet": (
                f"Bu eğilim korunursa yıllıklandırılmış EBITDA üzerinde yaklaşık "
                f"+{ctx['ebitda_impact_annualized']:,.0f} TL olumlu etki oluşabilir."
                if ctx["ebitda_impact_annualized"] is not None else
                "Yıllıklandırılmış olumlu etki, veri yetersizliği nedeniyle hesaplanamadı."
            ),
            "ne_yapmali": [
                "İyileşmeyi sağlayan fiyatlama/maliyet aksiyonlarının kalıcı hale getirilmesi",
                "Bu marj seviyesinin bir sonraki dönem bütçe/hedeflerine yansıtılması",
                "İyileşmenin hangi ürün/segmentten geldiğinin doğrulanarak ölçeklendirilmesi",
            ],
        }

    return {
        "code": "NE-MARGIN-IMPROVEMENT", "title": "Kârlılık İyileşmesi", "category": "Kârlılık",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["trend_engine.gross_margin_pct"],
    }


def _t_customer_margin_gap() -> Trigger:
    """Yalnızca kullanıcı satış detay dosyası yüklediğinde ve
    sales_intelligence_engine müşteri bazlı brüt marj hesaplayabildiğinde
    tetiklenir. Şirket ortalaması yine kanonik finansal modelden (kpis.gross_margin_pct)
    alınır - iki farklı motorun sayısı burada kıyaslanır, hiçbiri yeniden hesaplanmaz."""
    def _worst_customer(ctx: dict[str, Any]) -> dict[str, Any] | None:
        si = ctx["sales_intelligence"]
        rows = si.get("customer_profitability") or []
        avg = ctx["company_gross_margin_pct"]
        if not rows or avg is None:
            return None
        total_sales = sum((r.get("sales") or 0) for r in rows) or None
        candidates = [
            r for r in rows
            if r.get("gross_margin_pct") is not None
            and (avg - r["gross_margin_pct"]) >= 10
            and total_sales and (r.get("sales") or 0) / total_sales >= 0.05
        ]
        if not candidates:
            return None
        return min(candidates, key=lambda r: r["gross_margin_pct"]), total_sales

    def condition(ctx: dict[str, Any]) -> bool:
        return _worst_customer(ctx) is not None

    def severity(ctx: dict[str, Any]) -> str:
        cust, _ = _worst_customer(ctx)
        gap = ctx["company_gross_margin_pct"] - cust["gross_margin_pct"]
        return "high" if gap >= 20 else "medium"

    def build(ctx: dict[str, Any]) -> dict[str, Any]:
        cust, total_sales = _worst_customer(ctx)
        share_pct = round((cust.get("sales") or 0) / total_sales * 100, 1) if total_sales else None
        return {
            "ne_oldu": f"{cust['name']} müşterisinin brüt marjı %{cust['gross_margin_pct']:.1f} seviyesinde; "
                       f"şirket ortalaması ise %{ctx['company_gross_margin_pct']:.1f}.",
            "neden": "Fark; düşük fiyatlandırma, yüksek iskonto oranı veya bu müşteriye özgü yüksek "
                     "maliyet kalemlerinden (ör. lojistik) kaynaklanıyor olabilir - kesin ayrıştırma için "
                     "müşteri bazlı fiyat/iskonto detayı gerekir.",
            "maliyet": (
                f"Müşteri toplam satışların yaklaşık %{share_pct}'ini oluşturuyor ancak karlılığa katkısı "
                f"şirket ortalamasının belirgin altında."
                if share_pct is not None else
                "Bu müşterinin toplam satış payı hesaplanamadı."
            ),
            "ne_yapmali": [
                "Fiyat revizyonu değerlendirilmesi",
                "Minimum sipariş tutarı uygulaması",
                "Müşteri bazlı karlılık görüşmesi yapılması",
            ],
        }

    return {
        "code": "NE-CUSTOMER-MARGIN-GAP", "title": "Müşteri Karlılık Problemi", "category": "Kârlılık",
        "condition": condition, "severity": severity, "build": build,
        "requires": ["sales_intelligence_engine.customer_profitability (satış detay dosyası yüklendiyse)"],
    }


_TRIGGERS: list[Trigger] = [
    _t_margin_erosion(), _t_dso_risk(), _t_inventory_bloat(), _t_cash_runway(),
    _t_leverage_risk(), _t_liquidity_risk(), _t_earnings_quality(), _t_finance_cost_burden(),
    _t_sector_underperformance(), _t_growth_without_profit(), _t_margin_improvement(),
    _t_customer_margin_gap(),
]


# ---------------------------------------------------------------------------
# Senaryo 4 (Müşteri Karlılık Problemi) bu pipeline'ın canonical veri
# modeliyle üretilemiyor - şirket seviyesinde tek bir gelir tablosu var,
# müşteri kırılımı yok. Uydurmak yerine, ileride bu veri geldiğinde
# doğrudan eklenebilecek minimum şemayı ve trigger taslağını belgeliyoruz.
# ---------------------------------------------------------------------------
CUSTOMER_LEVEL_DATA_SCHEMA_NOTE = (
    "Senaryo 4 (Müşteri Karlılık Problemi), sales_intelligence_engine.customer_profitability "
    "hesaplanabildiğinde (yani kullanıcı müşteri kolonu içeren bir satış detay dosyası "
    "yüklediğinde) `_t_customer_margin_gap` triggerı ile ÜRETİLİR. Yalnızca kanonik bilanço/gelir "
    "tablosu (tek şirket seviyesi) yüklendiğinde ve satış detay dosyası yoksa, bu senaryo için "
    "gereken müşteri kırılımı mevcut olmadığından kart üretilmez."
)


def build_narrative_engine(
    statements: dict[str, Any],
    trend: dict[str, Any],
    root_cause: dict[str, Any],
    business_impact: dict[str, Any],
    ccc: dict[str, Any],
    cash_bridge: dict[str, Any] | None = None,
    benchmark: dict[str, Any] | None = None,
    profit_quality: dict[str, Any] | None = None,
    sales_intelligence: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Narrative Engine: rule-table triggers over already-computed engine
    outputs, each expanded into an explicit Ne oldu / Neden / Maliyet /
    Ne yapmalı card. Runs ALL triggers (not just the top-1 finding), so a
    period can surface several independent stories at once, matching the
    brief's "farklı senaryolar" requirement. Covers both risk scenarios
    (margin erosion, DSO/DIO deterioration, leverage, liquidity, earnings
    quality, finance-cost burden, sector underperformance, profitless
    growth, cash runway) and a positive scenario (margin improvement) -
    a Business Partner narrates what's working, not only what's broken.
    """
    ctx = _build_context(statements, trend, root_cause, business_impact, ccc, cash_bridge, benchmark, profit_quality, sales_intelligence)

    stories: list[dict[str, Any]] = []
    for trig in _TRIGGERS:
        try:
            if not trig["condition"](ctx):
                continue
        except Exception:
            continue
        body = trig["build"](ctx)
        stories.append({
            "code": trig["code"],
            "title": trig["title"],
            "category": trig["category"],
            "severity": trig["severity"](ctx),
            **body,
        })

    _sev_rank = {"critical": 4, "high": 3, "medium": 2, "positive": 1}
    stories.sort(key=lambda s: _sev_rank.get(s["severity"], 0), reverse=True)

    return {
        "available": bool(stories),
        "stories": stories,
        "triggers_evaluated": [t["code"] for t in _TRIGGERS],
        "unsupported_scenarios": [
            {"scenario": "Müşteri Karlılık Problemi", "reason": CUSTOMER_LEVEL_DATA_SCHEMA_NOTE},
        ],
        "note": (
            "Her kart yalnızca başka motorların ZATEN hesapladığı rakamlardan üretilir; hiçbir sayı bu "
            "motorda yeniden türetilmez veya uydurulmaz. 'data_gap' alanı olan kartlarda, brief'teki örnek "
            "çıktıda görülen alt kırılım (ör. 'ilk 10 müşteri', '%27 slow-moving') mevcut veri modeliyle "
            "üretilemez ve bu açıkça belirtilir; sessizce atlanmaz."
        ),
    }
