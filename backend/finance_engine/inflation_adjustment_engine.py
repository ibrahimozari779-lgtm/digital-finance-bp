"""Inflation Adjustment & Real Capital Erosion Engine (Enflasyon Düzeltmeli Gerçek Kârlılık Röntgeni).

Reveals the difference between nominal accounting profit and real economic profit
under high inflation environments.
Key analytical pillars:
1. Inventory Phantom Profit (Fiktif Stok Kârı): Due to historical FIFO/weighted cost,
   nominal COGS is understated relative to current replacement cost.
2. Real Equity Erosion (Özkaynak Satın Alma Gücü Kaybı): Non-monetary asset gains vs monetary
   losses; assesses whether net profit exceeds inflation-driven capital preservation requirements.
3. Real Economic Net Margin vs Nominal Accounting Margin.
"""
from __future__ import annotations
from typing import Any


def build_inflation_adjustment_analysis(
    statements: dict[str, Any],
    annual_inflation_rate: float = 0.45,  # %45 varsayılan yıllık TÜFE/ÜFE göstergesi
) -> dict[str, Any]:
    """Calculates inflation-adjusted economic profitability and purchasing power erosion."""
    pl = statements.get("profit_and_loss", {})
    bs = statements.get("balance_sheet", {})
    k = statements.get("kpis", {})

    net_sales = float(pl.get("Net sales") or 0.0)
    cogs = float(pl.get("COGS") or 0.0)
    gross_profit = float(pl.get("Gross profit") or 0.0)
    operating_profit = float(pl.get("Operating profit") or 0.0)
    net_profit = float(pl.get("Net profit") or 0.0)

    inventory = float(k.get("inventory") or 0.0)
    equity = float(bs.get("Total equity incl. current result") or 0.0)
    monetary_assets = float(k.get("cash") or 0.0) + float(k.get("receivables") or 0.0)
    monetary_liabilities = float(bs.get("Current liabilities") or 0.0)

    # 1. Stok Tutma Süresi ve Fiktif Stok Kârı (Replacement Cost Gap)
    stock_holding_days = (inventory / cogs * 365.0) if cogs > 0 else 0.0
    stock_inflation_factor = (stock_holding_days / 365.0) * annual_inflation_rate
    phantom_inventory_profit = cogs * stock_inflation_factor if cogs > 0 else 0.0

    # 2. Net Parasal Pozisyon Kaybı / Kazancı
    net_monetary_position = monetary_assets - monetary_liabilities
    monetary_position_loss = net_monetary_position * annual_inflation_rate

    # 3. Sermaye Koruma Eşiği
    equity_preservation_threshold = max(0.0, equity * annual_inflation_rate)

    # 4. Reel Ekonomik Kâr
    real_economic_profit = net_profit - phantom_inventory_profit - max(0.0, monetary_position_loss)
    real_margin_pct = (real_economic_profit / net_sales * 100.0) if net_sales > 0 else 0.0
    nominal_margin_pct = (net_profit / net_sales * 100.0) if net_sales > 0 else 0.0

    is_capital_eroding = net_profit < equity_preservation_threshold if equity > 0 else True
    capital_erosion_amount = max(0.0, equity_preservation_threshold - net_profit) if equity > 0 else 0.0

    def _tl(v: float) -> str:
        return f"{v:,.0f}".replace(",", ".")

    severity = "critical" if real_economic_profit < 0 and net_profit > 0 else ("high" if is_capital_eroding else "medium")

    if real_economic_profit < 0 and net_profit > 0:
        executive_assessment = (
            f"İllüzyon Kâr Uyarısı: Defterde {_tl(net_profit)} TL nominal net kâr görünmesine rağmen, "
            f"yıllık %{annual_inflation_rate*100:.0f} enflasyon ve stok yenileme maliyeti düşüldüğünde "
            f"şirketiniz aslında -{_tl(abs(real_economic_profit))} TL REEL ZARARDADIR. "
            f"Kâr zannettiğiniz tutarın {_tl(phantom_inventory_profit)} TL'si satılan stoğu aynı fiyattan "
            f"yerine koyamama (fiktif stok kârı) kaynaklıdır."
        )
    elif is_capital_eroding:
        executive_assessment = (
            f"Sermaye Erimesi: Şirket kâr üretmektedir ancak net kâr ({_tl(net_profit)} TL), "
            f"özkaynakların enflasyona karşı korunması için gereken {_tl(equity_preservation_threshold)} TL "
            f"kârlılık eşiğinin altında kalmıştır. Şirket özkaynağı reel olarak yılda {_tl(capital_erosion_amount)} TL erimektedir."
        )
    else:
        executive_assessment = (
            f"Reel Kârlılık Pozitif: Şirket net kârı ({_tl(net_profit)} TL), "
            f"yıllık %{annual_inflation_rate*100:.0f} enflasyon ve stok ikame maliyetlerini karşılayarak "
            f"+{_tl(real_economic_profit)} TL reel ekonomik katma değer üretmektedir."
        )

    return {
        "annual_inflation_rate_pct": round(annual_inflation_rate * 100, 1),
        "nominal_net_profit": round(net_profit, 2),
        "nominal_net_margin_pct": round(nominal_margin_pct, 2),
        "phantom_inventory_profit": round(phantom_inventory_profit, 2),
        "stock_holding_days": round(stock_holding_days, 1),
        "net_monetary_position": round(net_monetary_position, 2),
        "monetary_position_loss": round(monetary_position_loss, 2),
        "equity_preservation_threshold": round(equity_preservation_threshold, 2),
        "real_economic_profit": round(real_economic_profit, 2),
        "real_net_margin_pct": round(real_margin_pct, 2),
        "margin_gap_pp": round(nominal_margin_pct - real_margin_pct, 2),
        "is_capital_eroding": is_capital_eroding,
        "capital_erosion_amount": round(capital_erosion_amount, 2),
        "severity": severity,
        "executive_assessment": executive_assessment,
    }
