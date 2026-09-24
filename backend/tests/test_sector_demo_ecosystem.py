import sys
from pathlib import Path
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import app
from finance_engine.benchmarking_engine import resolve_sector, SECTOR_BANDS, SECTOR_WORKING_CAPITAL_BENCHMARKS

client = TestClient(app)

def test_resolve_sector_aliases():
    assert resolve_sector("uretim_sanayi") == "Üretim / Sanayi"
    assert resolve_sector("imalat") == "Üretim / Sanayi"
    assert resolve_sector("toptan_ticaret") == "Toptan Dağıtım / Ticaret"
    assert resolve_sector("perakende_eticaret") == "Perakende / Ticaret"
    assert resolve_sector("hizmet_yazilim") == "Hizmet"
    assert resolve_sector("insaat_taahhut") == "İnşaat / Taahhüt"
    assert resolve_sector("saglik_medikal") == "Sağlık / Medikal"
    assert resolve_sector("lojistik_tasimacilik") == "Lojistik / Taşımacılık"
    assert resolve_sector(None) == "Genel"
    assert resolve_sector("Bilinmeyen Sektör") == "Genel"

def test_list_sector_demos_endpoint():
    resp = client.get("/api/sample/sectors")
    assert resp.status_code == 200
    data = resp.json()
    assert "sectors" in data
    sectors = data["sectors"]
    assert len(sectors) == 7
    sector_ids = {s["id"] for s in sectors}
    assert sector_ids == {
        "uretim_sanayi", "toptan_ticaret", "perakende_eticaret",
        "hizmet_yazilim", "insaat_taahhut", "saglik_medikal", "lojistik_tasimacilik"
    }

@pytest.mark.parametrize("sector_id", [
    "uretim_sanayi",
    "toptan_ticaret",
    "perakende_eticaret",
    "hizmet_yazilim",
    "insaat_taahhut",
    "saglik_medikal",
    "lojistik_tasimacilik",
])
def test_run_sector_demo_end_to_end(sector_id):
    resp = client.post(f"/api/sample/run-sector/{sector_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data.get("sector_demo_active") is True
    assert data.get("account_count") >= 50
    bp = data.get("business_partner", {})
    assert bp.get("health_score") is not None
    assert 0 <= bp.get("health_score") <= 100
    # Benchmarking validation
    bm = bp.get("benchmarking", {})
    assert bm.get("sector") in SECTOR_BANDS
    # Core statements presence
    stmts = data.get("statements", {})
    assert "profit_and_loss" in stmts
    assert "balance_sheet" in stmts
    assert "kpis" in stmts

def test_get_sector_sample_file():
    resp = client.get("/api/sample/sector/uretim_sanayi/mizan_cur")
    assert resp.status_code == 200
    assert len(resp.content) > 1000
    assert resp.headers.get("content-type") == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

def test_invalid_sector_demo():
    resp = client.post("/api/sample/run-sector/gecersiz_sektor")
    assert resp.status_code == 404
