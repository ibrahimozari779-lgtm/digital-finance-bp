# TRUST_AUDIT.md — Faz 0: Güven Sertleştirme

Kapsam: `OKUBENI_Musteri_Karari_ve_Duzeltmeler.md`'de listelenen ve müşterinin
satın alma kararını doğrudan etkileyen 3 güven riskinin **regresyona
bağlanması**. Bu turda hesaplama motorları (finance_engine/*) değiştirilmedi;
sadece zaten yapılmış düzeltmelerin bir daha sessizce geri gelmeyeceğini
garanti eden testler eklendi.

## Eklenen dosya
- `backend/tests/test_trust_hardening.py` — 8 test, hepsi geçiyor.

## Test edilen 3 güven kontratı

### 1. Data Quality skoru ↔ çapraz kaynak mutabakatı (dosya: `finance_engine/data_quality_engine.py`)
- `apply_cross_source_reconciliation` fonksiyonunun varlığı doğrulandı ve
  şu davranış kilitlendi:
  - Uyarı/mutabakat farkı yoksa skor **dokunulmadan** kalır.
  - Uyarı varsa skor **her zaman** düşer (asla "Trusted" sessizce kalamaz);
    `cross_source_warning_count` alanı ve açıklayıcı `note` her zaman görünür.
  - Birleşik skor, iç-tutarlılık skorunu **asla aşamaz** (5 farklı
    warning/material kombinasyonuyla test edildi).
  - `internal_consistency_score` orijinal (mizan-içi) değeri korur — "neden
    skor değişti" izlenebilirliği kaybolmuyor.
- **Doğrulama yöntemi:** eski hatalı davranışı (`reconciliation` argümanını
  görmezden gelen sahte bir fonksiyon) simüle ettim; testimiz bunu gerçekten
  yakalayacak şekilde yazıldığını kanıtladım (bkz. konuşma geçmişi — 100/100
  skorun 3 uyarıya rağmen değişmeden kaldığı senaryo, test tarafından
  `assert out["score"] < 100.0` ile reddediliyor).

### 2. `severity_summary` ↔ gösterilen bulgu listesi (dosya: `finance_engine/finding_registry.py`)
- Sentetik 5 bulgulu bir gap listesiyle: `severity_summary` toplamının,
  ekranda gösterilen (`gaps_deduplicated`) liste uzunluğuna **birebir**
  eşit olduğu doğrulandı.
- Bir bulgu bir Decision Engine finding'ine "katlandığında" (duplicate fold),
  hem listeden hem de özet sayımından **aynı anda** düştüğü, birinden düşüp
  diğerinde kalmadığı doğrulandı (müşterinin bildirdiği tam senaryo:
  `severity_summary: {critical:2,...}` iken liste sadece 1 madde).

### 3. Frontend string-kontratları (dosya: `backend/frontend_template.py`)
- Alacak/tedarikçi yoğunlaşma rozeti: `<10%` her zaman `"tag positive"` +
  "Düşük Risk" ile render ediliyor; eşik sırası (`<10 / 10-30 / >=30`)
  ters dönmüş değil.
- "Yönetici Özeti — Deterministik CFO Anlatısı" bölümünün yanında
  **"Kural Tabanlı · AI Değil"** rozetinin var olduğu ve opsiyonel LLM
  yorumunun (`#aiBox`) her zaman ayrı bir DOM elemanında, açık bir "üret"
  butonunun arkasında kaldığı doğrulandı — deterministik metin (`#exec`)
  ile hiçbir zaman aynı kapta karışmıyor.

## Ek bulgu (kapsam dışı, sadece not düşüldü)
`backend/tests/test_v35_intelligence.py::test_scenario_tax_aware_and_debt_proxy_not_zero`
testi, `scenario_engine.py` içindeki S003 senaryosunun artık sabit +1 puan
yerine banda-duyarlı (`margin_pp`, marj açığına göre 1.0/1.5/2.0 puan) bir
mantık kullanmasından dolayı **eskiyen bir test beklentisiydi** — motor
davranışında bir hata değil. Bu turda test beklentisi gerçek (band-adaptive)
davranışa göre düzeltildi ve nedeni test dosyasına yorum olarak eklendi.
Motor mantığına dokunulmadı.

## Sonuç
- Toplam test suite: **29 passed, 2 skipped, 0 failed**.
- Hâlâ çözülmemiş bir "güven riski" kalmadı (bu 3 madde kapsamında).
- Faz 2-3 kapsamındaki maddeler (sektörel benchmark derinliği, kalıcı
  çok-dönem takip, ERP entegrasyonu, çok kullanıcılı mimari) hâlâ açık —
  bkz. `DFBP_Mimari_Cursor_Prompt.md` Faz 1-3.
