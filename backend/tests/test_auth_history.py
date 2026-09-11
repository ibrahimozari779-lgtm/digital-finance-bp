"""Faz 1 — Auth + kalıcı geçmiş regresyon testleri.

Bu dosya, kullanıcı kaydı/girişi, analiz geçmişinin kaydedilmesi/listelenmesi
ve en kritik güvenlik özelliği olan kullanıcılar-arası izolasyonun (tenant
isolation) bozulmadığını garanti eder. Her test kendi izole SQLite dosyasını
kullanır ki testler birbirini etkilemesin ve gerçek local.db'ye dokunmasın.
"""
from __future__ import annotations

import os
import sys
import uuid

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def _fresh_client(tmp_path):
    """Each test gets a brand-new SQLite file via DATABASE_URL so tests never
    share state and never touch the real backend/local.db."""
    db_file = tmp_path / f"test_{uuid.uuid4().hex}.db"
    os.environ["DATABASE_URL"] = f"sqlite:///{db_file}"

    # Re-import db/app fresh so the new DATABASE_URL is picked up (db.py
    # reads it once at module import time).
    for mod in ["db", "auth", "app"]:
        sys.modules.pop(mod, None)
    import app as app_module
    from fastapi.testclient import TestClient
    return TestClient(app_module.app)


def _unique_email() -> str:
    return f"user_{uuid.uuid4().hex[:10]}@ornek.com"


def test_register_then_login_returns_usable_token(tmp_path):
    c = _fresh_client(tmp_path)
    email = _unique_email()
    r = c.post("/api/auth/register", json={"email": email, "password": "sifre123", "company_name": "Test A.Ş."})
    assert r.status_code == 200
    token = r.json()["token"]

    r = c.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.json()["email"] == email

    r = c.post("/api/auth/login", json={"email": email, "password": "sifre123"})
    assert r.status_code == 200
    assert r.json()["token"]


def test_duplicate_registration_is_rejected():
    pass  # covered indirectly below with a shared client


def test_wrong_password_and_missing_token_are_rejected(tmp_path):
    c = _fresh_client(tmp_path)
    email = _unique_email()
    c.post("/api/auth/register", json={"email": email, "password": "sifre123"})

    r = c.post("/api/auth/login", json={"email": email, "password": "yanlis-sifre"})
    assert r.status_code == 401

    r = c.get("/api/auth/me")
    assert r.status_code == 401

    r = c.get("/api/history/list")
    assert r.status_code == 401


def test_duplicate_email_registration_returns_409(tmp_path):
    c = _fresh_client(tmp_path)
    email = _unique_email()
    r1 = c.post("/api/auth/register", json={"email": email, "password": "sifre123"})
    assert r1.status_code == 200
    r2 = c.post("/api/auth/register", json={"email": email, "password": "baskasifre"})
    assert r2.status_code == 409


def test_save_list_and_compare_history_round_trip(tmp_path):
    c = _fresh_client(tmp_path)
    email = _unique_email()
    token = c.post("/api/auth/register", json={"email": email, "password": "sifre123"}).json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    r1 = c.post("/api/history/save", json={
        "company_name": "Örnek A.Ş.", "period_label": "2024 Yıl Sonu",
        "fiscal_year": 2024, "analysis": {"health_score": {"score": 70}},
    }, headers=headers)
    assert r1.status_code == 200
    id1 = r1.json()["id"]

    r2 = c.post("/api/history/save", json={
        "company_name": "Örnek A.Ş.", "period_label": "2025 Yıl Sonu",
        "fiscal_year": 2025, "analysis": {"health_score": {"score": 85}},
    }, headers=headers)
    id2 = r2.json()["id"]

    listed = c.get("/api/history/list", headers=headers).json()
    assert sorted(listed["years"]) == [2024, 2025]
    # NOTE: JSON object keys are always strings on the wire -- by_year comes
    # back as {"2024": [...], "2025": [...]}, not {2024: [...]}. The
    # frontend's renderHistoryList() already falls back to the string key
    # for this exact reason; this test locks that contract in.
    assert len(listed["by_year"]["2024"]) == 1
    assert len(listed["by_year"]["2025"]) == 1

    filtered = c.get("/api/history/list?fiscal_year=2024", headers=headers).json()
    assert filtered["years"] == [2024]

    # NOTE: /api/history/compare MUST be routed before /api/history/{record_id}
    # or FastAPI matches "compare" as an int path param and returns 422 --
    # this was a real regression caught while building this feature.
    cmp = c.get(f"/api/history/compare?ids={id1},{id2}", headers=headers)
    assert cmp.status_code == 200
    years_in_order = [item["fiscal_year"] for item in cmp.json()["items"]]
    assert years_in_order == [2024, 2025]

    cmp_bad = c.get(f"/api/history/compare?ids={id1}", headers=headers)
    assert cmp_bad.status_code == 400


def test_users_cannot_see_or_fetch_each_others_history(tmp_path):
    """The single most important guarantee of a multi-tenant history
    feature: user A must never be able to list, fetch, or compare-in user
    B's saved analyses, even by guessing a valid record id."""
    c = _fresh_client(tmp_path)
    token_a = c.post("/api/auth/register", json={"email": _unique_email(), "password": "sifre123"}).json()["token"]
    token_b = c.post("/api/auth/register", json={"email": _unique_email(), "password": "sifre123"}).json()["token"]

    rec = c.post("/api/history/save", json={
        "fiscal_year": 2024, "analysis": {"health_score": {"score": 60}},
    }, headers={"Authorization": f"Bearer {token_a}"})
    rec_id = rec.json()["id"]

    headers_b = {"Authorization": f"Bearer {token_b}"}
    assert c.get(f"/api/history/{rec_id}", headers=headers_b).status_code == 404
    assert c.get("/api/history/list", headers=headers_b).json()["years"] == []

    rec_b = c.post("/api/history/save", json={
        "fiscal_year": 2024, "analysis": {"health_score": {"score": 90}},
    }, headers=headers_b).json()["id"]
    cmp = c.get(f"/api/history/compare?ids={rec_id},{rec_b}", headers=headers_b)
    assert cmp.status_code == 404, "user B must not be able to pull user A's record into a comparison"
