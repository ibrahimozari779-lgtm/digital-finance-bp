"""Persistence layer.

DATABASE_URL env var controls the backend:
  - Not set (local dev on Render free tier without a DB add-on) -> falls back
    to a local SQLite file. NOTE: on Render's free web-service disk this file
    is EPHEMERAL and is wiped on every redeploy/restart. This is fine for a
    quick local test, but for real persistent history in production you must
    set DATABASE_URL to a real hosted Postgres (e.g. Supabase free tier,
    Render's own Postgres add-on, Neon, etc).
  - Set to a postgres:// / postgresql:// URL -> used as-is (normalized to the
    psycopg driver).
"""
from __future__ import annotations

import os
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local.db")
if DATABASE_URL.startswith("postgres://"):
    # SQLAlchemy 2.x / psycopg need the explicit "postgresql://" scheme.
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

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
    created_at = Column(DateTime, default=datetime.utcnow)

    analyses = relationship("AnalysisRecord", back_populates="owner", cascade="all, delete-orphan")


class AnalysisRecord(Base):
    """One saved analysis snapshot, classified by fiscal year so the
    frontend can group/filter/compare a user's uploads over time."""
    __tablename__ = "analysis_records"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    company_name = Column(String(255), nullable=True)
    period_label = Column(String(64), nullable=True)   # e.g. "2025 Q4", "2025"
    fiscal_year = Column(Integer, nullable=False, index=True)
    health_score = Column(Integer, nullable=True)
    result_json = Column(Text, nullable=False)          # full analysis payload, as JSON text
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
