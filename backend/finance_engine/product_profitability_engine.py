"""Product Profitability & Portfolio Intelligence Engine.

Evaluates SKU level performance: revenue contribution, gross margin %,
profit contribution, and correlation with inventory stock age and tied-up capital.
"""
from __future__ import annotations

from typing import Any


def build_product_profitability_analysis(
    sales_analysis: dict[str, Any] | None,
    inventory_analysis: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not sales_analysis or not sales_analysis.get('product_profitability'):
        return {
            'status': 'DATA_MISSING_EXPECTED',
            'reason': 'Ürün bazlı satış ve maliyet verisi (Satış Defteri) bulunamadı.',
            'products': [],
            'findings': [],
        }

    raw_prods = sales_analysis.get('product_profitability', [])
    total_sales = float(sales_analysis.get('net_sales') or sum(p.get('sales', 0) for p in raw_prods) or 1.0)
    total_profit = sum(p.get('gross_profit', 0) for p in raw_prods)
    company_margin_pct = float(sales_analysis.get('gross_margin', 0.25) * 100) if sales_analysis.get('gross_margin') is not None else 25.0

    # Build inventory lookup if available
    inv_by_sku: dict[str, float] = {}
    if inventory_analysis and isinstance(inventory_analysis.get('raw_rows'), list):
        for r in inventory_analysis['raw_rows']:
            p_name = str(r.get('product', '')).strip().lower()
            inv_by_sku[p_name] = inv_by_sku.get(p_name, 0.0) + float(r.get('value', 0.0))

    processed = []
    for p in raw_prods:
        name = str(p.get('name', 'Bilinmeyen Ürün'))
        s = float(p.get('sales', 0.0))
        c = float(p.get('cogs', 0.0))
        gp = float(p.get('gross_profit', s - c))
        margin_pct = float(p.get('gross_margin_pct') or ((gp / s * 100) if s > 0 else 0.0))
        sales_share = round((s / total_sales) * 100, 2) if total_sales > 0 else 0.0
        profit_share = round((gp / total_profit) * 100, 2) if total_profit > 0 else 0.0

        lookup = name.strip().lower()
        tied_inv = inv_by_sku.get(lookup, 0.0)

        # Strategic product classification
        if sales_share >= 15 and margin_pct >= company_margin_pct:
            category = "Lokomotif Kârlı"
        elif sales_share >= 15 and margin_pct < company_margin_pct:
            category = "Hacimli ama Marjı Düşük (Kârı Aşağı Çeken)"
        elif sales_share < 15 and margin_pct >= company_margin_pct:
            category = "Niş Yüksek Kârlı"
        else:
            category = "Düşük Katkı"

        processed.append({
            'name': name,
            'sales': round(s, 2),
            'cogs': round(c, 2),
            'gross_profit': round(gp, 2),
            'gross_margin_pct': round(margin_pct, 1),
            'sales_share_pct': sales_share,
            'profit_share_pct': profit_share,
            'inventory_tied_value': round(tied_inv, 2),
            'category': category,
        })

    processed.sort(key=lambda x: x['sales'], reverse=True)

    findings = []
    # Identify products with high sales but low margin
    drag_products = [p for p in processed if p['sales_share_pct'] >= 15 and p['gross_margin_pct'] < company_margin_pct]
    if drag_products:
        dp = drag_products[0]
        findings.append({
            'code': 'PP-001',
            'category': 'Ürün Kârlılığı',
            'severity': 'high',
            'title': f"{dp['name']} en yüksek cirolardan birini üretiyor ancak marjı kârı aşağı çekiyor",
            'detail': f"{dp['name']} toplam satışların %{dp['sales_share_pct']}'sini ({dp['sales']:,.0f} TL) oluşturuyor fakat brüt marjı %{dp['gross_margin_pct']:.1f} ile şirket ortalamasının (%{company_margin_pct:.1f}) belirgin şekilde altında kalmaktadır.",
            'evidence': [
                f"Satış Payı: %{dp['sales_share_pct']} ({dp['sales']:,.0f} TL)",
                f"Brüt Marj: %{dp['gross_margin_pct']:.1f} (Ortalama: %{company_margin_pct:.1f})",
                f"Toplam Kâra Katkı: %{dp['profit_share_pct']}"
            ],
            'recommendation': f"{dp['name']} için birim maliyet kırılımı, tedarikçi alım fiyatları ve satış fiyatlama politikası optimize edilerek marj en az 2-3 puan yukarı taşınmalıdır.",
            'confidence': 'high',
        })

    return {
        'status': 'PASS',
        'product_count': len(processed),
        'products': processed,
        'findings': findings,
    }
