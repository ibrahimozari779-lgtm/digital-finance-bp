from __future__ import annotations

from typing import Any

from .cash_conversion_engine import build_cash_conversion_cycle

# (key, label, statements_bucket, source_field, higher_is_better)
# higher_is_better drives the "improved / worsened" read on each period-over-
# period change so the comparison view can color a change correctly even when
# "up" is bad news (e.g. debt/equity, CCC days) instead of good news.
_METRIC_DEFS = [
    ("net_sales", "Net Satışlar", "profit_and_loss", "Net sales", True),
    ("gross_profit", "Brüt Kâr", "profit_and_loss", "Gross profit", True),
    ("operating_profit", "Faaliyet Kârı", "profit_and_loss", "Operating profit", True),
    ("net_profit", "Net Kâr", "profit_and_loss", "Net profit", True),
    ("total_assets", "Toplam Varlıklar", "balance_sheet", "Total assets", True),
    ("total_equity", "Özkaynaklar", "balance_sheet", "Total equity incl. current result", True),
    ("financial_debt", "Finansal Borç", "kpis", "financial_debt", False),
]

_RATIO_DEFS = [
    ("gross_margin_pct", "Brüt Marj %", "kpis", True),
    ("operating_margin_pct", "Faaliyet Marjı %", "kpis", True),
    ("net_margin_pct", "Net Marj %", "kpis", True),
    ("current_ratio", "Cari Oran", "kpis", True),
    ("debt_to_equity", "Borç/Özkaynak", "kpis", False),
]

# Curated subset shown as the prominent, at-a-glance period-vs-period cards
# (the full table below still lists every metric for traceability).
_HEADLINE_KEYS = ["net_sales", "operating_profit", "net_profit", "net_margin_pct", "debt_to_equity", "ccc_days"]


def _extract(statements: dict[str, Any], defs) -> dict[str, float | None]:
    out = {}
    for key, _label, bucket, *rest in defs:
        field = rest[0] if rest and isinstance(rest[0], str) else key
        val = statements.get(bucket, {}).get(field)
        out[key] = float(val) if val is not None else None
    return out


def _pct_change(prev: float | None, curr: float | None) -> float | None:
    if prev in (None, 0) or curr is None:
        return None
    return round((curr - prev) / abs(prev) * 100, 1)


def _assessment(change: float | None, higher_is_better: bool, flat_band: float = 2.0) -> str:
    """Turn a raw change into 'improved' / 'worsened' / 'flat' given metric polarity."""
    if change is None:
        return "bilinmiyor"
    if abs(change) <= flat_band:
        return "flat"
    is_up = change > 0
    improved = is_up if higher_is_better else not is_up
    return "improved" if improved else "worsened"


def _direction(change_pct: float | None) -> str:
    if change_pct is None:
        return "bilinmiyor"
    if change_pct > 2:
        return "yükseliş"
    if change_pct < -2:
        return "düşüş"
    return "yatay"


def _clean_period_label(raw: str | None, fallback: str) -> str:
    if not raw:
        return fallback
    raw_str = str(raw).strip()
    raw_lower = raw_str.lower()
    if "hub_mizan_prior" in raw_lower or "period1" in raw_lower or "donem1" in raw_lower or "2024" in raw_str:
        return "Önceki Dönem (2024)"
    if "hub_mizan" in raw_lower or "period2" in raw_lower or "donem2" in raw_lower or "2025" in raw_str:
        return "Cari Dönem (2025)"
    clean = raw_str.split("/")[-1].split("\\")[-1]
    if clean.endswith((".xlsx", ".xls", ".csv")):
        clean = clean.rsplit(".", 1)[0]
    return clean or fallback



def build_trend_analysis(
    current_statements: dict[str, Any],
    previous_periods: list[dict[str, Any]] | None = None,
    current_label: str = "Cari Dönem",
) -> dict[str, Any]:
    """Trend Analysis Engine.

    Compares the current period against prior periods when they are
    supplied (each item: {"label": str, "statements": <same shape as the
    current statements dict>}, ordered oldest -> most recent, NOT including
    the current period). The pipeline currently ingests one workbook per
    call, so this engine is intentionally optional: with no prior periods it
    reports that trend analysis is unavailable instead of fabricating a
    trend from a single data point.
    """
    if not previous_periods:
        return {
            "available": False,
            "periods_analyzed": 1,
            "reason": "Trend analizi için en az bir önceki döneme ait finansal tablo verisi gereklidir. Şu an yalnızca tek dönem yüklendi.",
        }

    timeline = [
        {
            "label": _clean_period_label(p.get("label") or p.get("period_label") or p.get("filename"), f"Dönem {i+1}"),
            "statements": p["statements"],
        }
        for i, p in enumerate(previous_periods)
    ]
    curr_l = _clean_period_label(current_statements.get("period_metadata", {}).get("label") if isinstance(current_statements.get("period_metadata"), dict) else current_label, current_label)
    timeline.append({"label": curr_l, "statements": current_statements})

    amount_series = {key: [] for key, *_ in _METRIC_DEFS}
    ratio_series = {key: [] for key, *_ in _RATIO_DEFS}
    ccc_series: list[float | None] = []
    dso_series: list[float | None] = []
    dio_series: list[float | None] = []
    period_labels = [t["label"] for t in timeline]

    for t in timeline:
        amounts = _extract(t["statements"], _METRIC_DEFS)
        ratios = {}
        for key, _label, bucket, _hib in _RATIO_DEFS:
            val = t["statements"].get(bucket, {}).get(key)
            ratios[key] = float(val) if val is not None else None
        for key, v in amounts.items():
            amount_series[key].append(v)
        for key, v in ratios.items():
            ratio_series[key].append(v)
        # CCC needs its own engine call per period (DSO/DIO/DPO derive from
        # AR/inventory/AP + net sales/COGS, not a single statement field).
        # Every period in the timeline already carries a full `statements`
        # shape, so this reuses the same single-period logic consistently.
        try:
            p_days = None
            if isinstance(t["statements"].get("period_metadata"), dict):
                p_days = t["statements"]["period_metadata"].get("period_days")
            period_ccc = build_cash_conversion_cycle(t["statements"], period_days=p_days)
            ccc_series.append(period_ccc.get("cash_conversion_cycle_days"))
            dso_series.append(period_ccc.get("dso_days"))
            dio_series.append(period_ccc.get("dio_days"))
        except Exception:
            ccc_series.append(None)
            dso_series.append(None)
            dio_series.append(None)

    higher_is_better = {key: hib for key, _l, _b, _f, hib in _METRIC_DEFS}
    higher_is_better.update({key: hib for key, _l, _b, hib in _RATIO_DEFS})
    higher_is_better["ccc_days"] = False

    metric_trends: dict[str, Any] = {}
    for key, label, *_rest, hib in _METRIC_DEFS:
        series = amount_series[key]
        changes = [_pct_change(series[i - 1], series[i]) for i in range(1, len(series))]
        cagr = None
        n_intervals = len(series) - 1
        if n_intervals >= 1 and series[0] not in (None, 0) and series[-1] is not None and series[0] > 0 and series[-1] > 0:
            cagr = round(((series[-1] / series[0]) ** (1 / n_intervals) - 1) * 100, 1)
        latest_change = changes[-1] if changes else None
        metric_trends[key] = {
            "label": label, "series": series, "period_over_period_change_pct": changes,
            "period_over_period_change_abs": [
                (round(series[i] - series[i - 1], 2) if series[i] is not None and series[i - 1] is not None else None)
                for i in range(1, len(series))
            ],
            "latest_direction": _direction(latest_change),
            "latest_assessment": _assessment(latest_change, hib),
            "cagr_pct": cagr, "higher_is_better": hib,
        }

    for key, label, _bucket, hib in _RATIO_DEFS:
        series = ratio_series[key]
        changes = [
            (round(series[i] - series[i - 1], 2) if series[i] is not None and series[i - 1] is not None else None)
            for i in range(1, len(series))
        ]
        latest_change_pp = changes[-1] if changes else None
        metric_trends[key] = {
            "label": label, "series": series, "period_over_period_change_pp": changes,
            "latest_direction": _direction(latest_change_pp * 10 if latest_change_pp is not None else None),
            "latest_assessment": _assessment(latest_change_pp, hib, flat_band=0.5),
            "higher_is_better": hib,
        }

    ccc_changes = [
        (round(ccc_series[i] - ccc_series[i - 1], 1) if ccc_series[i] is not None and ccc_series[i - 1] is not None else None)
        for i in range(1, len(ccc_series))
    ]
    latest_ccc_change = ccc_changes[-1] if ccc_changes else None
    metric_trends["ccc_days"] = {
        "label": "Nakit Dönüşüm Süresi (gün)", "series": ccc_series,
        "period_over_period_change_abs": ccc_changes,
        "latest_direction": _direction((latest_ccc_change / max(1, abs(ccc_series[-2] or 1)) * 100) if latest_ccc_change is not None and len(ccc_series) > 1 and ccc_series[-2] else None),
        "latest_assessment": _assessment(latest_ccc_change, False, flat_band=3.0),
        "higher_is_better": False,
    }

    # DSO/DIO tracked as their own series (Faz 3: quantified, per-driver
    # narrative needs the individual day-metrics, not just the combined CCC -
    # "DSO went from 58 to 82 days" is a different, more actionable claim
    # than "CCC lengthened", even though CCC already reflected the same
    # underlying move.
    for series, key, label in ((dso_series, "dso_days", "Alacak Tahsilat Süresi / DSO (gün)"), (dio_series, "dio_days", "Stok Devir Süresi / DIO (gün)")):
        changes_abs = [
            (round(series[i] - series[i - 1], 1) if series[i] is not None and series[i - 1] is not None else None)
            for i in range(1, len(series))
        ]
        latest_change = changes_abs[-1] if changes_abs else None
        metric_trends[key] = {
            "label": label, "series": series,
            "period_over_period_change_abs": changes_abs,
            "latest_direction": _direction((latest_change / max(1, abs(series[-2] or 1)) * 100) if latest_change is not None and len(series) > 1 and series[-2] else None),
            "latest_assessment": _assessment(latest_change, False, flat_band=3.0),
            "higher_is_better": False,
        }

    trend_findings: list[dict[str, Any]] = []
    nm = metric_trends.get("net_margin_pct", {}).get("series", [])
    if len(nm) >= 3 and all(v is not None for v in nm[-3:]) and nm[-1] < nm[-2] < nm[-3]:
        trend_findings.append({
            "code": "T001", "severity": "high",
            "title": "Net kâr marjında sürekli düşüş trendi",
            "interpretation": f"Net marj son {len(nm)} dönemde art arda geriliyor ({nm[-3]:.1f}% → {nm[-2]:.1f}% → {nm[-1]:.1f}%).",
            "recommendation": "Marj erozyonunun fiyatlama, maliyet enflasyonu veya ürün karmasından mı kaynaklandığını Kök Neden Motoru ile birlikte incele.",
        })
    de = metric_trends.get("debt_to_equity", {}).get("series", [])
    if len(de) >= 2 and de[-1] is not None and de[0] not in (None, 0) and de[-1] > de[0] * 1.2:
        trend_findings.append({
            "code": "T002", "severity": "medium",
            "title": "Kaldıraç zaman içinde artıyor",
            "interpretation": f"Borç/özkaynak oranı {de[0]:.2f}x seviyesinden {de[-1]:.2f}x seviyesine yükseldi.",
            "recommendation": "Kaldıraç artış hızını sermaye planı ve borç vade profili ile karşılaştır.",
        })
    ccc_valid = [v for v in ccc_series if v is not None]
    if len(ccc_valid) >= 2 and ccc_series[-1] is not None and ccc_series[0] is not None and ccc_series[-1] > ccc_series[0] + 10:
        trend_findings.append({
            "code": "T003", "severity": "medium",
            "title": "Nakit dönüşüm süresi uzuyor",
            "interpretation": f"Nakit dönüşüm süresi {ccc_series[0]:.0f} günden {ccc_series[-1]:.0f} güne çıktı — işletme sermayesi zaman içinde daha fazla nakit bağlıyor.",
            "recommendation": "Alacak tahsilat, stok devir ve tedarikçi vade koşullarının hangisinin bu artışı sürüklediğini Working Capital bölümüyle birlikte incele.",
        })
    net_sales_series = metric_trends.get("net_sales", {}).get("series", [])
    net_profit_series = metric_trends.get("net_profit", {}).get("series", [])
    if (len(net_sales_series) >= 2 and net_sales_series[-1] is not None and net_sales_series[0] not in (None, 0)
            and net_sales_series[-1] > net_sales_series[0] * 1.1
            and len(net_profit_series) >= 2 and net_profit_series[-1] is not None and net_profit_series[0] is not None
            and net_profit_series[-1] <= net_profit_series[0]):
        trend_findings.append({
            "code": "T004", "severity": "high",
            "title": "Büyüme kâra dönüşmüyor",
            "interpretation": f"Net satışlar {net_sales_series[0]:,.0f} TL'den {net_sales_series[-1]:,.0f} TL'ye büyüdü, ancak net kâr aynı dönemde artmadı/geriledi.",
            "recommendation": "Marj erozyonu mu, faaliyet dışı/finansman gideri artışı mı olduğunu Profitability Bridge ve Kök Neden bölümleriyle birlikte incele.",
        })

    # Headline comparison: the last two points of the timeline, in a shape the
    # frontend can render directly as side-by-side cards without recomputing
    # anything. With more than 2 periods loaded, this still just compares the
    # most recent pair; the full series above covers the longer history.
    headline_labels = {
        "net_sales": "Net Satış", "operating_profit": "Faaliyet Kârı", "net_profit": "Net Kâr",
        "net_margin_pct": "Net Marj", "debt_to_equity": "Borç/Özkaynak", "ccc_days": "Nakit Dönüşüm Süresi",
    }
    headline_comparison = []
    if len(period_labels) >= 2:
        for key in _HEADLINE_KEYS:
            mt = metric_trends.get(key)
            if not mt or len(mt["series"]) < 2:
                continue
            a, b = mt["series"][-2], mt["series"][-1]
            is_pct_point_metric = key in {"net_margin_pct"}
            change_abs = round(b - a, 2) if (a is not None and b is not None) else None
            change_pct = _pct_change(a, b) if not is_pct_point_metric else None
            headline_comparison.append({
                "key": key, "label": headline_labels.get(key, mt["label"]),
                "period_a_label": period_labels[-2], "period_b_label": period_labels[-1],
                "period_a_value": a, "period_b_value": b,
                "change_abs": change_abs, "change_pct": change_pct,
                "unit": "pct_points" if is_pct_point_metric else ("x" if key == "debt_to_equity" else ("days" if key == "ccc_days" else "amount")),
                "assessment": mt.get("latest_assessment", "bilinmiyor"),
            })

    return {
        "available": True,
        "periods_analyzed": len(timeline),
        "period_labels": period_labels,
        "metric_trends": metric_trends,
        "headline_comparison": headline_comparison,
        "trend_findings": trend_findings,
        "note": "Trend, kullanıcının yüklediği önceki dönem tabloları üzerinden hesaplanır; dönemlerin karşılaştırılabilir muhasebe politikası ve süre uzunluğuna sahip olduğu varsayılır. Nakit dönüşüm süresi, dönem-sonu bakiyeleriyle proxy olarak hesaplanır.",
    }
