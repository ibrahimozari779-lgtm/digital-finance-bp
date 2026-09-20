"""Cash Flow & 13-Week Dynamic Liquidity Projection Engine (Nakit Akışı & 13 Haftalık Karar Motoru).

Calculates:
1. TMS 7 Indirect Cash Flow Statement (İşletme, Yatırım, Finansman Nakit Akışları ve Kasa Mutabakatı).
2. 13-Week Rolling Cash Flow Projection (Haftalık nakit akış seyri, nakit açığı riski, deficit week tespiti).
3. Patron Karar Kokpiti: "Para nerede? → Sorun ne? → Kaç TL? → Bu hafta ne yapmalıyım?" ve WhatsApp talimatları.
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
) -> dict[str, Any]:
    """Generates standard TMS 7 indirect cash flow, 13-week forecast, and executive actions."""
    kpis = statements.get("kpis", {})
    pl = statements.get("profit_and_loss", {})
    bs = statements.get("balance_sheet", {})

    # 1. Base Variables
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
    total_equity = _safe_float(bs.get("Total equity incl. current result"))

    # Working capital metrics (DSO, DPO, DIO)
    ccc_dict = ccc or statements.get("cash_conversion_cycle") or {}
    dso = _safe_float(ccc_dict.get("dso_days") or ccc_dict.get("dso"), 60.0)
    dpo = _safe_float(ccc_dict.get("dpo_days") or ccc_dict.get("dpo"), 45.0)
    dio = _safe_float(ccc_dict.get("dio_days") or ccc_dict.get("dio"), 60.0)

    # Multi-source Subledger (AR / AP aging) overrides
    analysis_ar = (data_hub or {}).get("analysis_ar") or (data_hub or {}).get("ar_aging") or {}
    analysis_ap = (data_hub or {}).get("analysis_ap") or (data_hub or {}).get("ap_aging") or {}
    overdue_ar = _safe_float(analysis_ar.get("overdue") or analysis_ar.get("overdue_total"))
    overdue_ap = _safe_float(analysis_ap.get("overdue") or analysis_ap.get("overdue_total"))

    # =========================================================================
    # A) TMS 7 Indirect Cash Flow Statement
    # =========================================================================
    has_prior = previous_statement is not None
    if has_prior:
        pk = previous_statement.get("kpis", {})
        pbs = previous_statement.get("balance_sheet", {})
        ppl = previous_statement.get("profit_and_loss", {})

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
    else:
        # Single-period heuristic (management proxy based on cumulative balances and turnover)
        opening_cash_tms7 = max(0.0, cash - (operating_profit * 0.2))
        delta_rec = -min(receivables * 0.25, net_sales * (dso / 365.0) * 0.3)
        delta_inv = -min(inventory * 0.20, cogs * (dio / 365.0) * 0.25)
        delta_pay = min(payables * 0.20, cogs * (dpo / 365.0) * 0.25)
        delta_debt = financial_debt * 0.15
        delta_capex = -max(0.0, noncurrent_assets * 0.05)

    # 1. Operating Cash Flow
    # Add back non-cash and financing expenses
    depreciation_est = noncurrent_assets * 0.05 if noncurrent_assets > 0 else (opex * 0.08)
    wc_change_total = delta_rec + delta_inv + delta_pay
    operating_cf = net_profit + depreciation_est + finance_costs + wc_change_total

    # 2. Investing Cash Flow
    investing_cf = delta_capex

    # 3. Financing Cash Flow
    financing_cf = delta_debt - finance_costs

    net_cash_flow_tms7 = operating_cf + investing_cf + financing_cf
    closing_cash_tms7 = opening_cash_tms7 + net_cash_flow_tms7
    reconciliation_diff = round(cash - closing_cash_tms7, 2) if has_prior else 0.0

    tms7_statement = {
        "is_two_period": has_prior,
        "mode": "TMS 7 Dolaylı Nakit Akış Tablosu",
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
            "closing_cash": round(cash, 2),
            "reconciliation_difference": reconciliation_diff,
        },
    }

    # =========================================================================
    # B) 13-Week Rolling Cash Flow Projection (13 Haftalık Dinamik Projeksiyon)
    # =========================================================================
    # Weekly run rates:
    monthly_sales = net_sales / 12.0 if net_sales > 0 else (receivables * 1.5)
    weekly_base_sales = monthly_sales / 4.33

    monthly_cogs = cogs / 12.0 if cogs > 0 else (monthly_sales * 0.70)
    weekly_supplier_burn = monthly_cogs / 4.33

    monthly_opex = opex / 12.0 if opex > 0 else (monthly_sales * 0.15)
    weekly_payroll_opex = monthly_opex / 4.33

    monthly_finance = finance_costs / 12.0 if finance_costs > 0 else (financial_debt * 0.45 / 12.0)
    weekly_finance_service = monthly_finance / 4.33

    # Minimum safety liquidity buffer (e.g. 1.5 weeks of operational burn)
    weekly_total_burn = weekly_supplier_burn + weekly_payroll_opex + weekly_finance_service
    min_safety_buffer = max(50_000.0, weekly_total_burn * 1.5)

    weeks_projection = []
    running_cash = cash
    deficit_weeks = []
    lowest_cash_point = cash
    lowest_week = 1

    # Overdue AR recovery pool:
    uncollected_overdue = overdue_ar if overdue_ar > 0 else (receivables * 0.35)

    for w in range(1, 14):
        # 1. Inflows:
        collection_factor = 1.0
        if w in (1, 2):
            collection_factor = 0.85  # Beginning of month lag
        elif w in (3, 4, 7, 8, 11, 12):
            collection_factor = 1.10  # Mid/end-month collection peak

        base_collection = weekly_base_sales * collection_factor
        overdue_recovery_weekly = (uncollected_overdue * 0.05) if w > 2 else (uncollected_overdue * 0.02)
        total_inflows = base_collection + overdue_recovery_weekly

        # 2. Outflows:
        # Supplier payments
        supp_multiplier = 1.30 if (w % 4 == 2) else 0.90
        supp_outflow = weekly_supplier_burn * supp_multiplier

        # Payroll & SGK: peaks on weeks 4, 8, 12
        if w in (4, 8, 12):
            payroll_outflow = weekly_payroll_opex * 2.2
            tax_outflow = max(20_000.0, (tax_expense / 12.0) * 1.2 if tax_expense > 0 else monthly_sales * 0.03)
        else:
            payroll_outflow = weekly_payroll_opex * 0.6
            tax_outflow = 0.0

        # Debt / Interest Service:
        if w in (4, 8, 12):
            debt_outflow = weekly_finance_service * 2.5
        else:
            debt_outflow = weekly_finance_service * 0.5

        total_outflows = supp_outflow + payroll_outflow + tax_outflow + debt_outflow

        # Net change & ending cash
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

    # Runway calculation
    runway_weeks = 13.0
    if deficit_weeks:
        first_deficit = deficit_weeks[0]
        runway_weeks = float(first_deficit - 1)
    elif weekly_total_burn > 0:
        runway_weeks = round(cash / weekly_total_burn, 1)

    # =========================================================================
    # C) Patron Karar Kokpiti & Yönetici Yorum Motoru (Executive Interpretation)
    # =========================================================================
    total_operating_capital = cash + receivables + inventory
    cash_pct = round((cash / total_operating_capital) * 100, 1) if total_operating_capital > 0 else 0.0
    rec_pct = round((receivables / total_operating_capital) * 100, 1) if total_operating_capital > 0 else 0.0
    inv_pct = round((inventory / total_operating_capital) * 100, 1) if total_operating_capital > 0 else 0.0

    where_is_the_money = {
        "cash_amount": cash,
        "cash_pct": cash_pct,
        "receivables_amount": receivables,
        "receivables_pct": rec_pct,
        "inventory_amount": inventory,
        "inventory_pct": inv_pct,
        "payables_amount": payables,
        "net_working_capital": round(receivables + inventory - payables, 2),
        "headline": (
            f"Kasadaki sıcak para yalnızca ₺{cash:,.0f} (%{cash_pct}); "
            f"şirketin sermayesinin %{rec_pct + inv_pct:.0f}'i "
            f"(₺{receivables + inventory:,.0f}) müşteri senetlerinde ve depoda kilitli."
        ).replace(",", "."),
    }

    anomalies = []
    if dso > dpo:
        gap_days = round(dso - dpo)
        gap_exposure = round(net_sales * (gap_days / 365.0), 2) if net_sales > 0 else round(receivables * 0.3, 2)
        anomalies.append({
            "code": "ALM-VADE-MAKASI",
            "title": f"Vade Makası Açık ({gap_days} Gün Açık)",
            "description": f"Tedarikçiye ortalama {dpo:.0f} günde öderken, müşteriden {dso:.0f} günde tahsil ediyorsunuz. Şirket {gap_days} gün boyunca müşterilerini finanse etmek için kredi kullanmak zorunda kalıyor.",
            "exposure_tl": gap_exposure,
            "severity": "critical" if gap_days > 30 else "warning",
        })

    if deficit_weeks:
        first_def = deficit_weeks[0]
        deepest_deficit = abs(min(0.0, lowest_cash_point))
        anomalies.append({
            "code": "ALM-NAKIT-ACIGI",
            "title": f"{first_def}. Haftada Kasa Açığı Riski (-₺{deepest_deficit:,.0f})".replace(",", "."),
            "description": f"Önümüzdeki 13 haftalık projeksiyonda; maaş, SGK, vergi ve tedarikçi ödemelerinin kümelendiği {first_def}. haftada kasanız eksiye düşüyor.",
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

    if finance_costs > 0 and operating_profit > 0:
        fin_to_op = (finance_costs / operating_profit) * 100
        if fin_to_op > 20:
            anomalies.append({
                "code": "ALM-FAIZ-BASKISI",
                "title": f"Faiz Baskısı: Kârın %{fin_to_op:.0f}'i Bankaya Gidiyor",
                "description": f"Faaliyet kârınızın (₺{operating_profit:,.0f}) yaklaşık ₺{finance_costs:,.0f} tutarındaki kısmı kredi ve finansman faizlerine eriyor.",
                "exposure_tl": finance_costs,
                "severity": "critical" if fin_to_op > 40 else "warning",
            })

    actions = []
    ar_target = round(min(receivables * 0.25, overdue_ar if overdue_ar > 0 else receivables * 0.20), 2)
    actions.append({
        "id": "ACT-1",
        "task": "İlk 5 Büyük Müşteriden Vadeli Çek Yerine DBS veya Erken Tahsilat İskontosu Talep Et",
        "owner": "Satış & Finans Direktörü",
        "deadline": "15 Gün",
        "kpi": f"DSO'yu {dso:.0f} günden {max(30, dso - 15):.0f} güne çekmek",
        "cash_impact_tl": ar_target,
        "whatsapp_template": (
            f"Sayın Satış Direktörüm, haftalık nakit projeksiyonumuza göre acil likidite sağlamamız gerekiyor. "
            f"İlk 5 büyük müşterimizle görüşerek en az ₺{ar_target:,.0f} tutarında erken tahsilat veya DBS limiti "
            f"sağlanmasını, vadesi geçen bakiyeler kapatılmadan yeni sevkiyat açılmamasını rica ederim."
        ).replace(",", "."),
    })

    ap_target = round(payables * 0.15, 2)
    actions.append({
        "id": "ACT-2",
        "task": "Kritik Tedarikçilerle Görüşüp Ödeme Vadelerini 15 Gün Genişlet (Vade Makasını Kapat)",
        "owner": "Satınalma & Mali İşler",
        "deadline": "20 Gün",
        "kpi": f"DPO'yu {dpo:.0f} günden {dpo + 15:.0f} güne çıkarmak",
        "cash_impact_tl": ap_target,
        "whatsapp_template": (
            f"Sayın Satınalma Müdürüm, tedarikçi ödeme vadelerimizi incelediğimizde müşteriye göre çok erken "
            f"ödeme yaptığımızı görüyoruz. Ana tedarikçilerimizle görüşerek ödeme takvimine +15 gün ilave "
            f"vade alınmasını ve kasadan çıkacak ₺{ap_target:,.0f} tutarın ertelenmesini sağlayalım."
        ).replace(",", "."),
    })

    inv_target = round(inventory * 0.15, 2)
    actions.append({
        "id": "ACT-3",
        "task": "Depoda 90 Günden Fazla Bekleyen Hareketsiz Stoklar İçin Hızlı Tasfiye / İskonto Kampanyası Başlat",
        "owner": "Pazarlama & Depo Yönetimi",
        "deadline": "30 Gün",
        "kpi": f"DIO'yu {dio:.0f} günden {max(30, dio - 18):.0f} güne indirmek",
        "cash_impact_tl": inv_target,
        "whatsapp_template": (
            f"Depo ve Satış Ekibine: Depomuzda uzun süredir bekleyen atıl stoklar her ay finansman faizi üretmektedir. "
            f"Bu hafta 90+ gün hareketsiz ürün listesini çıkarıp özel iskonto ile en az ₺{inv_target:,.0f} "
            f"tutarında stok tasfiyesini tamamlayalım."
        ).replace(",", "."),
    })

    total_unlockable_cash = ar_target + ap_target + inv_target

    patron_cockpit = {
        "where_is_the_money": where_is_the_money,
        "runway_weeks": runway_weeks,
        "lowest_cash_point": round(lowest_cash_point, 2),
        "lowest_week": lowest_week,
        "deficit_weeks": deficit_weeks,
        "min_safety_buffer": round(min_safety_buffer, 2),
        "anomalies": anomalies,
        "actions": actions,
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
