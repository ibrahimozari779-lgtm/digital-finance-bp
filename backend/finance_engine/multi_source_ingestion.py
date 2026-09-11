from __future__ import annotations
import io
import re
from typing import Any
import pandas as pd
from .data_classifier import classify_dataframe
from .headerless_table_detector import infer_headerless_financial_table
from .numeric_utils import parse_number

MAX_ROWS=300_000

def _promote_header(raw: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    if raw is None or raw.empty:
        return raw, {"mode":"empty"}
    best = None
    keywords=(
        'customer','musteri','müşteri','çiftçi','vendor','supplier','tedarik','invoice','fatura',
        'date','tarih','due','vade','sales','satış','satis','amount','tutar','quantity','miktar',
        'sku','stok','product','ürün','urun','account','hesap','balance','bakiye','discount','iskonto',
        'maliyet','cost','peşin','pesin','vadeli','ödeme','odenen','outstanding','borç','borc','alacak'
    )
    for i in range(min(len(raw),120)):
        vals=[str(v).strip().lower() for v in raw.iloc[i].tolist() if pd.notna(v) and str(v).strip()]
        if len(vals) < 2:
            continue
        keyword_score=sum(2 if any(k==v for k in keywords) else 1 if any(k in v for k in keywords) else 0 for v in vals)
        text_count=sum(1 for v in vals if not v.replace('.','',1).replace(',','',1).replace('-','',1).isdigit())
        nonblank=len(vals)
        uniqueness=len(set(vals))/max(1,nonblank)
        score=keyword_score + min(8,text_count*0.5) + uniqueness*2
        if best is None or score>best[0]:
            best=(score,i)
    if best and best[0] >= 6:
        best_idx=best[1]
        headers=[]; seen={}
        for i,v in enumerate(raw.iloc[best_idx].tolist()):
            h=str(v).strip() if pd.notna(v) else f'Unnamed_{i}'
            h=h or f'Unnamed_{i}'
            n=seen.get(h,0); seen[h]=n+1; headers.append(h if n==0 else f'{h}_{n}')
        df=raw.iloc[best_idx+1:].copy()
        original_rows=(df.index.to_series()+1).astype(int)
        df.columns=headers
        df=df.dropna(how='all').copy()
        df['_source_row']=original_rows.loc[df.index].to_numpy() if len(df) else []
        df=df.reset_index(drop=True)
        return df,{"mode":"header_promoted","header_row":best_idx+1,"header_score":round(best[0],2)}
    inferred=infer_headerless_financial_table(raw)
    if inferred is not None:
        return inferred
    df=raw.dropna(how='all').reset_index(drop=True).copy()
    df.columns=[f'Column_{i+1}' for i in range(df.shape[1])]
    return df,{"mode":"raw_no_header"}


def _looks_like_statement_layout(df: pd.DataFrame) -> bool:
    """Detect accounting statement exports that lack a literal header row.

    Operational files can contain incidental 3-digit numbers, so the account-code
    pattern must occupy a meaningful share of a column before we keep the raw layout.
    """
    if df is None or df.empty or df.shape[1] < 2:
        return False
    n=min(len(df),5000)
    best_ratio=0.0; best_hits=0
    for c in df.columns:
        hits=0
        for v in df[c].iloc[:n]:
            sv='' if pd.isna(v) else str(v).strip()
            if re.fullmatch(r'\d{3}', sv) and 100 <= int(sv) <= 799:
                hits += 1
        ratio=hits/max(1,n)
        if ratio>best_ratio:
            best_ratio=ratio; best_hits=hits
    return best_hits >= 4 and best_ratio >= 0.12


def _resolve_sheet_layout(v: pd.DataFrame) -> pd.DataFrame:
    """Decide whether a raw (headerless-read) sheet has a real header row or is a
    genuinely headerless accounting-statement export.

    BUGFIX: previously this checked _looks_like_statement_layout() FIRST and only
    fell back to _promote_header() when it returned False. That heuristic just
    counts 3-digit values in the 100-799 range anywhere in a column — with no
    check that a real header row is absent. Any ordinary operational sheet whose
    quantity/amount/ID column happens to sit mostly in that numeric range (a very
    common coincidence, e.g. a "Miktar"/"Quantity" column) was misidentified as a
    headerless statement export, so its real header row (Müşteri/Ürün/Tarih/...)
    was discarded and columns fell back to bare 0/1/2/3/... positions — silently
    breaking Sales/AR/AP/Inventory Intelligence and PVM for that file.
    A genuine header row is strong, direct evidence the sheet is NOT headerless,
    so detecting one now takes priority; the statement-layout heuristic is only
    consulted when no confident header row is found.
    """
    promoted_df, meta = _promote_header(v)
    if meta.get('mode') == 'header_promoted' and meta.get('header_score', 0) >= 6:
        return promoted_df
    if _looks_like_statement_layout(v):
        return v.copy()
    return promoted_df


def _read_one(content:bytes, filename:str)->dict[str,pd.DataFrame]:
    ext=filename.lower().rsplit('.',1)[-1] if '.' in filename else ''
    bio=io.BytesIO(content)
    if ext=='csv':
        last=None
        for enc,kwargs in [('utf-8-sig',{'sep':';'}),('cp1254',{'sep':';'}),('utf-8',{})]:
            try:
                bio.seek(0); raw=pd.read_csv(bio,header=None,encoding=enc,**kwargs); last=None; break
            except Exception as exc: last=exc
        if last is not None: raise ValueError(f'CSV okunamadı: {last}')
        df,meta=_promote_header(raw); return {'CSV':df}
    if ext in {'xlsx','xlsm'}:
        raw=pd.read_excel(bio,sheet_name=None,header=None,engine='openpyxl');
        out={}
        for k,v in raw.items():
            out[str(k)] = _resolve_sheet_layout(v)
        return out
    if ext=='xls':
        try: raw=pd.read_excel(bio,sheet_name=None,header=None,engine='xlrd')
        except ImportError as exc: raise ValueError('Legacy .xls dosyası için xlrd>=2.0.1 gerekir.') from exc
        except Exception as exc: raise ValueError(f'.xls dosyası okunamadı: {exc}') from exc
        return {str(k):_resolve_sheet_layout(v) for k,v in raw.items()}
    raise ValueError('Yalnızca CSV, XLSX, XLSM ve XLS destekleniyor.')

def ingest_sources(files:list[tuple[str,bytes]], finance_processor=None, max_mb:float=15.0)->dict[str,Any]:
    sources=[]; errors=[]; file_results=[]
    for filename,content in files:
        if len(content)>max_mb*1024*1024:
            errors.append({'file':filename,'error':f'{max_mb:g} MB limitini aşıyor.'}); continue
        try: sheets=_read_one(content,filename)
        except Exception as e: errors.append({'file':filename,'error':str(e)}); continue
        file_roles=[]
        for sheet,df in sheets.items():
            if df is None or df.empty: continue
            if len(df)>MAX_ROWS: df=df.head(MAX_ROWS).copy()
            role,conf,mapping=classify_dataframe(df,filename,sheet)
            mapping = dict(mapping)
            mapping['_rows_loaded'] = int(len(df))
            mapping['_columns_loaded'] = int(len(df.columns))
            mapping['_header_mode'] = next((s.get('mode') for s in []), None)
            # A sales file with both sales and collection fields is intentionally sales-primary.
            roles=[x for x in mapping.get('_role_candidates','').split('|') if x]
            if role!='unknown' and role not in roles: roles.insert(0,role)
            file_roles.append({'sheet':sheet,'role':role,'roles':roles,'confidence':conf,'rows':len(df),'mapping':mapping})
            # Primary role only prevents accidental double counting. The sales engine itself exposes
            # collection/AR fields when present in the same source.
            if role!='unknown': sources.append({'filename':filename,'sheet':sheet,'role':role,'confidence':conf,'rows':len(df),'mapping':mapping,'df':df})
        if not file_roles: errors.append({'file':filename,'error':'Okunabilir tablo bulunamadı.'})
        elif all(x['role']=='unknown' for x in file_roles): errors.append({'file':filename,'error':'Dosya okundu ancak veri tipi otomatik sınıflandırılamadı. Kolon başlıklarını kontrol edin.'})
        file_results.append({'filename':filename,'roles':file_roles})
    return {'sources':sources,'files':file_results,'finance_candidates':[s for s in sources if s['role']=='finance'],'errors':errors}
