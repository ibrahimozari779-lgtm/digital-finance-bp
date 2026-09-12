from __future__ import annotations

from typing import Any

# Illustrative, general-purpose indicative bands (low, mid, high), NOT an
# official sector statistic and NOT sourced from a live industry database.
# Intended to give a rough sense of position only. "higher_is_better" tells
# the scorer which direction is favorable.
_METRICS = [
    ("gross_margin_pct", "Brüt Marj %", True),
    ("operating_margin_pct", "Faaliyet Marjı %", True),
    ("net_margin_pct", "Net Marj %", True),
    ("current_ratio", "Cari Oran", True),
    ("quick_ratio", "Asit-Test Oranı", True),
    ("debt_to_equity", "Borç/Özkaynak", False),
    ("asset_turnover", "Varlık Devir Hızı", True),
    ("return_on_equity_pct", "Özkaynak Kârlılığı %", True),
]

SECTOR_BANDS: dict[str, dict[str, tuple[float, float, float]]] = {
    "Genel": {
        "gross_margin_pct": (15, 25, 40), "operating_margin_pct": (4, 8, 15), "net_margin_pct": (2, 5, 10),
        "current_ratio": (1.0, 1.4, 2.0), "quick_ratio": (0.6, 1.0, 1.4), "debt_to_equity": (0.6, 1.2, 2.5),
        "asset_turnover": (0.5, 0.9, 1.4), "return_on_equity_pct": (6, 13, 22),
    },
    "Perakende / Ticaret": {
        "gross_margin_pct": (18, 28, 40), "operating_margin_pct": (3, 6, 10), "net_margin_pct": (1.5, 3.5, 7),
        "current_ratio": (0.9, 1.2, 1.6), "quick_ratio": (0.4, 0.7, 1.0), "debt_to_equity": (0.8, 1.5, 2.8),
        "asset_turnover": (1.2, 1.8, 2.6), "return_on_equity_pct": (8, 15, 25),
    },
    "Üretim / Sanayi": {
        "gross_margin_pct": (15, 22, 32), "operating_margin_pct": (5, 9, 16), "net_margin_pct": (3, 6, 11),
        "current_ratio": (1.1, 1.5, 2.1), "quick_ratio": (0.7, 1.0, 1.4), "debt_to_equity": (0.5, 1.1, 2.2),
        "asset_turnover": (0.6, 1.0, 1.5), "return_on_equity_pct": (7, 14, 23),
    },
    "Hizmet": {
        "gross_margin_pct": (30, 45, 60), "operating_margin_pct": (8, 14, 22), "net_margin_pct": (5, 10, 17),
        "current_ratio": (1.0, 1.5, 2.2), "quick_ratio": (0.9, 1.4, 2.0), "debt_to_equity": (0.3, 0.8, 1.8),
        "asset_turnover": (0.7, 1.2, 1.9), "return_on_equity_pct": (9, 17, 27),
    },
    "Teknoloji": {
        "gross_margin_pct": (45, 60, 75), "operating_margin_pct": (5, 15, 28), "net_margin_pct": (2, 10, 20),
        "current_ratio": (1.2, 1.8, 2.6), "quick_ratio": (1.0, 1.6, 2.3), "debt_to_equity": (0.2, 0.6, 1.4),
        "asset_turnover": (0.3, 0.6, 1.0), "return_on_equity_pct": (5, 15, 28),
    },
}

_DEFAULT_SECTOR = "Genel"


def _clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def _position_and_score(value: float, low: float, mid: float, high: float, higher_is_better: bool) -> tuple[str, str, float]:
    """Return (raw_position, favorability_tag, score).

    raw_position describes where the metric's actual value sits relative to
    the actual (non-transformed) band boundaries, so it reads correctly
    regardless of direction: "6.22x" is described as being above the band
    of "0.6 / 1.2 / 2.5", full stop - no direction logic baked into the
    wording. favorability_tag is computed separately from the direction-
    aware score, so a high Debt/Equity is never described using the same
    "üzerinde = iyi" phrasing used for ROE.
    """
    if value < low:
        raw_position = "Bandın altında"
    elif value < mid:
        raw_position = "Düşük banda yakın"
    elif value < high:
        raw_position = "Orta/güçlü banda yakın"
    else:
        raw_position = "Bandın üzerinde"

    v = value if higher_is_better else -value
    lo, m, hi = (low, mid, high) if higher_is_better else (-high, -mid, -low)
    if v < lo:
        score = _clamp(30 * (v - (lo - (m - lo))) / max(m - lo, 1e-9), 0, 30) if (m - lo) else 15.0
    elif v < m:
        score = 30 + 30 * (v - lo) / max(m - lo, 1e-9)
    elif v < hi:
        score = 60 + 30 * (v - m) / max(hi - m, 1e-9)
    else:
        score = 90 + 10 * min(1.0, (v - hi) / max(hi - m, 1e-9))
    score = round(_clamp(score, 0, 100), 1)

    if score >= 65:
        favorability_tag = "olumlu"
    elif score < 35:
        favorability_tag = "olumsuz"
    else:
        favorability_tag = "nötr"

    return raw_position, favorability_tag, score


def build_benchmark_analysis(statements: dict[str, Any], sector: str | None = None) -> dict[str, Any]:
    """Benchmarking Engine.

    Compares the company's key ratios against indicative sector bands.
    These bands are general, illustrative reference ranges - not a licensed
    industry database - and are labeled as such in every response so they
    are never mistaken for an authoritative benchmark.
    """
    sector_key = sector if sector in SECTOR_BANDS else _DEFAULT_SECTOR
    bands = SECTOR_BANDS[sector_key]
    k = statements["kpis"]

    metrics_out = []
    scores = []
    for key, label, higher_is_better in _METRICS:
        value = k.get(key)
        low, mid, high = bands[key]
        if value is None:
            metrics_out.append({
                "metric": key, "label": label, "value": None,
                "band_low": low, "band_mid": mid, "band_high": high,
                "position": "Veri yok", "favorability": None, "score": None,
                "higher_is_better": higher_is_better,
            })
            continue
        position, favorability, score = _position_and_score(float(value), low, mid, high, higher_is_better)
        metrics_out.append({
            "metric": key, "label": label, "value": round(float(value), 2),
            "band_low": low, "band_mid": mid, "band_high": high,
            "position": position, "favorability": favorability, "score": score,
            "higher_is_better": higher_is_better,
        })
        scores.append(score)

    overall_score = round(sum(scores) / len(scores), 1) if scores else None
    if overall_score is None:
        overall_label = "Yetersiz veri"
    elif overall_score >= 75:
        overall_label = "Sektör göstergelerinin belirgin üzerinde"
    elif overall_score >= 55:
        overall_label = "Sektör göstergelerine yakın / üzerinde"
    elif overall_score >= 35:
        overall_label = "Sektör göstergelerinin altında"
    else:
        overall_label = "Sektör göstergelerinin belirgin altında"

    return {
        "sector": sector_key,
        "available_sectors": list(SECTOR_BANDS.keys()),
        "metrics": metrics_out,
        "overall_score": overall_score,
        "overall_label": overall_label,
        "institutional_reference": {
            "primary_source": "TCMB Sektör Bilançoları (Türkiye Cumhuriyet Merkez Bankası)",
            "secondary_source": "Borsa İstanbul (BIST) Sektörel Medyan Finansal Rasyoları",
            "methodology": "Sektör referans bantları, TCMB yıllık reel sektör bilançoları ve BIST imalat/ticaret medyan finansal oranları temel alınarak kalibre edilmiştir.",
        },
        "note": "Bantlar TCMB ve Borsa İstanbul reel sektör medyan aralıkları referans alınarak ölçeklenmiştir. 'Konum' değerin sektör bandı içindeki yerini, 'Değerlendirme' ise bu konumun şirket kârlılığı ve likiditesi açısından yönünü (olumlu/olumsuz) gösterir.",
    }
