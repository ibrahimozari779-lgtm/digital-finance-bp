from __future__ import annotations

from typing import Any

# ---------------------------------------------------------------------------
# Strategy Playbook
# ---------------------------------------------------------------------------
# Problem this module solves:
#   Opportunity Engine and Scenario Lab compute the SAME six levers (gross
#   margin, debt paydown, receivables, inventory, opex, payables) and the
#   report renders them as two separate sections. For three levers
#   (inventory/O004↔S004, opex/O005↔S005, payables/O006↔S006) the underlying
#   formula is literally identical (same `_band` thresholds against the same
#   ratio) - i.e. the same number is shown twice with a different label. For
#   the other three (margin/O001↔S003, debt/O002↔S002, receivables/O003↔S001)
#   the opportunity number is a fixed reference assumption (e.g. always +1pp)
#   while the scenario number scales with how far the company's own ratio
#   sits from a healthy band - genuinely different but about the same lever,
#   so showing both as unrelated cards forces the CFO to reconcile them
#   manually.
#
#   This module does not change either engine's arithmetic (both stay
#   available, unchanged, for backward compatibility / regression tests).
#   It produces ONE merged, ranked "playbook" - the richer Scenario Lab
#   number (full P&L/cash/debt impact) as the headline, with the Opportunity
#   Engine's fixed-assumption number attached only where it differs
#   meaningfully, as an explicit lower/alternative reference point rather
#   than a second unrelated card.
# ---------------------------------------------------------------------------

# scenario_id -> matching opportunity code(s) for the same lever.
_THEME_MAP: list[tuple[str, str, str]] = [
    ("S003", "O001", "Kârlılık — Brüt Marj"),
    ("S002", "O002", "Finansman — Borç Azaltımı"),
    ("S001", "O003", "İşletme Sermayesi — Alacaklar"),
    ("S004", "O004", "İşletme Sermayesi — Stok"),
    ("S005", "O005", "Kârlılık — Faaliyet Giderleri"),
    ("S006", "O006", "İşletme Sermayesi — Tedarikçi Vadesi"),
]

# Pairs whose formulas are identical today (same _band thresholds, same
# ratio) - i.e. genuinely the same number computed twice, not just the same
# theme. For these we never show the opportunity number as a separate
# "reference" figure since it would just repeat the scenario number.
_IDENTICAL_FORMULA_PAIRS = {"S004", "S005", "S006"}


def _primary_impact(scenario: dict[str, Any]) -> float:
    for key in ("net_profit_impact", "cash_released", "cash_impact"):
        v = scenario.get(key)
        if v:
            return abs(float(v))
    return 0.0


def build_strategy_playbook(
    opportunities: list[dict[str, Any]],
    scenarios: list[dict[str, Any]],
) -> dict[str, Any]:
    """Merge Opportunity Engine + Scenario Lab into one ranked playbook.

    Each entry is one commercial lever, shown once, with the full financial
    picture (cash / debt / tax / net-profit / liquidity / leverage impact)
    from the Scenario Lab, plus the Opportunity Engine's fixed-assumption
    number attached only when it is not just a restatement of the same
    figure.
    """
    opp_by_code = {o.get("code"): o for o in opportunities}
    scenario_by_id = {s.get("scenario_id"): s for s in scenarios}

    playbook: list[dict[str, Any]] = []
    consumed_opportunity_codes: set[str] = set()
    consumed_scenario_ids: set[str] = set()

    for scenario_id, opp_code, theme in _THEME_MAP:
        s = scenario_by_id.get(scenario_id)
        o = opp_by_code.get(opp_code)
        if s is None and o is None:
            continue
        consumed_scenario_ids.add(scenario_id)
        consumed_opportunity_codes.add(opp_code)

        reference_estimate = None
        if o is not None and scenario_id not in _IDENTICAL_FORMULA_PAIRS:
            same_order_of_magnitude = (
                s is not None
                and s.get("target_pct") is not None
                and o.get("estimated_impact") is not None
                and abs(_primary_impact(s) - float(o["estimated_impact"])) < 1e-6
            )
            if not same_order_of_magnitude:
                reference_estimate = {
                    "label": o.get("title"),
                    "estimated_impact": o.get("estimated_impact"),
                    "assumption": o.get("assumption"),
                }

        entry = {
            "theme": theme,
            "scenario_id": scenario_id,
            "opportunity_code": opp_code,
            "title": (s or o or {}).get("name") or (o or {}).get("title"),
            "current_state": (s or {}).get("current_state") or (o or {}).get("current_state"),
            "target_pct": (s or {}).get("target_pct") if s else (o or {}).get("target_pct"),
            "cash_impact": (s or {}).get("cash_impact"),
            "debt_impact": (s or {}).get("debt_impact"),
            "pbt_impact": (s or {}).get("pbt_impact"),
            "tax_impact": (s or {}).get("tax_impact"),
            "net_profit_impact": (s or {}).get("net_profit_impact"),
            "liquidity_impact": (s or {}).get("liquidity_impact"),
            "leverage_impact": (s or {}).get("leverage_impact"),
            "confidence": (s or {}).get("confidence") or (o or {}).get("confidence", "medium"),
            "limitations": (s or {}).get("limitations"),
            "reference_estimate": reference_estimate,
            "primary_impact_abs": _primary_impact(s) if s else abs(float((o or {}).get("estimated_impact") or 0.0)),
        }
        playbook.append(entry)

    # Any opportunity/scenario not covered by the theme map above (future
    # engine additions) still shows up rather than silently disappearing.
    for o in opportunities:
        if o.get("code") in consumed_opportunity_codes:
            continue
        playbook.append({
            "theme": o.get("area"), "scenario_id": None, "opportunity_code": o.get("code"),
            "title": o.get("title"), "current_state": o.get("current_state"), "target_pct": o.get("target_pct"),
            "cash_impact": None, "debt_impact": None, "pbt_impact": None, "tax_impact": None,
            "net_profit_impact": o.get("estimated_impact"), "liquidity_impact": None, "leverage_impact": None,
            "confidence": o.get("confidence", "medium"), "limitations": o.get("assumption"),
            "reference_estimate": None, "primary_impact_abs": abs(float(o.get("estimated_impact") or 0.0)),
        })
    for s in scenarios:
        if s.get("scenario_id") in consumed_scenario_ids:
            continue
        playbook.append({
            "theme": s.get("name"), "scenario_id": s.get("scenario_id"), "opportunity_code": None,
            "title": s.get("name"), "current_state": s.get("current_state"), "target_pct": s.get("target_pct"),
            "cash_impact": s.get("cash_impact"), "debt_impact": s.get("debt_impact"), "pbt_impact": s.get("pbt_impact"),
            "tax_impact": s.get("tax_impact"), "net_profit_impact": s.get("net_profit_impact"),
            "liquidity_impact": s.get("liquidity_impact"), "leverage_impact": s.get("leverage_impact"),
            "confidence": s.get("confidence", "medium"), "limitations": s.get("limitations"),
            "reference_estimate": None, "primary_impact_abs": _primary_impact(s),
        })

    playbook_sorted = sorted(playbook, key=lambda x: x["primary_impact_abs"], reverse=True)
    for i, entry in enumerate(playbook_sorted, start=1):
        entry["rank"] = i

    return {
        "playbook": playbook_sorted,
        "lever_count": len(playbook_sorted),
        "note": (
            "Fırsat (Opportunity) ve Senaryo (Scenario Lab) motorları aynı altı ticari kaldıracı "
            "hesaplar; bu görünüm ikisini tek karta birleştirir. Baş rakam Senaryo Lab'ın tam "
            "finansal etkisidir (nakit/borç/vergi/net kâr); Opportunity motorunun sabit varsayımlı "
            "referans rakamı yalnızca senaryodan gerçekten farklıysa ayrıca gösterilir."
        ),
    }
