import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from finance_engine.european_accounting_standardizer import (
    detect_coa_standard,
    map_account_to_canonical,
    analyze_european_chart,
    COA_STANDARDS_METADATA,
)
from finance_engine.erp_standardizer import detect_erp_signature


def test_detect_datev_skr03():
    codes = ["1200", "1400", "1600", "8400", "3400", "4100"]
    names = ["Bank", "Forderungen aus L+L", "Verbindlichkeiten", "Erlöse 19% USt", "Wareneingang 19%", "Löhne und Gehälter"]
    std_code, meta, conf = detect_coa_standard(codes, names)
    assert std_code == "DE_SKR03"
    assert "DATEV" in meta["name"]
    assert conf >= 0.70


def test_detect_french_pcg():
    codes = ["411100", "401100", "512000", "707000", "607000", "641000"]
    names = ["Clients", "Fournisseurs", "Banque", "Ventes de marchandises", "Achats de marchandises", "Rémunérations du personnel"]
    std_code, meta, conf = detect_coa_standard(codes, names)
    assert std_code == "FR_PCG"
    assert "PCG" in meta["name"]
    assert conf >= 0.70


def test_detect_spanish_pgc():
    codes = ["430000", "400000", "572000", "700000", "600000", "640000"]
    names = ["Clientes", "Proveedores", "Bancos", "Ventas de mercaderías", "Compras de mercaderías", "Sueldos y salarios"]
    std_code, meta, conf = detect_coa_standard(codes, names)
    assert std_code == "ES_PGC"
    assert "PGC" in meta["name"]
    assert conf >= 0.70


def test_detect_turkish_tdhp():
    codes = ["100", "102", "120", "153", "320", "500", "600", "621"]
    names = ["Kasa", "Bankalar", "Alıcılar", "Ticari Mallar", "Satıcılar", "Sermaye", "Yurtiçi Satışlar", "Satılan Ticari Mallar Maliyeti"]
    std_code, meta, conf = detect_coa_standard(codes, names)
    assert std_code == "TR_TDHP"
    assert "TDHP" in meta["name"]


def test_canonical_mapping():
    # DATEV SKR03 AR
    m_ar = map_account_to_canonical("1400", "Forderungen", standard="DE_SKR03")
    assert m_ar["category"] == "ASSETS_CURRENT"
    assert m_ar["sub_category"] == "ACCOUNTS_RECEIVABLE"

    # DATEV SKR03 Revenue
    m_rev = map_account_to_canonical("8400", "Erlöse 19%", standard="DE_SKR03")
    assert m_rev["category"] == "REVENUE"
    assert m_rev["sub_category"] == "NET_SALES"

    # French PCG Supplier
    m_ap = map_account_to_canonical("401000", "Fournisseurs", standard="FR_PCG")
    assert m_ap["category"] == "LIABILITIES_CURRENT"
    assert m_ap["sub_category"] == "ACCOUNTS_PAYABLE"


def test_analyze_chart_report():
    accounts = [
        {"account_code": "1200", "account_name": "Bank"},
        {"account_code": "1400", "account_name": "Forderungen"},
        {"account_code": "1600", "account_name": "Verbindlichkeiten"},
        {"account_code": "8400", "account_name": "Erlöse 19%"},
    ]
    report = analyze_european_chart(accounts)
    assert report["status"] == "PASS"
    assert report["is_european"] is True
    assert report["detected_standard"] == "DE_SKR03"


def test_european_erp_signatures():
    erp, badge, conf = detect_erp_signature(["konto", "kontobezeichnung", "soll", "haben", "saldo"])
    assert erp == "datev"
    assert "DATEV" in badge

    erp_fr, badge_fr, _ = detect_erp_signature(["compte", "libelle compte", "debit", "credit", "solde"])
    assert erp_fr == "pennylane"
