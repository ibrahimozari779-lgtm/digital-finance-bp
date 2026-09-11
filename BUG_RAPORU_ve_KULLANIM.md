# Bug Raporu ve Yeni Demo Veri Seti

## Bulunan Kritik Bug (app.py)

`merge_workbook_statement_sheets()` fonksiyonu, `detect_special_layout()`'u
`is_special_financial_statement_layout()` kontrolünden **geçirmeden**
doğrudan çağırıyordu. `detect_special_layout()` çok genel bir sezgisel
kural kullanıyor ("5. satırdan sonra bir sütunda 8+ tane 3 haneli kod var
mı?") ve bu kural, tamamen standart/temiz bir mizanda bile (5+ hesaptan
sonra herhangi bir 3 haneli kod göründüğünde — yani hemen hemen HER
gerçek mizanda) yanlışlıkla tetikleniyordu.

Bu tetiklendiğinde dosya, sadece tek bir gerçek dünya "Balance Sheet /
Aktif" export formatı için yazılmış özel parser'a (`build_special_trial_balance`)
yönlendiriliyor; bu parser:
- İlk birkaç hesabı (genelde Kasa/Bankalar/Alıcılar/Stoklar) tamamen siliyor,
- Kalan hesapların işaretini/tutarını yanlış yorumluyor,

Sonuç: Toplam Varlıklar = 0, bilanço denklemi tutmuyor, ve buna bağlı
zincirleme olarak CCC, DuPont, Risk Ranking, Trend, Cash Bridge, Management
Actions gibi TÜM motorlar ya boş ya da anlamsız çıktı üretiyordu — kullanıcının
bildirdiği "2 boş, 3 boş, 4 tek madde, 5 boş, 6 boş" tam olarak bu zincirin sonucu.

**Düzeltme:** `detect_special_layout(raw)` çağrısı artık
`is_special_financial_statement_layout(raw)` True dönerse çalışıyor;
aksi halde normal akış (direct mapping / standard header / headerless
inference) devam ediyor. `app_FIXED.py` dosyasındaki değişikliği
projenizdeki `backend/app.py` içine uygulayın (satır ~717 civarı,
`det=detect_special_layout(raw)` satırını değiştirdik).

Doğrulama: Aşağıdaki 2 dönemlik demo mizanla test ettim — düzeltmeden önce
bilanço farkı -17.538.000 TL idi, düzeltmeden sonra 0.0 TL (tam denk).

## Yeni Demo Veri Seti (test/gösterim için)

Gerçekçi, kademeli bozulan bir şirket senaryosu (marj daralması, DSO artışı,
kaldıraç artışı, nakit sıkışması) — tüm 8 motoru ve Data Hub'ı aynı anda
göstermek için tasarlandı:

- `sample_mizan_2024_donem1.xlsx` — önceki dönem (sağlıklı)
- `sample_mizan_2025_donem2.xlsx` — güncel dönem (stresli) → Trend/Cash Bridge
  sekmesine bu ikisini eski→yeni sırayla yükleyin.
- `sample_ar_aging.xlsx` — alacak yaşlandırma (AR Intelligence, kritik müşteriler)
- `sample_ap_aging.xlsx` — borç yaşlandırma (AP Intelligence)
- `sample_sales_ledger.xlsx` — 2 yıllık ürün/müşteri kırılımlı satış (PVM,
  Sales Intelligence: fiyat artışı + hacim düşüşü + mix bozulması senaryosu)
- `sample_inventory.xlsx` — depo/ürün bazlı stok (Inventory Intelligence,
  yavaş hareket eden stok tespiti)

Data Hub sekmesine mizan + AR + AP + satış + stok dosyalarının hepsini
birlikte yükleyip sektör olarak "retail" seçerseniz, Financial Health,
Cash/Performance/Decision Intelligence gruplarının tamamı dolu içerikle
gelir (test ettiğim sonuçlar: health_score 62 "Dikkat Gerektiriyor",
5 finding, 6 fırsat, 3 sıralı risk, CCC 133.6 gün, 7 narrative story).

## Ek 2 Bug Daha Bulundu ve Düzeltildi (Data Hub / çoklu dosya tarafı)

1. **`multi_source_ingestion.py` — `_looks_like_statement_layout` yanlış öncelik:**
   Satış/AR/AP/stok gibi operasyonel dosyalarda "Miktar" gibi bir sütun
   tesadüfen çoğunlukla 100-799 aralığında sayılar içeriyorsa (çok yaygın),
   sistem bunu "başlıksız muhasebe tablosu" sanıp gerçek başlık satırını
   (Müşteri/Ürün/Tarih/...) yok sayıyor, sütunlar 0/1/2/3/4 pozisyon adına
   düşüyordu. Artık önce gerçek bir başlık satırı aranıyor; yalnızca
   bulunamazsa "headerless statement" varsayımına geçiliyor.

2. **`data_classifier.py` — tanımsız alan adı KeyError'ı:**
   `classify_dataframe`, `ALIASES` sözlüğünde hiç tanımlanmamış
   `debit_balance` / `credit_balance` / `debit_turnover` / `credit_turnover`
   alanlarını sorguluyordu. Bu, Data Hub'a bir mizan sayfası içeren HERHANGİ
   bir çoklu dosya yüklemesinde анlık KeyError ile tüm analizi çökertiyordu.
   Eksik alan takma adları eklendi.

Bu 2 düzeltmeyle birlikte mizan + AR + AP + satış + stok dosyalarının hepsi
tek seferde (Data Hub) yüklendiğinde hatasız çalışıyor ve AR/AP Intelligence,
Sales Intelligence, Inventory Intelligence, Reconciliation Engine dahil tüm
modüller dolu sonuç üretiyor (test edildi, hatasız).
