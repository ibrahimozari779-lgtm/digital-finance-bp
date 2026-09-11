"""Date handling which stays safe across mixed ERP exports and runtimes."""
from __future__ import annotations
from datetime import datetime
import pandas as pd


def safe_dates(values) -> pd.Series:
    """Parse dates one cell at a time.

    Some pandas builds on newer Python versions can crash in vectorised datetime
    coercion for mixed object arrays. A bad date must be a missing value, never
    a process-level failure during an upload.
    """
    parsed=[]
    for value in values:
        if pd.isna(value) or str(value).strip()=="":
            parsed.append(None); continue
        if isinstance(value, datetime):
            parsed.append(value.replace(tzinfo=None)); continue
        try:
            parsed.append(datetime.fromisoformat(str(value).strip().replace('Z','+00:00')).replace(tzinfo=None))
        except (TypeError, ValueError, OverflowError):
            # Most Turkish ERP exports use day-first literals.
            try:
                parsed.append(datetime.strptime(str(value).strip(), "%d.%m.%Y"))
            except (TypeError, ValueError, OverflowError):
                parsed.append(None)
    return pd.Series(parsed, index=getattr(values, "index", None), dtype=object)
