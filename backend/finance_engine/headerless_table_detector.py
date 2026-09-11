from __future__ import annotations

import re
from typing import Any
import pandas as pd
from .numeric_utils import parse_number


def _digits(value: Any) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return ""
    s = str(value).strip()
    if re.fullmatch(r"\d+(?:\.\d+)*", s):
        return re.sub(r"\D", "", s)
    return ""


def _number(value: Any) -> float | None:
    return parse_number(value)


def infer_headerless_financial_table(raw: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]] | None:
    """Infer a financial account table when column headers are missing.

    The detector deliberately uses conservative structural evidence rather than
    requiring literal headers. It recognises TDHP-like account codes (100-799),
    optional account-name columns, and one-to-four numeric amount columns.
    """
    if raw is None or raw.empty:
        return None

    nrows, ncols = raw.shape
    if nrows < 4 or ncols < 2:
        return None

    scan_rows = range(min(nrows, 1000))
    code_candidates: list[tuple[float, int, int]] = []
    for c in range(ncols):
        hits = 0
        valid = 0
        for r in scan_rows:
            d = _digits(raw.iat[r, c])
            if d:
                valid += 1
                if len(d) == 3 and 100 <= int(d) <= 799:
                    hits += 1
        if hits >= 4:
            code_candidates.append((hits / max(1, valid), hits, c))
    if not code_candidates:
        return None
    code_candidates.sort(reverse=True)
    _, code_hits, code_col = code_candidates[0]

    data_rows: list[int] = []
    for r in range(nrows):
        d = _digits(raw.iat[r, code_col])
        if len(d) == 3 and 100 <= int(d) <= 799:
            data_rows.append(r)
    if len(data_rows) < 4:
        return None

    # Find nearby non-numeric text column, typically account name/description.
    name_col = None
    name_scores: list[tuple[float, int, int]] = []
    for c in range(ncols):
        if c == code_col:
            continue
        text_hits = 0
        nonblank = 0
        for r in data_rows:
            v = raw.iat[r, c]
            if v is None or (isinstance(v, float) and pd.isna(v)):
                continue
            s = str(v).strip()
            if not s:
                continue
            nonblank += 1
            if _number(v) is None:
                text_hits += 1
        if nonblank:
            density = text_hits / nonblank
            distance = abs(c - (code_col + 1))
            name_scores.append((density, -distance, c))
    name_candidates = [x for x in name_scores if x[0] >= 0.65]
    if name_candidates:
        name_candidates.sort(reverse=True)
        name_col = name_candidates[0][2]

    # Numeric density for all other columns on account rows.
    numeric_cols: list[tuple[float, float, int]] = []
    for c in range(ncols):
        if c == code_col or c == name_col:
            continue
        vals = [_number(raw.iat[r, c]) for r in data_rows]
        valid = [v for v in vals if v is not None]
        density = len(valid) / len(vals)
        nonzero = sum(abs(v or 0.0) > 1e-12 for v in valid) / max(1, len(valid))
        if density >= 0.55:
            numeric_cols.append((density, nonzero, c))
    numeric_cols.sort(key=lambda x: x[2])
    if not numeric_cols:
        return None

    cols = ["account_code"]
    if name_col is not None:
        cols.append("account_name")

    selected = [c for _, _, c in numeric_cols]
    # Common headerless export shapes:
    #   code, name, balance
    #   code, name, debit, credit
    #   code, name, debit, credit, debit_balance, credit_balance
    if len(selected) >= 4:
        turnover_debit, turnover_credit = selected[:2]
        balance_debit, balance_credit = selected[-2:]
        amount_mapping = {
            balance_debit: "debit_balance",
            balance_credit: "credit_balance",
            turnover_debit: "debit_turnover",
            turnover_credit: "credit_turnover",
        }
        cols.extend([f"_c{c}" for c in selected])
    elif len(selected) == 3:
        amount_mapping = {selected[0]: "debit_turnover", selected[1]: "credit_turnover", selected[2]: "balance"}
        cols.extend([f"_c{c}" for c in selected])
    elif len(selected) == 2:
        amount_mapping = {selected[0]: "debit_turnover", selected[1]: "credit_turnover"}
        cols.extend([f"_c{c}" for c in selected])
    else:
        amount_mapping = {selected[0]: "balance"}
        cols.append(f"_c{selected[0]}")

    out_rows: list[dict[str, Any]] = []
    for r in data_rows:
        code = _digits(raw.iat[r, code_col])
        row: dict[str, Any] = {"account_code": code, "_source_row": r + 1}
        if name_col is not None:
            row["account_name"] = "" if pd.isna(raw.iat[r, name_col]) else str(raw.iat[r, name_col]).strip()
        for c in selected:
            row[f"_c{c}"] = raw.iat[r, c]
        out_rows.append(row)

    df = pd.DataFrame(out_rows)
    for c, target in amount_mapping.items():
        df[target] = pd.Series([_number(raw.iat[r, c]) or 0.0 for r in data_rows], dtype=float)

    # If we inferred debit/credit turnover only, derive balance. If we inferred closing
    # balances, derive signed balance from debit vs credit closing balances.
    if "debit_balance" in df.columns or "credit_balance" in df.columns:
        df["debit_balance"] = df.get("debit_balance", 0.0)
        df["credit_balance"] = df.get("credit_balance", 0.0)
        df["balance"] = df["debit_balance"] - df["credit_balance"]
        source = "inferred_debit_balance-credit_balance"
    elif "balance" not in df.columns:
        df["debit_turnover"] = df.get("debit_turnover", 0.0)
        df["credit_turnover"] = df.get("credit_turnover", 0.0)
        df["balance"] = df["debit_turnover"] - df["credit_turnover"]
        df["debit_balance"] = df["balance"].clip(lower=0)
        df["credit_balance"] = (-df["balance"]).clip(lower=0)
        source = "inferred_debit_turnover-credit_turnover"
    else:
        df["debit_turnover"] = 0.0
        df["credit_turnover"] = 0.0
        df["debit_balance"] = df["balance"].clip(lower=0)
        df["credit_balance"] = (-df["balance"]).clip(lower=0)
        source = "inferred_net_balance"

    # Final canonical-ish column order.
    for c in ["debit_turnover", "credit_turnover", "debit_balance", "credit_balance", "balance"]:
        if c not in df.columns:
            df[c] = 0.0
    keep = ["account_code", "account_name", "debit_turnover", "credit_turnover", "debit_balance", "credit_balance", "balance", "_source_row"]
    keep = [c for c in keep if c in df.columns]
    df = df[keep]
    return df.reset_index(drop=True), {
        "mode": "headerless_financial_inference",
        "code_column": f"Column {code_col + 1}",
        "name_column": None if name_col is None else f"Column {name_col + 1}",
        "numeric_columns": [f"Column {c + 1}" for c in selected],
        "account_rows": len(df),
        "confidence": "high" if code_hits >= 20 else "medium",
        "amount_inference": source,
    }
