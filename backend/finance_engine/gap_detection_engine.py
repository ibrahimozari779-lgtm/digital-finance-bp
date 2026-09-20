from __future__ import annotations
from typing import Any


def _pct(a, b):
    if a is None or b in (None, 0):
        return None
    return float(a) / float(b) * 100.0


def build_gap_detection(statements: dict[str, Any] | None, quality: dict[str, Any] | None,
                         data_hub: dict[str, Any] | None = None) -> dict[str, Any]:
    """Deterministic gap/weakness detector.

    It deliberately distinguishes observed weaknesses from missing evidence.
    Missing data is itself a finding because the platform is meant to expose
    what management cannot currently see, not pretend the blind spot is empty.
    """
    statements = statements or {}
    quality = quality or {}
    hub = data_hub or {}
    pl = statements.get('profit_and_loss') or {}
    bs = statements.get('balance_sheet') or {}
    k = statements.get('kpis') or {}
    findings: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []

    def add_gap(code, theme, severity, title, evidence, why, action, impact=None, confidence='high'):
        findings.append({
            'code': code, 'theme': theme, 'severity': severity, 'title': title,
            'evidence': evidence, 'why_it_matters': why, 'recommended_action': action,
            'estimated_impact': impact, 'confidence': confidence,
        })

    def add_missing(code, title, why, blocks, next_source):
        missing.append({'code': code, 'title': title, 'why_it_matters': why,
                        'blocked_intelligence': blocks, 'recommended_source': next_source,
                        'severity': 'medium'})

    # Financial core weaknesses
    de = k.get('debt_to_equity')
    finance = pl.get('Finance costs')
    op = pl.get('Operating profit')
    if de is not None and de > 5:
        add_gap('GAP-CAP-01','Capital Structure','critical','Sermaye yapısı aşırı borçlu',
                [f'Debt / Equity = {de:.2f}x', f"Financial debt = {float(k.get('financial_debt') or 0):,.0f} TL"],
                'Yüksek kaldıraç faiz, refinancing ve likidite hassasiyetini artırır.',
                'Borçları vade, faiz, para birimi ve teminat bazında çıkar; refinancing ve equity seçeneklerini karşılaştır.',
                impact=float(k.get('financial_debt') or 0)*0.10)
    if finance is not None and op not in (None,0):
        fco=float(finance)/float(op)
        if fco>0.60:
            add_gap('GAP-FIN-01','Profit Quality','critical','Finansman maliyeti faaliyet kârını aşındırıyor',
                    [f'Finance Cost / Operating Profit = {fco*100:.1f}%', f'Finance costs = {float(finance):,.0f} TL'],
                    'Faaliyet kârının önemli bölümü finansmana gidiyor; net kâra dönüşüm zayıflıyor.',
                    'Borç bazında faiz/vade analizi ve refinancing karşılaştırması yap.',
                    impact=float(finance))
    cr=k.get('current_ratio')
    if cr is not None and cr<1.2:
        add_gap('GAP-LIQ-01','Liquidity','medium','Likidite tamponu sınırlı',
                [f'Current Ratio = {cr:.2f}x', f"Cash = {float(k.get('cash') or 0):,.0f} TL"],
                'Kısa vadeli yükümlülükler için nakit tamponu sınırlanıyor.',
                '13 haftalık nakit planı ve minimum liquidity buffer tanımla.')
    rs=_pct(k.get('receivables'),pl.get('Net sales'))
    if rs is not None and rs>40:
        add_gap('GAP-WC-01','Working Capital','high','Alacaklar satışlara göre yüksek',
                [f'Receivables / Net Sales = {rs:.1f}%', f"Receivables = {float(k.get('receivables') or 0):,.0f} TL"],
                'Nakit işletme sermayesinde bağlı kalıyor ve finansman ihtiyacını artırabilir.',
                'AR aging ve müşteri bazlı vade/tahsilat analizi ile collection action list oluştur.',
                impact=float(k.get('receivables') or 0)*0.05, confidence='medium')

    gm=k.get('gross_margin_pct')
    if gm is not None and gm<15:
        add_gap('GAP-PROF-01','Profitability','high','Brüt marj baskı altında',
                [f'Gross Margin = {gm:.1f}%', f"COGS = {float(pl.get('COGS') or 0):,.0f} TL"],
                'Fiyatlama ve maliyet baskısı faaliyet kârı için tamponu azaltıyor.',
                'Ürün/müşteri bazında fiyat, indirim, hacim ve maliyet katkısını ayrıştır.')

    # Operational evidence from Data Hub
    summary=hub.get('summary') or {}
    an=hub.get('analysis') or {}
    sales=an.get('sales') or {}
    ar=an.get('ar_aging') or {}
    ap=an.get('ap_aging') or {}
    inv=an.get('inventory') or {}
    if sales:
        overdue=sales.get('overdue_amount_by_status')
        if overdue and overdue>0:
            add_gap('GAP-SALES-01','Collections','high','Satış kaynağında vadesi geçmiş bakiye var',
                    [f"Overdue = {float(overdue):,.0f} TL", f"Overdue rows = {sales.get('overdue_row_count',0)}"],
                    'Tahsilat riski doğrudan satış verisinde görülebiliyor.',
                    'Overdue müşterileri yaş, tutar ve yoğunlaşmaya göre sırala; tahsilat owner ve tarih ata.',
                    impact=float(overdue), confidence='high')
        prem=sales.get('term_premium_pct')
        if prem is not None and prem>10:
            add_gap('GAP-SALES-02','Pricing','medium','Vadeli fiyatlama primi yüksek',
                    [f'Term price premium = {prem:.1f}%'],
                    'Vade fiyatlaması marjı ve müşteri ödeme davranışını etkileyebilir.',
                    'Vade fiyatı, finansman maliyeti ve tahsilat riskini birlikte fiyatlama politikasına bağla.', confidence='high')
        top10=sales.get('top_10_customer_share_pct')
        if top10 is not None and top10>=30:
            add_gap('GAP-SALES-03','Commercial Risk','high','Müşteri yoğunlaşması yüksek',
                    [f'Top-10 customer share = {top10:.1f}%'],
                    'Satış ve tahsilat birkaç müşteri grubuna fazla bağımlı olabilir.',
                    'Top customers için exposure, margin, payment behaviour ve contingency plan oluştur.', confidence='high')
    if ar:
        overdue_pct=ar.get('overdue_pct')
        if overdue_pct is not None and overdue_pct>=20:
            add_gap('GAP-AR-01','Collections','high','AR aging vadesi geçmiş tutar içeriyor',
                    [f'Overdue AR = {float(ar.get("overdue") or 0):,.0f} TL', f'Overdue % = {overdue_pct:.1f}%'],
                    'Tahsilat gecikmesi doğrudan cash conversion ve liquidity üzerinde baskı yaratıyor.',
                    'En büyük gecikmiş müşteriler için tahsilat planı, dispute reason ve next action çıkar.',
                    impact=float(ar.get('overdue') or 0), confidence='high')
        conc=ar.get('top_10_share_pct')
        if conc is not None and conc>=50:
            add_gap('GAP-AR-02','Collections','medium','Alacak yoğunlaşması yüksek',
                    [f'Top-10 AR share = {conc:.1f}%'],
                    'Tahsilat performansı az sayıda müşteriyle yoğunlaşmış olabilir.',
                    'Top debtor risk map oluştur ve collection priority belirle.')
    if ap:
        overdue_pct=ap.get('overdue_pct')
        if overdue_pct is not None and overdue_pct>=20:
            add_gap('GAP-AP-01','Supplier Liquidity','high','Tedarikçi borçlarında vade baskısı var',
                    [f'Overdue AP = {float(ap.get("overdue") or 0):,.0f} TL', f'Overdue % = {overdue_pct:.1f}%'],
                    'Ödeme baskısı nakit planını sıkıştırabilir ve supplier riskini artırabilir.',
                    'Tedarikçi bazında vade, kritik tedarikçi ve ödeme önceliği matrisi oluştur.',
                    impact=float(ap.get('overdue') or 0), confidence='high')
    if inv:
        stale=inv.get('stale_180_amount')
        if stale and stale>0:
            add_gap('GAP-INV-01','Inventory','high','180+ gün yaşlanmış stok var',
                    [f'180+ day inventory = {float(stale):,.0f} TL'],
                    'Stokta bekleyen tutar nakit bağlar, değer düşüklüğü ve finansman maliyeti doğurur.',
                    'Ürün (SKU) bazında atıl ve yavaş hareket eden stok tasfiye planı ve nakit kurtarma hedefi belirle.',
                    impact=float(stale), confidence='high')

    # Missing intelligence should be explicit
    if not summary.get('sales_loaded'):
        add_missing('MISS-SALES','Satış verisi eksik','Müşteri, ürün, fiyatlama ve hacim kök nedenleri doğrulanamaz.',
                    ['customer/product concentration','pricing/mix','sales reconciliation'], 'Sales / invoice line export')
    if not summary.get('ar_aging_loaded'):
        add_missing('MISS-AR','AR aging eksik','Gerçek overdue exposure ve müşteri bazlı tahsilat davranışı doğrulanamaz.',
                    ['true DSO','overdue exposure','collection priority'], 'Customer AR aging / open invoices')
    if not summary.get('ap_aging_loaded'):
        add_missing('MISS-AP','AP aging eksik','Tedarikçi vade baskısı ve gerçek DPO doğrulanamaz.',
                    ['true DPO','supplier maturity risk'], 'Vendor AP aging / open invoices')
    if not summary.get('inventory_loaded'):
        add_missing('MISS-INV','Stok detayı eksik','DIO ve slow/obsolete stock analizi sınırlı kalır.',
                    ['true DIO','dead/excess stock','cash tied in inventory'], 'Inventory master + movements')
    if not (statements.get('period_metadata') or {}).get('available'):
        add_missing('MISS-PERIOD','Dönem bilgisi doğrulanamadı','Days-based metrics için fallback kullanılması gerekebilir.',
                    ['DSO/DPO/DIO','trend normalization'], 'Period-end / fiscal calendar')

    return {
        'gaps': findings,
        'missing_intelligence': missing,
        'gap_count': len(findings),
        'missing_count': len(missing),
        'severity_summary': {s:sum(1 for x in findings if x['severity']==s) for s in ('critical','high','medium','low')},
        'methodology': 'Gap engine deterministik finansal eşikler ve yüklenen operasyonel kaynak kanıtları kullanır; kanıt yoksa eksik istihbaratı açıkça işaretler.'
    }


def build_extended_root_cause(statements, base_root_cause, data_hub, gaps):
    """Promote the root-cause model from finance-only to cross-source investigation."""
    rc=dict(base_root_cause or {})
    chains=list(rc.get('causal_chains') or [])
    an=(data_hub or {}).get('analysis') or {}
    sales=an.get('sales') or {}; ar=an.get('ar_aging') or {}; ap=an.get('ap_aging') or {}; inv=an.get('inventory') or {}

    def add(code,title,problem,evidence,driver,impact,missing,actions,status='confirmed_by_data'):
        chains.append({'code':code,'title':title,'problem':problem,'evidence':evidence,'chain':[problem,driver,impact],
                       'primary_driver':driver,'financial_impact':impact,'required_additional_evidence':missing,
                       'recommended_actions':actions,'causal_status':status})
    # Sales -> AR -> cash -> financing chain
    if sales:
        outstanding=sales.get('outstanding_total')
        if outstanding and outstanding>0:
            e=[f"Sales outstanding = {float(outstanding):,.0f} TL"]
            if sales.get('overdue_amount_by_status'): e.append(f"Overdue = {float(sales['overdue_amount_by_status']):,.0f} TL")
            add('RC-OPS-CASH','Satış → Tahsilat → Nakit zinciri',
                'Satış kaynağında kapanmamış alacak bakiyesi bulunuyor',e,
                'Tahsilat döngüsü satış performansından sonra nakde dönüşümü belirliyor',
                'Uzayan tahsilat nakdi işletme sermayesinde tutar ve finansman ihtiyacını artırabilir',
                ['AR aging','payment terms','customer collection history'],
                ['Müşteri bazlı overdue listesi çıkar','13 haftalık nakit planına bağla'], 'likely_driver')
    if sales and sales.get('term_premium_pct') is not None and sales.get('term_premium_pct') > 10:
        add('RC-PRICE','Fiyatlama → Marj / Tahsilat zinciri','Vadeli fiyatlama ile peşin fiyat arasında belirgin fark var',
            [f"Term premium = {float(sales['term_premium_pct']):.1f}%"],
            'Vade fiyatlama politikası', 'Finansman maliyetinin ve tahsilat riskinin fiyatlara ne ölçüde yansıtıldığı belirsiz',
            ['customer-level payment terms','actual financing cost','product margin by payment term'],
            ['Vade primini customer/product bazında karşılaştır','Vade fiyatını financing cost + credit risk ile yeniden kalibre et'], 'confirmed_by_data')
    reconciliation=(data_hub or {}).get('reconciliation') or {}
    for chk in reconciliation.get('checks',[]):
        if chk.get('status')=='warning' and chk.get('difference') is not None:
            diff=abs(float(chk.get('difference') or 0))
            gl=abs(float(chk.get('gl_value') or 0))
            if diff>0 and (gl==0 or diff/max(gl,1)>0.002):
                add('RC-RECON','GL → Operasyon mutabakat zinciri',f"{chk.get('name')} mutabakatında fark var",
                    [f"GL = {float(chk.get('gl_value') or 0):,.0f} TL", f"Source = {float(chk.get('source_value') or 0):,.0f} TL", f"Difference = {float(chk.get('difference') or 0):,.0f} TL"],
                    'Kaynak kapsamı / dönem / mapping farkı', 'Operasyonel rapor ile GL arasında karar vermeden önce açıklanması gereken bir fark bulunuyor',
                    ['invoice exclusions','returns/discount mapping','period cut-off','reconciliation detail'],
                    ['Farkı belge bazında köprüle','Cut-off ve iade/iskonto mapping kontrolü yap'], 'confirmed_by_data')
                break

    if inv and inv.get('stale_180_amount'):
        add('RC-INV-CASH','Stok → Nakit dönüşüm zinciri','Yaşlanmış stok nakdi bağlıyor',
            [f"180+ inventory = {float(inv['stale_180_amount']):,.0f} TL"],
            'Yavaş hareket eden stok', 'Stokta bağlı nakit ve olası değer düşüklüğü riski',
            ['Stok hareket geçmişi','Satış hızı','Değer düşüklüğü karşılık politikası'],
            ['Atıl stok tasfiye planı','Ürün bazlı nakit kurtarma hedefi'], 'confirmed_by_data')
    if ap and ap.get('overdue'):
        add('RC-AP-CASH','Tedarikçi → Nakit zinciri','Ödenecek borçlarda vade baskısı var',
            [f"Overdue AP = {float(ap['overdue']):,.0f} TL"],
            'Tedarikçi vade baskısı', 'Kısa vadeli nakit ihtiyacı ve tedarikçi devamlılığı/mal temin riski',
            ['Tedarikçi kritiklik derecesi','Ödeme vadeleri','13 haftalık nakit planı'],
            ['Kritik tedarikçi önceliklendirmesi','Haftalık ödeme takvimi'], 'confirmed_by_data')

    # Convert missing intelligence into a first-class root cause/gap track.
    missing=[m['title'] for m in (gaps or {}).get('missing_intelligence',[])]
    if missing:
        chains.append({'code':'RC-DATA','title':'Karar Görünürlüğü Kök Nedeni',
                       'problem':'Bazı kritik yönetim kararları için veri görünürlüğü eksik',
                       'evidence':missing,
                       'chain':['Kritik operasyonel veri kaynakları eksik','Gerçek sürücüler tam doğrulanamıyor','Karar güveni sınırlanıyor'],
                       'primary_driver':'Eksik / parçalı operasyonel veri',
                       'financial_impact':'Yanlış önceliklendirme ve geciken aksiyon riski',
                       'required_additional_evidence':[m['recommended_source'] for m in (gaps or {}).get('missing_intelligence',[])],
                       'recommended_actions':['Eksik veri kaynaklarını Data Hub’a bağla','Kaynak → KPI coverage haritası oluştur'],
                       'causal_status':'data_gap'})
    rc['causal_chains']=chains
    rc['gap_detection']=gaps
    return rc
