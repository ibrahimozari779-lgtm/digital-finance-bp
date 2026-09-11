from __future__ import annotations
from typing import Any

def build_calculation_audit(statements: dict[str,Any]) -> dict[str,Any]:
    pl=statements['profit_and_loss']; bs=statements['balance_sheet']; k=statements['kpis']; checks=[]
    def add(name,calc,reported,tol=0.01):
        diff=None if calc is None or reported is None else float(calc)-float(reported)
        checks.append({'name':name,'calculated':calc,'reported':reported,'difference':diff,'status':'passed' if diff is not None and abs(diff)<=tol else 'failed'})
    add('Net sales = revenue - deductions',float(pl['Revenue'])-float(pl['Sales deductions']),pl['Net sales'])
    add('Gross profit = net sales - COGS',float(pl['Net sales'])-float(pl['COGS']),pl['Gross profit'])
    add('Operating profit = gross profit - opex',float(pl['Gross profit'])-float(pl['Operating expenses']),pl['Operating profit'])
    add('PBT bridge',float(pl['Operating profit'])+float(pl['Other operating income'])-float(pl['Other operating expense'])+float(pl['Other non-operating income'])-float(pl['Other non-operating expense'])-float(pl['Finance costs']),pl['Pre-tax profit'])
    add('Net profit = PBT - tax',float(pl['Pre-tax profit'])-float(pl['Tax expense']),pl['Net profit'])
    add('Balance sheet equation',float(bs['Total assets'])-float(bs['Total liabilities & equity']),float(bs['Balance check difference']))
    add('Net debt = debt - cash',float(k['financial_debt'])-float(k['cash']),float(k['net_debt']))
    failed=[c for c in checks if c['status']=='failed']
    return {'status':'PASS' if not failed else 'FAIL','checks':checks,'failed_count':len(failed),'note':'Core KPI formulas are independently re-evaluated from the statement layer before being exposed as validated facts.'}
