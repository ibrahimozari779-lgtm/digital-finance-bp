from __future__ import annotations
from typing import Any
import pandas as pd
from .multi_source_ingestion import ingest_sources
from .sales_intelligence_engine import analyze_sales
from .receivables_payables_engine import analyze_ar, analyze_ap
from .inventory_intelligence_engine import analyze_inventory
from .reconciliation_engine import build_reconciliation
from .operational_finance_engine import build_operational_finance

def _group_sources(sources):
    grouped={}
    for s in sources:
        grouped.setdefault(s['role'],[]).append(s)
    return grouped

def _canonicalize(items):
    """Merge same-role files even when their source headers differ.

    A merged data frame must not inherit only the first workbook's mapping.
    Semantic fields are renamed to private canonical columns before concat.
    """
    frames=[]
    for source in items:
        frame=source['df'].copy()
        for semantic, original in source.get('mapping',{}).items():
            if semantic.startswith('_') or original not in frame.columns: continue
            frame[f'__{semantic}']=frame[original]
        frames.append(frame)
    mapping={key:f'__{key}' for key in ('customer','vendor','product','date','due_date','payment_date','status','net_sales','gross_sales','cash_price','term_price','discount','quantity','cost','amount','paid','outstanding','balance','unit_cost','warehouse','last_movement')}
    combined=pd.concat(frames,ignore_index=True,sort=False) if frames else pd.DataFrame()
    return combined, {k:v for k,v in mapping.items() if v in combined.columns}

def build_multi_source_intelligence(files:list[tuple[str,bytes]], finance_processor, statements:dict[str,Any]|None=None, max_mb:float=15.0)->dict[str,Any]:
    bundle=ingest_sources(files,finance_processor,max_mb=max_mb)
    sources=bundle['sources']; result={'sources':[],'files':bundle.get('files',[]),'reconciliation':{},'findings':[],'errors':bundle['errors'], 'source_quality': {'failed_files': list(bundle.get('errors',[])), 'processed_files': [], 'role_confidence': []}}
    grouped=_group_sources(sources)
    period_meta=(statements or {}).get('period_metadata') or {}
    period_days=period_meta.get('period_days') or 365
    as_of=period_meta.get('period_end')
    for role,items in grouped.items():
        combined,mappings=_canonicalize(items)


        file_names=[{'filename':s['filename'],'sheet':s['sheet'],'rows':s['rows'],'confidence':s['confidence']} for s in items]
        for s in items:
            result['source_quality']['processed_files'].append(s['filename'])
            result['source_quality']['role_confidence'].append({'filename':s['filename'],'sheet':s['sheet'],'role':s['role'],'confidence':s['confidence']})
            result['sources'].append({'filename':s['filename'],'sheet':s['sheet'],'role':s['role'],'confidence':s['confidence'],'rows':s['rows'],'mapping':s['mapping']})
        if role=='sales':
            analysis=analyze_sales(combined,mappings); analysis['source_files']=file_names; result['analysis_sales']=analysis
            result['findings'].extend([{**f,'source':'sales'} for f in analysis.get('findings',[])])
            try:
                from .pvm_engine import build_pvm_analysis
                if 'date' in mappings and 'product' in mappings and 'quantity' in mappings and 'net_sales' in mappings:
                    combined['_pvm_period'] = [str(d.year) if hasattr(d, 'year') else str(d)[:4] for d in combined[mappings['date']]]
                    pvm = build_pvm_analysis(combined, '_pvm_period', mappings['product'], mappings['quantity'], mappings['net_sales'])
                    analysis['pvm_analysis'] = pvm
            except Exception as e:
                pass
        elif role=='ar_aging':
            analysis=analyze_ar(combined,mappings,(statements or {}).get('profit_and_loss',{}).get('Net sales'),period_days,as_of_date=as_of); analysis['source_files']=file_names; result['analysis_ar']=analysis
        elif role=='ap_aging':
            cogs_val = (statements or {}).get('profit_and_loss',{}).get('Cost of sales') or (statements or {}).get('profit_and_loss',{}).get('COGS')
            analysis=analyze_ap(combined,mappings,cogs_val,period_days,as_of_date=as_of); analysis['source_files']=file_names; result['analysis_ap']=analysis
        elif role=='inventory':
            cogs_val = (statements or {}).get('profit_and_loss',{}).get('Cost of sales') or (statements or {}).get('profit_and_loss',{}).get('COGS')
            analysis=analyze_inventory(combined,mappings,cogs_val,period_days,as_of_date=as_of); analysis['source_files']=file_names; result['analysis_inventory']=analysis
    sales = result.pop('analysis_sales', None)
    ar = result.pop('analysis_ar', None)
    ap = result.pop('analysis_ap', None)
    inventory = result.pop('analysis_inventory', None)

    # Customer & Product Profitability
    from .customer_profitability_engine import build_customer_profitability_analysis
    from .product_profitability_engine import build_product_profitability_analysis
    from .pricing_opportunity_engine import build_pricing_opportunity_analysis

    cust_prof = build_customer_profitability_analysis(sales, ar)
    prod_prof = build_product_profitability_analysis(sales, inventory)
    pricing_opp = build_pricing_opportunity_analysis(sales)

    if cust_prof.get('findings'):
        result['findings'].extend([{**f, 'source': 'customer_profitability'} for f in cust_prof['findings']])
    if prod_prof.get('findings'):
        result['findings'].extend([{**f, 'source': 'product_profitability'} for f in prod_prof['findings']])
    if pricing_opp.get('findings'):
        result['findings'].extend([{**f, 'source': 'pricing_opportunity'} for f in pricing_opp['findings']])
    if ar and ar.get('findings'):
        result['findings'].extend([{**f, 'source': 'ar'} for f in ar['findings']])
    if ap and ap.get('findings'):
        result['findings'].extend([{**f, 'source': 'ap'} for f in ap['findings']])
    if inventory and inventory.get('findings'):
        result['findings'].extend([{**f, 'source': 'inventory'} for f in inventory['findings']])

    if statements:
        result['reconciliation'] = build_reconciliation(statements, sales, ar, ap, inventory)

    result['summary'] = {
        'finance_core_available': bool(statements),
        'sales_loaded': sales is not None,
        'ar_aging_loaded': ar is not None,
        'ap_aging_loaded': ap is not None,
        'inventory_loaded': inventory is not None,
        'customer_profitability_loaded': cust_prof.get('status') == 'PASS',
        'product_profitability_loaded': prod_prof.get('status') == 'PASS',
        'pricing_opportunity_loaded': pricing_opp.get('status') == 'PASS',
    }
    result['analysis'] = {
        'sales': sales,
        'ar_aging': ar,
        'ap_aging': ap,
        'inventory': inventory,
        'customer_profitability': cust_prof,
        'product_profitability': prod_prof,
        'pricing_opportunity': pricing_opp,
    }
    result['analysis_sales'] = sales
    result['analysis_ar'] = ar
    result['analysis_ap'] = ap
    result['analysis_inventory'] = inventory
    result['customer_profitability'] = cust_prof
    result['product_profitability'] = prod_prof
    result['pricing_opportunity'] = pricing_opp
    result['operational_finance'] = build_operational_finance(result, statements)
    return result
