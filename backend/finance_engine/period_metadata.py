from __future__ import annotations
import re
from datetime import date
from typing import Any

MONTHS = {
    'ocak':1,'subat':2,'şubat':2,'mart':3,'nisan':4,'mayis':5,'mayıs':5,'haziran':6,
    'temmuz':7,'agustos':8,'ağustos':8,'eylul':9,'eylül':9,'ekim':10,'kasim':11,'kasım':11,'aralik':12,'aralık':12,
}

def infer_period(filename: str, sheets: dict[str, Any] | None = None) -> dict[str, Any]:
    text = filename.lower()
    if sheets:
        try:
            for name, df in sheets.items():
                if df is not None and not df.empty:
                    tokens = [str(x).lower() for x in df.iloc[:5].to_numpy().ravel() if x is not None and not (isinstance(x, float) and x != x)]
                    text += ' ' + str(name).lower() + ' ' + ' '.join(tokens)
        except Exception:
            pass
    # 1. Exact dates (delimited like 31.12.2024 or 31/12/2025)
    exact_match = re.search(r'\b(0[1-9]|[12]\d|3[01])[-/.](0[1-9]|1[0-2])[-/.](20[12]\d)\b', text)
    if exact_match:
        d_str, m_str, y_str = exact_match.group(1), exact_match.group(2), exact_match.group(3)
        y = int(y_str)
        m = int(m_str)
        d = int(d_str)
        if 2015 <= y <= 2027:
            if m == 12 and d == 31:
                days = 366 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 365
                return {'available': True, 'period_type': 'annual', 'period_start': f'{y}-01-01', 'period_end': f'{y}-12-31', 'period_days': days, 'label': str(y), 'confidence': 'high'}
            elif m == 6 and d == 30:
                return {'available': True, 'period_type': 'semi_annual', 'period_start': f'{y}-01-01', 'period_end': f'{y}-06-30', 'period_days': 181 + (1 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 0), 'label': f'H1 {y}', 'confidence': 'high'}
            elif m == 9 and d == 30:
                return {'available': True, 'period_type': 'nine_months', 'period_start': f'{y}-01-01', 'period_end': f'{y}-09-30', 'period_days': 273 + (1 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 0), 'label': f'9M {y}', 'confidence': 'high'}
            elif m == 3 and d == 31:
                return {'available': True, 'period_type': 'quarterly', 'period_start': f'{y}-01-01', 'period_end': f'{y}-03-31', 'period_days': 90 + (1 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 0), 'label': f'Q1 {y}', 'confidence': 'high'}

    # 2. Year from filename or text (strictly 2015-2027 with word boundaries)
    fname_years = [int(y) for y in re.findall(r'\b(20[12]\d)\b', filename.lower()) if 2015 <= int(y) <= 2027]
    text_years = [int(y) for y in re.findall(r'\b(20[12]\d)\b', text) if 2015 <= int(y) <= 2027]
    year = fname_years[-1] if fname_years else (text_years[-1] if text_years else None)

    # Delimited dates fallback
    dates = re.findall(r'\b(?:31[./-]12|30[./-]06|30[./-]09|31[./-]03)[./-](20[12]\d)\b', text)
    if dates:
        y = int(dates[-1])
        if 2015 <= y <= 2027:
            if '31.12' in text or '31/12' in text or '31-12' in text:
                return {'available': True, 'period_type': 'annual', 'period_start': f'{y}-01-01', 'period_end': f'{y}-12-31', 'period_days': 365 + (1 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 0), 'label': str(y), 'confidence': 'high'}

    for mname, m in MONTHS.items():
        if mname in text and year:
            import calendar
            days = calendar.monthrange(year, m)[1]
            return {'available': True, 'period_type': 'monthly', 'period_start': f'{year}-{m:02d}-01', 'period_end': f'{year}-{m:02d}-{days:02d}', 'period_days': days, 'label': f'{mname.title()} {year}', 'confidence': 'medium'}

    if year:
        return {'available': True, 'period_type': 'annual', 'period_start': f'{year}-01-01', 'period_end': f'{year}-12-31', 'period_days': 365 + (1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0), 'label': str(year), 'confidence': 'medium'}

    # If still not found, check if filename implies current period
    if any(w in filename.lower() for w in ['cur', 'cari', 'donem2', 'dönem2', 'current']):
        return {'available': True, 'period_type': 'annual', 'period_start': '2025-01-01', 'period_end': '2025-12-31', 'period_days': 365, 'label': '2025', 'confidence': 'medium'}
    if any(w in filename.lower() for w in ['prior', 'onceki', 'önceki', 'donem1', 'dönem1']):
        return {'available': True, 'period_type': 'annual', 'period_start': '2024-01-01', 'period_end': '2024-12-31', 'period_days': 365, 'label': '2024', 'confidence': 'medium'}

    return {'available': False, 'period_type':None, 'period_start':None, 'period_end':None, 'period_days':None, 'label':None, 'confidence':'low'}
