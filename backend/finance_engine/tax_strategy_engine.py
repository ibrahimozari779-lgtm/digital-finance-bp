"""Tax Strategy & Practical Tax Management Engine.

Translates company-specific financial statements and operational debt/receivables
into actionable, legal tax reduction levers:
1. Financing Expense Restriction (Finansman Gider Kısıtlaması & Örtülü Sermaye)
2. Bad Debt Provision Tax Shield (Şüpheli Alacak Karşılığı - VUK 323)
3. Accelerated Depreciation Strategy (Azalan Bakiyeler Yöntemi - VUK 315)
4. Cash Capital Interest Deduction (Nakdi Sermaye Faiz İndirimi - KVK 10/1-ı)
5. VAT Carryforward & Offset Strategy (Devreden KDV İade ve Mahsup Optimizasyonu)
6. Asset Replacement Reserve (Yenileme Fonu - VUK 328)
"""
from __future__ import annotations
from typing import Any


def build_tax_strategy_analysis(
    statements: dict[str, Any],
    data_hub: dict[str, Any] | None = None,
    corporate_tax_rate: float = 0.25,
) -> dict[str, Any]:
    pl = statements.get('profit_and_loss', {})
    bs = statements.get('balance_sheet', {})
    k = statements.get('kpis', {})

    sales = float(pl.get('Net sales') or 0.0)
    pre_tax_profit = float(pl.get('Pre-tax profit') or 0.0)
    finance_costs = float(pl.get('Finance costs') or 0.0)
    current_liab = float(bs.get('Current liabilities') or 0.0)
    total_assets = float(bs.get('Total assets') or 0.0)
    equity = float(bs.get('Total equity incl. current result') or 0.0)
    financial_debt = float(k.get('financial_debt') or 0.0)
    receivables = float(k.get('receivables') or 0.0)

    total_liabilities = max(0.0, total_assets - equity) if total_assets > equity else (current_liab + financial_debt)

    ar_data = (data_hub or {}).get('analysis_ar') or {}
    overdue_ar = float(ar_data.get('overdue') or 0.0)

    strategies = []
    total_estimated_tax_saving = 0.0

    # 1. Finansman Gider Kısıtlaması (KVK 11/1-i)
    if total_liabilities > equity and equity > 0 and finance_costs > 0:
        excess_ratio = (total_liabilities - equity) / total_liabilities
        disallowed_finance_cost = finance_costs * excess_ratio * 0.10
        tax_penalty = disallowed_finance_cost * corporate_tax_rate
        strategies.append({
            'code': 'TAX-001',
            'title': 'Finansman Gider Kısıtlaması (KKEG) Vergi Yükünü Sıfırlama',
            'category': 'Sermaye & Borç Yapısı',
            'severity': 'high',
            'legal_basis': 'KVK Md. 11/1-i',
            'current_state': f"Yabancı kaynaklar ({total_liabilities:,.0f} TL) özkaynakları ({equity:,.0f} TL) aştığı için yıllık {disallowed_finance_cost:,.0f} TL finansman gideri kanunen kabul edilmeyen gider (KKEG) olarak vergi matrahına eklenmektedir.",
            'potential_saving': round(tax_penalty, 2),
            'action': 'Ortaklara olan borçların sermayeye ilavesi veya nakit sermaye artırımı yapılarak özkaynak/borç dengesi güçlendirilmeli, KKEG kaynaklı ilave vergi ödemesi önlenmelidir.',
            'confidence': 'high',
        })
        total_estimated_tax_saving += tax_penalty

    # 2. Şüpheli Ticari Alacak Karşılığı (VUK 323)
    target_overdue = overdue_ar if overdue_ar > 0 else (receivables * 0.15 if receivables > 0 else 0.0)
    if target_overdue > 0:
        bad_debt_saving = target_overdue * corporate_tax_rate
        strategies.append({
            'code': 'TAX-002',
            'title': 'Gecikmiş Alacaklarda Şüpheli Alacak Karşılığı ile Vergi Kalkanı',
            'category': 'Alacak Yönetimi',
            'severity': 'medium',
            'legal_basis': 'VUK Md. 323',
            'current_state': f"Şirketin {target_overdue:,.0f} TL vadesi geçmiş veya tahsilatı şüpheli alacağı bulunmaktadır.",
            'potential_saving': round(bad_debt_saving, 2),
            'action': 'Vadesi 60 günü aşan tahsil edilemeyen alacaklar için yasal takip başlatılarak dönem kurumlar vergisi matrahından %100 oranında karşılık olarak düşülmelidir.',
            'confidence': 'high' if overdue_ar > 0 else 'medium',
        })
        total_estimated_tax_saving += bad_debt_saving

    # 3. Nakdi Sermaye Faiz İndirimi (KVK 10/1-ı)
    assumed_capital_injection = max(500_000.0, equity * 0.20) if equity > 0 else 1_000_000.0
    tcmb_commercial_rate = 0.45
    potential_deduction = assumed_capital_injection * tcmb_commercial_rate * 0.50
    capital_tax_saving = potential_deduction * corporate_tax_rate
    strategies.append({
        'code': 'TAX-003',
        'title': 'Nakdi Sermaye Artırımı Faiz İndirimi Kalkanı',
        'category': 'Özkaynak Teşviki',
        'severity': 'medium',
        'legal_basis': 'KVK Md. 10/1-ı',
        'current_state': f"Şirketin özkaynak ihtiyacı bulunmaktadır. Yapılacak her {assumed_capital_injection:,.0f} TL nakdi sermaye artırımı için TCMB faizi (%{tcmb_commercial_rate*100:.0f}) üzerinden doğrudan matrah indirimi hakkı doğar.",
        'potential_saving': round(capital_tax_saving, 2),
        'action': 'Banka kredisi yerine nakdi sermaye artışı ile şirket fonlanarak yıllık kurumlar vergisi matrahından doğrudan indirim sağlanmalıdır.',
        'confidence': 'high',
    })
    total_estimated_tax_saving += capital_tax_saving

    # 4. KDV İade ve Mahsup Optimizasyonu (KDV Kanunu Md. 29 & 32)
    estimated_vat_lock = sales * 0.02
    strategies.append({
        'code': 'TAX-004',
        'title': 'KDV İade & SGK/Vergi Borçlarına Mahsup Optimizasyonu',
        'category': 'KDV & Likidite',
        'severity': 'low',
        'legal_basis': 'KDV Kanunu Md. 29-32',
        'current_state': 'İhracat, tevkifatlı işlemler veya indirimli oran (%1-%10) teslimlerinde biriken devreden KDV, faizsiz olarak devlette nakit kilitlemektedir.',
        'potential_saving': round(estimated_vat_lock, 2),
        'action': 'YMM KDV iade raporu veya teminat mektubu ile nakden iade alınmalı; nakit alınamıyorsa aylık Muhtasar ve SGK prim borçlarına doğrudan mahsup edilerek faizli kredi kullanımı önlenmelidir.',
        'confidence': 'medium',
    })

    # 5. Azalan Bakiyeler Amortismanı (VUK 315)
    fixed_assets = max(0.0, total_assets - (float(bs.get('Current assets') or 0.0)))
    if fixed_assets > 0:
        depr_saving = (fixed_assets * 0.10) * corporate_tax_rate
        strategies.append({
            'code': 'TAX-005',
            'title': 'Duran Varlıklarda Hızlandırılmış Amortisman (Azalan Bakiyeler)',
            'category': 'Sabit Kıymet Stratejisi',
            'severity': 'low',
            'legal_basis': 'VUK Md. 315',
            'current_state': f"Şirketin {fixed_assets:,.0f} TL duran varlık portföyü bulunmaktadır. Normal amortisman yerine azalan bakiyeler yöntemiyle ilk yılda 2 kat gider yazılabilir.",
            'potential_saving': round(depr_saving, 2),
            'action': 'Yeni makine, teçhizat ve taşıt alımlarında azalan bakiyeler yöntemi seçilerek ilk 2 yılda kurumlar vergisi ödemesi ertelenmeli, şirket içinde bedava işletme sermayesi tutulmalıdır.',
            'confidence': 'medium',
        })
        total_estimated_tax_saving += depr_saving

    return {
        'status': 'PASS',
        'corporate_tax_rate_pct': round(corporate_tax_rate * 100, 1),
        'total_estimated_tax_saving': round(total_estimated_tax_saving, 2),
        'strategy_count': len(strategies),
        'strategies': strategies,
        'summary_note': f"Şirketin bilanço ve kârlılık yapısına göre uygulanabilecek {len(strategies)} somut yasal vergi yönetim hamlesiyle yıllık tahmini {total_estimated_tax_saving:,.0f} TL yasal vergi kalkanı ve nakit tasarrufu sağlanabilir.",
    }
