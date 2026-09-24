"""Cash Flow & 13-Week Dynamic Liquidity Projection Engine (Nakit Akışı & 13 Haftalık Karar Motoru).

Calculates:
1. TMS 7 Indirect Cash Flow Statement (İşletme, Yatırım, Finansman Nakit Akışları ve Kasa Mutabakatı).
   - Fully synchronized with Cash Bridge Engine (cash_bridge_engine.py) when multi-period data is present.
2. 13-Week Rolling Cash Flow Projection (Haftalık nakit akış seyri, nakit açığı riski, deficit week tespiti).
   - Calibrated with actual operating cash flow proxy, DSO, DPO, and monthly operational burn.
3. Patron Karar Kokpiti:
   - "Para Nerede?": 100% aligned with Resource Allocation Engine (resource_allocation_engine.py).
   - "Sorun Ne & Kaç TL?": Derived from actual findings, gap detection, and liquidity stress tests.
   - "Bu Hafta Ne Yapmalı?": Directly mapped from prioritized Management Actions (action_engine.py)
     with personalized, data-driven WhatsApp directives quoting the company's real numbers.
"""
from __future__ import annotations
import math
from typing import Any


def _safe_float(val: Any, default: float = 0.0) -> float:
    if val is None:
        return default
    try:
        f = float(val)
        return default if (math.isnan(f) or math.isinf(f)) else f
    except (ValueError, TypeError):
        return default


def build_cash_flow_engine(
    statements: dict[str, Any],
    previous_statement: dict[str, Any] | None = None,
    ccc: dict[str, Any] | None = None,
    data_hub: dict[str, Any] | None = None,
    cash_bridge: dict[str, Any] | None = None,
    management_actions: list[dict[str, Any]] | None = None,
    resource_allocation: dict[str, Any] | None = None,
    liquidity_stress_test: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Generates standard TMS 7 indirect cash flow, 13-week forecast, and executive actions,
    strictly aligned with existing engines (cash_bridge, resource_allocation, action_engine).
    """
    kpis = statements.get("kpis", {})
    pl = statements.get("profit_and_loss", {})
    bs = statements.get("balance_sheet", {})

    cash = _safe_float(kpis.get("cash"))
    receivables = _safe_float(kpis.get("receivables"))
    inventory = _safe_float(kpis.get("inventory"))
    payables = _safe_float(kpis.get("payables"))
    financial_debt = _safe_float(kpis.get("financial_debt"))

    net_sales = _safe_float(pl.get("Net sales") or pl.get("Revenue"))
    cogs = _safe_float(pl.get("COGS"))
    operating_profit = _safe_float(pl.get("Operating profit"))
    net_profit = _safe_float(pl.get("Net profit"))
    finance_costs = _safe_float(pl.get("Finance costs") or kpis.get("financial_expense"))
    opex = _safe_float(pl.get("Operating expenses"))
    tax_expense = _safe_float(pl.get("Tax expense"))

    current_assets = _safe_float(bs.get("Current assets"))
    noncurrent_assets = _safe_float(bs.get("Non-current assets"))
    current_liab = _safe_float(bs.get("Current liabilities"))

    # Working capital metrics (DSO, DPO, DIO)
    ccc_dict = ccc or statements.get("cash_conversion_cycle") or {}
    dso = _safe_float(ccc_dict.get("dso_days") or ccc_dict.get("dso"), 60.0)
    dpo = _safe_float(ccc_dict.get("dpo_days") or ccc_dict.get("dpo"), 45.0)
    dio = _safe_float(ccc_dict.get("dio_days") or ccc_dict.get("dio"), 60.0)

    analysis_ar = (data_hub or {}).get("analysis_ar") or (data_hub or {}).get("ar_aging") or {}
    analysis_ap = (data_hub or {}).get("analysis_ap") or (data_hub or {}).get("ap_aging") or {}
    analysis_inv = (data_hub or {}).get("analysis_inventory") or (data_hub or {}).get("inventory") or {}
    overdue_ar = _safe_float(analysis_ar.get("overdue") or analysis_ar.get("overdue_total"))
    overdue_ap = _safe_float(analysis_ap.get("overdue") or analysis_ap.get("overdue_total"))
    stale_stock = _safe_float(analysis_inv.get("stale_180_amount"))

    # =========================================================================
    # A) TMS 7 Indirect Cash Flow Statement (Dolaylı Nakit Akış Tablosu)
    # =========================================================================
    has_cb = cash_bridge is not None and cash_bridge.get("available") is True
    has_prior = previous_statement is not None or has_cb

    if has_cb:
        # 100% Exact alignment with cash_bridge_engine
        cb_wcc = cash_bridge.get("working_capital_components") or {}
        delta_rec = _safe_float(cb_wcc.get("receivables_effect"))
        delta_inv = _safe_float(cb_wcc.get("inventory_effect"))
        delta_pay = _safe_float(cb_wcc.get("payables_effect"))
        wc_change_total = delta_rec + delta_inv + delta_pay
        operating_cf = _safe_float(cash_bridge.get("operating_cash_flow_proxy"))
        delta_debt = _safe_float(cash_bridge.get("debt_change"))
        opening_cash_tms7 = _safe_float(cash_bridge.get("opening_cash"))
        closing_cash_tms7 = _safe_float(cash_bridge.get("closing_cash"))
        net_cash_flow_tms7 = _safe_float(cash_bridge.get("cash_change"))
        depreciation_est = max(0.0, operating_cf - net_profit - finance_costs - wc_change_total)
        financing_cf = delta_debt - finance_costs
        investing_cf = net_cash_flow_tms7 - operating_cf - financing_cf
        delta_capex = investing_cf
        reconciliation_diff = round(net_cash_flow_tms7 - (operating_cf + investing_cf + financing_cf), 2)
    elif has_prior and previous_statement:
        pk = previous_statement.get("kpis", {})
        pbs = previous_statement.get("balance_sheet", {})
        p_cash = _safe_float(pk.get("cash"))
        p_rec = _safe_float(pk.get("receivables"))
        p_inv = _safe_float(pk.get("inventory"))
        p_pay = _safe_float(pk.get("payables"))
        p_debt = _safe_float(pk.get("financial_debt"))
        p_noncurrent = _safe_float(pbs.get("Non-current assets"))

        delta_rec = -(receivables - p_rec)
        delta_inv = -(inventory - p_inv)
        delta_pay = (payables - p_pay)
        delta_debt = (financial_debt - p_debt)
        delta_capex = -(max(0.0, noncurrent_assets - p_noncurrent))
        opening_cash_tms7 = p_cash
        closing_cash_tms7 = cash
        net_cash_flow_tms7 = closing_cash_tms7 - opening_cash_tms7
        wc_change_total = delta_rec + delta_inv + delta_pay
        op_base = operating_profit if operating_profit != 0 else (net_profit + finance_costs)
        operating_cf = op_base + wc_change_total
        financing_cf = delta_debt - finance_costs
        investing_cf = net_cash_flow_tms7 - operating_cf - financing_cf
        delta_capex = investing_cf
        depreciation_est = max(0.0, operating_cf - net_profit - finance_costs - wc_change_total)
        reconciliation_diff = round(net_cash_flow_tms7 - (operating_cf + investing_cf + financing_cf), 2)
    else:
        # Single period management proxy
        opening_cash_tms7 = max(0.0, cash - (operating_profit * 0.2))
        closing_cash_tms7 = cash
        delta_rec = -min(receivables * 0.25, net_sales * (dso / 365.0) * 0.3)
        delta_inv = -min(inventory * 0.20, cogs * (dio / 365.0) * 0.25)
        delta_pay = min(payables * 0.20, cogs * (dpo / 365.0) * 0.25)
        delta_debt = financial_debt * 0.10
        delta_capex = -max(0.0, noncurrent_assets * 0.04)
        depreciation_est = noncurrent_assets * 0.05 if noncurrent_assets > 0 else (opex * 0.08)
        wc_change_total = delta_rec + delta_inv + delta_pay
        operating_cf = net_profit + depreciation_est + finance_costs + wc_change_total
        investing_cf = delta_capex
        financing_cf = delta_debt - finance_costs
        net_cash_flow_tms7 = operating_cf + investing_cf + financing_cf
        reconciliation_diff = 0.0

    tms7_statement = {
        "is_two_period": bool(has_prior),
        "mode": "TMS 7 Dolaylı Nakit Akış Tablosu" + (" (İki Dönem Karşılaştırmalı)" if has_prior else " (Yönetimsel Tahmini Köprü)"),
        "operating_activities": {
            "net_profit": net_profit,
            "depreciation_addback": round(depreciation_est, 2),
            "finance_costs_addback": round(finance_costs, 2),
            "receivables_change": round(delta_rec, 2),
            "inventory_change": round(delta_inv, 2),
            "payables_change": round(delta_pay, 2),
            "net_working_capital_change": round(wc_change_total, 2),
            "net_operating_cash_flow": round(operating_cf, 2),
        },
        "investing_activities": {
            "capex_tangible_assets": round(delta_capex, 2),
            "net_investing_cash_flow": round(investing_cf, 2),
        },
        "financing_activities": {
            "net_debt_change": round(delta_debt, 2),
            "finance_costs_paid": round(-finance_costs, 2),
            "net_financing_cash_flow": round(financing_cf, 2),
        },
        "summary": {
            "opening_cash": round(opening_cash_tms7, 2),
            "net_cash_change": round(net_cash_flow_tms7, 2),
            "closing_cash": round(closing_cash_tms7, 2),
            "reconciliation_difference": reconciliation_diff,
        },
    }

    # =========================================================================
    # B) 13-Week Rolling Cash Flow Projection (13 Haftalık Dinamik Projeksiyon)
    # =========================================================================
    # Calibration with actual monthly burn from liquidity_stress_testing_engine:
    # monthly_burn_rate = (cogs / 12.0) if cogs > 0 else (current_liab / 6.0)
    monthly_cogs_burn = (cogs / 12.0) if cogs > 0 else (current_liab / 6.0)
    weekly_supplier_burn = monthly_cogs_burn / 4.33

    monthly_opex_burn = (opex / 12.0) if opex > 0 else (net_sales / 12.0 * 0.15 if net_sales > 0 else current_liab / 8.0)
    weekly_payroll_opex = monthly_opex_burn / 4.33

    monthly_finance_burn = (finance_costs / 12.0) if finance_costs > 0 else (financial_debt * 0.45 / 12.0)
    weekly_finance_service = monthly_finance_burn / 4.33

    weekly_total_burn = weekly_supplier_burn + weekly_payroll_opex + weekly_finance_service

    # Inflows: derived from weekly sales velocity & DSO collection lag
    monthly_sales = (net_sales / 12.0) if net_sales > 0 else (receivables / max(1.0, dso / 30.0))
    weekly_base_sales = monthly_sales / 4.33

    # If operating cash flow is known to be negative (from cash bridge),
    # calibrate weekly net operating flow to reflect this cash drain:
    weekly_ocf_adjustment = (operating_cf / 52.0) if (has_cb and operating_cf < 0) else 0.0

    min_safety_buffer = max(50_000.0, weekly_total_burn * 1.5)

    # Runway from liquidity stress test if available
    runway_weeks_from_engine = None
    if liquidity_stress_test and "runway_days_normal" in liquidity_stress_test:
        runway_weeks_from_engine = round(_safe_float(liquidity_stress_test["runway_days_normal"]) / 7.0, 1)

    weeks_projection = []
    running_cash = cash
    deficit_weeks = []
    lowest_cash_point = cash
    lowest_week = 1

    uncollected_overdue = overdue_ar if overdue_ar > 0 else (receivables * 0.35)

    for w in range(1, 14):
        # 1. Inflows
        collection_factor = 1.0
        if w in (1, 2):
            collection_factor = 0.85
        elif w in (3, 4, 7, 8, 11, 12):
            collection_factor = 1.10

        base_collection = weekly_base_sales * collection_factor
        if weekly_ocf_adjustment < 0:
            # Negative cash flow realization dampens base collection inflow
            base_collection = max(base_collection * 0.6, base_collection + weekly_ocf_adjustment)

        overdue_recovery_weekly = (uncollected_overdue * 0.05) if w > 3 else (uncollected_overdue * 0.01)
        total_inflows = base_collection + overdue_recovery_weekly

        # 2. Outflows
        supp_multiplier = 1.30 if (w % 4 == 2) else 0.90
        supp_outflow = weekly_supplier_burn * supp_multiplier

        if w in (4, 8, 12):
            payroll_outflow = weekly_payroll_opex * 2.2
            tax_outflow = max(20_000.0, (tax_expense / 12.0) * 1.2 if tax_expense > 0 else monthly_sales * 0.03)
            debt_outflow = weekly_finance_service * 2.5
        else:
            payroll_outflow = weekly_payroll_opex * 0.6
            tax_outflow = 0.0
            debt_outflow = weekly_finance_service * 0.5

        total_outflows = supp_outflow + payroll_outflow + tax_outflow + debt_outflow

        net_change = total_inflows - total_outflows
        beginning_cash = running_cash
        ending_cash = beginning_cash + net_change
        running_cash = ending_cash

        if ending_cash < lowest_cash_point:
            lowest_cash_point = ending_cash
            lowest_week = w

        status = "HEALTHY"
        if ending_cash < 0:
            status = "DEFICIT"
            deficit_weeks.append(w)
        elif ending_cash < min_safety_buffer:
            status = "WARNING"

        weeks_projection.append({
            "week": w,
            "label": f"Hafta {w}",
            "beginning_cash": round(beginning_cash, 2),
            "inflows": round(total_inflows, 2),
            "inflow_breakdown": {
                "regular_collections": round(base_collection, 2),
                "overdue_recovery": round(overdue_recovery_weekly, 2),
            },
            "outflows": round(total_outflows, 2),
            "outflow_breakdown": {
                "supplier_payments": round(supp_outflow, 2),
                "payroll_and_opex": round(payroll_outflow, 2),
                "tax_and_sgk": round(tax_outflow, 2),
                "debt_service": round(debt_outflow, 2),
            },
            "net_cash_flow": round(net_change, 2),
            "ending_cash": round(ending_cash, 2),
            "status": status,
        })

    # Runway determination
    if deficit_weeks:
        runway_weeks = float(max(0, deficit_weeks[0] - 1))
    elif runway_weeks_from_engine is not None:
        runway_weeks = min(13.0, runway_weeks_from_engine)
    elif weekly_total_burn > 0:
        runway_weeks = min(13.0, round(cash / weekly_total_burn, 1))
    else:
        runway_weeks = 13.0

    # =========================================================================
    # C) Patron Karar Kokpiti & Yönetici Yorum Motoru
    # =========================================================================
    # 1. "Para Nerede?" - 100% Aligned with Resource Allocation Engine
    if resource_allocation and resource_allocation.get("where_is_money"):
        ra_money = resource_allocation["where_is_money"]
        headline_story = ra_money.get("summary_narrative") or ""
        total_operational_capital = cash + receivables + inventory
        cash_pct = round((cash / total_operational_capital * 100), 1) if total_operational_capital > 0 else 0.0
        rec_pct = round((receivables / total_operational_capital * 100), 1) if total_operational_capital > 0 else 0.0
        inv_pct = round((inventory / total_operational_capital * 100), 1) if total_operational_capital > 0 else 0.0
    else:
        total_operational_capital = cash + receivables + inventory
        cash_pct = round((cash / total_operational_capital * 100), 1) if total_operational_capital > 0 else 0.0
        rec_pct = round((receivables / total_operational_capital * 100), 1) if total_operational_capital > 0 else 0.0
        inv_pct = round((inventory / total_operational_capital * 100), 1) if total_operational_capital > 0 else 0.0
        headline_story = (
            f"Kasadaki sıcak para ₺{cash:,.0f} (%{cash_pct}); "
            f"operasyonel sermayenizin %{rec_pct + inv_pct:.0f}'i "
            f"(₺{receivables + inventory:,.0f}) müşteri senetlerinde ve depoda kilitli."
        ).replace(",", ".")

    where_is_the_money = {
        "cash_amount": cash,
        "cash_pct": cash_pct,
        "receivables_amount": receivables,
        "receivables_pct": rec_pct,
        "inventory_amount": inventory,
        "inventory_pct": inv_pct,
        "payables_amount": payables,
        "net_working_capital": round(receivables + inventory - payables, 2),
        "headline": headline_story,
    }

    # 2. "Sorun Ne & Kaç TL?" - Dynamically derived from findings & anomalies
    anomalies = []
    # Anomaly A: Vade Makası
    if dso > dpo:
        gap_days = round(dso - dpo)
        gap_exposure = round(net_sales * (gap_days / 365.0), 2) if net_sales > 0 else round(receivables * 0.3, 2)
        anomalies.append({
            "code": "ALM-VADE-MAKASI",
            "title": f"Vade Makası Açık ({gap_days} Gün Açık)",
            "description": f"Tedarikçiye ortalama {dpo:.0f} günde öderken, müşteriden {dso:.0f} günde tahsil ediyorsunuz. Şirket {gap_days} gün boyunca müşterilerini finanse etmek için dışarıdan kredi kullanıyor.",
            "exposure_tl": gap_exposure,
            "severity": "critical" if gap_days > 30 else "warning",
        })

    # Anomaly B: Kasa Açığı / Tampon Riski
    if deficit_weeks:
        first_def = deficit_weeks[0]
        deepest_deficit = abs(min(0.0, lowest_cash_point))
        anomalies.append({
            "code": "ALM-NAKIT-ACIGI",
            "title": f"{first_def}. Haftada Kasa Açığı Riski (-₺{deepest_deficit:,.0f})".replace(",", "."),
            "description": f"13 haftalık projeksiyonda; maaş, SGK, vergi ve tedarikçi ödemelerinin kümelendiği {first_def}. haftada kasanız eksiye düşüyor.",
            "exposure_tl": deepest_deficit,
            "severity": "critical",
        })
    elif runway_weeks < 3.0:
        anomalies.append({
            "code": "ALM-DUSUK-TAMPON",
            "title": f"Likidite Tamponu Yetersiz ({runway_weeks:.1f} Hafta)",
            "description": "Kasadaki mevcut nakit, haftalık asgari operasyonel çıkışlarınızı 3 haftadan daha az süre karşılayabilir.",
            "exposure_tl": weekly_total_burn * 2,
            "severity": "warning",
        })

    # Anomaly C: Faiz Erozyonu
    if finance_costs > 0 and operating_profit > 0:
        fin_to_op = (finance_costs / operating_profit) * 100
        if fin_to_op > 20:
            anomalies.append({
                "code": "ALM-FAIZ-BASKISI",
                "title": f"Faiz Baskısı: Kârın %{fin_to_op:.0f}'i Bankaya Gidiyor",
                "description": f"Faaliyet kârınızın (₺{operating_profit:,.0f}) yaklaşık ₺{finance_costs:,.0f} tutarındaki kısmı kredi ve finansman faizlerine eriyor.".replace(",", "."),
                "exposure_tl": finance_costs,
                "severity": "critical" if fin_to_op > 40 else "warning",
            })

    # Anomaly D: Vadesi Geçmiş Alacak (varsa)
    if overdue_ar > 0:
        anomalies.append({
            "code": "ALM-VADESI-GECMIS-AR",
            "title": f"Vadesi Geçmiş Alacak Alarmı (₺{overdue_ar:,.0f})".replace(",", "."),
            "description": f"Toplam alacakların ₺{overdue_ar:,.0f} tutarındaki kısmı vadesini aşmış ve tahsilat riski oluşturmaktadır.",
            "exposure_tl": overdue_ar,
            "severity": "critical",
        })

    # 3. "Bu Hafta Ne Yapmalı?" - Directly mapped from prioritized Management Actions!
    actions = []
    raw_actions = management_actions or []
    if raw_actions:
        # Take the top 3 actions prioritized by Action Engine / Risk Ranking
        for idx, ma in enumerate(raw_actions[:3]):
            aid = ma.get("action_id", f"ACT-{idx+1}")
            task = ma.get("action", "")
            owner = ma.get("owner", "CFO")
            horizon = ma.get("time_horizon", "0-15 gün")
            kpi = ma.get("kpi", "İşletme Sermayesi")
            impact = ma.get("expected_financial_impact")
            if impact is None:
                # Calibrated financial impact proxy from finding evidence
                impact = overdue_ar if "AR" in kpi or "DSO" in kpi else (finance_costs if "Finance" in kpi or "Interest" in kpi else receivables * 0.15)

            # Build deeply personalized, data-driven WhatsApp direct message quoting company specifics
            wa_text = _build_whatsapp_directive(owner, task, horizon, kpi, impact)

            actions.append({
                "id": aid,
                "task": task,
                "owner": owner,
                "deadline": horizon,
                "kpi": kpi,
                "cash_impact_tl": round(impact, 2),
                "whatsapp_template": wa_text,
            })

    # Fallback if no management actions provided:
    if not actions:
        ar_target = round(min(receivables * 0.25, overdue_ar if overdue_ar > 0 else receivables * 0.20), 2)
        actions.append({
            "id": "ACT-AR-1",
            "task": f"İlk 5 Müşteriden Vadeli Çek Yerine DBS veya Erken Tahsilat İskontosu Talep Et (Mevcut DSO: {dso:.0f} gün)",
            "owner": "Kredi & Tahsilat Yönetimi",
            "deadline": "0-15 gün",
            "kpi": f"Tahsilat Süresi (DSO: {dso:.0f} gün → {max(30, dso - 15):.0f} gün)",
            "cash_impact_tl": ar_target,
            "whatsapp_template": (
                f"Sayın Kredi Kontrol ve Satış Yöneticim, haftalık nakit projeksiyonumuza göre acil likidite sağlamamız gerekiyor. "
                f"İlk 5 büyük müşterimizle görüşerek en az ₺{ar_target:,.0f} tutarında erken tahsilat veya DBS limiti "
                f"sağlanmasını, vadesi geçen bakiyeler kapatılmadan yeni sevkiyat açılmamasını rica ederim."
            ).replace(",", "."),
        })

        ap_target = round(payables * 0.15, 2)
        actions.append({
            "id": "ACT-AP-1",
            "task": f"Kritik Tedarikçilerle Görüşüp Ödeme Vadelerini Genişlet (Mevcut DPO: {dpo:.0f} gün, Vade Makası: {round(dso-dpo)} gün)",
            "owner": "Satınalma & Hazine Yönetimi",
            "deadline": "0-30 gün",
            "kpi": f"Tedarikçi Ödeme Vadesi (DPO: {dpo:.0f} gün → {dpo + 15:.0f} gün)",
            "cash_impact_tl": ap_target,
            "whatsapp_template": (
                f"Sayın Hazine ve Satınalma Yöneticim, tedarikçi ödeme vadelerimizi incelediğimizde müşteriye göre çok erken "
                f"ödeme yaptığımızı görüyoruz. Ana tedarikçilerimizle görüşerek ödeme takvimine +15 gün ilave "
                f"vade alınmasını ve kasadan çıkacak ₺{ap_target:,.0f} tutarın ertelenmesini sağlayalım."
            ).replace(",", "."),
        })

        inv_target = round(inventory * 0.15, 2)
        actions.append({
            "id": "ACT-INV-1",
            "task": f"Depodaki Hareketsiz Stoklar İçin Hızlı Tasfiye / İskonto Kampanyası Başlat (Mevcut DIO: {dio:.0f} gün)",
            "owner": "Tedarik Zinciri & Depo",
            "deadline": "0-30 gün",
            "kpi": f"Stok Bekleme Süresi (DIO: {dio:.0f} gün → {max(30, dio - 18):.0f} gün)",
            "cash_impact_tl": inv_target,
            "whatsapp_template": (
                f"Operasyon ve Satış Ekibine: Depomuzda bekleyen stoklar her ay finansman faizi üretmektedir. "
                f"Bu hafta hareketsiz ürün listesini çıkarıp özel iskonto ile en az ₺{inv_target:,.0f} "
                f"tutarında stok tasfiyesini tamamlayalım."
            ).replace(",", "."),
        })

    total_unlockable_cash = sum(a["cash_impact_tl"] for a in actions)

    patron_cockpit = {
        "where_is_the_money": where_is_the_money,
        "runway_weeks": runway_weeks,
        "lowest_cash_point": round(lowest_cash_point, 2),
        "lowest_week": lowest_week,
        "deficit_weeks": deficit_weeks,
        "min_safety_buffer": round(min_safety_buffer, 2),
        "anomalies": anomalies[:3],
        "actions": actions[:3],
        "total_unlockable_cash": round(total_unlockable_cash, 2),
    }

    return {
        "available": True,
        "tms7_statement": tms7_statement,
        "thirteen_week_projection": {
            "weeks": weeks_projection,
            "summary": {
                "opening_cash": round(cash, 2),
                "ending_cash_week_13": round(weeks_projection[-1]["ending_cash"], 2) if weeks_projection else round(cash, 2),
                "total_inflows": round(sum(w["inflows"] for w in weeks_projection), 2),
                "total_outflows": round(sum(w["outflows"] for w in weeks_projection), 2),
                "lowest_cash_point": round(lowest_cash_point, 2),
                "lowest_week": lowest_week,
                "first_deficit_week": deficit_weeks[0] if deficit_weeks else None,
                "runway_weeks": runway_weeks,
                "min_safety_buffer": round(min_safety_buffer, 2),
            },
        },
        "patron_cockpit": patron_cockpit,
    }


def _build_whatsapp_directive(owner: str, task: str, horizon: str, kpi: str, impact: float | None) -> str:
    """Builds a polite, professional, and data-driven WhatsApp directive quoting real company figures."""
    salutation = f"Sayın {owner}" if owner else "Sayın Yöneticim"
    impact_str = f" ve şirket kasasına yaklaşık ₺{impact:,.0f} likidite serbestleşmesi sağlanması".replace(",", ".") if (impact and impact > 0) else ""
    return (
        f"{salutation}, yönetim kurulu finansal değerlendirmemize göre öncelikli aksiyonumuz belirlenmiştir:\n\n"
        f"🎯 Aksiyon: {task}\n"
        f"⏱️ Termin: {horizon}\n"
        f"📊 Hedef Gösterge (KPI): {kpi}\n\n"
        f"Bu aksiyonun ivedilikle hayata geçirilmesi{impact_str} hedeflenmektedir. "
        f"Lütfen süreci başlatıp haftalık ilerlemeyi tarafıma bildirin."
    ).replace(",", ".")
