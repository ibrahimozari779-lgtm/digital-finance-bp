"""Faz 0 — Guven Sertlestirme regresyon testleri.

Bu dosya, OKUBENI_Musteri_Karari_ve_Duzeltmeler.md'de listelenen ve musterinin
satin alma kararini degistiren 3 guven kirilmasinin bir daha SESSIZCE geri
gelmedigini garanti eder:

  1) Data Quality skoru, capraz kaynak mutabakat uyarilari varken sessizce
     "100/100 Trusted" gosteremez (data_quality_engine.apply_cross_source_reconciliation).
  2) severity_summary sayilari, ekranda gosterilen bulgu listesiyle HER ZAMAN
     birebir eslesmeli (finding_registry.build_finding_registry).
  3) Dusuk risk bulgular (ör. dagilmis alacak tabani) kritik/kirmizi rozetle
     gosterilemez; AI (LLM) yorumu ile deterministik metin UI'da her zaman
     ayri ve etiketli kalmali (frontend_template.py string-kontrat testi).

Bu testler mevcut hesaplama motorlarini DEGISTIRMEZ; sadece zaten yapilmis
duzeltmelerin regresyonunu yakalar. Bkz. TRUST_AUDIT.md.
"""

from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from finance_engine.data_quality_engine import apply_cross_source_reconciliation
from finance_engine.finding_registry import build_finding_registry


# ---------------------------------------------------------------------------
# 1) Data Quality skoru capraz kaynak uyarilariyla celismemeli
# ---------------------------------------------------------------------------

def _base_quality(score: float = 100.0, status: str = "Trusted") -> dict:
    return {
        "score": score,
        "status": status,
        "checks": [],
        "critical_issues": [],
        "warnings": [],
        "unmapped_accounts": 0,
        "internal_consistency_score": score,
        "internal_consistency_status": status,
    }


def test_no_cross_source_warnings_leaves_score_untouched():
    q = _base_quality(100.0, "Trusted")
    out = apply_cross_source_reconciliation(q, {"warning_count": 0, "material_difference_count": 0})
    assert out["score"] == 100.0
    assert out["status"] == "Trusted"
    # No silent field injection when there is nothing to report.
    assert "cross_source_warning_count" not in out


def test_reconciliation_warnings_always_lower_the_headline_score():
    """A perfect internal score can never remain untouched-and-unlabeled once
    cross-source reconciliation finds problems -- this was the exact bug the
    customer flagged (100/100 'Trusted' next to 3 unresolved warnings)."""
    q = _base_quality(100.0, "Trusted")
    out = apply_cross_source_reconciliation(q, {"warning_count": 3, "material_difference_count": 0})
    assert out["score"] < 100.0, "score must drop once reconciliation warnings exist"
    assert out["cross_source_warning_count"] == 3
    # The original mizan-only number must remain visible for transparency,
    # not overwritten -- otherwise the "why did the score change" trail is lost.
    assert out["internal_consistency_score"] == 100.0
    assert "note" in out and str(out["cross_source_warning_count"]) in out["note"]


def test_headline_score_never_exceeds_internal_score():
    """Cross-source reconciliation may only ever be a penalty, never a bonus --
    a combined score higher than the mizan-only score would be an even more
    confusing contradiction than the original bug."""
    for warnings, materials in [(0, 0), (1, 0), (0, 1), (5, 2), (10, 5)]:
        q = _base_quality(87.0, "Review")
        out = apply_cross_source_reconciliation(
            q, {"warning_count": warnings, "material_difference_count": materials}
        )
        assert out["score"] <= 87.0


def test_status_label_matches_the_combined_score_not_the_stale_one():
    q = _base_quality(100.0, "Trusted")
    out = apply_cross_source_reconciliation(q, {"warning_count": 6, "material_difference_count": 1})
    # penalty = min(35, 6*6 + 1*15) = 35 -> combined = 65 -> "Caution"
    assert out["score"] == 65.0
    assert out["status"] == "Caution"
    assert out["status"] != "Trusted"


# ---------------------------------------------------------------------------
# 2) severity_summary sayilari, gosterilen listeyle birebir eslesmeli
# ---------------------------------------------------------------------------

def _gap(code: str, severity: str) -> dict:
    return {
        "code": code,
        "severity": severity,
        "title": f"Test gap {code}",
        "category": "test",
        "evidence": [],
        "why_it_matters": "",
        "recommended_action": "",
        "confidence": "medium",
    }


def test_severity_summary_matches_deduplicated_gap_list_length():
    gaps = [
        _gap("GAP-A", "critical"),
        _gap("GAP-B", "high"),
        _gap("GAP-C", "medium"),
        _gap("GAP-D", "medium"),
        _gap("GAP-E", "low"),
    ]
    gap_detection = {"gaps": gaps, "methodology": "test"}
    reg = build_finding_registry([], gap_detection, {}, {}, {})
    dedup = reg["gap_detection_deduplicated"]

    shown = dedup["gaps"]
    summary = dedup["severity_summary"]

    assert dedup["gap_count"] == len(shown)
    assert sum(summary.values()) == len(shown), (
        "severity_summary total must equal the number of gap cards actually "
        "rendered -- this exact mismatch (summary counts > visible list) was "
        "the customer-reported trust bug."
    )
    # And each bucket must match an actual recount, not a stale pre-dedup figure.
    for sev in ("critical", "high", "medium", "low"):
        assert summary[sev] == sum(1 for g in shown if g["severity"] == sev)


def test_severity_summary_drops_folded_duplicates_from_the_count():
    """When a gap is folded into a Decision Engine finding (duplicate), it
    must disappear from BOTH the visible list and the severity_summary --
    never from just one of the two."""
    from finance_engine.finding_registry import DUPLICATE_GAP_TO_FINDING

    dup_gap_code, target_finding_code = next(iter(DUPLICATE_GAP_TO_FINDING.items()))
    gaps = [_gap(dup_gap_code, "critical"), _gap("GAP-KEEP", "medium")]
    gap_detection = {"gaps": gaps, "methodology": "test"}
    findings = [{"code": target_finding_code, "severity": "critical", "category": "test",
                 "title": "t", "evidence": [], "interpretation": "", "recommendation": ""}]

    reg = build_finding_registry(findings, gap_detection, {}, {}, {})
    dedup = reg["gap_detection_deduplicated"]

    codes_shown = {g["code"] for g in dedup["gaps"]}
    assert dup_gap_code not in codes_shown
    assert sum(dedup["severity_summary"].values()) == len(dedup["gaps"])


# ---------------------------------------------------------------------------
# 3) Frontend string-kontratlari: risk rengi ve AI/deterministik ayrimi
# ---------------------------------------------------------------------------

def _frontend_source() -> str:
    path = os.path.join(os.path.dirname(__file__), "..", "frontend_template.py")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def test_low_concentration_never_renders_a_critical_badge():
    src = _frontend_source()
    m = re.search(r"const concTag=.*?;", src)
    assert m, "concentration badge logic not found in frontend_template.py"
    line = m.group(0)
    # The <10% (low-risk / dispersed) branch must map to a 'positive' tag,
    # and must not be reachable through the 'critical' branch at the same time.
    assert '"tag positive"' in line or "'tag positive'" in line
    assert "Düşük Risk" in line
    # Sanity: the critical branch must be gated behind a higher threshold (>=30)
    # than the positive branch, i.e. thresholds are ordered, not inverted.
    assert "t10>=30" in line.replace(" ", "")
    assert "t10>=10" in line.replace(" ", "")


def test_ai_narrative_is_always_labeled_separately_from_deterministic_summary():
    src = _frontend_source()
    assert "Kural Tabanlı · AI Değil" in src, (
        "the deterministic executive summary must always carry an explicit "
        "'rule-based, not AI' badge next to it"
    )
    assert "AI CFO yorumunu üret" in src, (
        "the optional LLM narrative must remain an explicit opt-in action, "
        "not something rendered inline as if it were the deterministic summary"
    )
    # The two must not share the same DOM id (that would make it impossible
    # to style/label them independently going forward).
    assert 'id="exec"' in src
    assert 'id="aiBox"' in src
    assert 'id="exec"' != 'id="aiBox"'
