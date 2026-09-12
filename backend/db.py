"""Persistence layer.

DATABASE_URL env var controls the backend:
  - Not set or SQLite -> uses SQLite. If SQLAlchemy is installed, uses SQLAlchemy;
    otherwise seamlessly falls back to Python's built-in sqlite3 standard library
    with a drop-in Session API.
  - Set to postgresql:// -> uses SQLAlchemy with PostgreSQL.
"""
from __future__ import annotations

import json
import os
import sqlite3
import threading
from datetime import datetime
from typing import Any

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local.db")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

_HAVE_SQLALCHEMY = False
try:
    from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
    from sqlalchemy.orm import declarative_base, sessionmaker, relationship
    _HAVE_SQLALCHEMY = True
except ImportError:
    _HAVE_SQLALCHEMY = False

if _HAVE_SQLALCHEMY:
    connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
    engine = create_engine(DATABASE_URL, connect_args=connect_args)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True, index=True)
        email = Column(String(255), unique=True, index=True, nullable=False)
        password_hash = Column(String(255), nullable=False)
        company_name = Column(String(255), nullable=True)
        tenant_id = Column(String(64), nullable=True, index=True, default="default")
        plan = Column(String(32), nullable=True, default="starter")
        created_at = Column(DateTime, default=datetime.utcnow)

        analyses = relationship("AnalysisRecord", back_populates="owner", cascade="all, delete-orphan")

    class AnalysisRecord(Base):
        __tablename__ = "analysis_records"
        id = Column(Integer, primary_key=True, index=True)
        user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
        tenant_id = Column(String(64), nullable=True, index=True, default="default")
        company_name = Column(String(255), nullable=True)
        period_label = Column(String(64), nullable=True)
        fiscal_year = Column(Integer, nullable=False, index=True)
        health_score = Column(Integer, nullable=True)
        result_json = Column(Text, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow, index=True)

        owner = relationship("User", back_populates="analyses")

    def init_db() -> None:
        Base.metadata.create_all(bind=engine)

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

else:
    # -----------------------------------------------------------------------
    # Zero-dependency Built-in sqlite3 Fallback Implementation
    # Provides a drop-in query/add/commit/refresh interface matching SQLAlchemy.
    # -----------------------------------------------------------------------
    _SQLITE_PATH = DATABASE_URL.replace("sqlite:///", "").replace("sqlite://", "") or "./local.db"
    if _SQLITE_PATH.startswith("./"):
        _SQLITE_PATH = os.path.join(os.path.dirname(__file__), _SQLITE_PATH[2:])

    class User:
        def __init__(self, id=None, email=None, password_hash=None, company_name=None, tenant_id="default", plan="starter", created_at=None):
            self.id = id
            self.email = email
            self.password_hash = password_hash
            self.company_name = company_name
            self.tenant_id = tenant_id or "default"
            self.plan = plan or "starter"
            self.created_at = created_at or datetime.utcnow()

    class AnalysisRecord:
        def __init__(self, id=None, user_id=None, tenant_id="default", company_name=None, period_label=None, fiscal_year=None, health_score=None, result_json=None, created_at=None):
            self.id = id
            self.user_id = user_id
            self.tenant_id = tenant_id or "default"
            self.company_name = company_name
            self.period_label = period_label
            self.fiscal_year = fiscal_year
            self.health_score = health_score
            self.result_json = result_json
            self.created_at = created_at or datetime.utcnow()

    class _Query:
        def __init__(self, model_cls, session):
            self.model_cls = model_cls
            self.session = session
            self._filters = []
            self._order_by = []

        def filter(self, *criteria):
            self._filters.extend(criteria)
            return self

        def order_by(self, *order_criteria):
            self._order_by.extend(order_criteria)
            return self

        def _execute(self):
            conn = self.session.conn
            table = "users" if self.model_cls is User else "analysis_records"
            where_clauses = []
            params = []
            for col, op, val in self._filters:
                if op == "==":
                    where_clauses.append(f"{col} = ?")
                    params.append(val)
                elif op == "in":
                    placeholders = ",".join("?" for _ in val)
                    where_clauses.append(f"{col} IN ({placeholders})")
                    params.extend(val)
            query = f"SELECT * FROM {table}"
            if where_clauses:
                query += " WHERE " + " AND ".join(where_clauses)
            if self._order_by:
                query += " ORDER BY " + ", ".join(self._order_by)
            cur = conn.cursor()
            cur.execute(query, params)
            rows = cur.fetchall()
            cols = [d[0] for d in cur.description] if cur.description else []
            objs = []
            for r in rows:
                d = dict(zip(cols, r))
                if self.model_cls is User:
                    obj = User(
                        id=d.get("id"),
                        email=d.get("email"),
                        password_hash=d.get("password_hash"),
                        company_name=d.get("company_name"),
                        tenant_id=d.get("tenant_id", "default"),
                        plan=d.get("plan", "starter"),
                        created_at=datetime.fromisoformat(d["created_at"]) if d.get("created_at") else datetime.utcnow()
                    )
                else:
                    obj = AnalysisRecord(
                        id=d.get("id"),
                        user_id=d.get("user_id"),
                        tenant_id=d.get("tenant_id", "default"),
                        company_name=d.get("company_name"),
                        period_label=d.get("period_label"),
                        fiscal_year=d.get("fiscal_year"),
                        health_score=d.get("health_score"),
                        result_json=d.get("result_json"),
                        created_at=datetime.fromisoformat(d["created_at"]) if d.get("created_at") else datetime.utcnow()
                    )
                objs.append(obj)
            return objs

        def first(self):
            res = self._execute()
            return res[0] if res else None

        def all(self):
            return self._execute()

    class _ColumnExpr:
        def __init__(self, name):
            self.name = name

        def __eq__(self, other):
            return (self.name, "==", other)

        def in_(self, other):
            return (self.name, "in", other)

        def desc(self):
            return f"{self.name} DESC"

        def asc(self):
            return f"{self.name} ASC"

    # Attach expression proxies to model classes
    User.id = _ColumnExpr("id")
    User.email = _ColumnExpr("email")
    User.tenant_id = _ColumnExpr("tenant_id")
    AnalysisRecord.id = _ColumnExpr("id")
    AnalysisRecord.user_id = _ColumnExpr("user_id")
    AnalysisRecord.tenant_id = _ColumnExpr("tenant_id")
    AnalysisRecord.fiscal_year = _ColumnExpr("fiscal_year")
    AnalysisRecord.created_at = _ColumnExpr("created_at")

    class _Session:
        def __init__(self):
            global _SQLITE_PATH
            try:
                self.conn = sqlite3.connect(_SQLITE_PATH, check_same_thread=False)
            except Exception:
                _SQLITE_PATH = ":memory:"
                self.conn = sqlite3.connect(_SQLITE_PATH, check_same_thread=False)
            self._pending_add = []

        def query(self, model_cls):
            return _Query(model_cls, self)

        def add(self, obj):
            self._pending_add.append(obj)

        def commit(self):
            cur = self.conn.cursor()
            for obj in self._pending_add:
                created = obj.created_at.isoformat() if hasattr(obj.created_at, 'isoformat') else str(obj.created_at)
                if isinstance(obj, User):
                    if obj.id is None:
                        cur.execute(
                            "INSERT INTO users (email, password_hash, company_name, tenant_id, plan, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                            (obj.email, obj.password_hash, obj.company_name, getattr(obj, 'tenant_id', 'default'), getattr(obj, 'plan', 'starter'), created)
                        )
                        obj.id = cur.lastrowid
                elif isinstance(obj, AnalysisRecord):
                    if obj.id is None:
                        cur.execute(
                            "INSERT INTO analysis_records (user_id, tenant_id, company_name, period_label, fiscal_year, health_score, result_json, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (obj.user_id, getattr(obj, 'tenant_id', 'default'), obj.company_name, obj.period_label, obj.fiscal_year, obj.health_score, obj.result_json, created)
                        )
                        obj.id = cur.lastrowid
            self.conn.commit()
            self._pending_add.clear()

        def refresh(self, obj):
            pass

        def close(self):
            self.conn.close()

    def init_db() -> None:
        global _SQLITE_PATH
        try:
            conn = sqlite3.connect(_SQLITE_PATH)
        except Exception:
            _SQLITE_PATH = ":memory:"
            conn = sqlite3.connect(_SQLITE_PATH)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                company_name TEXT,
                tenant_id TEXT DEFAULT 'default',
                plan TEXT DEFAULT 'starter',
                created_at TEXT
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS analysis_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                tenant_id TEXT DEFAULT 'default',
                company_name TEXT,
                period_label TEXT,
                fiscal_year INTEGER NOT NULL,
                health_score INTEGER,
                result_json TEXT NOT NULL,
                created_at TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        conn.commit()
        conn.close()

    def get_db():
        db = _Session()
        try:
            yield db
        finally:
            db.close()

