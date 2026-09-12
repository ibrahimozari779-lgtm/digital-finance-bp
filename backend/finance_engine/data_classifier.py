from __future__ import annotations
import re
from typing import Any
import pandas as pd

ALIASES = {
    'customer': {'customer','customer name','customer code','customer id','customer no','musteri id','müşteri id','cari hesap','cari hesap kodu','müşteri id','customer no','musteri','musteri adi','musteri kodu','müşteri','müşteri adı','müşteri kodu','cari','cari ad','cari adı','cari kod','cari kodu','cari unvan','cari ünvan','unvan','ünvan','çiftçi'},
    'vendor': {'vendor','vendor name','vendor code','supplier','supplier name','supplier code','tedarikci','tedarikçi','tedarikci adi','tedarikçi adı','tedarikci kodu','tedarikçi kodu','satıcı','satici','satıcı adı','satici adi'},
    'invoice': {'invoice','invoice no','invoice number','invoice code','fatura','fatura no','fatura numarasi','fatura numarası','fatura num','document no','belge no','belge numarasi','belge numarası','document number'},
    'product': {'product','product name','product code','urun','ürün','urun adi','ürün adı','urun kodu','ürün kodu','sku','stock code','stok kodu','material','malzeme','material code'},
    'date': {'date','tarih','invoice date','fatura tarihi','document date','belge tarihi','transaction date','işlem tarihi','sales date','satış tarihi','satis tarihi'},
    'due_date': {'due date','vade','vade tarihi','due_date','payment due','son ödeme','son odeme','vade sonu'},
    'payment_date': {'payment date','ödeme tarihi','odeme tarihi','actual payment date','tahsil tarihi','tahsilat tarihi'},
    'status': {'overdue/not due','overdue','not due','vadesi geçmiş','vadesi gecmis','vadesi gelmemiş','vadesi gelmemis'},
    'amount': {'amount','tutar','tutar (tl)','tl tutar','net tutar','tutar','total','total amount','gross sales','gross amount','net sales','net sales amount','net amount','amount due','acik tutar','açık tutar','outstanding','value','değer','net tutar','satış tutarı','satis tutari','toplam tutar','belge tutarı','belge tutari'},
    'net_sales': {'net sales','net sales amount','net sale','net ciro','net satış','net satis','sales','sales amount','ciro','sales value','satış','satis','satış tutarı','satis tutari','net tutar','net satış tutarı','net satis tutari','vadeli fiyat','vadeli tutar'},
    'cash_price': {'cash price','peşin fiyat','pesin fiyat','cash sales price'},
    'term_price': {'term price','vadeli fiyat','vadeli satış fiyatı','vadeli satis fiyati'},
    'gross_sales': {'gross sales','revenue','ciro','gross revenue','gross revenue','brut satis','brüt satış','gross amount','gross sales amount','brüt ciro','brut ciro'},
    'discount': {'discount','iskonto','indirim','discount amount','discount value','iskonto tutarı','iskonto tutari'},
    'quantity': {'quantity','qty','miktar','adet','quantity sold','satış miktarı','satis miktari','satılan miktar','satilan miktar'},
    'unit_cost': {'unit cost','birim maliyet','unit price cost','cost per unit','birim fiyat maliyet','unit cost amount'},
    'cost': {'cost','cogs','cost of sales','maliyet','satış maliyeti','satis maliyeti','cost amount','maliyet tutarı','maliyet tutari'},
    'outstanding': {'outstanding','open amount','open balance','acik bakiye','açık bakiye','kalan','kalan bakiye','açık tutar','acik tutar','bakiye','kalan tutar','ödenmemiş','odenmemis'},
    'paid': {'paid','paid amount','odenen','ödenen','tahsil edilen','tahsilat','odeme','ödeme','ödenen tutar'},
    'currency': {'currency','para birimi','doviz','döviz','pb','currency code','doviz kodu','döviz kodu'},
    'warehouse': {'warehouse','depo','depo adi','depo adı','location','lokasyon','warehouse name','depo kodu'},
    'last_movement': {'last movement','last movement date','son hareket','son hareket tarihi','last transaction','son işlem tarihi','son islem tarihi'},
    'balance': {'balance','bakiye','closing balance','donem sonu bakiye','dönem sonu bakiye','closing'},
    'account_code': {'account code','hesap kodu','hesap no','hesap numarası','hesap numarasi','account number','gl account','hesap'},
    # BUGFIX: classify_dataframe() below calls _best_column(cols,'debit_balance') /
    # 'credit_balance' / 'debit_turnover' / 'credit_turnover' when deciding whether a
    # sheet inside a multi-file Data Hub upload is a full trial balance ("finance"
    # role). Those four keys were never defined in ALIASES, so ALIAS_NORM[field]
    # raised a bare KeyError and crashed the ENTIRE Data Hub / multi-source analysis
    # any time it tried to classify a sheet with an account_code column — i.e. any
    # multi-file upload that included a mizan sheet. Aliases mirror app.py's
    # FIELD_ALIASES so both detectors agree on the same column names.
    'debit_balance': {'borc bakiye','borç bakiye','borc bakiyesi','borç bakiyesi','donem borc bakiye','dönem borç bakiye','debit balance','debit closing balance'},
    'credit_balance': {'alacak bakiye','alacak bakiyesi','donem alacak bakiye','dönem alacak bakiye','credit balance','credit closing balance'},
    'debit_turnover': {'borc','borç','debit','borc hareket','borç hareket','borc toplami','borç toplamı','debit turnover'},
    'credit_turnover': {'alacak','credit','alacak hareket','alacak toplami','alacak toplamı','credit turnover'},
}

CONTAINS_HINTS = {
    'customer': ('customer','musteri','müşteri','cari','çiftçi'), 'vendor': ('vendor','supplier','tedarik','satici','satıcı'),
    'invoice': ('invoice','fatura','belge','document'), 'product': ('product','urun','ürün','sku','stok','material','malzeme'),
    'date': ('date','tarih'), 'due_date': ('due','vade','son odeme','son ödeme'), 'payment_date': ('payment','odeme','ödeme','tahsil'),
    'net_sales': ('net sales','net satis','net satış','net ciro','sales value','sales amount','satış tut','satis tut','ciro','vadeli fiyat','vadeli satis'),
    'cash_price': ('peşin fiyat','pesin fiyat','cash price'), 'term_price': ('vadeli fiyat','term price'),
    'gross_sales': ('gross sales','brut satis','brüt satış','gross revenue'), 'discount': ('discount','iskonto','indirim'),
    'quantity': ('quantity','qty','miktar','adet'), 'unit_cost': ('unit cost','birim maliyet','cost per unit'), 'cost': ('cogs','cost','maliyet'),
    'outstanding': ('outstanding','open amount','open balance','acik bakiye','açık bakiye','kalan','ödenmemiş','odenmemis'),
    'paid': ('paid','odenen','ödenen','tahsil'),
    'status': ('overdue','not due','vadesi'), 'currency': ('currency','para birimi','döviz','doviz'), 'warehouse': ('warehouse','depo','lokasyon','location'),
    'last_movement': ('last movement','son hareket'), 'balance': ('balance','bakiye','closing balance'), 'account_code': ('account code','hesap kodu','hesap no','account number'),
}

def norm(x: Any) -> str:
    # BUGFIX: same Turkish-İ casefolding bug as app.py's normalize() — see the
    # detailed note there. Translating Turkish letters (upper + lower) to
    # ASCII *before* lower() avoids the stray combining-dot-above character
    # that Python's default .lower() produces for capital "İ", which used to
    # silently break alias matching for any header/word starting with İ
    # (İskonto, İstanbul, İşlem, İnşaat, İhracat, ...).
    s=str(x).strip()
    s=s.translate(str.maketrans({
        'ı':'i','İ':'i','I':'i','ş':'s','Ş':'s','ğ':'g','Ğ':'g',
        'ü':'u','Ü':'u','ö':'o','Ö':'o','ç':'c','Ç':'c',
    }))
    s=s.lower()
    return re.sub(r'[^a-z0-9]+',' ',s).strip()

ALIAS_NORM={k:{norm(v) for v in vals} for k,vals in ALIASES.items()}

def _best_column(columns:list[Any], field:str) -> str|None:
    vals=ALIAS_NORM[field]
    for c in columns:
        if norm(c) in vals:
            return str(c)
    hints=CONTAINS_HINTS.get(field,())
    best=None; best_score=0
    for c in columns:
        nc=norm(c); score=0
        for h in hints:
            nh=norm(h)
            if nh and (nc==nh or nh in nc): score=max(score,2 if nc==nh else 1)
        if score>best_score: best_score=score; best=str(c)
    return best

def header_score(columns:list[Any])->dict[str,int]:
    return {k:(1 if _best_column(columns,k) else 0) for k in ALIAS_NORM}

def classify_dataframe(df: pd.DataFrame, filename: str, sheet: str='') -> tuple[str,float,dict[str,str]]:
    # Internal/synthetic bookkeeping columns (e.g. "_source_row", added by the ingestion
    # layer to preserve traceability to the original spreadsheet row) must never feed the
    # content-based classification heuristics below. A row-number column for any sheet with
    # more than ~100 data rows will *always* contain a dense run of literal 3-digit values
    # between 100 and 799 purely because of its length - which is indistinguishable, to the
    # structural account-code scan, from a real TDHP account-code column. Left unguarded this
    # silently misclassifies large sales/AR/AP/stock sheets as "finance" (mizan) and vice
    # versa, which is the source of intermittent "format/pattern mismatch" failures on bigger
    # files. Any column name starting with "_" is considered internal and is excluded here.
    cols=[c for c in df.columns if not str(c).startswith('_')]
    sc=header_score(cols); fnorm=norm(filename+' '+sheet)
    # Structural signals for headerless financial inference: the upstream reader may
    # already have promoted columns to canonical names. Keep this check before filename heuristics.
    canonical_finance = 'account_code' in cols and any(c in cols for c in ('balance','debit_balance','credit_balance','debit_turnover','credit_turnover'))
    candidates=[]
    # Statement-style / headerless accounting layout: identify a column where TDHP-like
    # 3-digit account codes occupy a meaningful share of rows, plus another numeric column.
    structural_finance=False
    n=min(len(df),5000)
    col_list=list(df.columns)
    for c in cols:
        hits=0; detail_hits=0
        idx=col_list.index(c)
        col_values=df[c].iloc[:n]
        for i,v in enumerate(col_values):
            sv='' if pd.isna(v) else str(v).strip()
            if re.fullmatch(r'\d{3}', sv) and 100 <= int(sv) <= 799:
                hits += 1
                # A real TDHP account-code column is immediately followed by an account
                # NAME (text). A numeric amount column (e.g. a pivoted profit/quantity total)
                # that merely happens to fall in the same 100-799 numeric range will instead
                # have another number - or nothing - beside it. This neighbor check is what
                # separates genuine headerless financial statements from large operational/
                # pivot exports whose amount columns coincidentally collide with the
                # account-code range (the false positive that misclassified multi-thousand-row
                # sales/profitability pivots as "finance").
                if idx+1 < len(col_list):
                    nv=df.iat[i, idx+1] if i < len(df) else None
                    if pd.notna(nv) and not isinstance(nv,(int,float)):
                        detail_hits += 1
        if hits >= 4 and hits/max(1,n) >= 0.12 and detail_hits/max(1,hits) >= 0.5:
            other_numeric=0
            for oc in cols:
                if oc==c: continue
                if pd.api.types.is_numeric_dtype(df[oc]):
                    other_numeric += 1
                else:
                    sample=df[oc].iloc[:min(n,300)]
                    valid=sum(1 for v in sample if pd.notna(v) and re.search(r'\d',str(v)) and any(ch in str(v) for ch in ',.'))
                    if valid/max(1,len(sample)) >= 0.35: other_numeric += 1
            if other_numeric:
                structural_finance=True; break
    sales_signals=sum(sc[k] for k in ('net_sales','gross_sales','cash_price','term_price','discount','quantity','product','customer','paid','outstanding','date'))
    strong_operational_sales = bool(sc['customer'] and (sc['net_sales'] or sc['cash_price'] or sc['term_price'] or sc['invoice'] or sc['date']))
    if structural_finance and not strong_operational_sales:
        candidates.append(('finance',0.97))
    if canonical_finance and not strong_operational_sales:
        candidates.append(('finance', 0.995))
    if sc['account_code'] and (sc['balance'] or _best_column(cols,'debit_balance') or _best_column(cols,'credit_balance') or _best_column(cols,'debit_turnover') or _best_column(cols,'credit_turnover')) and not strong_operational_sales:
        candidates.append(('finance',0.99))
    # Sales should win even when the same file also contains payment/outstanding fields.
    if (sc['cash_price'] and sc['term_price']) or (sc['term_price'] and (sc['customer'] or sc['date'])):
        candidates.append(('sales',0.995))
    elif sc['net_sales'] and (sc['customer'] or sc['product'] or sc['date'] or sc['invoice']):
        candidates.append(('sales',0.98))
    elif sc['gross_sales'] and (sc['customer'] or sc['product'] or sc['invoice']):
        candidates.append(('sales',0.93))
    elif sales_signals>=4 and (sc['customer'] or sc['product']):
        candidates.append(('sales',0.90))
    if sc['customer'] and sc['due_date'] and (sc['outstanding'] or sc['amount']) and not ((sc['cash_price'] and sc['term_price']) or sc['term_price']):
        candidates.append(('ar_aging',0.97))
    if sc['vendor'] and sc['due_date'] and (sc['outstanding'] or sc['amount']): candidates.append(('ap_aging',0.97))
    if sc['product'] and (sc['quantity'] or sc['unit_cost'] or sc['warehouse'] or sc['amount']) and not sc['customer']:
        candidates.append(('inventory',0.92))
    if sc['vendor'] and not sc['due_date'] and (sc['amount'] or sc['outstanding']): candidates.append(('vendor_master',0.72))
    if not candidates:
        if any(x in fnorm for x in ('sales','satis','satis')): candidates.append(('sales',0.45))
        elif any(x in fnorm for x in ('aging','alacak','receivable')) and sc['customer']: candidates.append(('ar_aging',0.45))
        elif any(x in fnorm for x in ('aging','borc','payable')) and sc['vendor']: candidates.append(('ap_aging',0.45))

    # Finance-like numeric account code column without literal header.
    if not candidates:
        for c in cols:
            vals=pd.to_numeric(df[c],errors='coerce') if pd.api.types.is_numeric_dtype(df[c]) else None
            if vals is not None:
                ok=((vals.dropna().astype(int).between(100,799)).mean() if len(vals.dropna()) else 0)
                if ok>=0.55 and len(vals.dropna())>=4:
                    candidates.append(('finance',0.88)); break

    if not candidates: return 'unknown',0.0,{}
    role,conf=max(candidates,key=lambda x:x[1]); mapping={}
    customer_id_col=_best_column(cols,'customer')
    # Prefer explicit customer identifiers over a generic person/name field such as 'Çiftçi'.
    explicit_id=next((str(c) for c in cols if norm(c) in {norm('Customer ID'),norm('Customer Code'),norm('Müşteri Kodu'),norm('Müşteri ID')}),None)
    for field in ALIAS_NORM:
        c=_best_column(cols,field)
        if c: mapping[field]=c
    if explicit_id: mapping['customer']=explicit_id
    mapping['_role_candidates']='|'.join(r for r,_ in sorted(candidates,key=lambda x:x[1],reverse=True))
    return role,conf,mapping
