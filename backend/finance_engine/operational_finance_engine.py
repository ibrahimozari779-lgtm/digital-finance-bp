"""Cross-source operational finance signals, kept explicitly evidence-based."""
from __future__ import annotations
from typing import Any


def build_operational_finance(data_hub: dict[str, Any] | None, statements: dict[str, Any] | None) -> dict[str, Any]:
    analysis=(data_hub or {}).get('analysis') or {}
    sales, ar, ap, inventory=(analysis.get('sales') or {}, analysis.get('ar_aging') or {}, analysis.get('ap_aging') or {}, analysis.get('inventory') or {})
    pl=(statements or {}).get('profit_and_loss') or {}
    signals=[]
    overdue_ar=float(ar.get('overdue') or sales.get('overdue_amount_by_status') or 0)
    stale=float(inventory.get('stale_180_amount') or 0)
    overdue_ap=float(ap.get('overdue') or 0)
    cash_release=overdue_ar + stale
    if overdue_ar: signals.append({'code':'OF-AR','title':'Tahsilat serbest nakit fırsatı','evidence_amount':overdue_ar,'status':'observed','action':'Vadesi geçmiş müşterileri tahsilat planına al.'})
    if stale: signals.append({'code':'OF-INV','title':'Stokta bağlı nakit','evidence_amount':stale,'status':'observed','action':'Yaşlanmış SKU’lar için satış / tasfiye planı oluştur.'})
    if overdue_ap: signals.append({'code':'OF-AP','title':'Tedarikçi ödeme baskısı','evidence_amount':overdue_ap,'status':'observed','action':'Kritik tedarikçileri ve ödeme takvimini önceliklendir.'})
    return {'available_sources':[name for name,value in [('sales',sales),('ar_aging',ar),('ap_aging',ap),('inventory',inventory)] if value],
            'cash_release_proxy':cash_release or None,
            'cash_release_proxy_note':'Tahsil edilebilir veya tasfiye edilebilir tutar değildir; operasyonel takip için üst sınır niteliğinde brüt maruziyettir.' if cash_release else None,
            'signals':signals,
            'profitability_coverage':{'customer_profitability':bool(sales.get('customer_profitability')),'product_profitability':bool(sales.get('product_profitability')),'transaction_cost_available':sales.get('cogs') is not None}}
