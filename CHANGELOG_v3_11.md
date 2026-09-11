# v3.11.0 — Faz 3 revize: "AI CFO yazsın" değil, Kural + Veri + Sebep Zinciri

`APP_VERSION`: 3.10.0 → **3.11.0** · `engine_version`: 1.8 → **1.9**

## Kabul ettiğim itiraz

> "AI CFO özet yazıyor. Ama gerçek CFO gibi düşünmüyor... Narrative Engine =
> Kural + Veri + Sebep Zinciri yaklaşımına geçmelisin."

Doğruydu. Önceki turda (v3.10.0) `narrative_chain` zaten kural-tabanlıydı
(LLM'e yazdırmıyordu) ama tek bir düz liste halindeydi — CFO'nun gerçek
düşünme sırasını (`KPI değişti → Neden → Finansal Etki → Risk → Ne
Yapılmalı`) açık bir yapı olarak göstermiyordu, ve sürücü değişimlerini TL'ye
çevirmiyordu (sadece "% veya puan" diyordu, "kaç TL" demiyordu).

## Bu turda ne eklendi

### 1. Trend Motoru artık DSO ve DIO'yu ayrı ayrı izliyor

Önceden yalnızca birleşik CCC (Nakit Dönüşüm Süresi) günü izleniyordu. Artık
`trend_engine.py` her dönem için `build_cash_conversion_cycle()`'ın zaten
hesapladığı `dso_days` ve `dio_days`'i de kendi zaman serisi olarak
topluyor — "DSO 58 günden 82 güne çıktı" gibi somut, tek-metrik iddialar
artık mümkün (önceden sadece "CCC uzadı" diyebiliyordu).

### 2. Sürücü değişimleri artık TL'ye çevriliyor — gerçek formüllerle

`executive_summary_engine.py`'ye `_tl_impact_for_metric()` eklendi. Yeni
uydurulmuş bir sayı değil — sistemde zaten var olan formüllerin aynısı:

| Metrik | Formül | Zaten nerede kullanılıyordu |
|---|---|---|
| DSO gün değişimi | gün × (Net Satış / 365) | `cash_conversion_engine.py`'nin `estimated_cash_tied_up` hesabı |
| DIO gün değişimi | gün × (COGS / 365) | Aynı motor |
| Marj puan değişimi | puan × Net Satış | `root_cause_engine.py`'nin margin bridge `pct_of_sales` mantığı |
| Finansal borç değişimi | zaten TL cinsinden | doğrudan `financial_debt` serisi |

Test edilen gerçek örnek (DSO 58→70→82 gün, senaryonuzdaki ile aynı şekil):
```
Alacak Tahsilat Süresi / DSO (gün) +12.0 gün (~6,197,260 TL ilave nakit ihtiyacı)
```

### 3. Yeni `narrative_story` alanı — açık 5 adımlı yapı

`executive_summary_engine` çıktısına, en üst risk için şu yapı eklendi:

```
{
  "finding_code": "...",
  "kpi_change": {...},          # KPI değişti
  "why": [...],                  # Neden (TL-quantified, kategoriye göre genel)
  "root_cause": {...},           # Kök Neden Motoru'ndan, causal_status etiketli
  "financial_impact": {...},     # Finansal etkisi ne (Business Impact Engine)
  "risk": {...},                 # Risk ne (Risk Ranking Engine — tier + score)
  "forward_projection": {...},   # opsiyonel, gerçek eşiğe doğrusal projeksiyon
  "what_to_do": {...},           # Ne yapılmalı (Action Engine'in atadığı gerçek aksiyon)
  "scope_note": "..."            # neyin kapsam dışı olduğu, açıkça
}
```

Bu, sizin diyagramınızın (`KPI değişti → Neden → Finansal etki → Risk → Ne
yapılmalı`) birebir kod karşılığı — ama her adım gerçek bir motordan geliyor,
şablon metne LLM doldurmuyor.

## Kasıtlı olarak yapmadıklarım (dürüst kapsam sınırı)

Verdiğiniz 5 senaryonun hepsini birebir üretemem, çünkü bazıları bu sistemin
**veri modelinde bulunmayan bir ayrıntı seviyesi** istiyor:

| Senaryo | Durum | Neden |
|---|---|---|
| 1. Kârlılık erozyonu | ✅ Genel olarak destekleniyor | Marj + TL etkisi hesaplanıyor. Ama "hammadde maliyeti +%12 / fiyat +%2" ayrımı — COGS'un ne kadarının hammadde, ne kadarının fiyatlamadan geldiği — ürün/kalem seviyesi veri ister, sistemde yok |
| 2. Tahsilat riski (DSO) | ✅ Genel formül destekleniyor | Ama "ilk 10 müşteride yoğunlaşma" — müşteri boyutu sistemde hiç yok |
| 3. Stok şişmesi | ✅ DIO + TL formülü destekleniyor | Ama "yavaş hareket eden ürünler stokun %27'si" — SKU seviyesi veri yok |
| 4. Müşteri kârlılığı | ❌ Desteklenmiyor | Müşteri bazlı hiçbir veri (satış, marj, iskonto) bu pipeline'a hiç girmiyor |
| 5. Nakit krizi erken uyarı | ❌ Desteklenmiyor | Sistem dönemsel (yıllık/çeyreklik) bilanço okuyor; aylık nakit bakiyesi/burn-rate takibi yok — bu Faz 6 (Forecast) + Faz 8 (Autonomous Agent, periyodik takip) gerektirir |

Bu satırlar `narrative_story.scope_note` alanında da açıkça belirtiliyor —
üretilemeyen adım sessizce atlanıyor, uydurulmuyor.

## Test kanıtı

`test_eight_engines.py`'ye iki yeni regresyon:
- Driver bullet + projeksiyon mantığının Kârlılık/Borçluluk gibi farklı
  kategorilerde genellendiğini kanıtlayan test (önceki turdan)
- **Yeni:** `narrative_story`'nin uçtan uca dolduğunu VE DSO TL etkisinin
  gerçek formülle (`gün × günlük satış`) eşleştiğini doğrulayan test

## Regresyon durumu

Tüm eski testler + `engine_version == '1.9'` + iki yeni test geçiyor.
`test_business_partner_engine.py` değişmedi, aynen geçiyor.
