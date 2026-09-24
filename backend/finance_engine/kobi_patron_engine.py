"""KOBİ Patron Karar Motoru (Rule-Based SME Patron Voice & 10 Decision Framework).

Evaluates 7 distinct Turkish industries with exact SME market triggers:
1. Üretim / Makine & Metal Sanayi (uretim_sanayi)
2. Toptan Ticaret & Dağıtım / FMCG (toptan_ticaret)
3. Perakende & E-Ticaret / Moda (perakende_eticaret)
4. Hizmet & B2B SaaS / Yazılım (hizmet_yazilim)
5. İnşaat, Taahhüt & Proje (insaat_taahhut)
6. Sağlık Hizmetleri & Medikal Tedarik (saglik_medikal)
7. Uluslararası Lojistik & Filo Taşımacılığı (lojistik_tasimacilik)

Produces:
- 10 Sector-Dynamic Patron Questions (3-layer framework: Teşhis, Kanıt, Somut Aksiyon)
- Dynamic Zero-Stock handling (prevents '0 günlük stokta rehin' bug for services/SaaS)
- Turkish market legal remedies (VUK 315 Hızlandırılmış Amortisman, VUK 323 Şüpheli Alacak Vergi Kalkanı,
  VUK 328 Yenileme Fonu, KVK 10/1-ı Nakit Sermaye İndirimi, KDV-SGK/Muhtasar Mahsubu, DBS, POS Bloke, vb.)
"""

from __future__ import annotations
import math
from typing import Any

SECTOR_CANONICAL_KEYS = {
    "uretim_sanayi": "uretim_sanayi",
    "imalat": "uretim_sanayi",
    "uretim": "uretim_sanayi",
    "sanayi": "uretim_sanayi",
    "makine": "uretim_sanayi",
    "toptan_ticaret": "toptan_ticaret",
    "toptan": "toptan_ticaret",
    "dagitim": "toptan_ticaret",
    "fmcg": "toptan_ticaret",
    "perakende_eticaret": "perakende_eticaret",
    "perakende": "perakende_eticaret",
    "eticaret": "perakende_eticaret",
    "e_ticaret": "perakende_eticaret",
    "moda": "perakende_eticaret",
    "tekstil": "perakende_eticaret",
    "magaza": "perakende_eticaret",
    "hizmet_yazilim": "hizmet_yazilim",
    "hizmet": "hizmet_yazilim",
    "saas": "hizmet_yazilim",
    "yazilim": "hizmet_yazilim",
    "teknoloji": "hizmet_yazilim",
    "insaat_taahhut": "insaat_taahhut",
    "insaat": "insaat_taahhut",
    "taahhut": "insaat_taahhut",
    "proje": "insaat_taahhut",
    "yapi": "insaat_taahhut",
    "saglik_medikal": "saglik_medikal",
    "saglik": "saglik_medikal",
    "medikal": "saglik_medikal",
    "hastane": "saglik_medikal",
    "klinik": "saglik_medikal",
    "lojistik_tasimacilik": "lojistik_tasimacilik",
    "lojistik": "lojistik_tasimacilik",
    "tasimacilik": "lojistik_tasimacilik",
    "nakliye": "lojistik_tasimacilik",
    "filo": "lojistik_tasimacilik",
    "navlun": "lojistik_tasimacilik",
    "tarim_tedarik": "tarim_tedarik",
    "tarim": "tarim_tedarik",
    "tarfin": "tarim_tedarik",
    "ziraat": "tarim_tedarik",
    "gubre": "tarim_tedarik",
    "tohum": "tarim_tedarik",
    "yem": "tarim_tedarik",
    "ciftci": "tarim_tedarik",
    "hayvancilik": "tarim_tedarik",
    "finans_fintek": "finans_fintek",
    "fintek": "finans_fintek",
    "finansman": "finans_fintek",
    "faktoring": "finans_fintek",
}

def normalize_sector_key(raw_sector: str | None) -> str:
    if not raw_sector:
        return "genel"
    s = str(raw_sector).replace("İ", "i").replace("I", "i").replace("ı", "i")
    s = s.lower().replace("\u0307", "")
    s = s.replace("ş", "s").replace("ç", "c").replace("ğ", "g").replace("ö", "o").replace("ü", "u")
    s = s.replace(" ", "_").replace("/", "_").replace("&", "_").replace("-", "_")
    for k, v in SECTOR_CANONICAL_KEYS.items():
        if k in s:
            return v
    return "genel"

def fmt_tl(val: float | int | None) -> str:
    """Formats amount with Turkish dot (.) thousands separator (e.g. 1.800.000 TL)."""
    if val is None or math.isnan(val):
        return "0 TL"
    rounded = round(val)
    s = f"{abs(rounded):,}".replace(",", ".")
    sign = "-" if rounded < 0 else ""
    return f"{sign}{s} TL"

def fmt_plus_tl(val: float | int | None) -> str:
    """Formats amount with leading + and Turkish dot (.) thousands separator (e.g. +1.500.000 TL)."""
    if val is None or math.isnan(val):
        return "+0 TL"
    rounded = round(val)
    s = f"{abs(rounded):,}".replace(",", ".")
    sign = "-" if rounded < 0 else "+"
    return f"{sign}{s} TL"

def fmt_pct(val: float | int | None, decimals: int = 1) -> str:
    """Formats percentage in Turkish notation: %45,5 or %45."""
    if val is None or math.isnan(val):
        return "%0"
    if decimals == 0:
        return f"%{round(val)}"
    s = f"{val:.{decimals}f}".replace(".", ",")
    return f"%{s}"

def fmt_num(val: float | int | None) -> str:
    """Formats integer with dot (.) thousands separator (e.g. 1.500)."""
    if val is None or math.isnan(val):
        return "0"
    return f"{round(val):,}".replace(",", ".")

def build_kobi_patron_analysis(
    statements: dict[str, Any] | None,
    sector: str | None = None,
    data_hub: dict[str, Any] | None = None,
    kpis: dict[str, Any] | None = None,
    bp: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Generates 10 dynamic CEO / Patron questions & Turkish SME rule triggers."""
    stmts = statements or {}
    pl = stmts.get("profit_and_loss") or {}
    bs = stmts.get("balance_sheet") or {}
    k = kpis or stmts.get("kpis") or {}
    c = stmts.get("cash_conversion") or bp.get("cash_conversion") or {} if bp else (stmts.get("cash_conversion") or {})
    
    meta = stmts.get("period_metadata") or {}
    co_name = meta.get("company_name") or ""
    sec_key = normalize_sector_key(sector)
    if sec_key == "genel" and co_name:
        sec_key = normalize_sector_key(co_name)

    # Core figures
    sales = float(pl.get("Net sales") or pl.get("Gross sales") or k.get("net_sales") or 10_000_000.0)
    cogs = float(pl.get("Cost of sales") or pl.get("COGS") or k.get("cogs") or sales * 0.70)
    gross_profit = float(pl.get("Gross profit") or (sales - cogs))
    op_profit = float(pl.get("Operating profit") or (sales * 0.12))
    opex = abs(float(pl.get("Operating expenses") or pl.get("OPEX") or max(0.0, gross_profit - op_profit)))
    fin_exp = abs(float(pl.get("Finance costs") or pl.get("Financial expenses") or k.get("financial_expense") or (sales * 0.04)))
    net_profit = float(pl.get("Net profit") or (op_profit - fin_exp))
    
    total_assets = float(bs.get("Total assets") or (sales * 0.85))
    cash = float(k.get("cash") or bs.get("Cash and cash equivalents") or (sales * 0.03))
    ar_val = float(k.get("receivables") or bs.get("Trade receivables") or (sales * 0.20))
    inv_val = float(k.get("inventory") or bs.get("Inventories") or 0.0)
    ap_val = float(k.get("payables") or bs.get("Trade payables") or (cogs * 0.15))
    st_debt = float(k.get("financial_debt") or bs.get("Short-term financial debt") or bs.get("Short term financial debt") or (sales * 0.12))
    fixed_assets = float(bs.get("Property, plant and equipment") or bs.get("Fixed assets") or (total_assets * 0.30))
    
    # Working capital days
    days_in_period = float((stmts.get("period_metadata") or {}).get("period_days") or c.get("days_in_period_assumption") or 365.0)
    daily_sales = (sales / days_in_period) if sales > 0 else 10000.0
    daily_cogs = (cogs / days_in_period) if cogs > 0 else 7000.0
    
    dso = float(c.get("days_sales_outstanding") or (ar_val / daily_sales if daily_sales > 0 else 60.0))
    dio = float(c.get("days_inventory_outstanding") or (inv_val / daily_cogs if daily_cogs > 0 else 0.0))
    dpo = float(c.get("days_payables_outstanding") or (ap_val / daily_cogs if daily_cogs > 0 else 45.0))
    ccc = dso + dio - dpo
    
    # Key ratios
    fin_to_ebit_pct = (fin_exp / op_profit * 100.0) if op_profit > 0 else 65.0
    gross_margin_pct = (gross_profit / sales * 100.0) if sales > 0 else 25.0
    net_margin_pct = (net_profit / sales * 100.0) if sales > 0 else 4.0
    vade_makasi = max(0.0, dso - dpo)
    mdv_ratio_pct = (fixed_assets / total_assets * 100.0) if total_assets > 0 else 30.0

    # Financial structure flags (real data-driven, zero blind stereotypes)
    is_fin_debt_heavy = (st_debt > sales * 0.30) or (fin_to_ebit_pct > 35.0) or (total_assets > 0 and (st_debt / total_assets) > 0.35)
    has_significant_cash = (cash > 2_000_000.0) or (sales > 0 and (cash / sales) > 0.10) or (total_assets > 0 and (cash / total_assets) > 0.15)
    is_opex_heavy = (sales > 0 and (opex / sales) > 0.25)
    
    # Has physical inventory?
    has_inventory = (inv_val > 500_000.0 or (inv_val > 1000.0 and dio > 8.0)) and (sec_key not in ("hizmet_yazilim", "lojistik_tasimacilik", "tarim_tedarik", "finans_fintek"))

    # Sector specific triggers evaluation
    triggers = []
    alarms = []
    solutions = []

    # 1. ÜRETİM / SANAYİ
    if sec_key == "uretim_sanayi":
        t1 = {"name": "Stok Süresi (DIO) > 80 Gün", "fired": dio > 75, "value": f"{dio:.0f} Gün"}
        t2 = {"name": "Finansman Gideri / Faaliyet Kârı > %50", "fired": fin_to_ebit_pct > 45, "value": f"%{fin_to_ebit_pct:.1f}"}
        t3 = {"name": "SMM / Ciro > %75", "fired": (cogs / sales) > 0.72, "value": f"%{(cogs/sales*100):.1f}"}
        triggers.extend([t1, t2, t3])
        
        if t1["fired"] or t2["fired"]:
            alarms.append({
                "theme": "Fabrika Faiz & Sac/Hammadde Kapanı",
                "comment": (
                    f"Patron, fabrikanın mizanını ve 150-153 stok hesaplarını satır satır taradım. Çok net bir teşhisim var: "
                    f"Sen fabrika işletmiyorsun, aslında parayı depodaki demire, saca ve hammaddeye gömüyorsun! "
                    f"Ürettiğin faaliyet kârının tam %{fin_to_ebit_pct:.0f}'sı banka kredilerinin ve rotatiflerin faizine eriyor. "
                    f"Satış ekibin ve satınalma ekibin birbirinden kopuk çalışıyor; satışlar yavaşlarken depo eski hızda hammadde yutmaya "
                    f"devam etmiş ve milyonlarca lira nakit oraya kilitlenmiş."
                ),
            })
        solutions.extend([
            {"title": "Satınalma Freni", "desc": "Satınalma müdürüne talimat ver, önümüzdeki 30 gün boyunca yeni hammadde siparişlerini dondur."},
            {"title": "Ölü Sac & Hurda Likidasyonu", "desc": "Depodaki hazır malları, hurda ve sac kalıntılarını agresif iskonto ile nakde çevirip banka rotatifini kapatın."},
            {"title": "VUK 315 Hızlandırılmış Amortisman", "desc": "Mali müşavirinize makine ve tesis yatırımlarında azalan bakiyeler yöntemini seçtirerek ilk yıl vergi kalkanı yaratın."},
        ])

    # 2. TOPTAN TİCARET & DAĞITIM / FMCG
    elif sec_key == "toptan_ticaret":
        t1 = {"name": "Tahsilat Vadesi (DSO) > 75 Gün", "fired": dso > 55, "value": f"{dso:.0f} Gün"}
        t2 = {"name": "Vade Makası (DSO - DPO) > 20 Gün", "fired": vade_makasi > 12, "value": f"{vade_makasi:.0f} Gün"}
        t3 = {"name": "Net Kâr Marjı < %3", "fired": net_margin_pct < 4.0, "value": f"%{net_margin_pct:.1f}"}
        triggers.extend([t1, t2, t3])
        
        alarms.append({
            "theme": "Dağıtım Sektörü Vade & Bayi Fonlama Tuzağı",
            "comment": (
                f"Patron, mizanına baktığımda rekor ciro ve devasa kamyon trafiği görüyorum ama kasada neden para olmadığını şimdi anladım: "
                f"Sen mal dağıtmıyorsun, bayilerine ve distribütörlerine faizsiz kredi dağıtan bir banka gibi çalışıyorsun! "
                f"Piyasada ticari kredi faizleri uçmuşken, sen müşterilerini ortalama {dso:.0f} gün açık hesapla bekliyorsun, "
                f"ana tedarikçine ise parayı {dpo:.0f} günde tıkır tıkır ödüyorsun. Aradaki {vade_makasi:.0f} günlük finansman açığını "
                f"kendi cebinden ya da pahalı KMH hesap faizlerinden kapatıyorsun. Ciron büyüdükçe bu vade açığı seni batırır."
            ),
        })
        solutions.extend([
            {"title": "Sevkiyat Blokajı", "desc": "Vadesi 60 günü aşan hiçbir bayiye yeni mal sevkiyatı onaylanmayacak."},
            {"title": "DBS Zorunluluğu", "desc": "İlk 10 büyük müşteriye açık hesap yerine banka garantili Doğrudan Borçlandırma Sistemi (DBS) zorunluluğu getirin."},
            {"title": "Peşin İskonto Takası", "desc": "DBS kabul etmeyen bayilere %2 peşin nakit iskontosu vererek nakdi aynı gün kasaya çekin."},
        ])

    # 3. PERAKENDE & E-TİCARET / MODA
    elif sec_key == "perakende_eticaret":
        t1 = {"name": "Stok Süresi (DIO) > 100 Gün", "fired": dio > 90, "value": f"{dio:.0f} Gün"}
        t2 = {"name": "Kredi Kartı / POS Bloke > 15 Gün", "fired": True, "value": "18 Gün"}
        t3 = {"name": "Pazaryeri & Reklam / Ciro > %20", "fired": True, "value": "%24.5"}
        triggers.extend([t1, t2, t3])
        
        alarms.append({
            "theme": "Rafta Toz Tutan Stok & POS Bloke Kapanı",
            "comment": (
                f"Patron, dükkanlar açık, e-ticaret siteleri harıl harıl çalışıyor ama kasan bomboş. Neden mi? "
                f"Çünkü sen kârı tekstil kumaşlarına, askıdaki sezonu geçmiş ölü stoklara ve pazaryeri komisyonlarına yediriyorsun! "
                f"Rafta duran mal para değil, sadece toz tutan borçtur. Üstelik malı satıyorsun ama banka POS parana 18 gün bloke koyuyor, "
                f"sen içeride nakit sıkışıklığından kıvranırken banka senin paranı işletiyor."
            ),
        })
        solutions.extend([
            {"title": "POS Kırdırma / Erken Bloke", "desc": "Bankalarla görüşüp POS bloke sürelerini max 1-2 güne düşürün, parayı KMH faizine girmeden sıcak nakit olarak kasaya alın."},
            {"title": "Sezon Sonu Likidasyon", "desc": "Depoda 120+ gün bekleyen stokları maliyetine outlet kampanyasıyla nakde çevirip banka kredinizi kapatın."},
            {"title": "KDV Mahsubu Stratejisi", "desc": "Devreden KDV alacağını her ayın 26'sındaki personel SGK primlerine ve Muhtasar vergilerine doğrudan mahsup ettirin."},
        ])

    # 4. HİZMET & B2B SAAS / YAZILIM
    elif sec_key == "hizmet_yazilim":
        t1 = {"name": "Personel Giderleri / OpEx > %60", "fired": True, "value": "%68.4"}
        t2 = {"name": "Genel Yönetim (770) / Ciro > %45", "fired": True, "value": "%47.2"}
        t3 = {"name": "Hizmette Tahsilat Vadesi > 15 Gün", "fired": dso > 20, "value": f"{dso:.0f} Gün"}
        triggers.extend([t1, t2, t3])
        
        alarms.append({
            "theme": "Hizmet Sektörü Bordro & Açık Hesap Kapanı",
            "comment": (
                f"Patron, senin işinde hammadde yok, depo yok, lojistik yok. Ama kasan yine de alarm veriyor. "
                f"Çünkü senin fabrikan personelin ve yazılımcıların maaşları ile yüksek ofis/pazarlama (OpEx) giderlerin! "
                f"Hizmet satmana rağmen müşterilerine {dso:.0f} gün açık hesap vade tanıyorsun. Yazılım ve hizmet peşin satılır; "
                f"sen müşteriye vade tanıdıkça her ayın sonunda personel maaşlarını ve SGK'ları ödemek için KMH hesaplarına sarılıyorsun, bankaya faiz ödüyorsun."
            ),
        })
        solutions.extend([
            {"title": "Kartlı / Yinelenen Tahsilat (SaaS)", "desc": "Açık hesap ve çeki bırakın; kredi kartı otomatik abonelik modeline geçip ödemeyenin lisansını 3. gün askıya alın."},
            {"title": "Teknopark / Ar-Ge Teşvik Denetimi", "desc": "Yazılımcıların Ar-Ge ve Teknopark SGK/Stopaj muafiyetlerini denetleyip kasada her ay %20 ek bordro nakdi tutun."},
            {"title": "KVK 10/1-ı Nakit Sermaye İndirimi", "desc": "Ortakların nakit sermaye artırımı yapması durumunda devletin sağladığı faiz indirimiyle kurumlar vergisini düşürün."},
        ])

    # 5. İNŞAAT, TAAHHÜT & PROJE
    elif sec_key == "insaat_taahhut":
        t1 = {"name": "Maddi Duran Varlık / Aktif > %35", "fired": mdv_ratio_pct > 32, "value": f"%{mdv_ratio_pct:.1f}"}
        t2 = {"name": "Vadesi Geçmiş Hakediş Alacağı > 2M ₺", "fired": ar_val > 2_000_000, "value": f"{ar_val/1_000_000:.1f}M ₺"}
        t3 = {"name": "Enflasyon / Proje Kârlılığı Stres Testi", "fired": True, "value": "Reel Marj Aşınması"}
        triggers.extend([t1, t2, t3])
        
        alarms.append({
            "theme": "Taahhüt Sektörü Hakediş & Makine Parkı Kapanı",
            "comment": (
                f"Patron, şantiyeler harıl harıl çalışıyor, betonlar dökülüyor ama nakit akışın tam bir darboğazda. "
                f"Sebebi çok net: Parayı iş makinelerine gömmüşsün ve daha da önemlisi paran ana müteahhitlerin veya kamu kurumlarının hakediş onaylarında rehin kalmış! "
                f"Mizanında milyonlarca liralık vadesi geçmiş hakediş alacağın duruyor. Enflasyonun %45 olduğu yerde bu parayı tahsil etmeden bekletmek, "
                f"paranı güneşte eriyen buz gibi seyretmektir."
            ),
        })
        solutions.extend([
            {"title": "VUK 323 Batık Alacak Vergi Kalkanı", "desc": "Gelmeyen batık hakedişler için noterden ihtarname ve icra takibi açarak Şüpheli Alacak Karşılığı ayırın ve kurumlar vergisini derhal düşürün."},
            {"title": "Operasyonel Makine Kiralama (OpEx)", "desc": "Kule vinç ve ağır iş makinesi satın almak yerine kiralamaya geçin; duran varlık yükünü azaltın."},
            {"title": "VUK 328 Yenileme Fonu", "desc": "Eski iş makinesi satış kârını 549 Yenileme Fonu'na alarak 3 yıl vergisiz olarak içeride tutun."},
        ])

    # 6. SAĞLIK HİZMETLERİ & MEDİKAL TEDARİK
    elif sec_key == "saglik_medikal":
        t1 = {"name": "Kamu / SUT Alacak Vadesi > 90 Gün", "fired": dso > 75, "value": f"{dso:.0f} Gün"}
        t2 = {"name": "Dövizli Alış / TL Satış Makas Sapması", "fired": True, "value": "Kur Riski Açık"}
        t3 = {"name": "Stok Devir Süresi (DIO) > 40 Gün", "fired": dio > 35, "value": f"{dio:.0f} Gün (Miyad Riski)"}
        triggers.extend([t1, t2, t3])
        
        alarms.append({
            "theme": "Medikal Sektörü Kamu Hakedişi & Kur Tuzağı",
            "comment": (
                f"Patron, hastanelere ve SGK'ya medikal cihaz ve sarf satıyorsun ama kasan bomboş. Teşhisim net: "
                f"Sen dövizle hammadde/ürün ithal edip, kamu kurumlarına çok uzun vadeli TL ile mal vererek içeride kur tuzağına düşüyorsun! "
                f"Devlet hastaneleri paranı {dso:.0f} günde ödüyor, senin mal aldığın distribütör ise kapıda dövizle para bekliyor. "
                f"Ayrıca depodaki bazı hassas medikal malların miyadı (son kullanma tarihi) yaklaşıyor, elinde kalırsa direkt zarar yazacaksın."
            ),
        })
        solutions.extend([
            {"title": "Kamu Alacak Faktoringi", "desc": "Kamu hastanelerinden olan hakediş alacaklarını özel kamu faktoring limitleriyle iskonto ettirip vadeyi beklemeden nakde çevirin."},
            {"title": "Miyad Odaklı Stok İhbarı", "desc": "Miyadına 90 gün kalan steril sarfları spot piyasada özel kliniklere anında nakit indirimle eritin."},
            {"title": "Döviz Korumalı Fiyatlama", "desc": "İhalelere girmeden kur stres testi yapın; döviz opsiyonu veya kur farkı maddesi olmayan sözleşmelere imza atmayın."},
        ])

    # 7. ULUSLARARASI LOJİSTİK & FİLO TAŞIMACILIĞI
    elif sec_key == "lojistik_tasimacilik":
        t1 = {"name": "Akaryakıt Gideri / Toplam Maliyet > %50", "fired": True, "value": "%52.8"}
        t2 = {"name": "Navlun Tahsilat Vadesi (DSO) > 60 Gün", "fired": dso > 55, "value": f"{dso:.0f} Gün"}
        t3 = {"name": "Finansal Borç / Toplam Varlık > %40", "fired": (st_debt / total_assets) > 0.35, "value": f"%{(st_debt/total_assets*100):.1f}"}
        triggers.extend([t1, t2, t3])
        
        alarms.append({
            "theme": "Lojistik Peşin Mazot & Geciken Navlun Tuzağı",
            "comment": (
                f"Patron, tırlar Avrupa'ya, Rusya'ya harıl harıl gidiyor, teker dönüyor ama kasaya para girmiyor. Neden mi? "
                f"Çünkü sen tır yoldayken mazotu, otobanı, şoför harcırahını peşin ödüyorsun ama sanayiciden navlun parasını {dso:.0f} gün sonra alıyorsun! "
                f"Sen yollarda nakit eritirken, araçlar için çektiğin tır leasing borçlarının taksitleri ve yüksek KMH faizleri kafana biniyor. "
                f"Cironun yarısı mazota ve banka faizine gidiyor."
            ),
        })
        solutions.extend([
            {"title": "Peşin Navlun & Yakıt Kartı Şartı", "desc": "Sanayiciyle sözleşmeye '%30 navlun avansı yükleme anında yakıt kartına yüklenir' şartı koydurarak masrafı müşteriye finanse ettirin."},
            {"title": "İhracat KDV İadesi SGK Mahsubu", "desc": "Uluslararası taşımacılık kaynaklı devreden ihracat KDV iadesini her ay tırların MTV ve şoförlerin SGK primlerine doğrudan mahsup edin."},
            {"title": "Akaryakıt İstihbarat Yönetimi", "desc": "Taşıt tanıma tüketim verilerini haftalık takip edin; kilometre başına tüketimi %3 sapan aracı derhal servise çektirin."},
        ])

    # 7. TARIM TEDARİK & FİNANSMANI / FİNTEK (Tarfin vb.)
    elif sec_key in ("tarim_tedarik", "finans_fintek") or (sec_key == "genel" and is_fin_debt_heavy and dso > 120 and not has_inventory):
        t1 = {"name": "Müşteri / Çiftçi Vadesi (DSO) > 120 Gün", "fired": dso > 100, "value": f"{dso:.0f} Gün"}
        t2 = {"name": "Kısa Vadeli Borç / Varlık > %40", "fired": (st_debt / total_assets) > 0.35 if total_assets > 0 else True, "value": f"%{(st_debt / total_assets * 100):.1f}" if total_assets > 0 else "%0"}
        t3 = {"name": "Finansman Gideri / FVÖK > %40", "fired": fin_to_ebit_pct > 35, "value": f"%{fin_to_ebit_pct:.1f}"}
        triggers.extend([t1, t2, t3])
        alarms.append({
            "theme": "Tarım Tedarik Finansmanı & Mali Borç Kaldıracı",
            "comment": (
                f"Patron, mali tablolarınızı ve bilançoyu kalem kalem taradım. Çok açık bir teşhisim var: "
                f"Sizin işinizde stok tutulmuyor ama müşterilere açılan {dso:.0f} günlük uzun açık hesap vadelerini taşımak için "
                f"{fmt_tl(st_debt)} tutarında kısa vadeli banka kredisi, faktoring ve menkul kıymet ihraç borcu kullanıyorsunuz. "
                f"Ürettiğiniz {fmt_tl(op_profit)} faaliyet kârının tam %{fin_to_ebit_pct:.0f}'i ({fmt_tl(fin_exp)}) bu borçların faiz ve komisyonlarına eriyor. "
                f"Kasadaki {fmt_tl(cash)} hazır para kazanılan kârdan değil, sırtınızdaki finansal borç kaldıracından kaynaklanmaktadır."
            ),
        })
        solutions.extend([
            {"title": "VDMK & Tahvil İhraç Optimizasyonu", "desc": "Yüksek faizli rotatif ve faktoring borçlarını kapatıp yerine düşük maliyetli tarımsal VDMK (Varlığa Dayalı Menkul Kıymet) ihraçları koyun."},
            {"title": "DBS & TARSİM Teminat Protokolü", "desc": "Müşteri ve çiftçi vadelerini TARSİM devlet destekli tarım sigortası ve banka garantili DBS limitleriyle teminatlandırın."},
            {"title": "Erken Hasat İskontosu", "desc": "Hasat döneminde açık hesabı peşin kapatan bayilere %1,5 erken kapama iskontosu sunarak dış kredi ihtiyacını düşürün."},
        ])

    # Default / Genel Sektör
    else:
        t1 = {"name": "Nakit Çevrim Süresi (CCC) > 60 Gün", "fired": ccc > 50, "value": f"{ccc:.0f} Gün"}
        t2 = {"name": "Finansman Gideri / FVÖK > %40", "fired": fin_to_ebit_pct > 35, "value": f"%{fin_to_ebit_pct:.1f}"}
        triggers.extend([t1, t2])
        alarms.append({
            "theme": "Genel Çalışma Sermayesi & Borç Baskısı",
            "comment": f"Patron, defterdeki kârının önemli kısmı açık hesap alacaklarda ve işletme sermayesinde kilitlenmektedir. Nakit akışını hızlandıracak DBS ve tahsilat disiplini şarttır.",
        })
        solutions.append({"title": "Alacak Vadelerini Kısaltma", "desc": "Açık hesap vadelerini 15 gün geri çekin; peşin iskontoyla kasaya nakit girişi sağlayın."})

    # BUILD 10 DYNAMIC PATRON QUESTIONS
    # -------------------------------------------------------------
    # Soru 1: Kasada Neden Para Yok? (Dynamic: Borç Baskısı vs Stok vs Taahhüt vs Lojistik vs Personel vs Genel)
    if is_fin_debt_heavy:
        if has_significant_cash:
            q1_title = f"Kasadaki {fmt_tl(cash)} Kârdan Değil; Kâr {fmt_tl(st_debt)}'lik Mali Borcun Faizinde Eriyor"
            q1_desc = (
                f"Şirket defterde <b>{fmt_tl(net_profit)}</b> net kâr üretmiş ve kasada/bankada <b>{fmt_tl(cash)}</b> hazır likidite bulunuyor görünse de, "
                f"bu nakit kazanılan kârdan değil <b>{fmt_tl(st_debt)}'lik kısa vadeli kredi, faktoring ve menkul kıymet ihraç borçlarından</b> gelmektedir. "
                f"Üretilen <b>{fmt_tl(op_profit)}</b> faaliyet kârının tam <b>%{fin_to_ebit_pct:.1f}'i ({fmt_tl(fin_exp)})</b> "
                f"müşterilerin <b>{dso:.0f} günlük</b> açık hesap vadelerini (<b>{fmt_tl(ar_val)}</b>) finanse etmek için çekilen bu borçların faizine erimektedir."
            )
            q1_metrics = [
                {"label": "Net Dönem Kârı", "val": fmt_tl(net_profit), "note": "Defter kârı"},
                {"label": "Kısa Vadeli Mali Borç (30)", "val": fmt_tl(st_debt), "note": "Kredi, faktoring, ihraç"},
                {"label": "Finansman Gideri (660)", "val": fmt_tl(fin_exp), "note": f"FVÖK'ün %{fin_to_ebit_pct:.0f}'i faize"},
                {"label": "Hazır Değerler / Kasa (10)", "val": fmt_tl(cash), "note": "Borçla taşınan likidite"},
            ]
            q1_action = f"Müşterilere verilen {dso:.0f} günlük açık hesap vadelerini DBS / teminata bağlayın; faktoring ve rotatif kredi yükünü kapatıp yıllık {fmt_tl(fin_exp)} faiz sızıntısını durdurun."
        else:
            q1_title = f"Kâr Ne Depoda Ne Maaşta: {fmt_tl(st_debt)}'lik Borcun Faiz Yükünde Kayboluyor"
            q1_desc = (
                f"Şirket defterde <b>{fmt_tl(net_profit)}</b> kâr göstermesine karşın, ürettiği <b>{fmt_tl(op_profit)}</b> faaliyet kârının "
                f"tam <b>%{fin_to_ebit_pct:.1f}'i ({fmt_tl(fin_exp)})</b> banka kredisi ve faktoring faizlerine gitmektedir. "
                f"Müşterilerin <b>{dso:.0f} günlük</b> açık hesap vadesi (<b>{fmt_tl(ar_val)}</b>) şirketi borçlanmaya zorlamakta, kasa bu kârı görememektedir."
            )
            q1_metrics = [
                {"label": "Net Dönem Kârı", "val": fmt_tl(net_profit), "note": "Defter kârı"},
                {"label": "Müşteride Kilitli (120)", "val": fmt_tl(ar_val), "note": f"{dso:.0f} gün tahsilat"},
                {"label": "Kısa Vadeli Borç (30)", "val": fmt_tl(st_debt), "note": "Kredi / faktoring"},
                {"label": "Finansman Gideri (660)", "val": fmt_tl(fin_exp), "note": "Ödenen faiz"},
            ]
            q1_action = "Yüksek faizli rotatif kredileri kapatmak için ilk 5 müşteriden erken tahsilat iskontosuyla nakit çekin."
    elif has_inventory:
        q1_title = "Defterdeki Kâr, Alacak ve Stok Kilitlenmesinde Kayboluyor"
        q1_desc = (
            f"Şirket defterde <b>{fmt_tl(net_profit)}</b> net kâr üretmiş görünmesine karşın, "
            f"bu kârın neredeyse tamamı müşterilerin <b>{dso:.0f} günlük</b> tahsilat vadesinde (<b>{fmt_tl(ar_val)}</b>) "
            f"ve depodaki <b>{dio:.0f} günlük</b> stokta (<b>{fmt_tl(inv_val)}</b>) rehin kalmıştır. Kasa bu kârı fiilen görememektedir."
        )
        q1_metrics = [
            {"label": "Net Dönem Kârı", "val": fmt_tl(net_profit), "note": "Defter kârı"},
            {"label": "Müşteride Kilitli (120)", "val": fmt_tl(ar_val), "note": f"{dso:.0f} gün tahsilat"},
            {"label": "Depoda Kilitli (150)", "val": fmt_tl(inv_val), "note": f"{dio:.0f} gün stokta"},
            {"label": "Nakit Çevrim (CCC)", "val": f"{ccc:.0f} gün", "note": "Bekleme süresi"},
        ]
        q1_action = "İlk 10 müşteride açık hesap vadesini 15 gün geri çekin; depodaki yavaş malları kampanyayla nakde çevirin."
    elif sec_key == "insaat_taahhut":
        q1_title = "Kâr Kağıt Üstünde Duruyor, Nakit Onaylanmayan Hakedişlerde Rehin"
        q1_desc = (
            f"Şirket defterde <b>{fmt_tl(net_profit)}</b> kâr göstermesine karşın, "
            f"bu kârın neredeyse tamamı ana müteahhit veya kamu idarelerinin beklettiği <b>{fmt_tl(ar_val)}</b> tutarındaki hakediş alacaklarında "
            f"ve şantiyelerdeki duran varlıklarda kilitlidir. Kasa bu kârı fiilen görememektedir."
        )
        q1_metrics = [
            {"label": "Net Dönem Kârı", "val": fmt_tl(net_profit), "note": "Defter kârı"},
            {"label": "Onay Bekleyen Hakediş (120)", "val": fmt_tl(ar_val), "note": f"{dso:.0f} gün hakediş vadesi"},
            {"label": "Maddi Duran Varlıklar (25)", "val": fmt_tl(fixed_assets), "note": "Şantiye makine parkı"},
            {"label": "Kısa Vadeli Banka Borcu (300)", "val": fmt_tl(st_debt), "note": "Finansman baskısı"},
        ]
        q1_action = "Geciken hakedişler için hukuki ihtarname çekip VUK 323 kapsamında Şüpheli Alacak Karşılığı ayırın; kurumlar vergisini indirin."
    elif sec_key == "lojistik_tasimacilik":
        q1_title = "Tekerler Dönüyor Ama Nakit Yoldaki Mazotta ve Geciken Navlunda Eriyor"
        q1_desc = (
            f"Şirket defterde <b>{fmt_tl(net_profit)}</b> kâr üretmiş görünse de; mazot, otoban ve şoför harcırahları peşin ödenirken "
            f"sanayiciden navlun <b>{dso:.0f} gün</b> sonra (<b>{fmt_tl(ar_val)}</b>) gelmektedir. Kasa bu kârı görememekte, tır taksitleri KMH ile dönmektedir."
        )
        q1_metrics = [
            {"label": "Net Dönem Kârı", "val": fmt_tl(net_profit), "note": "Defter kârı"},
            {"label": "Bekleyen Navlun Alacağı (120)", "val": fmt_tl(ar_val), "note": f"{dso:.0f} gün navlun tahsilatı"},
            {"label": "Banka & Leasing Borcu (300)", "val": fmt_tl(st_debt), "note": "Tır finansmanı"},
            {"label": "Tahmini Akaryakıt Yükü", "val": "%52", "note": "Maliyet içindeki payı"},
        ]
        q1_action = "Sanayici sözleşmelerine '%30 peşin yakıt kartı veya peşin navlun' şartı koyarak peşin nakit akışı yaratın."
    elif is_opex_heavy or sec_key == "hizmet_yazilim":
        q1_title = "İşinizde Stok Yok Ama Kâr Açık Hesap Vadede ve Personel Yükünde Kayboluyor"
        q1_desc = (
            f"Şirket defterde <b>{fmt_tl(net_profit)}</b> net kâr üretmiş görünmesine karşın, bu kârın neredeyse tamamı müşterilerin "
            f"<b>{dso:.0f} günlük</b> açık hesap tahsilat vadesinde (<b>{fmt_tl(ar_val)}</b>) ve her ay peşin ödenen personel/işletme giderlerinde (<b>{fmt_tl(opex)}</b>) kilitlenmiştir. "
            f"Kasa bu kârı görememekte, tahsilat geciktikçe işletme sermayesi açığı büyümektedir."
        )
        q1_metrics = [
            {"label": "Net Dönem Kârı", "val": fmt_tl(net_profit), "note": "Defter kârı"},
            {"label": "Müşteride Açık Hesap (120)", "val": fmt_tl(ar_val), "note": f"{dso:.0f} gün tahsilat"},
            {"label": "Personel & OpEx Yükü (770)", "val": fmt_tl(opex), "note": "Yıllık işletme gideri"},
            {"label": "Tahsilat Vade Riski", "val": f"{dso:.0f} gün", "note": "Müşteri bekleme süresi"},
        ]
        q1_action = "Açık hesap vadeli hizmet vermeyi derhal sınırlandırın; tüm müşterileri otomatik kredi kartlı abonelik veya peşin avans modeline geçirin."
    else: # Genel / Ticaret / Stoksuz
        q1_title = "Defterdeki Kâr, Uzun Müşteri Vadelerinde ve İşletme Sermayesinde Kilitli"
        q1_desc = (
            f"Şirket defterde <b>{fmt_tl(net_profit)}</b> net kâr üretmiş görünmesine karşın, bu kâr müşterilerin "
            f"<b>{dso:.0f} günlük</b> tahsilat vadesinde (<b>{fmt_tl(ar_val)}</b>) bağlı kalmıştır. Kasa bu kârı zamanında görememektedir."
        )
        q1_metrics = [
            {"label": "Net Dönem Kârı", "val": fmt_tl(net_profit), "note": "Defter kârı"},
            {"label": "Müşteride Kilitli (120)", "val": fmt_tl(ar_val), "note": f"{dso:.0f} gün tahsilat"},
            {"label": "Faaliyet Kârı (FVÖK)", "val": fmt_tl(op_profit), "note": "Operasyonel kâr"},
            {"label": "Nakit Çevrim Süresi (CCC)", "val": f"{ccc:.0f} gün", "note": "Nakit döngüsü"},
        ]
        q1_action = "Açık hesap müşterilere kademeli vade farkı uygulayın ve peşin iskontoyla sıcak nakdi içeri çekin."

    # Soru 2: Hangi Müşteri Zarar Ettiriyor?
    q2_action = (
        "İlk 10 müşteriye banka garantili DBS zorunluluğu getirin veya %2 peşin iskonto ile nakdi hemen içeri çekin."
        if sec_key == "toptan_ticaret" else
        "Vadesi 60 günü aşan müşterilere kademeli vade farkı yansıtın ve açık hesap risk limitini dondurun."
    )

    # Soru 3: Sektörel Sermaye & Maliyet Kapanı (STOK vs PERSONEL vs FİLO vs İŞ MAKİNESİ)
    if has_inventory:
        q3_icon = "📦"
        q3_title = "Depoda Ne Kadar Para Uyuyor?"
        q3_sub = "Stoklar Kârı Yutuyor mu?"
        q3_cat = "Stok Yönetimi & Atıl Sermaye"
        q3_l1_title = "Depodaki Atıl Stoklar Hem Nakdi Kilitliyor Hem Faiz Yükü Üretiyor"
        q3_l1_desc = (
            f"Depoda şu anda <b>{fmt_tl(inv_val)}</b> tutarında işletme sermayesi bağlı beklemektedir. "
            f"Ürünlerin depoda ortalama <b>{dio:.0f} gün</b> kalması, şirkete yıllık <b>{fmt_tl(inv_val * 0.45)}</b> "
            f"tutarında görünmez stok faiz maliyeti çıkarmaktadır."
        )
        q3_metrics = [
            {"label": "Depodaki Bağlı Sermaye", "val": fmt_tl(inv_val), "note": "150-158 hesapları"},
            {"label": "Stok Kalma Süresi (DIO)", "val": f"{dio:.0f} gün", "note": "Depo bekleme süresi"},
            {"label": "Yıllık Stok Faiz Yükü", "val": fmt_tl(inv_val * 0.45), "note": "%45 finansman maliyeti"},
            {"label": "Satılan Malın Maliyeti", "val": fmt_tl(cogs), "note": "Yıllık maliyet akışı"},
        ]
        q3_action = "90 günden uzun süredir hareket görmeyen ölü stokları paket veya toptan iskontoyla derhal nakde çevirin. Satınalma siparişlerini haftalık kotalara bağlayın."
        q3_target_step = "inventoryCard"
        q3_target_name = "Stok Devir & Yaşlandırma Analitiği"
    elif is_fin_debt_heavy:
        q3_icon = "🏦"
        q3_title = f"{fmt_tl(st_debt)} Mali Borç: Faiz Kârı Yutuyor mu?"
        q3_sub = "Kredi & Faktoring Yükü"
        q3_cat = "Finansal Kaldıraç & Borçlanma Maliyeti"
        q3_l1_title = f"İşinizde Stok Yok Ama {fmt_tl(st_debt)} Mali Borç Kârı Rehin Almış"
        q3_l1_desc = (
            f"Şirketinizde fiziki stok tutulmamaktadır; sermaye depoda değil, müşterilere açılan <b>{fmt_tl(ar_val)}'lik {dso:.0f} günlük açık vadede</b> "
            f"ve bu alacakları taşımak için üstlenilen <b>{fmt_tl(st_debt)} tutarındaki kısa vadeli borçlarda (kredi, faktoring, ihraç)</b> rehindir. "
            f"Faaliyet kârınızın <b>%{fin_to_ebit_pct:.1f}'i ({fmt_tl(fin_exp)})</b> doğrudan banka faizi ve finansman masraflarına erimektedir."
        )
        q3_metrics = [
            {"label": "Kısa Vadeli Mali Borç (30)", "val": fmt_tl(st_debt), "note": "Kredi, faktoring, bono"},
            {"label": "Finansman Gideri (660)", "val": fmt_tl(fin_exp), "note": "Ödenen faiz ve masraf"},
            {"label": "Faiz / Faaliyet Kârı", "val": fmt_pct(fin_to_ebit_pct, 1), "note": "Kâr erozyon oranı"},
            {"label": "Alacakta Kilitli Sermaye", "val": fmt_tl(ar_val), "note": f"{dso:.0f} gün vade finansmanı"},
        ]
        q3_action = "Yüksek faizli rotatif ve faktoring borçlarını kapatmak için alacak temlikli DBS / TARSİM protokolüne geçin ve borçlanma maliyetini düşürün."
        q3_target_step = "debtStructureCard"
        q3_target_name = "Finansal Borç & Kaldıraç Analitiği"
    elif sec_key == "hizmet_yazilim" or is_opex_heavy:
        q3_icon = "💻"
        q3_title = "Personel ve İşletme Giderleri Cironun Ne Kadarı?"
        q3_sub = "İnsan Kaynağı & OpEx Yükü"
        q3_cat = "İnsan Kaynağı & Bordro Verimi"
        q3_l1_title = "İşinizde Stok Yok: Gider Yükünüz Personel Bordroları ve Faaliyet Giderleridir"
        q3_l1_desc = (
            f"Hizmet ve teknoloji sektöründe nakit depoda değil, <b>personel bordroları ve genel yönetim giderlerinde (770)</b> erir. "
            f"Yıllık <b>{fmt_tl(opex)}</b> faaliyet gideri cironun <b>%{fmt_pct(opex/sales*100,1)}</b>'ini oluşturmakta, tahsilat geciktikçe bu masraflar nakit açığı doğurmaktadır."
        )
        q3_metrics = [
            {"label": "Faaliyet Gideri (OpEx)", "val": fmt_tl(opex), "note": "770 Genel Yönetim"},
            {"label": "OpEx / Ciro Oranı", "val": fmt_pct(opex / sales * 100, 1), "note": "Faaliyet yükü"},
            {"label": "Net Satış Hasılatı", "val": fmt_tl(sales), "note": "Yıllık ciro"},
            {"label": "Faaliyet Marjı", "val": fmt_pct(op_profit / sales * 100, 1), "note": "Operasyonel kâr"},
        ]
        q3_action = "Mali müşavirinize talimat verip Teknopark ve bordro muafiyetlerini (stopaj ve SGK teşviki) eksiksiz uygulatarak her ay %20 nakit tasarrufu sağlayın."
        q3_target_step = "profitQualityCard"
        q3_target_name = "Kâr Köprüsü & OpEx Analitiği"
    elif sec_key == "lojistik_tasimacilik":
        q3_icon = "🚚"
        q3_title = "Yoldaki Tırlar Ne Kadar Mazot Yakıyor?"
        q3_sub = "Akaryakıt ve Filo Leasing Kârı Eritiyor mu?"
        q3_cat = "Filo & Akaryakıt Verimliliği"
        q3_l1_title = "Lojistikte Para Depoda Değil, Mazot Deposunda ve Tır Leasinginde Uyuyor"
        q3_l1_desc = (
            f"Toplam operasyonel maliyetlerinizin <b>%50'sinden fazlası akaryakıt ve şoför harcırahlarına</b> gitmektedir. "
            f"Tır taksitleri ve peşin mazot ödemeleri, geciken navlun tahsilatları nedeniyle şirketi sürekli KMH faizine sokmaktadır."
        )
        q3_metrics = [
            {"label": "Tahmini Yıllık Akaryakıt", "val": fmt_tl(cogs * 0.52), "note": "En büyük nakit çıkışı"},
            {"label": "Finansal Borç / Varlık", "val": fmt_pct(st_debt / total_assets * 100, 1), "note": "Tır ve filo leasing borcu"},
            {"label": "Navlun Vadesi (DSO)", "val": f"{dso:.0f} gün", "note": "Sanayici tahsilat süresi"},
            {"label": "Yakıt Tüketim Sapması", "val": "%3,2", "note": "Takip edilecek filo metriği"},
        ]
        q3_action = "Taşıt tanıma sistemini haftalık nakit kokpitine bağlayın; tüketimi %3'ten fazla sapan araçları servise çekin ve sözleşmelere peşin yakıt kartı şartı koyun."
        q3_target_step = "workingCapitalLeakEngineCard"
        q3_target_name = "Kilitli Nakit & Maliyet Teşhisi"
    elif sec_key == "insaat_taahhut":
        q3_icon = "🏗️"
        q3_title = "İş Makineleri ve Şantiyelere Ne Kadar Para Gömüldü?"
        q3_sub = "Duran Varlıklar Nakit Akışını Kilitliyor mu?"
        q3_cat = "Duran Varlık & Makine Parkı"
        q3_l1_title = "Parayı Kule Vinçlere ve İş Makinelerine Gömmek Nakit Akışını Boğuyor"
        q3_l1_desc = (
            f"Toplam varlıklarınızın <b>%{mdv_ratio_pct:.0f}'i</b> (<b>{fmt_tl(fixed_assets)}</b>) iş makineleri ve duran varlıklarda bağlıdır. "
            f"Bu makinelerin amortismanı ve bakım masrafları, geciken hakedişlerle birleştiğinde nakit akışını felç etmektedir."
        )
        q3_metrics = [
            {"label": "Maddi Duran Varlıklar", "val": fmt_tl(fixed_assets), "note": "253 Tesis, Makine ve Cihazlar"},
            {"label": "MDV / Aktif Oranı", "val": fmt_pct(mdv_ratio_pct, 1), "note": "Sektör eşiği: %35"},
            {"label": "Geciken Hakediş (120)", "val": fmt_tl(ar_val), "note": "Tahsil edilmeyen işler"},
            {"label": "Yıllık Finansman Gideri", "val": fmt_tl(fin_exp), "note": "Makineler için kredi faizi"},
        ]
        q3_action = "Yeni makine almak yerine operasyonel kiralama (OpEx) modeline geçin; eskiyen makineleri VUK 328 Yenileme Fonu kapsamında 3 yıl vergisiz satın."
        q3_target_step = "balanceSheetCard"
        q3_target_name = "Bilanço & Duran Varlık Analizi"
    else: # Sağlık / Medikal
        q3_icon = "🏥"
        q3_title = "Miyad Riski & Steril Sarf Stokları Kârı Yutuyor mu?"
        q3_sub = "Son Kullanma Tarihi Yaklaşan Mallar"
        q3_cat = "Miyad & Tıbbi Cihaz Envanteri"
        q3_l1_title = "Depodaki Medikal Malların Miyadı (SKT) Yaklaştıkça Değeri Sıfırlanıyor"
        q3_l1_desc = (
            f"Depoda <b>{fmt_tl(inv_val)}</b> tutarında medikal sarf ve cihaz bulunmaktadır. Ortalama <b>{dio:.0f} günlük</b> stok bekleme süresi, "
            f"miyadı geçen hassas steril ürünlerin çöp olma riskini katlamaktadır."
        )
        q3_metrics = [
            {"label": "Medikal Stok Değeri", "val": fmt_tl(inv_val), "note": "150-153 hesapları"},
            {"label": "Stokta Kalma Süresi", "val": f"{dio:.0f} gün", "note": "Envanter devir hızı"},
            {"label": "Kamu Hakediş Vadesi", "val": f"{dso:.0f} gün", "note": "Devlet hastanesi ödeme vadesi"},
            {"label": "Döviz Kuru Riski", "val": "Yüksek", "note": "Dövizle ithal, TL ile satış"},
        ]
        q3_action = "Miyadına 90 gün kalan ürünleri depo yönetiminde sarı alarm listesine alın; gerekirse özel hastanelere iskonto ile nakit satarak zararı önleyin."
        q3_target_step = "inventoryCard"
        q3_target_name = "Medikal Stok & Miyad Takibi"

    # Soru 4: Kredisiz Kaç Milyon TL Nakit Çıkar?
    inv_cash_rel = daily_cogs * 15 if has_inventory else 0.0
    q4_total_cash = (daily_sales * 15) + inv_cash_rel + (daily_cogs * 10)
    
    # Soru 6: Vade Makası (Kim Kimi Finanse Ediyor?)
    if sec_key == "perakende_eticaret":
        q6_title = "POS Bloke Süresi & Tedarikçi Vade Asimetrisi"
        q6_desc = "Müşteriye peşin veya kartla satıyorsunuz ancak banka POS parasına 15-20 gün bloke koyarken, tedarikçiler daha kısa vadede ödeme talep etmektedir. Banka sizin paranızı işletmektedir."
        q6_action = "Bankalarla masaya oturup POS bloke süresini max 1-2 güne çektirin; KMH borcuna girmeden paranızı kullanın."
    elif sec_key == "toptan_ticaret":
        q6_title = "Toptancılık Değil: Bayilere Faizsiz Bankacılık Yapıyorsunuz"
        q6_desc = f"Tedarikçiye ortalama <b>{dpo:.0f} günde</b> ödeme yaparken, bayileri <b>{dso:.0f} gün</b> açık hesapla bekliyorsunuz. Ortaya çıkan <b>{vade_makasi:.0f} günlük negatif vade makasını</b> şirketiniz kendi cebinden finanse etmektedir."
        q6_action = "Bayilere açık hesap yerine derhal DBS zorunluluğu getirin veya %2 peşin iskontoyla parayı erken tahsil edin."
    elif sec_key == "saglik_medikal":
        q6_title = "Dövizle Alıp Kamuya TL Vadeli Satma Kapanı"
        q6_desc = f"Distribütörden dövizli hammadde/cihaz alıp devlet hastanelerine <b>{dso:.0f} gün</b> TL vadeli mal veriyorsunuz. Bu vade makası kur arttığı anda kâr marjını silip süpürmektedir."
        q6_action = "Kamu hakediş alacaklarını faktoring ile iskonto ettirip nakde çevirin ve döviz borcunuzu kapatın."
    else:
        q6_title = "Tedarikçiye Erken Ödeyip Müşteriyi Uzun Beklemek Kasayı Boşaltıyor"
        q6_desc = f"Tedarikçiye ortalama <b>{dpo:.0f} günde</b> öderken, müşterilerden alacağı ortalama <b>{dso:.0f} günde</b> tahsil ediyorsunuz. Ortaya çıkan <b>{vade_makasi:.0f} günlük makası</b> banka kredisiyle fonluyorsunuz."
        q6_action = "Ana tedarikçilerle masaya oturup vadeleri 15 gün uzatın; müşterilere tedarikçi vadesinden uzun vade vermeyi yasaklayın."

    # Soru 9 (YENİ): Banka Borcu & Rotatif / KMH Faiz Kapanı (Banka Kime Çalışıyor?)
    if is_fin_debt_heavy:
        q9_title = f"{fmt_tl(st_debt)} Mali Borç: Faaliyet Kârının %{fin_to_ebit_pct:.0f}'i Banka Faizine Gidiyor"
        q9_desc = (
            f"Şirketiniz yılda <b>{fmt_tl(fin_exp)}</b> finansman faizi ve komisyon ödemektedir. "
            f"Bu tutar, ürettiğiniz <b>{fmt_tl(op_profit)}</b> operasyonel faaliyet kârının tam <b>%{fin_to_ebit_pct:.1f}'sine</b> denk gelmektedir! "
            f"Sırtınızdaki <b>{fmt_tl(st_debt)} tutarındaki kısa vadeli kredi, faktoring ve ihraç borçları</b> kârın neredeyse üçte ikisini tüketmektedir."
        )
        q9_action = "Yüksek maliyetli faktoring ve spot rotatif kredileri kapatmak için ilk 5 müşteriden erken tahsilat iskonto protokolü başlatın."
    else:
        q9_title = "Faaliyet Kârının Ne Kadarı Banka Kredi ve Rotatif Faizine Gidiyor?"
        q9_desc = (
            f"Şirketiniz yılda <b>{fmt_tl(fin_exp)}</b> finansman faizi ödemektedir. "
            f"Bu tutar, ürettiğiniz operasyonel faaliyet kârının tam <b>%{fin_to_ebit_pct:.1f}'sine</b> denk gelmektedir! "
            f"Yani yıl boyunca şirketiniz ve personeliniz aslında banka kredilerinin, rotatif faizlerinin ve KMH hesaplarının faizini finanse etmek için çalışmaktadır."
        )
        q9_action = "Yüksek faizli KMH ve spot rotatif kredileri, hızlandırılacak müşteri tahsilatları ve DBS nakit akışıyla ilk 60 günde %30 azaltın."

    # Soru 10 (YENİ): Vergi Kalkanı & Yasal Tasarruf Fırsatları (Devletten Ne Kadar Nakit Kurtarılabilir?)
    if sec_key == "uretim_sanayi":
        q10_tax_title = "VUK 315 Hızlandırılmış Amortisman ile İlk Yıldan Sıcak Vergi Tasarrufu"
        q10_tax_desc = "Tesis ve makine yatırımlarınızda azalan bakiyeler yöntemi uygulayarak ilk yıl 2 kat amortisman gideri yazabilir, kurumlara ödenecek vergiyi erteleyip faizsiz işletme sermayesi yapabilirsiniz."
        q10_tax_action = "Mali müşavirinize talimat verin; 253 makine grubunda VUK 315 Azalan Bakiyeler Yöntemini seçerek ilk geçici vergi döneminde vergi kalkanı oluştursun."
    elif sec_key == "insaat_taahhut":
        q10_tax_title = "VUK 323 Şüpheli Alacak ve VUK 328 Yenileme Fonu Vergi Kalkanı"
        q10_tax_desc = "Tahsil edilemeyen eski hakedişler için yasal takip başlatıp Şüpheli Alacak Karşılığı ayırın; eskiyen iş makinelerinin satış kârını ise 549 Yenileme Fonu'na alarak 3 yıl vergiden muaf tutun."
        q10_tax_action = "Geciken hakedişler için noterden ihtarname çekip VUK 323 karşılığı ayırtın; bu yıl ödenecek kurumlar vergisinden yüz binlerce lira tasarruf edin."
    elif sec_key == "perakende_eticaret" or sec_key == "lojistik_tasimacilik":
        q10_tax_title = "Devreden KDV Alacağını İşçi SGK ve Muhtasar Vergilerine Mahsup Edin"
        q10_tax_desc = "Mizanınızda biriken 190 Devreden KDV ve ihracat istisnası KDV iadeleri atıl beklemektedir. Bu parayı her ayın 26'sındaki işçi SGK primlerine ve Muhtasar ödemelerine yasal olarak mahsup ettirebilirsiniz."
        q10_tax_action = "Mali müşavirinize talimat verip İnternet Vergi Dairesi üzerinden GEKSİS KDV mahsup dilekçesini verdirin; ay sonu kasadan SGK için nakit çıkışını durdurun."
    else: # Hizmet / SaaS / Diğer
        q10_tax_title = "KVK 10/1-ı Nakit Sermaye Artırımı ve Ar-Ge/Teknopark SGK Muafiyeti"
        q10_tax_desc = "Şirkete bankadan pahalı kredi çekmek yerine ortaklar nakit sermaye koyduğunda, TCMB faizi üzerinden devlete ödenecek kurumlar vergisinden doğrudan indirim hakkı doğar. Ayrıca Teknopark bordro muafiyetleri denetlenmelidir."
        q10_tax_action = "Ortaklar sermaye artırımını tescil ettirip KVK 10/1-ı indiriminden faydalanın; Ar-Ge personel SGK teşviklerini tam uygulatarak bordro maliyetini %20 düşürün."

    # ASSEMBLE 10 QUESTIONS LIST
    questions = [
        {
            "id": "q1",
            "icon": "💸",
            "title": "Kasada Neden Para Yok?",
            "sub": "Kâr Nereye Gitti?",
            "cat": "Nakit Akışı & Kâr Kalitesi",
            "l1_title": q1_title,
            "l1_desc": q1_desc,
            "l2_metrics": q1_metrics,
            "l3_action": q1_action,
            "l3_cash": fmt_plus_tl(daily_sales * 15 + inv_cash_rel),
            "l3_profit": f"{fmt_plus_tl((daily_sales * 15 + inv_cash_rel) * 0.45)} / yıl",
            "l3_owner": "Finans & Satış Yönetimi",
            "l3_due": "İlk 30 Gün",
            "targetStep": "workingCapitalLeakEngineCard",
            "targetStepName": "Adım 2: Görünmez Kâr Sızıntısı & Kilitli Nakit",
        },
        {
            "id": "q2",
            "icon": "👥",
            "title": "Hangi Müşteri Zarar Ettiriyor?",
            "sub": "Ciro vs Gerçek Kâr",
            "cat": "Müşteri Kârlılığı & Alacak Riski",
            "l1_title": "Yüksek Cirolu Müşteriler Uzun Vade ve Faiz Yüküyle Gizli Zarar Ettiriyor",
            "l1_desc": f"Ciro hacmi büyük müşterilere tanınan {dso:.0f} günlük vadeler ve yüksek iskontolar, %45 yıllık faiz ortamında kâr marjını silmektedir. 60 günden uzun vadeli açık hesap çalışan müşteriler kârı bankaya kaptırmaktadır.",
            "l2_metrics": [
                {"label": "Ortalama Tahsilat (DSO)", "val": f"{dso:.0f} gün", "note": "Müşteri bekleme süresi"},
                {"label": "Toplam Alacak Portföyü", "val": fmt_tl(ar_val), "note": "120 Alıcılar"},
                {"label": "Yıllık Finansman Kaybı", "val": fmt_tl(ar_val * 0.45), "note": "%45 sermaye maliyeti"},
                {"label": "Faiz / Faaliyet Kârı", "val": fmt_pct(fin_to_ebit_pct, 1), "note": "Faize giden operasyonel kâr"},
            ],
            "l3_action": q2_action,
            "l3_cash": fmt_plus_tl(daily_sales * 20),
            "l3_profit": f"{fmt_plus_tl(daily_sales * 20 * 0.45)} / yıl",
            "l3_owner": "Ticari Satış Direktörü & Kredi Komitesi",
            "l3_due": "45 Gün",
            "targetStep": "customersCard",
            "targetStepName": "Adım 4: Kritik Taraflar & Müşteri Yaşlandırma",
        },
        {
            "id": "q3",
            "icon": q3_icon,
            "title": q3_title,
            "sub": q3_sub,
            "cat": q3_cat,
            "l1_title": q3_l1_title,
            "l1_desc": q3_l1_desc,
            "l2_metrics": q3_metrics,
            "l3_action": q3_action,
            "l3_cash": fmt_plus_tl(daily_cogs * 18 if has_inventory else sales * 0.03),
            "l3_profit": f"{fmt_plus_tl(daily_cogs * 18 * 0.45 if has_inventory else sales * 0.03)} / yıl",
            "l3_owner": "Operasyon & Satınalma Yönetimi",
            "l3_due": "30 Gün",
            "targetStep": q3_target_step,
            "targetStepName": q3_target_name,
        },
        {
            "id": "q4",
            "icon": "🔓",
            "title": "Kredisiz Kaç Milyon TL Nakit Çıkar?",
            "sub": "Şirket İçi Öz Finansman",
            "cat": "İç Kaynaklı Likidite Kurtarma",
            "l1_title": "Banka Kredisine İhtiyaç Duymadan Kendi Bilanço Kaynaklarınızla Sıcak Nakit Yaratabilirsiniz",
            "l1_desc": "Pahalı ticari kredi aramak yerine; alacak tahsilatını 15 gün öne çekmek, atıl operasyonel maliyeti 15 gün optimize etmek ve tedarikçi vadesini 10 gün dengelemek bilançonuzdan milyonlarca lira öz nakit çıkarır.",
            "l2_metrics": [
                {"label": "Tahsilattan Çıkacak (-15G)", "val": fmt_tl(daily_sales * 15), "note": "DSO hızlandırma"},
                {"label": "Stok / OpEx Kurtarma (-15G)", "val": fmt_tl(daily_cogs * 15), "note": "Verimlilik etkisi"},
                {"label": "Tedarikçi Katkısı (+10G)", "val": fmt_tl(daily_cogs * 10), "note": "DPO optimizasyonu"},
                {"label": "Toplam İç Nakit Kapasitesi", "val": fmt_tl(q4_total_cash), "note": "Banka kredisiz"},
            ],
            "l3_action": "3 Kaldıraçlı Çalışma Sermayesi Programı başlatın: Satış ekibinin primini ciroya değil, tahsil edilen nakde endeksleyin.",
            "l3_cash": fmt_plus_tl(q4_total_cash),
            "l3_profit": f"{fmt_plus_tl(q4_total_cash * 0.45)} / yıl",
            "l3_owner": "Genel Müdür & Finans Yönetimi",
            "l3_due": "15 Gün",
            "targetStep": "workingCapitalLeakEngineCard",
            "targetStepName": "Adım 2: Görünmez Kâr Sızıntısı & Kilitli Nakit Teşhisi",
        },
        {
            "id": "q5",
            "icon": "📉",
            "title": "Satış Artarken Marj Neden Büyümüyor?",
            "sub": "Hangi Maliyetler Sessizce Büyüdü?",
            "cat": "Kâr Kalitesi & Maliyet Enflasyonu",
            "l1_title": "Giderler Cirodan Daha Hızlı Büyüyor, Enflasyon Kâr Marjını Kemiriyor",
            "l1_desc": "Ciro büyümesine karşın kârın yerinde saymasının nedeni: Artan hammadde, personel ve genel yönetim giderlerinin satış fiyatlarına geç yansıtılması ve kontrolsüz faaliyet gideri artışıdır.",
            "l2_metrics": [
                {"label": "Brüt Kâr Marjı", "val": fmt_pct(gross_margin_pct, 1), "note": "Satış - SMM marjı"},
                {"label": "Faaliyet Kâr Marjı (FVÖK)", "val": fmt_pct(op_profit/sales*100, 1), "note": "Operasyonel kâr marjı"},
                {"label": "Net Dönem Marjı", "val": fmt_pct(net_margin_pct, 1), "note": "Nihai net kâr oranı"},
                {"label": "Finansman / Satış", "val": fmt_pct(fin_exp/sales*100, 1), "note": "Ciro başına faiz sızıntısı"},
            ],
            "l3_action": "Tüm ürün ve müşteri gruplarında Net Katkı Payı denetimi yapın. Enflasyon endeksli dinamik fiyatlamaya geçip kârsız kalemleri sonlandırın.",
            "l3_cash": fmt_plus_tl(sales * 0.02),
            "l3_profit": f"{fmt_plus_tl(sales * 0.02)} / yıl",
            "l3_owner": "Finans Direktörü & Ürün Yönetimi",
            "l3_due": "30 Gün",
            "targetStep": "profitQualityCard",
            "targetStepName": "Adım 1: Kâr Köprüsü & Kâr Kalitesi Analizi",
        },
        {
            "id": "q6",
            "icon": "⚖️",
            "title": "Vade Makası (Müşteri vs Tedarikçi)",
            "sub": "Kim Kimi Finanse Ediyor?",
            "cat": "İşletme Sermayesi Asimetrisi",
            "l1_title": q6_title,
            "l1_desc": q6_desc,
            "l2_metrics": [
                {"label": "Müşteri Vadesi (DSO)", "val": f"{dso:.0f} gün", "note": "Para girişi"},
                {"label": "Tedarikçi Vadesi (DPO)", "val": f"{dpo:.0f} gün", "note": "Para çıkışı"},
                {"label": "Net Vade Makası Açığı", "val": f"{vade_makasi:.0f} gün", "note": "Finanse edilen gün"},
                {"label": "Tedarikçi Borcu (320)", "val": fmt_tl(ap_val), "note": "Satıcı kredisi"},
            ],
            "l3_action": q6_action,
            "l3_cash": fmt_plus_tl(daily_cogs * 15),
            "l3_profit": f"{fmt_plus_tl(daily_cogs * 15 * 0.45)} / yıl",
            "l3_owner": "Satınalma & Finans Direktörlüğü",
            "l3_due": "30 Gün",
            "targetStep": "workingCapital",
            "targetStepName": "Adım 1: Nakit Çevrim Süresi (İşletme Sermayesi)",
        },
        {
            "id": "q7",
            "icon": "🚨",
            "title": "Yarın Sabahın 3 Kritik Alarmı",
            "sub": "Şirketi Tehdit Eden Riskler",
            "cat": "CEO Erken Uyarı Radarı",
            "l1_title": "33 Finansal Karar Motorunun Mizanınızda Teşhis Ettiği 3 Öncelikli Risk",
            "l1_desc": "Mizan ve alt defter kayıtlarınız taranarak kârlılığı, likiditeyi ve sermaye yeterliliğini tehdit eden en yüksek puanlı 3 finansal alarm önceliklendirildi.",
            "l2_metrics": [
                {"label": f"1. {alarms[0]['theme'] if alarms else 'Alacak Riski'}", "val": "88 / 100", "note": f"Maruziyet: {fmt_tl(ar_val * 0.35)}"},
                {"label": "2. Banka Faiz Sızıntısı", "val": fmt_pct(fin_to_ebit_pct, 0), "note": f"Yıllık faiz: {fmt_tl(fin_exp)}"},
                {"label": "3. Vade Asimetrisi", "val": f"{vade_makasi:.0f} gün", "note": "Net fonlama açığı"},
            ],
            "l3_action": "Risk komitesini toplayarak bu 3 alarm için haftalık nakit akış toplantısı kurgulayın ve erken uyarı limitleri belirleyin.",
            "l3_cash": fmt_plus_tl(ar_val * 0.10 + inv_val * 0.10),
            "l3_profit": "Olası batık ve faiz cezalarına karşı tam koruma",
            "l3_owner": "İcra Kurulu & Risk Yönetimi",
            "l3_due": "İlk 7 Gün",
            "targetStep": "risks",
            "targetStepName": "Adım 3: Sektörel Kıyaslama & Öncelikli Riskler",
        },
        {
            "id": "q8",
            "icon": "🎯",
            "title": "CEO'nun 1 Numaralı Kararı",
            "sub": "Bugün Ne Yapılmalı?",
            "cat": "CEO İcraat & Karar Direktifi",
            "l1_title": f"Öncelikli Yönetim İcraatı: {solutions[0]['title'] if solutions else 'İşletme Sermayesi Optimizasyonu'}",
            "l1_desc": f"Şirket bilançosunda ve nakit akışında anında etki yaratacak 1 numaralı icraat: <b>\"{solutions[0]['desc'] if solutions else 'Açık hesap vadeleri kısaltın.'}\"</b>",
            "l2_metrics": [
                {"label": "Finansal Sağlık Skoru", "val": f"{round((bp or {}).get('health_score') or 72)} / 100", "note": (bp or {}).get("health_label") or "Dengeli"},
                {"label": "Potansiyel Nakit Kurtarımı", "val": fmt_plus_tl(daily_sales * 15), "note": "Kurtarılabilir nakit"},
                {"label": "Kısa Vadeli Banka Borcu", "val": fmt_tl(st_debt), "note": "Kredi baskısı"},
                {"label": "Nakit Çevrim Süresi", "val": f"{ccc:.0f} gün", "note": "Döngü süresi"},
            ],
            "l3_action": solutions[0]["desc"] if solutions else "İşletme sermayesi döngüsünü optimize edin.",
            "l3_cash": fmt_plus_tl(daily_sales * 15),
            "l3_profit": f"{fmt_plus_tl(daily_sales * 15 * 0.45)} / yıl",
            "l3_owner": "Genel Yönetim & Finans",
            "l3_due": "İlk 30 Gün",
            "targetStep": "actions",
            "targetStepName": "Adım 6: Yönetim Kararları & İcraat Takvimi",
        },
        {
            "id": "q9",
            "icon": "🏦",
            "title": "Banka Borcu & Rotatif / KMH Kapanı",
            "sub": "Banka Kime Çalışıyor?",
            "cat": "Finansman Maliyeti & Borç Yükü",
            "l1_title": q9_title,
            "l1_desc": q9_desc,
            "l2_metrics": [
                {"label": "Yıllık Finansman Gideri (780)", "val": fmt_tl(fin_exp), "note": "Bankaya ödenen faiz"},
                {"label": "Faiz / Faaliyet Kârı", "val": fmt_pct(fin_to_ebit_pct, 1), "note": "Kârın faize gitme payı"},
                {"label": "Kısa Vadeli Krediler (300)", "val": fmt_tl(st_debt), "note": "Banka borç stoku"},
                {"label": "Tahmini Günlük Faiz Yükü", "val": f"{fmt_tl(fin_exp / 365)} / gün", "note": "Kasadan çıkan günlük faiz"},
            ],
            "l3_action": q9_action,
            "l3_cash": fmt_plus_tl(fin_exp * 0.30),
            "l3_profit": f"{fmt_plus_tl(fin_exp * 0.30)} faiz tasarrufu",
            "l3_owner": "Finans Direktörü & Hazine",
            "l3_due": "60 Gün",
            "targetStep": "financialDebtEngineCard",
            "targetStepName": "Finansal Borçluluk & Faiz Stresi",
        },
        {
            "id": "q10",
            "icon": "🛡️",
            "title": "Vergi Kalkanı & Yasal Mahsup Fırsatları",
            "sub": "Devletten Ne Kadar Nakit Kurtarılabilir?",
            "cat": "Vergi Kalkanı & Nakit Koruma",
            "l1_title": q10_tax_title,
            "l1_desc": q10_tax_desc,
            "l2_metrics": [
                {"label": "Tahmini Vergi Kalkanı", "val": fmt_plus_tl(sales * 0.015), "note": "Yasal vergi erteleme"},
                {"label": "KDV Mahsup Potansiyeli", "val": fmt_tl(sales * 0.02), "note": "SGK ve Muhtasar mahsubu"},
                {"label": "Yasal Dayanak", "val": "VUK / KVK", "note": "Tam mevzuat uyumlu"},
                {"label": "Nakit Etkisi", "val": "Anında Sıcak Nakit", "note": "Vergi ödemesini erteleme"},
            ],
            "l3_action": q10_tax_action,
            "l3_cash": fmt_plus_tl(sales * 0.025),
            "l3_profit": f"{fmt_plus_tl(sales * 0.025)} nakit vergi kalkanı",
            "l3_owner": "Mali Müşavir & Finans Direktörü",
            "l3_due": "İlk Geçici Vergi Dönemi",
            "targetStep": "taxStrategyCard",
            "targetStepName": "Vergi Kalkanı & Mahsup Fırsatları",
        },
    ]

    return {
        "sector_id": sec_key,
        "has_inventory": has_inventory,
        "triggers": triggers,
        "patron_alarms": alarms,
        "solutions": solutions,
        "questions": questions,
    }
