from __future__ import annotations

import re
from typing import Any

_SEVERITY_WEIGHT = {"critical": 100.0, "high": 70.0, "medium": 40.0, "low": 15.0}
_CONFIDENCE_WEIGHT = {"high": 1.0, "medium": 0.8, "low": 0.6}
_SEVERITY_RANK = {"critical": 4, "high": 3, "medium": 2, "low": 1}

# Categories whose findings routinely fire together for the same underlying
# condition (e.g. a highly-leveraged company trips L002 "kaldıraç yüksek",
# D004/D005 "borç yükü" and D006/D007 "faiz karşılama" all at once). Grouping
# them under one umbrella key mirrors the consolidation already used by the
# Management Actions engine, and is what prevents the priority risk list from
# showing several near-identical "reduce your debt" entries back to back.
_UMBRELLA_CATEGORY = {
    "Borçluluk": "Borçluluk / Sermaye Yapısı",
    "Likidite": "Likidite",
    "İşletme Sermayesi": "İşletme Sermayesi",
}


def _tier(score: float) -> str:
    if score >= 85:
        return "Kritik"
    if score >= 55:
        return "Yüksek"
    if score >= 25:
        return "Orta"
    return "Düşük"


def _norm_text(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def build_risk_ranking(
    findings: list[dict[str, Any]],
    business_impact: dict[str, Any],
    statements: dict[str, Any],
) -> dict[str, Any]:
    """Risk Ranking Engine.

    Produces a single composite risk score per *risk theme* by combining
    severity, confidence, and financial exposure (when quantifiable), so
    findings from different categories (liquidity, leverage, profitability,
    working capital) can be compared on one prioritized list instead of
    only being grouped by severity label.

    Findings are first consolidated by risk theme (see `_UMBRELLA_CATEGORY`,
    and exact-duplicate recommendation text within any category) so that
    several rules tripping on the same underlying condition produce ONE
    prioritized entry with combined evidence and de-duplicated recommendation
    text, instead of a handful of near-identical entries competing for the
    top ranking slots.
    """
    net_sales = float(statements["profit_and_loss"].get("Net sales") or 0.0)
    exposure_by_code = {
        x["code"]: x["estimated_exposure"]
        for x in business_impact.get("findings_impact", [])
    }

    strengths: list[dict[str, Any]] = []
    actionable = []
    for f in findings:
        if f["severity"] == "positive":
            strengths.append({"code": f["code"], "title": f["title"], "category": f["category"]})
            continue
        actionable.append(f)

    # Group by umbrella theme when one applies, otherwise by (category, normalized
    # recommendation) so that unrelated findings in the same category that genuinely
    # give different advice are NOT forced together, while two findings that would
    # literally repeat the same recommendation are.
    groups: dict[Any, list[dict[str, Any]]] = {}
    for f in actionable:
        theme = _UMBRELLA_CATEGORY.get(f["category"])
        key = theme if theme else (f["category"], _norm_text(f["recommendation"]))
        groups.setdefault(key, []).append(f)

    ranked: list[dict[str, Any]] = []
    for key, items in groups.items():
        items_sorted = sorted(
            items,
            key=lambda x: (_SEVERITY_RANK.get(x["severity"], 0), _CONFIDENCE_WEIGHT.get(x["confidence"], 0.7)),
            reverse=True,
        )
        anchor = items_sorted[0]
        base = _SEVERITY_WEIGHT.get(anchor["severity"], 10.0) * _CONFIDENCE_WEIGHT.get(anchor["confidence"], 0.7)

        exposures = [exposure_by_code[x["code"]] for x in items if exposure_by_code.get(x["code"]) is not None]
        exposure = max(exposures) if exposures else None
        impact_bonus = 0.0
        if exposure is not None and net_sales:
            ratio = exposure / net_sales
            # Asymptotic (never fully saturating) scaling: 20 * ratio/(1+ratio).
            # This still rewards a bigger exposure-to-sales ratio, but keeps
            # discriminating between e.g. 100% and 500% of net sales instead
            # of both hitting the same hard cap.
            impact_bonus = 20.0 * (ratio / (1.0 + ratio))
        # Multiple independent findings corroborating the same risk theme raise
        # confidence in the signal, but should never let a pile of low-severity
        # findings out-rank one genuinely critical, isolated finding - hence the
        # small cap.
        corroboration_bonus = min(6.0, (len(items) - 1) * 2.0)
        score = round(min(100.0, base * 0.85 + impact_bonus + corroboration_bonus), 1)

        evidence: list[str] = []
        seen_evidence: set[str] = set()
        for x in items_sorted:
            for e in x.get("evidence", []):
                k = _norm_text(e)
                if k and k not in seen_evidence:
                    seen_evidence.add(k)
                    evidence.append(e)

        recommendations: list[str] = []
        seen_rec: set[str] = set()
        for x in items_sorted:
            k = _norm_text(x["recommendation"])
            if k and k not in seen_rec:
                seen_rec.add(k)
                recommendations.append(x["recommendation"])

        title = anchor["title"] if len(items) == 1 else f"{anchor['title']} (+{len(items) - 1} ilişkili bulgu)"

        ranked.append({
            "code": anchor["code"],
            "contributing_codes": [x["code"] for x in items_sorted],
            "title": title,
            "category": anchor["category"],
            "severity": anchor["severity"],
            "confidence": anchor["confidence"],
            "estimated_exposure": exposure,
            "evidence": evidence,
            "risk_score": score,
            "risk_tier": _tier(score),
            # Kept as a single string for backward compatibility with existing
            # consumers; distinct, de-duplicated recommendations are joined with
            # numbering instead of being repeated as separate top-level entries.
            "recommendation": recommendations[0] if len(recommendations) == 1 else " ".join(
                f"{i}) {r}" for i, r in enumerate(recommendations, start=1)
            ),
        })

    ranked_sorted = sorted(ranked, key=lambda x: x["risk_score"], reverse=True)
    for i, r in enumerate(ranked_sorted, start=1):
        r["rank"] = i

    return {
        "ranked_risks": ranked_sorted,
        "top_3": ranked_sorted[:3],
        "strengths": strengths,
        "methodology": "Risk skoru = (şiddet ağırlığı × güven ağırlığı) × 0.85 + (parasal etki / net satışlar oranına göre 0-20 arası asimptotik bonus, ör. oran %100'de ~10 puan, %500'de ~17 puan) + (aynı risk temasını doğrulayan ek bulgu başına +2, en fazla +6 puan). Aynı temadaki veya birebir aynı öneriyi taşıyan bulgular tek bir kalemde birleştirilir; bu nedenle listede mükerrer öneri görünmez. 0-100 ölçeğinde, 100 en yüksek öncelik.",
    }
