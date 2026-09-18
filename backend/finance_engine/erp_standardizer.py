from __future__ import annotations

import io
import re
from typing import Any
import pandas as pd

from .data_classifier import classify_dataframe, norm, ALIAS_NORM, _best_column
from .multi_source_ingestion import _read_one


# ---------------------------------------------------------------------------
# Supported ERP Signatures & Recognition Heuristics
# ---------------------------------------------------------------------------
ERP_PROFILES: dict[str, dict[str, Any]] = {
    "logo": {
        "name": "Logo (Tiger / Go / Wings)",
        "badge": "Logo Tiger/Go",
        "keywords": {"hesap_kodu", "hesap_adi", "borc_bakiye", "alacak_bakiye", "ch_kodu", "cari_kodu", "fis_no", "fatura_no"},
        "exact_headers": {"hesap kodu", "hesap aciklamasi", "borc bakiye", "alacak bakiye", "ch kodu", "cari kod", "tutar (tl)"},
    },
    "mikro": {
        "name": "Mikro Yazılım (Fly / Jump / V16)",
        "badge": "Mikro Fly/Jump",
        "keywords": {"hesap_no", "hesap_ismi", "borc_toplam", "alacak_toplam", "borc_bakiye", "alacak_bakiye", "sorumluluk_merkezi"},
        "exact_headers": {"hesap no", "hesap ismi", "borc toplam", "alacak toplam", "borc bakiye", "alacak bakiye", "sorumluluk merkezi"},
    },
    "netsis": {
        "name": "Netsis (Entegre / Enterprise)",
        "badge": "Netsis Enterprise",
        "keywords": {"hesap_kodu", "hesap_adi", "b_bakiye", "a_bakiye", "bakiye", "cari_kodu", "sube_kodu"},
        "exact_headers": {"hesap_kodu", "hesap_adi", "b_bakiye", "a_bakiye", "bakiye", "cari_kodu"},
    },
    "luca": {
        "name": "Luca TÜRMOB",
        "badge": "Luca TÜRMOB",
        "keywords": {"borc_tutari", "alacak_tutari", "borc_kalan", "alacak_kalan", "luca", "turmob"},
        "exact_headers": {"hesap kodu", "hesap adi", "borc tutari", "alacak tutari", "borc kalan", "alacak kalan"},
    },
    "zirve": {
        "name": "Zirve Müşavir / Finans",
        "badge": "Zirve Müşavir",
        "keywords": {"kodu", "adi", "b_bakiye", "a_bakiye", "borc", "alacak"},
        "exact_headers": {"kodu", "adi", "borc", "alacak", "b-bakiye", "a-bakiye"},
    },
    "sap": {
        "name": "SAP (S/4HANA & ECC)",
        "badge": "SAP S/4HANA",
        "keywords": {"gl_account", "account_long_text", "accumulated_balance", "doc_date", "posting_date", "company_code"},
        "exact_headers": {"g/l account", "account long text", "debit", "credit", "accumulated balance", "doc. date", "posting date"},
    },
    "datev": {
        "name": "DATEV (Kanzlei-Rechnungswesen / Unternehmen online)",
        "badge": "DATEV SKR03/04",
        "keywords": {"konto", "kontobezeichnung", "soll", "haben", "saldo", "belegfeld_1", "buchungstext", "debitoren", "kreditoren"},
        "exact_headers": {"konto", "kontobezeichnung", "soll", "haben", "saldo", "datum", "belegfeld 1", "buchungstext"},
    },
    "pennylane": {
        "name": "Pennylane / Cegid / Sage France",
        "badge": "Pennylane / PCG",
        "keywords": {"compte", "libelle_compte", "debit", "credit", "solde_debiteur", "solde_crediteur", "numero_de_piece"},
        "exact_headers": {"compte", "libelle compte", "debit", "credit", "solde", "date piece"},
    },
    "holded": {
        "name": "Holded / A3ERP / Contasol (España)",
        "badge": "Holded / PGC",
        "keywords": {"cuenta", "descripcion", "debe", "haber", "saldo_deudor", "saldo_acreedor", "n_asiento"},
        "exact_headers": {"cuenta", "descripcion", "debe", "haber", "saldo", "fecha"},
    },
    "exact_online": {
        "name": "Exact Online / Twinfield (Nederland & Benelux)",
        "badge": "Exact Online / RGS",
        "keywords": {"rekening", "rekeningomschrijving", "debet", "credit", "saldo", "factuurnummer", "relatie"},
        "exact_headers": {"rekening", "omschrijving", "debet", "credit", "saldo", "datum"},
    },
    "zucchetti": {
        "name": "Zucchetti / TeamSystem (Italia)",
        "badge": "Zucchetti / Civile",
        "keywords": {"codice_conto", "descrizione", "dare", "avere", "saldo", "data_registrazione"},
        "exact_headers": {"conto", "descrizione", "dare", "avere", "saldo"},
    },
    "xero": {
        "name": "Xero / QuickBooks Online (UK / Global IFRS)",
        "badge": "Xero / QBO IFRS",
        "keywords": {"account_code", "account_name", "debit", "credit", "net_balance", "invoice_date", "contact_name"},
        "exact_headers": {"account code", "account name", "debit", "credit", "balance", "net"},
    },
}


# ---------------------------------------------------------------------------
# Canonical Target Schemas with Field Labels & Required Flags
# ---------------------------------------------------------------------------
CANONICAL_SCHEMAS: dict[str, dict[str, Any]] = {
    "finance": {
        "label": "Mizan (Büyük Defter)",
        "description": "Hesap planı (TDHP), borç/alacak hareketleri ve bakiye dökümü",
        "fields": {
            "account_code": {"label": "Hesap Kodu (TDHP)", "required": True, "type": "string"},
            "account_name": {"label": "Hesap Adı / Açıklama", "required": False, "type": "string"},
            "debit_balance": {"label": "Borç Bakiye", "required": False, "type": "number"},
            "credit_balance": {"label": "Alacak Bakiye", "required": False, "type": "number"},
            "balance": {"label": "Net Bakiye", "required": False, "type": "number"},
            "debit_turnover": {"label": "Borç Hareketi", "required": False, "type": "number"},
            "credit_turnover": {"label": "Alacak Hareketi", "required": False, "type": "number"},
        },
    },
    "sales": {
        "label": "Satış Faturaları / Satış Dökümü",
        "description": "Fatura detayları, müşteri adları, satılan ürünler ve ciro",
        "fields": {
            "date": {"label": "Fatura Tarihi", "required": False, "type": "date"},
            "invoice": {"label": "Fatura / Belge No", "required": False, "type": "string"},
            "customer": {"label": "Müşteri / Cari Adı", "required": True, "type": "string"},
            "product": {"label": "Ürün Adı / SKU", "required": False, "type": "string"},
            "quantity": {"label": "Satış Miktarı", "required": False, "type": "number"},
            "net_sales": {"label": "Net Satış Tutarı", "required": True, "type": "number"},
            "cost": {"label": "Satış Maliyeti (SMM)", "required": False, "type": "number"},
            "term_price": {"label": "Vadeli Satış Tutarı", "required": False, "type": "number"},
            "cash_price": {"label": "Peşin Satış Tutarı", "required": False, "type": "number"},
        },
    },
    "ar_aging": {
        "label": "Müşteri Alacak Yaşlandırma (120)",
        "description": "Müşteri vadeleri, açık hesaplar ve geciken tahsilat takvimi",
        "fields": {
            "customer": {"label": "Müşteri / Cari Adı", "required": True, "type": "string"},
            "outstanding": {"label": "Açık / Kalan Bakiye", "required": True, "type": "number"},
            "due_date": {"label": "Vade Tarihi", "required": False, "type": "date"},
            "amount": {"label": "Toplam Fatura Tutarı", "required": False, "type": "number"},
            "paid": {"label": "Tahsil Edilen Tutar", "required": False, "type": "number"},
        },
    },
    "ap_aging": {
        "label": "Tedarikçi Borç Yaşlandırma (320)",
        "description": "Tedarikçi borçları, ödeme vadeleri ve açık hesaplar",
        "fields": {
            "vendor": {"label": "Tedarikçi / Satıcı Adı", "required": True, "type": "string"},
            "outstanding": {"label": "Kalan Borç Tutarı", "required": True, "type": "number"},
            "due_date": {"label": "Ödeme Vadesi", "required": False, "type": "date"},
            "amount": {"label": "Toplam Belge Tutarı", "required": False, "type": "number"},
        },
    },
    "inventory": {
        "label": "Stok Envanteri & Defteri",
        "description": "Depodaki ürünler, miktarlar ve bağlı sermaye tutarı",
        "fields": {
            "product": {"label": "Ürün Adı / Malzeme", "required": True, "type": "string"},
            "amount": {"label": "Toplam Stok Değeri", "required": False, "type": "number"},
            "quantity": {"label": "Depo Miktarı", "required": False, "type": "number"},
            "unit_cost": {"label": "Birim Maliyet", "required": False, "type": "number"},
            "warehouse": {"label": "Depo / Lokasyon", "required": False, "type": "string"},
            "last_movement": {"label": "Son Hareket Tarihi", "required": False, "type": "date"},
        },
    },
}


def detect_erp_signature(columns: list[str], sample_text: str = "", filename: str = "") -> tuple[str, str, float]:
    """Identify the originating ERP / accounting software with a confidence score."""
    fn_lower = filename.lower()
    raw_headers = {str(c).strip().lower() for c in columns}
    norm_headers = {norm(c).replace(" ", "_") for c in columns}
    combined_text = (sample_text + " " + " ".join(columns) + " " + filename).lower()

    scores: dict[str, float] = {}

    for erp_key, prof in ERP_PROFILES.items():
        score = 0.0
        # 1. Exact header matches
        exact_hits = len(raw_headers.intersection(prof["exact_headers"]))
        if exact_hits >= 3:
            score += 0.55 + min(0.35, exact_hits * 0.1)
        elif exact_hits >= 1:
            score += 0.25

        # 2. Normalized keyword matches
        keyword_hits = len(norm_headers.intersection(prof["keywords"]))
        if keyword_hits >= 3:
            score += 0.35 + min(0.20, keyword_hits * 0.05)
        elif keyword_hits >= 1:
            score += 0.15

        # 3. Text & metadata markers (e.g. "TÜRMOB", "LOGO TIGER", "MIKRO YAZILIM")
        if erp_key in fn_lower or erp_key in combined_text:
            score += 0.20
        if erp_key == "luca" and ("turmob" in combined_text or "türmob" in combined_text):
            score += 0.30

        scores[erp_key] = min(0.99, score)

    best_erp, best_score = max(scores.items(), key=lambda x: x[1])
    if best_score >= 0.50:
        prof = ERP_PROFILES[best_erp]
        return best_erp, prof["badge"], round(best_score, 2)

    return "generic", "Standart Excel / CSV", 0.85


def inspect_file_structure(content: bytes, filename: str) -> dict[str, Any]:
    """Rapid pre-flight inspector (<80ms):

    Determines ERP origin, classifies role, auto-maps columns to canonical
    schema, and produces sample preview rows for the UI Smart Auto-Mapper.
    """
    try:
        sheets = _read_one(content, filename)
    except Exception as exc:
        return {
            "status": "error",
            "filename": filename,
            "error": str(exc),
        }

    inspected_sheets = []
    sample_text = content[:4096].decode("utf-8", errors="ignore")

    for sname, df in sheets.items():
        if df is None or df.empty:
            continue

        raw_cols = [str(c) for c in df.columns if not str(c).startswith("_")]
        role, role_conf, mapping = classify_dataframe(df, filename, sname)

        erp_key, erp_badge, erp_conf = detect_erp_signature(raw_cols, sample_text, filename)

        schema = CANONICAL_SCHEMAS.get(role, CANONICAL_SCHEMAS["finance"])
        fields_def = schema["fields"]

        # Build column mapping details
        mapped_details = []
        unmapped_required = []

        for canonical_key, f_meta in fields_def.items():
            matched_col = mapping.get(canonical_key)
            if matched_col and matched_col in raw_cols:
                mapped_details.append({
                    "canonical_field": canonical_key,
                    "canonical_label": f_meta["label"],
                    "source_column": matched_col,
                    "is_required": f_meta["required"],
                    "type": f_meta["type"],
                    "confidence": round(role_conf, 2),
                })
            elif f_meta["required"]:
                unmapped_required.append({
                    "canonical_field": canonical_key,
                    "canonical_label": f_meta["label"],
                    "is_required": True,
                })

        # Produce first 4 rows for visual preview safely
        preview_rows = []
        for r in df.head(4).to_dict(orient="records"):
            clean_r = {str(k): (str(v)[:40] if pd.notna(v) and str(v) != "NaT" else "") for k, v in r.items() if not str(k).startswith("_")}
            preview_rows.append(clean_r)

        # Check European standard if role == 'finance'
        coa_info = None
        row_anomalies = []
        if role == "finance":
            code_col = mapping.get("account_code")
            name_col = mapping.get("account_name")
            if code_col and code_col in df.columns:
                # Satır bazlı anomali taraması (örn. TDHP 1xx-7xx standardı dışı veya bozuk format)
                for idx, val in df[code_col].items():
                    if pd.isna(val):
                        continue
                    s_val = str(val).strip()
                    # Başlık satırları veya boşlukları atla
                    if not s_val or s_val.lower() in ("hesap", "kod", "hesap kodu", "account", "toplam"):
                        continue
                    m = re.match(r"^(\d{3})", s_val)
                    if not m:
                        row_anomalies.append({
                            "line_number": int(idx) + 2,  # 1-based + 1 header row
                            "raw_value": s_val,
                            "reason": "Geçersiz hesap kodu formatı (3 basamaklı TDHP/hesap kökü bulunamadı)",
                            "suggestion": "Hesap kodunun '100', '120.01' vb. formatta olduğunu kontrol edin.",
                        })
                    elif m.group(1)[0] not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        row_anomalies.append({
                            "line_number": int(idx) + 2,
                            "raw_value": s_val,
                            "reason": f"Bilinmeyen ana hesap sınıfı ({m.group(1)})",
                            "suggestion": "Standart TDHP 1xx-7xx hesap kodları kullanılmalıdır.",
                        })
                    if len(row_anomalies) >= 10:  # UI'ı tıkamamak için ilk 10 anomaliyi al
                        break

            try:
                from .european_accounting_standardizer import detect_coa_standard
                sample_codes = [str(x) for x in df[code_col].dropna().head(50)] if code_col and code_col in df.columns else []
                sample_names = [str(x) for x in df[name_col].dropna().head(50)] if name_col and name_col in df.columns else []
                std_code, std_meta, std_conf = detect_coa_standard(sample_codes, sample_names, filename)
                coa_info = {
                    "standard": std_code,
                    "standard_name": std_meta["name"],
                    "flag": std_meta["country_flag"],
                    "confidence": std_conf,
                    "is_european": std_code != "TR_TDHP",
                }
            except Exception:
                pass

        inspected_sheets.append({
            "sheet_name": sname,
            "detected_erp": erp_key,
            "erp_badge": erp_badge,
            "erp_confidence": erp_conf,
            "coa_standard": coa_info,
            "role": role,
            "role_label": schema["label"],
            "role_description": schema["description"],
            "confidence": round(role_conf, 2),
            "total_rows": int(len(df)),
            "columns": raw_cols,
            "mapped_fields": mapped_details,
            "unmapped_required": unmapped_required,
            "row_anomalies": row_anomalies,
            "is_ready": len(unmapped_required) == 0,
            "preview_rows": preview_rows,
        })

    # Multi-statement workbook intelligence (e.g. separate BS Asset, BS Liab, and P&L sheets)
    has_assets = any(s["role"] == "assets" or any(k in s["sheet_name"].lower() for k in ["asset", "aktif"]) for s in inspected_sheets)
    has_liab = any(s["role"] == "liabilities_equity" or any(k in s["sheet_name"].lower() for k in ["liab", "pasif", "equity"]) for s in inspected_sheets)
    has_pnl = any(s["role"] == "profit_and_loss" or any(k in s["sheet_name"].lower() for k in ["income", "gelir", "p&l", "pl"]) for s in inspected_sheets)

    # Sort sheets: valid financial/operational sheets before unknown notes
    ranked_sheets = sorted(
        inspected_sheets,
        key=lambda s: (
            1 if s["role"] in ("finance", "assets", "liabilities_equity", "profit_and_loss") else (0.8 if s["role"] != "unknown" else 0),
            len(s.get("mapped_fields", [])),
            s.get("total_rows", 0)
        ),
        reverse=True
    )
    primary_sheet = ranked_sheets[0] if ranked_sheets else None

    if has_assets and (has_liab or has_pnl) and primary_sheet:
        primary_sheet = {
            **primary_sheet,
            "detected_erp": "multi_statement",
            "erp_badge": "Çoklu Finansal Tablo (Bilanço & P&L)",
            "erp_confidence": 0.98,
            "role": "finance",
            "role_label": "Bilanço (Aktif/Pasif) & Gelir Tablosu",
            "is_multi_statement": True,
            "statement_summary": {
                "has_assets": has_assets,
                "has_liabilities": has_liab,
                "has_pnl": has_pnl,
            }
        }

    return {
        "status": "success",
        "filename": filename,
        "primary": primary_sheet,
        "sheets": inspected_sheets,
        "is_multi_statement": has_assets and (has_liab or has_pnl),
    }
