# v3.12.0 — Faz 4: Tek hikâyeden çok-senaryolu Narrative Engine'e geçiş

`APP_VERSION`: 3.11.0 → **3.12.0** · `engine_version`: 1.9 → **2.0**

## Kabul ettiğim itiraz

> "Bu narrative engine çok önemli... farklı senaryolar, kurallar zinciri...
> sadece örnek verdim, sen bizim projemizin gerekliklerine uyan daha fazla
> senaryo ekle."

v3.11.0'daki `narrative_story`, brief'teki 5 örneğin tam olarak istediği
`Ne oldu → Neden → Maliyet → Ne yapmalı` yapısını üretiyordu, ama yalnızca
**dönemin en kritik tek bulgusu** için (top-1). Gerçek bir Digital Finance
Business Partner'ın yaptığı şey bu değil: aynı dönemde kârlılık erozyonu
DA, tahsilat riski DE, kaldıraç artışı DA aynı anda oluşabilir — hepsinin
ayrı ayrı, birbirinden bağımsız anlatılması gerekir.

## Bu turda ne eklendi

### 1. Yeni modül: `finance_engine/narrative_engine.py`

Brief'te tarif edilen JSON trigger-tablosu mimarisinin birebir Python
karşılığı. Her tetikleyici üç parçadan oluşur:

```python
{
  "code": "...", "title": "...", "category": "...",
  "condition": ctx -> bool,   # eşik kontrolü
  "severity": ctx -> str,     # critical/high/medium/positive
  "build": ctx -> {...},      # şablonu doldur
}
```

Motor, TÜM tetikleyicileri aynı anda değerlendirir (top-1 değil) ve
tetiklenenleri severity'ye göre sıralanmış kart listesi olarak döner. Hiçbir
sayı bu motorda yeniden hesaplanmaz — her rakam `trend_engine`,
`root_cause_engine`, `cash_conversion_engine`, `cash_bridge_engine`,
`benchmarking_engine`, `profit_quality_engine` veya (varsa)
`sales_intelligence_engine`'in zaten ürettiği çıktıdan okunur.

### 2. 12 senaryo tetikleyicisi

| Kod | Senaryo | Kaynak |
|---|---|---|
| NE-MARGIN-EROSION | Kârlılık Erozyonu | trend + root_cause |
| NE-DSO-RISK | Tahsilat Riski | trend.dso_days + cash_conversion |
| NE-INVENTORY-BLOAT | Stok Şişmesi | trend.dio_days + cash_conversion |
| NE-CASH-RUNWAY | Nakit Krizi Erken Uyarısı | cash_bridge (kaba aylık proxy, `approx:true` etiketli) |
| NE-LEVERAGE-RISK | Kaldıraç Artışı | trend.debt_to_equity |
| NE-LIQUIDITY-RISK | Likidite Daralması | trend.current_ratio |
| NE-EARNINGS-QUALITY | Kazanç Kalitesi / Nakde Dönmeyen Kâr | cash_bridge.cash_realization_pct |
| NE-FINANCE-BURDEN | Finansman Maliyeti Baskısı | Finance costs / Operating profit |
| NE-SECTOR-UNDERPERFORMANCE | Sektör Altı Performans | benchmarking_engine |
| NE-GROWTH-WITHOUT-PROFIT | Kârsız Büyüme | trend (satış büyürken net marj geriliyor) |
| NE-MARGIN-IMPROVEMENT | Kârlılık İyileşmesi (pozitif) | trend |
| NE-CUSTOMER-MARGIN-GAP | Müşteri Karlılık Problemi | sales_intelligence_engine.customer_profitability (koşullu — bkz. aşağı) |

`NE-MARGIN-IMPROVEMENT` bilinçli olarak eklendi: bir Business Partner
yalnızca kötü haberi değil, neyin işe yaradığını da aynı formatta
anlatabilmeli.

### 3. Bir düzeltme: Senaryo 4 (Müşteri Karlılık) aslında destekleniyormuş

v3.11'in changelog'unda bu senaryo "❌ Desteklenmiyor, müşteri bazlı hiçbir
veri sisteme girmiyor" olarak işaretlenmişti. Bu turda kod tabanını yeniden
incelerken `sales_intelligence_engine.py`'nin, kullanıcı müşteri kolonlu bir
satış detay dosyası yüklediğinde `customer_profitability` (müşteri bazlı
ciro/COGS/brüt marj) alanını ZATEN hesapladığı görüldü. `NE-CUSTOMER-MARGIN-GAP`
bu veriyi, kanonik gelir tablosundaki şirket ortalama brüt marjıyla
kıyaslıyor. Veri yüklenmediyse tetiklenmiyor — uydurulmuyor, sessizce
atlanıyor.

### 4. Raporda konum: "Why" ile "Now What" arasına taşındı

İlk sürümde bu kartlar akışın sonuna (eski adım 6b) eklenmişti. Bu, akışın
mantığını bozuyordu: kartlar zaten Kök Neden (Why) bilgisini + Finansal
Etki + Aksiyon önerisini birleştiriyor, yani doğal yeri **Why'ın hemen
ardı, Now What'tan hemen önce**. Adım numaraları buna göre yeniden
sıralandı:

```
1 What → 2 So What → 3 Kritik Taraflar → 4 Why (Kök Neden)
  → 5 Senaryo Anlatıları (YENİ konum)
  → 6 Now What → 7 What If → 8 AI CFO
```

Böylece okuyucu "bu neden oldu" (4) dedikten hemen sonra "işte tam olarak
ne anlama geliyor ve ne yapmalıyım" (5) hikâyesini okuyor, en sona
ertelenmiş bir ek gibi değil.

### 5. `finance_engine/decision_engine.py` wiring

`build_narrative_engine()`, trend/root_cause/business_impact/ccc/
cash_bridge/benchmark/profit_quality zaten hesaplandıktan sonra çağrılıyor
ve `data_hub['analysis_sales']` varsa `sales_intelligence` olarak da
besleniyor. Çıktı, ana response'a `narrative_engine` anahtarıyla ekleniyor.

## Kasıtlı olarak yapmadıklarım (dürüst kapsam sınırı, devam ediyor)

| Alt kırılım | Durum | Neden |
|---|---|---|
| "İlk 10 müşteride tahsilat yoğunlaşması" | ❌ | AR aging/subledger verisi pipeline'a girmiyor |
| "%27 slow-moving stok" | ❌ | SKU seviyesi hareket verisi pipeline'a girmiyor |
| Kesin ay-bazlı nakit runway | ⚠️ Yaklaşık | Aylık nakit akışı/banka hareketi verisi yok; dönemsel proxy'den türetilen kaba tahmin `approx:true` ile açıkça işaretleniyor |

Bu satırlar `narrative_engine.stories[].data_gap` alanında ilgili karta
iliştirilmiş olarak görünüyor — ayrı, unutulması kolay bir listede değil.

## Test kanıtı

Sentetik iki-dönem veri seti ile uçtan uca doğrulandı: `build_narrative_engine()`
tek çağrıda 7 senaryoyu (kârlılık erozyonu, finansman baskısı, DSO, DIO,
nakit runway, likidite, sektör altı performans) doğru severity sırasıyla
aynı anda üretti; ayrı bir sentetik `customer_profitability` girdisiyle
`NE-CUSTOMER-MARGIN-GAP` da bağımsız olarak doğrulandı.

## Regresyon durumu

Mevcut hiçbir motorun imzası/dönüş değeri değişmedi (`narrative_engine`
yeni ve additive bir anahtar). `narrative_story`/`narrative_chain`
(top-1, v3.11) hâlâ `executive_summary_engine` içinde duruyor ve
kaldırılmadı — iki katman birbirini tamamlıyor: biri "en kritik tek
hikâye" (AI CFO paragrafına besleniyor), diğeri "bu dönemde tetiklenen
tüm hikâyeler" (adım 5, Senaryo Anlatıları).
