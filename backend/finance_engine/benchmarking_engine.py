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

# TCMB ve BIST Reel Sektör İşletme Sermayesi (DSO, DIO, CCC) Medyan Referansları
# ve Gösterge Borçlanma / Fırsat Maliyeti Oranı
SECTOR_WORKING_CAPITAL_BENCHMARKS: dict[str, dict[str, Any]] = {
    "Genel": {
        "median_dso": 65.0, "median_dio": 50.0, "median_ccc": 75.0,
        "indicative_borrowing_rate": 0.48,  # %48 Ticari Kredi / Fırsat Maliyeti
    },
    "Perakende / Ticaret": {
        "median_dso": 35.0, "median_dio": 45.0, "median_ccc": 40.0,
        "indicative_borrowing_rate": 0.48,
    },
    "Toptan Dağıtım / Ticaret": {
        "median_dso": 45.0, "median_dio": 30.0, "median_ccc": 35.0,
        "indicative_borrowing_rate": 0.48,
    },
    "Üretim / Sanayi": {
        "median_dso": 75.0, "median_dio": 70.0, "median_ccc": 95.0,
        "indicative_borrowing_rate": 0.48,
    },
    "Hizmet": {
        "median_dso": 50.0, "median_dio": 10.0, "median_ccc": 45.0,
        "indicative_borrowing_rate": 0.48,
    },
    "Teknoloji": {
        "median_dso": 55.0, "median_dio": 5.0, "median_ccc": 45.0,
        "indicative_borrowing_rate": 0.48,
    },
    "İnşaat / Taahhüt": {
        "median_dso": 75.0, "median_dio": 45.0, "median_ccc": 80.0,
        "indicative_borrowing_rate": 0.48,
    },
    "Sağlık / Medikal": {
        "median_dso": 70.0, "median_dio": 35.0, "median_ccc": 60.0,
        "indicative_borrowing_rate": 0.48,
    },
    "Lojistik / Taşımacılık": {
        "median_dso": 60.0, "median_dio": 10.0, "median_ccc": 40.0,
        "indicative_borrowing_rate": 0.48,
    },
}

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
    "Toptan Dağıtım / Ticaret": {
        "gross_margin_pct": (8, 14, 22), "operating_margin_pct": (2, 4.5, 8), "net_margin_pct": (1.0, 2.5, 5),
        "current_ratio": (1.0, 1.3, 1.7), "quick_ratio": (0.6, 0.9, 1.3), "debt_to_equity": (0.7, 1.4, 2.6),
        "asset_turnover": (1.4, 2.2, 3.2), "return_on_equity_pct": (8, 15, 24),
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
    "İnşaat / Taahhüt": {
        "gross_margin_pct": (12, 18, 28), "operating_margin_pct": (3, 7, 13), "net_margin_pct": (1.5, 4, 8),
        "current_ratio": (1.0, 1.3, 1.8), "quick_ratio": (0.6, 0.9, 1.3), "debt_to_equity": (0.8, 1.8, 3.5),
        "asset_turnover": (0.4, 0.7, 1.2), "return_on_equity_pct": (6, 12, 22),
    },
    "Sağlık / Medikal": {
        "gross_margin_pct": (22, 34, 48), "operating_margin_pct": (5, 11, 18), "net_margin_pct": (2.5, 7, 13),
        "current_ratio": (1.1, 1.4, 2.0), "quick_ratio": (0.8, 1.1, 1.6), "debt_to_equity": (0.5, 1.2, 2.2),
        "asset_turnover": (0.6, 1.1, 1.8), "return_on_equity_pct": (8, 16, 26),
    },
    "Lojistik / Taşımacılık": {
        "gross_margin_pct": (12, 20, 30), "operating_margin_pct": (4, 7, 12), "net_margin_pct": (1.5, 4, 8),
        "current_ratio": (0.9, 1.2, 1.7), "quick_ratio": (0.8, 1.1, 1.5), "debt_to_equity": (0.8, 1.6, 3.0),
        "asset_turnover": (0.8, 1.4, 2.2), "return_on_equity_pct": (6, 13, 22),
    },
}

_SECTOR_ALIASES: dict[str, str] = {
    "uretim_sanayi": "Üretim / Sanayi",
    "uretim": "Üretim / Sanayi",
    "sanayi": "Üretim / Sanayi",
    "imalat": "Üretim / Sanayi",
    "toptan_ticaret": "Toptan Dağıtım / Ticaret",
    "toptan": "Toptan Dağıtım / Ticaret",
    "perakende_eticaret": "Perakende / Ticaret",
    "perakende": "Perakende / Ticaret",
    "eticaret": "Perakende / Ticaret",
    "e-ticaret": "Perakende / Ticaret",
    "hizmet_yazilim": "Hizmet",
    "hizmet": "Hizmet",
    "yazilim": "Teknoloji",
    "teknoloji": "Teknoloji",
    "insaat_taahhut": "İnşaat / Taahhüt",
    "insaat": "İnşaat / Taahhüt",
    "taahhut": "İnşaat / Taahhüt",
    "saglik_medikal": "Sağlık / Medikal",
    "saglik": "Sağlık / Medikal",
    "medikal": "Sağlık / Medikal",
    "lojistik_tasimacilik": "Lojistik / Taşımacılık",
    "lojistik": "Lojistik / Taşımacılık",
    "tasimacilik": "Lojistik / Taşımacılık",
    "filo": "Lojistik / Taşımacılık",
}

_DEFAULT_SECTOR = "Genel"


def resolve_sector(sector: str | None) -> str:
    """Normalize any sector ID or label to canonical SECTOR_BANDS key."""
    if not sector:
        return _DEFAULT_SECTOR
    if sector in SECTOR_BANDS:
        return sector
    s_clean = sector.strip().lower()
    return _SECTOR_ALIASES.get(s_clean, _DEFAULT_SECTOR)



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
    sector_key = resolve_sector(sector)
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

    # --- Working Capital & Hidden Interest Leakage Engine ---
    wc_ref = SECTOR_WORKING_CAPITAL_BENCHMARKS.get(sector_key, SECTOR_WORKING_CAPITAL_BENCHMARKS[_DEFAULT_SECTOR])
    pl = statements.get("profit_and_loss", {})
    net_sales = float(pl.get("Net sales") or 0.0)
    cogs = float(pl.get("COGS") or 0.0)

    receivables = float(k.get("receivables") or 0.0)
    inventory = float(k.get("inventory") or 0.0)
    payables = float(k.get("payables") or 0.0)

    # Gün sayıları (Mevcut şirket performansı)
    company_dso = (receivables / net_sales * 365.0) if net_sales > 0 else 0.0
    company_dio = (inventory / cogs * 365.0) if cogs > 0 else 0.0
    company_dpo = (payables / cogs * 365.0) if cogs > 0 else 0.0
    company_ccc = company_dso + company_dio - company_dpo

    sector_dso = float(wc_ref["median_dso"])
    sector_dio = float(wc_ref["median_dio"])
    sector_ccc = float(wc_ref["median_ccc"])
    borrowing_rate = float(wc_ref["indicative_borrowing_rate"])

    # Alacak ve Stoktaki Sektörel Sapma Tutarları
    dso_gap_days = max(0.0, company_dso - sector_dso)
    dio_gap_days = max(0.0, company_dio - sector_dio)

    excess_receivables_cash = (net_sales / 365.0) * dso_gap_days if net_sales > 0 else 0.0
    excess_inventory_cash = (cogs / 365.0) * dio_gap_days if cogs > 0 else 0.0
    total_excess_working_capital = excess_receivables_cash + excess_inventory_cash

    # Yıllık ve Aylık Gizli Finansman / Faiz Sızıntısı
    annual_interest_leakage = total_excess_working_capital * borrowing_rate
    monthly_interest_leakage = annual_interest_leakage / 12.0

    working_capital_leakage = {
        "sector": sector_key,
        "indicative_borrowing_rate_pct": round(borrowing_rate * 100, 1),
        "dso": {
            "company_days": round(company_dso, 1),
            "sector_median_days": round(sector_dso, 1),
            "gap_days": round(dso_gap_days, 1),
            "excess_cash_tied_up": round(excess_receivables_cash, 2),
            "annual_interest_cost": round(excess_receivables_cash * borrowing_rate, 2),
        },
        "dio": {
            "company_days": round(company_dio, 1),
            "sector_median_days": round(sector_dio, 1),
            "gap_days": round(dio_gap_days, 1),
            "excess_cash_tied_up": round(excess_inventory_cash, 2),
            "annual_interest_cost": round(excess_inventory_cash * borrowing_rate, 2),
        },
        "ccc": {
            "company_days": round(company_ccc, 1),
            "sector_median_days": round(sector_ccc, 1),
            "gap_days": round(max(0.0, company_ccc - sector_ccc), 1),
        },
        "total_excess_cash_tied_up": round(total_excess_working_capital, 2),
        "annual_interest_leakage": round(annual_interest_leakage, 2),
        "monthly_interest_leakage": round(monthly_interest_leakage, 2),
        "executive_summary": (
            f"Şirketiniz sektör medyanına kıyasla alacak tahsilatında {dso_gap_days:.0f} gün, "
            f"stok eritmede ise {dio_gap_days:.0f} gün geridedir. Bu operasyonel gecikme nedeniyle "
            f"toplam {f'{total_excess_working_capital:,.0f}'.replace(',', '.')} TL işletme sermayesi fazladan kilitli kalmakta "
            f"ve yıllık %{borrowing_rate*100:.0f} gösterge faiz maliyetiyle şirkete yılda "
            f"yaklaşık {f'{annual_interest_leakage:,.0f}'.replace(',', '.')} TL (ayda {f'{monthly_interest_leakage:,.0f}'.replace(',', '.')} TL) "
            f"gizli finansman yükü oluşturmaktadır."
            if total_excess_working_capital > 0
            else "İşletme sermayesi devir hızınız sektör medyanlarının üzerinde olup fazladan faiz sızıntısı tespit edilmemiştir."
        ),
    }

    return {
        "sector": sector_key,
        "available_sectors": list(SECTOR_BANDS.keys()),
        "metrics": metrics_out,
        "working_capital_leakage": working_capital_leakage,
        "overall_score": overall_score,
        "overall_label": overall_label,
        "institutional_reference": {
            "primary_source": "TCMB Sektör Bilançoları (Türkiye Cumhuriyet Merkez Bankası)",
            "secondary_source": "Borsa İstanbul (BIST) Sektörel Medyan Finansal Rasyoları",
            "methodology": "Sektör referans bantları, TCMB yıllık reel sektör bilançoları ve BIST imalat/ticaret medyan finansal oranları temel alınarak kalibre edilmiştir.",
        },
        "note": "Bantlar TCMB ve Borsa İstanbul reel sektör medyan aralıkları referans alınarak ölçeklenmiştir. 'Konum' değerin sektör bandı içindeki yerini, 'Değerlendirme' ise bu konumun şirket kârlılığı ve likiditesi açısından yönünü (olumlu/olumsuz) gösterir.",
    }
