from __future__ import annotations
import math
import re
from typing import Any
import pandas as pd

CURRENCY_RE = re.compile(r"[₺$€£¥₹]|TL|TRY|USD|EUR|GBP|CHF", re.I)
PERCENT_RE = re.compile(r"[%％]")
SPACE_RE = re.compile(r"[\s\u00a0\u2000-\u200b\u202f\u205f\u3000]+")

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
    # Handle negative parenthetical notation: (123.45) or ( 123,45 )
    neg = False
    if s.startswith('(') and s.endswith(')'):
        neg = True
        s = s[1:-1].strip()
    elif s.startswith('-') or s.startswith('\u2212') or s.startswith('\u2013') or s.startswith('\u2014'):
        neg = True
        s = s[1:].strip()
    elif s.endswith('-'):
        neg = True
        s = s[:-1].strip()

    s = CURRENCY_RE.sub('', s)
    s = PERCENT_RE.sub('', s)
    s = SPACE_RE.sub('', s)

    if not s:
        return None

    # Handle common Turkish/European and US accounting formats robustly:
    # Case 1: Both comma and dot present
    if ',' in s and '.' in s:
        last_comma = s.rfind(',')
        last_dot = s.rfind('.')
        if last_comma > last_dot:
            # 1.234.567,89 -> Turkish / European format
            s = s.replace('.', '').replace(',', '.')
        else:
            # 1,234,567.89 -> US format
            s = s.replace(',', '')
    # Case 2: Only comma present
    elif ',' in s:
        parts = s.split(',')
        if len(parts) > 2:
            # 1,234,567 (thousands separator)
            s = ''.join(parts)
        elif len(parts) == 2:
            # If 3 digits after comma, could be thousand (e.g. 1,000) or decimal (e.g. 0,125)
            # If preceding part has more than 3 digits (e.g. 1234,50 or 1234,500) -> comma is decimal!
            # If part before is 1-3 digits and after is exactly 3 digits (e.g. 100,000) -> thousand sep
            if len(parts[1]) in (1, 2) or (len(parts[0]) > 3 and len(parts[1]) <= 4) or len(parts[0]) == 0:
                s = s.replace(',', '.')
            elif len(parts[1]) == 3 and len(parts[0]) <= 3:
                # Ambiguous: could be 1,000 (thousand) or 1,250 (decimal).
                # In standard Turkish accounting, thousand sep is '.', so single comma with 3 digits is usually thousand or decimal.
                # If parsed as decimal: 1.250 vs 1000. For safety with 3 digits, replace with dot if leading is 0 (0,123)
                if parts[0] in ('0', '-0', ''):
                    s = s.replace(',', '.')
                else:
                    # In Turkish ERPs, 1.250 is thousand, 1,25 is decimal. But in US, 1,250 is thousand.
                    # Default: treat comma with 3 digits as decimal if followed by calculation, or decimal
                    s = s.replace(',', '.')
            else:
                s = s.replace(',', '.')
        else:
            s = s.replace(',', '')
    # Case 3: Multiple dots present
    elif s.count('.') > 1:
        parts = s.split('.')
        if len(parts[-1]) in (1, 2, 3, 4):
            s = ''.join(parts[:-1]) + '.' + parts[-1]
        else:
            s = ''.join(parts)

    try:
        x = float(s)
    except Exception:
        return None
    if neg:
        x = -abs(x)
    return x

def to_numeric_series(series: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        return pd.to_numeric(series, errors='coerce').fillna(0.0)
    return series.map(lambda x: parse_number(x) if parse_number(x) is not None else 0.0).astype(float)

