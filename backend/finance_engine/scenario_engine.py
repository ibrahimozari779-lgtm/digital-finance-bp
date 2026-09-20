from __future__ import annotations
from typing import Any


def _band(value: float | None, bands: list[tuple[float, float]], default: float) -> float:
    """Pick the first (threshold, result) pair whose threshold the value clears.

    `bands` must be sorted with the highest threshold first. Used throughout
    this module so every scenario's assumed magnitude reflects how far the
    underlying ratio actually is from a healthy range *for this company, in
    this period* - not a single fixed percentage applied to every business
    regardless of its current financial state.
    """
    if value is None:
        return default
    for threshold, result in bands:
        if value >= threshold:
            return result
    return default


def build_scenarios(statements: dict[str, Any]) -> list[dict[str, Any]]:
    pl=statements['profit_and_loss']; k=statements['kpis']; bs=statements['balance_sheet']
    sales=float(pl.get('Net sales') or 0); cogs=float(pl.get('COGS') or 0); gp=float(pl.get('Gross profit') or 0); opex=float(pl.get('Operating expenses') or 0)
    op=float(pl.get('Operating profit') or 0); fin=float(pl.get('Finance costs') or 0); pbt=float(pl.get('Pre-tax profit') or 0); tax=float(pl.get('Tax expense') or 0); net=float(pl.get('Net profit') or 0)
    ar=float(k.get('receivables') or 0); inv=float(k.get('inventory') or 0); debt=float(k.get('financial_debt') or 0); cash=float(k.get('cash') or 0); net_debt=float(k.get('net_debt') or 0)
    ca=float(bs.get('Current assets') or 0); cl=float(bs.get('Current liabilities') or 0); eq=float(bs.get('Total equity incl. current result') or 0)
    debt_to_equity = k.get('debt_to_equity')
    current_ratio = k.get('current_ratio')
    gross_margin_pct = k.get('gross_margin_pct')
    tax_rate=(tax/pbt) if pbt>0 else 0.0
    scenarios=[]
    def tax_on_increment(delta_pbt):
        tax_delta=max(0.0,delta_pbt)*tax_rate
        return tax_delta
    def add(i,name,assumption,change,cash_impact=0.0,profit_impact=0.0,net_profit_impact=None,debt_impact=0.0,pbt_impact=0.0,tax_impact=0.0,confidence='medium',limitations='',target_pct=None,current_state=None):
        if net_profit_impact is None: net_profit_impact=profit_impact
        new_cash=cash+cash_impact; new_debt=debt+debt_impact; new_net_debt=new_debt-new_cash
        scenarios.append({'scenario_id':i,'name':name,'assumptions':[assumption],'baseline':{'cash':cash,'financial_debt':debt,'net_debt':net_debt,'net_profit':net},
                           'change':change,'cash_impact':cash_impact,'cash_used':max(0,-cash_impact),'cash_released':max(0,cash_impact),
                           'gross_profit_impact':change.get('gross_profit',0.0) if isinstance(change,dict) else 0.0,
                           'pbt_impact':pbt_impact,'tax_impact':tax_impact,'profit_impact':net_profit_impact,
                           'net_profit_impact':net_profit_impact,'debt_impact':debt_impact,'net_debt_impact':new_net_debt-net_debt,
                           'liquidity_impact':((ca+cash_impact)/cl-ca/cl) if cl else None,
                           'leverage_impact':(new_debt/eq-debt/eq) if eq else None,'confidence':confidence,
                           # target_pct/current_state make the "why this %, not some other %" reasoning explicit:
                           # the assumed magnitude is derived from where this company's own ratio sits today,
                           # not a fixed template value applied regardless of financial state.
                           'target_pct':target_pct,'current_state':current_state,
                           'limitations':limitations or 'Mekanik duyarlılık analizidir; operasyonel davranış ve zamanlama ayrıca doğrulanmalıdır.'})

    # --- S001: receivables reduction ------------------------------------------------
    # More receivables tied up relative to sales -> more realistic room (and urgency)
    # to bring that ratio down, so the assumed release scales with the actual
    # receivables/sales ratio instead of a flat 10% for every company.
    ar_to_sales = (ar / sales) if sales else None
    ar_pct = _band(ar_to_sales, [(0.50, 0.20), (0.35, 0.15), (0.20, 0.10)], 0.05)
    add('S001', f'Alacakları %{ar_pct*100:.0f} azalt', 'Tahsil edilen tutarın tamamı nakit olarak tutulur.',
        {'receivables': -ar*ar_pct}, cash_impact=ar*ar_pct, confidence='medium',
        target_pct=ar_pct, current_state={'receivables_to_sales_pct': round(ar_to_sales*100,1) if ar_to_sales is not None else None})

    # --- S002: financial debt reduction ----------------------------------------------
    # Higher leverage (debt/equity) -> a more ambitious deleveraging target is both
    # more urgent and, relative to the balance sheet size, more realistic to model.
    debt_pct = _band(debt_to_equity, [(3.0, 0.20), (2.0, 0.15), (1.0, 0.10)], 0.05)
    repay=min(debt*debt_pct,cash)
    # Debt repayment creates future finance-cost benefit, but only if a finance-cost saving assumption is made.
    annual_interest_rate=(fin/debt) if debt>0 else 0.0
    future_fin=repay*annual_interest_rate
    future_tax=tax_on_increment(future_fin)
    future_net=future_fin-future_tax
    add('S002', f'Finansal borcu %{debt_pct*100:.0f} azalt', 'Mevcut nakitten borç ödenir; gelecekte aynı borcun faiz yükünün oluşmadığı varsayılır.',
        {'financial_debt':-repay},cash_impact=-repay,debt_impact=-repay,pbt_impact=future_fin,tax_impact=future_tax,net_profit_impact=future_net,
        confidence='low' if debt and fin else 'medium',limitations='Gelecekteki faiz tasarrufu mevcut Finansman Gideri / Finansal Borç oranı üzerinden hesaplanır; gerçek sözleşme faiziyle güncellenebilir.',
        target_pct=debt_pct, current_state={'debt_to_equity': round(debt_to_equity,2) if debt_to_equity is not None else None})

    # --- S003: gross margin uplift ----------------------------------------------------
    # When the current margin already sits well below a general-purpose 30% reference
    # band, showing a bigger (but still deliberately modest) improvement scenario is
    # more relevant than the same +1pp used for an already-healthy margin, where a
    # smaller, more realistic increment is shown instead.
    margin_gap = (30.0 - gross_margin_pct) if gross_margin_pct is not None else None
    margin_pp = _band(margin_gap, [(15.0, 0.02), (5.0, 0.015)], 0.01)
    uplift=sales*margin_pp
    tax_u=tax_on_increment(uplift)
    add('S003', f'Brüt marjı +{margin_pp*100:.1f} puan', 'Satış hacmi ve faaliyet giderleri sabit; artış tamamen PBT\'ye gider.',
        {'gross_profit':uplift},pbt_impact=uplift,tax_impact=tax_u,net_profit_impact=uplift-tax_u,confidence='high',
        target_pct=margin_pp, current_state={'gross_margin_pct': round(gross_margin_pct,1) if gross_margin_pct is not None else None})

    # --- S004: inventory reduction -----------------------------------------------------
    if inv>0:
        inv_to_sales = (inv / sales) if sales else None
        inv_pct = _band(inv_to_sales, [(0.35, 0.15), (0.20, 0.10)], 0.05)
        add('S004', f'Envanteri %{inv_pct*100:.0f} azalt', 'Envanterden nakit serbestleştiği ve kâr etkisi olmadığı varsayılır.',
            {'inventory':-inv*inv_pct},cash_impact=inv*inv_pct,confidence='medium',
            target_pct=inv_pct, current_state={'inventory_to_sales_pct': round(inv_to_sales*100,1) if inv_to_sales is not None else None})

    # --- S005: operating expense reduction ---------------------------------------------
    # A heavier opex/sales load leaves more realistic room for a cost-discipline
    # program than a lean cost base already running close to the bone.
    opex_to_sales = (opex / sales) if sales else None
    opex_pct = _band(opex_to_sales, [(0.30, 0.05), (0.15, 0.03)], 0.02)
    opex_save=opex*opex_pct; tax_o=tax_on_increment(opex_save)
    add('S005', f'Faaliyet giderlerini %{opex_pct*100:.0f} azalt', 'Giderlerin bir kısmı yönetilebilir ve tasarruf doğrudan PBT\'ye yansır.',
        {'operating_expenses':-opex*opex_pct,'operating_profit':opex_save},pbt_impact=opex_save,tax_impact=tax_o,net_profit_impact=opex_save-tax_o,confidence='medium',
        target_pct=opex_pct, current_state={'opex_to_sales_pct': round(opex_to_sales*100,1) if opex_to_sales is not None else None})

    # --- S006: payables term extension --------------------------------------------------
    # A tighter current ratio makes a larger payment-term extension both more
    # urgent (liquidity relief) and the natural lever a CFO would reach for first.
    pay=float(k.get('payables') or 0)
    pay_pct = _band((-current_ratio if current_ratio is not None else None), [(-1.0, 0.20), (-1.2, 0.15), (-1.5, 0.10)], 0.05)
    add('S006', f'Ticari borç vadesini %{pay_pct*100:.0f} uzat', 'Tedarikçi koşulları değişmeden ödeme zamanı ötelenir.',
        {'payables':pay*pay_pct},cash_impact=pay*pay_pct,confidence='low',
        limitations='Vade uzaması yalnızca zamanlama etkisidir; supplier relationship/cost etkisi modellenmez.',
        target_pct=pay_pct, current_state={'current_ratio': round(current_ratio,2) if current_ratio is not None else None})

    return scenarios
