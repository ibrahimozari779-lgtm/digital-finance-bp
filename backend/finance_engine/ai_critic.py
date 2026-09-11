"""A deterministic guardrail for optional AI narratives."""
from __future__ import annotations
import re
from typing import Any


def critique_ai_response(response: Any, facts: dict[str, Any]) -> dict[str, Any]:
    text=str(response or '')
    known_numbers={str(int(abs(float(v)))) for v in _numbers(facts) if abs(float(v)) >= 1}
    mentioned=re.findall(r'(?<!\w)\d[\d.,]*(?:\s*(?:TL|%|x))?', text)
    unverified=[x for x in mentioned if x.replace('.','').replace(',','').split()[0].isdigit() and x.replace('.','').replace(',','').split()[0] not in known_numbers]
    return {'status':'review_required' if unverified else 'passed','checked_claims':len(mentioned),'unverified_numeric_claims':unverified[:20],
            'methodology':'AI çıktısındaki sayısal ifadeler, doğrulanmış motor çıktılarındaki sayılarla kaba eşleştirmeden geçirilir. Eşleşmeyen ifade karar kanıtı değildir.'}

def _numbers(value):
    if isinstance(value,dict):
        for v in value.values(): yield from _numbers(v)
    elif isinstance(value,list):
        for v in value: yield from _numbers(v)
    elif isinstance(value,(int,float)) and not isinstance(value,bool): yield value
