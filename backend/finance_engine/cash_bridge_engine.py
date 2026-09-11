from __future__ import annotations
from typing import Any

def _v(s,k): return float(s.get('kpis',{}).get(k) or 0)

def build_cash_bridge(current: dict[str,Any], previous: dict[str,Any] | None = None) -> dict[str,Any]:
    if previous is None:
        return {'available':False,'mode':'snapshot','note':'Gerçek nakit akış köprüsü için en az iki dönem gerekir. Tek dönem verisinden nakit akışı uydurulmaz.','working_capital_proxy':{'receivables':_v(current,'receivables'),'inventory':_v(current,'inventory'),'payables':_v(current,'payables')}}
    ck=current['kpis']; pk=previous['kpis']
    dr=float(ck.get('receivables') or 0)-float(pk.get('receivables') or 0)
    di=float(ck.get('inventory') or 0)-float(pk.get('inventory') or 0)
    dp=float(ck.get('payables') or 0)-float(pk.get('payables') or 0)
    op=float(current['profit_and_loss'].get('Operating profit') or 0)
    net_profit=float(current['profit_and_loss'].get('Net profit') or 0)
    wc_release=-dr-di+dp
    operating_proxy=op+wc_release
    cash_change=float(ck.get('cash') or 0)-float(pk.get('cash') or 0)
    debt_change=float(ck.get('financial_debt') or 0)-float(pk.get('financial_debt') or 0)
    # Cash realization: what share of the NET PROFIT actually shows up as
    # operating cash. Uses net profit (not operating profit) as the anchor
    # because "does book profit really turn into cash" is a net-profit
    # question - finance costs and tax already happened and are real cash
    # events too, so they belong in the bridge, not stripped out before it.
    non_operating_addback = op - net_profit  # finance costs + tax + non-operating items, net
    operating_cash_flow_proxy = net_profit + non_operating_addback + wc_release  # == operating_proxy, expressed from net profit
    cash_realization_pct = (operating_cash_flow_proxy / net_profit * 100) if net_profit else None
    return {'available':True,'mode':'management_bridge','opening_cash':float(pk.get('cash') or 0),'closing_cash':float(ck.get('cash') or 0),'cash_change':cash_change,'operating_profit':op,'net_profit':net_profit,'working_capital_effect':wc_release,'working_capital_components':{'receivables_effect':-dr,'inventory_effect':-di,'payables_effect':dp},'debt_change':debt_change,'unexplained_cash_change':cash_change-operating_proxy-debt_change,'operating_cash_flow_proxy':operating_cash_flow_proxy,'non_operating_addback':non_operating_addback,'cash_realization_pct':cash_realization_pct,'note':'Bu köprü yönetimsel bir proxydir. Gerçek CFO cash flow için banka hareketleri, capex ve finansman işlemleri gerekir.'}
