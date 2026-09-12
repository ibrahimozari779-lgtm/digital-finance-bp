"""Customer Profitability & 4-Quadrant Intelligence Engine.

Classifies customers into strategic quadrants based on revenue and gross margin,
augmented by collection risk and overdue history from AR aging.
"""
from __future__ import annotations

from typing import Any


def build_customer_profitability_analysis(
    sales_analysis: dict[str, Any] | None,
    ar_analysis: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not sales_analysis or not sales_analysis.get('customer_profitability'):
        return {
            'status': 'DATA_MISSING_EXPECTED',
            'reason': 'Müşteri bazlı satış ve maliyet verisi (Satış Defteri) bulunamadı.',
            'quadrants': {'q1_stars': [], 'q2_high_volume_low_margin': [], 'q3_profitable_niche': [], 'q4_low_value': []},
            'customers': [],
            'findings': [],
        }

    raw_custs = sales_analysis.get('customer_profitability', [])
    total_sales = float(sales_analysis.get('net_sales') or sum(c.get('sales', 0) for c in raw_custs) or 1.0)
    company_margin_pct = float(sales_analysis.get('gross_margin', 0.25) * 100) if sales_analysis.get('gross_margin') is not None else 25.0

    # Build customer AR overdue map if AR analysis is available
    ar_overdue_by_customer: dict[str, float] = {}
    ar_total_by_customer: dict[str, float] = {}
    ar_days_by_customer: dict[str, float] = {}
    if ar_analysis and isinstance(ar_analysis.get('top_parties'), list):
        for p in ar_analysis['top_parties']:
            name = str(p.get('name', '')).strip().lower()
            ar_total_by_customer[name] = float(p.get('amount') or 0.0)
        if isinstance(ar_analysis.get('overdue_by_party'), dict):
            for k, v in ar_analysis['overdue_by_party'].items():
                ar_overdue_by_customer[str(k).strip().lower()] = float(v)
        if isinstance(ar_analysis.get('weighted_overdue_days_by_party'), dict):
            for k, v in ar_analysis['weighted_overdue_days_by_party'].items():
                ar_days_by_customer[str(k).strip().lower()] = float(v)

    # Calculate median or mean sales threshold for quadrants
    sales_values = [float(c.get('sales', 0)) for c in raw_custs]
    sales_threshold = sorted(sales_values)[len(sales_values) // 2] if sales_values else 0.0
    # Also define high revenue as >= 5% of total sales or above median
    sales_threshold = min(sales_threshold, total_sales * 0.05) if total_sales > 0 else sales_threshold

    processed = []
    q1, q2, q3, q4 = [], [], [], []

    for c in raw_custs:
        name = str(c.get('name', 'Bilinmeyen Müşteri'))
        s = float(c.get('sales', 0.0))
        cogs = float(c.get('cogs', 0.0))
        gp = float(c.get('gross_profit', s - cogs))
        margin_pct = float(c.get('gross_margin_pct') or ((gp / s * 100) if s > 0 else 0.0))
        share_pct = round((s / total_sales) * 100, 2) if total_sales > 0 else 0.0

        lookup = name.strip().lower()
        cust_ar = ar_total_by_customer.get(lookup, 0.0)
        cust_overdue = ar_overdue_by_customer.get(lookup, 0.0)
        cust_overdue_days = ar_days_by_customer.get(lookup, 0.0)
        overdue_ratio = (cust_overdue / cust_ar * 100) if cust_ar > 0 else 0.0

        # Collection health rating
        if cust_overdue_days > 60 or overdue_ratio > 50:
            collection_health = 'Kritik Gecikme'
            collection_color = 'critical'
        elif cust_overdue_days > 20 or overdue_ratio > 20:
            collection_health = 'Orta Risk'
            collection_color = 'high'
        else:
            collection_health = 'Düzenli'
            collection_color = 'positive'

        item = {
            'name': name,
            'sales': round(s, 2),
            'cogs': round(cogs, 2),
            'gross_profit': round(gp, 2),
            'gross_margin_pct': round(margin_pct, 1),
            'share_pct': share_pct,
            'ar_balance': round(cust_ar, 2),
            'ar_overdue': round(cust_overdue, 2),
            'overdue_days': round(cust_overdue_days, 1),
            'collection_health': collection_health,
            'collection_color': collection_color,
        }

        # Quadrant allocation
        is_high_sales = (s >= sales_threshold)
        is_high_margin = (margin_pct >= company_margin_pct)

        if is_high_sales and is_high_margin:
            item['quadrant'] = 'Q1_STARS'
            item['quadrant_label'] = 'Yıldız Müşteri (Yüksek Ciro / Yüksek Kâr)'
            q1.append(item)
        elif is_high_sales and not is_high_margin:
            item['quadrant'] = 'Q2_VOLUME_RISK'
            item['quadrant_label'] = 'Hacimli / Düşük Marj (Fiyat/Maliyet Baskısı)'
            q2.append(item)
        elif not is_high_sales and is_high_margin:
            item['quadrant'] = 'Q3_PROFITABLE_NICHE'
            item['quadrant_label'] = 'Kârlı Niş (Düşük Ciro / Yüksek Marj)'
            q3.append(item)
        else:
            item['quadrant'] = 'Q4_LOW_VALUE'
            item['quadrant_label'] = 'Düşük Değer (Düşük Ciro / Düşük Marj)'
            q4.append(item)

        processed.append(item)

    # Sort each quadrant by sales
    q1.sort(key=lambda x: x['sales'], reverse=True)
    q2.sort(key=lambda x: x['sales'], reverse=True)
    q3.sort(key=lambda x: x['sales'], reverse=True)
    q4.sort(key=lambda x: x['sales'], reverse=True)

    findings = []
    # Generate business partner insights
    if q2:
        worst_q2 = q2[0]
        findings.append({
            'code': 'CP-001',
            'category': 'Müşteri Kârlılığı',
            'severity': 'high',
            'title': f"{worst_q2['name']} yüksek ciro yaratıyor ancak kârlılığı şirket ortalamasının altında",
            'detail': f"{worst_q2['name']} toplam satışların %{worst_q2['share_pct']}'sini ({worst_q2['sales']:,.0f} TL) oluştururken, brüt kâr marjı %{worst_q2['gross_margin_pct']:.1f} seviyesinde kaldı (Şirket ortalaması: %{company_margin_pct:.1f}).",
            'evidence': [
                f"Müşteri Satışı: {worst_q2['sales']:,.0f} TL (Pay: %{worst_q2['share_pct']})",
                f"Müşteri Marjı: %{worst_q2['gross_margin_pct']:.1f} vs Ortalama %{company_margin_pct:.1f}",
                f"Tahsilat Durumu: {worst_q2['collection_health']}" + (f" ({worst_q2['overdue_days']} gün gecikme)" if worst_q2['overdue_days'] > 0 else "")
            ],
            'recommendation': f"{worst_q2['name']} ile yapılan sözleşme şartları, uygulanan iskonto oranları ve teslimat maliyetleri gözden geçirilerek marjı en az şirket ortalamasına (%{company_margin_pct:.1f}) çekecek fiyatlama yapılmalı.",
            'confidence': 'high',
        })

    # Risky large customers with delayed collection
    risky_big = [c for c in processed if c['share_pct'] >= 10 and c['collection_color'] in ('critical', 'high')]
    if risky_big:
        rb = risky_big[0]
        findings.append({
            'code': 'CP-002',
            'category': 'Tahsilat Riski',
            'severity': 'critical',
            'title': f"Büyük müşteri {rb['name']} üzerinde tahsilat gecikmesi nakit baskısı yaratıyor",
            'detail': f"{rb['name']} şirketin en büyük müşterilerinden biri (Pay: %{rb['share_pct']}), ancak {rb['ar_overdue']:,.0f} TL gecikmiş alacak bulunmaktadır (ortalama {rb['overdue_days']:.0f} gün gecikme). Yüksek ciro nakde dönüşememektedir.",
            'evidence': [
                f"Ciro Payı: %{rb['share_pct']}",
                f"Açık Bakiye: {rb['ar_balance']:,.0f} TL",
                f"Gecikmiş Tutar: {rb['ar_overdue']:,.0f} TL",
                f"Ortalama Gecikme: {rb['overdue_days']:.0f} gün"
            ],
            'recommendation': f"{rb['name']} için yeni vadeli sevkiyatlar mevcut açık bakiye tahsilat planına bağlanmalı, haftalık nakit tahsilat takip protokolü başlatılmalıdır.",
            'confidence': 'high',
        })

    return {
        'status': 'PASS',
        'company_average_gross_margin_pct': round(company_margin_pct, 1),
        'customer_count': len(processed),
        'stars': q1,
        'volume_chasers': q2,
        'niche_profit': q3,
        'low_value': q4,
        'quadrants': {
            'q1_stars': q1,
            'q2_high_volume_low_margin': q2,
            'q3_profitable_niche': q3,
            'q4_low_value': q4,
        },
        'quadrant_summary': {
            'q1_count': len(q1), 'q1_sales': round(sum(x['sales'] for x in q1), 2),
            'q2_count': len(q2), 'q2_sales': round(sum(x['sales'] for x in q2), 2),
            'q3_count': len(q3), 'q3_sales': round(sum(x['sales'] for x in q3), 2),
            'q4_count': len(q4), 'q4_sales': round(sum(x['sales'] for x in q4), 2),
        },
        'customers': processed,
        'findings': findings,
    }
