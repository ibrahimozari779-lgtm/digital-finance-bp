# Digital Finance BP v3.6 — Operational Intelligence

## v3.6.4 (P0 — Master Finding Registry)

- **New `finance_engine/finding_registry.py`**: consolidates Decision Engine findings,
  Gap Detection, Root Cause, Risk Ranking and Business Impact into one de-duplicated,
  cross-referenced `finding_registry.master_findings` list. Each entry lists every engine
  that independently corroborates it (`source_engines`), so the same underlying condition
  no longer appears as several unrelated-looking findings.
- Identified and folded 5 exact statement-level duplicates that Gap Detection was
  re-deriving under its own `GAP-*` code with the same metric/threshold already covered
  by a Decision Engine finding: `GAP-CAP-01`→`L002`, `GAP-FIN-01`→`L001`, `GAP-LIQ-01`→`Q002`,
  `GAP-WC-01`→`W001`, `GAP-PROF-01`→`P003`. `build_gap_detection()` itself is unchanged
  (existing tests and any direct callers keep getting the full, un-consolidated list);
  the deduplication happens at the `decision_engine` assembly layer, so the report/API
  output (`gap_detection_engine`, frontend "Gap & Weakness Detection" section) no longer
  shows these 5 as separate cards from the Findings list.
- Operational-evidence gaps (customer/AR/AP/inventory-sourced: `GAP-SALES-*`, `GAP-AR-*`,
  `GAP-AP-*`, `GAP-INV-*`) are NOT duplicates and remain first-class registry entries.
- `build_finance_business_partner_analysis()` now returns a top-level `finding_registry`
  key; this is the intended canonical source for CFO-facing reporting going forward.
- No breaking changes: all pre-existing top-level keys are still returned unchanged in
  shape; only the *contents* of `gap_detection_engine.gaps` are filtered.
- Verification: `test_eight_engines.py` all green; full pytest suite unchanged
  (20 passed / 2 skipped, plus 1 pre-existing unrelated failure in
  `test_scenario_tax_aware_and_debt_proxy_not_zero` present before this change too —
  not touched here, flagged separately).

## v3.6.3

- **Root-cause fix for intermittent "format/pattern mismatch" upload errors**: the classifier
  (`finance_engine/data_classifier.py`) was scanning the internal `_source_row` bookkeeping
  column (and any ordinary amount column that coincidentally contained 3-digit values) as if
  it were a TDHP account-code column. Any sheet with 100+ rows could therefore be silently
  misclassified as `finance`/mizan regardless of its real content (confirmed on real files:
  a 4,741-row sales/profitability pivot was misread as a trial balance at 97% confidence).
  Fixed by (1) excluding `_`-prefixed internal columns from classification and (2) requiring
  a genuine adjacent account-name (text) column before accepting a numeric column as account
  codes - the same signal already used for statement-layout detection elsewhere in the code.
- **Risk Ranking**: findings that fire together for the same underlying theme (e.g. several
  independent leverage rules on a highly-leveraged company) are now consolidated into one
  ranked entry with merged evidence and de-duplicated recommendation text, instead of
  appearing as several near-identical top risks.
- **Profit Quality**: flags that would restate a condition already reported in the main
  Findings list (e.g. finance-cost burden = L001) are now cross-referenced instead of
  re-narrated, plus a new headline `quality_score`/`quality_label`.
- **Scenario Lab & Opportunity Engine**: scenario/opportunity magnitudes (receivables,
  inventory, debt, opex, payables terms) now scale with how far the company's own ratio sits
  from a healthy band this period, instead of a fixed percentage applied to every company
  regardless of state. O001/O002/O003 arithmetic is unchanged (frozen for regression tests).
- **AR/AP Aging**: added per-bucket item counts and % of total, a deterministic collection-risk
  estimate (bucket-weighted), per-party average overdue days, and an overall aging risk tier.

## Delivered

- Semantic multi-file merge: same-role files with different source headers are mapped to common fields before aggregation.
- Sales profitability: customer and product gross-profit views are produced whenever transaction-level cost is available.
- AR/AP intelligence: top overdue counterparties and weighted overdue days are included alongside aging buckets, DSO and DPO.
- Inventory intelligence: adds 365+ dead-stock proxy and value-based inventory aging buckets.
- Operational-finance layer: connects AR overdue, aged stock and AP pressure to evidence-based cash and action signals. The cash-release number is explicitly labelled as a gross exposure proxy, not a forecast.
- AI critic: optional AI narratives are screened for numeric claims that are not traceable to verified engine facts.
- Ingestion resilience: invalid or mixed date cells no longer terminate sales, AR/AP or inventory processing. The implementation avoids the unstable vectorised datetime path observed in the supplied runtime.
- Dependency completeness: adds `httpx`, required by FastAPI's integration-test client.
- Local launcher: `run_local.sh` creates a project-local virtual environment and installs declared dependencies, including `xlrd`, before starting the app. This prevents a locked global Python environment from breaking legacy `.xls` uploads.
- Finder-friendly launcher: double-click `Digital_Finance_BP_BASLAT.command` on macOS.

## Verification

- Core and new unit/regression suite: **20 passed, 2 skipped**.
- One API integration test is ready but could not run in this machine because `httpx` is not currently installed globally. It is now declared in `backend/requirements.txt`; after `pip install -r requirements.txt`, the full suite should include it.
- `python -m compileall`: passed.

## Notes

The AI critic is a guardrail, not an assurance opinion: it flags numeric statements requiring review. Reconciliation results remain source-period/cut-off aware and are not silently forced to match.
