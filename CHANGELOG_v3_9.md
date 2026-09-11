# v3.9.0 — Master Decision Hub (Sprint 1) + CFO Narrative FACT/INFERENCE (Sprint 2)

`APP_VERSION` (badge: "Finance Core v3.9.0 · WHAT-WHY-SOWHAT Flow") · `engine_version` (decision_engine payload): **1.6** (was 1.5)

## Sprint 1 — `finding_registry.py` genişletildi: gerçek bir Master Decision Hub

Önceden `finding_registry.py` yalnızca Gap Detection ↔ Decision Engine bulgularını
(ve dolaylı olarak Root Cause / Risk Ranking / Business Impact'i) birleştiriyordu.
Opportunity Engine ve Management Actions hâlâ ayrı, bağlantısız bölümlerdi — aynı
altta yatan koşul (ör. "brüt marj düşük") Risk listesinde, Root Cause zincirinde,
Opportunity kartında ve Action listesinde dört ayrı isimle tekrar tekrar
görünüyordu.

**Değişen:**
- `build_finding_registry()` artık iki opsiyonel parametre alıyor:
  `opportunities` ve `management_actions` (geriye dönük uyumlu — verilmezse
  eski davranış aynen çalışır).
- Her `master_finding` artık şunları taşıyor:
  - `linked_opportunities`: kategori→alan eşlemesiyle bulunan en yakın 2 fırsat
    (kod, başlık, tahmini etki).
  - `linked_action`: management_actions içinden `finding_id` veya
    `merged_finding_codes` eşleşmesiyle bulunan atanmış aksiyon.
  - `confidence_score` (0-100): bulgunun kendi güven etiketi + kaç motorun
    bağımsız doğruladığı + opportunity/action'ın var olup olmadığı birleşik
    bir puana dönüşüyor.
- `decision_engine.py`, `build_finding_registry()` çağrısına
  `opportunities_sorted` ve `management_actions`'ı artık geçiyor.

**Dosyalar:** `finance_engine/finding_registry.py`, `finance_engine/decision_engine.py`

## Sprint 2 — `executive_summary_engine.py`: FACT/INFERENCE narrative chain

CFO Narrative motoru gerçek sayıları ("net marj %18 düştü") ve bu motorun kendi
yorumunu ("bunun sebebi X,Y,Z") aynı cümlede, ayrım yapmadan veriyordu.

**Eklenen:** `narrative_chain` alanı — üç kademeli, etiketli liste:
1. **FACT** — sağlık skoru, en büyük risk + parasal büyüklüğü (başka
   motorlardan doğrudan alınır, yorum eklenmez).
2. **INFERENCE** — kök neden zinciri; Root Cause Engine'in kendi
   `causal_status` alanı (`likely_driver` / `hypothesis`) `causal_status_label`
   olarak taşınır, böylece "olası ana sürücü" ile "hipotez — doğrulanmalı"
   aynı güvenle sunulmaz.
3. **INFERENCE** (opsiyonel) — ileriye dönük projeksiyon: yalnızca Trend
   Engine gerçek çok-dönemli düşüş tespit ettiyse (T001) **ve** Business
   Impact bugün zaten ölçülmüş bir likidite açığı (`liquidity_gap` driver)
   içeriyorsa üretilir. İkisi birden yoksa bu adım listede hiç yer almaz —
   uydurma sayı yok.

**Dosya:** `finance_engine/executive_summary_engine.py`

## Test / regresyon

- `test_eight_engines.py`: `engine_version == '1.6'` olarak güncellendi, geri
  kalan tüm assert'ler değişmeden geçiyor.
- `test_business_partner_engine.py`: değişiklik gerekmedi, aynen geçiyor.

## Sırada (henüz bu sürümde değil)

- Sprint 3 — Management Simulator (serbest parametre girişi: "DSO 15 gün
  azalsa?")
- Sprint 4 — Industry Intelligence (8 sektör karar ağacı, gerçek TCMB/TÜİK
  veri kaynağı gerekiyor)
