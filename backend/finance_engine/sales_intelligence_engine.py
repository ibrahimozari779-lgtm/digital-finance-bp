from __future__ import annotations
import pandas as pd
from typing import Any
from .data_classifier import norm
from .numeric_utils import to_numeric_series, parse_number
from .date_utils import safe_dates

def _num(s):
    if s is None:
        return pd.Series(dtype=float)
    return to_numeric_series(s)


def analyze_sales(df:pd.DataFrame,mapping:dict[str,str])->dict[str,Any]:
    work=df.copy()
    def col(k): return mapping.get(k)
    numeric_cols=[]
    for key in ['net_sales','gross_sales','cash_price','term_price','discount','quantity','cost','amount','paid','outstanding']:
        if col(key): work.loc[:, f'_{key}']=_num(work[col(key)]); numeric_cols.append(f'_{key}')
    if col('date'): work['_date']=safe_dates(work[col('date')])
    # Strictly exclude any non-sales or operational columns from product value columns:
    blocked_exact = {
        'miktar', 'quantity', 'qty', 'adet', 'maliyet', 'cost', 'cogs', 'iskonto', 'discount', 'indirim',
        'birim', 'unit', 'fiyat', 'price', 'rate', 'oran', 'yuzde', 'percent', 'weighted', 'date', 'tarih',
        'id', 'no', 'kod', 'code', 'bakiye', 'balance', 'amount', 'tutar', 'paid', 'odenen', 'outstanding',
        'overdue', 'vade', 'odeme', 'payment', 'customer', 'musteri', 'ciftci', 'cari', 'region', 'il',
        'ilce', 'depo', 'warehouse', 'status', 'durum', 'kdv', 'tax', 'currency', 'para', 'doviz'
    }
    excluded = {col(k) for k in ('customer','date','due_date','payment_date','paid','outstanding','cash_price','term_price','net_sales','gross_sales','discount','quantity','unit_cost','cost','amount','currency','status','warehouse') if col(k)}
    product_value_cols = []
    for c in work.columns:
        nc = norm(c)
        if c in excluded or str(c).startswith('_') or str(c).startswith('Unnamed_'):
            continue
        tokens = set(nc.split())
        if tokens & blocked_exact:
            continue
        if any(x in nc for x in ('weighted due', 'weighted actual', 'outstanding balance', 'customer id', 'birim fiyat', 'satis miktari', 'iskonto tutari', 'maliyet tutari')):
            continue
        s = _num(work[c])
        if s.notna().mean() > 0.85 and float(s.abs().sum()) > 0 and not pd.api.types.is_datetime64_any_dtype(work[c]):
            product_value_cols.append(str(c))

    term = float(work['_term_price'].sum()) if '_term_price' in work else None
    cash = float(work['_cash_price'].sum()) if '_cash_price' in work else None
    gross = float(work['_gross_sales'].sum()) if '_gross_sales' in work else None
    discount = float(work['_discount'].sum()) if '_discount' in work else None

    # Economically sound Net Sales priority:
    # 1. Explicit net_sales
    # 2. Gross sales minus discount (if both exist)
    # 3. amount
    # 4. term_price or cash_price
    # 5. Sum of genuine wide product category columns (only if nothing else exists)
    if '_net_sales' in work:
        net = float(work['_net_sales'].sum())
    elif gross is not None and discount is not None:
        net = gross - discount
    elif '_amount' in work:
        net = float(work['_amount'].sum())
    elif term is not None:
        net = term
    elif cash is not None:
        net = cash
    elif product_value_cols:
        net = float(sum(_num(work[c]).sum() for c in product_value_cols))
    else:
        net = None

    product_total = float(sum(_num(work[c]).sum() for c in product_value_cols)) if product_value_cols else None
    if gross is None:
        gross = (net + discount) if (net is not None and discount is not None) else net

    cost = float(work['_cost'].sum()) if '_cost' in work else None
    paid = float(work['_paid'].sum()) if '_paid' in work else None
    outstanding = float(work['_outstanding'].sum()) if '_outstanding' in work else None
    result = {
        'rows': len(work), 'net_sales': net, 'gross_sales': gross, 'cash_price_total': cash, 'term_price_total': term,
        'term_premium': (term - cash if term is not None and cash is not None else None),
        'term_premium_pct': ((term / cash - 1) * 100 if term is not None and cash else None),
        'product_value_total': product_total, 'product_value_columns': product_value_cols,
        'discounts': discount, 'cogs': cost, 'paid_total': paid, 'outstanding_total': outstanding,
        'collection_rate_pct': None,
        'collection_metric_note': 'Ödenen Tutar ile Açık Bakiye satır bazında bağımsız dönemleri temsil ediyor olabileceğinden doğrudan tahsilat oranı olarak yorumlanmaz.',
        'gross_margin': ((net - cost) / net if net and cost is not None else None),
    }
    if col('customer') and net is not None:
        base = '_net_sales' if '_net_sales' in work else '_amount' if '_amount' in work else '_term_price'
        if base in work:
            grp = work.groupby(col('customer'), dropna=False)[base].sum().sort_values(ascending=False)
            result['customer_count'] = int(len(grp))
            result['top_customers'] = [{'name': str(k), 'sales': float(v)} for k, v in grp.head(10).items()]
            result['top_10_customer_share_pct'] = float(grp.head(10).sum() / net * 100) if net else None
            if cost is not None:
                cost_grp=work.groupby(col('customer'),dropna=False)['_cost'].sum()
                customer_profit=[]
                for name, sales_value in grp.items():
                    c=float(cost_grp.get(name, 0.0)); gp=float(sales_value)-c
                    customer_profit.append({'name':str(name),'sales':float(sales_value),'cogs':c,'gross_profit':gp,'gross_margin_pct':gp/float(sales_value)*100 if sales_value else None})
                result['customer_profitability']=sorted(customer_profit,key=lambda x:x['gross_profit'],reverse=True)[:20]
    if col('product') and net is not None:
        base='_term_price' if '_term_price' in work else '_net_sales' if '_net_sales' in work else '_amount'
        if base in work:
            grp=work.groupby(col('product'),dropna=False)[base].sum().sort_values(ascending=False)
            result['product_count']=int(len(grp)); result['top_products']=[{'name':str(k),'sales':float(v)} for k,v in grp.head(10).items()]
            result['top_10_product_share_pct']=float(grp.head(10).sum()/net*100) if net else None
            if cost is not None:
                cost_grp=work.groupby(col('product'),dropna=False)['_cost'].sum()
                product_profit=[]
                for name, sales_value in grp.items():
                    c=float(cost_grp.get(name, 0.0)); gp=float(sales_value)-c
                    product_profit.append({'name':str(name),'sales':float(sales_value),'cogs':c,'gross_profit':gp,'gross_margin_pct':gp/float(sales_value)*100 if sales_value else None})
                result['product_profitability']=sorted(product_profit,key=lambda x:x['gross_profit'],reverse=True)[:20]
    if col('date') and '_date' in work:
        base='_term_price' if '_term_price' in work else '_net_sales' if '_net_sales' in work else '_amount'
        if base in work:
            periods=work['_date'].map(lambda d: f'{d.year:04d}-{d.month:02d}' if d else None)
            monthly=work.loc[periods.notna()].groupby(periods[periods.notna()])[base].sum()
            result['monthly_series']=[{'period':str(k),'sales':float(v)} for k,v in monthly.items()]
    # Wide product analysis, e.g. Fide / Gübre / Tohum / Yem.
    if product_value_cols:
        prod=[]
        for c in product_value_cols:
            v=float(_num(work[c]).sum()); share=(v/net*100 if net else None)
            prod.append({'name':str(c),'sales':v,'share_pct':share})
        result['product_mix']=sorted(prod,key=lambda x:x['sales'],reverse=True)
    if col('status') and outstanding is not None:
        status_series=work[col('status')].astype(str).str.strip().str.lower()
        result['overdue_amount_by_status']=float(work.loc[status_series.str.contains('overdue|vadesi.*gec',regex=True,na=False),'_outstanding'].sum()) if '_outstanding' in work else None
        result['not_due_amount_by_status']=float(work.loc[status_series.str.contains('not due|gelmem',regex=True,na=False),'_outstanding'].sum()) if '_outstanding' in work else None
        result['overdue_row_count']=int(status_series.str.contains('overdue|vadesi.*gec',regex=True,na=False).sum())
        result['not_due_row_count']=int(status_series.str.contains('not due|gelmem',regex=True,na=False).sum())

    findings=[]
    if result.get('top_10_customer_share_pct') is not None and result['top_10_customer_share_pct']>=60:
        findings.append({'severity':'high','title':'Müşteri yoğunlaşması yüksek','detail':f"İlk 10 müşteri satışların %{result['top_10_customer_share_pct']:.1f}'ini oluşturuyor."})
    if result.get('term_premium_pct') is not None and result['term_premium_pct']>0:
        findings.append({'severity':'medium','title':'Vadeli satış fiyatı peşin fiyattan yüksek','detail':f"Vadeli fiyat toplamı peşin fiyata göre %{result['term_premium_pct']:.1f} daha yüksek; vade fiyatlaması ayrı bir finansal/ticari politika konusu olarak izlenmeli."})
    if result.get('overdue_amount_by_status') is not None and result.get('overdue_amount_by_status',0)>0:
        findings.append({'severity':'high','title':'Satış dosyasında vadesi geçmiş bakiye bulunuyor','detail':f"Overdue statüsündeki satırlarda açık bakiye {result['overdue_amount_by_status']:,.0f} ve {result.get('overdue_row_count',0)} satır bulunuyor."})
    if result.get('gross_margin') is not None and result['gross_margin']<0.10:
        findings.append({'severity':'high','title':'Satış marjı zayıf','detail':f"Satış datasına göre brüt marj %{result['gross_margin']*100:.1f}."})
    if product_value_cols and result.get('product_value_total') is not None and net is not None:
        diff=abs(result['product_value_total']-net)
        if diff>max(1,abs(net)*0.005): findings.append({'severity':'medium','title':'Ürün kırılımı ile satış toplamı arasında fark var','detail':f"Ürün kolonları toplamı {result['product_value_total']:,.0f} ile satış baz tutarı {net:,.0f} arasında {diff:,.0f} fark bulunuyor. Mapping / iade / yuvarlama kontrolü gerekir."})
    result['findings']=findings
    result['classification']='sales_primary_with_collection_fields' if (paid is not None or outstanding is not None) else 'sales'
    return result
