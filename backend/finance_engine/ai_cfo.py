from __future__ import annotations
import json, os, re, time, urllib.request, urllib.error
from pathlib import Path
from typing import Any
from .ai_critic import critique_ai_response

# Guarantee dotenv loading if invoked standalone or from different directories
try:
    from dotenv import load_dotenv
    load_dotenv()
    load_dotenv(Path(__file__).resolve().parent.parent / '.env')
    load_dotenv(Path(__file__).resolve().parent.parent.parent / '.env')
except ImportError:
    pass

SYSTEM='''You are a senior CFO / Finance Business Partner. Use ONLY the verified financial facts supplied in the JSON. Never invent figures, dates, customers, causes or benchmarks. Distinguish FACT from INFERENCE. If evidence is insufficient, say so. Explain financial implications in plain Turkish. Give management actions tied to measurable KPIs. Do not perform independent accounting calculations when a verified value is supplied.'''

def _clean_json_text(text: str) -> str:
    text = text.strip()
    if text.startswith('```'):
        text = re.sub(r'^```(?:json)?\s*', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\s*```$', '', text)
    return text.strip()

def _payload(analysis:dict[str,Any])->dict[str,Any]:
    bp=analysis.get('business_partner',analysis)
    return {'health_score':bp.get('health_score'),'health_label':bp.get('health_label'),'derived_metrics':bp.get('derived_metrics'),'findings':bp.get('findings',[])[:8],'opportunities':bp.get('opportunities',[])[:6],'risk_ranking':bp.get('risk_ranking_engine',{}).get('ranked_risks',[])[:6],'ccc':bp.get('cash_conversion_cycle'),'profit_quality':bp.get('profit_quality_engine'),'actions':bp.get('management_actions',[])[:8],'validation':analysis.get('calculation_audit')}

def _execute_gemini_request(model: str, key: str, prompt: str, retries: int = 1) -> tuple[dict[str, Any] | None, str | None]:
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent'
    body = json.dumps({
        'contents': [{'parts': [{'text': prompt}]}],
        'generationConfig': {'responseMimeType': 'application/json'}
    }).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=body,
        headers={'Content-Type': 'application/json', 'x-goog-api-key': key},
        method='POST'
    )
    last_err = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.loads(r.read().decode('utf-8'))
            candidates = data.get('candidates', [])
            if not candidates:
                feedback = data.get('promptFeedback', {})
                return None, f"Gemini yanıt üretmedi (Filtre/Geri bildirim: {feedback})"
            first_candidate = candidates[0]
            content = first_candidate.get('content', {})
            parts = content.get('parts', [])
            if not parts or 'text' not in parts[0]:
                finish_reason = first_candidate.get('finishReason', 'UNKNOWN')
                return None, f"Model boş yanıt döndü (Bitiş nedeni: {finish_reason})"
            raw_text = parts[0]['text']
            cleaned = _clean_json_text(raw_text)
            parsed = json.loads(cleaned)
            return parsed, None
        except urllib.error.HTTPError as exc:
            detail = ''
            try:
                detail = exc.read().decode('utf-8', 'replace')[:1000]
            except Exception:
                pass
            last_err = f"HTTP {exc.code}: {detail or exc.reason}"
            # If 503 (high demand) or 429 (rate limit), wait briefly and retry once
            if exc.code in (503, 429) and attempt < retries:
                time.sleep(1.5)
                continue
            return None, last_err
        except json.JSONDecodeError as exc:
            return None, f"JSON ayrıştırma hatası: {exc}"
        except Exception as exc:
            last_err = f"{type(exc).__name__}: {exc}"
            if attempt < retries:
                time.sleep(1.0)
                continue
            return None, last_err
    return None, last_err

def build_ai_cfo_response(analysis:dict[str,Any], user_instruction:str|None=None)->dict[str,Any]:
    key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
    model = os.getenv('GEMINI_MODEL', 'gemini-3.6-flash')
    facts = _payload(analysis)
    if isinstance(analysis, dict) and analysis.get('data_hub'):
        facts['data_hub'] = analysis['data_hub']
    if not key:
        return {
            'available': False,
            'provider': 'gemini',
            'model': model,
            'reason': 'GEMINI_API_KEY (veya GOOGLE_API_KEY) tanımlı değil. Lütfen proje dizinindeki .env dosyasına API anahtarınızı ekleyin.',
            'facts_used': facts
        }
    if user_instruction and user_instruction.strip():
        task = f"Kullanıcı Özel Sorusu / Stratejik Talimat: '{user_instruction.strip()}'\nDoğrulanmış verileri temel alarak bu soruya bir Kıdemli CFO olarak derinlemesine, somut ve doğrudan yanıt ver. Gerekirse ilgili risk ve aksiyonları da belirt."
    else:
        task = 'Yönetim için 5 maddelik CFO özeti, en kritik 3 risk, 3 aksiyon ve 3 yönetim sorusu üret.'

    prompt = (SYSTEM + '\n\nVerified data:\n' + json.dumps(facts, ensure_ascii=False, default=str) +
              '\n\nTask:\n' + task +
              '\nReturn valid JSON with keys: executive_message, key_risks, actions, management_questions, limitations.')

    # Preferred model with 1 retry
    parsed, err = _execute_gemini_request(model, key, prompt, retries=1)

    # If preferred model failed due to high demand (503), rate limit (429), not found (404), timeout, or server error
    if err and any(sig in err for sig in ['HTTP 503', 'HTTP 429', 'HTTP 404', 'HTTP 500', 'HTTP 502', 'NOT_FOUND', 'UNAVAILABLE', 'TimeoutError', 'URLError']):

        fallback_candidates = ['gemini-2.5-flash-lite', 'gemini-2.5-flash', 'gemini-1.5-flash-latest', 'gemini-1.5-flash', 'gemini-2.5-pro', 'gemini-1.5-pro']
        for fallback_model in fallback_candidates:
            if fallback_model == model:
                continue
            f_parsed, f_err = _execute_gemini_request(fallback_model, key, prompt, retries=0)
            if f_parsed is not None:
                return {
                    'available': True,
                    'provider': 'gemini',
                    'model': fallback_model,
                    'fallback_used': True,
                    'note': f"'{model}' yoğunluk nedeniyle yanıt vermedi, otomatik olarak '{fallback_model}' kullanıldı.",
                    'response': f_parsed,
                    'facts_used': facts,
                    'critic': critique_ai_response(f_parsed, facts)
                }

    if parsed is not None:
        return {
            'available': True,
            'provider': 'gemini',
            'model': model,
            'response': parsed,
            'facts_used': facts,
            'critic': critique_ai_response(parsed, facts)
        }
    return {
        'available': False,
        'provider': 'gemini',
        'model': model,
        'reason': f"AI servisi hatası: {err}",
        'facts_used': facts
    }
