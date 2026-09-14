from __future__ import annotations
from typing import Any


def build_core_metrics(
    statements: dict[str, Any],
    quality: dict[str, Any],
    ccc: dict[str, Any],
    health_score: float,
    health_label: str,
    data_hub: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Single Source of Truth (SSOT) Core Metrics Layer.

    Computes and canonicalizes all top-level financial metrics once so that every
    UI card, root cause card, executive summary, trend module, and PDF board deck
    reads the exact same figures, sources, and rounding.
    """
    pl = statements.get("profit_and_loss", {})
    bs = statements.get("balance_sheet", {})
    k = statements.get("kpis", {})

    net_sales = float(pl.get("Net sales") or 0.0)
    gross_profit = float(pl.get("Gross profit") or 0.0)
    operating_profit = float(pl.get("Operating profit") or 0.0)
    net_profit = float(pl.get("Net profit") or 0.0)

    gross_margin_pct = float(k.get("gross_margin_pct") or ((gross_profit / net_sales * 100) if net_sales else 0.0))
    operating_margin_pct = float(k.get("operating_margin_pct") or ((operating_profit / net_sales * 100) if net_sales else 0.0))
    net_margin_pct = float(k.get("net_margin_pct") or ((net_profit / net_sales * 100) if net_sales else 0.0))

    # Working Capital / CCC Single Source of Truth
    dso_days = ccc.get("dso_days")
    dio_days = ccc.get("dio_days")
    dpo_days = ccc.get("dpo_days")
    ccc_days = ccc.get("cash_conversion_cycle_days")
    cash_tied_up = ccc.get("estimated_cash_tied_up")

    # Multi-source / Subledger figures
    analysis_sales = (data_hub or {}).get("analysis_sales") or {}
    sales_gross = float(analysis_sales.get("gross_sales") or analysis_sales.get("gross_or_revenue") or 0.0)

    analysis_ar = (data_hub or {}).get("analysis_ar") or (data_hub or {}).get("ar_aging") or {}
    subledger_ar_dso = analysis_ar.get("dso_days") or analysis_ar.get("weighted_dso")
    subledger_ar_outstanding = analysis_ar.get("outstanding")

    analysis_ap = (data_hub or {}).get("analysis_ap") or (data_hub or {}).get("ap_aging") or {}
    subledger_ap_dpo = analysis_ap.get("dpo_days") or analysis_ap.get("weighted_dpo")
    subledger_ap_outstanding = analysis_ap.get("outstanding")

    # Cross-source Reconciliation Status
    reconciliation = (data_hub or {}).get("reconciliation") or {}
    checks = reconciliation.get("checks") or []
    material_mismatches = [c for c in checks if c.get("status") == "material_difference"]
    has_reconciliation_gap = len(material_mismatches) > 0 or (
        subledger_ar_dso is not None and dso_days is not None and abs(float(subledger_ar_dso) - float(dso_days)) > 2.0
    )

    # Data Trust & Conditional Health Score
    data_trust_score = float(quality.get("score") or 100.0)
    data_trust_status = quality.get("status", "Trusted")
    is_conditional_score = has_reconciliation_gap or (data_trust_score < 75.0)

    conditional_badge = None
    if is_conditional_score:
        diff_detail = ""
        ar_check = next((c for c in checks if "Receivables" in c.get("name", "")), None)
        if ar_check and ar_check.get("difference_pct") is not None:
            diff_detail = f"%{abs(ar_check['difference_pct']):.1f} Alt Defter Farkı"
        conditional_badge = {
            "is_conditional": True,
            "status_label": "Şartlı Skor (Veri Doğrulaması Bekleniyor)",
            "warning_text": (
                f"Bu sağlık skoru {diff_detail or 'alt defter mutabakat farkı'} içeren verilere dayanmaktadır. "
                "Mizan ve alt defter denkliği teyit edilene kadar finansal sağlık skoru şartlı değerlendirilmelidir."
            ),
            "data_trust_score": data_trust_score,
        }

    return {
        # 1. Canonical Income Statement
        "canonical_net_sales": round(net_sales, 2),
        "net_sales": round(net_sales, 2),
        "gross_profit": round(gross_profit, 2),
        "operating_profit": round(operating_profit, 2),
        "net_profit": round(net_profit, 2),
        "gross_margin_pct": round(gross_margin_pct, 1),
        "operating_margin_pct": round(operating_margin_pct, 1),
        "net_margin_pct": round(net_margin_pct, 1),

        # 2. Canonical Working Capital & Cash Conversion Cycle
        "canonical_dso_days": round(dso_days, 1) if dso_days is not None else None,
        "dso_days": round(dso_days, 1) if dso_days is not None else None,
        "dio_days": round(dio_days, 1) if dio_days is not None else None,
        "dpo_days": round(dpo_days, 1) if dpo_days is not None else None,
        "canonical_ccc_days": round(ccc_days, 1) if ccc_days is not None else None,
        "ccc_days": round(ccc_days, 1) if ccc_days is not None else None,
        "estimated_cash_tied_up": round(cash_tied_up, 2) if cash_tied_up is not None else None,

        # 3. Source Attribution & Multi-source Mapping
        "dso_source": "mizan_120",
        "dso_source_label": "Mizan 120 (Resmi Muhasebe)",
        "subledger_ar_dso_days": round(float(subledger_ar_dso), 1) if subledger_ar_dso is not None else None,
        "subledger_ar_source_label": "AR Yaşlandırma Defteri (Açık Faturalar)",
        "subledger_ar_outstanding": round(float(subledger_ar_outstanding), 2) if subledger_ar_outstanding is not None else None,

        "sales_ledger_gross_sales": round(sales_gross, 2) if sales_gross else None,
        "sales_ledger_source_label": "Satış Defteri (Brüt İşlem Toplamı)",

        # 4. Scores & Trust
        "health_score": round(health_score, 1),
        "health_label": (health_label + " (Şartlı)") if is_conditional_score else health_label,
        "raw_health_label": health_label,
        "data_trust_score": round(data_trust_score, 1),
        "data_trust_status": data_trust_status,
        "is_conditional_score": is_conditional_score,
        "conditional_badge": conditional_badge,

        # 5. Two-Layer Audit Status
        "audit_layer_a_internal_equation": quality.get("internal_consistency_status", "Trusted"),
        "audit_layer_b_subledger_reconciliation": "review" if has_reconciliation_gap else "matched",
    }
