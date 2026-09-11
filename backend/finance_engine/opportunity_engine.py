from __future__ import annotations

from typing import Any


def _safe_div(a: float | None, b: float | None) -> float | None:
    if a is None or b in (None, 0):
        return None
    return float(a) / float(b)


def _band(value: float | None, bands: list[tuple[float, float]], default: float) -> float:
    """Pick the first (threshold, result) pair whose threshold the value clears.

    `bands` must be sorted with the highest threshold first. See scenario_engine's
    identical helper for the same rationale: the assumed magnitude should reflect
    how far this company's own ratio sits from a healthy range today, not a fixed
    percentage applied regardless of financial state.
    """
    if value is None:
        return default
    for threshold, result in bands:
        if value >= threshold:
            return result
    return default


def build_opportunities(statements: dict[str, Any]) -> list[dict[str, Any]]:
    """Opportunity Engine.

    Produces deterministic, formula-backed scenario opportunities from the
    canonical financial model. Every opportunity carries its calculation and
    the assumption behind it so it can be defended to a CFO. No opportunity
    is invented without a supporting statement figure.

    NOTE: O001, O002 and O003 formulas are frozen for backward compatibility
    with existing regression tests (test_business_partner_engine.py) - do
    not change their arithmetic. O004-O006 scale their target percentage with
    the company's own current ratio (inventory/opex intensity vs. sales,
    liquidity pressure) the same way the Scenario Lab does, instead of using a
    single fixed percentage for every company regardless of its actual state.
    """
    pl = statements["profit_and_loss"]
    k = statements["kpis"]

    net_sales = float(pl.get("Net sales") or 0.0)
    net_profit = float(pl.get("Net profit") or 0.0)
    opex = float(pl.get("Operating expenses") or 0.0)
    finance_costs = float(pl.get("Finance costs") or 0.0)
    financial_debt = float(k.get("financial_debt") or 0.0)
    receivables = float(k.get("receivables") or 0.0)
    inventory = float(k.get("inventory") or 0.0)
    payables = float(k.get("payables") or 0.0)
    current_ratio = k.get("current_ratio")

    opportunities: list[dict[str, Any]] = []

    if net_sales > 0:
        margin_1pp = net_sales * 0.01
        opportunities.append({
            "code": "O001", "title": "Brüt marjı 1 puan iyileştirme", "area": "Kârlılık",
            "estimated_impact": margin_1pp, "impact_type": "annual_profit_if_period_is_annual",
            "calculation": "Net sales × 1%",
            "assumption": "Satış hacmi ve faaliyet giderleri sabit kabul edilir.",
        })

    if finance_costs > 0 and financial_debt > 0:
        effective_rate = finance_costs / financial_debt
        debt_reduction = financial_debt * 0.10
        saving = debt_reduction * effective_rate
        opportunities.append({
            "code": "O002", "title": "Finansal borcu %10 azaltma", "area": "Finansman",
            "estimated_impact": saving, "impact_type": "finance_cost_saving_proxy",
            "calculation": "Debt × 10% × observed finance-cost/debt ratio",
            "assumption": "Mevcut finansman gideri/borç oranının korunacağı ve giderlerin ağırlıkla finansal borca bağlı olduğu varsayılır.",
        })

    if receivables > 0:
        receivable_release_5pct = receivables * 0.05
        opportunities.append({
            "code": "O003", "title": "Ticari alacakları %5 azaltma", "area": "İşletme Sermayesi",
            "estimated_impact": receivable_release_5pct, "impact_type": "cash_release",
            "calculation": "Trade receivables × 5%",
            "assumption": "Aging verisi olmadan yalnızca senaryo amaçlı nakit serbestleşme potansiyelidir.",
        })

    if inventory > 0:
        inv_to_sales = _safe_div(inventory, net_sales)
        inv_pct = _band(inv_to_sales, [(0.35, 0.15), (0.20, 0.10)], 0.05)
        inventory_release = inventory * inv_pct
        opportunities.append({
            "code": "O004", "title": f"Stokları %{inv_pct*100:.0f} azaltma", "area": "İşletme Sermayesi",
            "estimated_impact": inventory_release, "impact_type": "cash_release",
            "calculation": f"Inventory × {inv_pct*100:.0f}%",
            "assumption": "Stok devir verisi olmadan yalnızca senaryo amaçlı nakit serbestleşme potansiyelidir.",
            "target_pct": inv_pct, "current_state": {"inventory_to_sales_pct": round(inv_to_sales*100,1) if inv_to_sales is not None else None},
        })

    if opex > 0:
        opex_to_sales = _safe_div(opex, net_sales)
        opex_pct = _band(opex_to_sales, [(0.30, 0.05), (0.15, 0.03)], 0.02)
        opex_saving = opex * opex_pct
        opportunities.append({
            "code": "O005", "title": f"Faaliyet giderlerini %{opex_pct*100:.0f} azaltma", "area": "Kârlılık",
            "estimated_impact": opex_saving, "impact_type": "annual_profit_if_period_is_annual",
            "calculation": f"Operating expenses × {opex_pct*100:.0f}%",
            "assumption": "Gider kaleminin bir kısmının hacimden bağımsız (yönetilebilir) olduğu varsayılır.",
            "target_pct": opex_pct, "current_state": {"opex_to_sales_pct": round(opex_to_sales*100,1) if opex_to_sales is not None else None},
        })

    if payables > 0:
        pay_pct = _band((-current_ratio if current_ratio is not None else None), [(-1.0, 0.20), (-1.2, 0.15), (-1.5, 0.10)], 0.05)
        payable_extension = payables * pay_pct
        opportunities.append({
            "code": "O006", "title": f"Tedarikçi vadesini uzatarak nakit tutma (%{pay_pct*100:.0f})", "area": "İşletme Sermayesi",
            "estimated_impact": payable_extension, "impact_type": "cash_release",
            "calculation": f"Trade payables × {pay_pct*100:.0f}%",
            "assumption": "Tedarikçi koşullarının yeniden müzakere edilebileceği ve erken ödeme iskontosu kaybının ihmal edilebilir olduğu varsayılır.",
            "target_pct": pay_pct, "current_state": {"current_ratio": round(current_ratio,2) if current_ratio is not None else None},
        })

    for o in opportunities:
        o.setdefault("target_pct", None)
        o.setdefault("current_state", None)
        o["pct_of_net_sales"] = round(o["estimated_impact"] / net_sales * 100, 2) if net_sales else None
        o["pct_of_net_profit"] = round(o["estimated_impact"] / net_profit * 100, 2) if net_profit else None

    opportunities_sorted = sorted(opportunities, key=lambda x: x["estimated_impact"], reverse=True)
    for i, o in enumerate(opportunities_sorted, start=1):
        o["rank"] = i

    return opportunities_sorted
