from __future__ import annotations

from typing import Any

_DAYS_IN_PERIOD = 365


def _rating(ccc: float | None) -> str:
    if ccc is None:
        return "Hesaplanamadı"
    if ccc < 0:
        return "Çok İyi (negatif nakit döngüsü)"
    if ccc < 30:
        return "Çok İyi"
    if ccc < 60:
        return "İyi"
    if ccc < 90:
        return "Orta"
    return "Zayıf"


def build_cash_conversion_cycle(statements: dict[str, Any], period_days: int | None = None, average_balances: dict[str, float] | None = None) -> dict[str, Any]:
    """Cash Conversion Cycle Engine.

    Computes DSO, DIO, DPO and CCC from the canonical financial model. This
    is a single-snapshot approximation: it uses period-end (closing)
    balances as a proxy for period-average balances, and assumes a 365-day
    annual period, because the current pipeline does not yet ingest
    opening balances or a stated period length. Where COGS or net sales are
    zero/unavailable, the corresponding day-metric is left as None rather
    than guessed.
    """
    pl = statements["profit_and_loss"]
    k = statements["kpis"]

    net_sales = float(pl.get("Net sales") or 0.0)
    cogs = float(pl.get("COGS") or 0.0)
    average_balances = average_balances or {}
    receivables = float(average_balances.get("receivables", k.get("receivables") or 0.0))
    inventory = float(average_balances.get("inventory", k.get("inventory") or 0.0))
    payables = float(average_balances.get("payables", k.get("payables") or 0.0))
    days = int(period_days or _DAYS_IN_PERIOD)

    dso = (receivables / net_sales * days) if net_sales else None
    dio = (inventory / cogs * days) if cogs else None
    dpo = (payables / cogs * days) if cogs else None

    inventory_flag = None
    if cogs and inventory == 0:
        inventory_flag = (
            "Envanter bakiyesi 0 TL olarak tespit edildi. Bu, ya stoksuz/hizmet ağırlıklı bir iş modelini "
            "yansıtıyor olabilir ya da mizanda envanter hesabı (15x) bulunmuyor/eşlenemiyor olabilir. "
            "DIO=0 sonucu bu ayrım yapılmadan doğrudan 'mükemmel stok yönetimi' olarak yorumlanmamalıdır."
        )

    ccc = None
    if dso is not None and dio is not None and dpo is not None:
        ccc = dso + dio - dpo

    cash_tied_up = (ccc / days * net_sales) if (ccc is not None and net_sales) else None

    return {
        "available": ccc is not None,
        "days_in_period_assumption": days,
        "dso_days": round(dso, 1) if dso is not None else None,
        "dio_days": round(dio, 1) if dio is not None else None,
        "dpo_days": round(dpo, 1) if dpo is not None else None,
        "cash_conversion_cycle_days": round(ccc, 1) if ccc is not None else None,
        "rating": _rating(ccc),
        "estimated_cash_tied_up": round(cash_tied_up, 2) if cash_tied_up is not None else None,
        "inventory_flag": inventory_flag,
        "components": {
            "receivables": receivables, "inventory": inventory, "payables": payables,
            "net_sales": net_sales, "cogs": cogs,
        },
        "note": (
            ("DSO/DIO/DPO ortalama bakiyelerle hesaplanmıştır." if average_balances else "DSO/DIO/DPO dönem-sonu bakiyeleriyle hesaplanmıştır.") +
            (f" Dönem uzunluğu: {days} gün." if period_days else " Dönem uzunluğu tespit edilemediği için 365 gün varsayılmıştır.") +
            " Kesin operasyonel CCC için açılış/ortalama bakiyeler ve subledger aging tercih edilir."
        ),
    }
