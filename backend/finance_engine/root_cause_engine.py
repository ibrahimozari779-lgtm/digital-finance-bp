from __future__ import annotations

from typing import Any


def _safe_div(a: float | None, b: float | None) -> float | None:
    if a is None or b in (None, 0):
        return None
    return float(a) / float(b)


def build_root_cause_analysis(statements: dict[str, Any], findings: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """Root Cause Engine.

    Decomposes net sales -> net profit into a percent-of-sales waterfall
    (margin bridge) and identifies which line item is the largest driver of
    margin compression. Also builds causal chains linking symptom findings
    (e.g. weak operating margin, high finance-cost pressure, working-capital
    strain) to their most likely underlying driver, using only figures
    already present in the canonical financial model - nothing is inferred
    beyond what the statements support.

    Master Decision Hub wiring (Faz 1): when `findings` is supplied (the
    Decision Engine's own Findings list, already computed from these same
    statements), each causal chain fires ONLY when the Finding(s) it
    explains are themselves already present in that list - Root Cause
    stops re-deriving its own, independently-threshold-checked diagnosis
    and instead narrates *why* a Finding that already exists looks the way
    it does. This closes a real inconsistency risk: before this change,
    Root Cause used its own copy of each threshold (e.g. operating_margin
    < 10 here vs. < 5 for P002 in decision_engine.py, receivables/sales >
    0.40 here vs. > 0.50 for W001) - two independently-maintained copies of
    "the same" rule that could silently drift apart and produce a root
    cause chain for a symptom the Findings list never actually flagged, or
    vice versa. `findings=None` preserves the old threshold-based standalone
    behaviour for any caller that has no Findings list to pass yet.
    """
    pl = statements["profit_and_loss"]
    k = statements["kpis"]

    net_sales = float(pl.get("Net sales") or 0.0)
    cogs = float(pl.get("COGS") or 0.0)
    gross_profit = float(pl.get("Gross profit") or 0.0)
    opex = float(pl.get("Operating expenses") or 0.0)
    operating_profit = float(pl.get("Operating profit") or 0.0)
    other_op_income = float(pl.get("Other operating income") or 0.0)
    other_op_expense = float(pl.get("Other operating expense") or 0.0)
    finance_costs = float(pl.get("Finance costs") or 0.0)
    other_nonop_income = float(pl.get("Other non-operating income") or 0.0)
    other_nonop_expense = float(pl.get("Other non-operating expense") or 0.0)
    pre_tax = float(pl.get("Pre-tax profit") or 0.0)
    tax = float(pl.get("Tax expense") or 0.0)
    net_profit = float(pl.get("Net profit") or 0.0)

    def pct(v: float) -> float | None:
        return round(v / net_sales * 100, 2) if net_sales else None

    def _tl(v: float) -> str:
        return f"{v:,.0f}".replace(",", ".")

    bridge = [
        {"label": "Net satışlar", "amount": net_sales, "pct_of_sales": pct(net_sales), "is_subtotal": True},
        {"label": "Satışların maliyeti (COGS)", "amount": -cogs, "pct_of_sales": pct(-cogs), "is_subtotal": False},
        {"label": "Brüt kâr", "amount": gross_profit, "pct_of_sales": pct(gross_profit), "is_subtotal": True},
        {"label": "Faaliyet giderleri", "amount": -opex, "pct_of_sales": pct(-opex), "is_subtotal": False},
        {"label": "Faaliyet kârı", "amount": operating_profit, "pct_of_sales": pct(operating_profit), "is_subtotal": True},
        {"label": "Diğer faaliyet gelir/gideri (net)", "amount": other_op_income - other_op_expense, "pct_of_sales": pct(other_op_income - other_op_expense), "is_subtotal": False},
        {"label": "Finansman giderleri", "amount": -finance_costs, "pct_of_sales": pct(-finance_costs), "is_subtotal": False},
        {"label": "Diğer faaliyet dışı gelir/gider (net)", "amount": other_nonop_income - other_nonop_expense, "pct_of_sales": pct(other_nonop_income - other_nonop_expense), "is_subtotal": False},
        {"label": "Vergi öncesi kâr", "amount": pre_tax, "pct_of_sales": pct(pre_tax), "is_subtotal": True},
        {"label": "Vergi gideri", "amount": -tax, "pct_of_sales": pct(-tax), "is_subtotal": False},
        {"label": "Net kâr", "amount": net_profit, "pct_of_sales": pct(net_profit), "is_subtotal": True},
    ]

    # Rank the deduction lines (non-subtotal, negative amount = margin drag) by
    # magnitude to find the single biggest driver of margin compression.
    drags = [row for row in bridge if not row["is_subtotal"] and row["amount"] is not None and row["amount"] < 0]
    primary_driver = max(drags, key=lambda r: abs(r["amount"])) if drags else None

    gross_margin_pct = k.get("gross_margin_pct")
    operating_margin_pct = k.get("operating_margin_pct")
    finance_cost_to_op = _safe_div(finance_costs, operating_profit)
    debt_to_equity = k.get("debt_to_equity")
    receivables_to_sales = _safe_div(float(k.get("receivables") or 0.0), net_sales)

    causal_chains: list[dict[str, Any]] = []

    # Findings actually raised for this period (non-positive only - a
    # "positive" finding like P001 means the symptom this chain would
    # explain does not exist). None when no Findings list was supplied.
    codes_present: set[str] | None = None
    if findings is not None:
        codes_present = {f.get("code") for f in findings if f.get("severity") != "positive"}

    # Profitability root cause chain.
    profitability_triggered = (
        bool(codes_present & {"P002", "P003"}) if codes_present is not None
        else (operating_margin_pct is not None and operating_margin_pct < 10)
    )
    if profitability_triggered:
        gross_margin_low = (
            "P003" in codes_present if codes_present is not None
            else (gross_margin_pct is not None and gross_margin_pct < 15)
        )
        opex_heavy = bool(opex and net_sales and (opex / net_sales) > 0.20)
        if gross_margin_low:
            chain = [
                "Brüt marj düşük (fiyatlama ve/veya maliyet baskısı)",
                "Faaliyet giderleri brüt kârın önemli bölümünü tüketiyor",
                "Faaliyet kârı zayıflıyor",
            ]
            driver = "Satış maliyeti / fiyatlama"
        elif opex_heavy:
            chain = [
                "Brüt marj kabul edilebilir seviyede",
                "Faaliyet giderleri satışlara göre ağır",
                "Faaliyet kârı zayıflıyor",
            ]
            driver = "Faaliyet giderleri (OPEX)"
        else:
            chain = [
                "Faaliyet marjı zayıf görünüyor",
                "Tek başına brüt marj veya OPEX oranı eşik dışı değil; birleşik etki olası",
            ]
            driver = "Brüt marj + OPEX bileşimi"

        rc_p_evidence: list[str] = []
        if gross_margin_pct is not None:
            rc_p_evidence.append(f"Brüt Kâr Marjı: %{gross_margin_pct:.1f}")
        if opex and net_sales:
            rc_p_evidence.append(f"Faaliyet Gideri / Ciro: %{(opex / net_sales * 100):.1f}")
        if operating_margin_pct is not None:
            rc_p_evidence.append(f"Faaliyet Kâr Marjı: %{operating_margin_pct:.1f}")
        if operating_profit is not None:
            rc_p_evidence.append(f"Faaliyet Kârı: {_tl(operating_profit)} TL")

        causal_chains.append({
            "code": "RC-P", "title": "Faaliyet Kârlılığı Kök Nedeni",
            "chain": chain, "primary_driver": driver,
            "evidence": rc_p_evidence,
            "financial_impact": f"Faaliyet kârı erimesi (~{_tl(abs(opex))} TL gider yükü)",
            "recommended_actions": [
                "Ürün bazlı kârlılık kırılımını çıkarıp negatif marjlı ürünleri fiyatlayın",
                "Faaliyet giderlerinde (770/760) tasarruf bütçesi belirleyin",
            ],
            "related_findings": ["P001", "P002", "P003"],
            "causal_status": "likely_driver",
            "required_additional_evidence": ["product/customer margin", "pricing and discount data", "cost breakdown"],
        })

    # Financing pressure root cause chain.
    financing_triggered = (
        bool(codes_present & {"L001", "L002", "D004", "D005", "D006", "D007"}) if codes_present is not None
        else (finance_cost_to_op is not None and finance_cost_to_op > 0.25)
    )
    if financing_triggered:
        chain = ["Finansal borç seviyesi yüksek"]
        if debt_to_equity is not None and debt_to_equity > 2:
            chain.append("Borç/özkaynak oranı yüksek, kaldıraç sınırlı özkaynakla destekleniyor")
        chain.append("Finansman giderleri faaliyet kârının önemli bölümünü tüketiyor")

        rc_l_evidence: list[str] = []
        if finance_costs is not None:
            rc_l_evidence.append(f"Finansman Gideri: {_tl(finance_costs)} TL")
        if finance_cost_to_op is not None:
            rc_l_evidence.append(f"Finansman Gideri / Faaliyet Kârı: %{(finance_cost_to_op * 100):.1f}")
        if debt_to_equity is not None:
            rc_l_evidence.append(f"Borç / Özkaynak (Kaldıraç): {debt_to_equity:.2f}x")
        fin_debt = float(k.get("financial_debt") or 0.0)
        if fin_debt > 0:
            rc_l_evidence.append(f"Toplam Finansal Borç: {_tl(fin_debt)} TL")

        causal_chains.append({
            "code": "RC-L", "title": "Finansman Baskısı Kök Nedeni",
            "chain": chain, "primary_driver": "Finansal kaldıraç (borç seviyesi)",
            "evidence": rc_l_evidence,
            "financial_impact": f"Yıllık {_tl(finance_costs)} TL nakit faiz sızıntısı",
            "recommended_actions": [
                "Kredi vadelerini yeniden yapılandırın ve yüksek faizli rotatifleri kapatın",
                "Nakit sermaye artırımı (KVK 10/1-ı) ile faiz indiriminden faydalanın",
            ],
            "related_findings": ["L001", "L002", "D004", "D005", "D006", "D007"],
            "causal_status": "likely_driver",
            "required_additional_evidence": ["debt maturity schedule", "interest rates by facility", "currency mix", "cash flow forecast"],
        })

    # Working-capital root cause chain.
    working_capital_triggered = (
        bool(codes_present & {"W001", "WC004"}) if codes_present is not None
        else (receivables_to_sales is not None and receivables_to_sales > 0.40)
    )
    if working_capital_triggered:
        chain = ["Ticari alacaklar satışlara göre yüksek seviyede"]
        if debt_to_equity is not None and debt_to_equity > 2:
            chain.append("Tahsilatın gecikmesi işletme sermayesi açığı yaratıyor")
            chain.append("Açık, ek borçlanma ile kapatılıyor olabilir (borç/özkaynak yüksek)")
        else:
            chain.append("Nakde dönüşüm süresi uzuyor, likidite tamponu daralabilir")

        rc_w_evidence: list[str] = []
        rec_val = float(k.get("receivables") or 0.0)
        if rec_val > 0:
            rc_w_evidence.append(f"Müşteri Alacakları (120): {_tl(rec_val)} TL")
        if receivables_to_sales is not None:
            rc_w_evidence.append(f"Alacak / Satış Oranı: %{(receivables_to_sales * 100):.1f}")
        dso_val = k.get("dso")
        if dso_val is not None:
            rc_w_evidence.append(f"Ortalama Tahsilat Vadesi (DSO): {round(float(dso_val))} gün")

        causal_chains.append({
            "code": "RC-W", "title": "İşletme Sermayesi Kök Nedeni",
            "chain": chain, "primary_driver": "Alacak tahsilat hızı",
            "evidence": rc_w_evidence,
            "financial_impact": f"Müşteri vadelerinde kilitli {_tl(rec_val)} TL sermaye",
            "recommended_actions": [
                "Vadesi geçen alacaklar için DBS / teminat protokolü uygulayın",
                "Erken ödeme yapan müşterilere peşin iskontosu sunarak nakdi çekin",
            ],
            "related_findings": ["W001", "WC004"],
            "causal_status": "hypothesis",
            "required_additional_evidence": ["AR aging", "customer concentration", "payment terms", "collection history"],
        })

    return {
        "margin_bridge": bridge,
        "primary_margin_driver": primary_driver,
        "causal_chains": causal_chains,
        "findings_driven": codes_present is not None,
        "note": (
            "Kök neden zinciri yalnızca kanonik finansal modeldeki kalemlerden türetilir; dönem/subledger detay verisi olmadan nihai kök neden değil, en olası sürücü gösterilir. "
            + (
                "Her zincir, Findings listesinde zaten mevcut olan bulgular üzerinden tetiklenir (Master Decision Hub: Finding → Root Cause); eşik kontrolü ayrıca tekrarlanmaz."
                if codes_present is not None else
                "Findings listesi sağlanmadığından zincirler kendi eşik kontrolleriyle bağımsız çalıştı (standalone mod)."
            )
        ),
    }
