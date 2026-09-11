from __future__ import annotations
import pandas as pd
from datetime import datetime
from typing import Any
from .numeric_utils import to_numeric_series
from .date_utils import safe_dates

def _num(s):
    return to_numeric_series(s)

def analyze_inventory(df,mapping,cogs=None,period_days=365,as_of_date=None):
    work=df.copy(); out={'rows':len(work)}
    value_col=mapping.get('amount') or mapping.get('balance')
    if value_col: value=_num(work[value_col])
    elif mapping.get('quantity') and mapping.get('unit_cost'): value=_num(work[mapping['quantity']])*_num(work[mapping['unit_cost']])
    else: value=pd.Series([0.0]*len(work))
    out['value']=float(value.sum()); out['sku_count']=int(work[mapping['product']].nunique()) if mapping.get('product') else None
    if mapping.get('warehouse'):
        wh=value.groupby(work[mapping['warehouse']]).sum().sort_values(ascending=False); out['warehouse_concentration_pct']=float(wh.head(3).sum()/out['value']*100) if out['value'] else None
    if mapping.get('last_movement'):
        last=safe_dates(work[mapping['last_movement']]); ref=datetime.fromisoformat(str(as_of_date)[:10]) if as_of_date else datetime.now(); age=last.map(lambda d:(ref-d).days if d else None); known=age.fillna(-1)
        out['stale_90_amount']=float(value[known>90].sum()); out['stale_180_amount']=float(value[known>180].sum())
        out['dead_stock_amount']=float(value[known>365].sum())
        out['inventory_aging_buckets']=[{'bucket':name,'amount':float(value[(known>=lo)&(known<=hi)].sum())} for name,lo,hi in [('0-90',-10**9,90),('91-180',91,180),('181-365',181,365),('365+',366,10**9)]]
    out['dio_days']=out['value']/cogs*period_days if cogs else None
    out['findings']=[]
    if out.get('stale_180_amount') and out['stale_180_amount']>0:
        out['findings'].append({'severity':'high','title':'Yavaş / yaşlanmış stok riski','detail':f"180+ gün hareket görmeyen stok değeri {out['stale_180_amount']:,.0f} TL."})
    return out
