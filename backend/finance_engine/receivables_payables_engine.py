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
    today=datetime.fromisoformat(str(as_of_date)[:10]) if as_of_date else datetime.now()
    work['_days']=work['_due'].map(lambda due: (today-due).days if due else None)
    known_days=work['_days'].fillna(0)
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
        out['top_overdue_parties']=[{
            'name': str(k), 'amount': float(v),
            'avg_days_overdue': round(float(days_by_party.loc[k,'_w']/days_by_party.loc[k,'_amt']), 1) if k in days_by_party.index and days_by_party.loc[k,'_amt'] else None,
        } for k, v in overdue_by_party.head(10).items()]
    else:
        out['party_count']=None; out['top_parties']=[]; out['top_10_share_pct']=None; out['top_overdue_parties']=[]
    out['weighted_average_overdue_days']=float((work.loc[known_days>0, '_days'] * work.loc[known_days>0, '_amt']).sum() / out['overdue']) if out['overdue'] else None
    out['kind']=kind
    out['risk_tier']=_risk_tier(out['overdue_pct'], out['weighted_average_overdue_days'], out['top_10_share_pct'])
    return out

def analyze_ar(df,mapping,net_sales=None,period_days=365,as_of_date=None):
    r=_aging(df,mapping,'AR',as_of_date=as_of_date)
    r['dso_days']=r['outstanding']/net_sales*period_days if net_sales else None
    return r

def analyze_ap(df,mapping,cogs=None,period_days=365,as_of_date=None):
    r=_aging(df,mapping,'AP',as_of_date=as_of_date)
    r['dpo_days']=r['outstanding']/cogs*period_days if cogs else None
    return r
