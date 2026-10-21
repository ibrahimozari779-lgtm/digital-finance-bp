from __future__ import annotations
from typing import Any


def build_management_actions(findings, opportunities, statements, causal_chains=None, gap_detection=None, priority_by_code=None):
    """Consolidated management actions driven by findings + root-cause themes.

    The engine avoids one recommendation per symptom. Related findings are
    grouped under the same decision theme and a deterministic exposure proxy is
    shown only when there is evidence for it.

    Master Decision Hub wiring (Faz 1): `priority_by_code` is the Priority
    Score computed by Risk Ranking (severity x confidence x financial
    exposure - see risk_ranking_engine.py), keyed by finding code. When
    supplied, group ordering is driven by this score instead of a bare
    severity label, so a group's position here matches its position in the
    Risk Ranking list rather than being decided by an independent, second
    copy of "how severe is this" logic. Falls back to severity-only ordering
    when no priority map is supplied (e.g. direct/standalone calls).
    """
    mapping={
      'L001':('Borç bazında faiz oranı ve vade analizi çıkar; yeniden fiyatlama/refinansman seçeneklerini karşılaştır.','Finans & Hazine Yönetimi','0-30 gün','Finansman Gideri / Faaliyet Kârı'),
      'L002':('Kısa ve uzun vadeli borçları vade duvarı, faiz ve para birimi bazında yeniden yapılandırma senaryolarına ayır.','Finans & Hazine Yönetimi','0-30 gün','Net Borç / Özkaynak'),
      'D004':('Sermaye yapısı stres testi yap ve minimum likidite tamponunu tanımla.','Finans Yönetimi','0-30 gün','Borç / Aktif Oranı'),
      'D005':('Borç yoğunluğunu azaltacak finansman ve özkaynak seçeneklerini karşılaştır.','Finans & Hazine Yönetimi','0-30 gün','Borç / Aktif Oranı'),
      'D006':('Faiz karşılama stres testi ve borç servis kapasitesi analizi yap.','Finans & Hazine Yönetimi','0-30 gün','Faiz Karşılama Oranı'),
      'D007':('Faiz maliyetini azaltacak refinansman seçeneklerini değerlendir.','Finans & Hazine Yönetimi','30-60 gün','Faiz Karşılama Oranı'),
      'W001':('Alacak yaşlandırma ve müşteri bazlı vade/yoğunlaşma analizi ile tahsilat aksiyon listesi oluştur.','Kredi & Tahsilat Yönetimi','0-30 gün','Tahsilat Süresi (DSO) / Vadesi Geçen Alacak'),
      'WC004':('Alacak tahsilatı ile borç vade yapısını birlikte optimize et; 13 haftalık nakit planına bağla.','Finans & Nakit Yönetimi','0-30 gün','Nakit Çevrim Süresi (CCC) / Net Borç'),
      'Q001':('Kısa vadeli yükümlülük takvimini çıkar, minimum nakit tamponu ve acil kredi limitini belirle.','Finans & Hazine Yönetimi','0-30 gün','Cari Oran'),
      'Q002':('Minimum nakit tamponu ve tahsilat stres senaryolarını belirle.','Finans & Hazine Yönetimi','0-30 gün','Nakit Oran'),
      'Q003':('Serbest nakit yaratımı ve borç azaltımını birlikte planla.','Finans & Hazine Yönetimi','0-30 gün','Nakit / Finansal Borç'),
      'P002':('Brüt marjı müşteri/ürün/fiyatlama kırılımında incele ve düşük katkılı segmentleri yeniden fiyatla.','Ticari Satış Yönetimi','30-60 gün','Brüt Kâr Marjı'),
      'P003':('Fiyat listelerini maliyet enflasyonuna göre güncelle; iskonto yetkilerini sınırlandır.','Ticari Satış & Pazarlama','15-30 gün','Brüt Kâr Marjı'),
      'P004':('Faaliyet giderlerini (760 Pazarlama ve 770 Genel Yönetim) kalem bazında denetle; ciroya katkı sağlamayan sabit giderleri %10-%15 daralt.','Operasyon & Genel Yönetim','30-60 gün','Faaliyet Gideri / Net Satış'),
      'W002':('Depoda 75+ gün bekleyen yavaş/atıl stokları peşin iskonto kampanyasıyla nakde çevir; satınalma siparişlerini haftalık satış hızına bağla.','Tedarik Zinciri & Depo','15-30 gün','Stok Bekleme Süresi (DIO)'),
      'W003':('Müşteri tahsilat vadesi (DSO) ile tedarikçi ödeme vadesi (DPO) arasındaki negatif vade makasını kapat; açık hesap müşterileri DBS veya erken ödeme iskontosuna geçir.','Finans & Ticari Satış Yönetimi','0-30 gün','Net Vade Makası (DSO - DPO)'),
      'W005':('Kritik hammadde/mal tedarikçileriyle ödeme takvimini 13 haftalık nakit akışına göre yapılandır; peşin alım iskontosu fırsatlarını değerlendir.','Satınalma & Hazine Yönetimi','0-30 gün','Tedarikçi Ödeme Süresi (DPO)'),
      'L003':('Kasadaki atıl TL/döviz mevduatın bir kısmıyla en yüksek faizli kısa vadeli rotatif/KMH kredilerini kapatarak negatif faiz taşıma maliyetini sıfırla.','Finans & Hazine Yönetimi','0-15 gün','Net Faiz Gideri / Kasa Verimi'),
      'E001':('Ana faaliyet kârlılığını diğer gelirlerden ayrı takip et; tek seferlik gelir bağımlılığını test et.','Mali İşler & Planlama','30-60 gün','Faaliyet Kârı / Net Kâr'),
      'E002':('Defter kârının kasaya girmesini engelleyen alacak ve stok şişmesini 15 günlük tahsilat/stok eritme hedefiyle sıcak nakde dönüştür.','Genel Müdür & Finans Yönetimi','0-30 gün','Kârın Nakde Dönüşüm Oranı'),
      'A001':('Sermaye bağlayan varlıkları incele ve düşük devirli kalemleri azalt.','Operasyon Yönetimi','30-60 gün','Aktif Devir Hızı'),
      'GAP-SALES-01':('Vadesi geçmiş müşterileri tutar ve risk bazında sırala, tahsilat aksiyonlarını ata.','Kredi & Tahsilat Yönetimi','0-15 gün','Gecikmiş Alacak / Tahsilat Süresi'),
      'GAP-SALES-02':('Vadeli satış fiyat farkını finansman faiz maliyeti ile birlikte yeniden fiyatla.','Ticari Satış Yönetimi','0-30 gün','Vade Farkı / Brüt Kâr'),
      'GAP-SALES-03':('Müşteri yoğunlaşması için risk limiti ve teminat takip haritası oluştur.','Ticari Satış Yönetimi','0-30 gün','İlk 10 Müşteri Payı'),
      'GAP-AR-01':('Gecikmiş alacaklar için müşteri bazlı tahsilat planı ve yönetim eskalasyon süreci oluştur.','Kredi & Tahsilat Yönetimi','0-15 gün','Gecikmiş Alacak / Tahsilat Süresi'),
      'GAP-AR-02':('En büyük borçlular için müşteri risk limiti ve öncelikli tahsilat takvimi belirle.','Kredi & Tahsilat Yönetimi','0-30 gün','İlk 10 Alacak Payı'),
      'GAP-AP-01':('Kritik tedarikçileri önceliklendir ve ödeme takvimini 13 haftalık nakit akış planına bağla.','Satınalma & Hazine Yönetimi','0-30 gün','Tedarikçi Vadesi / Gecikmiş Borç'),
      'GAP-INV-01':('180+ gün stoklar için atıl stok tasfiye planı ve nakit kurtarma hedefi belirle.','Tedarik Zinciri & Depo','0-30 gün','Stok Bekleme Süresi / Atıl Stok'),
    }
    cluster_by_code={}; cluster_meta={}
    for chain in (causal_chains or []):
        cid=chain.get('code'); cluster_meta[cid]=chain
        for code in chain.get('related_findings',[]): cluster_by_code[code]=cid
    gap_by_theme={}
    for g in (gap_detection or {}).get('gaps',[]): gap_by_theme.setdefault(g.get('theme'),[]).append(g)

    severity_rank={'critical':3,'high':2,'medium':1}
    eligible=[f for f in findings if f.get('severity') in severity_rank]
    groups=[]; used=set()
    for f in eligible:
        if f.get('code') in used: continue
        cid=cluster_by_code.get(f.get('code'))
        if cid:
            group=[x for x in eligible if cluster_by_code.get(x.get('code'))==cid]
        else:
            # Consolidate obvious finance/liquidity duplicates even if no root-cause cluster exists.
            category=f.get('category')
            key='capital' if category=='Borçluluk' else category
            group=[x for x in eligible if (('capital' if x.get('category')=='Borçluluk' else x.get('category'))==key and key in {'capital','Likidite','İşletme Sermayesi'})]
            if not group: group=[f]
        for x in group: used.add(x.get('code'))
        groups.append(group)

    def _group_priority(group):
        """Priority Score for this group: the highest Risk Ranking score
        among its own finding codes when available, otherwise a severity-
        based fallback scaled to roughly the same 0-100 range so mixed
        priority_by_code/severity comparisons stay sane."""
        if priority_by_code:
            scored = [priority_by_code[x.get('code')] for x in group if x.get('code') in priority_by_code]
            if scored:
                return max(scored)
        return max(severity_rank.get(x.get('severity'), 0) for x in group) * 25.0

    groups.sort(key=lambda g: (_group_priority(g), len(g)), reverse=True)

    pl = (statements or {}).get('profit_and_loss') or {}
    k = (statements or {}).get('kpis') or {}
    fin_costs = float(pl.get('Finance costs') or 0.0)
    net_sales = float(pl.get('Net sales') or 0.0)
    opex = abs(float(pl.get('Operating expenses') or 0.0))
    other_inc = float(pl.get('Other income') or 0.0)
    receivables = float(k.get('receivables') or 0.0)
    inventory = float(k.get('inventory') or 0.0)
    payables = float(k.get('payables') or 0.0)
    fin_debt = float(k.get('financial_debt') or 0.0)

    theme_tr_map = {
        'Capital Structure': 'Sermaye & Borç Yapısı',
        'Borçluluk': 'Sermaye & Borç Yapısı',
        'Profit Quality': 'Kâr Kalitesi',
        'Working Capital': 'İşletme Sermayesi',
        'Collections': 'Alacak & Tahsilat Yönetimi',
        'Commercial Risk': 'Ticari Yoğunlaşma Riski',
        'Supplier Liquidity': 'Tedarikçi & Ödeme Dengesi',
        'Inventory': 'Stok & Depo Optimizasyonu',
        'Liquidity': 'Likidite Yönetimi',
    }

    def _fallback_impact(code_str: str) -> float | None:
        if code_str in {'L001', 'D006', 'D007'} and fin_costs > 0:
            return round(fin_costs * 0.25, 2)
        if code_str in {'L002', 'D004', 'D005', 'Q003'} and fin_debt > 0:
            return round(fin_debt * 0.15, 2)
        if code_str in {'W001', 'WC004', 'Q001', 'Q002', 'GAP-AR-01', 'GAP-AR-02', 'GAP-SALES-01', 'GAP-SALES-03'} and receivables > 0:
            return round(receivables * 0.15, 2)
        if code_str in {'P002', 'GAP-SALES-02'} and net_sales > 0:
            return round(net_sales * 0.015, 2)
        if code_str == 'P003' and opex > 0:
            return round(opex * 0.05, 2)
        if code_str == 'E001' and other_inc > 0:
            return round(other_inc * 0.50, 2)
        if code_str in {'A001', 'GAP-INV-01'} and inventory > 0:
            return round(inventory * 0.15, 2)
        if code_str == 'GAP-AP-01' and payables > 0:
            return round(payables * 0.15, 2)
        return None

    actions=[]
    for group in groups:
        if len(actions)>=8: break
        primary=sorted(group,key=lambda x:severity_rank.get(x.get('severity'),0),reverse=True)[0]
        code=primary.get('code'); a=mapping.get(code,(primary.get('recommendation',''), 'Finans & Hazine Yönetimi','30-60 gün', code))
        cid=cluster_by_code.get(code)
        cluster=cluster_meta.get(cid,{}) if cid else {}
        raw_theme=cluster.get('title') or ('Capital Structure' if primary.get('category')=='Borçluluk' else primary.get('category'))
        decision_theme=theme_tr_map.get(raw_theme, raw_theme)
        theme_aliases=[primary.get('category'), raw_theme, decision_theme]
        if primary.get('category')=='Borçluluk': theme_aliases += ['Capital Structure','Profit Quality']
        if primary.get('category')=='İşletme Sermayesi': theme_aliases += ['Working Capital','Collections']
        if primary.get('category')=='Likidite': theme_aliases += ['Liquidity']
        gaps=[]
        for t in theme_aliases:
            gaps += gap_by_theme.get(t,[])
        expected=next((g.get('estimated_impact') for g in gaps if g.get('estimated_impact') is not None),None)
        if expected is None:
            expected=_fallback_impact(code)
        kpis=[]
        for item in group:
            cand=mapping.get(item.get('code'))
            if cand: kpis.append(cand[3])
        kpis=list(dict.fromkeys(kpis))
        evidence_snippet=', '.join(e for e in (primary.get('evidence') or [])[:2] if e)
        action_text=a[0]
        if evidence_snippet:
            action_text=f"{a[0]} (Mevcut durum: {evidence_snippet}.)"
        actions.append({
            'action_id':f'ACT-{code}','finding_id':code,'merged_finding_codes':[x.get('code') for x in group] if len(group)>1 else None,
            'priority':len(actions)+1,'action':action_text,'owner':a[1],'time_horizon':a[2],
            'kpi':' / '.join(kpis) if kpis else a[3],'severity':primary.get('severity'),
            'decision_theme':decision_theme,'expected_financial_impact':expected,
            'expected_impact_label':'Tahmini Finansal Etki / Fırsat' if expected is not None else None,
            'priority_score':_group_priority(group),
        })
    # Add source-driven actions that are not represented by an accounting finding.
    represented_codes={a.get('finding_id') for a in actions}
    covered_themes={a.get('decision_theme') for a in actions}
    theme_aliases={
        'Capital Structure': {'Capital Structure','Sermaye & Borç Yapısı','Profit Quality','Kâr Kalitesi','Borçluluk','Finansman Baskısı Kök Nedeni'},
        'Working Capital': {'Working Capital','Collections','Alacak & Tahsilat Yönetimi','İşletme Sermayesi','İşletme Sermayesi Kök Nedeni'},
        'Liquidity': {'Liquidity','Likidite','Likidite Yönetimi'},
    }
    for gap in (gap_detection or {}).get('gaps', []):
        if len(actions)>=10: break
        if gap.get('severity') not in severity_rank: continue
        code=gap.get('code')
        if code in represented_codes: continue
        gtheme=gap.get('theme')
        gtheme_tr=theme_tr_map.get(gtheme, gtheme)
        # Specific operational actions remain visible even when their broader theme is already covered.
        force_source_action = code in {'GAP-SALES-01','GAP-SALES-02','GAP-AR-01','GAP-INV-01','GAP-AP-01'}
        # Do not create a second action for a problem already covered by the same strategic theme.
        skip=False
        for covered in covered_themes:
            if covered in {gtheme, gtheme_tr}: skip=True; break
            if any(covered in aliases and (gtheme in aliases or gtheme_tr in aliases) for aliases in theme_aliases.values()): skip=True; break
        if skip and not force_source_action: continue
        a=mapping.get(code,(gap.get('recommended_action',''), 'Finans & Hazine Yönetimi','30-60 gün', gtheme_tr or 'KPI'))
        gap_impact = gap.get('estimated_impact') if gap.get('estimated_impact') is not None else _fallback_impact(code)
        actions.append({
            'action_id':f'ACT-{code}','finding_id':code,'merged_finding_codes':None,'priority':len(actions)+1,
            'action':a[0],'owner':a[1],'time_horizon':a[2],'kpi':a[3], 'severity':gap.get('severity'),
            'decision_theme':gtheme_tr,'expected_financial_impact':gap_impact,
            'expected_impact_label':'Tahmini Finansal Etki / Fırsat' if gap_impact is not None else None,
            'priority_score':severity_rank.get(gap.get('severity'), 0) * 25.0,
        })
    return actions
