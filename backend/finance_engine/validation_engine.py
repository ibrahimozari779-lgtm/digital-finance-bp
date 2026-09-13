from __future__ import annotations
from typing import Any

def build_calculation_audit(statements: dict[str, Any]) -> dict[str, Any]:
    pl = statements.get('profit_and_loss') or {}
    bs = statements.get('balance_sheet') or {}
    k = statements.get('kpis') or {}
    checks = []

    def add(name, calc, reported, tol=0.01):
        diff = None if calc is None or reported is None else float(calc) - float(reported)
        checks.append({
            'name': name,
            'calculated': calc,
            'reported': reported,
            'difference': diff,
            'status': 'passed' if diff is not None and abs(diff) <= tol else 'failed'
        })

    def _v(d: dict, key: str) -> float | None:
        v = d.get(key)
        try:
            return float(v) if v is not None else None
        except (ValueError, TypeError):
            return None

    # Safe independent evaluations
    rev = _v(pl, 'Revenue')
    ded = _v(pl, 'Sales deductions')
    net_s = _v(pl, 'Net sales')
    if rev is not None and ded is not None and net_s is not None:
        add('Net sales = revenue - deductions', rev - ded, net_s)

    cogs = _v(pl, 'COGS')
    gp = _v(pl, 'Gross profit')
    if net_s is not None and cogs is not None and gp is not None:
        add('Gross profit = net sales - COGS', net_s - cogs, gp)

    opex = _v(pl, 'Operating expenses')
    op = _v(pl, 'Operating profit')
    if gp is not None and opex is not None and op is not None:
        add('Operating profit = gross profit - opex', gp - opex, op)

    oth_inc = _v(pl, 'Other operating income') or 0.0
    oth_exp = _v(pl, 'Other operating expense') or 0.0
    non_inc = _v(pl, 'Other non-operating income') or 0.0
    non_exp = _v(pl, 'Other non-operating expense') or 0.0
    fin = _v(pl, 'Finance costs') or 0.0
    pbt = _v(pl, 'Pre-tax profit')
    if op is not None and pbt is not None:
        add('PBT bridge', op + oth_inc - oth_exp + non_inc - non_exp - fin, pbt)

    tax = _v(pl, 'Tax expense') or 0.0
    np = _v(pl, 'Net profit')
    if pbt is not None and np is not None:
        add('Net profit = PBT - tax', pbt - tax, np)

    tot_a = _v(bs, 'Total assets')
    tot_le = _v(bs, 'Total liabilities & equity')
    bal_diff = _v(bs, 'Balance check difference') or 0.0
    if tot_a is not None and tot_le is not None:
        add('Balance sheet equation', tot_a - tot_le, bal_diff)

    fin_d = _v(k, 'financial_debt')
    cash = _v(k, 'cash')
    net_d = _v(k, 'net_debt')
    if fin_d is not None and cash is not None and net_d is not None:
        add('Net debt = debt - cash', fin_d - cash, net_d)

    failed = [c for c in checks if c['status'] == 'failed']
    return {
        'status': 'PASS' if not failed else 'FAIL',
        'checks': checks,
        'failed_count': len(failed),
        'note': 'Core KPI formulas are independently re-evaluated from the statement layer before being exposed as validated facts.'
    }
