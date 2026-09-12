from __future__ import annotations
import pandas as pd
from datetime import datetime
from typing import Any
from .numeric_utils import to_numeric_series
from .date_utils import safe_dates

def _num(s):
    return to_numeric_series(s)

def analyze_inventory(df, mapping, cogs=None, period_days=365, as_of_date=None):
    work = df.copy()
    out = {'rows': len(work)}
    value_col = mapping.get('amount') or mapping.get('balance')
    if value_col:
        value = _num(work[value_col])
    elif mapping.get('quantity') and mapping.get('unit_cost'):
        value = _num(work[mapping['quantity']]) * _num(work[mapping['unit_cost']])
    else:
        value = pd.Series([0.0] * len(work))

    work['_val'] = value
    total_val = float(value.sum())
    out['value'] = total_val
    out['sku_count'] = int(work[mapping['product']].nunique()) if mapping.get('product') else len(work)

    # Warehouse breakdown
    warehouse_breakdown = []
    if mapping.get('warehouse'):
        wh = work.groupby(mapping['warehouse'], dropna=False)['_val'].sum().sort_values(ascending=False)
        out['warehouse_concentration_pct'] = float(wh.head(3).sum() / total_val * 100) if total_val else None
        warehouse_breakdown = [{'name': str(k), 'amount': float(v), 'share_pct': round(float(v)/total_val*100, 1) if total_val else 0.0} for k, v in wh.items()]
    out['warehouses'] = warehouse_breakdown

    # Age and movement analysis
    raw_rows = []
    if mapping.get('product'):
        for _, r in work.iterrows():
            raw_rows.append({
                'product': str(r.get(mapping.get('product'), '')),
                'warehouse': str(r.get(mapping.get('warehouse'), '')) if mapping.get('warehouse') else 'Merkez',
                'quantity': float(r.get(mapping.get('quantity'), 0.0)) if mapping.get('quantity') else None,
                'value': float(r.get('_val', 0.0)),
                'last_movement': str(r.get(mapping.get('last_movement'), '')) if mapping.get('last_movement') else None,
            })
    out['raw_rows'] = raw_rows

    if mapping.get('last_movement'):
        last = safe_dates(work[mapping['last_movement']])
        ref = datetime.fromisoformat(str(as_of_date)[:10]) if as_of_date else datetime.now()
        age = last.map(lambda d: (ref - d).days if d else None)
        known = age.fillna(-1)
        stale_90 = float(value[known > 90].sum())
        stale_180 = float(value[known > 180].sum())
        dead = float(value[known > 365].sum())
        out['stale_90_amount'] = stale_90
        out['stale_180_amount'] = stale_180
        out['dead_stock_amount'] = dead
        out['stale_180_share_pct'] = round((stale_180 / total_val * 100), 1) if total_val else 0.0

        buckets = [
            ('0-90 gün (Hızlı/Aktif)', -10**9, 90),
            ('91-180 gün (Yavaşlayan)', 91, 180),
            ('181-365 gün (Yaşlanmış)', 181, 365),
            ('365+ gün (Ölü Stok)', 366, 10**9)
        ]
        out['inventory_aging_buckets'] = [{
            'bucket': name,
            'amount': float(value[(known >= lo) & (known <= hi)].sum()),
            'share_pct': round(float(value[(known >= lo) & (known <= hi)].sum()) / total_val * 100, 1) if total_val else 0.0,
            'count': int(((known >= lo) & (known <= hi)).sum())
        } for name, lo, hi in buckets]

        # Troubled SKUs > 180 days
        troubled_skus = []
        if mapping.get('product'):
            troubled_mask = known > 180
            for idx, r in work.loc[troubled_mask].iterrows():
                troubled_skus.append({
                    'sku': str(r[mapping['product']]),
                    'value': float(r['_val']),
                    'age_days': int(known.loc[idx]),
                    'warehouse': str(r[mapping['warehouse']]) if mapping.get('warehouse') else 'Depo',
                })
        troubled_skus.sort(key=lambda x: x['value'], reverse=True)
        out['troubled_skus'] = troubled_skus[:10]

    out['dio_days'] = round(out['value'] / cogs * period_days, 1) if cogs and cogs > 0 else None

    # Plain language findings and actions
    findings = []
    if out.get('stale_180_amount') and out['stale_180_amount'] > 0:
        pct = out.get('stale_180_share_pct', 0.0)
        findings.append({
            'code': 'INV-001',
            'category': 'Stok Zekâsı',
            'severity': 'high',
            'title': 'Hareketsiz ve yaşlanmış stokta bağlı nakit riski',
            'detail': f"{out['stale_180_amount']:,.0f} TL tutarında 180 günden uzun süredir hareket görmeyen stok bulunmaktadır. Bu tutar toplam stokun yaklaşık %{pct:.1f}'ine denk gelmektedir.",
            'evidence': [
                f"180+ Gün Yaşlanmış Stok: {out['stale_180_amount']:,.0f} TL (Pay: %{pct:.1f})",
                f"Toplam Stok Değeri: {total_val:,.0f} TL",
                f"Stokta Bağlı Gün Süresi (DIO): {out.get('dio_days', 'N/A')} gün"
            ],
            'recommendation': "180+ gün bekleyen SKU'lar için acil tasfiye, bundle promosyonu veya tedarikçiye iade aksiyon planı oluşturularak bağlı sermaye serbest bırakılmalıdır.",
            'confidence': 'high',
        })
    out['findings'] = findings
    return out

