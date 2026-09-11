from __future__ import annotations
from typing import Any

def reconciliation_item(name:str, gl_value:float|None, source_value:float|None, tolerance:float=0.01)->dict[str,Any]:
    if gl_value is None or source_value is None:
        return {'name':name,'status':'not_available','gl_value':gl_value,'source_value':source_value,'difference':None,'difference_pct':None,'tolerance':tolerance}
    diff=float(source_value)-float(gl_value)
    base=max(abs(float(gl_value)),1.0)
    return {'name':name,'status':'matched' if abs(diff)<=tolerance else ('warning' if abs(diff)/base<=0.01 else 'material_difference'),'gl_value':float(gl_value),'source_value':float(source_value),'difference':diff,'difference_pct':diff/base*100,'tolerance':tolerance}

def build_reconciliation(statements:dict[str,Any], sales:dict[str,Any]|None=None, ar:dict[str,Any]|None=None, ap:dict[str,Any]|None=None, inventory:dict[str,Any]|None=None)->dict[str,Any]:
    pl=statements.get('profit_and_loss',{}); k=statements.get('kpis',{})
    checks=[reconciliation_item('Revenue vs Sales Data',pl.get('Revenue'),(sales.get('gross_or_revenue') if sales and sales.get('gross_or_revenue') is not None else sales.get('gross_sales')) if sales else None),
            reconciliation_item('Net Sales vs Sales Data',pl.get('Net sales'),sales.get('net_sales') if sales else None),
            reconciliation_item('Trade Receivables vs AR Aging',k.get('receivables'),ar.get('outstanding') if ar else None),
            reconciliation_item('Trade Payables vs AP Aging',k.get('payables'),ap.get('outstanding') if ap else None),
            reconciliation_item('Inventory vs Inventory File',k.get('inventory'),inventory.get('value') if inventory else None)]
    available=[x for x in checks if x['status']!='not_available']
    material=[x for x in available if x['status']=='material_difference']
    warnings=[x for x in available if x['status']=='warning']
    return {'checks':checks,'matched_count':sum(x['status']=='matched' for x in checks),'warning_count':len(warnings),'material_difference_count':len(material),'status':'matched' if material==[] and warnings==[] and available else ('review' if material or warnings else 'not_available')}
