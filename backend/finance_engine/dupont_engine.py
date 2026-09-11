"""DuPont 3-Stage and 5-Stage Value Driver Decomposition Engine."""
from __future__ import annotations
from typing import Any

def build_dupont_analysis(statements: dict[str, Any]) -> dict[str, Any]:
    pl = statements.get('profit_and_loss', {})
    bs = statements.get('balance_sheet', {})
    k = statements.get('kpis', {})

    sales = float(pl.get('Net sales') or 0.0)
    op = float(pl.get('Operating profit') or 0.0)
    pbt = float(pl.get('Pre-tax profit') or 0.0)
    net_profit = float(pl.get('Net profit') or 0.0)

    total_assets = float(bs.get('Total assets') or 0.0)
    total_equity = float(bs.get('Total equity incl. current result') or 0.0)

    # 3-Stage DuPont
    # 1. Net Profit Margin (Profitability)
    net_profit_margin_pct = (net_profit / sales * 100.0) if sales > 0 else 0.0
    # 2. Asset Turnover (Efficiency)
    asset_turnover = (sales / total_assets) if total_assets > 0 else 0.0
    # 3. Equity Multiplier / Financial Leverage (Solvency/Leverage)
    equity_multiplier = (total_assets / total_equity) if total_equity > 0 else 0.0

    # Calculated ROE & ROA
    roe_pct = (net_profit / total_equity * 100.0) if total_equity > 0 else 0.0
    roa_pct = (net_profit / total_assets * 100.0) if total_assets > 0 else 0.0

    # 5-Stage DuPont Extensions (Tax Burden, Interest Burden, Operating Margin)
    tax_burden = (net_profit / pbt) if pbt > 0 else (1.0 if net_profit >= 0 else 0.0)
    interest_burden = (pbt / op) if op > 0 else (1.0 if pbt >= 0 else 0.0)
    operating_margin_pct = (op / sales * 100.0) if sales > 0 else 0.0

    # Diagnosis & Primary Driver of Value
    diagnosis = []
    if roe_pct < 5.0:
        diagnosis.append("Özkaynak kârlılığı (ROE) sermaye maliyetinin altında, hissedar değeri erozyonu riski var.")
    elif roe_pct > 25.0:
        diagnosis.append("Yüksek özkaynak kârlılığı (ROE) sergileniyor.")

    if equity_multiplier > 4.0:
        diagnosis.append(f"Finansal kaldıraç çarpanı {equity_multiplier:.2f}x ile yüksek; kârlılık borçlanma üzerinden kaldıraçlanıyor, risk yüksek.")
    elif equity_multiplier < 1.5:
        diagnosis.append(f"Muhafazakar sermaye yapısı ({equity_multiplier:.2f}x kaldıraç çarpanı); borçlanma kapasitesi mevcut.")

    if asset_turnover < 0.8:
        diagnosis.append(f"Varlık devir hızı ({asset_turnover:.2f}x) düşük; varlıkların satış üretme verimliliği artırılmalı.")
    elif asset_turnover > 2.0:
        diagnosis.append(f"Yüksek varlık devir hızı ({asset_turnover:.2f}x); sermaye etkin kullanılıyor.")

    return {
        "roe_pct": round(roe_pct, 2),
        "roa_pct": round(roa_pct, 2),
        "net_profit_margin_pct": round(net_profit_margin_pct, 2),
        "asset_turnover": round(asset_turnover, 2),
        "equity_multiplier": round(equity_multiplier, 2),
        "operating_margin_pct": round(operating_margin_pct, 2),
        "interest_burden": round(interest_burden, 2),
        "tax_burden": round(tax_burden, 2),
        "tree": {
            "roe": {"value": round(roe_pct, 2), "label": "Özkaynak Kârlılığı (ROE %)"},
            "roa": {"value": round(roa_pct, 2), "label": "Aktif Kârlılığı (ROA %)"},
            "margin": {"value": round(net_profit_margin_pct, 2), "label": "Net Kâr Marjı (%)"},
            "turnover": {"value": round(asset_turnover, 2), "label": "Varlık Devir Hızı (x)"},
            "leverage": {"value": round(equity_multiplier, 2), "label": "Finansal Kaldıraç Çarpanı (x)"}
        },
        "diagnosis": diagnosis,
        "methodology": "DuPont 3 ve 5 aşamalı ayrıştırma: ROE = Net Marj x Varlık Devir Hızı x Kaldıraç Çarpanı."
    }
