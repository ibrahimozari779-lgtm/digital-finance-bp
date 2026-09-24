from __future__ import annotations
import pandas as pd
from datetime import datetime
from typing import Any
from .numeric_utils import to_numeric_series
from .date_utils import safe_dates

def _num(s):
    return to_numeric_series(s)

# Simple, deterministic collection-risk weights by aging bucket. Not a formal
# expected-credit-loss model - just a transparent proxy so a CFO can see which
# slice of the overdue balance is most likely to become a write-off, without
# needing separate aging software. 0-30 days overdue rarely turns into a real
# loss; 180+ days overdue frequently does.
_RISK_WEIGHT_BY_BUCKET = {
    'Current': 0.00, '1-30': 0.02, '31-60': 0.08, '61-90': 0.20, '91-180': 0.45, '180+': 0.75,
}


def _risk_tier(overdue_pct: float | None, weighted_days: float | None, concentration_pct: float | None) -> str:
    score = 0
    if overdue_pct is not None:
        score += 3 if overdue_pct >= 40 else 2 if overdue_pct >= 20 else 1 if overdue_pct >= 10 else 0
    if weighted_days is not None:
        score += 3 if weighted_days >= 120 else 2 if weighted_days >= 60 else 1 if weighted_days >= 30 else 0
    if concentration_pct is not None:
        score += 2 if concentration_pct >= 60 else 1 if concentration_pct >= 40 else 0
    if score >= 6: return 'Kritik'
    if score >= 4: return 'Yüksek'
    if score >= 2: return 'Orta'
    return 'Düşük'


def _aging(df,mapping,kind,as_of_date=None):
    work=df.copy(); out={}
    amount_col=mapping.get('outstanding') or mapping.get('amount')
    if amount_col:
        work['_amt']=_num(work[amount_col])
    else:
        work['_amt']=0.0
    if mapping.get('due_date'): work['_due']=safe_dates(work[mapping['due_date']])
    else: work['_due']=None
    today = None
    if as_of_date:
        try:
            today = datetime.fromisoformat(str(as_of_date)[:10])
        except Exception:
            today = None
    if not today:
        valid_dues = work['_due'].dropna() if work['_due'] is not None else None
        if valid_dues is not None and len(valid_dues) > 0:
            today = max(valid_dues)
        else:
            today = datetime.now()
    elif work['_due'] is not None:
        valid_dues = work['_due'].dropna()
        if len(valid_dues) > 0:
            years = [d.year for d in valid_dues if hasattr(d, 'year')]
            if years:
                median_year = sorted(years)[len(years) // 2]
                if abs(today.year - median_year) > 2:
                    today = datetime(median_year, 12, 31)

    work['_days'] = work['_due'].map(lambda due: min(730, max(-365, (today - due).days)) if due else None)
    known_days = work['_days'].fillna(0)
    out['rows']=len(work); out['outstanding']=float(work['_amt'].sum()); out['overdue']=float(work.loc[known_days>0,'_amt'].sum())
    out['overdue_pct']=out['overdue']/out['outstanding']*100 if out['outstanding'] else None
    buckets=[('Current',(-10**9,0)),('1-30',(1,30)),('31-60',(31,60)),('61-90',(61,90)),('91-180',(91,180)),('180+',(181,10**9))]
    bucket_amounts={n: float(work.loc[(known_days>=lo)&(known_days<=hi),'_amt'].sum()) for n,(lo,hi) in buckets}
    bucket_counts={n: int(((known_days>=lo)&(known_days<=hi)).sum()) for n,(lo,hi) in buckets}
    out['aging_buckets']=[{
        'bucket': n,
        'amount': bucket_amounts[n],
        'count': bucket_counts[n],
        'pct_of_outstanding': round(bucket_amounts[n]/out['outstanding']*100, 1) if out['outstanding'] else None,
    } for n,_ in buckets]
    # FIX (customer-trust bug): a bucket can have count > 0 with amount == 0
    # (e.g. invoices already settled to zero but whose due date still falls in
    # an aged bucket). Left unexplained, this looks like a broken report to a
    # buyer comparing row counts against amounts. Surface it explicitly.
    zero_amount_buckets = [n for n, _ in buckets if bucket_counts[n] > 0 and bucket_amounts[n] == 0]
    out['data_anomalies'] = (
        [f"'{n}' aralığında {bucket_counts[n]} kayıt var ama toplam tutar 0 TL — muhtemelen bakiyesi kapanmış (tamamen tahsil/ödenmiş) ama vade tarihi bu aralığa düşen kayıtlar."
         for n in zero_amount_buckets]
    )
    # Deterministic expected-loss proxy: sum(bucket amount × bucket risk weight).
    # Purely a transparency aid for prioritization, not a formal provisioning policy.
    out['collection_risk_estimate'] = round(sum(bucket_amounts[n] * _RISK_WEIGHT_BY_BUCKET.get(n, 0.0) for n, _ in buckets), 2)
    out['collection_risk_estimate_pct_of_outstanding'] = round(out['collection_risk_estimate']/out['outstanding']*100, 1) if out['outstanding'] else None
    party=mapping.get('customer') if kind=='AR' else mapping.get('vendor')
    if party:
        grp=work.groupby(party,dropna=False)['_amt'].sum().sort_values(ascending=False)
        out['party_count']=len(grp)
        out['top_parties']=[{
            'name': str(k), 'amount': float(v),
            'pct_of_outstanding': round(float(v)/out['outstanding']*100, 1) if out['outstanding'] else None,
        } for k, v in grp.head(10).items()]
        out['top_10_share_pct']=float(grp.head(10).sum()/out['outstanding']*100) if out['outstanding'] else None
        # 80% concentration ("Pareto") analysis: how many counterparties make up
        # ~80% of total outstanding exposure. Computed over the FULL party list
        # (not just top 10) so this is exact, not an estimate from a truncated
        # sample. Used to answer "which handful of customers/suppliers actually
        # matter" without forcing the reader to read a full ledger dump.
        if out['outstanding']:
            cum = grp.cumsum()
            n80 = int((cum < out['outstanding'] * 0.8).sum()) + 1
            n80 = min(n80, len(grp))
            out['concentration_80pct_party_count'] = n80
            out['concentration_80pct_share_of_parties_pct'] = round(n80 / len(grp) * 100, 1) if len(grp) else None
            out['concentration_80pct_amount'] = float(grp.head(n80).sum())
        else:
            out['concentration_80pct_party_count'] = None
            out['concentration_80pct_share_of_parties_pct'] = None
            out['concentration_80pct_amount'] = None
        overdue_mask = known_days > 0
        overdue_by_party = work.loc[overdue_mask].groupby(party,dropna=False)['_amt'].sum().sort_values(ascending=False)
        days_by_party = (
            work.loc[overdue_mask].assign(_w=work.loc[overdue_mask,'_amt']*work.loc[overdue_mask,'_days'])
            .groupby(party,dropna=False)
            .agg(_w=('_w','sum'), _amt=('_amt','sum'))
        )
        out['overdue_by_party'] = {str(k): float(v) for k, v in overdue_by_party.items()}
        out['weighted_overdue_days_by_party'] = {
            str(k): round(float(days_by_party.loc[k, '_w'] / days_by_party.loc[k, '_amt']), 1)
            for k in days_by_party.index if days_by_party.loc[k, '_amt'] > 0
        }
        out['top_overdue_parties'] = [{
            'name': str(k), 'amount': float(v),
            'avg_days_overdue': round(float(days_by_party.loc[k, '_w'] / days_by_party.loc[k, '_amt']), 1) if k in days_by_party.index and days_by_party.loc[k, '_amt'] else None,
        } for k, v in overdue_by_party.head(10).items()]
    else:
        out['party_count'] = None; out['top_parties'] = []; out['top_10_share_pct'] = None; out['top_overdue_parties'] = []
        out['overdue_by_party'] = {}; out['weighted_overdue_days_by_party'] = {}
    out['weighted_average_overdue_days'] = float((work.loc[known_days > 0, '_days'] * work.loc[known_days > 0, '_amt']).sum() / out['overdue']) if out['overdue'] else None
    out['kind'] = kind
    out['risk_tier'] = _risk_tier(out['overdue_pct'], out['weighted_average_overdue_days'], out['top_10_share_pct'])
    return out

def analyze_ar(df, mapping, net_sales=None, period_days=365, as_of_date=None):
    r = _aging(df, mapping, 'AR', as_of_date=as_of_date)
    dso = round(r['outstanding'] / net_sales * period_days, 1) if net_sales and net_sales > 0 else None
    r['dso_days'] = dso

    # Cash release potential: 10 days DSO reduction = (Net Sales / 365) * 10
    daily_sales = (net_sales / period_days) if net_sales and net_sales > 0 else (r['outstanding'] / 90)
    cash_release_10d = round(daily_sales * 10, 2)
    r['cash_release_potential_10_days'] = cash_release_10d

    # Helper for Turkish currency format
    _tl = lambda v: f"{round(v or 0):,}".replace(",", ".") + " TL"

    # Plain language narrative
    dso_str = f"{dso:.0f} gün" if dso else "yaklaşık 80+ gün"
    overdue_str = _tl(r['overdue'])
    overdue_pct_str = f"%{r['overdue_pct']:.1f}".replace(".", ",") if r['overdue_pct'] is not None else "yüksek oranda"
    r['narrative'] = (
        f"Müşterileriniz ortalama {dso_str} sürede ödeme yapıyor. Toplam {_tl(r['outstanding'])} ticari alacağın "
        f"{overdue_str}'si ({overdue_pct_str}) vadesi geçmiş durumda. "
        f"Tahsilat süresini 10 gün öne çekmek işletmenize yaklaşık {_tl(cash_release_10d)} serbest nakit kazandırabilir."
    )

    # Modül 2: Akıllı Alacak Yönetimi (Credit Scoring & Risk Direktifleri)
    credit_scoring = []
    top_parties = r.get('top_parties', [])
    overdue_by_party = r.get('overdue_by_party', {})
    weighted_days_by_party = r.get('weighted_overdue_days_by_party', {})

    for p in top_parties:
        name = p['name']
        bal = p['amount']
        od = overdue_by_party.get(name, 0.0)
        days = weighted_days_by_party.get(name, 0.0)
        od_ratio = (od / bal * 100) if bal > 0 else 0.0

        if days > 60 or od_ratio > 60:
            tier = 'D'
            tier_label = 'Kritik (Temerrüt Riski)'
            color = '#DC2626'
            directive = "DBS veya nakit teminat olmadan yeni sevkiyatı derhal durdurun; açık hesap bakiyesini yapılandırma protokolüne bağlayın."
        elif days > 30 or od_ratio > 30:
            tier = 'C'
            tier_label = 'Yüksek Risk (Yakın İzleme)'
            color = '#EA580C'
            directive = "Açık hesap risk limitini %50 düşürün; yeni siparişlerde en az %40 peşinat veya vadeli çek şartı koşun."
        elif days > 0 or od_ratio > 0:
            tier = 'B'
            tier_label = 'Orta Risk (Takip)'
            color = '#D97706'
            directive = "Vade gününde otomatik SMS/E-posta hatırlatması kurun; haftalık tahsilat mutabakatı yapın."
        else:
            tier = 'A'
            tier_label = 'Güvenli (Düzenli)'
            color = '#16A34A'
            directive = "Mevcut ticari şartları koruyun; ciro artışı için erken ödeme iskontosu teklif edin."

        credit_scoring.append({
            'name': name,
            'amount': bal,
            'overdue': od,
            'overdue_pct': round(od_ratio, 1),
            'avg_overdue_days': round(days, 1),
            'pct_of_outstanding': p.get('pct_of_outstanding'),
            'tier': tier,
            'tier_label': tier_label,
            'color': color,
            'directive': directive,
        })
    r['customer_credit_scoring'] = credit_scoring

    # Alacak Yoğunlaşması ve Sistemik Temerrüt Şoku (Concentration Shock Simulation)
    top_1 = top_parties[0] if top_parties else None
    top_3_amount = sum(p['amount'] for p in top_parties[:3]) if top_parties else 0.0
    top_3_pct = round(top_3_amount / r['outstanding'] * 100, 1) if r.get('outstanding') else 0.0

    shock_sim = {
        'top_1_name': top_1['name'] if top_1 else 'Bilinmiyor',
        'top_1_amount': top_1['amount'] if top_1 else 0.0,
        'top_1_pct': top_1.get('pct_of_outstanding', 0.0) if top_1 else 0.0,
        'top_3_amount': top_3_amount,
        'top_3_pct': top_3_pct,
    }
    if top_1 and top_1['amount'] > 0:
        shock_sim['narrative'] = (
            f"En büyük müşteriniz ({top_1['name']}) temerrüde düşer veya vadesini 60 gün geciktirirse, "
            f"şirket kasasında {_tl(top_1['amount'])} tutarında ani bir likidite deliği oluşacaktır. "
            f"İlk 3 müşterinizin toplam alacaklarınızın %{top_3_pct:.1f}'ini ({_tl(top_3_amount)}) oluşturması, "
            f"tahsilat akışınızın yüksek oranda yoğunlaşma riski taşıdığını göstermektedir."
        )
    else:
        shock_sim['narrative'] = "Müşteri bazlı alacak kırılımı bulunmadığından yoğunlaşma simülasyonu genel toplam üzerinden değerlendirilmiştir."
    r['concentration_shock'] = shock_sim

    findings = []
    if r.get('overdue_pct') and r['overdue_pct'] >= 20:
        findings.append({
            'code': 'AR-001',
            'category': 'Tahsilat Zekâsı',
            'severity': 'critical' if r['overdue_pct'] >= 40 else 'high',
            'title': 'Vadesi geçmiş alacak oranı nakit akışını zorluyor',
            'detail': r['narrative'],
            'evidence': [
                f"Toplam Alacak: {_tl(r['outstanding'])}",
                f"Vadesi Geçmiş: {_tl(r['overdue'])} (Oran: {overdue_pct_str})",
                f"Ortalama Gecikme: {r.get('weighted_average_overdue_days', 0):.0f} gün",
                f"Alacak Tahsilat Süresi (DSO): {dso_str}"
            ],
            'recommendation': "91+ gün gecikmiş alacakların en büyük bölümünü oluşturan ilk 5 müşteriyi bu hafta öncelikli tahsilat protokolüne alın; yeni sevkiyatları nakit akışına bağlayın.",
            'confidence': 'high',
        })

    # Add CR-001 finding for Tier D customers if any
    critical_customers = [c for c in credit_scoring if c['tier'] == 'D']
    if critical_customers:
        crit_names = ", ".join(c['name'] for c in critical_customers[:3])
        crit_total = sum(c['overdue'] for c in critical_customers)
        findings.append({
            'code': 'AR-CREDIT-001',
            'category': 'Akıllı Alacak & Müşteri Risk Skoru',
            'severity': 'critical',
            'title': f"{len(critical_customers)} Müşteride Kritik Temerrüt Riski (Tier D)",
            'detail': f"{crit_names} başta olmak üzere {len(critical_customers)} müşteride 60+ gün gecikmiş toplam {_tl(crit_total)} bakiye bulunmaktadır.",
            'evidence': [
                f"Kritik Müşteri Sayısı: {len(critical_customers)}",
                f"Gecikmiş Risk Maruziyeti: {_tl(crit_total)}",
                f"Yoğunlaşma (İlk 3 Müşteri Payı): %{top_3_pct:.1f}"
            ],
            'recommendation': "DBS veya nakit teminat olmadan yeni sipariş onaylamayın. Açık hesap risk limitlerini dondurup yapılandırma takvimi imzalattırın.",
            'confidence': 'high',
        })

    r['findings'] = findings
    return r

def analyze_ap(df, mapping, cogs=None, period_days=365, as_of_date=None):
    _tl = lambda v: f"{round(v or 0):,}".replace(",", ".") + " TL"
    r = _aging(df, mapping, 'AP', as_of_date=as_of_date)
    dpo = round(r['outstanding'] / cogs * period_days, 1) if cogs and cogs > 0 else None
    r['dpo_days'] = dpo

    dpo_str = f"{dpo:.0f} gün" if dpo else "bilinmiyor"
    overdue_pct_str = f"%{r.get('overdue_pct', 0):.1f}".replace(".", ",")
    r['narrative'] = (
        f"Tedarikçilerinize ortalama {dpo_str} vadede ödeme yapıyorsunuz. Toplam {_tl(r['outstanding'])} borcun "
        f"{_tl(r['overdue'])}'si ({overdue_pct_str}) vadesi geçmiş statüdedir."
    )

    findings = []
    if r.get('overdue_pct') and r['overdue_pct'] >= 20:
        findings.append({
            'code': 'AP-001',
            'category': 'Tedarikçi & Ödeme Baskısı',
            'severity': 'high',
            'title': 'Kritik tedarikçilerde ödeme takvimi ve nakit planı uyumsuzluğu',
            'detail': f"Tedarikçi borçlarının {overdue_pct_str}'inde ({_tl(r['overdue'])}) vade aşımı oluşmuş durumdadır. Bu durum hammadde/mal tedarik güvenliğini riske sokabilir.",
            'evidence': [
                f"Toplam Tedarikçi Borcu: {_tl(r['outstanding'])}",
                f"Vadesi Geçen Borç: {_tl(r['overdue'])}",
                f"Borç Ödeme Süresi (DPO): {dpo_str}"
            ],
            'recommendation': "Borçları tek taraflı geciktirmek yerine; kritik tedarikçilerde ödeme takvimini, vade yapısını ve 13 haftalık nakit projeksiyonunu birlikte gözden geçirin.",
            'confidence': 'high',
        })
    r['findings'] = findings
    return r

