from __future__ import annotations
from typing import Any
import pandas as pd

def build_pvm_analysis(sales_df: pd.DataFrame, period_col: str, product_col: str, qty_col: str, revenue_col: str) -> dict[str, Any]:
    if not all(c in sales_df.columns for c in [period_col, product_col, qty_col, revenue_col]):
        return {"available": False, "status": "DATA_MISSING_EXPECTED", "reason": f"Eksik sütunlar. PVM için '{period_col}', '{product_col}', '{qty_col}', '{revenue_col}' gereklidir."}

    work = sales_df.copy()
    work.loc[:, qty_col] = pd.to_numeric(work[qty_col], errors='coerce').fillna(0)
    work.loc[:, revenue_col] = pd.to_numeric(work[revenue_col], errors='coerce').fillna(0)

    periods = sorted([p for p in work[period_col].unique() if pd.notna(p)])
    if len(periods) < 2:
        return {"available": False, "status": "DATA_MISSING_EXPECTED", "reason": "PVM hesaplaması için en az 2 farklı dönem (period) verisi gereklidir."}


    per1, per2 = periods[-2], periods[-1]

    df1 = work[work[period_col] == per1].groupby(product_col).agg({qty_col: 'sum', revenue_col: 'sum'}).copy()
    df2 = work[work[period_col] == per2].groupby(product_col).agg({qty_col: 'sum', revenue_col: 'sum'}).copy()

    df1.loc[:, 'price'] = df1[revenue_col] / df1[qty_col].replace(0, pd.NA)
    df2.loc[:, 'price'] = df2[revenue_col] / df2[qty_col].replace(0, pd.NA)

    merged = df1.join(df2, lsuffix='_1', rsuffix='_2', how='outer').fillna(0)

    total_rev_1 = float(merged[f"{revenue_col}_1"].sum())
    total_rev_2 = float(merged[f"{revenue_col}_2"].sum())

    results = []
    tot_vol, tot_px, tot_mix = 0.0, 0.0, 0.0

    for product, row in merged.iterrows():
        v1, v2 = float(row[f"{qty_col}_1"]), float(row[f"{qty_col}_2"])
        r1, r2 = float(row[f"{revenue_col}_1"]), float(row[f"{revenue_col}_2"])
        price1 = float(row['price_1']) if v1 != 0 else 0.0
        price2 = float(row['price_2']) if v2 != 0 else 0.0

        if v1 == 0 and v2 > 0:
            vol_eff = v2 * price2
            px_eff = 0.0
            mix_eff = 0.0
        elif v2 == 0 and v1 > 0:
            vol_eff = -v1 * price1
            px_eff = 0.0
            mix_eff = 0.0
        else:
            vol_eff = (v2 - v1) * price1
            px_eff = (price2 - price1) * v1
            mix_eff = (price2 - price1) * (v2 - v1)

        tot_vol += vol_eff
        tot_px += px_eff
        tot_mix += mix_eff

        if abs(r2 - r1) > 0.01:
            results.append({
                "product": str(product),
                "revenue_1": r1,
                "revenue_2": r2,
                "delta": r2 - r1,
                "volume_effect": vol_eff,
                "price_effect": px_eff,
                "mix_effect": mix_eff
            })

    results.sort(key=lambda x: abs(x['delta']), reverse=True)

    return {
        "available": True,
        "period_1": str(per1),
        "period_2": str(per2),
        "revenue_1": total_rev_1,
        "revenue_2": total_rev_2,
        "revenue_delta": total_rev_2 - total_rev_1,
        "total_volume_effect": float(tot_vol),
        "total_price_effect": float(tot_px),
        "total_mix_effect": float(tot_mix),
        "product_level": results[:15]
    }
