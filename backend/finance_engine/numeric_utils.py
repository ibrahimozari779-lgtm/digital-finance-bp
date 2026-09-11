from __future__ import annotations
import math, re
from typing import Any
import pandas as pd

CURRENCY_RE = re.compile(r"[₺$€£¥₹]|TL|TRY|USD|EUR|GBP", re.I)
SPACE_RE = re.compile(r"\s+")

def parse_number(value: Any) -> float | None:
    if value is None or (isinstance(value, float) and math.isnan(value)) or pd.isna(value):
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).strip()
    if not s:
        return None
    neg = s.startswith('(') and s.endswith(')')
    s = s.strip('()').replace('\u2212','-').replace('\u2013','-').replace('\u2014','-')
    s = CURRENCY_RE.sub('', s)
    s = SPACE_RE.sub('', s)
    # Handle common Turkish/European accounting formats robustly.
    if ',' in s and '.' in s:
        last_comma = s.rfind(','); last_dot = s.rfind('.')
        if last_comma > last_dot:
            # 1.234.567,89
            s = s.replace('.', '').replace(',', '.')
        else:
            # 1,234,567.89
            s = s.replace(',', '')
    elif ',' in s:
        parts = s.split(',')
        if len(parts) > 2:
            s = ''.join(parts)
        elif len(parts) == 2 and len(parts[1]) in (1,2):
            s = s.replace(',', '.')
        else:
            s = s.replace(',', '')
    elif s.count('.') > 1:
        parts=s.split('.')
        if len(parts[-1]) in (1,2):
            s=''.join(parts[:-1])+'.'+parts[-1]
        else:
            s=''.join(parts)
    try:
        x=float(s)
    except Exception:
        return None
    if neg:
        x=-abs(x)
    return x

def to_numeric_series(series: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        return pd.to_numeric(series, errors='coerce').fillna(0.0)
    return series.map(lambda x: parse_number(x) if parse_number(x) is not None else 0.0).astype(float)
