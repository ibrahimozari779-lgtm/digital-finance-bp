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
                    text += ' ' + str(name).lower() + ' ' + ' '.join(str(x).lower() for x in df.iloc[:5].fillna('').values.ravel())
        except Exception:
            pass
    years = [int(y) for y in re.findall(r'(?<!\d)(20\d{2})(?!\d)', text)]
    year = years[-1] if years else None
    # Exact dates first.
    dates = re.findall(r'(?:31[./-]12|30[./-]06|30[./-]09|31[./-]03)[./-](20\d{2})', text)
    if dates:
        y = int(dates[-1]);
        if '31.12' in text or '31/12' in text or '31-12' in text:
            return {'available': True, 'period_type':'annual', 'period_start':f'{y}-01-01', 'period_end':f'{y}-12-31', 'period_days':365 + (1 if y%4==0 and (y%100!=0 or y%400==0) else 0), 'label':str(y), 'confidence':'high'}
    for mname, m in MONTHS.items():
        if mname in text and year:
            # month-only labels are a point-in-time statement; use month days for flow metrics only if explicitly monthly.
            import calendar
            days=calendar.monthrange(year,m)[1]
            return {'available': True, 'period_type':'monthly', 'period_start':f'{year}-{m:02d}-01', 'period_end':f'{year}-{m:02d}-{days:02d}', 'period_days':days, 'label':f'{mname.title()} {year}', 'confidence':'medium'}
    if year:
        return {'available': True, 'period_type':'annual', 'period_start':f'{year}-01-01', 'period_end':f'{year}-12-31', 'period_days':365 + (1 if year%4==0 and (year%100!=0 or year%400==0) else 0), 'label':str(year), 'confidence':'medium'}
    return {'available': False, 'period_type':None, 'period_start':None, 'period_end':None, 'period_days':None, 'label':None, 'confidence':'low'}
