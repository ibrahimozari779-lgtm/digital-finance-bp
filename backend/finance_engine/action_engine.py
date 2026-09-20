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
      'L001':('Borç bazında faiz oranı ve vade analizi çıkar; yeniden fiyatlama/refinansman seçeneklerini karşılaştır.','CFO / Treasury','0-30 gün','Finance Cost / Operating Profit'),
      'L002':('Kısa ve uzun vadeli borçları vade duvarı, faiz ve para birimi bazında yeniden yapılandırma senaryolarına ayır.','CFO / Treasury','0-30 gün','Net Debt / Equity'),
      'D004':('Sermaye yapısı stres testi yap ve minimum likidite tamponunu tanımla.','CFO','0-30 gün','Debt / Assets'),
      'D005':('Borç yoğunluğunu azaltacak finansman ve özkaynak seçeneklerini karşılaştır.','CFO / Treasury','0-30 gün','Debt / Assets'),
      'D006':('Faiz karşılama stres testi ve borç servis kapasitesi analizi yap.','CFO / Treasury','0-30 gün','Interest Coverage'),
      'D007':('Faiz maliyetini azaltacak refinansman seçeneklerini değerlendir.','CFO / Treasury','30-60 gün','Interest Coverage'),
      'W001':('AR aging ve müşteri bazlı vade/yoğunlaşma analizi ile tahsilat aksiyon listesi oluştur.','CFO / Credit Control','0-30 gün','DSO / Overdue AR'),
      'WC004':('Alacak tahsilatı ile borç vade yapısını birlikte optimize et; 13 haftalık nakit planına bağla.','CFO / Treasury','0-30 gün','CCC / Net Debt'),
      'Q001':('Kısa vadeli yükümlülük takvimini çıkar, minimum nakit tamponu ve acil kredi limitini belirle.','CFO / Treasury','0-30 gün','Current Ratio'),
      'Q002':('Minimum nakit tamponu ve tahsilat stres senaryolarını belirle.','CFO / Treasury','0-30 gün','Cash Ratio'),
      'Q003':('Serbest nakit yaratımı ve borç azaltımını birlikte planla.','CFO / Treasury','0-30 gün','Cash / Financial Debt'),
      'P002':('Brüt marjı müşteri/ürün/fiyatlama kırılımında incele ve düşük katkılı segmentleri ayır.','CFO / Commercial','30-60 gün','Gross Margin'),
      'P003':('Faaliyet giderlerini kalem bazında incele ve tasarruf alanlarını önceliklendir.','CFO / Operations','30-60 gün','OPEX / Net Sales'),
      'E001':('Ana faaliyet kârlılığını diğer gelirlerden ayrı takip et; tek seferlik gelir bağımlılığını test et.','CFO / FP&A','30-60 gün','Operating Profit / Net Profit'),
      'A001':('Sermaye bağlayan varlıkları incele ve düşük devirli kalemleri azalt.','CFO / Operations','30-60 gün','Asset Turnover'),
      'GAP-SALES-01':('Vadesi geçmiş müşterileri tutar ve risk bazında sırala, tahsilat aksiyonlarını ata.','CFO / Kredi Kontrol','0-15 gün','Gecikmiş Alacak / DSO'),
      'GAP-SALES-02':('Vadeli satış fiyat farkını finansman faiz maliyeti ile birlikte yeniden fiyatla.','CFO / Ticari Yönetim','0-30 gün','Vade Farkı / Brüt Kâr'),
      'GAP-SALES-03':('Müşteri yoğunlaşması için risk limiti ve teminat takip haritası oluştur.','CFO / Ticari Yönetim','0-30 gün','İlk 10 Müşteri Payı'),
      'GAP-AR-01':('Gecikmiş alacaklar için müşteri bazlı tahsilat planı ve yönetim eskalasyon süreci oluştur.','CFO / Kredi Kontrol','0-15 gün','Gecikmiş Alacak / DSO'),
      'GAP-AR-02':('En büyük borçlular için müşteri risk limiti ve öncelikli tahsilat takvimi belirle.','CFO / Kredi Kontrol','0-30 gün','İlk 10 Alacak Payı'),
      'GAP-AP-01':('Kritik tedarikçileri önceliklendir ve ödeme takvimini 13 haftalık nakit akış planına bağla.','CFO / Hazine','0-30 gün','Tedarikçi Vadesi / Gecikmiş Borç'),
      'GAP-INV-01':('180+ gün stoklar için atıl stok tasfiye planı ve nakit kurtarma hedefi belirle.','CFO / Operasyon','0-30 gün','Stok Bekleme Süresi / Atıl Stok'),
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

    actions=[]
    for group in groups:
        if len(actions)>=8: break
        primary=sorted(group,key=lambda x:severity_rank.get(x.get('severity'),0),reverse=True)[0]
        code=primary.get('code'); a=mapping.get(code,(primary.get('recommendation',''), 'Finance','30-60 gün', code))
        cid=cluster_by_code.get(code)
        cluster=cluster_meta.get(cid,{}) if cid else {}
        decision_theme=cluster.get('title') or ('Capital Structure' if primary.get('category')=='Borçluluk' else primary.get('category'))
        theme_aliases=[primary.get('category'), decision_theme]
        if primary.get('category')=='Borçluluk': theme_aliases += ['Capital Structure','Profit Quality']
        if primary.get('category')=='İşletme Sermayesi': theme_aliases += ['Working Capital','Collections']
        if primary.get('category')=='Likidite': theme_aliases += ['Liquidity']
        gaps=[]
        for t in theme_aliases:
            gaps += gap_by_theme.get(t,[])
        expected=next((g.get('estimated_impact') for g in gaps if g.get('estimated_impact') is not None),None)
        kpis=[]
        for item in group:
            cand=mapping.get(item.get('code'))
            if cand: kpis.append(cand[3])
        kpis=list(dict.fromkeys(kpis))
        # Data-driven, situational recommendation: the generic playbook
        # sentence (a[0]) states WHAT to do; this appends the company's own
        # current numbers from the finding's own evidence (already computed
        # from this period's statements), so the recommendation reads as
        # "given your %62 receivables-to-sales ratio, do X" rather than a
        # static template that would say the same thing regardless of the
        # figures. No new calculation is introduced here - only the evidence
        # already produced by the Decision Engine for this finding is quoted.
        evidence_snippet=', '.join(e for e in (primary.get('evidence') or [])[:2] if e)
        action_text=a[0]
        if evidence_snippet:
            action_text=f"{a[0]} (Mevcut durum: {evidence_snippet}.)"
        actions.append({
            'action_id':f'ACT-{code}','finding_id':code,'merged_finding_codes':[x.get('code') for x in group] if len(group)>1 else None,
            'priority':len(actions)+1,'action':action_text,'owner':a[1],'time_horizon':a[2],
            'kpi':' / '.join(kpis) if kpis else a[3],'severity':primary.get('severity'),
            'decision_theme':decision_theme,'expected_financial_impact':expected,
            'expected_impact_label':'Exposure / opportunity proxy' if expected is not None else None,
            'priority_score':_group_priority(group),
        })
    # Add source-driven actions that are not represented by an accounting finding.
    represented_codes={a.get('finding_id') for a in actions}
    covered_themes={a.get('decision_theme') for a in actions}
    theme_aliases={
        'Capital Structure': {'Capital Structure','Profit Quality','Borçluluk','Finansman Baskısı Kök Nedeni'},
        'Working Capital': {'Working Capital','Collections','İşletme Sermayesi','İşletme Sermayesi Kök Nedeni'},
        'Liquidity': {'Liquidity','Likidite'},
    }
    for gap in (gap_detection or {}).get('gaps', []):
        if len(actions)>=10: break
        if gap.get('severity') not in severity_rank: continue
        code=gap.get('code')
        if code in represented_codes: continue
        gtheme=gap.get('theme')
        # Specific operational actions remain visible even when their broader theme is already covered.
        force_source_action = code in {'GAP-SALES-01','GAP-SALES-02','GAP-AR-01','GAP-INV-01','GAP-AP-01'}
        # Do not create a second action for a problem already covered by the same strategic theme.
        skip=False
        for covered in covered_themes:
            if covered==gtheme: skip=True; break
            if any(covered in aliases and gtheme in aliases for aliases in theme_aliases.values()): skip=True; break
        if skip and not force_source_action: continue
        a=mapping.get(code,(gap.get('recommended_action',''), 'Finance','30-60 gün', gap.get('theme','KPI')))
        actions.append({
            'action_id':f'ACT-{code}','finding_id':code,'merged_finding_codes':None,'priority':len(actions)+1,
            'action':a[0],'owner':a[1],'time_horizon':a[2],'kpi':a[3], 'severity':gap.get('severity'),
            'decision_theme':gap.get('theme'),'expected_financial_impact':gap.get('estimated_impact'),
            'expected_impact_label':'Exposure / opportunity proxy' if gap.get('estimated_impact') is not None else None,
            'priority_score':severity_rank.get(gap.get('severity'), 0) * 25.0,
        })
    return actions
