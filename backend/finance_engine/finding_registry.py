from __future__ import annotations

from typing import Any

# ---------------------------------------------------------------------------
# Master Finding Registry
# ---------------------------------------------------------------------------
# Problem this module solves:
#   Root Cause, Gap Detection, Risk Ranking, Business Impact and Action
#   engines were each free to describe the same underlying condition (e.g.
#   "receivables high relative to sales") under their own code and their own
#   wording. Business Impact / Risk Ranking / Action already key off the
#   Decision Engine's finding codes (P001, L001, W001, ...), so those three
#   were already implicitly linked. Gap Detection, however, independently
#   re-derives a handful of the exact same statement-level conditions under
#   its own GAP-* codes with the exact same thresholds, and the frontend
#   renders both the Findings list and the Gap Detection list as separate
#   report sections - so a CFO reading the PDF/report sees the same finding
#   twice under two different titles.
#
#   This module does not replace or rewrite any individual engine. It is a
#   thin consolidation layer that runs *after* all engines have produced
#   their own output:
#     1. Declares which GAP-* codes are exact statement-level duplicates of
#        an existing Decision Engine finding code (same metric, same
#        threshold family) - `DUPLICATE_GAP_TO_FINDING`.
#     2. Produces `master_findings`: one CFO-facing list where every
#        distinct underlying condition appears exactly once, annotated with
#        every engine that independently corroborates it.
#     3. Produces a de-duplicated view of Gap Detection's own `gaps` list
#        (duplicates removed, cross-referenced to the master finding they
#        are folded into) for use in the assembled report, WITHOUT mutating
#        or reducing the output of `build_gap_detection()` itself - other
#        callers/tests that need the full, un-consolidated gap list keep
#        getting it unchanged.
# ---------------------------------------------------------------------------

# gap_code -> master finding code it duplicates (same underlying metric).
# Keep this list to genuine 1:1 duplicates only. Gaps sourced from
# operational data (GAP-SALES-*, GAP-AR-*, GAP-AP-*, GAP-INV-*) are NOT
# duplicates of the statement-level findings - they carry evidence no other
# engine has (invoice/aging/inventory level detail) and must stay first-class.
DUPLICATE_GAP_TO_FINDING: dict[str, str] = {
    "GAP-CAP-01": "L002",   # sermaye yapısı / debt-to-equity  <-> Finansal kaldıraç yüksek
    "GAP-FIN-01": "L001",   # finansman maliyeti / op. kâr     <-> Finansman gider baskısı
    "GAP-LIQ-01": "Q002",   # current ratio                    <-> Likidite tamponu sınırlı
    "GAP-WC-01": "W001",    # alacak / satış                   <-> Alacak bakiyesi yüksek
    "GAP-PROF-01": "P003",  # brüt marj                        <-> Brüt marj sınırlı
}


# Extended (data-hub) root-cause chain code -> gap code it narrates the same
# underlying evidence as. Root Cause tells the causal story ("sales ->
# receivables -> cash"); Gap Detection raises the same evidence as a
# standalone weakness card. Both are useful, but showing the identical
# underlying number as a chain AND a separate card is the same duplication
# problem as the statement-level one above - so these fold the same way,
# with the gap kept as the canonical single mention (Root Cause is the
# narrative that explains it, referenced from the gap's `related_root_cause`).
DUPLICATE_EXTENDED_RC_TO_GAP: dict[str, str] = {
    "RC-OPS-CASH": "GAP-SALES-01",
    "RC-INV-CASH": "GAP-INV-01",
    "RC-AP-CASH": "GAP-AP-01",
}


# ---------------------------------------------------------------------------
# Sprint 1 extension: Opportunity + Action consolidation
# ---------------------------------------------------------------------------
# Problem: a finding like "Brüt marj sınırlı" (P003) was independently
# reachable as a Finding, a Risk Ranking entry, a Root Cause chain AND an
# Opportunity Engine lever (O001) AND a Management Action - five different
# report sections describing the exact same underlying condition with no
# link between them. Risk Ranking and Root Cause were already folded in
# above; this section closes the loop for Opportunity and Action so every
# master finding shows, in one place, "what it costs you" (impact),
# "what you could gain by fixing it" (opportunity) and "what to actually do"
# (action) - instead of the reader having to cross-reference three report
# sections by category name themselves.
#
# Opportunities don't carry a finding code (they are lever-based, not
# finding-based), so the link is by *category/area*, not by exact code
# match. `_CATEGORY_TO_OPPORTUNITY_AREAS` mirrors the same category
# normalization action_engine.py already uses for its own theme_aliases -
# kept in sync deliberately, not re-derived, so a finding and its action are
# never routed to a different opportunity area than the one used to justify
# the action's own KPI.
_CATEGORY_TO_OPPORTUNITY_AREAS: dict[str, list[str]] = {
    "Kârlılık": ["Kârlılık"],
    "Borçluluk": ["Finansman"],
    "Likidite": ["Finansman", "İşletme Sermayesi"],
    "İşletme Sermayesi": ["İşletme Sermayesi"],
    "Verimlilik": ["İşletme Sermayesi"],
    "Kazanç Kalitesi": ["Kârlılık"],
}

_CONFIDENCE_BASE = {"high": 80.0, "medium": 60.0, "low": 40.0}


def _linked_opportunities(category: str | None, opportunities: list[dict[str, Any]], limit: int = 2) -> list[dict[str, Any]]:
    areas = _CATEGORY_TO_OPPORTUNITY_AREAS.get(category or "", [])
    if not areas:
        return []
    matches = [o for o in opportunities if o.get("area") in areas]
    matches_sorted = sorted(matches, key=lambda o: o.get("estimated_impact") or 0.0, reverse=True)
    return [
        {
            "code": o.get("code"),
            "title": o.get("title"),
            "estimated_impact": o.get("estimated_impact"),
            "impact_type": o.get("impact_type"),
        }
        for o in matches_sorted[:limit]
    ]


def _linked_action(code: str | None, actions: list[dict[str, Any]]) -> dict[str, Any] | None:
    for a in actions:
        if a.get("finding_id") == code or code in (a.get("merged_finding_codes") or []):
            return {
                "action_id": a.get("action_id"),
                "action": a.get("action"),
                "owner": a.get("owner"),
                "time_horizon": a.get("time_horizon"),
                "expected_financial_impact": a.get("expected_financial_impact"),
            }
    return None


def _confidence_score(own_confidence: str | None, source_engine_count: int, has_opportunity: bool, has_action: bool) -> float:
    """Composite 0-100 confidence that combines this finding's own confidence
    label with how many independent engines corroborate the same underlying
    condition. More corroborating engines (Root Cause, Risk Ranking, Business
    Impact, Opportunity, Action all pointing at the same code) raises
    confidence that this is a real, actionable condition rather than a
    single rule tripping in isolation - but is capped so a pile of
    low-confidence corroboration can never out-score a single high-confidence,
    well-evidenced finding.
    """
    base = _CONFIDENCE_BASE.get(own_confidence or "medium", 50.0)
    corroboration_bonus = min(20.0, max(0, source_engine_count - 1) * 7.0)
    completeness_bonus = (5.0 if has_opportunity else 0.0) + (5.0 if has_action else 0.0)
    return round(min(100.0, base + corroboration_bonus + completeness_bonus), 1)


def build_finding_registry(
    findings: list[dict[str, Any]],
    gap_detection: dict[str, Any] | None,
    root_cause: dict[str, Any] | None,
    risk_ranking: dict[str, Any] | None,
    business_impact: dict[str, Any] | None,
    opportunities: list[dict[str, Any]] | None = None,
    management_actions: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Assemble the single, de-duplicated, cross-engine finding list.

    Every entry has a stable `id` (the Decision Engine finding code, or the
    gap code for operational findings that have no statement-level twin).
    `source_engines` lists every engine that independently produced or
    corroborated the same finding, so the registry is additive evidence,
    not a rewrite of any engine's own analysis.

    `opportunities` and `management_actions` are optional (both default to
    None / not linked) so existing callers that only pass the first five
    arguments keep working unchanged; passing them upgrades every entry with
    `linked_opportunities` + `linked_action` and a composite
    `confidence_score` (see Sprint 1 extension above).
    """
    gap_detection = gap_detection or {}
    root_cause = root_cause or {}
    risk_ranking = risk_ranking or {}
    business_impact = business_impact or {}
    opportunities = opportunities or []
    management_actions = management_actions or []

    all_gaps = gap_detection.get("gaps", []) or []
    gaps_by_code = {g.get("code"): g for g in all_gaps}

    # Which finding codes does Root Cause corroborate (via causal_chains.related_findings)?
    rc_codes_by_finding: dict[str, list[str]] = {}
    for chain in root_cause.get("causal_chains", []) or []:
        for code in chain.get("related_findings", []) or []:
            rc_codes_by_finding.setdefault(code, []).append(chain.get("code"))

    # Which finding codes does Risk Ranking corroborate (via contributing_codes)?
    risk_entry_by_finding: dict[str, dict[str, Any]] = {}
    for entry in risk_ranking.get("ranked_risks", []) or []:
        for code in entry.get("contributing_codes", [entry.get("code")]):
            risk_entry_by_finding[code] = entry

    # Which finding codes does Business Impact quantify?
    impact_by_finding: dict[str, dict[str, Any]] = {
        x.get("code"): x for x in business_impact.get("findings_impact", []) or []
    }

    duplicate_gap_codes = set(DUPLICATE_GAP_TO_FINDING.keys())

    # Extended root-cause chains only fold their matching gap when that
    # chain actually fired for this company (causal_chains only contains
    # chains supported by this period's evidence).
    rc_chain_codes_present = {c.get("code") for c in root_cause.get("causal_chains", []) or []}
    extended_duplicate_gap_codes = {
        gap_code for rc_code, gap_code in DUPLICATE_EXTENDED_RC_TO_GAP.items()
        if rc_code in rc_chain_codes_present
    }
    duplicate_gap_codes |= extended_duplicate_gap_codes

    master_findings: list[dict[str, Any]] = []
    duplicates_folded: list[dict[str, Any]] = []

    for rc_code, gap_code in DUPLICATE_EXTENDED_RC_TO_GAP.items():
        if gap_code in extended_duplicate_gap_codes and gap_code in gaps_by_code:
            duplicates_folded.append({
                "gap_code": gap_code,
                "folded_into": rc_code,
                "folded_into_engine": "root_cause_engine",
                "gap_title": gaps_by_code[gap_code].get("title"),
            })

    # 1) Decision Engine findings are the backbone of the registry.
    for f in findings:
        code = f.get("code")
        source_engines = ["decision_engine"]
        also_reported_as: list[dict[str, str]] = []

        # Fold in any gap that duplicates this exact finding.
        for gap_code, target_code in DUPLICATE_GAP_TO_FINDING.items():
            if target_code == code and gap_code in gaps_by_code:
                source_engines.append("gap_detection_engine")
                also_reported_as.append({"engine": "gap_detection_engine", "code": gap_code})
                duplicates_folded.append({
                    "gap_code": gap_code,
                    "folded_into": code,
                    "gap_title": gaps_by_code[gap_code].get("title"),
                })

        if code in rc_codes_by_finding:
            source_engines.append("root_cause_engine")
            for chain_code in rc_codes_by_finding[code]:
                also_reported_as.append({"engine": "root_cause_engine", "code": chain_code})

        if code in risk_entry_by_finding:
            source_engines.append("risk_ranking_engine")

        if code in impact_by_finding:
            source_engines.append("business_impact_engine")

        linked_opps = _linked_opportunities(f.get("category"), opportunities)
        if linked_opps:
            source_engines.append("opportunity_engine")
        linked_action = _linked_action(code, management_actions)
        if linked_action:
            source_engines.append("action_engine")

        source_engines_unique = sorted(set(source_engines))
        master_findings.append({
            "id": code,
            "title": f.get("title"),
            "category": f.get("category"),
            "severity": f.get("severity"),
            "confidence": f.get("confidence"),
            "evidence": f.get("evidence"),
            "interpretation": f.get("interpretation"),
            "recommendation": f.get("recommendation"),
            "root_cause": f.get("root_cause"),
            "estimated_exposure": (impact_by_finding.get(code) or {}).get("estimated_exposure"),
            "risk_score": (risk_entry_by_finding.get(code) or {}).get("risk_score"),
            "risk_tier": (risk_entry_by_finding.get(code) or {}).get("risk_tier"),
            "linked_opportunities": linked_opps,
            "linked_action": linked_action,
            "confidence_score": _confidence_score(
                f.get("confidence"), len(source_engines_unique), bool(linked_opps), bool(linked_action)
            ),
            "source_engines": source_engines_unique,
            "also_reported_as": also_reported_as,
        })

    # 2) Genuinely new findings from Gap Detection (operational evidence with
    #    no statement-level twin) are added as first-class registry entries
    #    in their own right - they are not duplicates, so they must not be
    #    dropped.
    for g in all_gaps:
        code = g.get("code")
        if code in duplicate_gap_codes:
            continue
        gap_source_engines = ["gap_detection_engine"]
        linked_action = _linked_action(code, management_actions)
        if linked_action:
            gap_source_engines.append("action_engine")
        # Gaps carry an operational theme, not one of the statement-level
        # categories opportunities are keyed on, so opportunity linking is
        # intentionally skipped here - forcing a match by theme string would
        # create false-positive links (e.g. GAP-SALES-01 has no matching
        # commercial lever in the Opportunity Engine today).
        master_findings.append({
            "id": code,
            "title": g.get("title"),
            "category": g.get("theme"),
            "severity": g.get("severity"),
            "confidence": g.get("confidence", "medium"),
            "evidence": g.get("evidence"),
            "interpretation": g.get("why_it_matters"),
            "recommendation": g.get("recommended_action"),
            "root_cause": None,
            "estimated_exposure": g.get("estimated_impact"),
            "risk_score": None,
            "risk_tier": None,
            "linked_opportunities": [],
            "linked_action": linked_action,
            "confidence_score": _confidence_score(
                g.get("confidence", "medium"), len(set(gap_source_engines)), False, bool(linked_action)
            ),
            "source_engines": sorted(set(gap_source_engines)),
            "also_reported_as": [],
        })

    severity_rank = {"critical": 4, "high": 3, "medium": 2, "low": 1, "positive": 0}
    master_findings_sorted = sorted(
        master_findings,
        key=lambda x: (severity_rank.get(x["severity"], 0), len(x["source_engines"])),
        reverse=True,
    )

    # De-duplicated view of the Gap Detection list for report rendering:
    # exact statement-level duplicates removed and replaced with a pointer
    # to the master finding they were folded into. `build_gap_detection()`
    # itself is untouched - this is purely a display-layer projection.
    gaps_deduplicated = []
    for g in all_gaps:
        if g.get("code") in duplicate_gap_codes:
            continue
        gaps_deduplicated.append(g)

    # FIX (customer-trust bug): severity_summary must reflect what is actually
    # shown in `gaps` after de-duplication, not the pre-dedup raw list. Showing
    # e.g. "critical: 2" next to a list containing 0 critical items destroys
    # trust in the numbers at first glance.
    severity_summary_deduplicated = {
        s: sum(1 for x in gaps_deduplicated if x.get("severity") == s)
        for s in ("critical", "high", "medium", "low")
    }

    return {
        "master_findings": master_findings_sorted,
        "finding_count": len(master_findings_sorted),
        "duplicate_findings_folded": duplicates_folded,
        "duplicate_findings_folded_count": len(duplicates_folded),
        "gap_detection_deduplicated": {
            **gap_detection,
            "gaps": gaps_deduplicated,
            "gap_count": len(gaps_deduplicated),
            "severity_summary": severity_summary_deduplicated,
            "severity_summary_all_findings_note": (
                "Bu sayfadaki bulguların çoğu zaten üst kısımdaki 'Bulgular' "
                "listesinde ayrı kartlarla gösteriliyor; buradaki özet yalnızca "
                "bu listede görünen maddeleri sayar."
            ),
            "note": (
                f"{len(duplicates_folded)} bulgu, Bulgular listesindeki (Findings) aynı kalemle "
                "birleştirildiği için burada ayrıca gösterilmiyor; bkz. finding_registry."
                if duplicates_folded else gap_detection.get("methodology", "")
            ),
        },
        "methodology": (
            "Registry, Root Cause / Gap Detection / Risk Ranking / Business Impact / Opportunity / "
            "Action motorlarının ürettiği bulguları tek bir CFO görünümünde birleştirir. Aynı temel "
            "koşulu (ör. alacak/satış oranı) birden fazla motor bağımsız olarak raporladığında "
            "bulgu bir kez gösterilir ve hangi motorların onu doğruladığı source_engines alanında "
            "belirtilir; bu sayede aynı bulgu farklı isimlerle tekrar tekrar raporlanmaz. Her "
            "bulgu artık kendi ilgili Fırsat(lar)ını (linked_opportunities) ve atanmış Aksiyonunu "
            "(linked_action) da taşır, böylece 'düşük brüt marj' aynı anda Risk, Kök Neden, Fırsat "
            "ve Aksiyon olarak dört ayrı bölümde tekrar tekrar anlatılmak yerine tek bir kayıtta "
            "uçtan uca görülür. confidence_score, bulgunun kendi güven etiketini kaç motorun "
            "bağımsız olarak doğruladığıyla birleştiren 0-100 bileşik bir puandır."
        ),
    }
