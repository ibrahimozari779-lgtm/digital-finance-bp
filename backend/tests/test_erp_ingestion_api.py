import pytest
from fastapi.testclient import TestClient
from app import app
from finance_engine import (
    validate_api_key,
    parse_edefter_xml,
    parse_sap_odata_payload,
    parse_netsuite_payload,
    generate_mock_erp_payload,
    process_ingestion_payload,
)


@pytest.fixture
def client():
    return TestClient(app)


def test_api_key_validation():
    # Valid default keys
    assert validate_api_key("live_sec_cfo_demo_893247") is not None
    assert validate_api_key("Bearer sap_prod_token_991823") is not None
    assert validate_api_key("test_key_custom_tenant") is not None

    # Invalid keys
    assert validate_api_key("") is None
    assert validate_api_key(None) is None
    assert validate_api_key("completely_invalid_key_xyz") is None


def test_edefter_xml_parser():
    xml_data, src, fn = generate_mock_erp_payload("edefter")
    df = parse_edefter_xml(xml_data)
    assert not df.empty
    assert "account_code" in df.columns
    assert "debit_balance" in df.columns
    assert "credit_balance" in df.columns
    # Check TDHP accounts exist
    codes = df["account_code"].tolist()
    assert "100" in codes
    assert "120" in codes
    assert "600" in codes


def test_sap_odata_parser():
    sap_data, src, fn = generate_mock_erp_payload("sap")
    df = parse_sap_odata_payload(sap_data)
    assert not df.empty
    assert "account_code" in df.columns
    codes = df["account_code"].tolist()
    assert "100" in codes
    assert "600" in codes


def test_netsuite_parser():
    ns_data, src, fn = generate_mock_erp_payload("netsuite")
    df = parse_netsuite_payload(ns_data)
    assert not df.empty
    assert "account_code" in df.columns
    codes = df["account_code"].tolist()
    assert "100" in codes
    assert "600" in codes


def test_connectors_status_endpoint(client):
    res = client.get("/api/v1/connectors/status")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "online"
    assert len(data["supported_connectors"]) >= 4
    connector_ids = [c["id"] for c in data["supported_connectors"]]
    assert "edefter_xml" in connector_ids
    assert "sap_odata" in connector_ids
    assert "netsuite" in connector_ids
    assert "desktop_agent" in connector_ids


def test_connectors_simulate_sap(client):
    res = client.post("/api/v1/connectors/simulate", json={"connector": "sap", "sector": "URETIM"})
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert data["simulated_connector"] == "sap"
    assert "business_partner" in data
    assert "statements" in data
    assert data["account_count"] > 10


def test_connectors_simulate_edefter_xml(client):
    res = client.post("/api/v1/connectors/simulate", json={"connector": "edefter_xml", "sector": "TICARET"})
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert data["simulated_connector"] == "edefter_xml"
    assert "business_partner" in data
    assert data["statements"]["profit_and_loss"]["Net sales"] > 0


def test_ingest_mizan_json_sap(client):
    sap_payload, _, _ = generate_mock_erp_payload("sap")
    res = client.post(
        "/api/v1/ingest/mizan",
        json={"payload": sap_payload, "source_type": "sap_odata", "sector": "GENEL"},
        headers={"X-API-KEY": "sap_prod_token_991823"},
    )
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert data["automated_ingestion"] is True
    assert data["tenant"]["company_id"] == "sap_enterprise"
    assert data["account_count"] > 10


def test_ingest_mizan_edefter_xml(client):
    xml_data, _, _ = generate_mock_erp_payload("edefter")
    res = client.post(
        "/api/v1/ingest/mizan",
        content=xml_data,
        headers={"Content-Type": "application/xml", "X-API-KEY": "edefter_sovos_key_77123"},
    )
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert data["automated_ingestion"] is True
    assert data["statements"]["profit_and_loss"]["Revenue"] > 0


def test_ingest_mizan_invalid_api_key(client):
    res = client.post(
        "/api/v1/ingest/mizan",
        json={"payload": {}},
        headers={"X-API-KEY": "hacker_key_999"},
    )
    assert res.status_code == 401


def test_connector_configs_list_and_save(client):
    # 1. List configs
    res = client.get("/api/v1/connectors/configs")
    assert res.status_code == 200
    data = res.json()
    assert "configs" in data

    # 2. Save a new config
    save_res = client.post(
        "/api/v1/connectors/configs",
        json={
            "provider": "uyumsoft",
            "api_key": "uyum_live_sec_token_9918234",
            "endpoint_url": "https://api.efatura.entegrator.com/edefter/v1",
            "sync_frequency": "daily"
        }
    )
    assert save_res.status_code == 200
    saved = save_res.json()
    assert saved["status"] == "success"
    assert saved["config"]["provider"] == "uyumsoft"
    # Verify API key is masked (no plain text exposure)
    assert saved["config"]["api_key_masked"].startswith("uyum***")

