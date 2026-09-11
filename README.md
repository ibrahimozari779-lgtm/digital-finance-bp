# Digital Finance Business Partner v3.8.0

## Product focus
Universal multi-source finance/operations ingestion, deterministic root-cause intelligence, gap detection, financial impact, management actions and scenario analysis.

### v3.8.0 changes — Comparative Analysis + first sellability pass
- **Karşılaştırmalı Analiz (Comparative Analysis) upgraded to a first-class
  feature.** Previously, uploading 2+ periods (Trend tab) only produced a
  small raw table buried in the Appendix, and `trend_findings` computed by
  the backend were never rendered anywhere. Now:
  - `trend_engine.py` adds a Cash Conversion Cycle trend (calls the CCC
    engine per period), a `higher_is_better`-aware "improved/worsened/flat"
    assessment per metric, and a `headline_comparison` payload built
    specifically for a clean period-vs-period card view.
  - A new **Karşılaştırmalı Analiz** card appears right under the headline
    metrics in "1 — What" whenever 2+ periods are loaded: side-by-side
    metric cards (Net Satış, Faaliyet Kârı, Net Kâr, Net Marj, Borç/Özkaynak,
    CCC) with colored delta badges, the previously-hidden trend findings
    (e.g. "büyüme kâra dönüşmüyor", "kaldıraç artıyor", "nakit dönüşüm
    süresi uzuyor") rendered as real insight cards, and a collapsible full
    multi-period table for traceability.
  - The old Appendix B trend block now points to the new card instead of
    repeating the same numbers (keeps the earlier "one explanation per
    fact" fix intact).
  - Verified against a simulated 2019→2020 case (25% revenue growth, 10%
    profit decline, 40% debt growth): correctly fired "Büyüme kâra
    dönüşmüyor" and showed CCC improving while margin/debt stayed flat.
- **Sellability quick wins:**
  - Added a legal/KVKK disclaimer line to the footer (not accounting/tax/
    legal/investment advice; uploaded files are processed in memory only
    and not persisted server-side — verified true against the current
    codebase, no file write path exists).
  - Added a one-click **"Örnek veriyle dene"** button on the landing hero:
    fetches a bundled sample workbook via new `/api/sample/{key}` and
    `/api/sample` endpoints and runs the full analysis with zero uploads —
    for demos and first-time evaluation.
  - Turkicized the remaining English card titles ("Profitability Bridge &
    Quality" → "Kâr Köprüsü & Kâr Kalitesi", "Leverage & Liquidity" →
    "Kaldıraç & Likidite", "Working Capital" → "İşletme Sermayesi", "Cash
    Flow Bridge" → "Nakit Akış Köprüsü") for a consistent Turkish-first UI.

### v3.7.1 changes
- **Universal Reader fix**: sheets whose header row was already promoted to real
  column names upstream (e.g. "Hesap Kodu", "Borç Bakiye") were falling through
  the trial-balance detector, which only knew how to find a header *row* inside
  still-headerless data. Result: valid mizan files failed with "Dosyada
  otomatik olarak finansal hesap satırları tespit edilemedi." Fixed by mapping
  a sheet's own column names directly before falling back to row-scanning.
  See `CHANGELOG_v3_7.md` for the full detail and verification steps.
- **Executive Summary de-duplication**: the "Yönetici bu raporla ne yapmalı"
  guidance was written twice in the same AI CFO card — once folded into the
  narrative paragraph, once as its own bullet list below. The paragraph is now
  facts-only; the bullet list is the single place that guidance is stated.
- **Profitability Bridge & Profit Quality merged** into one card/cluster with
  a single connecting commentary (where margin is lost → whether what's left
  is durable), instead of two separate cards with no shared narrative.
- **Working Capital commentary added**: the CCC/DSO/DIO/DPO card previously
  showed numbers with no plain-language interpretation. It now explains what
  the CCC figure means, which driver is stretching it most, and what band
  it's in.

### v3.5 changes
- Content-first source discovery; filename is only a weak fallback signal.
- CSV/XLS/XLSX/XLSM defensive readers and isolated per-file failures.
- Cross-source root-cause chains across Sales → AR → Cash → Financing, Inventory → Cash and AP → Liquidity where evidence exists.
- First-class Gap & Weakness Detection, including missing intelligence requirements.
- Scenario economics now separates Gross Profit, PBT, Tax and Net Profit impact; debt repayment uses a clearly-labelled finance-cost saving proxy.
- Management actions expose expected impact when a deterministic proxy exists.
- Multi-source operational outputs are surfaced at top-level API fields as well as inside Data Hub.
- AI remains downstream of verified deterministic outputs.

## Run
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```
