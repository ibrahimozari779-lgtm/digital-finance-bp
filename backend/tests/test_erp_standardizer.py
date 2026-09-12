import io
from pathlib import Path
import sys
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from finance_engine.erp_standardizer import detect_erp_signature, inspect_file_structure, CANONICAL_SCHEMAS
from app import app


def test_erp_signature_detection_logo():
    cols = ["HESAP KODU", "HESAP AÇIKLAMASI", "BORÇ", "ALACAK", "BORÇ BAKİYE", "ALACAK BAKİYE"]
    erp_key, badge, conf = detect_erp_signature(cols, "Logo Tiger 3 Mizan Raporu", "mizan_logo.xlsx")
    assert erp_key == "logo"
    assert "Logo" in badge
    assert conf >= 0.70


def test_erp_signature_detection_luca():
    cols = ["Hesap Kodu", "Hesap Adı", "Borç Tutarı", "Alacak Tutarı", "Borç Kalan", "Alacak Kalan"]
    erp_key, badge, conf = detect_erp_signature(cols, "TÜRMOB Luca Mali Müşavir Paketi Mizan", "luca_mizan.xlsx")
    assert erp_key == "luca"
    assert "Luca" in badge
    assert conf >= 0.70


def test_erp_signature_detection_mikro():
    cols = ["Hesap No", "Hesap İsmi", "Borç Toplam", "Alacak Toplam", "Borç Bakiye", "Alacak Bakiye", "Sorumluluk Merkezi"]
    erp_key, badge, conf = detect_erp_signature(cols, "Mikro Fly V16 Mizan Dökümü", "mikro_rapor.xlsx")
    assert erp_key == "mikro"
    assert "Mikro" in badge
    assert conf >= 0.70


def test_erp_signature_detection_netsis():
    cols = ["HESAP_KODU", "HESAP_ADI", "B_BAKIYE", "A_BAKIYE", "BAKIYE", "CARI_KODU"]
    erp_key, badge, conf = detect_erp_signature(cols, "Netsis Entegre Mizan Dökümü", "netsis.csv")
    assert erp_key == "netsis"
    assert "Netsis" in badge
    assert conf >= 0.60


def test_erp_signature_detection_sap():
    cols = ["G/L Account", "Account Long Text", "Debit", "Credit", "Accumulated Balance", "Posting Date"]
    erp_key, badge, conf = detect_erp_signature(cols, "SAP S/4HANA Trial Balance Report", "sap_gl.xlsx")
    assert erp_key == "sap"
    assert "SAP" in badge
    assert conf >= 0.70


def test_erp_signature_detection_generic():
    cols = ["Code", "Description", "Value", "Notes"]
    erp_key, badge, conf = detect_erp_signature(cols, "Custom Sheet", "custom.csv")
    assert erp_key == "generic"
    assert "Standart" in badge


def test_inspect_file_structure_csv():
    csv_data = (
        "Hesap Kodu;Hesap Adı;Borç Bakiye;Alacak Bakiye\n"
        "100;Kasa;50000;0\n"
        "102;Bankalar;1500000;0\n"
        "120;Alıcılar;2500000;0\n"
        "320;Satıcılar;0;1200000\n"
    ).encode("utf-8-sig")

    res = inspect_file_structure(csv_data, "mizan_test.csv")
    assert res["status"] == "success"
    assert res["filename"] == "mizan_test.csv"
    primary = res["primary"]
    assert primary is not None
    assert primary["role"] == "finance"
    assert primary["total_rows"] == 4
    assert len(primary["mapped_fields"]) >= 2
    assert primary["is_ready"] is True
    assert len(primary["preview_rows"]) == 4


def test_inspect_file_structure_sales():
    csv_data = (
        "Tarih;Fatura No;Müşteri Adı;Ürün Adı;Miktar;Net Satış\n"
        "01.01.2025;FTR-001;ABC A.Ş.;Endüstriyel Vana;10;150000\n"
        "02.01.2025;FTR-002;XYZ Ltd.;Pompa;5;85000\n"
    ).encode("utf-8-sig")

    res = inspect_file_structure(csv_data, "satis_listesi.csv")
    assert res["status"] == "success"
    primary = res["primary"]
    assert primary["role"] == "sales"
    assert primary["is_ready"] is True


def test_api_inspect_schemas():
    client = TestClient(app)
    resp = client.get("/api/inspect/schemas")
    assert resp.status_code == 200
    data = resp.json()
    assert "finance" in data
    assert "sales" in data
    assert "ar_aging" in data
    assert "inventory" in data


def test_api_inspect_endpoint():
    client = TestClient(app)
    csv_bytes = (
        "HESAP KODU;HESAP AÇIKLAMASI;BORÇ BAKİYE;ALACAK BAKİYE\n"
        "100;Kasa Hesabı;25000;0\n"
        "120;Müşteriler Hesabı;85000;0\n"
    ).encode("utf-8-sig")
    files = {"files": ("logo_tiger_mizan.csv", io.BytesIO(csv_bytes), "text/csv")}
    resp = client.post("/api/inspect", files=files)
    assert resp.status_code == 200
    body = resp.json()
    assert body["count"] == 1
    assert "Logo" in body["erp_badge"]
    assert body["role"] == "finance"
    assert len(body["files"]) == 1
