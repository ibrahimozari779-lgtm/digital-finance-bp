# v3.10.0 — Faz 1: Master Decision Hub, gerçek pipeline mimarisi

`APP_VERSION`: 3.9.0 → **3.10.0** · `engine_version`: 1.6 → **1.7**

## Önceki turdaki dürüst itiraz neydi

v3.9.0'da Faz 2 (Finding Consolidation) gerçekten tamamlanmıştı, ama Faz 1
hâlâ eksikti — kabul ettiğim eleştiri şuydu:

> "Her motor bağımsız üretiyor, sonradan finding_registry yamalıyor."

`finding_registry.py` çıktıyı toparlıyordu ama Root Cause, Business Impact,
Risk Ranking ve Action hâlâ `statements`'tan **paralel ve birbirinden
habersiz** üretiliyordu. İki somut kanıtı vardı:

1. Root Cause Engine kendi eşiklerini taşıyordu (`operating_margin < 10`,
   `receivables_to_sales > 0.40`) — bunlar decision_engine.py'deki gerçek
   Finding eşikleriyle (`P002: <5`, `W001: >0.50`) **birebir aynı değildi**.
   İki kopya aynı kuralı farklı sayılarla kontrol ediyordu; zamanla drift
   riski vardı.
2. Management Actions kendi `severity_rank`'ine göre sıralanıyordu —
   Risk Ranking'in ürettiği composite `risk_score`'u hiç kullanmıyordu.
   Aksiyon listesi ile Risk listesi aynı önceliklendirmeyi **tesadüfen**
   paylaşıyordu, garantili değildi.

## Bu turda ne değişti (gerçek mimari, yama değil)

Artık pipeline diyagramdaki gibi **zorunlu bir veri akışı**:

```
Finding → Root Cause → Business Impact → Priority Score → Management Action
```

### 1. `root_cause_engine.py` — artık Findings'i tüketiyor, tekrar üretmiyor

`build_root_cause_analysis(statements, findings=None)` yeni imza. Findings
listesi verildiğinde her nedensel zincir (`RC-P`, `RC-L`, `RC-W`) KENDİ
eşiğini yeniden hesaplamıyor; o zincirin açıkladığı Finding kodları
(`P002/P003`, `L001/L002/D004-D007`, `W001/WC004`) Findings listesinde zaten
var mı diye bakıyor. Sonuç çıktısında yeni bir `findings_driven: bool` alanı
var — hangi modda çalıştığı şeffaf. `findings=None` geçilirse eski
threshold-tabanlı standalone davranış korunuyor (geriye dönük uyumluluk).

### 2. `decision_engine.py` — gerçek Priority Score adımı eklendi

Root Cause çağrısı artık `findings=findings_sorted` alıyor. Risk Ranking'den
sonra yeni bir adım var:

```python
priority_by_code = {
    code: r["risk_score"]
    for r in risk_ranking["ranked_risks"]
    for code in r["contributing_codes"]
}
```

Bu harita — yani gerçek Priority Score — `build_management_actions()`'a
geçiliyor.

### 3. `action_engine.py` — sıralama artık Priority Score'a göre

`priority_by_code` parametresi eklendi. Grup sıralaması artık
`severity_rank` yerine (varsa) Risk Ranking'in `risk_score`'unu kullanıyor;
her action çıktısına da kendi `priority_score`'u yazılıyor — böylece Action
listesindeki sıra ile Risk listesindeki sıra **garanti olarak** aynı.

## Test kanıtı

`test_eight_engines.py`'ye yeni bir regresyon eklendi:

```
PASS: Master Decision Hub — Management Actions follow the Priority Score from Risk Ranking
```

Bu test, her action'ın `priority_score`'unun kendi Risk Ranking `risk_score`'una
eşit olduğunu VE action listesinin bu skora göre azalan sırada olduğunu
doğruluyor — yani mimari iddia (yama değil, gerçek pipeline) artık kod
seviyesinde test edilebilir bir garanti.

Gerçek örnek veri üzerinde gözlemlenen sonuç:

```
Risk Ranking:        1) L001 (100.0)   2) WC004 (69.5)   3) Q002 (34.0)
Management Actions:  1) L001 (100.0)   2) W001  (69.5)   3) Q002 (34.0)
```

İki liste artık aynı Priority Score'dan besleniyor — önceden bu örtüşme
tesadüfiydi, şimdi yapısal.

## Regresyon durumu

- `test_eight_engines.py`: tüm eski assert'ler + `engine_version == '1.7'` +
  yeni `findings_driven` + Priority Score testleri geçiyor.
- `test_business_partner_engine.py`: değişmedi, aynen geçiyor
  (health_score=54.0, O001/O002 rakamları frozen, birebir korundu).

## Hâlâ yapılmayan (kapsam dışı, bilerek)

- Business Impact ve Risk Ranking'in kendi iç formülleri değişmedi (zaten
  Finding-driven çalışıyorlardı, refactor gerekmiyordu).
- Gap Detection tarafındaki aksiyonlar (`GAP-*` kodları) Risk Ranking'in
  kapsamına girmediği için hâlâ kendi severity fallback'ini kullanıyor —
  Gap Detection'ı da Risk Ranking'e dahil etmek ayrı bir faz/karar
  gerektirir, bu turda kapsam dışı bırakıldı.

## Sırada

- Faz 3 zaten v3.9.0'da (FACT/INFERENCE narrative chain)
- Faz 4 — Industry Intelligence (8 sektör karar ağacı)
- Faz 7 — Management Simulator (serbest parametre girişi)
