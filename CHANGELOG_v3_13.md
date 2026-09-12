# v3.13.0 — Demo/test verisi "yetersiz görünüyor" şikâyetinin kök nedenleri

`APP_VERSION`: 3.12.0 → **3.13.0**

## Şikâyet

Canlıda (Render) tüm örnek/demo akışlarında (Genel Mizan, Dönem Karşılaştırma,
3 Tablo, Data Hub) WHAT→WHY→SO WHAT→NOW WHAT bölümlerinin çoğu boş geliyordu;
sistem gerçekte çalışıyor olsa da "test verisi yetersiz / sistem bir şey
göstermiyor" izlenimi veriyordu.

## Kök nedenler (3 gerçek bug + 1 zayıf demo verisi)

### Bug 1 — Türkçe büyük "İ" harfi kolon/kelime eşlemesini kırıyordu
`app.py:normalize()` ve `finance_engine/data_classifier.py:norm()` önce
`.lower()` çağırıp *sonra* Türkçe karakterleri ASCII'ye çeviriyordu. Python'da
`"İ".lower()` tek karaktere değil `"i" + U+0307 (combining dot above)`
ikilisine dönüşür. Türkçe harf çevirisi bu noktada artık devreye giremiyordu
(karakter zaten "İ" değildi), ve ardından çalışan
`re.sub(r"[^a-z0-9]+", " ", s)` bu görünmez noktayı ayraç sayıp kelimenin
ortasına boşluk sokuyordu:

```
normalize("İskonto Tutarı")  ->  "i skonto tutari"   (YANLIŞ, önceki hâl)
normalize("İskonto Tutarı")  ->  "iskonto tutari"     (DOĞRU, düzeltme sonrası)
```

Bu, **İ ile başlayan her Türkçe kelimeyi** etkiliyordu: İskonto, İstanbul,
İşlem, İnşaat, İhracat, İade vb. Sonuç: satış defterindeki "İskonto Tutarı"
kolonu hiç tanınmıyor, indirim/iskonto tutarları PVM ve kâr köprüsü
motorlarına hiç girmiyordu — ve bu sınıf, dosyalardaki herhangi bir İ-baş
harfli kolon/şirket/şehir adı için sessizce tekrarlanabilecek bir hataydı.

**Düzeltme:** Türkçe karakterleri (büyük/küçük) `.lower()`'dan **önce** ASCII'ye
çeviriyoruz, böylece hiçbir zaman combining-mark üretilmiyor.

### Bug 2 — Gelir Tablosu sayfası hiç okunmuyordu (3 Tablo örneği)
`is_special_financial_statement_layout()` yalnızca metinde "balance sheet /
bilanço" **ve** "assets / aktif" arıyordu. Aynı fiziksel yapıya (başlık
satırları + hesap kodu kolonu + tutar kolonu) sahip olan ama farklı
başlıklara sahip **INCOME STATEMENT** ve **BALANCE SHEET (LIABILITIES)**
sayfaları bu kapıdan hiç geçemiyor, `mode="ignored_or_unrecognized", rows=0`
ile tamamen atlanıyordu. Sonuç: Net Satış, Faaliyet Kârı, Net Kâr, Toplam
Pasif hep **0** çıkıyor, "Balance check difference" milyonlarca TL fark
veriyordu.

**Düzeltme:** Kapı artık "income statement / gelir tablosu / kâr zarar" ve
"liabilities / pasif / kaynaklar" varyantlarını da tanıyor. Regresyon testi
(`test_finance_bp_v2.py`) artık üçü de (Net Satış, Faaliyet Kârı, Balance
check difference = 0) doğru geliyor.

### Bug 3 (demo verisi) — Data Hub örnek dosyaları GL ile tutarsız ve çok dar
- Örnek satış defterinde İskonto/Maliyet/Ödenen Tutar/Açık Bakiye kolonları
  yoktu → PVM, kâr kalitesi ve tahsilat metrikleri hep `null` geliyordu.
- Örnek satış defteri toplamı, mizandaki cironun (10.920.000 TL) sadece
  **%44**'ü kadardı → "satış verisi eksik" izlenimi buradan geliyordu.
- AP yaşlandırma toplamı (1.252.451 TL), mizandaki Satıcılar bakiyesinden
  (850.000 TL) belirgin şekilde sapıyordu.
- Stok tutarı (1.284.936 TL), mizandaki Ticari Mallar bakiyesinden
  (1.900.000 TL) sapıyordu.
- Tek dönemlik "Genel Mizan" / "Dönem Karşılaştırma" örnekleri o kadar küçük
  ve borçsuzdu ki (0 kredi, 0 finansman gideri) sistem gerçekten
  raporlayacak bir bulgu bulamıyor, Now What / risk bölümleri boş kalıyordu.

**Düzeltme — tüm demo verisi setleri yeniden üretildi:**
- `sample_sales_ledger.xlsx`: 96 → **240 satır**, 15 müşteri, 6 ürün;
  Brüt Satış / İskonto Tutarı / Net Satış / Maliyet / Ödenen Tutar / Açık
  Bakiye kolonlarıyla; net satış toplamı GL cirosuyla (10.800.000 TL net)
  birebir uyumlu.
- `sample_ar_aging.xlsx`: 27 → **42 fatura**, 11 müşteri; toplam Alıcılar
  bakiyesiyle (2.400.000 TL) uyumlu.
- `sample_ap_aging.xlsx`: 13 → **24 belge**, 8 tedarikçi; toplam Satıcılar
  bakiyesiyle (850.000 TL) uyumlu.
- `sample_inventory.xlsx`: 8 → **15 satır**, 6 SKU × 2-3 depo, gerçekçi
  durgun (90+ gün) ve ölü stok (180+ gün) senaryolarıyla; toplam Ticari
  Mallar bakiyesiyle (1.900.000 TL) uyumlu.
- `sample_mizan.xlsx` / `sample_mizan_period1.xlsx` (Genel Mizan + Dönem
  Karşılaştırma örnekleri): kısa/uzun vadeli banka kredisi ve finansman
  gideri eklendi; ciro %24,5 büyürken faaliyet kârı marjı daralıyor, net
  borç artıyor — yani sistemin gerçekten "kök neden" ve "aksiyon"
  üretebileceği, ana sayfadaki "Net Satış ↑, Faaliyet Kârı ↓, Net Borç ↑"
  anlatısıyla tutarlı, gerçekçi bir hikâye.

## Doğrulama
- `pytest` (backend/): **35 passed, 2 skipped** (önceden 3 test kalıcı olarak
  başarısızdı — hepsi Bug 1/2 yüzündenmiş, artık geçiyor).
- Data Hub örnek seti: `data_hub_errors: []`, veri kalitesi skoru 78 → **100**
  (three_sheet), GL ↔ AR/AP/Satış mutabakat kontrollerinin çoğu artık
  "matched".
- Root cause / risk ranking / senaryo / strateji playbook / narrative engine
  / yönetim aksiyonları — hepsi dolu ve birbirini destekleyen rakamlarla
  geliyor (WHAT→WHY→SO WHAT→NOW WHAT akışının tamamı canlanıyor).

## Deploy notu
Bu değişiklikler yalnızca kod (`backend/app.py`,
`backend/finance_engine/data_classifier.py`) ve kök dizindeki / `demo_data/`
altındaki örnek `.xlsx` dosyalarıdır — şema veya API sözleşmesi değişmedi.
Render'a normal `git push` ile deploy edilebilir; ek migration gerekmez.
