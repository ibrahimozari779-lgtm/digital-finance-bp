# Digital Finance BP v3.7 — Reader Fix & Report Cleanup

## v3.7.1

### 1. Universal Reader fix — mizan files were being rejected
**Symptom:** valid, well-formed mizan workbooks (with a normal "Hesap Kodu /
Hesap Adı / Borç / Alacak / Borç Bakiye / Alacak Bakiye" header row) failed
with:
> Dosyada otomatik olarak finansal hesap satırları tespit edilemedi.
> Çalışma sayfalarında hesap kodu ve finansal tutar yapısı bulunamadı.

**Root cause:** the ingestion layer (`finance_engine/multi_source_ingestion.py
_read_one` / `_promote_header`) already scans every sheet, finds the header
row by keyword score, and promotes it into real pandas column names before
`app.py` ever sees the sheet. But `merge_workbook_statement_sheets()` in
`app.py` treated every sheet as still headerless: it only tried (a)
`detect_special_layout`, which looks for raw 3-digit numeric codes sitting in
data cells, and (b) `detect_standard_header_sheet`, which re-scans the first
~80 rows of *values* looking for a row that itself contains the words "Hesap
Kodu" etc. Once the header row had already been promoted to a column name
upstream, neither check could find it — the header text was in
`raw.columns`, not in a data row — so the sheet was silently dropped, and
with no sheet producing a trial balance, the workbook-level 422 fired.

**Fix:** added a direct-mapping attempt in `merge_workbook_statement_sheets`
(`app.py`) that runs `detect_mapping()` against the sheet's own column names
*before* falling back to row-scanning. If `account_code` resolves with
sufficient confidence, the trial balance is built straight from that mapping
(`mode: "standard_mizan_direct"` in `sheet_meta`). The two older detectors are
kept unchanged as fallbacks for sheets that genuinely arrive headerless.

**Verified against:**
- `Digital_Finance_BP_Test_Mizan_7A_Detayli.xlsx` (the file that reproduced
  the bug) — now reads 44 account rows / 9 columns correctly.
- `sample_mizan.xlsx`, `sample_three_sheet_financials.xlsx` (bundled samples)
  — unchanged, no regression.
- `Tarfin_Q1_Q2.xlsx` (statement-layout workbook, different code path) —
  unchanged, still 219 rows via `statement_layout` mode.

### 2. Executive Summary duplication
`finance_engine/executive_summary_engine.py` appended the sentence
`"Yönetici bu raporla ne yapmalı: " + decision_points` into the narrative
paragraph (`parts`), while the same `decision_points` list was *also*
rendered separately as its own bulleted block in the frontend
(`execDecision`, inside the "AI CFO" card). Same guidance shown twice in one
card. Removed the paragraph append; `decision_points` is now returned only
for the dedicated bullet block.

### 3. Profitability Bridge & Profit Quality merged
`frontend_template.py`: these were two side-by-side cards with independent
headers and no shared explanation. Merged into a single "Profitability
Bridge & Quality" card (bridge waterfall + quality metrics side by side) with
one commentary function (`profitabilityNarrative`) underneath that explains
where margin is lost across the bridge and then whether what's left is
durable, using the quality score.

### 4. Working Capital commentary added
The CCC/DSO/DIO/DPO card previously rendered only numbers plus the backend's
short technical `note` — no plain-language read of what the number means.
Added `workingCapitalNarrative()`: states the CCC in plain terms, names
whichever of DSO/DIO/DPO is stretching it the most, and labels the band
(healthy / moderate / high pressure).

### Version
`APP_VERSION` in `backend/app.py` bumped from the stale `3.5.0` to `3.7.1`
(the header badge and `/config` endpoint were still reporting v3.5 despite
the folder already being on v3.7.0 — now in sync).
