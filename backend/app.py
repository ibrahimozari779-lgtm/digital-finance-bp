from __future__ import annotations

import io
import os
import re
from typing import Any

import pandas as pd

# Load a local .env file (if present) into environment variables before
# anything reads os.getenv(...) — this is what lets GEMINI_API_KEY be set
# once in a file instead of exported in every terminal session.
try:
    from dotenv import load_dotenv
    from pathlib import Path
    _b_env = Path(__file__).resolve().parent / '.env'
    if _b_env.is_file():
        load_dotenv(_b_env)
    _r_env = Path(__file__).resolve().parent.parent / '.env'
    if _r_env.is_file():
        load_dotenv(_r_env)
except Exception:
    pass

from fastapi import FastAPI, File, Form, HTTPException, UploadFile, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, Response
from finance_engine import (
    build_finance_business_partner_analysis,
    SECTOR_BANDS,
    process_ingestion_payload,
    validate_api_key,
    generate_mock_erp_payload,
)
from finance_engine.period_metadata import infer_period
from finance_engine.data_quality_engine import build_data_quality_report, apply_cross_source_reconciliation
from finance_engine.ai_cfo import build_ai_cfo_response
from finance_engine.headerless_table_detector import infer_headerless_financial_table
from finance_engine.multi_source_intelligence import build_multi_source_intelligence
from finance_engine.multi_source_ingestion import _read_one
from finance_engine.data_classifier import classify_dataframe
from finance_engine.numeric_utils import to_numeric_series
from finance_engine.erp_standardizer import inspect_file_structure, detect_erp_signature, CANONICAL_SCHEMAS

APP_VERSION = "3.13.0"

app = FastAPI(title="Digital Finance Business Partner", version=APP_VERSION)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    svg_icon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1D4ED8"/><stop offset="100%" stop-color="#0E7C66"/></linearGradient></defs><rect width="64" height="64" rx="16" fill="url(#g)"/><path d="M16 48 L16 16 L32 16 C42 16 48 22 48 32 C48 42 42 48 32 48 Z" fill="none" stroke="#FFFFFF" stroke-width="5"/><polyline points="20,40 30,30 38,36 48,22" fill="none" stroke="#38BDF8" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="48" cy="22" r="3" fill="#38BDF8"/></svg>'''
    return Response(content=svg_icon, media_type="image/svg+xml")


TDHP_GROUPS = {
    "1": ("Current Assets", "BS_ASSET"),
    "2": ("Non-current Assets", "BS_ASSET"),
    "3": ("Short-term Liabilities", "BS_LIABILITY"),
    "4": ("Long-term Liabilities", "BS_LIABILITY"),
    "5": ("Equity", "BS_EQUITY"),
}

ACCOUNT_BUCKETS = [
    ("600", "Domestic Sales", "REVENUE"), ("601", "Export Sales", "REVENUE"), ("602", "Other Sales", "REVENUE"),
    ("610", "Sales Returns", "CONTRA_REVENUE"), ("611", "Sales Discounts", "CONTRA_REVENUE"), ("612", "Other Sales Deductions", "CONTRA_REVENUE"),
    ("620", "Cost of Sales", "COGS"), ("621", "Cost of Merchandise Sold", "COGS"), ("622", "Cost of Services", "COGS"), ("623", "Cost of Other Sales", "COGS"),
    ("630", "R&D Expenses", "OPEX_RD"), ("631", "Marketing & Sales Expenses", "OPEX_SALES"), ("632", "General & Administrative Expenses", "OPEX_GA"),
    ("640", "Other Operating Income", "OTHER_OPERATING_INCOME"), ("641", "Other Operating Income", "OTHER_OPERATING_INCOME"), ("642", "Interest Income", "OTHER_OPERATING_INCOME"),
    ("643", "Other Operating Income", "OTHER_OPERATING_INCOME"), ("644", "Other Operating Income", "OTHER_OPERATING_INCOME"), ("645", "Other Operating Income", "OTHER_OPERATING_INCOME"), ("646", "FX Gains", "OTHER_OPERATING_INCOME"), ("647", "Other Operating Income", "OTHER_OPERATING_INCOME"), ("649", "Other Operating Income", "OTHER_OPERATING_INCOME"),
    ("650", "Other Operating Expense", "OTHER_OPERATING_EXPENSE"), ("651", "Other Operating Expense", "OTHER_OPERATING_EXPENSE"), ("652", "Other Operating Expense", "OTHER_OPERATING_EXPENSE"), ("653", "Other Operating Expense", "OTHER_OPERATING_EXPENSE"), ("654", "Other Operating Expense", "OTHER_OPERATING_EXPENSE"), ("655", "Other Operating Expense", "OTHER_OPERATING_EXPENSE"), ("656", "FX Losses", "OTHER_OPERATING_EXPENSE"), ("657", "Other Operating Expense", "OTHER_OPERATING_EXPENSE"), ("659", "Other Operating Expense", "OTHER_OPERATING_EXPENSE"),
    ("660", "Finance Costs", "FINANCE"), ("661", "Finance Costs", "FINANCE"), ("662", "Finance Costs", "FINANCE"), ("663", "Finance Costs", "FINANCE"),
    ("670", "Other Non-operating Income", "OTHER_NON_OPERATING_INCOME"), ("671", "Other Non-operating Income", "OTHER_NON_OPERATING_INCOME"), ("679", "Other Non-operating Income", "OTHER_NON_OPERATING_INCOME"),
    ("680", "Other Non-operating Expense", "OTHER_NON_OPERATING_EXPENSE"), ("681", "Other Non-operating Expense", "OTHER_NON_OPERATING_EXPENSE"), ("689", "Other Non-operating Expense", "OTHER_NON_OPERATING_EXPENSE"),
    ("690", "Pre-tax Period Result", "PERIOD_RESULT"), ("691", "Current Tax Expense", "TAX"), ("692", "Net Period Result", "PERIOD_RESULT"),
    ("710", "Direct Material - 7/A", "COST_7A_PRODUCTION"), ("711", "Direct Material Reflection - 7/A", "REFLECTION_7A"),
    ("720", "Direct Labor - 7/A", "COST_7A_PRODUCTION"), ("721", "Direct Labor Reflection - 7/A", "REFLECTION_7A"),
    ("730", "General Manufacturing - 7/A", "COST_7A_PRODUCTION"), ("731", "General Manufacturing Reflection - 7/A", "REFLECTION_7A"),
    ("740", "Service Production Cost - 7/A", "COST_7A_PRODUCTION"), ("741", "Service Production Cost Reflection - 7/A", "REFLECTION_7A"),
    ("750", "R&D Expenses - 7/A", "OPEX_7A_RD"), ("751", "R&D Reflection - 7/A", "REFLECTION_7A"),
    ("760", "Marketing & Sales - 7/A", "OPEX_7A_SALES"), ("761", "Marketing & Sales Reflection - 7/A", "REFLECTION_7A"),
    ("770", "General Administration - 7/A", "OPEX_7A_GA"), ("771", "General Administration Reflection - 7/A", "REFLECTION_7A"),
    ("780", "Finance Costs - 7/A", "FINANCE_7A"), ("781", "Finance Costs Reflection - 7/A", "REFLECTION_7A"),
    ("790", "Finance Costs - 7/B", "FINANCE_7A"), ("791", "Finance Costs Reflection - 7/B", "REFLECTION_7A"),
]

FIELD_ALIASES = {
    "account_code": ["hesap kodu", "hesap no", "hesap numarasi", "hesap numarası", "hesap kod", "account code", "account no", "account number"],
    "account_name": ["hesap adi", "hesap adı", "hesap aciklamasi", "hesap açıklaması", "hesap adi aciklama", "account name", "description", "aciklama", "açıklama"],
    "debit_turnover": ["borc", "borç", "debit", "borc hareket", "borç hareket", "borc toplami", "borç toplamı", "debit turnover"],
    "credit_turnover": ["alacak", "credit", "alacak hareket", "alacak toplami", "alacak toplamı", "credit turnover"],
    "debit_balance": ["borc bakiye", "borç bakiye", "borc bakiyesi", "borç bakiyesi", "donem borc bakiye", "dönem borç bakiye", "debit balance", "debit closing balance"],
    "credit_balance": ["alacak bakiye", "alacak bakiyesi", "donem alacak bakiye", "dönem alacak bakiye", "credit balance", "credit closing balance"],
    "balance": ["net bakiye", "ending balance", "closing balance", "donem sonu bakiye", "dönem sonu bakiye", "bakiye", "balance"],
}
TOTAL_LABELS = {"toplam", "genel toplam", "grand total", "total", "ara toplam", "subtotal", "toplamlar", "bakiye toplam", "borc toplam", "alacak toplam"}


def normalize(text: Any) -> str:
    # BUGFIX: Python's str.lower() turns the Turkish capital dotted "İ" into
    # "i" + a combining dot-above (U+0307) rather than plain ASCII "i" — a
    # two-character sequence. The old code lowercased *before* translating,
    # so by the time the Turkish-character map ran, "İ" no longer existed in
    # the string (it was already "i" + combining dot) and the map never
    # fired. The regex below then stripped that combining dot as a
    # non-alphanumeric character, inserting a stray space in the middle of
    # the word — e.g. "İskonto Tutarı" -> "i skonto tutari" instead of
    # "iskonto tutari". That silently broke alias/keyword matching for every
    # Turkish word starting with İ (İskonto, İstanbul, İşlem, İnşaat,
    # İhracat, ...), which is why columns/sheets/entities using those words
    # were dropped from analysis. Fix: translate Turkish letters (both cases)
    # to ASCII *before* calling .lower(), so combining marks never appear.
    s = str(text).replace("\n", " ").replace("\r", " ").strip()
    s = s.translate(str.maketrans({
        "ı": "i", "İ": "i", "I": "i", "ş": "s", "Ş": "s", "ğ": "g", "Ğ": "g",
        "ü": "u", "Ü": "u", "ö": "o", "Ö": "o", "ç": "c", "Ç": "c",
    }))
    s = s.lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def account_digits(code: Any) -> str:
    if code is None:
        return ""
    s = str(code).strip()
    if re.fullmatch(r"\d+(?:\.\d+)*", s):
        return re.sub(r"\D", "", s)
    return ""


def to_number_scalar(value: Any) -> float | None:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).strip().replace("₺", "").replace("TL", "").replace("TRY", "").replace("€", "")
    s = re.sub(r"\s", "", s)
    neg = s.startswith("(") and s.endswith(")")
    s = s.replace("(", "").replace(")", "")
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        # Turkish decimal unless comma is clearly a thousands separator.
        if s.count(",") == 1 and len(s.split(",")[-1]) <= 2:
            s = s.replace(",", ".")
        else:
            s = s.replace(",", "")
    try:
        x = float(s)
    except Exception:
        return None
    return -x if neg else x


def to_number(series: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        return pd.to_numeric(series, errors="coerce").fillna(0.0)
    return series.map(lambda x: to_number_scalar(x) or 0.0)


def read_workbook_all_sheets(content: bytes, filename: str) -> dict[str, pd.DataFrame]:
    """Read workbook bytes without assuming headers. Supports xlsx/xlsm/xls/csv."""
    try:
        # _read_one applies header/structure discovery and legacy-xls handling consistently.
        return _read_one(content, filename)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Dosya okunamadı: {exc}") from exc


def score_header_row(values: list[Any]) -> int:
    present = {normalize(v) for v in values if pd.notna(v)}
    alias_sets = {k: {normalize(a) for a in vals} for k, vals in FIELD_ALIASES.items()}
    score = 8 if present & alias_sets["account_code"] else 0
    score += 2 if present & alias_sets["account_name"] else 0
    for fld in ("debit_turnover", "credit_turnover", "debit_balance", "credit_balance", "balance"):
        if present & alias_sets[fld]: score += 3
    return score


def detect_standard_header_sheet(sheets: dict[str, pd.DataFrame]) -> tuple[str, int, pd.DataFrame] | None:
    candidates = []
    for sname, raw in sheets.items():
        if raw is None or raw.empty:
            continue
        for ridx in range(min(len(raw), 80)):
            sc = score_header_row(raw.iloc[ridx].tolist())
            if sc >= 8:
                candidates.append((sc, sname, ridx, raw))
    if not candidates:
        return None
    candidates.sort(key=lambda x: (x[0], x[3].iloc[x[2]].notna().sum()), reverse=True)
    _, sname, header_row, raw = candidates[0]
    raw_headers = list(raw.iloc[header_row].tolist())
    headers, seen = [], {}
    for i, v in enumerate(raw_headers):
        base = str(v).strip() if pd.notna(v) else f"Unnamed_{i}"
        base = base or f"Unnamed_{i}"
        count = seen.get(base, 0); seen[base] = count + 1
        headers.append(base if count == 0 else f"{base}_{count}")
    df = raw.iloc[header_row + 1:].copy(); df.columns = headers
    # Preserve the original spreadsheet row number (1-based) for each data row
    # before any filtering/reindexing, so downstream traceability (source_row)
    # survives regardless of source layout (statement-style or standard mizan).
    row_numbers = (df.index + 1).to_series(index=df.index)
    keep_mask = df.notna().any(axis=1)
    df = df[keep_mask].reset_index(drop=True)
    row_numbers = row_numbers[keep_mask].reset_index(drop=True)
    df["_source_row"] = row_numbers
    return sname, header_row + 1, df


def detect_column_by_alias(columns: list[str], field: str) -> tuple[str | None, float]:
    aliases = {normalize(a) for a in FIELD_ALIASES[field]}
    best = (None, 0.0)
    for col in columns:
        nc = normalize(col)
        if nc.startswith("unnamed"): continue
        has_balance_word = any(x in nc for x in ("bakiye", "balance", "closing", "ending"))
        if field in {"debit_turnover", "credit_turnover"} and has_balance_word: continue
        if field in {"debit_balance", "credit_balance"} and not has_balance_word: continue
        if nc in aliases: score = 100.0
        else:
            overlap = max((len(set(nc.split()) & set(a.split())) for a in aliases), default=0)
            score = min(88.0, 50 + overlap * 15) if overlap else 0
        if score > best[1]: best = (col, score)
    return best


def detect_mapping(columns: list[str]) -> dict[str, dict[str, Any]]:
    result = {}
    for field in FIELD_ALIASES:
        col, score = detect_column_by_alias(columns, field)
        if col is not None and score >= 65:
            result[field] = {"source_column": col, "confidence": round(score,1)}
    if "debit_balance" in result or "credit_balance" in result:
        result.pop("balance", None)
    return result


def safe_extract_texts(raw: pd.DataFrame, max_rows: int = 15) -> str:
    """Safely extracts text tokens from first N rows without crashing on datetimes."""
    tokens = []
    sample = raw.iloc[:max_rows]
    for row in sample.itertuples(index=False, name=None):
        for val in row:
            if val is not None and not (isinstance(val, float) and pd.isna(val)):
                s = str(val).strip()
                if s and s != "nan" and s != "NaT":
                    tokens.append(normalize(s))
    return " ".join(tokens)


def is_special_financial_statement_layout(raw: pd.DataFrame, sname: str = "") -> bool:
    # Detect layouts like the uploaded real-world file: title rows, code in a detail column,
    # statement amount in a later column, and English/Turkish statement headers such as B&S vs Sales Data.
    texts = safe_extract_texts(raw, 12)
    ns = normalize(sname)
    tokens = set(ns.split())

    is_bs_name = (
        "bs asset" in ns or "bs assets" in ns
        or "bs liab" in ns or "bs liabilities" in ns
        or "balance sheet" in ns or "bilanco" in ns
        or ("bs" in tokens and any(k in tokens for k in ["asset", "assets", "liab", "liabilities"]))
    )
    is_pl_name = (
        "pl" in tokens or "p l" in ns or "p&l" in ns
        or "income statement" in ns or "gelir tablosu" in ns or "kar zarar" in ns
    )

    is_balance_sheet = is_bs_name or (("balance sheet" in texts or "bilanco" in texts) and (
        "assets" in texts or "aktif" in texts or "liabilities" in texts or "pasif" in texts
        or "kaynaklar" in texts or "b s vs sales data" in texts
    ))
    is_income_statement = is_pl_name or (("income statement" in texts or "gelir tablosu" in texts or "kar zarar" in texts) and (
        "net sales" in texts or "net satislar" in texts or "gross sales" in texts or "brut satislar" in texts
    ))
    return is_balance_sheet or is_income_statement


def detect_special_layout(raw: pd.DataFrame) -> tuple[int, int, int, int] | None:
    """Return (code_col, name_col, amount_col, start_row) for statement-style sheets."""
    nrows, ncols = raw.shape
    code_scores = []
    for c in range(ncols):
        hits = 0; detail_hits = 0
        for r in range(5, min(nrows, 500)):
            v = raw.iat[r,c]
            d = account_digits(v)
            if len(d) == 3 and d not in {"100"}:
                hits += 1
                # Neighbor immediately to the right should usually be a non-numeric account name.
                if c+1 < ncols:
                    nv = raw.iat[r,c+1]
                    if nv is not None and not (isinstance(nv,(int,float)) and not pd.isna(nv)):
                        detail_hits += 1
        code_scores.append((detail_hits, hits, c))
    code_scores.sort(reverse=True)
    if not code_scores or code_scores[0][0] < 8:
        return None
    _, _, code_col = code_scores[0]
    name_col = code_col + 1

    # Find the best statement amount column by numeric density on detailed account rows.
    detail_rows = []
    for r in range(5, min(nrows, 500)):
        if len(account_digits(raw.iat[r, code_col])) == 3:
            detail_rows.append(r)
    if not detail_rows:
        return None
    amount_scores = []
    for c in range(name_col+1, ncols):
        nums = 0; nonzero = 0
        for r in detail_rows:
            val = to_number_scalar(raw.iat[r,c])
            if val is not None:
                nums += 1
                if abs(val) > 1e-12: nonzero += 1
        # Favor a column with meaningful density. In this source the statement amount is F.
        density = nums / len(detail_rows)
        amount_scores.append((density, nonzero / max(1,len(detail_rows)), c))
    amount_scores.sort(reverse=True)
    if not amount_scores or amount_scores[0][0] < 0.10:
        return None
    amount_col = amount_scores[0][2]
    return code_col, name_col, amount_col, min(detail_rows)


def build_special_trial_balance(raw: pd.DataFrame, detected: tuple[int,int,int,int]) -> tuple[pd.DataFrame, dict[str,Any]]:
    code_col, name_col, amount_col, start_row = detected
    records = []
    source_subtotals = {}
    for r in range(5, len(raw)):
        group_code = account_digits(raw.iat[r,1]) if raw.shape[1] > 1 else ""
        if group_code in {"1","2","3","4","5","60","61","62","63","64","65","66","67","68","69"}:
            amt = to_number_scalar(raw.iat[r, amount_col]) if amount_col < raw.shape[1] else None
            if amt is not None:
                nm = "" if raw.shape[1] <= 2 or pd.isna(raw.iat[r,2]) else str(raw.iat[r,2]).strip()
                source_subtotals[group_code] = {"name": nm, "amount": float(amt), "row": r+1}
    for r in range(start_row, len(raw)):
        raw_code = "" if pd.isna(raw.iat[r,code_col]) else str(raw.iat[r,code_col]).strip()
        code = account_digits(raw_code)
        name = "" if pd.isna(raw.iat[r,name_col]) else str(raw.iat[r,name_col]).strip()
        # Real-world layouts may render 690/692 as "690.DÖNEM..." in the code cell.
        if len(code) != 3:
            m = re.match(r"\s*(\d{3})\s*\.", raw_code)
            if m:
                code = m.group(1)
            else:
                m = re.match(r"\s*(69[012])\s*\.", name)
                if m:
                    code = m.group(1)
                else:
                    continue
        amount = to_number_scalar(raw.iat[r,amount_col]) or 0.0
        # Statement-style sources generally show liabilities/equity as positive presentation values,
        # while our internal model uses signed balances (assets +, liabilities/equity -).
        # P&L rows retain their source sign because income/expense presentation already carries +/- semantics.
        first_digit = code[0]
        code3 = int(code)
        # Canonical internal sign convention:
        # assets positive; liabilities/equity negative; P&L income negative and expense positive.
        if first_digit in {"3", "4"}:
            internal_balance = -abs(amount)
        elif first_digit == "5":
            # Equity is presented with its natural sign in this source layout; invert to canonical sign.
            internal_balance = -amount
        elif code3 in {600,601,602,640,641,642,643,644,645,646,647,649,670,671,679}:
            internal_balance = -abs(amount)
        elif code3 in {610,611,612,620,621,622,623,630,631,632,650,651,652,653,654,655,656,657,659,660,661,662,663,680,681,689,691}:
            internal_balance = abs(amount)
        elif code3 in {690,692}:
            internal_balance = -abs(amount)
        elif first_digit == "7":
            internal_balance = abs(amount)
        else:
            internal_balance = amount
        records.append({
            "account_code": code,
            "account_name": name,
            "balance": internal_balance,
            "debit_balance": max(internal_balance,0),
            "credit_balance": max(-internal_balance,0),
            "debit_turnover": 0.0,
            "credit_turnover": 0.0,
            "source_amount": amount,
            "source_row": r+1,
        })
    tb = pd.DataFrame(records)
    if tb.empty:
        raise HTTPException(status_code=422, detail="Finansal tablo yapısından hesap satırları çıkarılamadı.")
    tb[["account_group", "statement_bucket"]] = pd.DataFrame(tb["account_code"].map(account_class).tolist(), index=tb.index)
    # Capture explicit reconciliation columns when the source provides them (e.g.
    # "B&S vs Sales Data" and "Difference"). Non-zero differences are data-quality
    # findings, not reasons to alter the accounting totals.
    reconciliation_findings = []
    header_window = raw.iloc[:12]
    diff_cols = []
    for c in range(raw.shape[1]):
        labels = [normalize(x) for x in header_window.iloc[:, c].tolist() if pd.notna(x)]
        if any("difference" in x or "fark" in x or "reconcil" in x for x in labels):
            diff_cols.append(c)
    for r in range(start_row, len(raw)):
        code = account_digits(raw.iat[r, code_col])
        if len(code) == 3:
            for c in diff_cols:
                val = to_number_scalar(raw.iat[r,c])
                if val is not None and abs(val) >= 0.01:
                    reconciliation_findings.append({"account_code":code,"account_name":("" if pd.isna(raw.iat[r,name_col]) else str(raw.iat[r,name_col]).strip()),"difference":float(val),"row":r+1,"column":c+1})
    tb.attrs["source_controls"] = {"subtotals": source_subtotals, "reconciliation_findings": reconciliation_findings}
    meta = {
        "mode": "statement_layout",
        "code_column": f"Column {code_col + 1}",
        "name_column": f"Column {name_col + 1}",
        "amount_column": f"Column {amount_col + 1}",
        "detail_start_row": start_row + 1,
    }
    return tb, meta


def is_total_or_header_row(code: str, name: str) -> bool:
    c = account_digits(code); n = normalize(name)
    if not c: return True
    if len(c) == 3: return False
    return True


def account_class(code: str) -> tuple[str,str]:
    digits = account_digits(code)
    if not digits: return "Unmapped", "UNMAPPED"
    for prefix, label, bucket in sorted(ACCOUNT_BUCKETS, key=lambda x: len(x[0]), reverse=True):
        if digits.startswith(prefix): return label, bucket
    return TDHP_GROUPS.get(digits[:1], ("Unmapped", "UNMAPPED"))


def prepare_trial_balance(df: pd.DataFrame, mapping: dict[str,dict[str,Any]]) -> tuple[pd.DataFrame,str]:
    if "account_code" not in mapping:
        raise HTTPException(status_code=422, detail="Mizan için Hesap Kodu alanı bulunamadı.")
    work = pd.DataFrame(index=df.index)
    work["account_code"] = df[mapping["account_code"]["source_column"]].astype(str).str.strip()
    work["account_name"] = df[mapping["account_name"]["source_column"]].fillna("").astype(str).str.strip() if "account_name" in mapping else ""
    work["source_row"] = df["_source_row"] if "_source_row" in df.columns else (df.index + 1)
    work["debit_turnover"] = to_number(df[mapping["debit_turnover"]["source_column"]]) if "debit_turnover" in mapping else 0.0
    work["credit_turnover"] = to_number(df[mapping["credit_turnover"]["source_column"]]) if "credit_turnover" in mapping else 0.0
    if "debit_balance" in mapping or "credit_balance" in mapping:
        work["debit_balance"] = to_number(df[mapping["debit_balance"]["source_column"]]) if "debit_balance" in mapping else 0.0
        work["credit_balance"] = to_number(df[mapping["credit_balance"]["source_column"]]) if "credit_balance" in mapping else 0.0
        work["balance"] = work["debit_balance"] - work["credit_balance"]
        source = "debit_balance-credit_balance"
    elif "balance" in mapping:
        work["balance"] = to_number(df[mapping["balance"]["source_column"]])
        work["debit_balance"] = work.balance.clip(lower=0); work["credit_balance"] = (-work.balance).clip(lower=0)
        source = "net_balance"
    elif "debit_turnover" in mapping or "credit_turnover" in mapping:
        work["balance"] = work["debit_turnover"] - work["credit_turnover"]
        work["debit_balance"] = work.balance.clip(lower=0); work["credit_balance"] = (-work.balance).clip(lower=0)
        source = "debit_turnover-credit_turnover"
    else:
        raise HTTPException(status_code=422, detail="Mizan bakiyesi/borç-alacak alanı bulunamadı.")
    work = work[work["account_code"].map(account_digits).str.len() >= 3].copy().reset_index(drop=True)
    work["account_code"] = work["account_code"].map(account_digits)
    work["account_group"], work["statement_bucket"] = zip(*work["account_code"].map(account_class))
    return work, source


def amount(tb: pd.DataFrame,bucket:str,positive_side:str="debit") -> float:
    subset=tb.loc[tb.statement_bucket==bucket,"balance"]
    return float((-subset).clip(lower=0).sum()) if positive_side=="credit" else float(subset.clip(lower=0).sum())


def prefix_balance(tb:pd.DataFrame,prefixes:tuple[str,...])->float:
    codes=tb.account_code.astype(str)
    return float(tb.loc[codes.str.startswith(prefixes),"balance"].sum())


def canonicalize_transactions(tb: pd.DataFrame) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    """Create a single canonical account-level model and flag conflicting duplicate accounts.

    Multiple sheets/files can present the same account. Exact duplicates are kept once;
    conflicting values are not silently summed and are reported for review.
    """
    work = tb.copy()
    findings = []
    if "source_sheet" not in work.columns:
        work["source_sheet"] = "source"
    dup_groups = work.groupby("account_code", dropna=False)
    keep_rows=[]
    for code, grp in dup_groups:
        balances = [round(float(x), 2) for x in grp["balance"].tolist()]
        unique_bal = sorted(set(balances))
        if len(unique_bal) == 1:
            # Same account repeated on multiple sheets with the same value: one canonical line.
            keep_rows.append(grp.iloc[0])
            if len(grp) > 1:
                findings.append({"type":"duplicate_same_value","account_code":str(code),"copies":len(grp),"difference":0.0})
        else:
            # Conflicting representations: keep the source with the strongest role when possible,
            # otherwise keep the first, but surface the conflict.
            priority={"profit_and_loss":3,"liabilities_equity":2,"assets":1}
            idx=max(grp.index, key=lambda i: priority.get(str(grp.loc[i].get("source_role","")),0))
            keep_rows.append(grp.loc[idx])
            findings.append({"type":"duplicate_conflict","account_code":str(code),"copies":len(grp),"values":unique_bal})
    canonical=pd.DataFrame(keep_rows).reset_index(drop=True)
    return canonical, findings

def aggregate_statements(tb:pd.DataFrame)->dict[str,Any]:
    codes=tb.account_code.astype(str)
    current_assets=float(tb.loc[codes.str.startswith("1"),"balance"].sum())
    noncurrent_assets=float(tb.loc[codes.str.startswith("2"),"balance"].sum())
    total_assets=current_assets+noncurrent_assets
    current_liabilities=float((-tb.loc[codes.str.startswith("3"),"balance"]).sum())
    long_term_liabilities=float((-tb.loc[codes.str.startswith("4"),"balance"]).sum())
    total_liabilities=current_liabilities+long_term_liabilities

    # Equity uses the source account signs. 590/591 are presentation/result accounts
    # and are excluded from equity-before-current-result.
    equity_before_result=float(
        (-tb.loc[codes.str.startswith("5"),"balance"]).sum()
        - (-tb.loc[codes.str.startswith(("590","591")),"balance"]).sum()
    )

    revenue=amount(tb,"REVENUE","credit")
    contra=amount(tb,"CONTRA_REVENUE","debit")
    net_sales=revenue-contra
    cogs=amount(tb,"COGS","debit")
    opex=amount(tb,"OPEX_RD","debit")+amount(tb,"OPEX_SALES","debit")+amount(tb,"OPEX_GA","debit")
    if opex<=0.01:
        opex=amount(tb,"OPEX_7A_RD","debit")+amount(tb,"OPEX_7A_SALES","debit")+amount(tb,"OPEX_7A_GA","debit")
    finance=amount(tb,"FINANCE","debit")
    if finance<=0.01:
        finance=amount(tb,"FINANCE_7A","debit")

    other_operating_income=amount(tb,"OTHER_OPERATING_INCOME","credit")
    other_non_operating_income=amount(tb,"OTHER_NON_OPERATING_INCOME","credit")
    other_operating_expense=amount(tb,"OTHER_OPERATING_EXPENSE","debit")
    other_non_operating_expense=amount(tb,"OTHER_NON_OPERATING_EXPENSE","debit")
    other_income=other_operating_income+other_non_operating_income
    other_expense=other_operating_expense+other_non_operating_expense
    tax=amount(tb,"TAX","debit")

    gross_profit=net_sales-cogs
    operating_profit=gross_profit-opex
    operating_result_after_other=operating_profit+other_operating_income-other_operating_expense
    pre_tax=operating_result_after_other+other_non_operating_income-other_non_operating_expense-finance
    net_profit=pre_tax-tax

    posted_690=float((-tb.loc[codes.str.startswith("690"),"balance"]).sum())
    posted_691=float(amount(tb,"TAX","debit"))
    posted_692=float((-tb.loc[codes.str.startswith("692"),"balance"]).sum())
    result_control={
        "posted_690":posted_690,
        "computed_pre_tax_profit":pre_tax,
        "pre_tax_difference":pre_tax-posted_690 if posted_690 else None,
        "posted_691":posted_691,
        "computed_tax":tax,
        "tax_difference":tax-posted_691 if posted_691 else None,
        "posted_692":posted_692,
        "computed_net_profit":net_profit,
        "net_profit_difference":net_profit-posted_692 if posted_692 else None,
    }

    current_period_result=net_profit
    total_equity=equity_before_result+current_period_result
    bs_difference=total_assets-(total_liabilities+total_equity)

    cash=prefix_balance(tb,("100","101","102","108"))
    receivables=prefix_balance(tb,("120","121","122"))
    inventory=prefix_balance(tb,("150","151","152","153","157","158"))
    payables=-prefix_balance(tb,("320","321","322","326","329"))
    debt=-prefix_balance(tb,("300","301","302","303","304","305","306","307","308","309","400","401","402","403","404","405","406","407","408","409"))
    net_debt=debt-cash

    kpis={
        "gross_margin_pct":gross_profit/net_sales*100 if net_sales else None,
        "operating_margin_pct":operating_profit/net_sales*100 if net_sales else None,
        "net_margin_pct":net_profit/net_sales*100 if net_sales else None,
        "current_ratio":current_assets/current_liabilities if current_liabilities else None,
        "quick_ratio":(current_assets-inventory)/current_liabilities if current_liabilities else None,
        "cash_ratio":cash/current_liabilities if current_liabilities else None,
        "debt_to_equity":debt/total_equity if total_equity else None,
        "net_debt":net_debt,"cash":cash,"receivables":receivables,"inventory":inventory,"payables":payables,"financial_debt":debt,
        "return_on_equity_pct":net_profit/equity_before_result*100 if equity_before_result else None,
        "return_on_assets_pct":net_profit/total_assets*100 if total_assets else None,
        "asset_turnover":net_sales/total_assets if total_assets else None,
    }

    source_controls=getattr(tb,"attrs",{}).get("source_controls",{}) if hasattr(tb,"attrs") else {}
    return {
        "profit_and_loss":{
            "Revenue":revenue,"Sales deductions":contra,"Net sales":net_sales,"COGS":cogs,"Gross profit":gross_profit,
            "Operating expenses":opex,"Operating profit":operating_profit,
            "Other operating income":other_operating_income,"Other operating expense":other_operating_expense,
            "Other non-operating income":other_non_operating_income,"Other non-operating expense":other_non_operating_expense,
            "Other income":other_income,"Other expense":other_expense,
            "Finance costs":finance,"Pre-tax profit":pre_tax,"Tax expense":tax,"Net profit":net_profit,
        },
        "balance_sheet":{
            "Current assets":current_assets,"Non-current assets":noncurrent_assets,"Total assets":total_assets,
            "Current liabilities":current_liabilities,"Long-term liabilities":long_term_liabilities,"Total liabilities":total_liabilities,
            "Equity before current result":equity_before_result,"Current period profit/loss":current_period_result,
            "Total equity incl. current result":total_equity,"Total liabilities & equity":total_liabilities+total_equity,"Balance check difference":bs_difference,
        },
        "kpis":kpis,
        "controls":{"result_control":result_control,"source_controls":source_controls},
    }


def quality_checks(source_df:pd.DataFrame,mapping:dict[str,Any],tb:pd.DataFrame,meta:dict[str,Any],statements:dict[str,Any])->dict[str,Any]:
    controls=statements["controls"]["result_control"]
    checks=[]
    checks.append({"name":"Rows loaded","status":"passed" if len(tb) else "failed","value":int(len(tb)),"display_type":"count"})
    checks.append({"name":"Workbook sheet classification","status":"passed" if meta.get("sheets") else "failed","value":len(meta.get("sheets",[])),"display_type":"count"})
    checks.append({"name":"Account code detection","status":"passed" if len(tb) else "failed","value":int(tb.account_code.nunique()),"display_type":"count"})

    if meta.get("mode") == "standard_mizan":
        balance_diff=float(tb.debit_balance.sum()-tb.credit_balance.sum())
        checks.append({"name":"Closing balance control","status":"passed" if abs(balance_diff)<0.01 else "warning","value":round(balance_diff,2),"display_type":"currency"})
    else:
        bs_diff=float(statements["balance_sheet"]["Balance check difference"])
        checks.append({"name":"Statement balance equation","status":"passed" if abs(bs_diff)<0.01 else "warning","value":round(bs_diff,2),"display_type":"currency"})

    unmapped=int((tb.statement_bucket=="UNMAPPED").sum())
    checks.append({"name":"Recognized accounts","status":"passed" if unmapped==0 else "warning","value":int(len(tb)-unmapped),"display_type":"count"})
    if unmapped:
        checks.append({"name":"Unmapped accounts","status":"warning","value":unmapped,"display_type":"count"})

    for name,key in [("690 vs calculated PBT","pre_tax_difference"),("691 vs calculated tax","tax_difference"),("692 vs calculated net profit","net_profit_difference")]:
        val=controls.get(key)
        checks.append({"name":name,"status":"passed" if val is None or abs(val)<0.01 else "warning","value":None if val is None else round(val,2),"display_type":"currency"})

    source_meta=statements["controls"].get("source_controls",{})
    source_subtotals=source_meta.get("subtotals",{})
    source_recons=source_meta.get("reconciliation_findings",[])
    if not source_recons and isinstance(meta,dict):
        source_recons=meta.get("reconciliation_findings",[])

    if source_recons:
        total_abs=sum(abs(x["difference"]) for x in source_recons)
        checks.append({"name":"Source reconciliation findings","status":"warning","value":len(source_recons),"display_type":"count"})
        checks.append({"name":"Source reconciliation difference (absolute total)","status":"warning","value":round(total_abs,2),"display_type":"currency"})
    else:
        checks.append({"name":"Source reconciliation findings","status":"passed","value":0,"display_type":"count"})
    pl=statements["profit_and_loss"]
    # P&L subtotal checks: compare the source's signed presentation amount with detail-derived amounts.
    calc_map={
        "60":pl["Revenue"],
        "61":-pl["Sales deductions"],
        "62":-pl["COGS"],
        "63":-pl["Operating expenses"],
        "64":pl["Other operating income"],
        "65":-pl["Other operating expense"],
        "66":-pl["Finance costs"],
        "67":pl["Other non-operating income"],
        "68":-pl["Other non-operating expense"],
        "69":pl["Pre-tax profit"],
    }
    for code,calc in calc_map.items():
        if code in source_subtotals:
            src=float(source_subtotals[code]["amount"])
            diff=src-float(calc)
            checks.append({"name":f"{code} subtotal vs detail","status":"passed" if abs(diff)<0.01 else "warning","value":round(diff,2),"display_type":"currency"})

    # Source balance-sheet group controls. For the statement-layout source,
    # group totals are positive presentation amounts for assets/liabilities/equity.
    if meta.get("mode") != "standard_mizan":
        for code,prefix in [("1","1"),("2","2"),("3","3"),("4","4")]:
            if code in source_subtotals:
                src=abs(float(source_subtotals[code]["amount"]))
                if code in {"1","2"}:
                    calc=abs(float(tb.loc[tb.account_code.str.startswith(prefix),"balance"].sum()))
                else:
                    calc=abs(float(tb.loc[tb.account_code.str.startswith(prefix),"balance"].sum()))
                diff=src-calc
                checks.append({"name":f"{code} balance group vs detail","status":"passed" if abs(diff)<0.01 else "warning","value":round(diff,2),"display_type":"currency"})
        if "5" in source_subtotals:
            src=abs(float(source_subtotals["5"]["amount"]))
            # Include all 5xx equity detail balances including current result presentation.
            calc=abs(float(-tb.loc[tb.account_code.str.startswith("5"),"balance"].sum()))
            diff=src-calc
            checks.append({"name":"5 Equity group vs detail","status":"passed" if abs(diff)<0.01 else "warning","value":round(diff,2),"display_type":"currency"})

    # Data Quality is a trust score, not a decorative 100. Source/detail inconsistencies matter.
    score=100
    for chk in checks:
        if chk["status"]=="failed": score-=30
        elif chk["status"]=="warning": score-=7
    return {"score":max(0,score),"checks":checks}

from frontend_template import HOME_HTML as _HOME_T, PRICING_HTML as _PRICING_T, ABOUT_HTML as _ABOUT_T, CONTACT_HTML as _CONTACT_T, SECURITY_HTML as _SECURITY_T, APP_HTML as _APP_T
HOME_PAGE = _HOME_T.replace("__APP_VERSION__", APP_VERSION)
PRICING_PAGE = _PRICING_T.replace("__APP_VERSION__", APP_VERSION)
ABOUT_PAGE = _ABOUT_T.replace("__APP_VERSION__", APP_VERSION)
CONTACT_PAGE = _CONTACT_T.replace("__APP_VERSION__", APP_VERSION)
SECURITY_PAGE = _SECURITY_T.replace("__APP_VERSION__", APP_VERSION)
HTML = _APP_T.replace("__APP_VERSION__", APP_VERSION)  # the analysis app itself

@app.get('/',response_class=HTMLResponse)
def home()->str:return HOME_PAGE

@app.get('/paketler',response_class=HTMLResponse)
def pricing_page()->str:return PRICING_PAGE

@app.get('/hakkimizda',response_class=HTMLResponse)
def about_page()->str:return ABOUT_PAGE

@app.get('/iletisim',response_class=HTMLResponse)
def contact_page()->str:return CONTACT_PAGE

@app.get('/guvenlik',response_class=HTMLResponse)
def security_page()->str:return SECURITY_PAGE

@app.get('/uygulama',response_class=HTMLResponse)
def app_page()->str:return HTML

@app.get('/api/health')
def health()->dict[str,str]:return {'status':'ok','service':'digital-finance-bp','version':APP_VERSION}

# Bundled sample workbooks live one directory above backend/. Serving them by
# a fixed, whitelisted name (never a user-supplied path) lets the landing page
# offer a one-click "try with sample data" demo — no upload needed to see the
# full WHAT-WHY-SOWHAT-NOWWHAT flow, which matters far more for a sales demo
# than for day-to-day use.
import os as _os
from fastapi.staticfiles import StaticFiles
_PROJECT_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
_STATIC_DIR = _os.path.join(_PROJECT_ROOT, 'static')
if _os.path.exists(_STATIC_DIR):
    app.mount('/static', StaticFiles(directory=_STATIC_DIR), name='static')
_SAMPLE_FILES = {
    'mizan': ('sample_mizan.xlsx', 'Örnek Mizan (Genel)'),
    'mizan_prior': ('sample_mizan_period1.xlsx', 'Örnek Mizan (Önceki Dönem)'),
    'three_sheet': ('sample_three_sheet_financials.xlsx', 'Örnek 3 Tablo (Bilanço + Gelir Tablosu)'),
    # Data Hub demo set — a matching mizan + AR/AP aging + inventory + sales ledger
    # so the multi-source engines (AR/AP intelligence, inventory, PVM/sales-driven
    # profit bridge) actually have data to run against in the one-click demo.
    'hub_mizan': ('demo_data/sample_mizan_2025_donem2.xlsx', 'Data Hub — Mizan (2025 Cari Dönem)'),
    'hub_mizan_prior': ('demo_data/sample_mizan_2024_donem1.xlsx', 'Data Hub — Mizan (2024 Önceki Dönem)'),
    'ar_aging': ('demo_data/sample_ar_aging.xlsx', 'Data Hub — AR Yaşlandırma'),
    'ap_aging': ('demo_data/sample_ap_aging.xlsx', 'Data Hub — AP Yaşlandırma'),
    'inventory': ('demo_data/sample_inventory.xlsx', 'Data Hub — Stok'),
    'sales_ledger': ('demo_data/sample_sales_ledger.xlsx', 'Data Hub — Satış Defteri'),
}
# The set of keys fetched together for the one-click "Data Hub'ı örnekle dene" demo.
DATA_HUB_SAMPLE_KEYS = ['hub_mizan_prior', 'hub_mizan', 'ar_aging', 'ap_aging', 'inventory', 'sales_ledger']

@app.get('/api/sample/{key}')
def get_sample(key: str):
    from fastapi.responses import Response
    entry = _SAMPLE_FILES.get(key)
    if not entry:
        raise HTTPException(status_code=404, detail='Örnek dosya bulunamadı.')
    fname, _label = entry
    fpath = _os.path.join(_PROJECT_ROOT, fname)
    if not _os.path.isfile(fpath):
        raise HTTPException(status_code=404, detail='Örnek dosya sunucuda bulunamadı.')
    with open(fpath, 'rb') as f:
        data = f.read()
    return Response(content=data, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                     headers={'Content-Disposition': f'inline; filename="{fname}"'})

@app.get('/api/sample')
def list_samples() -> dict[str, Any]:
    return {'samples': [{'key': k, 'filename': v[0], 'label': v[1]} for k, v in _SAMPLE_FILES.items()],
            'data_hub_demo_keys': DATA_HUB_SAMPLE_KEYS}


def classify_sheet(sname: str, raw: pd.DataFrame) -> str:
    ns = normalize(sname)
    tokens = set(ns.split())
    texts = safe_extract_texts(raw, 15)

    # 1. Operational Subledgers (Sales, Aging, Inventory, Notes)
    if any(k in ns for k in ["sales", "satis", "satış", "fatura", "musteri", "customer", "pivot", "profitability", "profit analyze"]):
        return "sales"
    if any(k in ns for k in ["aging", "yaslandirma", "yaşlandırma"]):
        return "aging"
    if any(k in ns for k in ["inventory", "stok"]):
        return "inventory"
    if any(k in ns for k in ["kontrol", "notlar", "notes", "summary", "ozet", "özet", "q1", "q2", "task"]):
        return "notes_or_other"

    # 2. Financial Statements: Profit & Loss (P&L, Gelir Tablosu)
    if (
        "pl" in tokens
        or "p l" in ns
        or "p&l" in ns
        or any(k in ns for k in ["income statement", "income", "gelir tablosu", "kar zarar", "gelir tab"])
        or "income statement" in texts
        or "gelir tablosu" in texts
        or "gross sales" in texts
    ):
        return "profit_and_loss"

    # 3. Financial Statements: Balance Sheet Liabilities / Equity (Pasif, Kaynaklar)
    if (
        "bs liab" in ns
        or "bs liabilities" in ns
        or any(k in ns for k in ["liabilit", "equity", "pasif", "kaynak", "ozkaynak", "özkaynak"])
        or "liabilities" in texts
        or "pasif" in texts
        or "short term liabilities" in texts
        or "financial liabilities" in texts
    ):
        return "liabilities_equity"

    # 4. Financial Statements: Balance Sheet Assets (Aktif, Varlıklar)
    if (
        "bs asset" in ns
        or "bs assets" in ns
        or any(k in ns for k in ["asset", "aktif", "varlik", "varlık"])
        or "current assets" in texts
        or "donen varliklar" in texts
        or "dönen varlıklar" in texts
    ):
        return "assets"

    # Fallback from dominant account groups.
    counts = {"assets": 0, "liabilities_equity": 0, "profit_and_loss": 0}
    for col in range(raw.shape[1]):
        for r in range(min(len(raw), 250)):
            d = account_digits(raw.iat[r, col])
            if len(d) == 3:
                c = int(d)
                if 100 <= c <= 299: counts["assets"] += 1
                elif 300 <= c <= 599: counts["liabilities_equity"] += 1
                elif 600 <= c <= 799: counts["profit_and_loss"] += 1
    return max(counts, key=counts.get) if max(counts.values()) else "unknown"


def merge_workbook_statement_sheets(sheets: dict[str,pd.DataFrame]):
    parsed=[]
    all_findings=[]
    sheet_meta=[]
    for sname, raw in sheets.items():
        if raw is None or raw.empty:
            continue
        role = classify_sheet(sname, raw)
        # Skip operational sheets (sales, customer tables, aging, notes) from being parsed as trial balance
        if role in ("sales", "aging", "inventory", "notes_or_other"):
            sheet_meta.append({"sheet": sname, "role": role, "mode": f"operational_{role}_sheet", "rows": int(len(raw))})
            continue

        det = detect_special_layout(raw) if is_special_financial_statement_layout(raw, sname) else None
        if det:
            try:
                tb, meta=build_special_trial_balance(raw, det)
                tb.loc[:,"source_sheet"]=sname
                tb.loc[:,"source_role"]=role
                parsed.append(tb)
                sc=tb.attrs.get("source_controls",{})
                all_findings.extend([{**x,"sheet":sname} for x in sc.get("reconciliation_findings",[])])
                sheet_meta.append({"sheet":sname,"role":role,"mode":meta.get("mode"),"rows":int(len(tb)),"code_column":meta.get("code_column"),"name_column":meta.get("name_column"),"amount_column":meta.get("amount_column")})
                continue
            except Exception:
                pass
        # Universal Reader v4: ingestion (multi_source_ingestion._read_one) already
        # promotes a detected header row into real column names before this function
        # ever sees the sheet (e.g. columns literally named "Hesap Kodu", "Borç Bakiye").
        direct_mp = detect_mapping([str(c) for c in raw.columns])
        if "account_code" in direct_mp:
            try:
                tb, _src = prepare_trial_balance(raw, direct_mp)
                tb.loc[:, "source_sheet"] = sname
                tb.loc[:, "source_role"] = role
                parsed.append(tb)
                amt_field = direct_mp.get("balance") or direct_mp.get("debit_balance") or direct_mp.get("debit_turnover") or {}
                sheet_meta.append({"sheet": sname, "role": role, "mode": "standard_mizan_direct", "rows": int(len(tb)),
                                    "code_column": direct_mp["account_code"]["source_column"],
                                    "amount_column": amt_field.get("source_column")})
                continue
            except Exception:
                pass
        # Try standard header format on this individual sheet.
        one={sname:raw}
        std=detect_standard_header_sheet(one)
        if std:
            _,header_row,df=std
            mp=detect_mapping([str(c) for c in df.columns])
            if "account_code" in mp:
                tb,_src=prepare_trial_balance(df,mp)
                tb.loc[:,"source_sheet"]=sname
                tb.loc[:,"source_role"]=role
                parsed.append(tb)
                sheet_meta.append({"sheet":sname,"role":role,"mode":"standard_mizan","rows":int(len(tb)),"header_row":header_row+1,"code_column":mp["account_code"]["source_column"],"amount_column":mp.get("balance",mp.get("debit_balance",{})).get("source_column") if isinstance(mp.get("balance",mp.get("debit_balance",{})),dict) else None})
                continue
        # Final fallback: headerless account exports.
        try:
            inferred = infer_headerless_financial_table(raw)
        except Exception:
            inferred = None
        if inferred is not None:
            inferred_df, inferred_meta = inferred
            try:
                mp = {"account_code": {"source_column": "account_code", "confidence": 100}}
                if "balance" in inferred_df.columns:
                    mp["balance"] = {"source_column": "balance", "confidence": 100}
                elif "debit_balance" in inferred_df.columns:
                    mp["debit_balance"] = {"source_column": "debit_balance", "confidence": 100}
                if "account_name" in inferred_df.columns:
                    mp["account_name"] = {"source_column": "account_name", "confidence": 100}
                tb,_src = prepare_trial_balance(inferred_df, mp)
                tb["source_sheet"] = sname
                tb["source_role"] = role
                parsed.append(tb)
                sheet_meta.append({"sheet":sname,"role":role,"mode":inferred_meta.get("mode","headerless_financial_inference"),"rows":int(len(tb)),**{k:v for k,v in inferred_meta.items() if k not in {"mode","confidence","account_rows"}}})
                continue
            except Exception:
                pass
        # A sheet without detectable financial rows is not fatal.
        sheet_meta.append({"sheet":sname,"role":role,"mode":"ignored_or_unrecognized","rows":0})

    if not parsed:
        return None, None, None, all_findings, sheet_meta
    # Concatenate all financial sheets. Deduplicate exact same account/source only.
    tb=pd.concat(parsed, ignore_index=True)
    tb, duplicate_findings = canonicalize_transactions(tb)
    all_findings.extend(duplicate_findings)
    tb.attrs["source_controls"]={"reconciliation_findings":all_findings}
    has_separate_statements = any(s.get("role") in ("assets", "liabilities_equity", "profit_and_loss") for s in sheet_meta if s.get("rows", 0) > 0)
    if has_separate_statements:
        workbook_mode = "multi_statement_financial_workbook"
    elif len(parsed) > 1:
        workbook_mode = "multi_sheet"
    else:
        workbook_mode = "single_sheet"
    return tb, sheet_meta, workbook_mode, all_findings, sheet_meta

MAX_UPLOAD_BYTES = 15 * 1024 * 1024

def _validate_upload(filename: str, content: bytes) -> None:
    ext = filename.lower().rsplit('.', 1)[-1] if '.' in filename else ''
    if ext not in {"xlsx", "xlsm", "xls", "csv", "xml", "json"}:
        raise HTTPException(status_code=400, detail="Yalnızca CSV, XLSX, XLSM, XLS, GİB e-Defter XML ve JSON destekleniyor.")
    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="Dosya boyutu 15 MB sınırını aşıyor.")

def _process_workbook(content: bytes, filename: str) -> dict[str, Any]:
    """Shared single-workbook pipeline: bytes in, statements/quality/tb out.

    Used by single-period, multi-period trend, and automated ERP / e-Defter
    ingestion pipelines so all stay in sync with canonical model logic.
    """
    _validate_upload(filename, content)
    ext = filename.lower().rsplit('.', 1)[-1] if '.' in filename else ''
    if ext in {"xml", "json"}:
        df, meta_ingest = process_ingestion_payload(content, filename=filename)
        tb = df.copy()
        if 'account_code' not in tb.columns:
            raise HTTPException(status_code=422, detail='Dosyada hesap kodu tespit edilemedi.')
        if 'debit_balance' not in tb.columns:
            tb['debit_balance'] = 0.0
        if 'credit_balance' not in tb.columns:
            tb['credit_balance'] = 0.0
        if 'balance' not in tb.columns:
            tb['balance'] = tb['debit_balance'] - tb['credit_balance']
        if 'debit_turnover' not in tb.columns:
            tb['debit_turnover'] = tb.get('debit_total', tb['debit_balance'])
        if 'credit_turnover' not in tb.columns:
            tb['credit_turnover'] = tb.get('credit_total', tb['credit_balance'])
        if 'account_name' not in tb.columns:
            tb['account_name'] = tb['account_code'].astype(str)

        tb[['account_group', 'statement_bucket']] = pd.DataFrame(tb['account_code'].map(account_class).tolist(), index=tb.index)
        tb['source_sheet'] = meta_ingest.get('detected_source', 'ERP Ingestion')
        tb['source_row'] = range(1, len(tb) + 1)

        statements = aggregate_statements(tb)
        period = infer_period(filename, {})
        statements['period_metadata'] = period
        sheet_meta = [{'sheet_name': meta_ingest.get('detected_source', 'Ingestion'), 'role': 'finance', 'erp_badge': meta_ingest.get('erp_badge', 'ERP')}]
        mapping = {'workbook_mode': 'ingestion', 'sheet_count': 1, 'sheets': sheet_meta}
        meta = {'mode': 'ingestion', 'erp_badge': meta_ingest.get('erp_badge'), 'detected_source': meta_ingest.get('detected_source'), 'reconciliation_findings': []}
        quality = quality_checks(None, mapping, tb, meta, statements)
        quality['advanced'] = build_data_quality_report(tb, statements, quality, period)
        top = (tb.assign(abs_balance=tb.balance.abs()).sort_values('abs_balance', ascending=False).head(80)
               [['account_code', 'account_name', 'debit_turnover', 'credit_turnover', 'debit_balance', 'credit_balance', 'balance', 'account_group', 'statement_bucket']]
               .to_dict(orient='records'))
        return {
            'tb': tb, 'statements': statements, 'mapping': mapping, 'meta': meta, 'quality': quality,
            'mode': 'ingestion', 'sheet_meta': sheet_meta, 'top': top,
        }

    try:
        sheets = read_workbook_all_sheets(content, filename)
    except HTTPException:
        raise
    if not sheets:
        raise HTTPException(status_code=422, detail='Dosyada okunabilir çalışma sayfası bulunamadı.')

    merged = merge_workbook_statement_sheets(sheets)
    tb, sheet_meta, mode, findings, _ = merged
    if tb is None or tb.empty:
        raise HTTPException(status_code=422, detail='Dosyada otomatik olarak finansal hesap satırları tespit edilemedi. Çalışma sayfalarında hesap kodu ve finansal tutar yapısı bulunamadı.')

    statements = aggregate_statements(tb)
    period = infer_period(filename, sheets)
    statements['period_metadata'] = period
    mapping = {'workbook_mode': mode, 'sheet_count': len(sheet_meta), 'sheets': sheet_meta}
    meta = {'mode': mode, 'sheet_count': len(sheet_meta), 'sheets': sheet_meta, 'reconciliation_findings': findings}
    quality = quality_checks(None, mapping, tb, meta, statements)
    quality['advanced'] = build_data_quality_report(tb, statements, quality, period)
    top = (tb.assign(abs_balance=tb.balance.abs()).sort_values('abs_balance', ascending=False).head(80)
           [['account_code', 'account_name', 'debit_turnover', 'credit_turnover', 'debit_balance', 'credit_balance', 'balance', 'account_group', 'statement_bucket']]
           .to_dict(orient='records'))
    return {
        'tb': tb, 'statements': statements, 'mapping': mapping, 'meta': meta, 'quality': quality,
        'mode': mode, 'sheet_meta': sheet_meta, 'top': top,
    }


def _canonical_model(statements: dict[str, Any], tb=None) -> dict[str, Any]:
    model = {
        'period_metadata': statements.get('period_metadata'),
        'profit_and_loss': statements['profit_and_loss'],
        'balance_sheet': statements['balance_sheet'],
        'kpis': statements['kpis'],
    }
    if tb is not None:
        # Defensive: some ingestion paths may not populate every traceability
        # column. Never let a missing column turn a successful analysis into a
        # 500 error — fall back to None for whatever isn't present instead.
        wanted = ['account_code','account_name','balance','account_group','statement_bucket','source_sheet','source_row']
        safe_tb = tb.copy()
        for col in wanted:
            if col not in safe_tb.columns:
                safe_tb[col] = None
        model['accounts'] = [
            {k:(float(v) if isinstance(v,(int,float)) else v) for k,v in row.items()}
            for row in safe_tb[wanted].to_dict(orient='records')
        ]
    return model


@app.get('/api/inspect/schemas')
def get_canonical_schemas() -> dict[str, Any]:
    """Return available canonical data schemas and fields for client-side mapping UI."""
    return CANONICAL_SCHEMAS


def _is_upload_file(f: Any) -> bool:
    return f is not None and hasattr(f, 'filename') and hasattr(f, 'read') and bool(getattr(f, 'filename', None))


@app.post('/api/inspect')
async def inspect_uploaded_files(
    file: UploadFile | None = File(None),
    files: list[UploadFile] | None = File(None),
) -> dict[str, Any]:
    """Rapid pre-flight structure & ERP inspection endpoint (<80ms).

    Determines originating ERP (Logo, Mikro, Netsis, Luca, Zirve, SAP, Excel),
    infers canonical role, maps columns, and returns preview rows for the Smart
    Auto-Mapper Wizard without running the full 33 engines.
    """
    selected = []
    if isinstance(files, list):
        selected.extend([f for f in files if _is_upload_file(f)])
    elif _is_upload_file(files):
        selected.append(files)
    if _is_upload_file(file):
        selected.insert(0, file)
    if not selected:
        raise HTTPException(status_code=400, detail='İncelenecek dosya seçilmedi.')

    inspected_files = []
    for f in selected:
        if not f.filename:
            continue
        content = await f.read()
        res = inspect_file_structure(content, f.filename)
        inspected_files.append(res)

    primary = inspected_files[0].get('primary') if inspected_files and inspected_files[0].get('status') == 'success' else None
    return {
        'count': len(inspected_files),
        'files': inspected_files,
        'primary': primary,
        'detected_erp': primary.get('detected_erp') if primary else 'generic',
        'erp_badge': primary.get('erp_badge') if primary else 'Standart Excel / CSV',
        'erp_confidence': primary.get('erp_confidence') if primary else 0.85,
        'role': primary.get('role') if primary else 'finance',
        'role_label': primary.get('role_label') if primary else 'Mizan (Büyük Defter)',
        'is_ready': primary.get('is_ready', True) if primary else True,
    }


@app.post('/api/mizan/analyze')
async def analyze_mizan(
    file: UploadFile | None = File(None),
    files: list[UploadFile] | None = File(None),
    sector: str | None = Form(None),
) -> dict[str, Any]:
    # Backward compatible: old clients can still send `file`; multi-file clients
    # are automatically routed to Data Hub instead of receiving a 422.
    selected = []
    if isinstance(files, list):
        selected.extend([f for f in files if _is_upload_file(f)])
    elif _is_upload_file(files):
        selected.append(files)
    if _is_upload_file(file):
        selected.insert(0, file)
    if len(selected) == 0:
        raise HTTPException(status_code=400, detail='En az bir dosya seçin.')
    if len(selected) > 1:
        raw=[]
        for f in selected:
            if not f.filename: continue
            content=await f.read(); _validate_upload(f.filename,content); raw.append((f.filename,content))
        # Reuse the same Data Hub pipeline and response contract.
        return await _analyze_data_hub_raw(raw, sector)
    file=selected[0]
    if not file.filename:
        raise HTTPException(status_code=400, detail='Dosya adı bulunamadı.')
    content = await file.read()
    result = _process_workbook(content, file.filename)
    tb, statements, mapping, meta, quality = result['tb'], result['statements'], result['mapping'], result['meta'], result['quality']

    business_partner = build_finance_business_partner_analysis(statements, quality, sector=sector)
    return {
        'filename': file.filename,
        'source': {'mode': result['mode'], 'sheet_count': len(result['sheet_meta']), 'sheets': result['sheet_meta']},
        'columns': [],
        'mapping': mapping,
        'quality': quality,
        'statements': statements,
        'business_partner': business_partner,
        'fx_rates': business_partner.get('fx_rates'),
        'account_count': int(tb.account_code.nunique()),
        'rows': int(len(tb)),
        'canonical_model': _canonical_model(statements, tb),
        'top_accounts_by_abs_balance': result['top'],
        'available_sectors': list(SECTOR_BANDS.keys()),
    }


@app.post('/api/mizan/analyze-trend')
async def analyze_mizan_trend(
    files: list[UploadFile] = File(...),
    sector: str | None = Form(None),
) -> dict[str, Any]:
    """Multi-period endpoint powering the Trend Analysis Engine.

    Upload 2+ workbooks in chronological order (oldest first, most recent
    last). The most recent file becomes the "current period" and drives the
    full business-partner analysis (root cause, risk, opportunities, CCC,
    benchmarking); the earlier files are used only to compute period-over-
    period trends.
    """
    if len(files) < 2:
        raise HTTPException(status_code=400, detail='Trend analizi için en az 2 dönem dosyası yüklemelisiniz (eski -> yeni sırayla).')

    periods = []
    for f in files:
        if not f.filename:
            raise HTTPException(status_code=400, detail='Dosya adı bulunamadı.')
        content = await f.read()
        r = _process_workbook(content, f.filename)
        periods.append({'label': f.filename, 'result': r})

    current = periods[-1]
    previous_periods = [{'label': p['label'], 'statements': p['result']['statements']} for p in periods[:-1]]

    statements = current['result']['statements']
    quality = current['result']['quality']
    business_partner = build_finance_business_partner_analysis(statements, quality, sector=sector, previous_periods=previous_periods)

    tb = current['result']['tb']
    return {
        'current_filename': current['label'],
        'period_filenames': [p['label'] for p in periods],
        'source': {'mode': current['result']['mode'], 'sheet_count': len(current['result']['sheet_meta']), 'sheets': current['result']['sheet_meta']},
        'quality': quality,
        'statements': statements,
        'business_partner': business_partner,
        'account_count': int(tb.account_code.nunique()),
        'rows': int(len(tb)),
        'canonical_model': _canonical_model(statements, tb),
        'top_accounts_by_abs_balance': current['result']['top'],
        'available_sectors': list(SECTOR_BANDS.keys()),
    }




async def _analyze_data_hub_raw(raw_files:list[tuple[str,bytes]], sector:str|None=None) -> dict[str,Any]:
    """Core multi-source orchestration shared by API entry points."""
    from finance_engine.multi_source_ingestion import ingest_sources
    inspected = ingest_sources(raw_files, _process_workbook, max_mb=MAX_UPLOAD_BYTES/1024/1024)

    # Ingest and classify all finance/mizan workbooks so multi-period trends and
    # the Cash Bridge (Net profit -> Working Capital drag -> Cash) work out of the box.
    finance_entries = []
    for fn, content in raw_files:
        if any(s.get('filename') == fn and any(r.get('role') == 'finance' for r in s.get('roles', [])) for s in inspected.get('files', [])):
            try:
                r = _process_workbook(content, fn)
                finance_entries.append({'filename': fn, 'content': content, 'result': r})
            except Exception:
                pass

    if finance_entries:
        def _fin_sort_key(entry):
            meta = entry['result']['statements'].get('period_metadata') or {}
            end = str(meta.get('period_end') or '')
            start = str(meta.get('period_start') or '')
            fn = entry['filename'].lower()
            years = re.findall(r'(?<!\d)(20\d{2})(?!\d)', fn)
            year_val = int(years[-1]) if years else 0
            is_prior = 0 if any(w in fn for w in ['prior', 'onceki', 'önceki', 'donem1', 'dönem1', 'period1']) else 1
            return (end, start, year_val, is_prior)

        sorted_fin = sorted(finance_entries, key=_fin_sort_key)
        current_entry = sorted_fin[-1]
        prior_entries = sorted_fin[:-1]
        previous_periods = [{'label': p['filename'], 'statements': p['result']['statements']} for p in prior_entries] if prior_entries else None

        finance_name = current_entry['filename']
        finance_result = current_entry['result']
        statements = finance_result['statements']
        quality = finance_result['quality']
        bp = build_finance_business_partner_analysis(statements, quality, sector=sector, previous_periods=previous_periods)
        base_resp = {
            'filename': finance_name,
            'source': {'mode': finance_result['mode'], 'sheet_count': len(finance_result['sheet_meta']), 'sheets': finance_result['sheet_meta']},
            'quality': quality,
            'statements': statements,
            'business_partner': bp,
            'account_count': int(finance_result['tb'].account_code.nunique()),
            'rows': int(len(finance_result['tb'])),
            'canonical_model': _canonical_model(statements, finance_result['tb']),
            'top_accounts_by_abs_balance': finance_result['top'],
        }
        if prior_entries:
            base_resp['period_filenames'] = [e['filename'] for e in sorted_fin]
        finance_filenames = {e['filename'] for e in sorted_fin}
        optional = [x for x in raw_files if x[0] not in finance_filenames]
    else:
        previous_periods = None
        statements = {}
        optional = raw_files
        base_resp = {
            'filename': None,
            'source': {'mode': 'operational_only'},
            'quality': {'score': None, 'status': 'Operational source only'},
            'statements': {},
            'business_partner': {},
        }

    ms = build_multi_source_intelligence(optional, _process_workbook, statements, max_mb=MAX_UPLOAD_BYTES/1024/1024)
    # FIX (customer-trust bug): fold cross-source reconciliation warnings into
    # the headline Data Quality Score instead of showing a contradictory
    # "100/100 Trusted" badge next to unresolved GL vs. Sales/AR/AP warnings.
    if base_resp.get('quality', {}).get('advanced'):
        base_resp['quality']['advanced'] = apply_cross_source_reconciliation(base_resp['quality']['advanced'], ms.get('reconciliation'))
    # Re-run the deterministic BP interpretation with cross-source evidence and previous periods so
    # root cause, gaps, actions, cash bridge, and PVM can use both operational and multi-period facts.
    if base_resp.get('business_partner') is not None:
        base_resp['business_partner'] = build_finance_business_partner_analysis(
            statements, quality, sector=sector, previous_periods=previous_periods, data_hub=ms
        )
    if base_resp.get('business_partner') is not None:
        cross = []
        for f in ms.get('findings', []):
            cross.append({
                'code': 'MS-' + str(len(cross) + 1).zfill(3),
                'category': 'Multi-Source',
                'severity': f.get('severity', 'medium'),
                'title': f.get('title', 'Cross-source finding'),
                'evidence': [f.get('detail', '')],
                'interpretation': f.get('detail', ''),
                'recommendation': 'İlgili operasyonel kaynağı ve GL mutabakatını inceleyin.',
                'confidence': 'medium',
            })
        base_resp['business_partner']['multi_source_findings'] = cross
    base_resp.update({'data_hub': ms, 'available_sectors': list(SECTOR_BANDS.keys()), 'data_hub_errors': ms.get('errors', [])})
    base_resp['ar_aging'] = ms.get('analysis', {}).get('ar_aging')
    base_resp['ap_aging'] = ms.get('analysis', {}).get('ap_aging')
    base_resp['sales_analysis'] = ms.get('analysis', {}).get('sales')
    base_resp['inventory_aging'] = ms.get('analysis', {}).get('inventory')
    base_resp['fx_rates'] = (base_resp.get('business_partner') or {}).get('fx_rates')
    return base_resp

@app.post('/api/data-hub/analyze')
async def analyze_data_hub(
    files: list[UploadFile] = File(...),
    sector: str | None = Form(None),
) -> dict[str, Any]:
    if not files:
        raise HTTPException(status_code=400, detail='Data Hub için en az bir dosya yükleyin.')
    raw=[]
    for f in files:
        if not f.filename: continue
        content=await f.read(); _validate_upload(f.filename,content); raw.append((f.filename,content))
    return await _analyze_data_hub_raw(raw, sector)

@app.post('/api/ai/cfo-narrative')
async def ai_cfo_narrative(payload: dict[str, Any]) -> dict[str, Any]:
    """Optional Gemini layer. The model receives verified engine outputs only."""
    instruction = payload.get('instruction')
    analysis = payload.get('analysis')
    if not isinstance(analysis, dict):
        raise HTTPException(status_code=400, detail='analysis alanı gerekli.')
    return build_ai_cfo_response(analysis, instruction)

@app.get('/api/config')
def config() -> dict[str, Any]:
    import os
    return {'version':APP_VERSION,'max_upload_mb':MAX_UPLOAD_BYTES/1024/1024,'ai_provider':'gemini','ai_configured':bool(os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')),'sectors':list(SECTOR_BANDS.keys()),'auth_enabled':True,'history_persistent':bool(os.getenv('DATABASE_URL'))}


# ---------------------------------------------------------------------------
# Otomatik ERP & e-Defter Ingestion API (Zero-Touch Ingestion Hub)
# ---------------------------------------------------------------------------
@app.get('/api/v1/connectors/status')
def get_connectors_status() -> dict[str, Any]:
    """Kayıtlı ERP ve e-Defter konnektörlerinin durumunu döner."""
    return {
        "status": "online",
        "webhook_endpoint": "/api/v1/ingest/mizan",
        "supported_connectors": [
            {
                "id": "edefter_xml",
                "name": "GİB e-Defter (Kebir / Yevmiye XML)",
                "type": "official_regulatory",
                "status": "active",
                "badge": "GİB e-Defter XML",
                "description": "Gelir İdaresi Başkanlığı resmi e-Defter Kebir XBRL-GL standart XML ayrıştırıcı.",
                "supported_integrators": ["Uyumsoft", "Sovos / Foriba", "Digital Planet", "KolayBi", "Logo İşbaşı", "Mikro Yazılım"],
                "protocol": "GİB XML / REST Webhook",
                "sync_frequency": "Aylık Otomatik / Anlık",
            },
            {
                "id": "sap_odata",
                "name": "SAP S/4HANA & SAP ECC",
                "type": "enterprise_erp",
                "status": "active",
                "badge": "SAP S/4HANA OData",
                "description": "SAP OData API_TRIALBALANCE_SRV ve Gecelik ABAP Drop-Zone (S3/SFTP) entegrasyonu.",
                "supported_versions": ["SAP S/4HANA Cloud", "SAP S/4HANA On-Premise", "SAP ECC 6.0"],
                "protocol": "OData v2/v4 REST / JSON",
                "sync_frequency": "Gecelik 02:00 / Talebe Bağlı",
            },
            {
                "id": "netsuite",
                "name": "Oracle NetSuite & Cloud ERP",
                "type": "cloud_erp",
                "status": "active",
                "badge": "Oracle NetSuite",
                "description": "SuiteQL & SuiteTalk REST Web Services otomatik mizan ve muavin dökümü.",
                "supported_versions": ["NetSuite OneWorld", "Oracle Fusion Financials Cloud"],
                "protocol": "SuiteQL REST / JSON",
                "sync_frequency": "Haftalık / Gecelik",
            },
            {
                "id": "desktop_agent",
                "name": "Yerel Sync Agent (Logo Tiger, Mikro, Netsis)",
                "type": "on_premise_agent",
                "status": "active",
                "badge": "Local Sync Agent",
                "description": "Yerel MS SQL muhasebe sunucusunda çalışan 15 MB hafif salt-okunur (read-only) veri aktarım ajanı.",
                "supported_erps": ["Logo Tiger 3", "Logo Go 3", "Mikro Fly/Jump", "Netsis 3 Enterprise", "Zirve Müşavir"],
                "protocol": "mTLS Outbound Webhook (Zero-Inbound Port)",
                "sync_frequency": "Gecelik 02:30",
            },
        ],
        "default_api_keys": [
            {"name": "Canlı Kurumsal API Anahtarı", "key": "live_sec_cfo_demo_893247", "active": True},
            {"name": "SAP S/4HANA Servis Belirteci", "key": "sap_prod_token_991823", "active": True},
            {"name": "Oracle NetSuite API Belirteci", "key": "netsuite_api_441092", "active": True},
            {"name": "e-Defter Özel Entegratör Anahtarı", "key": "edefter_sovos_key_77123", "active": True},
        ],
    }


@app.post('/api/v1/ingest/mizan')
async def ingest_mizan_api(request: Request) -> dict[str, Any]:
    """
    Dış ERP sistemlerinden (SAP OData, NetSuite SuiteQL, e-Defter XML, Curl scriptleri)
    gelen verileri doğrudan kabul eder, doğrular ve sıfır insan müdahalesiyle analiz üretir.
    """
    auth_header = request.headers.get("X-API-KEY") or request.headers.get("Authorization") or request.query_params.get("api_key")
    tenant_info = validate_api_key(auth_header) if auth_header else {"company_name": "Doğrudan Webhook Şirketi"}
    if auth_header and not tenant_info:
        raise HTTPException(status_code=401, detail="Geçersiz veya yetkisiz API Anahtarı.")

    content_type = request.headers.get("content-type", "").lower()
    sector = request.query_params.get("sector")

    raw_data: Any = None
    filename = "mizan_ingest.xlsx"
    source_type = "auto"

    if "application/json" in content_type:
        try:
            body_json = await request.json()
        except Exception:
            raise HTTPException(status_code=400, detail="Geçersiz JSON yükü.")
        raw_data = body_json.get("payload", body_json)
        source_type = body_json.get("source_type", "auto") if isinstance(body_json, dict) else "auto"
        sector = sector or (body_json.get("sector") if isinstance(body_json, dict) else None)
        filename = "ingest_payload.json"
    elif "xml" in content_type or "text/xml" in content_type:
        raw_data = await request.body()
        filename = "edefter_kebir.xml"
        source_type = "edefter_xml"
    elif "multipart/form-data" in content_type:
        form = await request.form()
        uploaded_file = form.get("file")
        if not uploaded_file:
            raise HTTPException(status_code=400, detail="Yüklenecek dosya 'file' parametresiyle gönderilmelidir.")
        filename = uploaded_file.filename or "upload.xlsx"
        raw_data = await uploaded_file.read()
        source_type = form.get("source_type", "auto")
        sector = sector or form.get("sector")
    else:
        # Raw body fallback
        raw_data = await request.body()
        if not raw_data:
            raise HTTPException(status_code=400, detail="Boş veri yükü gönderildi.")
        if b"<?xml" in raw_data[:200]:
            filename = "edefter_kebir.xml"
            source_type = "edefter_xml"
        else:
            filename = "ingest_stream.bin"

    try:
        if isinstance(raw_data, (bytes, str)) and filename.endswith((".xml", ".json", ".xlsx", ".xls", ".csv")):
            result = _process_workbook(raw_data if isinstance(raw_data, bytes) else raw_data.encode("utf-8"), filename)
        else:
            # Direct JSON payload handling
            df, meta_ingest = process_ingestion_payload(raw_data, source_type=source_type, filename=filename)
            tb = df.copy()
            if 'account_code' not in tb.columns:
                raise HTTPException(status_code=422, detail='Hesap kodu sütunu tespit edilemedi.')
            if 'debit_balance' not in tb.columns:
                tb['debit_balance'] = 0.0
            if 'credit_balance' not in tb.columns:
                tb['credit_balance'] = 0.0
            if 'balance' not in tb.columns:
                tb['balance'] = tb['debit_balance'] - tb['credit_balance']
            if 'debit_turnover' not in tb.columns:
                tb['debit_turnover'] = tb.get('debit_total', tb['debit_balance'])
            if 'credit_turnover' not in tb.columns:
                tb['credit_turnover'] = tb.get('credit_total', tb['credit_balance'])
            if 'account_name' not in tb.columns:
                tb['account_name'] = tb['account_code'].astype(str)

            tb[['account_group', 'statement_bucket']] = pd.DataFrame(tb['account_code'].map(account_class).tolist(), index=tb.index)
            tb['source_sheet'] = meta_ingest.get('detected_source', 'ERP Ingestion')
            tb['source_row'] = range(1, len(tb) + 1)

            statements = aggregate_statements(tb)
            statements['period_metadata'] = infer_period(filename, {})
            sheet_meta = [{'sheet_name': meta_ingest.get('detected_source', 'Ingestion'), 'role': 'finance', 'erp_badge': meta_ingest.get('erp_badge', 'ERP')}]
            mapping = {'workbook_mode': 'ingestion', 'sheet_count': 1, 'sheets': sheet_meta}
            meta = {'mode': 'ingestion', 'erp_badge': meta_ingest.get('erp_badge'), 'detected_source': meta_ingest.get('detected_source'), 'reconciliation_findings': []}
            quality = quality_checks(None, mapping, tb, meta, statements)
            quality['advanced'] = build_data_quality_report(tb, statements, quality, statements['period_metadata'])
            top = (tb.assign(abs_balance=tb.balance.abs()).sort_values('abs_balance', ascending=False).head(80)
                   [['account_code', 'account_name', 'debit_turnover', 'credit_turnover', 'debit_balance', 'credit_balance', 'balance', 'account_group', 'statement_bucket']]
                   .to_dict(orient='records'))
            result = {
                'tb': tb, 'statements': statements, 'mapping': mapping, 'meta': meta, 'quality': quality,
                'mode': 'ingestion', 'sheet_meta': sheet_meta, 'top': top,
            }
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=422, detail=f"Veri yükü işlenirken hata oluştu: {str(exc)}")

    tb, statements, mapping, meta, quality = result['tb'], result['statements'], result['mapping'], result['meta'], result['quality']
    business_partner = build_finance_business_partner_analysis(statements, quality, sector=sector)

    return {
        'status': 'success',
        'automated_ingestion': True,
        'tenant': tenant_info,
        'filename': filename,
        'source': {'mode': result['mode'], 'sheet_count': len(result['sheet_meta']), 'sheets': result['sheet_meta']},
        'columns': [],
        'mapping': mapping,
        'quality': quality,
        'statements': statements,
        'business_partner': business_partner,
        'fx_rates': business_partner.get('fx_rates'),
        'account_count': int(tb.account_code.nunique()),
        'rows': int(len(tb)),
        'canonical_model': _canonical_model(statements, tb),
        'top_accounts_by_abs_balance': result['top'],
        'available_sectors': list(SECTOR_BANDS.keys()),
    }


@app.post('/api/v1/connectors/simulate')
async def simulate_connector_sync(payload: dict[str, Any] = Body(...)) -> dict[str, Any]:
    """
    Arayüzde veya yatırımcı sunumlarında tek tıkla canlı SAP S/4HANA OData,
    Oracle NetSuite veya GİB e-Defter XML akışını simüle eder.
    """
    connector = payload.get("connector", "sap")
    sector = payload.get("sector")

    raw_data, src_type, filename = generate_mock_erp_payload(connector)
    content_bytes = raw_data if isinstance(raw_data, bytes) else _json.dumps(raw_data).encode("utf-8")

    result = _process_workbook(content_bytes, filename)
    tb, statements, mapping, meta, quality = result['tb'], result['statements'], result['mapping'], result['meta'], result['quality']
    business_partner = build_finance_business_partner_analysis(statements, quality, sector=sector)

    return {
        'status': 'success',
        'simulated_connector': connector,
        'filename': filename,
        'source': {'mode': result['mode'], 'sheet_count': len(result['sheet_meta']), 'sheets': result['sheet_meta']},
        'columns': [],
        'mapping': mapping,
        'quality': quality,
        'statements': statements,
        'business_partner': business_partner,
        'fx_rates': business_partner.get('fx_rates'),
        'account_count': int(tb.account_code.nunique()),
        'rows': int(len(tb)),
        'canonical_model': _canonical_model(statements, tb),
        'top_accounts_by_abs_balance': result['top'],
        'available_sectors': list(SECTOR_BANDS.keys()),
    }



# ---------------------------------------------------------------------------
# Auth + saved-history (Faz 1): register/login, save an analysis result under
# a fiscal year, list/filter by year, fetch one, compare two side by side.
# The analysis engines themselves are untouched -- this only persists their
# already-computed JSON output.
# ---------------------------------------------------------------------------
import json as _json
from pydantic import BaseModel as _BaseModel
try:
    from sqlalchemy.orm import Session as _Session
except ImportError:
    _Session = Any
from db import init_db as _init_db, get_db as _get_db, User as _User, AnalysisRecord as _AnalysisRecord
from auth import hash_password as _hash_password, verify_password as _verify_password, create_token as _create_token, get_current_user as _get_current_user
from fastapi import Depends as _Depends

_init_db()


class _RegisterPayload(_BaseModel):
    email: str
    password: str
    company_name: str | None = None


class _LoginPayload(_BaseModel):
    email: str
    password: str


class _SaveHistoryPayload(_BaseModel):
    company_name: str | None = None
    period_label: str | None = None
    fiscal_year: int
    analysis: dict[str, Any]


@app.post('/api/auth/register')
def auth_register(payload: _RegisterPayload, db: _Session = _Depends(_get_db)) -> dict[str, Any]:
    email = payload.email.strip().lower()
    if not email or '@' not in email:
        raise HTTPException(status_code=400, detail='Geçerli bir e-posta girin.')
    if len(payload.password) < 6:
        raise HTTPException(status_code=400, detail='Şifre en az 6 karakter olmalı.')
    if db.query(_User).filter(_User.email == email).first():
        raise HTTPException(status_code=409, detail='Bu e-posta zaten kayıtlı.')
    user = _User(email=email, password_hash=_hash_password(payload.password), company_name=payload.company_name)
    db.add(user); db.commit(); db.refresh(user)
    return {'token': _create_token(user.id, user.email), 'email': user.email, 'company_name': user.company_name}


@app.post('/api/auth/login')
def auth_login(payload: _LoginPayload, db: _Session = _Depends(_get_db)) -> dict[str, Any]:
    email = payload.email.strip().lower()
    user = db.query(_User).filter(_User.email == email).first()
    if not user or not _verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail='E-posta veya şifre hatalı.')
    return {'token': _create_token(user.id, user.email), 'email': user.email, 'company_name': user.company_name}


@app.get('/api/auth/me')
def auth_me(user: _User = _Depends(_get_current_user)) -> dict[str, Any]:
    return {'email': user.email, 'company_name': user.company_name}


@app.post('/api/history/save')
def history_save(payload: _SaveHistoryPayload, user: _User = _Depends(_get_current_user), db: _Session = _Depends(_get_db)) -> dict[str, Any]:
    score = None
    try:
        score = int(payload.analysis.get('health_score', {}).get('score'))
    except Exception:
        pass
    rec = _AnalysisRecord(
        user_id=user.id,
        company_name=payload.company_name or user.company_name,
        period_label=payload.period_label,
        fiscal_year=payload.fiscal_year,
        health_score=score,
        result_json=_json.dumps(payload.analysis),
    )
    db.add(rec); db.commit(); db.refresh(rec)
    return {'id': rec.id, 'saved_at': rec.created_at.isoformat()}


@app.get('/api/history/list')
def history_list(fiscal_year: int | None = None, user: _User = _Depends(_get_current_user), db: _Session = _Depends(_get_db)) -> dict[str, Any]:
    q = db.query(_AnalysisRecord).filter(_AnalysisRecord.user_id == user.id)
    if fiscal_year is not None:
        q = q.filter(_AnalysisRecord.fiscal_year == fiscal_year)
    records = q.order_by(_AnalysisRecord.fiscal_year.desc(), _AnalysisRecord.created_at.desc()).all()
    by_year: dict[int, list[dict[str, Any]]] = {}
    for r in records:
        by_year.setdefault(r.fiscal_year, []).append({
            'id': r.id, 'company_name': r.company_name, 'period_label': r.period_label,
            'health_score': r.health_score, 'created_at': r.created_at.isoformat(),
        })
    return {'years': sorted(by_year.keys(), reverse=True), 'by_year': by_year}


@app.get('/api/history/compare')
def history_compare(ids: str, user: _User = _Depends(_get_current_user), db: _Session = _Depends(_get_db)) -> dict[str, Any]:
    """ids = comma-separated record ids, e.g. '12,15'. Returns each record's
    saved analysis so the frontend can render a side-by-side comparison
    without recomputation.

    NOTE: this route MUST be declared before /api/history/{record_id} or
    FastAPI will match the literal path segment "compare" as record_id and
    fail with a 422 int-parsing error."""
    id_list = [int(x) for x in ids.split(',') if x.strip().isdigit()]
    if len(id_list) < 2:
        raise HTTPException(status_code=400, detail='Karşılaştırma için en az 2 kayıt id\'si gerekli.')
    records = db.query(_AnalysisRecord).filter(_AnalysisRecord.id.in_(id_list), _AnalysisRecord.user_id == user.id).all()
    if len(records) != len(id_list):
        raise HTTPException(status_code=404, detail='Bazı kayıtlar bulunamadı veya size ait değil.')
    ordered = sorted(records, key=lambda r: (r.fiscal_year, r.created_at))
    return {'items': [{'id': r.id, 'company_name': r.company_name, 'period_label': r.period_label, 'fiscal_year': r.fiscal_year, 'health_score': r.health_score, 'analysis': _json.loads(r.result_json)} for r in ordered]}


@app.get('/api/history/{record_id}')
def history_get(record_id: int, user: _User = _Depends(_get_current_user), db: _Session = _Depends(_get_db)) -> dict[str, Any]:
    r = db.query(_AnalysisRecord).filter(_AnalysisRecord.id == record_id, _AnalysisRecord.user_id == user.id).first()
    if not r:
        raise HTTPException(status_code=404, detail='Kayıt bulunamadı.')
    return {'id': r.id, 'company_name': r.company_name, 'period_label': r.period_label, 'fiscal_year': r.fiscal_year, 'created_at': r.created_at.isoformat(), 'analysis': _json.loads(r.result_json)}
