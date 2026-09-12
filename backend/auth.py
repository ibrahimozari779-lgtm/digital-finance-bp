"""Minimal JWT auth: register/login/token-verify.

Kept deliberately dependency-light: uses PyJWT if installed; otherwise seamlessly
falls back to Python's standard library hmac/hashlib/base64 to sign and verify
RFC 7519 JWT tokens with zero external dependencies.
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import secrets
import time
from datetime import datetime, timedelta, timezone

_HAVE_PYJWT = False
try:
    import jwt
    _HAVE_PYJWT = True
except ImportError:
    _HAVE_PYJWT = False

from fastapi import Depends, HTTPException, Header
from db import User, get_db

JWT_SECRET = os.getenv("JWT_SECRET") or secrets.token_hex(32)
JWT_ALGO = "HS256"
TOKEN_TTL_HOURS = 24 * 30  # 30 days


def hash_password(password: str, salt: str | None = None) -> str:
    salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 200_000)
    return f"{salt}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        salt, _ = stored.split("$", 1)
    except ValueError:
        return False
    return hmac.compare_digest(hash_password(password, salt), stored)


def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode('utf-8').rstrip('=')


def _b64url_decode(s: str) -> bytes:
    pad = 4 - (len(s) % 4)
    if pad != 4:
        s += '=' * pad
    return base64.urlsafe_b64decode(s)


def create_token(user_id: int, email: str, tenant_id: str = "default", plan: str = "starter") -> str:
    exp = int(time.time()) + TOKEN_TTL_HOURS * 3600
    payload = {
        "sub": str(user_id),
        "email": email,
        "tenant_id": tenant_id,
        "plan": plan,
        "exp": exp,
    }
    if _HAVE_PYJWT:
        return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)

    header = {"alg": "HS256", "typ": "JWT"}
    h_b64 = _b64url_encode(json.dumps(header, separators=(',', ':')).encode('utf-8'))
    p_b64 = _b64url_encode(json.dumps(payload, separators=(',', ':')).encode('utf-8'))
    signing_input = f"{h_b64}.{p_b64}".encode('utf-8')
    sig = hmac.new(JWT_SECRET.encode('utf-8'), signing_input, hashlib.sha256).digest()
    s_b64 = _b64url_encode(sig)
    return f"{h_b64}.{p_b64}.{s_b64}"


def decode_token(token: str) -> dict:
    if _HAVE_PYJWT:
        try:
            return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Oturum süresi doldu, tekrar giriş yapın.")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Geçersiz oturum.")

    parts = token.split('.')
    if len(parts) != 3:
        raise HTTPException(status_code=401, detail="Geçersiz oturum.")
    h_b64, p_b64, s_b64 = parts
    try:
        signing_input = f"{h_b64}.{p_b64}".encode('utf-8')
        expected_sig = hmac.new(JWT_SECRET.encode('utf-8'), signing_input, hashlib.sha256).digest()
        actual_sig = _b64url_decode(s_b64)
        if not hmac.compare_digest(expected_sig, actual_sig):
            raise HTTPException(status_code=401, detail="Geçersiz oturum.")
        payload_raw = _b64url_decode(p_b64).decode('utf-8')
        payload = json.loads(payload_raw)
        if payload.get("exp") and time.time() > payload["exp"]:
            raise HTTPException(status_code=401, detail="Oturum süresi doldu, tekrar giriş yapın.")
        return payload
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=401, detail="Geçersiz oturum.")


def get_current_user(authorization: str | None = Header(default=None), db = Depends(get_db)) -> User:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Giriş gerekli.")
    token = authorization.split(" ", 1)[1].strip()
    payload = decode_token(token)
    user = db.query(User).filter(User.id == int(payload["sub"])).first()
    if not user:
        raise HTTPException(status_code=401, detail="Kullanıcı bulunamadı.")
    return user

