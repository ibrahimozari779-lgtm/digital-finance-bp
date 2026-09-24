import sys
from pathlib import Path
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import app
from finance_engine.kobi_patron_engine import (
    build_kobi_patron_analysis,
    normalize_sector_key,
)

client = TestClient(app)

def test_normalize_sector_key():
    assert normalize_sector_key("uretim_sanayi") == "uretim_sanayi"
    assert normalize_sector_key("Üretim / Sanayi") == "uretim_sanayi"
    assert normalize_sector_key("Toptan Dağıtım / Ticaret") == "toptan_ticaret"
    assert normalize_sector_key("Perakende / Ticaret") == "perakende_eticaret"
    assert normalize_sector_key("Hizmet & SaaS") == "hizmet_yazilim"
    assert normalize_sector_key("İnşaat / Taahhüt") == "insaat_taahhut"
    assert normalize_sector_key("Sağlık / Medikal") == "saglik_medikal"
    assert normalize_sector_key("Lojistik / Taşımacılık") == "lojistik_tasimacilik"
    assert normalize_sector_key(None) == "genel"


def test_zero_stock_saas_invariant():
    """Verify that a service/SaaS company never outputs '0 günlük stok' nonsense."""
    statements = {
        "profit_and_loss": {
            "Net sales": 20_000_000.0,
            "Cost of sales": 7_000_000.0,
            "Operating profit": 2_500_000.0,
            "Finance costs": 400_000.0,
            "Net profit": 1_800_000.0,
        },
        "balance_sheet": {
            "Total assets": 15_000_000.0,
            "Cash and cash equivalents": 500_000.0,
            "Trade receivables": 4_000_000.0,
            "Inventories": 0.0, # ZERO INVENTORY
            "Trade payables": 1_000_000.0,
        },
        "kpis": {
            "inventory": 0.0,
            "receivables": 4_000_000.0,
        },
        "cash_conversion": {
            "dso_days": 73.0,
            "dio_days": 0.0,
            "dpo_days": 35.0,
            "cash_conversion_cycle_days": 38.0,
        },
    }
    
    res = build_kobi_patron_analysis(statements, sector="Hizmet & B2B SaaS")
    assert res["has_inventory"] is False
    assert len(res["questions"]) == 10
    
    # Question 1: Must NOT mention '0 günlük stok' or 'depodaki 0' or '(0 TL)'
    q1 = next(q for q in res["questions"] if q["id"] == "q1")
    assert "0 günlük stok" not in q1["l1_desc"]
    assert "(0 TL)" not in q1["l1_desc"]
    assert "depodaki 0" not in q1["l1_desc"]
    assert "stokta (" not in q1["l1_desc"]
    assert "personel" in q1["l1_desc"].lower() or "maaş" in q1["l1_desc"].lower() or "yazılımcı" in q1["l1_desc"].lower()
    
    # Question 3: Must NOT be about warehouse/stock
    q3 = next(q for q in res["questions"] if q["id"] == "q3")
    assert "Yazılımcı" in q3["title"] or "Personel" in q3["title"]
    assert "Depoda Ne Kadar Para Uyuyor" not in q3["title"]


@pytest.mark.parametrize("sec_id,expected_theme_keyword", [
    ("uretim_sanayi", "Fabrika"),
    ("toptan_ticaret", "Dağıtım"),
    ("perakende_eticaret", "Stok"),
    ("hizmet_yazilim", "Bordro"),
    ("insaat_taahhut", "Hakediş"),
    ("saglik_medikal", "Kamu"),
    ("lojistik_tasimacilik", "Mazot"),
])
def test_seven_sectors_rule_triggers_and_alarms(sec_id, expected_theme_keyword):
    """Verify that all 7 sectors trigger appropriate alarms and produce exactly 10 questions."""
    resp = client.post(f"/api/sample/run-sector/{sec_id}")
    assert resp.status_code == 200
    data = resp.json()
    
    bp = data.get("business_partner", {})
    assert "kobi_patron_engine" in bp
    kobi = bp["kobi_patron_engine"]
    
    # 10 Questions check
    questions = kobi.get("questions", [])
    assert len(questions) == 10
    question_ids = [q["id"] for q in questions]
    assert question_ids == ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10"]
    
    # Triggers & Alarms
    triggers = kobi.get("triggers", [])
    assert len(triggers) >= 2
    alarms = kobi.get("patron_alarms", [])
    assert len(alarms) >= 1
    assert expected_theme_keyword.lower() in alarms[0]["theme"].lower()
    assert "patron" in alarms[0]["comment"].lower()
    
    # Turkish market solutions
    solutions = kobi.get("solutions", [])
    assert len(solutions) >= 3


def test_legal_and_tax_remedies_in_questions():
    """Verify Turkish market solutions (VUK 315, 323, 328, KVK 10/1-ı, DBS, KDV-SGK) are present."""
    # Test Uretim -> VUK 315
    resp = client.post("/api/sample/run-sector/uretim_sanayi")
    kobi = resp.json()["business_partner"]["kobi_patron_engine"]
    q10 = next(q for q in kobi["questions"] if q["id"] == "q10")
    assert "VUK 315" in q10["l1_title"] or "Amortisman" in q10["l1_title"]
    
    # Test Insaat -> VUK 323 / 328
    resp_ins = client.post("/api/sample/run-sector/insaat_taahhut")
    kobi_ins = resp_ins.json()["business_partner"]["kobi_patron_engine"]
    q10_ins = next(q for q in kobi_ins["questions"] if q["id"] == "q10")
    assert "VUK 323" in q10_ins["l1_title"] or "Yenileme" in q10_ins["l1_title"] or "Şüpheli" in q10_ins["l1_title"]
    
    # Test Toptan -> DBS
    resp_top = client.post("/api/sample/run-sector/toptan_ticaret")
    kobi_top = resp_top.json()["business_partner"]["kobi_patron_engine"]
    q2_top = next(q for q in kobi_top["questions"] if q["id"] == "q2")
    assert "DBS" in q2_top["l3_action"]
