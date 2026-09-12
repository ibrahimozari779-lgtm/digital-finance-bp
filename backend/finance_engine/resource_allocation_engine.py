"""Resource Allocation & Capital Deployment Engine.

Answers the three critical questions every SME business owner asks:
1. "Para Nerede?" (Where is company cash trapped? Working capital vs Cash vs Debt)
2. "Nerede Kâr Var?" (Where is profit generated? Stars, high-margin products, top customers)
3. "Nerede Kayıp Var?" (Where are financial leakages? Finance costs, discounts, slow inventory, bad debts)
"""
from __future__ import annotations

from typing import Any


def build_resource_allocation_analysis(
    statements: dict[str, Any],
    data_hub: dict[str, Any] | None = None,
) -> dict[str, Any]:
    pl = statements.get("profit_and_loss", {})
    bs = statements.get("balance_sheet", {})
    k = statements.get("kpis", {})

    cash = float(k.get("cash") or 0.0)
    receivables = float(k.get("receivables") or 0.0)
    inventory = float(k.get("inventory") or 0.0)
    current_assets = float(bs.get("Current assets") or (cash + receivables + inventory))
    fixed_assets = float(bs.get("Non-current assets") or 0.0)
    total_assets = float(bs.get("Total assets") or (current_assets + fixed_assets))

    trade_payables = float(k.get("payables") or float(bs.get("Trade payables") or 0.0))
    short_term_debt = float(k.get("short_term_debt") or 0.0)
    long_term_debt = float(k.get("long_term_debt") or 0.0)
    financial_debt = float(k.get("financial_debt") or (short_term_debt + long_term_debt))
    equity = float(bs.get("Total equity incl. current result") or 0.0)

    working_capital_tied = receivables + inventory
    total_operational_capital = working_capital_tied + cash

    # Where is money tied up?
    cash_tied_breakdown = [
        {
            'name': 'Ticari Alacaklar (Müşterilerde)',
            'amount': round(receivables, 2),
            'share_pct': round((receivables / total_operational_capital * 100), 1) if total_operational_capital > 0 else 0.0,
            'status': 'high' if receivables > cash * 3 else 'normal',
            'note': 'Satışı yapılmış ancak henüz kasaya/bankaya girmemiş vadeli para.',
        },
        {
            'name': 'Stoklar (Depoda)',
            'amount': round(inventory, 2),
            'share_pct': round((inventory / total_operational_capital * 100), 1) if total_operational_capital > 0 else 0.0,
            'status': 'high' if inventory > cash * 2 else 'normal',
            'note': 'Hammadde veya mamul olarak depoda fiziken bekleyen nakit.',
        },
        {
            'name': 'Kasa ve Bankalar (Serbest Nakit)',
            'amount': round(cash, 2),
            'share_pct': round((cash / total_operational_capital * 100), 1) if total_operational_capital > 0 else 0.0,
            'status': 'critical' if cash < financial_debt * 0.2 else 'positive',
            'note': 'Hemen kullanıma hazır serbest likidite.',
        },
    ]

    wc_ratio_pct = round((working_capital_tied / total_operational_capital * 100), 1) if total_operational_capital > 0 else 0.0
    where_is_money_story = (
        f"Şirketinizin operasyonel sermayesinin %{wc_ratio_pct}'si ({working_capital_tied:,.0f} TL) nakitte değil; "
        f"müşteri alacaklarında ({receivables:,.0f} TL) ve depodaki stokta ({inventory:,.0f} TL) bağlı bulunmaktadır. "
        f"Kasadaki serbest nakit ({cash:,.0f} TL) toplam finansal borcun ({financial_debt:,.0f} TL) sadece %{(cash/financial_debt*100 if financial_debt else 100):.1f}'ini karşılamaktadır."
    )

    # Where is profit? ("Nerede Kâr Var?")
    net_sales = float(pl.get("Net sales") or 0.0)
    gross_profit = float(pl.get("Gross profit") or 0.0)
    operating_profit = float(pl.get("Operating profit") or 0.0)

    sales_analysis = (data_hub or {}).get("analysis_sales") or {}
    top_custs = sales_analysis.get("top_customers", [])
    top_prods = sales_analysis.get("top_products", [])

    profit_drivers = [
        {
            'area': 'Ana Faaliyetler (Brüt Kâr)',
            'amount': round(gross_profit, 2),
            'note': f"Net satışların ({net_sales:,.0f} TL) %{(gross_profit/net_sales*100 if net_sales else 0):.1f}'i brüt kâra dönüşüyor.",
        }
    ]
    if top_custs:
        profit_drivers.append({
            'area': 'En Kârlı Müşteri Tabanı',
            'amount': round(sum(c.get('sales', 0) for c in top_custs[:3]), 2),
            'note': f"İlk 3 müşteri ({', '.join(c.get('name','') for c in top_custs[:3])}) cironun ana taşıyıcısı.",
        })

    # Where are leakages? ("Nerede Kayıp Var?")
    finance_costs = float(pl.get("Finance costs") or 0.0)
    discounts = float(pl.get("Sales discounts") or float(sales_analysis.get("discounts") or 0.0))
    inv_analysis = (data_hub or {}).get("analysis_inventory") or {}
    stale_stock = float(inv_analysis.get("stale_180_amount") or 0.0)
    ar_analysis = (data_hub or {}).get("analysis_ar") or {}
    ar_overdue = float(ar_analysis.get("overdue") or 0.0)

    leakages = []
    if finance_costs > 0:
        fin_impact_pct = round((finance_costs / operating_profit * 100), 1) if operating_profit > 0 else 100.0
        leakages.append({
            'name': 'Finansman Giderleri (Kredi Faizleri)',
            'amount': round(finance_costs, 2),
            'severity': 'critical' if fin_impact_pct > 60 else 'high',
            'impact_description': f"Faaliyet kârının %{fin_impact_pct:.0f}'sini tek başına tüketiyor ({finance_costs:,.0f} TL).",
        })
    if discounts > 0:
        leakages.append({
            'name': 'Satış İskontoları & İndirimler',
            'amount': round(discounts, 2),
            'severity': 'medium',
            'impact_description': f"Doğrudan cirodan feragat edilen kâr tamponu ({discounts:,.0f} TL).",
        })
    if stale_stock > 0:
        leakages.append({
            'name': '180+ Gün Yaşlanmış/Ölü Stok',
            'amount': round(stale_stock, 2),
            'severity': 'high',
            'impact_description': f"Depoda hareketsiz kalarak değer kaybeden ve sermaye bağlayan stok ({stale_stock:,.0f} TL).",
        })
    if ar_overdue > 0:
        leakages.append({
            'name': 'Vadesi Geçmiş Alacaklar',
            'amount': round(ar_overdue, 2),
            'severity': 'critical',
            'impact_description': f"Müşterilerde vadesi aşıldığı halde tahsil edilemeyen likidite ({ar_overdue:,.0f} TL).",
        })

    return {
        'status': 'PASS',
        'where_is_money': {
            'summary_narrative': where_is_money_story,
            'breakdown': cash_tied_breakdown,
            'working_capital_tied': round(working_capital_tied, 2),
            'free_cash': round(cash, 2),
            'total_debt': round(financial_debt, 2),
        },
        'where_is_profit': {
            'gross_profit': round(gross_profit, 2),
            'operating_profit': round(operating_profit, 2),
            'drivers': profit_drivers,
        },
        'where_is_loss': {
            'leakages': leakages,
            'total_visible_leakage': round(finance_costs + discounts + stale_stock, 2),
        },
    }
