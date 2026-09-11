from __future__ import annotations

from typing import Any


# ---------------------------------------------------------------------------
# Sprint 2 (revised): FACT / INFERENCE narrative chain — general reasoning
# pattern, not a single hardcoded scenario
# ---------------------------------------------------------------------------
# The brief that shaped this section: "Net kâr %18 düştü → Sebep: [birden
# fazla, sayısallaştırılmış sürücü] → bu trend devam ederse N dönem içinde
# [somut eşik]." That is not one fixed scenario to special-case (margin +
# liquidity only) — it is the general shape every CFO narrative should
# follow for whichever finding is actually the top risk this period:
#
#   1. FACT       -> the headline metric's own period-over-period % move,
#                     taken straight from the Trend Engine, no interpretation.
#   2. FACT (n)    -> every trend metric relevant to the top finding's
#                     *category* (not one hardcoded metric name) that
#                     actually has a computed period-over-period change -
#                     this is the quantified "Sebep:" list. Only metrics
#                     Trend Engine actually computed are included; a
#                     category with no trend coverage yields zero bullets,
#                     not invented ones.
#   3. INFERENCE   -> which of those drivers Root Cause Engine's causal
#                     chain treats as the primary one, tagged with its own
#                     causal_status (never presented with false certainty).
#   4. INFERENCE   -> a forward projection is produced ONLY when a metric
#                     tied to the top finding's category has a real,
#                     multi-period trend moving toward one of the system's
#                     OWN existing critical thresholds (the same numbers
#                     decision_engine.py already uses to flag Q001/L002/etc,
#                     not new invented cut-offs). The number of periods
#                     projected ("N dönem") is a linear extrapolation of the
#                     metric's own observed average per-period change - a
#                     real computed number, never a fixed "2 quarters".
# ---------------------------------------------------------------------------

_CAUSAL_STATUS_LABEL = {
    "likely_driver": "olası ana sürücü (mevcut kanıtla tutarlı)",
    "hypothesis": "hipotez (ek veri ile doğrulanmalı)",
}

# Category -> which Trend Engine metric keys are potential drivers for a
# finding in that category. Mirrors finding_registry.py's
# _CATEGORY_TO_OPPORTUNITY_AREAS in spirit (same categories decision_engine.py
# assigns to findings), so a finding, its driver bullets and its linked
# opportunity are never routed to inconsistent metrics.
_CATEGORY_TO_DRIVER_METRICS: dict[str, list[str]] = {
    "Kârlılık": ["gross_margin_pct", "operating_margin_pct", "net_margin_pct"],
    "Borçluluk": ["financial_debt", "debt_to_equity"],
    "Likidite": ["current_ratio", "dso_days", "ccc_days"],
    "İşletme Sermayesi": ["dso_days", "dio_days", "ccc_days"],
    "Kazanç Kalitesi": ["net_margin_pct"],
    "Verimlilik": ["dio_days"],
}

_DRIVER_LABEL_OVERRIDE = {
    "financial_debt": "Finansal borç",
}

# metric_key -> (critical threshold value, direction that is "bad").
# These are NOT new numbers invented for narrative purposes - they are the
# exact thresholds decision_engine.py already uses to raise a finding
# (current_ratio < 1.0 = Q001 critical, debt_to_equity > 5 = L002 critical),
# plus the one universal, self-evidently defensible threshold that has no
# dedicated finding code: net margin crossing 0 (operating losses).
_CRITICAL_THRESHOLDS: dict[str, tuple[float, str]] = {
    "current_ratio": (1.0, "below"),     # Q001 critical threshold
    "debt_to_equity": (5.0, "above"),    # L002 critical threshold
    "net_margin_pct": (0.0, "below"),    # breakeven
}

_MAX_PROJECTED_PERIODS = 12  # beyond this, a linear projection is noise, not signal


def _root_cause_inference(top_finding: dict[str, Any] | None, root_cause: dict[str, Any]) -> dict[str, Any] | None:
    if not top_finding:
        return None
    code = top_finding.get("code")
    for chain in root_cause.get("causal_chains", []) or []:
        if code in (chain.get("related_findings") or []):
            status = chain.get("causal_status", "hypothesis")
            text = (
                f"{top_finding['title']} bulgusunun ardındaki en olası neden zinciri: "
                + " → ".join(chain.get("chain", []))
                + f" (kaynak: {chain.get('primary_driver', '')})."
            )
            return {
                "type": "INFERENCE",
                "text": text,
                "basis": "root_cause_engine",
                "causal_status": status,
                "causal_status_label": _CAUSAL_STATUS_LABEL.get(status, status),
            }
    return None


def _headline_profit_fact(trend: dict[str, Any]) -> dict[str, Any] | None:
    """The one always-relevant headline number: how net profit itself moved
    period-over-period, whatever the top finding turns out to be."""
    if not trend.get("available"):
        return None
    mt = trend.get("metric_trends", {}).get("net_profit")
    changes = (mt or {}).get("period_over_period_change_pct") or []
    chg = changes[-1] if changes else None
    if chg is None:
        return None
    direction = "arttı" if chg >= 0 else "düştü"
    return {
        "type": "FACT",
        "text": f"Net kâr önceki döneme göre %{abs(chg):.1f} {direction}.",
        "basis": "trend_engine",
        "metric": "net_profit",
    }


def _tl_impact_for_metric(key: str, mt: dict[str, Any], statements: dict[str, Any] | None) -> float | None:
    """Converts a driver's own day/percentage-point change into a TL figure,
    using only formulas that are already implicit elsewhere in this system
    (DSO days x daily sales = cash tied up in receivables - the same
    arithmetic build_cash_conversion_cycle uses for `estimated_cash_tied_up`;
    margin points x net sales = TL profit impact - the same arithmetic the
    margin bridge uses for `pct_of_sales`). Returns None whenever a required
    input is missing rather than guessing - no metric gets a fabricated
    currency figure it doesn't have the base data to support.
    """
    if not statements:
        return None
    pl = statements.get("profit_and_loss", {}) or {}
    net_sales = pl.get("Net sales")
    cogs = pl.get("COGS")

    def _latest(field: str) -> float | None:
        arr = mt.get(field) or []
        return arr[-1] if arr else None

    if key == "dso_days":
        chg = _latest("period_over_period_change_abs")
        if chg is None or not net_sales:
            return None
        return round(chg * (net_sales / 365.0), 2)
    if key == "dio_days":
        chg = _latest("period_over_period_change_abs")
        if chg is None or not cogs:
            return None
        return round(chg * (cogs / 365.0), 2)
    if key in ("gross_margin_pct", "operating_margin_pct", "net_margin_pct"):
        chg = _latest("period_over_period_change_pp")
        if chg is None or not net_sales:
            return None
        return round((chg / 100.0) * net_sales, 2)
    if key == "financial_debt":
        chg = _latest("period_over_period_change_abs")
        return round(chg, 2) if chg is not None else None
    return None


_TL_IMPACT_PHRASING = {
    "dso_days": lambda tl: f"~{abs(tl):,.0f} TL {'ilave nakit ihtiyacı' if tl >= 0 else 'nakit serbestleşmesi'}",
    "dio_days": lambda tl: f"~{abs(tl):,.0f} TL {'ilave bağlı sermaye' if tl >= 0 else 'serbestleşen sermaye'}",
    "gross_margin_pct": lambda tl: f"~{abs(tl):,.0f} TL {'kâr artışı' if tl >= 0 else 'kâr kaybı'}",
    "operating_margin_pct": lambda tl: f"~{abs(tl):,.0f} TL {'kâr artışı' if tl >= 0 else 'kâr kaybı'}",
    "net_margin_pct": lambda tl: f"~{abs(tl):,.0f} TL {'kâr artışı' if tl >= 0 else 'kâr kaybı'}",
    "financial_debt": lambda tl: f"~{abs(tl):,.0f} TL {'borç artışı' if tl >= 0 else 'borç azalışı'}",
}


def _quantified_driver_facts(category: str | None, trend: dict[str, Any], statements: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    """The general 'Sebep:' list: every trend metric relevant to the top
    finding's category that Trend Engine actually computed a change for -
    each bullet quantified in its own unit AND, where the base data
    supports it, converted into a TL figure (see _tl_impact_for_metric).
    Purely additive facts - each bullet is one metric's own number, no
    combination or interpretation across metrics happens here."""
    if not trend.get("available") or not category:
        return []
    facts: list[dict[str, Any]] = []
    for key in _CATEGORY_TO_DRIVER_METRICS.get(category, []):
        mt = trend.get("metric_trends", {}).get(key)
        if not mt:
            continue
        label = _DRIVER_LABEL_OVERRIDE.get(key, mt.get("label", key))
        if "period_over_period_change_pct" in mt:
            arr = mt["period_over_period_change_pct"]
            chg = arr[-1] if arr else None
            if chg is None:
                continue
            text = f"{label} {'+' if chg >= 0 else ''}{chg:.1f}%"
        elif "period_over_period_change_pp" in mt:
            arr = mt["period_over_period_change_pp"]
            chg = arr[-1] if arr else None
            if chg is None:
                continue
            text = f"{label} {'+' if chg >= 0 else ''}{chg:.1f} puan"
        elif "period_over_period_change_abs" in mt:
            arr = mt["period_over_period_change_abs"]
            chg = arr[-1] if arr else None
            if chg is None:
                continue
            unit = " gün" if key in ("ccc_days", "dso_days", "dio_days") else ""
            text = f"{label} {'+' if chg >= 0 else ''}{chg:.1f}{unit}"
        else:
            continue
        tl_impact = _tl_impact_for_metric(key, mt, statements)
        if tl_impact is not None and key in _TL_IMPACT_PHRASING:
            text += f" ({_TL_IMPACT_PHRASING[key](tl_impact)})"
        facts.append({"type": "FACT", "text": text, "basis": "trend_engine", "metric": key, "tl_impact": tl_impact})
    return facts


def _linear_periods_to_threshold(series: list[float | None]) -> tuple[float, float] | None:
    """Average per-period change and the latest value, from a metric's own
    historical series - a plain linear extrapolation, nothing fancier
    (the data is 2-4 points; a higher-order fit would just be overfitting)."""
    pts = [v for v in series if v is not None]
    if len(pts) < 3:
        return None
    n_intervals = len(pts) - 1
    avg_delta = (pts[-1] - pts[0]) / n_intervals
    return avg_delta, pts[-1]


def _forward_looking_projection(category: str | None, trend: dict[str, Any]) -> dict[str, Any] | None:
    if not trend.get("available") or not category:
        return None
    for key in _CATEGORY_TO_DRIVER_METRICS.get(category, []):
        if key not in _CRITICAL_THRESHOLDS:
            continue
        mt = trend.get("metric_trends", {}).get(key)
        if not mt:
            continue
        result = _linear_periods_to_threshold(mt.get("series", []))
        if not result:
            continue
        avg_delta, last_val = result
        threshold, direction = _CRITICAL_THRESHOLDS[key]
        moving_toward = (
            (direction == "below" and avg_delta < 0 and last_val > threshold)
            or (direction == "above" and avg_delta > 0 and last_val < threshold)
        )
        if not moving_toward:
            continue
        periods = (threshold - last_val) / avg_delta
        if periods <= 0 or periods > _MAX_PROJECTED_PERIODS:
            continue
        periods_rounded = max(1, round(periods))
        label = _DRIVER_LABEL_OVERRIDE.get(key, mt.get("label", key))
        n_points = len([v for v in mt.get("series", []) if v is not None])
        text = (
            f"{label}, son {n_points} dönemde dönem başına ortalama {avg_delta:+.2f} değişti "
            f"(en son değer: {last_val:.2f}). Bu hız değişmeden devam ederse, yaklaşık {periods_rounded} "
            f"dönem içinde kritik eşik olan {threshold:.2f} seviyesine ulaşılabilir; bu doğrusal bir "
            f"projeksiyondur, gerçek seyir gelecek dönem verisiyle doğrulanmalıdır."
        )
        return {
            "type": "INFERENCE",
            "text": text,
            "basis": "trend_extrapolation_linear",
            "metric": key,
            "periods_projected": periods_rounded,
            "avg_change_per_period": round(avg_delta, 4),
            "requires_validation": True,
        }
    return None


def _build_narrative_chain(
    health_score: float,
    health_label: str,
    top_risks: list[dict[str, Any]],
    business_impact: dict[str, Any],
    root_cause: dict[str, Any],
    trend: dict[str, Any],
    statements: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    chain: list[dict[str, Any]] = [
        {"type": "FACT", "text": f"Finansal sağlık skoru {health_score:.0f}/100 ({health_label}).", "basis": "decision_engine"},
    ]
    top = top_risks[0] if top_risks else None
    if top:
        exposure = next(
            (x["estimated_exposure"] for x in business_impact.get("findings_impact", []) if x["code"] == top["code"]),
            None,
        )
        fact_text = f"En önemli risk: {top['title']}"
        if exposure:
            fact_text += f" (yaklaşık {exposure:,.0f} TL etki büyüklüğünde)."
        else:
            fact_text += "."
        chain.append({"type": "FACT", "text": fact_text, "basis": "risk_ranking_engine / business_impact_engine"})

    profit_fact = _headline_profit_fact(trend)
    if profit_fact:
        chain.append(profit_fact)

    category = top.get("category") if top else None
    chain.extend(_quantified_driver_facts(category, trend, statements))

    if top:
        rc_inference = _root_cause_inference(top, root_cause)
        if rc_inference:
            chain.append(rc_inference)

    projection = _forward_looking_projection(category, trend)
    if projection:
        chain.append(projection)

    return chain


# ---------------------------------------------------------------------------
# Narrative Story: the explicit 5-step "Rule + Data + Causal Chain" shape
# ---------------------------------------------------------------------------
# This is the same reasoning `_build_narrative_chain` above already performs,
# re-packaged as the explicit, labeled structure a CFO actually thinks in -
# KPI değişti -> Neden değişti -> Finansal etkisi ne -> Risk ne -> Ne
# yapılmalı - so a consumer (frontend card, PDF section, API caller) can
# render each step in its own block instead of parsing a flat FACT/INFERENCE
# list. No new computation happens here beyond what narrative_chain already
# does; this function is pure re-assembly + the "Risk ne" and "Ne yapılmalı"
# steps, which narrative_chain doesn't carry (those come from Risk Ranking
# and the linked Management Action for the top finding's code respectively -
# both already computed elsewhere in the Master Decision Hub pipeline).
#
# Known, deliberate scope limits (not silently glossed over): this system's
# canonical financial model is one statement-level snapshot per period, so
# it can reason about *which KPI moved and why*, but it has no customer- or
# SKU-level dimension (no "top 10 customers", no "slow-moving 27% of
# inventory") and no monthly cash-flow cadence (no "3.6 months of runway
# left" burn-rate warning) - both would require a richer data source than
# this pipeline ingests today. Where a step can't be produced from real
# data, it's simply omitted, not fabricated.
# ---------------------------------------------------------------------------


def _risk_step(top_finding: dict[str, Any] | None, risk_ranking: dict[str, Any] | None) -> dict[str, Any] | None:
    if not top_finding or not risk_ranking:
        return None
    code = top_finding.get("code")
    for r in risk_ranking.get("ranked_risks", []) or []:
        if code in (r.get("contributing_codes") or [r.get("code")]):
            return {
                "risk_tier": r.get("risk_tier"),
                "risk_score": r.get("risk_score"),
                "basis": "risk_ranking_engine",
            }
    return None


def _action_step(top_finding: dict[str, Any] | None, management_actions: list[dict[str, Any]] | None) -> dict[str, Any] | None:
    if not top_finding or not management_actions:
        return None
    code = top_finding.get("code")
    for a in management_actions:
        if a.get("finding_id") == code or code in (a.get("merged_finding_codes") or []):
            return {
                "recommended_actions": [a.get("action")],
                "owner": a.get("owner"),
                "time_horizon": a.get("time_horizon"),
                "basis": "action_engine",
            }
    return None


def _build_narrative_story(
    top_risks: list[dict[str, Any]],
    business_impact: dict[str, Any],
    root_cause: dict[str, Any],
    trend: dict[str, Any],
    risk_ranking: dict[str, Any] | None,
    management_actions: list[dict[str, Any]] | None,
    statements: dict[str, Any] | None,
) -> dict[str, Any] | None:
    top = top_risks[0] if top_risks else None
    if not top:
        return None
    category = top.get("category")
    exposure = next(
        (x["estimated_exposure"] for x in business_impact.get("findings_impact", []) if x["code"] == top["code"]),
        None,
    )
    return {
        "finding_code": top.get("code"),
        "kpi_change": {
            "title": top.get("title"),
            "category": category,
            "headline_profit_fact": _headline_profit_fact(trend),
        },
        "why": _quantified_driver_facts(category, trend, statements),
        "root_cause": _root_cause_inference(top, root_cause),
        "financial_impact": (
            {"amount": exposure, "currency": "TRY", "basis": "business_impact_engine"} if exposure else None
        ),
        "risk": _risk_step(top, risk_ranking),
        "forward_projection": _forward_looking_projection(category, trend),
        "what_to_do": _action_step(top, management_actions),
        "scope_note": (
            "Bu yapı yalnızca kanonik finansal tablo modelinden (dönem-bazlı bilanço/gelir tablosu/KPI) "
            "hesaplanabilen adımları içerir. Müşteri/SKU seviyesi kırılım (ör. 'ilk 10 müşteri', 'yavaş "
            "hareket eden stokun %27'si') veya aylık nakit yakma hızı gibi bir projeksiyon, bu pipeline'ın "
            "henüz almadığı daha ayrıntılı bir veri kaynağı gerektirir; üretilemeyen adımlar sessizce "
            "atlanır, uydurulmaz."
        ),
    }


def build_executive_summary(
    health_score: float,
    health_label: str,
    findings_sorted: list[dict[str, Any]],
    opportunities_sorted: list[dict[str, Any]],
    root_cause: dict[str, Any],
    business_impact: dict[str, Any],
    ccc: dict[str, Any],
    trend: dict[str, Any],
    benchmark: dict[str, Any],
    management_actions: list[dict[str, Any]] | None = None,
    cash_bridge: dict[str, Any] | None = None,
    risk_ranking: dict[str, Any] | None = None,
    statements: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Executive Summary Engine.

    Synthesizes every other engine's output into a short narrative plus a
    bullet list of key points, using only facts already calculated
    elsewhere - no figure is invented here.
    """
    top_risks = [x for x in findings_sorted if x["severity"] in {"critical", "high", "medium"}][:3]
    positives = [x for x in findings_sorted if x["severity"] == "positive"][:2]

    parts = [f"Finansal sağlık skoru {health_score:.0f}/100 ({health_label})."]

    if positives:
        parts.append("Güçlü taraf: " + positives[0]["title"].lower() + ".")

    if top_risks:
        top = top_risks[0]
        exposure = next(
            (x["estimated_exposure"] for x in business_impact.get("findings_impact", []) if x["code"] == top["code"]),
            None,
        )
        if exposure:
            parts.append(f"En önemli risk: {top['title'].lower()} (yaklaşık {exposure:,.0f} TL etki büyüklüğünde).")
        else:
            parts.append(f"En önemli risk: {top['title'].lower()}.")

    if root_cause.get("primary_margin_driver"):
        drv = root_cause["primary_margin_driver"]
        parts.append(f"Marjı en çok baskılayan kalem: {drv['label'].lower()} (satışların %{abs(drv['pct_of_sales']):.1f}'i).")

    if opportunities_sorted:
        top_opp = opportunities_sorted[0]
        parts.append(f"En yüksek ilk senaryo fırsatı: {top_opp['title'].lower()}, yaklaşık {top_opp['estimated_impact']:,.0f} TL.")

    if ccc.get("available"):
        parts.append(f"Nakit dönüşüm süresi yaklaşık {ccc['cash_conversion_cycle_days']:.0f} gün ({ccc['rating'].lower()}).")

    if trend.get("available"):
        nm_dir = trend["metric_trends"].get("net_margin_pct", {}).get("latest_direction")
        if nm_dir and nm_dir != "bilinmiyor":
            parts.append(f"Net marj trendi son dönemde {nm_dir} yönünde.")
    else:
        parts.append("Trend analizi için yalnızca tek dönem verisi mevcut; karşılaştırma yapılamadı.")

    if benchmark.get("overall_score") is not None:
        parts.append(f"{benchmark['sector']} sektör göstergeleriyle kıyaslandığında genel konum: {benchmark['overall_label'].lower()}.")

    if cash_bridge and cash_bridge.get("available") and cash_bridge.get("cash_realization_pct") is not None:
        crp = cash_bridge["cash_realization_pct"]
        if crp < 50:
            parts.append(
                f"Net kârın yaklaşık %{crp:.0f}'i işletme nakdine dönüşüyor; geri kalanı alacak/stok/borç kalemlerinde bağlı — defter kârı henüz kasaya girmiş değil."
            )
        else:
            parts.append(f"Net kârın yaklaşık %{crp:.0f}'i işletme nakdine dönüşüyor.")

    # ---- Decision-oriented close: this is the part a manager actually acts
    # on. Every sentence above is a fact; this paragraph turns those facts
    # into "so what do I do with this on Monday morning" — the single
    # question an executive summary exists to answer. It leans on the same
    # management actions shown in detail in "Now What", but states the
    # decision implication in one sentence instead of leaving the reader to
    # infer it from a metric.
    decision_points: list[str] = []
    if management_actions:
        top = management_actions[0]
        impact_txt = f" (~{top['expected_financial_impact']:,.0f} TL beklenen etki)" if top.get("expected_financial_impact") else ""
        decision_points.append(
            f"Yönetim için ilk adım: {top.get('action', '')} — sahibi {top.get('owner', 'CFO')}, ufuk {top.get('time_horizon', '0-30 gün')}{impact_txt}."
        )
        if len(management_actions) > 1:
            second = management_actions[1]
            decision_points.append(f"Bunun hemen ardından: {second.get('action', '')} ({second.get('owner', 'CFO')}).")
    if health_score is not None:
        if health_score < 40:
            decision_points.append("Skor bandı: acil müdahale — nakit ve borç servis kapasitesi haftalık takip edilmeli, büyüme/yatırım kararları ertelenmeli.")
        elif health_score < 65:
            decision_points.append("Skor bandı: kontrollü büyüme — yeni yatırım/harcama kararları önce nakit dönüşüm ve kaldıraç iyileşmesine bağlanmalı.")
        else:
            decision_points.append("Skor bandı: sağlıklı — bu bant büyüme/yatırım kararları için elverişli, ancak yukarıdaki tekil riskler izlenmeli.")
    # NOTE: decision_points are intentionally NOT appended into `parts`/summary_text.
    # They are already rendered as their own bulleted "Yönetici bu raporla ne yapmalı"
    # block directly under this narrative (see execDecision in frontend_template.py).
    # Folding them into the paragraph too produced the same explanation twice in the
    # same card — once buried in prose at the top, once as a clean list at the bottom.
    # The narrative above stays fact-only; the decision list stays the single place
    # the "what should management do" guidance is stated.

    key_points = [
        f"Sağlık skoru: {health_score:.0f}/100 — {health_label}",
    ]
    if top_risks:
        key_points.append(f"En kritik risk: {top_risks[0]['title']}")
    if opportunities_sorted:
        key_points.append(f"En büyük fırsat: {opportunities_sorted[0]['title']} (~{opportunities_sorted[0]['estimated_impact']:,.0f} TL)")
    if ccc.get("available"):
        key_points.append(f"Nakit dönüşüm süresi: {ccc['cash_conversion_cycle_days']:.0f} gün")
    if trend.get("available"):
        key_points.append(f"Trend: {trend['periods_analyzed']} dönem karşılaştırıldı")
    else:
        key_points.append("Trend: tek dönem, karşılaştırma yok")
    if benchmark.get("overall_score") is not None:
        key_points.append(f"Sektör kıyası ({benchmark['sector']}): {benchmark['overall_label']}")
    if cash_bridge and cash_bridge.get("available") and cash_bridge.get("cash_realization_pct") is not None:
        key_points.append(f"Net kâr → nakit dönüşümü: %{cash_bridge['cash_realization_pct']:.0f}")

    summary_text = " ".join(parts)

    narrative_chain = _build_narrative_chain(
        health_score, health_label, top_risks, business_impact, root_cause, trend, statements,
    )
    narrative_story = _build_narrative_story(
        top_risks, business_impact, root_cause, trend, risk_ranking, management_actions, statements,
    )

    return {
        "text": summary_text,
        "key_points": key_points,
        "decision_points": decision_points,
        # Sprint 2: explicit FACT/INFERENCE chain for the top finding - see
        # module docstring above. Additive field; existing consumers of
        # `text`/`key_points`/`decision_points` are unaffected.
        "narrative_chain": narrative_chain,
        # Faz 3 (Narrative Engine = Rule + Data + Causal Chain, not "AI
        # writes a summary"): the same reasoning as narrative_chain,
        # re-packaged as the explicit KPI -> Neden -> Finansal Etki -> Risk
        # -> Ne Yapılmalı structure. See module docstring above the
        # _build_narrative_story function for exactly what is and isn't
        # covered by the current data model.
        "narrative_story": narrative_story,
        "narrative_chain_note": (
            "Her madde FACT (doğrudan başka bir motorun ürettiği sayı/yön, yorum eklenmeden) veya "
            "INFERENCE (bu motorun yaptığı neden ilişkilendirmesi veya ileriye dönük projeksiyon) "
            "olarak etiketlenir. Sayısallaştırılmış 'Sebep:' FACT maddeleri, en önemli riskin "
            "kategorisiyle ilişkili olup Trend Motoru'nun gerçekten hesapladığı metriklerden gelir; "
            "trend verisi veya ilgili metrik yoksa o madde hiç üretilmez. INFERENCE maddeleri Kök "
            "Neden Motoru'nun kendi causal_status etiketini taşır (olası ana sürücü / hipotez) ve "
            "ileriye dönük projeksiyon yalnızca ilgili metrik sistemin zaten kullandığı bir kritik "
            "eşiğe (ör. Cari Oran<1.0, Borç/Özkaynak>5) doğru, çok dönemli ve tutarlı biçimde "
            "ilerliyorsa üretilir; projeksiyondaki dönem sayısı metriğin kendi ortalama dönemsel "
            "değişim hızından doğrusal olarak hesaplanır, sabit bir sayı değildir."
        ),
    }
