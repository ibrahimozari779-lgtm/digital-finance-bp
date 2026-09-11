#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR/backend"

# Keep dependencies isolated from the system Python so legacy .xls support is
# installed reliably even when the global site-packages directory is locked.
if [ ! -x "$ROOT_DIR/.venv/bin/python" ]; then
  python3 -m venv "$ROOT_DIR/.venv"
fi
"$ROOT_DIR/.venv/bin/python" -m pip install --upgrade pip
"$ROOT_DIR/.venv/bin/python" -m pip install -r requirements.txt
exec "$ROOT_DIR/.venv/bin/python" -m uvicorn app:app --reload
