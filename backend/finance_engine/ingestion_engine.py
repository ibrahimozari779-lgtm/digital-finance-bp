from __future__ import annotations

import io
import json
import logging
import xml.etree.ElementTree as ET
from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from .erp_standardizer import detect_erp_signature, inspect_file_structure, CANONICAL_SCHEMAS
from .data_classifier import classify_dataframe

logger = logging.getLogger(__name__)

# Örnek Varsayılan / Geliştirici API Anahtarları
DEFAULT_INGESTION_KEYS = {
    "live_sec_cfo_demo_893247": {"company_id": "demo_corp", "company_name": "Demo Sanayi ve Ticaret A.Ş.", "active": True},
    "sap_prod_token_991823": {"company_id": "sap_enterprise", "company_name": "Holding Kurumsal SAP Grubu", "active": True},
    "netsuite_api_441092": {"company_id": "netsuite_global", "company_name": "Global Teknoloji A.Ş.", "active": True},
    "edefter_sovos_key_77123": {"company_id": "edefter_client", "company_name": "KOBİ Üretim Ltd. Şti.", "active": True},
}


def validate_api_key(api_key: str | None) -> dict[str, Any] | None:
    """Verilen API anahtarını doğrular."""
    if not api_key:
        return None
    key_clean = api_key.strip().replace("Bearer ", "")
    if key_clean in DEFAULT_INGESTION_KEYS:
        info = DEFAULT_INGESTION_KEYS[key_clean]
        if info.get("active"):
            return info
    # Eğer özel test anahtarı gelirse (demo amacıyla)
    if key_clean.startswith("test_key_") or key_clean.startswith("demo_"):
        return {"company_id": "custom_tenant", "company_name": "Özel Entegre Şirket", "active": True}
    return None


# ---------------------------------------------------------------------------
# 1. GİB e-Defter (Kebir / Yevmiye) XML Parser
# ---------------------------------------------------------------------------
def parse_edefter_xml(xml_content: bytes | str) -> pd.DataFrame:
    """
    Gelir İdaresi Başkanlığı (GİB) standardındaki e-Defter (Kebir / Yevmiye) XML'ini
    doğrudan çözümleyerek standart mizan tablosuna (DataFrame) dönüştürür.
    XBRL-GL (gl-cor, gl-bus) ve yerel GİB XML şemalarını destekler.
    """
    if isinstance(xml_content, str):
        xml_bytes = xml_content.encode("utf-8")
    else:
        xml_bytes = xml_content

    root = ET.fromstring(xml_bytes)

    # Namespace temizleme veya doğrudan tag sonunu arama
    records = []
    
    # 1. Senaryo: Standart GİB e-Kebir / Yevmiye XML (gl-cor / gl-bus veya defter düğümleri)
    accounts_found: dict[str, dict[str, Any]] = {}

    for elem in root.iter():
        tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
        
        # entryDetail veya entryItem veya kebir hesap dökümü
        if tag.lower() in ("entrydetail", "entryitem", "kayit", "hareket", "accountsummary", "kebirkaydi"):
            acc_num = None
            acc_desc = ""
            debit = 0.0
            credit = 0.0

            for child in elem.iter():
                ctag = (child.tag.split("}")[-1] if "}" in child.tag else child.tag).lower()
                text = (child.text or "").strip()
                if not text:
                    continue

                if ctag in ("accountmaindescription", "accountdescription", "hesapadi", "hesapaciklamasi", "accountdesc"):
                    acc_desc = text
                elif ctag in ("accountmainid", "accountid", "hesapkodu", "accountnumber", "hesapno"):
                    acc_num = text
                elif ctag in ("debitamount", "borctutari", "borc", "debit"):
                    try:
                        debit = float(text.replace(",", "."))
                    except ValueError:
                        pass
                elif ctag in ("creditamount", "alacaktutari", "alacak", "credit"):
                    try:
                        credit = float(text.replace(",", "."))
                    except ValueError:
                        pass

            if acc_num:
                if acc_num not in accounts_found:
                    accounts_found[acc_num] = {
                        "account_code": acc_num,
                        "account_name": acc_desc or f"Hesap {acc_num}",
                        "debit": 0.0,
                        "credit": 0.0,
                    }
                accounts_found[acc_num]["debit"] += debit
                accounts_found[acc_num]["credit"] += credit

    # 2. Senaryo: Eğer doğrudan mizan XML şeması ise
    if not accounts_found:
        for elem in root.iter():
            tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
            if tag.lower() in ("hesap", "account", "mizanrow", "mizankaydi", "record"):
                acc_code = elem.findtext(".//account_code") or elem.findtext(".//hesap_kodu") or elem.attrib.get("code") or elem.attrib.get("kodu")
                acc_name = elem.findtext(".//account_name") or elem.findtext(".//hesap_adi") or elem.attrib.get("name") or ""
                debit_str = elem.findtext(".//debit") or elem.findtext(".//borc") or elem.findtext(".//borc_bakiye") or "0"
                credit_str = elem.findtext(".//credit") or elem.findtext(".//alacak") or elem.findtext(".//alacak_bakiye") or "0"

                if acc_code:
                    try:
                        d_val = float(str(debit_str).replace(",", "."))
                        c_val = float(str(credit_str).replace(",", "."))
                    except ValueError:
                        d_val, c_val = 0.0, 0.0
                    
                    accounts_found[acc_code] = {
                        "account_code": str(acc_code).strip(),
                        "account_name": str(acc_name).strip(),
                        "debit": d_val,
                        "credit": c_val,
                    }

    if not accounts_found:
        raise ValueError("GİB e-Defter XML dosyasında geçerli hesap veya kebir kaydı bulunamadı.")

    for acc, data in accounts_found.items():
        deb = data["debit"]
        cred = data["credit"]
        bal = deb - cred
        records.append({
            "account_code": data["account_code"],
            "account_name": data["account_name"],
            "debit_total": deb,
            "credit_total": cred,
            "debit_balance": max(0.0, bal),
            "credit_balance": max(0.0, -bal),
        })

    df = pd.DataFrame(records)
    return df


# ---------------------------------------------------------------------------
# 2. SAP S/4HANA OData (API_TRIALBALANCE_SRV) Parser
# ---------------------------------------------------------------------------
def parse_sap_odata_payload(payload: dict[str, Any] | list[Any]) -> pd.DataFrame:
    """
    SAP S/4HANA OData 'API_TRIALBALANCE_SRV' ya da 'YY1_TRIALBALANCE' servisinden
    dönen JSON yükünü standart mizan DataFrame'ine dönüştürür.
    """
    items = []
    if isinstance(payload, dict):
        if "d" in payload and "results" in payload["d"]:
            items = payload["d"]["results"]
        elif "value" in payload:  # OData v4 format
            items = payload["value"]
        elif "TrialBalanceResult" in payload:
            items = payload["TrialBalanceResult"]
        else:
            items = [payload]
    elif isinstance(payload, list):
        items = payload

    records = []
    for it in items:
        acc_code = (
            it.get("GLAccount") or
            it.get("gl_account") or
            it.get("GLAccountNumber") or
            it.get("Account") or
            it.get("G_L_Account")
        )
        acc_name = (
            it.get("GLAccountName") or
            it.get("GLAccountLongText") or
            it.get("account_name") or
            it.get("Description") or
            ""
        )
        
        deb = float(it.get("DebitAmountInCoCodeCrcy") or it.get("DebitAmount") or it.get("debit") or 0.0)
        cred = float(it.get("CreditAmountInCoCodeCrcy") or it.get("CreditAmount") or it.get("credit") or 0.0)
        bal = float(it.get("EndingBalanceAmtInCoCodeCrcy") or it.get("AccumulatedBalance") or it.get("balance") or (deb - cred))

        if acc_code:
            records.append({
                "account_code": str(acc_code).strip(),
                "account_name": str(acc_name).strip(),
                "debit_total": deb,
                "credit_total": cred,
                "debit_balance": max(0.0, bal if bal > 0 else deb - cred),
                "credit_balance": max(0.0, -bal if bal < 0 else cred - deb),
            })

    if not records:
        raise ValueError("SAP OData payload'ında geçerli GLAccount kayıtları bulunamadı.")

    return pd.DataFrame(records)


# ---------------------------------------------------------------------------
# 3. Oracle NetSuite SuiteQL & SuiteTalk Parser
# ---------------------------------------------------------------------------
def parse_netsuite_payload(payload: dict[str, Any] | list[Any]) -> pd.DataFrame:
    """
    Oracle NetSuite SuiteQL REST query veya SuiteTalk Trial Balance
    JSON payload'ını standart mizan DataFrame'ine dönüştürür.
    """
    rows = []
    if isinstance(payload, dict):
        if "items" in payload:
            rows = payload["items"]
        elif "records" in payload:
            rows = payload["records"]
        else:
            rows = [payload]
    elif isinstance(payload, list):
        rows = payload

    records = []
    for r in rows:
        acc_code = (
            r.get("account_number") or
            r.get("acctnumber") or
            r.get("accountNumber") or
            r.get("account") or
            r.get("gl_code")
        )
        acc_name = (
            r.get("account_name") or
            r.get("acctname") or
            r.get("accountName") or
            r.get("name") or
            ""
        )
        deb = float(r.get("debit") or r.get("debit_amount") or r.get("amount_debit") or 0.0)
        cred = float(r.get("credit") or r.get("credit_amount") or r.get("amount_credit") or 0.0)
        net = float(r.get("balance") or r.get("net_amount") or (deb - cred))

        if acc_code:
            records.append({
                "account_code": str(acc_code).strip(),
                "account_name": str(acc_name).strip(),
                "debit_total": deb,
                "credit_total": cred,
                "debit_balance": max(0.0, net if net > 0 else deb - cred),
                "credit_balance": max(0.0, -net if net < 0 else cred - deb),
            })

    if not records:
        raise ValueError("Oracle NetSuite payload'ında geçerli muhasebe hesap kayıtları bulunamadı.")

    return pd.DataFrame(records)


# ---------------------------------------------------------------------------
# 4. Ana Ingestion ve Dönüştürme Yöneticisi (Dispatcher)
# ---------------------------------------------------------------------------
def process_ingestion_payload(
    raw_data: Union[bytes, str, dict, list],
    source_type: str = "auto",
    filename: str = "mizan.xlsx",
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Gelen herhangi bir ham ERP/e-Defter verisini çözer ve standart
    DataFrame ile kaynak metadata'sını döner.
    """
    meta: Dict[str, Any] = {
        "detected_source": source_type,
        "record_count": 0,
        "is_automated": True,
        "erp_badge": "Generic Ingestion",
    }

    # 1. XML ise (GİB e-Defter)
    is_xml = (
        source_type in ("edefter_xml", "gib_edefter", "xml") or
        filename.lower().endswith(".xml") or
        (isinstance(raw_data, (bytes, str)) and (b"<?xml" in raw_data[:200] if isinstance(raw_data, bytes) else "<?xml" in raw_data[:200]))
    )

    if is_xml:
        df = parse_edefter_xml(raw_data)
        meta["detected_source"] = "GİB e-Defter (Kebir XML)"
        meta["erp_badge"] = "GİB e-Defter XML"
        meta["record_count"] = len(df)
        return df, meta

    # 2. JSON ise (SAP OData veya NetSuite)
    if isinstance(raw_data, (dict, list)) or (isinstance(raw_data, (bytes, str)) and filename.lower().endswith(".json")):
        if isinstance(raw_data, (bytes, str)):
            parsed_json = json.loads(raw_data)
        else:
            parsed_json = raw_data

        if source_type == "sap_odata" or (isinstance(parsed_json, dict) and ("GLAccount" in str(parsed_json) or "TrialBalance" in str(parsed_json))):
            df = parse_sap_odata_payload(parsed_json)
            meta["detected_source"] = "SAP S/4HANA OData (API_TRIALBALANCE_SRV)"
            meta["erp_badge"] = "SAP S/4HANA OData"
            meta["record_count"] = len(df)
            return df, meta
        elif source_type == "netsuite" or (isinstance(parsed_json, dict) and ("acctnumber" in str(parsed_json) or "SuiteQL" in str(parsed_json))):
            df = parse_netsuite_payload(parsed_json)
            meta["detected_source"] = "Oracle NetSuite SuiteQL"
            meta["erp_badge"] = "Oracle NetSuite"
            meta["record_count"] = len(df)
            return df, meta

    # 3. Excel veya CSV ise erp_standardizer üzerinden geçir
    if isinstance(raw_data, bytes):
        if filename.lower().endswith((".xlsx", ".xls")):
            raw_df = pd.read_excel(io.BytesIO(raw_data))
        else:
            try:
                raw_df = pd.read_csv(io.BytesIO(raw_data), encoding="utf-8")
            except Exception:
                raw_df = pd.read_csv(io.BytesIO(raw_data), encoding="latin1")

        role, role_conf, mapping = classify_dataframe(raw_df, filename, "Sheet1")
        erp_key, erp_badge, erp_conf = detect_erp_signature([str(c) for c in raw_df.columns], "", filename)
        
        std_df = pd.DataFrame()
        for c_field, s_col in mapping.items():
            if s_col in raw_df.columns:
                std_df[c_field] = raw_df[s_col]
        if std_df.empty or "account_code" not in std_df.columns:
            std_df = raw_df

        meta["detected_source"] = f"{erp_badge} ({role})"
        meta["erp_badge"] = erp_badge
        meta["record_count"] = len(std_df)
        return std_df, meta

    raise ValueError(f"Desteklenmeyen veri yükü biçimi: {type(raw_data)}")


# ---------------------------------------------------------------------------
# 5. ERP & e-Defter Simülasyon Veri Üreticisi (Demo & Test)
# ---------------------------------------------------------------------------
def generate_mock_erp_payload(source: str = "sap") -> Tuple[Union[bytes, str, dict], str, str]:
    """
    Kullanıcıya veya yatırımcıya canlı ERP senkronizasyonunu anında gösterebilmek için
    gerçekçi SAP S/4HANA OData, Oracle NetSuite veya GİB e-Defter Kebir verisi üretir.
    Dönüş: (payload, source_type, filename)
    """
    src = source.lower()
    
    if "sap" in src:
        data = {
            "d": {
                "results": [
                    {"GLAccount": "100", "GLAccountLongText": "Kasa Hesabı", "DebitAmountInCoCodeCrcy": 250000.0, "CreditAmountInCoCodeCrcy": 0.0, "EndingBalanceAmtInCoCodeCrcy": 250000.0},
                    {"GLAccount": "102", "GLAccountLongText": "Bankalar", "DebitAmountInCoCodeCrcy": 1450000.0, "CreditAmountInCoCodeCrcy": 0.0, "EndingBalanceAmtInCoCodeCrcy": 1450000.0},
                    {"GLAccount": "120", "GLAccountLongText": "Alıcılar (Ticari Müşteriler)", "DebitAmountInCoCodeCrcy": 4200000.0, "CreditAmountInCoCodeCrcy": 0.0, "EndingBalanceAmtInCoCodeCrcy": 4200000.0},
                    {"GLAccount": "150", "GLAccountLongText": "İlk Madde ve Malzeme", "DebitAmountInCoCodeCrcy": 1800000.0, "CreditAmountInCoCodeCrcy": 0.0, "EndingBalanceAmtInCoCodeCrcy": 1800000.0},
                    {"GLAccount": "153", "GLAccountLongText": "Ticari Mallar", "DebitAmountInCoCodeCrcy": 950000.0, "CreditAmountInCoCodeCrcy": 0.0, "EndingBalanceAmtInCoCodeCrcy": 950000.0},
                    {"GLAccount": "253", "GLAccountLongText": "Tesis Makine ve Cihazlar", "DebitAmountInCoCodeCrcy": 5500000.0, "CreditAmountInCoCodeCrcy": 0.0, "EndingBalanceAmtInCoCodeCrcy": 5500000.0},
                    {"GLAccount": "257", "GLAccountLongText": "Birikmiş Amortismanlar (-)", "DebitAmountInCoCodeCrcy": 0.0, "CreditAmountInCoCodeCrcy": 1150000.0, "EndingBalanceAmtInCoCodeCrcy": -1150000.0},
                    {"GLAccount": "300", "GLAccountLongText": "Kısa Vadeli Banka Kredileri", "DebitAmountInCoCodeCrcy": 0.0, "CreditAmountInCoCodeCrcy": 2300000.0, "EndingBalanceAmtInCoCodeCrcy": -2300000.0},
                    {"GLAccount": "320", "GLAccountLongText": "Satıcılar (Tedarikçiler)", "DebitAmountInCoCodeCrcy": 0.0, "CreditAmountInCoCodeCrcy": 2600000.0, "EndingBalanceAmtInCoCodeCrcy": -2600000.0},
                    {"GLAccount": "500", "GLAccountLongText": "Ödenmiş Sermaye", "DebitAmountInCoCodeCrcy": 0.0, "CreditAmountInCoCodeCrcy": 6000000.0, "EndingBalanceAmtInCoCodeCrcy": -6000000.0},
                    {"GLAccount": "600", "GLAccountLongText": "Yurtiçi Satışlar", "DebitAmountInCoCodeCrcy": 0.0, "CreditAmountInCoCodeCrcy": 14500000.0, "EndingBalanceAmtInCoCodeCrcy": -14500000.0},
                    {"GLAccount": "610", "GLAccountLongText": "Satış İadeleri (-)", "DebitAmountInCoCodeCrcy": 250000.0, "CreditAmountInCoCodeCrcy": 0.0, "EndingBalanceAmtInCoCodeCrcy": 250000.0},
                    {"GLAccount": "621", "GLAccountLongText": "Satılan Mallar Maliyeti (-)", "DebitAmountInCoCodeCrcy": 9800000.0, "CreditAmountInCoCodeCrcy": 0.0, "EndingBalanceAmtInCoCodeCrcy": 9800000.0},
                    {"GLAccount": "760", "GLAccountLongText": "Pazarlama Satış Dağıtım Giderleri (-)", "DebitAmountInCoCodeCrcy": 1650000.0, "CreditAmountInCoCodeCrcy": 0.0, "EndingBalanceAmtInCoCodeCrcy": 1650000.0},
                    {"GLAccount": "770", "GLAccountLongText": "Genel Yönetim Giderleri (-)", "DebitAmountInCoCodeCrcy": 1250000.0, "CreditAmountInCoCodeCrcy": 0.0, "EndingBalanceAmtInCoCodeCrcy": 1250000.0},
                    {"GLAccount": "780", "GLAccountLongText": "Finansman Giderleri (-)", "DebitAmountInCoCodeCrcy": 950000.0, "CreditAmountInCoCodeCrcy": 0.0, "EndingBalanceAmtInCoCodeCrcy": 950000.0}
                ]
            }
        }
        return data, "sap_odata", "sap_s4hana_trialbalance.json"

    elif "net" in src or "suite" in src or "oracle" in src:
        data = {
            "items": [
                {"account_number": "100", "account_name": "Nakit ve Kasa", "debit": 320000.0, "credit": 0.0, "balance": 320000.0},
                {"account_number": "102", "account_name": "Vadesiz Ticari Banka", "debit": 1850000.0, "credit": 0.0, "balance": 1850000.0},
                {"account_number": "120", "account_name": "Müşteri Alacakları (AR)", "debit": 5100000.0, "credit": 0.0, "balance": 5100000.0},
                {"account_number": "153", "account_name": "Mamul & Ticari Mallar", "debit": 2900000.0, "credit": 0.0, "balance": 2900000.0},
                {"account_number": "253", "account_name": "Tesis ve Ekipmanlar", "debit": 6200000.0, "credit": 0.0, "balance": 6200000.0},
                {"account_number": "257", "account_name": "Kümülatif Amortisman (-)", "debit": 0.0, "credit": 1400000.0, "balance": -1400000.0},
                {"account_number": "300", "account_name": "Finansal Borçlar (Banka)", "debit": 0.0, "credit": 2900000.0, "balance": -2900000.0},
                {"account_number": "320", "account_name": "Tedarikçi Borçları (AP)", "debit": 0.0, "credit": 3200000.0, "balance": -3200000.0},
                {"account_number": "500", "account_name": "Ana Sermaye", "debit": 0.0, "credit": 7500000.0, "balance": -7500000.0},
                {"account_number": "600", "account_name": "Hasılat (Ciro)", "debit": 0.0, "credit": 18200000.0, "balance": -18200000.0},
                {"account_number": "610", "account_name": "İadeler ve İndirimler", "debit": 350000.0, "credit": 0.0, "balance": 350000.0},
                {"account_number": "621", "account_name": "Satışların Maliyeti (COGS)", "debit": 12100000.0, "credit": 0.0, "balance": 12100000.0},
                {"account_number": "760", "account_name": "Pazarlama ve Dağıtım", "debit": 1900000.0, "credit": 0.0, "balance": 1900000.0},
                {"account_number": "770", "account_name": "Yönetim Giderleri (OPEX)", "debit": 1450000.0, "credit": 0.0, "balance": 1450000.0},
                {"account_number": "780", "account_name": "Kredi ve Finansman Gideri", "debit": 1100000.0, "credit": 0.0, "balance": 1100000.0}
            ]
        }
        return data, "netsuite", "netsuite_suiteql_export.json"

    else:  # e-Defter Kebir XML (GİB Standart XBRL-GL formatı)
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<gl-cor:accountingEntries xmlns:gl-cor="http://www.xbrl.org/int/gl/cor/2006-10-25" xmlns:gl-bus="http://www.xbrl.org/int/gl/bus/2006-10-25">
  <gl-cor:documentInfo>
    <gl-cor:entriesType>kebir</gl-cor:entriesType>
    <gl-cor:creationDate>2026-03-31</gl-cor:creationDate>
  </gl-cor:documentInfo>
  <gl-cor:entryHeader>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>100</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Kasa Hesabı (TL/Döviz)</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>180000.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>0.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>102</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Bankalar Mevduat</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>1150000.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>0.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>120</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Alıcılar Cari Hesabı</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>3600000.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>0.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>153</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Ticari Mallar Deposu</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>2100000.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>0.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>253</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Tesis Makine Cihaz</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>4500000.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>0.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>257</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Birikmiş Amortismanlar</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>0.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>900000.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>300</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Kısa Vadeli Krediler</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>0.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>1950000.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>320</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Satıcılar Tedarikçi Cari</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>0.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>2200000.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>500</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Sermaye</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>0.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>5100000.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>600</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Yurtiçi Satış Gelirleri</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>0.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>12800000.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>610</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Satış İadeleri</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>200000.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>0.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>621</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Satılan Mal Maliyeti</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>8500000.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>0.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>760</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Pazarlama Giderleri</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>1400000.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>0.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>770</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Genel Yönetim Giderleri</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>1100000.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>0.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
    <gl-cor:entryDetail>
      <gl-cor:accountMainID>780</gl-cor:accountMainID>
      <gl-cor:accountMainDescription>Finansman Giderleri</gl-cor:accountMainDescription>
      <gl-cor:debitAmount>800000.00</gl-cor:debitAmount>
      <gl-cor:creditAmount>0.00</gl-cor:creditAmount>
    </gl-cor:entryDetail>
  </gl-cor:entryHeader>
</gl-cor:accountingEntries>"""
        return xml_content.encode("utf-8"), "edefter_xml", "gib_edefter_kebir_2026.xml"

