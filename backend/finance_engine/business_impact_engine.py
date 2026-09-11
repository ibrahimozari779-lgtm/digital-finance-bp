from __future__ import annotations

from typing import Any


def _exposure_for_finding(code: str, statements: dict[str, Any]) -> tuple[float | None, str, str | None]:
    """Return (estimated exposure in currency, basis explanation, driver_key) for a finding code.

    Every exposure is derived directly from statement figures - this is a
    scenario/order-of-magnitude number, not an audited loss estimate.

    driver_key identifies the underlying statement figure the exposure is
    computed from (e.g. "financial_debt", "receivables"). Several finding
    codes describe the same underlying balance from different angles (e.g.
    L002 "leverage vs equity" and D004 "leverage vs assets" are both driven
    by financial_debt) - the driver_key lets the caller de-duplicate before
    summing so a single balance isn't counted as risk exposure twice.
    """
    pl = statements["profit_and_loss"]
    bs = statements["balance_sheet"]
    k = statements["kpis"]

    net_sales = float(pl.get("Net sales") or 0.0)
    operating_margin = k.get("operating_margin_pct")
    operating_profit = float(pl.get("Operating profit") or 0.0)
    finance_costs = float(pl.get("Finance costs") or 0.0)
    financial_debt = float(k.get("financial_debt") or 0.0)
    net_debt = float(k.get("net_debt") or 0.0)
    receivables = float(k.get("receivables") or 0.0)
    current_assets = float(bs.get("Current assets") or 0.0)
    current_liabilities = float(bs.get("Current liabilities") or 0.0)
    total_equity = float(bs.get("Total equity incl. current result") or 0.0)
    non_core_income = float(pl.get("Other operating income") or 0.0) + float(pl.get("Other non-operating income") or 0.0)

    if code in ("P001", "P002"):
        if operating_margin is not None and net_sales:
            healthy_margin = 12.0
            gap_pp = healthy_margin - operating_margin
            if gap_pp > 0:
                return gap_pp / 100 * net_sales, "Genel sağlıklı faaliyet marjı referansı (%12) ile aradaki farkın satışlara uygulanması", "margin_gap"
        return None, "", None
    if code == "P003":
        return None, "", None
    if code == "L001":
        return finance_costs, "Yıllık finansman gideri tutarı", "finance_costs"
    if code == "L002":
        return financial_debt, "Refinansman/faiz duyarlılığına açık finansal borç tutarı", "financial_debt"
    if code in ("Q001", "Q002"):
        gap = current_liabilities - current_assets
        if gap > 0:
            return gap, "Kısa vadeli yükümlülüklerin dönen varlıkları aşan kısmı", "liquidity_gap"
        return None, "", None
    if code == "Q003":
        return max(net_debt, 0.0), "Net borç tutarı (nakit sonrası)", "net_debt"
    if code in ("W001", "WC004"):
        return receivables, "Bilanço tarihi itibarıyla tahsil edilmemiş ticari alacak tutarı", "receivables"
    if code == "E001":
        return non_core_income, "Kâra katkı sağlayan faaliyet dışı/ikincil gelir tutarı", "non_core_income"
    if code in ("D004", "D005"):
        return financial_debt, "Varlık tabanını finanse eden borç tutarı", "financial_debt"
    if code in ("D006", "D007"):
        return finance_costs, "Faiz karşılama riski altındaki yıllık finansman gideri", "finance_costs"
    if code == "D008":
        return abs(total_equity), "Negatif özkaynak tutarı", "negative_equity"
    return None, "", None


def build_business_impact(statements: dict[str, Any], findings: list[dict[str, Any]], opportunities: list[dict[str, Any]]) -> dict[str, Any]:
    """Business Impact Engine.

    Quantifies each risk finding in currency terms where the statements
    support a defensible calculation, and rolls both risk exposure and
    opportunity value up into comparable summaries so a business partner
    can talk about "how much is at stake", not just "what is wrong".

    Because several finding rules can key off the same underlying balance
    (e.g. financial debt drives both the "leverage vs equity" and "leverage
    vs assets" findings), a naive sum of every finding's exposure double-
    counts that balance. This engine reports both numbers explicitly:
    - total_quantifiable_risk_exposure: the plain sum across all findings
      (upper-bound, may contain overlap) - kept for continuity.
    - total_quantifiable_risk_exposure_unique: the same findings summed
      after de-duplicating by underlying driver (each distinct balance
      counted once, at its largest cited exposure) - the more defensible
      "how much is really at stake" figure.
    """
    findings_impact: list[dict[str, Any]] = []
    total_risk_exposure = 0.0
    exposure_by_driver: dict[str, float] = {}
    for f in findings:
        if f["severity"] == "positive":
            continue
        exposure, basis, driver_key = _exposure_for_finding(f["code"], statements)
        findings_impact.append({
            "code": f["code"],
            "title": f["title"],
            "severity": f["severity"],
            "category": f["category"],
            "estimated_exposure": exposure,
            "basis": basis or "Bu bulgu için doğrudan bir para birimi etkisi türetilemedi.",
            "driver_key": driver_key,
        })
        if exposure is not None:
            total_risk_exposure += exposure
            if driver_key is not None:
                exposure_by_driver[driver_key] = max(exposure_by_driver.get(driver_key, 0.0), exposure)

    total_risk_exposure_unique = sum(exposure_by_driver.values())
    overlap_amount = round(total_risk_exposure - total_risk_exposure_unique, 2)

    total_opportunity_value = sum(o["estimated_impact"] for o in opportunities)

    net_sales = float(statements["profit_and_loss"].get("Net sales") or 0.0)
    exposure_to_sales_pct = round(total_risk_exposure / net_sales * 100, 1) if net_sales else None
    exposure_unique_to_sales_pct = round(total_risk_exposure_unique / net_sales * 100, 1) if net_sales else None
    opportunity_to_sales_pct = round(total_opportunity_value / net_sales * 100, 1) if net_sales else None

    findings_impact_sorted = sorted(
        findings_impact,
        key=lambda x: (x["estimated_exposure"] if x["estimated_exposure"] is not None else -1),
        reverse=True,
    )

    return {
        "findings_impact": findings_impact_sorted,
        "total_quantifiable_risk_exposure": round(total_risk_exposure, 2),
        "total_quantifiable_risk_exposure_unique": round(total_risk_exposure_unique, 2),
        "overlap_amount": overlap_amount,
        "total_opportunity_value": round(total_opportunity_value, 2),
        "risk_exposure_to_net_sales_pct": exposure_to_sales_pct,
        "risk_exposure_unique_to_net_sales_pct": exposure_unique_to_sales_pct,
        "opportunity_value_to_net_sales_pct": opportunity_to_sales_pct,
        "note": (
            "İki toplam raporlanır: 'Toplam Risk Büyüklüğü' bulgu bazında ham toplamdır ve aynı bilanço "
            "kalemi (ör. finansal borç, ticari alacak) birden fazla bulguda referans alındığında çift sayılabilir. "
            "'Tekilleştirilmiş Risk Büyüklüğü' aynı kalemi yalnızca bir kez sayarak hesaplanır ve gerçek risk "
            "büyüklüğüne daha yakın bir göstergedir. Her iki tutar da farklı varsayım tabanlarına dayandığından "
            "fırsat toplamından doğrudan düşülerek 'net etki' olarak yorumlanmamalıdır."
        ),
    }
