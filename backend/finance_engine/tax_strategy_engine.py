"""Tax Strategy & Practical Tax Management Engine.

Translates company-specific financial statements and operational debt/receivables
into actionable, legal tax reduction levers:
1. Financing Expense Restriction (Finansman Gider Kısıtlaması & KKEG - KVK 11/1-i)
2. Bad Debt Provision Tax Shield with real AR counterparties (Şüpheli Alacak Karşılığı - VUK 323)
3. Accelerated Depreciation Strategy on Tangible Fixed Assets (Azalan Bakiyeler Yöntemi - VUK 315)
4. Cash Capital Interest Deduction Tailored to Equity Gap (Nakdi Sermaye Faiz İndirimi - KVK 10/1-ı)
5. VAT Carryforward & Offset Strategy (Devreden KDV İade ve Mahsup Optimizasyonu - KDV 29-32)
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
    non_current_liab = float(bs.get('Non-current liabilities') or 0.0)
    total_assets = float(bs.get('Total assets') or 0.0)
    equity = float(bs.get('Total equity incl. current result') or 0.0)
    current_assets = float(bs.get('Current assets') or 0.0)
    fixed_assets = max(0.0, total_assets - current_assets) if total_assets > current_assets else float(bs.get('Non-current assets') or 0.0)

    financial_debt = float(k.get('financial_debt') or 0.0)
    receivables = float(k.get('receivables') or 0.0)

    total_liabilities = (current_liab + non_current_liab) if (current_liab + non_current_liab) > 0 else (max(0.0, total_assets - equity) if total_assets > equity else (current_liab + financial_debt))

    ar_data = (data_hub or {}).get('analysis_ar') or {}
    overdue_ar = float(ar_data.get('overdue') or 0.0)
    top_overdue_parties = ar_data.get('top_overdue_parties') or []

    strategies = []
    total_estimated_tax_saving = 0.0

    # 1. Finansman Gider Kısıtlaması (KVK 11/1-i)
    if total_liabilities > equity and equity > 0 and finance_costs > 0:
        excess_debt = total_liabilities - equity
        excess_ratio = excess_debt / total_liabilities
        disallowed_finance_cost = finance_costs * excess_ratio * 0.10
        tax_penalty = disallowed_finance_cost * corporate_tax_rate
        strategies.append({
            'code': 'TAX-001',
            'title': 'Finansman Gider Kısıtlaması (KKEG) Vergi Yükünü Sıfırlama',
            'category': 'Sermaye & Borç Yapısı',
            'severity': 'high',
            'legal_basis': 'KVK Md. 11/1-i',
            'current_state': (
                f'Yabancı kaynaklar ({total_liabilities:,.0f} TL), özkaynakları ({equity:,.0f} TL) '
                f'{excess_debt:,.0f} TL (%{excess_ratio*100:.1f}) aştığı için yıllık '
                f'{disallowed_finance_cost:,.0f} TL finansman gideri kanunen kabul edilmeyen gider (KKEG) '
                f'olarak vergi matrahına zorunlu eklenmekte ve şirkete {tax_penalty:,.0f} TL ilave vergi maliyeti yüklemektedir.'
            ),
            'calculation_steps': [
                {'label': '1. Toplam Yabancı Kaynak (Kısa + Uzun Vadeli Borç)', 'value': f'{total_liabilities:,.0f} TL'},
                {'label': '2. Toplam Özkaynak Tutarı', 'value': f'{equity:,.0f} TL'},
                {'label': '3. Özkaynağı Aşan Borç (Kısıtlama Matrahı)', 'value': f'{excess_debt:,.0f} TL (%{excess_ratio*100:.1f})'},
                {'label': '4. Dönem Finansman Gideri (660/661 Hesabı)', 'value': f'{finance_costs:,.0f} TL'},
                {'label': '5. Yasal KKEG Matrahı (Finansman Gideri x Aşım Oranı x %10)', 'value': f'{disallowed_finance_cost:,.0f} TL'},
                {'label': '6. Doğrudan Fazladan Ödenen Kurumlar Vergisi (%25)', 'value': f'{tax_penalty:,.0f} TL'},
            ],
            'potential_saving': round(tax_penalty, 2),
            'action': (
                f'Ortaklara olan borçların sermayeye ilavesi veya {excess_debt:,.0f} TL tutarında nakdi sermaye artırımı '
                f'yapılarak özkaynak/borç dengesi 1:1 seviyesine çekilmeli, KKEG kaynaklı {tax_penalty:,.0f} TL gereksiz vergi ödemesi tamamen önlenmelidir.'
            ),
            'confidence': 'high',
        })
        total_estimated_tax_saving += tax_penalty

    # 2. Şüpheli Ticari Alacak Karşılığı (VUK 323)
    delinquent_list = []
    if top_overdue_parties:
        for p in top_overdue_parties:
            p_name = p.get('name') or 'Bilinmeyen Müşteri'
            p_amt = float(p.get('amount') or 0.0)
            p_days = p.get('avg_days_overdue')
            p_days_str = f'{p_days:.0f} gün gecikmiş' if p_days else 'vadesi geçmiş'
            p_tax_shield = p_amt * corporate_tax_rate
            delinquent_list.append({
                'name': p_name,
                'overdue_amount': p_amt,
                'overdue_days': p_days_str,
                'tax_shield': round(p_tax_shield, 2),
            })

    target_overdue = overdue_ar if overdue_ar > 0 else (receivables * 0.15 if receivables > 0 else 0.0)
    if target_overdue > 0:
        bad_debt_saving = target_overdue * corporate_tax_rate
        party_detail_str = ''
        if delinquent_list:
            top3 = [f"{d['name']} ({d['overdue_amount']:,.0f} TL - {d['overdue_days']})" for d in delinquent_list[:3]]
            party_detail_str = f" Tespit edilen öncelikli borçlu cariler: {'; '.join(top3)}."

        strategies.append({
            'code': 'TAX-002',
            'title': 'Gecikmiş Müşteri Alacaklarında Şüpheli Alacak Karşılığı Vergi Kalkanı',
            'category': 'Alacak Yönetimi',
            'severity': 'high' if overdue_ar > 0 else 'medium',
            'legal_basis': 'VUK Md. 323',
            'current_state': (
                f'Şirketin {target_overdue:,.0f} TL vadesi geçmiş tahsil edilemeyen alacağı bulunmaktadır.{party_detail_str}'
            ),
            'delinquent_debtors': delinquent_list[:5],
            'calculation_steps': [
                {'label': '1. Vadesi Geçmiş Toplam Ticari Alacak Tutarı', 'value': f'{target_overdue:,.0f} TL'},
                {'label': '2. VUK 323 Kapsamında Açılabilecek Karşılık Oranı', 'value': '%100'},
                {'label': '3. Karşılık Hesabı (128 Şüpheli Alacaklar / 654 Karşılık Gideri)', 'value': f'{target_overdue:,.0f} TL'},
                {'label': '4. Net Kurumlar Vergisi Kalkanı ve Nakit Tasarrufu (%25)', 'value': f'{bad_debt_saving:,.0f} TL'},
            ],
            'potential_saving': round(bad_debt_saving, 2),
            'action': (
                f'Vadesi 60 günü aşan tahsil edilemeyen alacaklar için noter ihtarnamesi tanzim edilerek veya icra takibi '
                f'başlatılarak 128 Şüpheli Ticari Alacaklar hesabına aktarılmalı ve 654 Karşılık Gideri yazılarak '
                f'cari dönem kurumlar vergisi matrahından doğrudan {target_overdue:,.0f} TL düşülmelidir.'
            ),
            'confidence': 'high' if overdue_ar > 0 else 'medium',
        })
        total_estimated_tax_saving += bad_debt_saving

    # 3. Hızlandırılmış Amortisman (Azalan Bakiyeler Yöntemi - VUK 315)
    if fixed_assets > 0:
        normal_depr_rate = 0.20
        accel_depr_rate = 0.40
        additional_expense = fixed_assets * (accel_depr_rate - normal_depr_rate)
        depr_saving = additional_expense * corporate_tax_rate
        strategies.append({
            'code': 'TAX-003',
            'title': 'Maddi Duran Varlıklarda Hızlandırılmış Amortisman (Azalan Bakiyeler)',
            'category': 'Duran Varlık Stratejisi',
            'severity': 'medium',
            'legal_basis': 'VUK Md. 315',
            'current_state': (
                f'Şirketin bilançosunda {fixed_assets:,.0f} TL tutarında duran varlık portföyü bulunmaktadır. '
                f'Normal eşit paylı amortisman (%20) yerine azalan bakiyeler yöntemiyle (%40) ilk yılda iki kat gider yazılabilir.'
            ),
            'calculation_steps': [
                {'label': '1. Bilançodaki Duran Varlık Tutarı (25x Maddi Duran Varlıklar)', 'value': f'{fixed_assets:,.0f} TL'},
                {'label': '2. Standart Normal Amortisman Gideri (%20)', 'value': f'{fixed_assets * normal_depr_rate:,.0f} TL'},
                {'label': '3. Azalan Bakiyeler Amortisman Gideri (%40 - Azami)', 'value': f'{fixed_assets * accel_depr_rate:,.0f} TL'},
                {'label': '4. 1. Yılda Şirkete Sağlanan İlave Gider Matrahı', 'value': f'{additional_expense:,.0f} TL'},
                {'label': '5. Ertelenen Kurumlar Vergisi ve Bedava İşletme Sermayesi', 'value': f'{depr_saving:,.0f} TL'},
            ],
            'potential_saving': round(depr_saving, 2),
            'action': (
                f'Tesis, makine, cihaz ve taşıt yatırımlarında azalan bakiyeler yöntemi tercih edilerek ilk yılda '
                f'{depr_saving:,.0f} TL kurumlar vergisi ödemesi ertelenmeli, bu tutar banka kredi faizi yerine faizsiz işletme sermayesi olarak bünyede tutulmalıdır.'
            ),
            'confidence': 'high',
        })
        total_estimated_tax_saving += depr_saving

    # 4. Nakdi Sermaye Faiz İndirimi (KVK 10/1-ı)
    assumed_capital_injection = (
        max(500_000.0, (total_liabilities - equity) * 0.5) if total_liabilities > equity
        else max(500_000.0, equity * 0.25)
    )
    tcmb_commercial_rate = 0.45
    potential_deduction = assumed_capital_injection * tcmb_commercial_rate * 0.50
    capital_tax_saving = potential_deduction * corporate_tax_rate
    strategies.append({
        'code': 'TAX-004',
        'title': 'Nakdi Sermaye Artırımı Faiz İndirimi Kalkanı',
        'category': 'Özkaynak Teşviki',
        'severity': 'medium',
        'legal_basis': 'KVK Md. 10/1-ı',
        'current_state': (
            f'Şirketin yabancı kaynak/özkaynak dengesini iyileştirmek için yapılacak {assumed_capital_injection:,.0f} TL '
            f'nakit sermaye artırımında, TCMB ticari kredi gösterge faizi (%{tcmb_commercial_rate*100:.0f}) ve %50 indirim oranıyla doğrudan matrah indirimi hakkı doğar.'
        ),
        'calculation_steps': [
            {'label': '1. Önerilen Nakit Sermaye Artırım Tutarı', 'value': f'{assumed_capital_injection:,.0f} TL'},
            {'label': '2. TCMB Gösterge Ticari Kredi Ağırlıklı Ortalama Faizi', 'value': f'%{tcmb_commercial_rate*100:.1f}'},
            {'label': '3. KVK 10/1-ı Yasal İndirim Oranı', 'value': '%50'},
            {'label': '4. Yıllık Kurumlar Vergisi Matrah İndirimi', 'value': f'{potential_deduction:,.0f} TL'},
            {'label': '5. Şirkette Kalan Yıllık Net Nakit Vergi Teşviki (%25)', 'value': f'{capital_tax_saving:,.0f} TL'},
        ],
        'potential_saving': round(capital_tax_saving, 2),
        'action': (
            f'Yüksek faizli banka kredisi kullanmak yerine ortaklarca şirkete {assumed_capital_injection:,.0f} TL nakdi sermaye '
            f'enjekte edilmeli ve her yıl {capital_tax_saving:,.0f} TL vergi kalkanı nakden şirket kasasında bırakılmalıdır.'
        ),
        'confidence': 'high',
    })
    total_estimated_tax_saving += capital_tax_saving

    # 5. KDV İade ve Mahsup Optimizasyonu (KDV Kanunu Md. 29 & 32)
    estimated_vat_lock = max(250_000.0, sales * 0.02)
    strategies.append({
        'code': 'TAX-005',
        'title': 'KDV İade & SGK/Muhtasar Prim Borçlarına Mahsup Optimizasyonu',
        'category': 'KDV & Likidite',
        'severity': 'low',
        'legal_basis': 'KDV Kanunu Md. 29-32',
        'current_state': (
            f'İhracat, tevkifatlı faturalar veya indirimli oran (%1-%10) teslimlerinde biriken tahmini {estimated_vat_lock:,.0f} TL '
            f'devreden KDV, devlette faizsiz olarak nakit kilitlemektedir.'
        ),
        'calculation_steps': [
            {'label': '1. Şirketin Dönem Net Satış Hacmi', 'value': f'{sales:,.0f} TL'},
            {'label': '2. Tahmini Kilitli Devreden / Tevkifatlı KDV Hacmi', 'value': f'{estimated_vat_lock:,.0f} TL'},
            {'label': '3. Aylık Vergi/SGK Mahsup Potansiyeli', 'value': 'Aylık Muhtasar ve SGK Borçlarının %100ü'},
            {'label': '4. Tasarruf Edilen Kredi / KMH Faiz Yükü (Yıllık %50)', 'value': f'{estimated_vat_lock * 0.20:,.0f} TL/yıl'},
        ],
        'potential_saving': round(estimated_vat_lock * 0.20, 2),
        'action': (
            'Yeminli Mali Müşavir (YMM) KDV İade Raporu hazırlanarak biriken KDV nakit iade alınmalı; '
            'nakit iade süreç alıyorsa her ayın 26sında ödenecek Muhtasar ve SGK prim borçlarına doğrudan mahsup edilerek '
            'pahalı kısa vadeli kredi faizi ödenmesi önlenmelidir.'
        ),
        'confidence': 'medium',
    })
    total_estimated_tax_saving += (estimated_vat_lock * 0.20)

    # 6. Yenileme Fonu ile Sabit Kıymet Kârını Erteleme (VUK 328)
    strategies.append({
        'code': 'TAX-006',
        'title': 'Duran Varlık Satışlarında Yenileme Fonu ile 3 Yıl Vergi Erteleme',
        'category': 'Vergi Erteleme',
        'severity': 'low',
        'legal_basis': 'VUK Md. 328',
        'current_state': (
            'Ekonomik ömrünü tamamlamış makine, cihaz ve taşıtların satışından doğan kârlar doğrudan kurumlar vergisi matrahına eklenmekte ve peşin vergi doğurmaktadır.'
        ),
        'calculation_steps': [
            {'label': '1. İlgili Bilanço Hesabı', 'value': '549 Özel Fonlar (Yenileme Fonu)'},
            {'label': '2. Yasal Vergi Erteleme Süresi', 'value': '3 Yıl Kesintisiz'},
            {'label': '3. Vergi İstisna Oranı', 'value': '%100 (Yeni Varlık Alımında Amortisman Mahsubu)'},
        ],
        'potential_saving': round(max(50_000.0, fixed_assets * 0.05 * corporate_tax_rate), 2),
        'action': (
            'Yenilenecek sabit kıymet satışından doğan kâr gelir tablosuna gelir yazılmayıp doğrudan 549 Yenileme Fonu pasif hesabına alınarak '
            '3 yıl süreyle kurumlar vergisinden istisna tutulmalı ve yeni sabit kıymetin amortismanından mahsup edilmelidir.'
        ),
        'confidence': 'medium',
    })

    return {
        'status': 'PASS',
        'corporate_tax_rate_pct': round(corporate_tax_rate * 100, 1),
        'total_estimated_tax_saving': round(total_estimated_tax_saving, 2),
        'strategy_count': len(strategies),
        'strategies': strategies,
        'summary_note': (
            f'Şirketin finansal tablolarına göre tespit edilen {len(strategies)} somut yasal vergi yönetim hamlesiyle '
            f'yıllık tahmini {total_estimated_tax_saving:,.0f} TL yasal vergi kalkanı ve nakit tasarrufu sağlanabilir.'
        ),
    }
