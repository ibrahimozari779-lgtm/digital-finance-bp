"""Pricing Opportunity & Target Margin Engine.

Simulates pricing adjustments across customer and product portfolios,
evaluating target margin gaps and the profit sensitivity of price increases.
"""
from __future__ import annotations

from typing import Any


def build_pricing_opportunity_analysis(
    sales_analysis: dict[str, Any] | None,
    target_margin_pct: float = 30.0,
) -> dict[str, Any]:
    if not sales_analysis or not sales_analysis.get('net_sales'):
        return {
            'status': 'DATA_MISSING_EXPECTED',
            'reason': 'Fiyatlama analizi için satış detay verisi bulunamadı.',
            'opportunities': [],
        }

    net_sales = float(sales_analysis.get('net_sales') or 0.0)
    cogs = float(sales_analysis.get('cogs') or 0.0)
    current_margin_pct = float(sales_analysis.get('gross_margin', 0.0) * 100) if sales_analysis.get('gross_margin') is not None else 0.0

    prods = sales_analysis.get('product_profitability', [])
    custs = sales_analysis.get('customer_profitability', [])

    # Identify items below target margin
    low_margin_products = []
    for p in prods:
        m = float(p.get('gross_margin_pct') or 0.0)
        s = float(p.get('sales') or 0.0)
        c = float(p.get('cogs') or 0.0)
        if m < target_margin_pct and s > 0:
            # required sales price for target margin: price = cost / (1 - target_margin)
            req_sales = c / (1 - target_margin_pct / 100) if target_margin_pct < 100 else s
            price_gap = req_sales - s
            low_margin_products.append({
                'name': p.get('name'),
                'current_sales': round(s, 2),
                'cogs': round(c, 2),
                'current_margin_pct': round(m, 1),
                'target_margin_pct': target_margin_pct,
                'required_price_increase_pct': round((price_gap / s) * 100, 1) if s > 0 else 0.0,
                'additional_profit_potential': round(price_gap, 2),
            })

    low_margin_products.sort(key=lambda x: x['additional_profit_potential'], reverse=True)

    # Scenarios for company-wide price increase
    elasticity_scenarios = [
        {
            'price_change_pct': 1.0,
            'assumed_volume_change_pct': 0.0,
            'profit_impact': round(net_sales * 0.01, 2),
            'note': '%1 fiyat artışı (hacim sabit varsayımıyla)',
        },
        {
            'price_change_pct': 2.0,
            'assumed_volume_change_pct': 0.0,
            'profit_impact': round(net_sales * 0.02, 2),
            'note': '%2 fiyat artışı (hacim sabit varsayımıyla)',
        },
        {
            'price_change_pct': 3.0,
            'assumed_volume_change_pct': -0.5,
            'profit_impact': round((net_sales * 1.03 * 0.995) - (cogs * 0.995) - (net_sales - cogs), 2),
            'note': '%3 fiyat artışı (talepte %0.5 esneklik kaybı varsayımıyla)',
        },
    ]

    findings = []
    if low_margin_products:
        top_low = low_margin_products[0]
        findings.append({
            'code': 'PO-001',
            'category': 'Fiyatlama Fırsatı',
            'severity': 'medium',
            'title': f"{top_low['name']} için hedef marj revizyonu kârlılığı destekleyebilir",
            'detail': f"{top_low['name']} mevcut %{top_low['current_margin_pct']:.1f} brüt marj ile satılmaktadır. Hedef marj olan %{target_margin_pct:.0f}'e ulaşmak için yaklaşık %{top_low['required_price_increase_pct']:.1f} fiyat artışı gerekmektedir.",
            'evidence': [
                f"Mevcut Ciro: {top_low['current_sales']:,.0f} TL",
                f"Mevcut Marj: %{top_low['current_margin_pct']:.1f}",
                f"Hedef Marj: %{target_margin_pct:.0f}",
                f"Potansiyel Kâr Katkısı: {top_low['additional_profit_potential']:,.0f} TL",
            ],
            'recommendation': f"{top_low['name']} ürününün pazar rekabeti kontrol edilerek aşamalı fiyat artışı veya girdi maliyet optimizasyonu uygulanmalıdır.",
            'confidence': 'medium',
        })

    return {
        'status': 'PASS',
        'current_margin_pct': round(current_margin_pct, 1),
        'target_margin_pct': target_margin_pct,
        'low_margin_products': low_margin_products[:10],
        'elasticity_scenarios': elasticity_scenarios,
        'findings': findings,
    }
