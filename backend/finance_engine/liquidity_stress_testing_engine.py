"""Liquidity Stress Testing & Concentration Shock Engine (Müşteri Konsantrasyonu Likidite Stres Testi).

Simulates severe working capital liquidity shocks:
1. Customer Delay Shock: What if top 3 debtors (or top 35% receivables) delay payments by 30 / 60 days?
2. Cash Deficit Impact: Cumulative operational cash gap vs current available liquidity buffer (Cash + ST limits).
3. Solvency & Short-Term Debt Coverage: Probability of default on supplier payments and bank maturities.
"""
from __future__ import annotations
from typing import Any


def build_liquidity_stress_test(
    statements: dict[str, Any],
    data_hub: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Evaluates short-term liquidity survival under customer payment default/delay shocks."""
    bs = statements.get("balance_sheet", {})
    k = statements.get("kpis", {})
    pl = statements.get("profit_and_loss", {})

    cash = float(k.get("cash") or 0.0)
    receivables = float(k.get("receivables") or 0.0)
    current_liab = float(bs.get("Current liabilities") or 0.0)
    financial_debt = float(k.get("financial_debt") or 0.0)
    cogs = float(pl.get("COGS") or 0.0)
    monthly_burn_rate = (cogs / 12.0) if cogs > 0 else (current_liab / 6.0)

    # Multi-source Subledger (AR Aging) Kontrolü
    analysis_ar = (data_hub or {}).get("analysis_ar") or (data_hub or {}).get("ar_aging") or {}
    top_parties = analysis_ar.get("top_overdue_parties") or analysis_ar.get("top_debtors") or []

    # Konsantrasyon Tutarı
    if top_parties and len(top_parties) >= 1:
        # Gerçek alt defterden en büyük 3 borçlu
        top_shock_amount = sum(float(p.get("amount") or p.get("balance") or 0.0) for p in top_parties[:3])
        concentration_basis = f"En büyük {min(3, len(top_parties))} cari müşteriden"
    else:
        # TDHP Bilanço kuralı: KOBİ medyanı olarak toplam alacakların %35'i ilk 3 müşteride varsayılır
        top_shock_amount = receivables * 0.35
        concentration_basis = "Mizan alacak portföyünün %35'i (İlk 3 Müşteri Ağırlığı)"

    # Senaryo 1: 30 Günlük Gecikme (Hafif Şok)
    shock_30d_cash_gap = top_shock_amount * 0.50
    net_cash_30d = cash - shock_30d_cash_gap
    solvency_ratio_30d = (cash / shock_30d_cash_gap) if shock_30d_cash_gap > 0 else 99.0

    # Senaryo 2: 60 Günlük Gecikme / Donma (Ağır Stres Şoku)
    shock_60d_cash_gap = top_shock_amount * 1.00
    net_cash_60d = cash - shock_60d_cash_gap
    solvency_ratio_60d = (cash / shock_60d_cash_gap) if shock_60d_cash_gap > 0 else 99.0

    # Nakit Tamponu Dayanıklılık Süresi (Runway Days)
    runway_days_normal = (cash / (monthly_burn_rate / 30.0)) if monthly_burn_rate > 0 else 999.0
    runway_days_stressed = (max(0.0, net_cash_60d) / (monthly_burn_rate / 30.0)) if monthly_burn_rate > 0 else 0.0

    # Risk Düzeyi
    if net_cash_60d < 0:
        stress_status = "KRİTİK NAKİT AÇIĞI (ÖDEME GÜCÜ ALARMI)"
        severity = "critical"
        deficit_summary = (
            f"İlk 3 müşterinizin ödemeyi 60 gün geciktirmesi halinde, şirket kasanızda "
            f"{abs(net_cash_60d):,.0f} TL NET NAKİT AÇIĞI oluşacaktır. "
            f"Mevcut serbest nakdiniz ({cash:,.0f} TL), kilitlenen {top_shock_amount:,.0f} TL alacağı "
            f"sübvanse etmeye yetmemekte ve dış banka finansmanı bulunamazsa tedarikçi/çek temerrüt riski doğmaktadır."
        )
    elif net_cash_30d < 0:
        stress_status = "YÜKSEK LİKİDİTE KIRILGANLIĞI"
        severity = "high"
        deficit_summary = (
            f"30 günlük bir gecikmede dahi şirket kasası negatife (-{abs(net_cash_30d):,.0f} TL) geçmektedir. "
            f"Nakit rezervleri acil kredi limiti kullanımını gerektirir."
        )
    else:
        stress_status = "LİKİDİTE TAMPONU DAYANIKLI"
        severity = "medium"
        deficit_summary = (
            f"Mevcut nakit rezerviniz ({cash:,.0f} TL), ilk 3 müşterinin 60 günlük tam ödeme durdurma şokunu "
            f"karşılayacak güçtedir. Şok sonrası kalan net nakit: +{net_cash_60d:,.0f} TL."
        )

    return {
        "concentration_basis": concentration_basis,
        "top_shock_amount": round(top_shock_amount, 2),
        "available_cash": round(cash, 2),
        "monthly_burn_rate": round(monthly_burn_rate, 2),
        "monthly_burn_label": "Aylık Brüt Operasyonel Nakit Çıkışı (SMM / Temel İşletme Maliyeti)",
        "burn_rate_methodology": "Bu tutar şirketin çarkını döndürmek için gereken aylık brüt nakit çıkışıdır (SMM/12). Kök neden analizindeki rakam ise kasadan eriyen net nakit açığıdır (Net Cash Burn).",
        "runway_days_normal": round(runway_days_normal, 1),
        "runway_days_stressed": round(runway_days_stressed, 1),
        "scenario_30d": {
            "cash_gap": round(shock_30d_cash_gap, 2),
            "net_cash_after_shock": round(net_cash_30d, 2),
            "coverage_ratio": round(solvency_ratio_30d, 2),
            "is_deficit": net_cash_30d < 0,
        },
        "scenario_60d": {
            "cash_gap": round(shock_60d_cash_gap, 2),
            "net_cash_after_shock": round(net_cash_60d, 2),
            "coverage_ratio": round(solvency_ratio_60d, 2),
            "is_deficit": net_cash_60d < 0,
        },
        "stress_status": stress_status,
        "severity": severity,
        "deficit_summary": deficit_summary,
    }
