"""Profit Improvement Simulation Engine.

Calculates deterministic sensitivity scenarios for SME executives:
- +1 pt gross margin improvement -> annual EBIT impact
- +2 pt gross margin improvement -> annual EBIT impact
- Operating expense (OpEx) reduction -> annual EBIT impact
- Product mix optimization -> annual EBIT impact
Provides explicit assumptions and confidence notes.
"""
from __future__ import annotations

from typing import Any


def build_profit_improvement_analysis(
    statements: dict[str, Any],
    sales_analysis: dict[str, Any] | None = None,
) -> dict[str, Any]:
    pl = statements.get("profit_and_loss", {})
    net_sales = float(pl.get("Net sales") or 0.0)
    if not net_sales and sales_analysis:
        net_sales = float(sales_analysis.get("net_sales") or 0.0)

    operating_profit = float(pl.get("Operating profit") or 0.0)
    cogs = float(pl.get("Cost of sales") or 0.0)
    opex = float(pl.get("Operating expenses") or (float(pl.get("Gross profit") or 0.0) - operating_profit))

    if net_sales <= 0:
        return {
            'status': 'DATA_MISSING_EXPECTED',
            'reason': 'Net satış tutarı bulunamadığı için kârlılık simülasyonu çalıştırılamadı.',
            'scenarios': [],
        }

    # 1. Gross margin +1 percentage point (0.01 * net_sales)
    ebit_impact_1pt = round(net_sales * 0.01, 2)
    # 2. Gross margin +2 percentage points (0.02 * net_sales)
    ebit_impact_2pt = round(net_sales * 0.02, 2)
    # 3. OpEx -5% reduction
    ebit_impact_opex_5pct = round(abs(opex) * 0.05, 2) if opex > 0 else round(net_sales * 0.005, 2)
    # 4. Price increase +2% (assuming 0 volume elasticity)
    ebit_impact_price_2pct = round(net_sales * 0.02, 2)
    # 5. COGS direct cost efficiency -2%
    ebit_impact_cogs_2pct = round(abs(cogs) * 0.02, 2) if cogs > 0 else round(net_sales * 0.015, 2)

    scenarios = [
        {
            'lever': 'Brüt Marjda +1 Puan İyileşme',
            'lever_code': 'PI-01',
            'annual_ebit_impact': ebit_impact_1pt,
            'new_operating_profit': round(operating_profit + ebit_impact_1pt, 2),
            'ebit_growth_pct': round((ebit_impact_1pt / operating_profit * 100), 1) if operating_profit > 0 else None,
            'description': f"Net satışların ({net_sales:,.0f} TL) sabit kaldığı varsayımıyla, brüt marjın 1 puan artması yıllık yaklaşık {ebit_impact_1pt:,.0f} TL ek faaliyet kârı yaratır.",
            'action': 'İskonto kontrolü, tedarikçi alım müzakeresi veya kârlı ürün payının artırılması.',
            'assumption': 'Satış hacmi ve genel faaliyet giderlerinin sabit kaldığı varsayılmıştır.',
        },
        {
            'lever': 'Brüt Marjda +2 Puan İyileşme',
            'lever_code': 'PI-02',
            'annual_ebit_impact': ebit_impact_2pt,
            'new_operating_profit': round(operating_profit + ebit_impact_2pt, 2),
            'ebit_growth_pct': round((ebit_impact_2pt / operating_profit * 100), 1) if operating_profit > 0 else None,
            'description': f"Net satışların ({net_sales:,.0f} TL) sabit kaldığı varsayımıyla, brüt marjın 2 puan artması yıllık yaklaşık {ebit_impact_2pt:,.0f} TL ek faaliyet kârı yaratır.",
            'action': 'Fiyatlama revizyonu ve düşük marjlı ürünlerde kota/fiyat artışı.',
            'assumption': 'Satış hacmi ve genel faaliyet giderlerinin sabit kaldığı varsayılmıştır.',
        },
        {
            'lever': 'Faaliyet Giderlerinde (OpEx) %5 Tasarruf',
            'lever_code': 'PI-03',
            'annual_ebit_impact': ebit_impact_opex_5pct,
            'new_operating_profit': round(operating_profit + ebit_impact_opex_5pct, 2),
            'ebit_growth_pct': round((ebit_impact_opex_5pct / operating_profit * 100), 1) if operating_profit > 0 else None,
            'description': f"Mevcut faaliyet giderlerinden ({abs(opex):,.0f} TL) yapılacak %5 tasarruf doğrudan yıllık {ebit_impact_opex_5pct:,.0f} TL net kâr katkısı sağlar.",
            'action': 'Pazarlama, lojistik ve genel yönetim giderlerinde gereksiz harcamaların budanması.',
            'assumption': 'Operasyonel hizmet kalitesinin ve satış gücünün bozulmadığı varsayılmıştır.',
        },
        {
            'lever': 'Doğrudan Ürün Maliyetinde (COGS) %2 İndirim',
            'lever_code': 'PI-04',
            'annual_ebit_impact': ebit_impact_cogs_2pct,
            'new_operating_profit': round(operating_profit + ebit_impact_cogs_2pct, 2),
            'ebit_growth_pct': round((ebit_impact_cogs_2pct / operating_profit * 100), 1) if operating_profit > 0 else None,
            'description': f"Tedarikçilerle yapılacak toplu alım ve maliyet disiplini ile maliyetlerin %2 düşürülmesi yıllık {ebit_impact_cogs_2pct:,.0f} TL ek kâr bırakır.",
            'action': 'Kritik tedarikçilerde hacim iskontosu ve alternatif tedarikçi teklifleri alma.',
            'assumption': 'Ürün kalitesinin korunduğu varsayılmıştır.',
        },
        {
            'lever': 'Hedefli %2 Fiyat Artışı (Sabit Hacim)',
            'lever_code': 'PI-05',
            'annual_ebit_impact': ebit_impact_price_2pct,
            'new_operating_profit': round(operating_profit + ebit_impact_price_2pct, 2),
            'ebit_growth_pct': round((ebit_impact_price_2pct / operating_profit * 100), 1) if operating_profit > 0 else None,
            'description': f"Talep kaybı olmaksızın seçili ürün/müşterilerde uygulanacak ortalama %2 fiyat artışı yıllık yaklaşık {ebit_impact_price_2pct:,.0f} TL ek brüt kâr üretir.",
            'action': 'Fiyat esnekliği düşük (vazgeçilmez) ürün gruplarında fiyat güncellemesi.',
            'assumption': 'Müşteri sipariş hacminde düşüş yaşanmadığı varsayılmıştır.',
        },
    ]

    total_potential = round(ebit_impact_1pt + ebit_impact_opex_5pct, 2)

    return {
        'status': 'PASS',
        'net_sales': net_sales,
        'current_operating_profit': operating_profit,
        'scenarios': scenarios,
        'combined_quick_win_impact': total_potential,
        'summary_narrative': f"Brüt marjda sadece 1 puanlık iyileşme ve faaliyet giderlerinde %5 tasarruf ile şirketin yıllık faaliyet kârı yaklaşık {total_potential:,.0f} TL (%{(total_potential/operating_profit*100):.1f} artış) artırılabilir.",
    }
