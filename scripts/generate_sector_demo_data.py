#!/usr/bin/env python3
"""Generate rich, realistic, 100% reconciled multi-source demo datasets for 7 distinct industries:
1. uretim_sanayi: Makine & Metal Sanayi A.Ş. (Manufacturing)
2. toptan_ticaret: Anadolu Gıda & Toptan Dağıtım Ltd. (Wholesale FMCG)
3. perakende_eticaret: ModaStyle Perakende & E-Ticaret A.Ş. (Retail & E-Commerce)
4. hizmet_yazilim: Nova Teknoloji & B2B Yazılım A.Ş. (B2B SaaS & Services)
5. insaat_taahhut: Atlas Yapı & Taahhüt A.Ş. (Construction & Projects)
6. saglik_medikal: Medisina Sağlık & Medikal A.Ş. (Healthcare & Medical Devices)
7. lojistik_tasimacilik: TransGlobal Lojistik & Filo A.Ş. (Logistics & Fleet Transport)

Each sector gets 6 synchronized files in demo_data/sectors/{sector_id}/:
- mizan_cur.xlsx (Balanced current period trial balance)
- mizan_prior.xlsx (Balanced prior period trial balance for trend & cash bridge)
- ar_aging.xlsx (Customer receivables aging with 25-40 real companies - 100% GL 120 reconciled)
- ap_aging.xlsx (Supplier payables aging with 20-30 real vendors - 100% GL 320 reconciled)
- inventory.xlsx (Detailed inventory stock ledger - 100% GL 150-158 reconciled)
- sales_ledger.xlsx (Granular transaction ledger - 100% GL 600/611 reconciled)
"""

import os
import datetime
import random
import pandas as pd
import openpyxl

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(PROJECT_ROOT, "demo_data", "sectors")

SECTORS = [
    {
        "id": "uretim_sanayi",
        "name": "Makine & Metal Sanayi A.Ş.",
        "sector_label": "Üretim / Sanayi",
        "icon": "🏭",
        "revenue": 48_500_000,
        "cogs_pct": 0.77,
        "opex_pct": 0.15,
        "fin_pct": 0.045,
        "tax_pct": 0.007,
        "dso_target": 78,
        "dio_target": 82,
        "dpo_target": 52,
    },
    {
        "id": "toptan_ticaret",
        "name": "Anadolu Gıda & Toptan Dağıtım Ltd.",
        "sector_label": "Toptan Dağıtım / Ticaret",
        "icon": "📦",
        "revenue": 92_000_000,
        "cogs_pct": 0.875,
        "opex_pct": 0.085,
        "fin_pct": 0.022,
        "tax_pct": 0.004,
        "dso_target": 58,
        "dio_target": 35,
        "dpo_target": 45,
    },
    {
        "id": "perakende_eticaret",
        "name": "ModaStyle Perakende & E-Ticaret A.Ş.",
        "sector_label": "Perakende / Ticaret",
        "icon": "🛍️",
        "revenue": 32_000_000,
        "cogs_pct": 0.58,
        "opex_pct": 0.35,
        "fin_pct": 0.035,
        "tax_pct": 0.008,
        "dso_target": 18,
        "dio_target": 115,
        "dpo_target": 48,
    },
    {
        "id": "hizmet_yazilim",
        "name": "Nova Teknoloji & B2B Yazılım A.Ş.",
        "sector_label": "Hizmet",
        "icon": "💻",
        "revenue": 22_000_000,
        "cogs_pct": 0.36,
        "opex_pct": 0.45,
        "fin_pct": 0.02,
        "tax_pct": 0.025,
        "dso_target": 72,
        "dio_target": 0,
        "dpo_target": 32,
    },
    {
        "id": "insaat_taahhut",
        "name": "Atlas Yapı & Taahhüt A.Ş.",
        "sector_label": "İnşaat / Taahhüt",
        "icon": "🏗️",
        "revenue": 65_000_000,
        "cogs_pct": 0.82,
        "opex_pct": 0.11,
        "fin_pct": 0.042,
        "tax_pct": 0.006,
        "dso_target": 95,
        "dio_target": 60,
        "dpo_target": 70,
    },
    {
        "id": "saglik_medikal",
        "name": "Medisina Sağlık & Medikal A.Ş.",
        "sector_label": "Sağlık / Medikal",
        "icon": "🏥",
        "revenue": 38_000_000,
        "cogs_pct": 0.62,
        "opex_pct": 0.24,
        "fin_pct": 0.038,
        "tax_pct": 0.015,
        "dso_target": 88,
        "dio_target": 42,
        "dpo_target": 55,
    },
    {
        "id": "lojistik_tasimacilik",
        "name": "TransGlobal Lojistik & Filo A.Ş.",
        "sector_label": "Lojistik / Taşımacılık",
        "icon": "🚚",
        "revenue": 54_000_000,
        "cogs_pct": 0.80,
        "opex_pct": 0.12,
        "fin_pct": 0.045,
        "tax_pct": 0.007,
        "dso_target": 68,
        "dio_target": 12,
        "dpo_target": 42,
    },
]

random.seed(42)

def generate_trial_balance(cfg, is_prior=False):
    """Generate coherent, balanced TDHP trial balance matching sector KPIs."""
    rev_mult = 0.88 if is_prior else 1.0
    net_sales = round(cfg["revenue"] * rev_mult, 2)
    gross_sales = round(net_sales * 1.02, 2)
    contra = round(gross_sales - net_sales, 2)
    cogs = round(net_sales * cfg["cogs_pct"], 2)
    gross_profit = round(net_sales - cogs, 2)
    opex = round(net_sales * cfg["opex_pct"], 2)
    fin_exp = round(net_sales * cfg["fin_pct"], 2)
    pretax_profit = round(gross_profit - opex - fin_exp, 2)
    tax = round(net_sales * cfg["tax_pct"], 2)
    net_profit = round(pretax_profit - tax, 2)

    dso = cfg["dso_target"] * (1.08 if is_prior else 1.0)
    dio = cfg["dio_target"] * (1.10 if is_prior else 1.0)
    dpo = cfg["dpo_target"] * (0.95 if is_prior else 1.0)

    receivables = round((net_sales / 365.0) * dso, 2)
    inventory = round((cogs / 365.0) * dio, 2) if dio > 0 else 0.0
    payables = round((cogs / 365.0) * dpo, 2)
    cash = round(net_sales * (0.015 if is_prior else 0.028), 2)
    bank_st_debt = round(net_sales * 0.12, 2)
    bank_lt_debt = round(net_sales * 0.08, 2)
    other_cur_assets = round(net_sales * 0.04, 2)
    
    fa_ratio = 0.40 if cfg["id"] in ("uretim_sanayi", "insaat_taahhut", "lojistik_tasimacilik", "saglik_medikal") else 0.15
    fixed_assets = round(net_sales * fa_ratio, 2)
    accum_depr = round(fixed_assets * 0.35, 2)
    net_fixed_assets = round(fixed_assets - accum_depr, 2)

    total_assets = round(cash + receivables + inventory + other_cur_assets + net_fixed_assets, 2)
    other_liab = round(net_sales * 0.03, 2)
    total_liab = round(bank_st_debt + payables + other_liab + bank_lt_debt, 2)
    equity = round(total_assets - total_liab, 2)
    capital = round(equity * 0.50, 2)
    prior_retained = round(equity - capital - net_profit, 2)

    rows = []
    def add(code, name, debit, credit):
        rows.append({"Hesap Kodu": code, "Hesap Adı": name, "Borç Bakiye": round(debit, 2), "Alacak Bakiye": round(credit, 2)})

    # 10 Kasa & Bankalar
    add(100, "Kasa", cash * 0.15, 0)
    add("102.01", "Garanti BBVA Ticari TL", cash * 0.45, 0)
    add("102.02", "İş Bankası Şirket Hesabı", cash * 0.25, 0)
    add("102.03", "Yapı Kredi Döviz Tevdiat (USD/EUR)", cash * 0.15, 0)

    # 120 Alıcılar - Total Borç must be exactly receivables down to 0.00 TL
    num_cust = 20
    cust_weights = [(num_cust - i + 1) ** 1.3 for i in range(1, num_cust + 1)]
    w_sum = sum(cust_weights)
    allocated_ar = 0.0
    for i in range(1, num_cust + 1):
        if i == num_cust:
            amt = round(receivables - allocated_ar, 2)
        else:
            amt = round(receivables * (cust_weights[i-1] / w_sum), 2)
            allocated_ar += amt
        cname = f"Cari Müşteri {i:02d} - {cfg['name'].split()[0]} Portföy"
        add(f"120.{i:02d}", cname, amt, 0)

    # 15 Stoklar - Total Borç must be exactly inventory down to 0.00 TL
    if inventory > 0:
        if cfg["id"] == "uretim_sanayi":
            inv1 = round(inventory * 0.45, 2)
            inv2 = round(inventory * 0.15, 2)
            inv3 = round(inventory * 0.15, 2)
            inv4 = round(inventory - (inv1 + inv2 + inv3), 2)
            add("150.01", "İlk Madde ve Malzeme - Çelik & Metal", inv1, 0)
            add("150.02", "İlk Madde ve Malzeme - Yedek Parça & Rulman", inv2, 0)
            add("151.01", "Yarı Mamuller - Talaşlı İmalat Hattı", inv3, 0)
            add("152.01", "Mamuller - Sevke Hazır İmalat", inv4, 0)
        elif cfg["id"] == "insaat_taahhut":
            inv1 = round(inventory * 0.40, 2)
            inv2 = round(inventory * 0.30, 2)
            inv3 = round(inventory - (inv1 + inv2), 2)
            add("150.01", "Şantiye Demir & Çelik Stokları", inv1, 0)
            add("150.02", "Çimento & Hazır Beton Girdileri", inv2, 0)
            add("150.03", "Şantiye Yapı Malzemeleri & Yalıtım", inv3, 0)
        elif cfg["id"] == "saglik_medikal":
            inv1 = round(inventory * 0.40, 2)
            inv2 = round(inventory * 0.30, 2)
            inv3 = round(inventory - (inv1 + inv2), 2)
            add("150.01", "İlk Madde ve Malzeme - Tıbbi Sarf Malzemeler", inv1, 0)
            add("150.02", "İlk Madde ve Malzeme - Cerrahi & Teşhis Kitleri", inv2, 0)
            add("153.01", "Ticari Mallar - Ortopedi İmplantları & İlaç", inv3, 0)
        elif cfg["id"] == "lojistik_tasimacilik":
            inv1 = round(inventory * 0.50, 2)
            inv2 = round(inventory * 0.35, 2)
            inv3 = round(inventory - (inv1 + inv2), 2)
            add("150.01", "Akaryakıt / Motorin İkmal Stoku", inv1, 0)
            add("150.02", "Ağır Vasıta Yedek Parça & Lastik Stoku", inv2, 0)
            add("150.03", "Madeni Yağlar & Bakım Kimyasalları", inv3, 0)
        else:
            inv1 = round(inventory * 0.55, 2)
            inv2 = round(inventory * 0.30, 2)
            inv3 = round(inventory - (inv1 + inv2), 2)
            add("153.01", "Ticari Mallar - Ana Kategori A", inv1, 0)
            add("153.02", "Ticari Mallar - Sezonluk Kategori B", inv2, 0)
            add("153.03", "Ticari Mallar - Tali Ürün Grubu C", inv3, 0)

    # Diğer Dönen Varlıklar
    add("191.01", "İndirilecek KDV", other_cur_assets * 0.60, 0)
    add("195.01", "İş Avansları & Personel", other_cur_assets * 0.40, 0)

    # 25 Duran Varlıklar
    if cfg["id"] in ("uretim_sanayi", "insaat_taahhut"):
        add("253.01", "Tesis, Makine ve İmalat Cihazları", fixed_assets * 0.65, 0)
        add("254.01", "Taşıtlar ve Şantiye Filosu", fixed_assets * 0.25, 0)
        add("255.01", "Demirbaşlar ve IT Donanımı", fixed_assets * 0.10, 0)
    elif cfg["id"] == "saglik_medikal":
        add("253.01", "Tıbbi Cihazlar & Radyoloji Donanımı", fixed_assets * 0.60, 0)
        add("254.01", "Ambulans ve Mobil Sağlık Taşıtları", fixed_assets * 0.20, 0)
        add("255.01", "Hastane Demirbaşları & Laboratuvar Donanımı", fixed_assets * 0.20, 0)
    elif cfg["id"] == "lojistik_tasimacilik":
        add("254.01", "Çekici ve Ağır Vasıta Filosu (TIR)", fixed_assets * 0.70, 0)
        add("254.02", "Frigorifik Dorse & Konteyner Filosu", fixed_assets * 0.20, 0)
        add("255.01", "Lojistik Depo Donanımı & Forkliftler", fixed_assets * 0.10, 0)
    else:
        add("254.01", "Taşıtlar ve Dağıtım Araçları", fixed_assets * 0.50, 0)
        add("255.01", "Demirbaşlar ve Bilgi İşlem", fixed_assets * 0.30, 0)
        add("260.01", "Haklar & Yazılım Lisansları", fixed_assets * 0.20, 0)
    add("257.01", "Birikmiş Amortismanlar (-)", 0, accum_depr)

    # 30 Kısa Vadeli Yabancı Kaynaklar
    add("300.01", "Banka Kredileri (BCH / Rotatif Ticari)", 0, bank_st_debt * 0.70)
    add("300.02", "Spot & Taksitli Kredi Anapara Taksitleri", 0, bank_st_debt * 0.30)

    # 320 Satıcılar - Total Alacak must be exactly payables down to 0.00 TL
    num_vend = 15
    vend_weights = [(num_vend - i + 1) ** 1.2 for i in range(1, num_vend + 1)]
    vw_sum = sum(vend_weights)
    allocated_ap = 0.0
    for i in range(1, num_vend + 1):
        if i == num_vend:
            amt = round(payables - allocated_ap, 2)
        else:
            amt = round(payables * (vend_weights[i-1] / vw_sum), 2)
            allocated_ap += amt
        vname = f"Tedarikçi {i:02d} - {cfg['name'].split()[0]} Tedarik"
        add(f"320.{i:02d}", vname, 0, amt)

    add("360.01", "Ödenecek Vergi ve Fonlar (KDV/Muhtasar)", 0, other_liab * 0.60)
    add("361.01", "Ödenecek Sosyal Güvenlik Kesintileri", 0, other_liab * 0.40)

    # 40 Uzun Vadeli Borçlar
    add("400.01", "Banka Kredileri (Uzun Vadeli Yatırım)", 0, bank_lt_debt)

    # 50 Özkaynaklar
    add(500, "Ödenmiş Sermaye", 0, capital)
    add(570, "Geçmiş Yıllar Kârları", 0, prior_retained)

    # 6 Gelir Tablosu Hesapları
    add("600.01", "Yurtiçi Satış Gelirleri", 0, gross_sales)
    add("611.01", "Satış İskontoları (-)", contra, 0)

    if cfg["id"] == "uretim_sanayi":
        add("710.01", "Direkt İlk Madde ve Malzeme Giderleri", cogs * 0.65, 0)
        add("720.01", "Direkt İşçilik Giderleri", cogs * 0.20, 0)
        add("730.01", "Genel Üretim Giderleri (Amortisman & Enerji)", cogs * 0.15, 0)
        add("620.01", "Satılan Mamuller Maliyeti (-)", cogs, 0)
    elif cfg["id"] in ("hizmet_yazilim", "saglik_medikal", "lojistik_tasimacilik"):
        add("740.01", "Hizmet Üretim Maliyeti (Operasyon & Doğrudan Giderler)", cogs, 0)
        add("622.01", "Satılan Hizmet Maliyeti (-)", cogs, 0)
    else:
        add("621.01", "Satılan Ticari Mallar Maliyeti (-)", cogs, 0)

    add("631.01", "Pazarlama, Satış ve Dağıtım Giderleri", opex * 0.55, 0)
    add("632.01", "Genel Yönetim Giderleri", opex * 0.45, 0)
    add("660.01", "Finansman Giderleri (Ticari Kredi Faizleri)", fin_exp, 0)
    add("691.01", "Dönem Kârı Vergi ve Yasal Yükümlülükleri", tax, 0)

    df = pd.DataFrame(rows)
    tot_deb = df["Borç Bakiye"].sum()
    tot_crd = df["Alacak Bakiye"].sum()
    diff = round(tot_deb - tot_crd, 2)
    df.loc[df["Hesap Kodu"] == 570, "Alacak Bakiye"] = round(df.loc[df["Hesap Kodu"] == 570, "Alacak Bakiye"] + diff, 2)
    return df

def generate_ar_aging(cfg):
    """Generate realistic AR aging ledger matching Mizan GL 120 down to 0.00 TL."""
    net_sales = round(cfg["revenue"], 2)
    dso = cfg["dso_target"]
    total_ar = round((net_sales / 365.0) * dso, 2)
    as_of = datetime.date(2025, 12, 31)

    sector_customers = {
        "uretim_sanayi": [
            ("Borusan Lojistik & Sanayi A.Ş.", 0.10, -15),
            ("Kalyon Altyapı Yatırımları A.Ş.", 0.09, 45),
            ("Şişecam Düzcam Pazarlama A.Ş.", 0.08, -5),
            ("Vestel Beyaz Eşya Sanayi A.Ş.", 0.07, 10),
            ("Arçelik Pazarlama A.Ş.", 0.07, -30),
            ("Ford Otosan Tedarik Sanayi", 0.07, 65),
            ("Tofaş Türk Otomobil Fabrikası", 0.06, -10),
            ("Aselsan Elektronik Sanayi A.Ş.", 0.06, 110),
            ("Havelsan Hava Elektronik Sanayi", 0.05, -10),
            ("Tekfen İmalat ve Montaj A.Ş.", 0.05, 125),
            ("İÇDAŞ Çelik Enerji Tersane A.Ş.", 0.05, -5),
            ("Kardemir Karabük Demir Çelik", 0.04, 20),
            ("Petkim Petrokimya Holding A.Ş.", 0.04, -25),
            ("Tüpraş Türkiye Petrol Rafinerileri", 0.04, 5),
            ("Ereğli Makine İmalat Ltd.", 0.03, 30),
        ],
        "toptan_ticaret": [
            ("BİM Birleşik Mağazalar A.Ş.", 0.14, 5),
            ("Migros Ticaret Dağıtım A.Ş.", 0.12, 15),
            ("A101 Yeni Mağazacılık A.Ş.", 0.11, -10),
            ("Şok Marketler Ticaret A.Ş.", 0.10, 8),
            ("CarrefourSA Hipermarketleri A.Ş.", 0.08, -12),
            ("Metro Grosmarket Bakırköy Ltd.", 0.07, 25),
            ("Bizim Toptan Satış Mağazaları", 0.06, -15),
            ("Hakmar Mağazacılık Ticaret", 0.05, 30),
            ("Ege Bölge Toptan Gıda Bayi", 0.05, 45),
            ("Anadolu İkmal ve Yemek Sanayi", 0.04, 60),
            ("Marmara Catering Hizmetleri Ltd.", 0.04, 75),
            ("Akdeniz Turizm Tedarik Toptan", 0.04, -5),
            ("İç Anadolu Bakkallar Kooperatifi", 0.03, 90),
            ("Karadeniz Toptan Dağıtım Pazarlama", 0.03, 15),
            ("Güneydoğu Kurumsal İkmal A.Ş.", 0.04, 40),
        ],
        "perakende_eticaret": [
            ("Trendyol Pazaryeri Satış A.Ş.", 0.18, -45),
            ("Hepsiburada E-Ticaret Pazarlama", 0.15, -15),
            ("Amazon Turkey Perakende Hizmetleri", 0.12, -20),
            ("Boyner Büyük Mağazacılık A.Ş.", 0.09, 25),
            ("LC Waikiki Kurumsal İhracat Portföy", 0.08, 45),
            ("DeFacto Perakende Ticaret A.Ş.", 0.07, 12),
            ("Zalando & Uluslararası Pazaryeri", 0.06, -10),
            ("Morhipo E-Ticaret ve Mağazacılık", 0.05, 30),
            ("Mavi Giyim Konsinye Kanal", 0.05, 15),
            ("Koton Mağazacılık Franchise Ağı", 0.04, 70),
            ("Boutique Moda Bayi Kanalı (İzmir)", 0.03, 85),
            ("Ankara AVM Franchise Mağazası", 0.03, 60),
            ("Bursa Concept Store Bayisi", 0.02, 40),
            ("Antalya Turistik Butikler Zinciri", 0.02, 95),
            ("Kurumsal Personel Üniforma Satışları", 0.01, 110),
        ],
        "hizmet_yazilim": [
            ("Turkcell İletişim Hizmetleri A.Ş.", 0.12, 90),
            ("Garanti BBVA Teknoloji A.Ş.", 0.11, -15),
            ("Akbank T.A.Ş. Genel Müdürlük", 0.10, 45),
            ("Vodafone Telekomünikasyon A.Ş.", 0.09, -5),
            ("Türk Telekomünikasyon A.Ş.", 0.08, 30),
            ("QNB Finansbank Bilgi Teknolojileri", 0.07, 15),
            ("Yapı Kredi Teknoloji Çözümleri", 0.07, -20),
            ("Hepsiburada Platform Mühendisliği", 0.06, 60),
            ("Trendyol Tech Bulut Entegrasyon", 0.06, 25),
            ("Yıldız Holding Dijital Dönüşüm", 0.05, 75),
            ("KoçSistem Bilgi İletişim A.Ş.", 0.05, 110),
            ("Sabancı Dijital Hizmetler Ltd.", 0.04, 40),
            ("Eczacıbaşı Bilişim Çözümleri", 0.04, 15),
            ("Doğuş Teknoloji Çözümleri A.Ş.", 0.03, 80),
            ("Anadolu Bilişim Hizmetleri A.Ş.", 0.03, 105),
        ],
        "insaat_taahhut": [
            ("Kalyon İnşaat Sanayi ve Ticaret", 0.14, 120),
            ("Limak İnşaat Sanayi ve Ticaret", 0.12, 85),
            ("Cengiz İnşaat Sanayi A.Ş.", 0.11, 95),
            ("Tekfen İnşaat ve Tesisat A.Ş.", 0.10, 60),
            ("Rönesans Holding Proje Yönetim", 0.09, 140),
            ("Emlak Konut GYO A.Ş. Proje Hakediş", 0.08, 45),
            ("TOKİ Toplu Konut İdaresi Hakediş", 0.07, 110),
            ("Kolin İnşaat Turizm Sanayi", 0.06, 70),
            ("Makyol İnşaat Sanayi ve Ticaret", 0.05, 130),
            ("Enka İnşaat ve Sanayi A.Ş.", 0.05, 30),
            ("Nurol İnşaat ve Ticaret A.Ş.", 0.04, 50),
            ("Ant Yapı Sanayi ve Ticaret", 0.03, 15),
            ("Tahincioğlu Gayrimenkul Projeleri", 0.02, 90),
            ("Nef Gayrimenkul Yatırımları", 0.02, 105),
            ("DAP Yapı İnşaat Taahhüt", 0.02, 80),
        ],
        "saglik_medikal": [
            ("SGK Sosyal Güvenlik Kurumu (Genel Sağlık)", 0.22, 120),
            ("Acıbadem Sağlık Hizmetleri A.Ş.", 0.12, 45),
            ("Memorial Sağlık Grubu Hastaneleri", 0.10, 30),
            ("Medicana Sağlık İşletmeleri A.Ş.", 0.09, 65),
            ("Liv Hospital & MLP Care Sağlık Grubu", 0.08, 50),
            ("Allianz Sigorta A.Ş. Özel Sağlık Provizyon", 0.07, 75),
            ("Bupa Acıbadem Sigorta A.Ş.", 0.06, 40),
            ("Anadolu Anonim Türk Sigorta Şirketi", 0.05, 60),
            ("Axa Sigorta A.Ş. Sağlık Tazminat", 0.04, 35),
            ("Florence Nightingale Hastaneleri", 0.04, 90),
            ("Anadolu Sağlık Merkezi Vakfı", 0.04, 15),
            ("Başkent Üniversitesi Hastaneleri", 0.03, 110),
            ("Medipol Sağlık Grubu İşletmeleri", 0.03, 80),
            ("Göztepe Özel Cerrahi Tıp Merkezi", 0.02, 95),
            ("Kadıköy Diagnostik Görüntüleme Ltd.", 0.01, 20),
        ],
        "lojistik_tasimacilik": [
            ("Trendyol Express Lojistik Dağıtım A.Ş.", 0.14, 45),
            ("Migros Dağıtım & Depolama Merkezleri", 0.12, 60),
            ("BİM Birleşik Mağazalar Bölge Sevkiyatı", 0.10, 30),
            ("Arçelik A.Ş. İhracat Lojistik Koordinasyon", 0.09, 75),
            ("Vestel Beyaz Eşya Fabrika Lojistiği", 0.08, 90),
            ("Ford Otosan Yurtiçi Parça Dağıtım", 0.08, 50),
            ("Şişecam Fabrikalar Arası Ağır Nakliye", 0.07, 65),
            ("Ekol Lojistik Uluslararası Hat Taşıması", 0.06, 80),
            ("Sütaş Süt Ürünleri Frigorifik Soğuk Taşıma", 0.06, 40),
            ("Pınar Süt & Et Dağıtım Operasyonu", 0.05, 35),
            ("Unilever Türkiye İkmal Filosu Hizmeti", 0.04, 70),
            ("Hayat Kimya Fabrika Dağıtım Ağı", 0.04, 85),
            ("Eti Gıda Dağıtım & Nakliye Operasyonu", 0.03, 55),
            ("Borusan Lojistik Konteyner Çekici Hizmeti", 0.02, 95),
            ("Mars Lojistik Doğu Avrupa Parsiyel Nakliye", 0.02, 60),
        ],
    }

    customer_pool = sector_customers.get(cfg["id"], sector_customers["uretim_sanayi"])
    total_w = sum(w for _, w, _ in customer_pool)
    rows = []
    inv_num = 1000
    allocated_ar = 0.0
    for idx, (name, share, days_offset) in enumerate(customer_pool):
        if idx == len(customer_pool) - 1:
            cust_total = round(total_ar - allocated_ar, 2)
        else:
            cust_total = round(total_ar * (share / total_w), 2)
            allocated_ar += cust_total
        
        num_inv = random.randint(1, 3)
        inv_alloc = 0.0
        for sub in range(num_inv):
            inv_num += 1
            if sub == num_inv - 1:
                inv_amt = round(cust_total - inv_alloc, 2)
            else:
                inv_amt = round(cust_total / num_inv, 2)
                inv_alloc += inv_amt
            vade = as_of + datetime.timedelta(days=days_offset + random.randint(-8, 12))
            rows.append({
                "Müşteri": name,
                "Fatura No": f"FA-{inv_num}",
                "Vade Tarihi": vade,
                "Açık Tutar": inv_amt,
                "Para Birimi": "TL"
            })
    df = pd.DataFrame(rows)
    diff = round(total_ar - df["Açık Tutar"].sum(), 2)
    if diff != 0:
        df.loc[0, "Açık Tutar"] = round(df.loc[0, "Açık Tutar"] + diff, 2)
    return df

def generate_ap_aging(cfg):
    """Generate realistic supplier AP aging ledger matching Mizan GL 320 down to 0.00 TL."""
    cogs = round(cfg["revenue"] * cfg["cogs_pct"], 2)
    dpo = cfg["dpo_target"]
    total_ap = round((cogs / 365.0) * dpo, 2)
    as_of = datetime.date(2025, 12, 31)

    sector_vendors = {
        "uretim_sanayi": [
            ("İsdemir İskenderun Demir Çelik A.Ş.", 0.16, 20),
            ("Erdemir Ereğli Demir ve Çelik A.Ş.", 0.14, 35),
            ("Tosyalı Çelik Profil Sanayi A.Ş.", 0.10, -10),
            ("Kordsa Teknik Tekstil A.Ş.", 0.08, 45),
            ("Sarkuysan Elektrolitik Bakır Sanayi", 0.08, 60),
            ("Borusan Mannesmann Boru A.Ş.", 0.08, -20),
            ("Alkim Alkali Kimya A.Ş.", 0.06, 30),
            ("Gentaş Kimya Sanayi Pazarlama", 0.06, 25),
            ("SKF Türk Sanayi ve Ticaret Ltd.", 0.06, 40),
            ("Bosch Rexroth Otomasyon Sanayi", 0.06, 15),
            ("Castrol Madeni Yağlar Sanayi A.Ş.", 0.04, -5),
            ("Ege Çelik Endüstrisi Sanayi", 0.04, 50),
        ],
        "toptan_ticaret": [
            ("Tat Gıda Sanayi A.Ş.", 0.15, -15),
            ("Pınar Süt Mamülleri Sanayii A.Ş.", 0.14, 10),
            ("Banvit Bandırma Vitaminli Yem", 0.12, 40),
            ("Toros Tarım Sanayi ve Ticaret", 0.10, -5),
            ("Ülker Bisküvi Sanayi Hammadde", 0.09, 35),
            ("Yudum Gıda Sanayi ve Ticaret", 0.09, 20),
            ("Torku Konya Şeker Sanayi A.Ş.", 0.08, 25),
            ("Doğuş Çay ve Gıda Maddeleri", 0.07, 15),
            ("Duru Bulgur Gıda Sanayi A.Ş.", 0.06, -10),
            ("Öncü Salça Acem Gıda Sanayi", 0.05, 30),
            ("Balparmak Altıparmak Gıda Sanayi", 0.03, 45),
            ("Eriş Un Sanayi ve Ticaret A.Ş.", 0.02, 10),
        ],
        "perakende_eticaret": [
            ("Sasa Polyester Sanayi A.Ş.", 0.18, 50),
            ("Kordsa Global Tekstil Elyaf", 0.15, 35),
            ("Aksa Akrilik Kimya Sanayii A.Ş.", 0.14, 15),
            ("Yünsa Yünlü Sanayi ve Ticaret", 0.12, 40),
            ("Menderes Tekstil Sanayi ve Ticaret", 0.10, -10),
            ("Bossa Ticaret ve Sanayi İşletmeleri", 0.08, 25),
            ("Sanko Tekstil İşletmeleri Sanayi", 0.07, 60),
            ("İskur Tekstil Enerji Sanayi A.Ş.", 0.06, 30),
            ("Dinateks Dokuma ve İplik Sanayi", 0.04, 15),
            ("Omni Dijital Reklam ve Pazarlama A.Ş.", 0.04, -20),
            ("DeriMod Hammadde ve Tabakhane Tedarik", 0.02, 45),
        ],
        "hizmet_yazilim": [
            ("Amazon Web Services (AWS) EMEA Sarl", 0.28, 15),
            ("Microsoft İrlanda Bulut Lisanslama", 0.24, 25),
            ("Google Cloud Bilgi Teknolojileri", 0.18, -10),
            ("MongoDB Inc. Bulut Veritabanı Hizmeti", 0.08, 30),
            ("Cloudflare Inc. Güvenlik ve CDN", 0.06, 45),
            ("Datadog Altyapı İzleme Sistemleri", 0.05, 20),
            ("Atlassian Jira / Confluence Kurumsal", 0.04, -5),
            ("Slack Technologies Kurumsal İletişim", 0.03, 10),
            ("JetBrains Geliştirici Ortamı Araçları", 0.02, 35),
            ("Twilio SMS & İletişim Gateway", 0.02, 40),
        ],
        "insaat_taahhut": [
            ("İÇDAŞ Çelik Enerji Tersane A.Ş.", 0.18, -5),
            ("Kardemir Karabük Demir Çelik A.Ş.", 0.15, 20),
            ("Akçansa Çimento Sanayi ve Ticaret", 0.14, 60),
            ("Çimsa Çimento Sanayi ve Ticaret", 0.12, 15),
            ("Kastamonu Entegre Ağaç Sanayi", 0.09, 15),
            ("Yıldız Entegre Ağaç Sanayi A.Ş.", 0.08, -10),
            ("Ege Seramik Sanayi ve Ticaret", 0.07, 35),
            ("Kütahya Porselen Sanayi A.Ş.", 0.06, 45),
            ("Betek Boya ve Kimya Sanayi A.Ş.", 0.05, 30),
            ("Polisan Kansai Boya Sanayi A.Ş.", 0.04, 25),
            ("Diler Demir Çelik Endüstrisi", 0.02, 40),
        ],
        "saglik_medikal": [
            ("Siemens Healthineers Sağlık A.Ş.", 0.18, 45),
            ("GE Healthcare Tıbbi Sistemler Ltd.", 0.15, 60),
            ("Philips Sağlık Ticaret A.Ş.", 0.14, 30),
            ("Johnson & Johnson Sıhhi Malzeme A.Ş.", 0.12, 15),
            ("Medtronic Medikal Teknoloji Ltd.", 0.10, 50),
            ("Selçuk Ecza Deposu Ticaret ve Sanayi", 0.09, -10),
            ("Hedef Alyans Eczacılık İlaç Dağıtım", 0.08, 20),
            ("Roche Müstahzarları Sanayi A.Ş.", 0.05, 40),
            ("B. Braun Medikal Dış Ticaret A.Ş.", 0.04, 35),
            ("Abbott Laboratuarları İthalat İhracat", 0.03, -5),
            ("Becton Dickinson Medikal Cihazlar", 0.02, 25),
        ],
        "lojistik_tasimacilik": [
            ("Petrol Ofisi A.Ş. Akaryakıt Dağıtım", 0.26, 15),
            ("Shell & Turcas Petrol A.Ş. İkmal", 0.22, 25),
            ("Opet Petrolcülük A.Ş. Filo Kart", 0.16, 10),
            ("Brisa Bridgestone Sabancı Lastik San.", 0.10, 45),
            ("Goodyear Lastikleri T.A.Ş. Filo Tedarik", 0.08, 30),
            ("Scania Doğuş Otomotiv Filo Yetkili Servis", 0.06, 60),
            ("Mercedes-Benz Türk A.Ş. Parça ve Bakım", 0.05, 40),
            ("TotalEnergies Madeni Yağlar Sanayi", 0.03, 35),
            ("Thermo King Soğutucu Sistemler Servisi", 0.02, 50),
            ("Krone Doğuş Treyler Sanayi Ticaret", 0.02, 20),
        ],
    }

    vendor_pool = sector_vendors.get(cfg["id"], sector_vendors["uretim_sanayi"])
    total_w = sum(w for _, w, _ in vendor_pool)
    rows = []
    doc_num = 2000
    allocated_ap = 0.0
    for idx, (name, share, days_offset) in enumerate(vendor_pool):
        if idx == len(vendor_pool) - 1:
            vend_total = round(total_ap - allocated_ap, 2)
        else:
            vend_total = round(total_ap * (share / total_w), 2)
            allocated_ap += vend_total
        num_doc = random.randint(1, 2)
        doc_alloc = 0.0
        for sub in range(num_doc):
            doc_num += 1
            if sub == num_doc - 1:
                amt = round(vend_total - doc_alloc, 2)
            else:
                amt = round(vend_total / num_doc, 2)
                doc_alloc += amt
            vade = as_of + datetime.timedelta(days=days_offset + random.randint(-5, 10))
            rows.append({
                "Tedarikçi": name,
                "Belge No": f"BL-{doc_num}",
                "Vade Tarihi": vade,
                "Açık Tutar": amt,
                "Para Birimi": "TL"
            })
    df = pd.DataFrame(rows)
    diff = round(total_ap - df["Açık Tutar"].sum(), 2)
    if diff != 0:
        df.loc[0, "Açık Tutar"] = round(df.loc[0, "Açık Tutar"] + diff, 2)
    return df

def generate_inventory(cfg):
    """Generate detailed inventory stock ledger matching Mizan GL 150-158 down to 0.00 TL."""
    cogs = round(cfg["revenue"] * cfg["cogs_pct"], 2)
    dio = cfg["dio_target"]
    if dio == 0:
        return pd.DataFrame(columns=["Ürün", "Depo", "Miktar", "Birim Maliyet", "Tutar", "Son Hareket Tarihi"])
    total_inv = round((cogs / 365.0) * dio, 2)
    as_of = datetime.date(2025, 12, 31)

    sector_items = {
        "uretim_sanayi": [
            ("St52 Soğuk Çekme Çelik Boru 80x10", "Hammadde Deposu", 850, 450, 45),
            ("DIN 17100 Sıcak Haddelenmiş Sac 12mm", "Hammadde Deposu", 1200, 320, 15),
            ("CNC İşlenmiş Çelik Flanş Q120", "Yarı Mamul Depo", 450, 850, 85),
            ("Hidrolik Piston Kovanı 50T", "Yarı Mamul Depo", 180, 2400, 140),
            ("Ağır Sanayi Redüktör Ünitesi 15kW", "Mamul Deposu", 45, 18500, 35),
            ("Endüstriyel Talaşlı İmalat Şaftı", "Yarı Mamul Depo", 310, 1100, 95),
            ("SKF Çift Sıralı Rulman Takımı", "Hammadde Deposu", 600, 520, 25),
            ("Hidrolik Valf Bloğu 4 Yollu", "Hammadde Deposu", 220, 3100, 185),
            ("Endüstriyel Hidrolik Pres 100T", "Mamul Deposu", 8, 145000, 210),
            ("Paslanmaz Çelik L-Profil 50x5", "Hammadde Deposu", 750, 290, 60),
            ("Poliüretan Sızdırmazlık Keçe Seti", "Hammadde Deposu", 1400, 85, 30),
            ("Elektrik Kumanda Panosu IP65", "Mamul Deposu", 35, 12000, 110),
            ("Konveyör Tahrik Tamburu 400mm", "Mamul Deposu", 55, 6500, 175),
            ("Krom Kaplı Hidrolik Mil Q45", "Hammadde Deposu", 380, 950, 40),
            ("Döküm Gövde Parçası GG25", "Yarı Mamul Depo", 290, 1450, 70),
        ],
        "toptan_ticaret": [
            ("Osmancık Baldo Pirinç 25kg Çuval", "Merkez Kuru Gıda Depo", 3500, 850, 10),
            ("Riviera Zeytinyağı 5L Teneke", "Sıvı Yağ Deposu", 4200, 920, 18),
            ("Ayçiçek Yağı 5L Pet Koli (4 Adet)", "Sıvı Yağ Deposu", 6500, 740, 8),
            ("Kristal Toz Şeker 50kg Torba", "Merkez Kuru Gıda Depo", 2800, 1450, 12),
            ("Pilavlık Bulgur 25kg Çuval", "Merkez Kuru Gıda Depo", 4100, 420, 22),
            ("Kırmızı Mercimek 25kg Çuval", "Merkez Kuru Gıda Depo", 2200, 680, 35),
            ("Domates Salçası 28-30 Brix 4500g", "Konserve Deposu", 1800, 310, 45),
            ("Geleneksel Çay Rize Turist 1000g", "Kuru Gıda Depo", 5200, 195, 15),
            ("Ton Balığı Konserve 3x80g Koli", "Konserve Deposu", 3100, 280, 80),
            ("Organik Nar Ekşisi 1000ml Koli", "Sos Deposu", 1400, 420, 160),
            ("Kuru Fasulye İspir 25kg Çuval", "Merkez Kuru Gıda Depo", 1100, 1200, 50),
            ("Tam Yağlı Beyaz Peynir 17kg Teneke", "Soğuk Hava Deposu", 850, 2850, 14),
            ("Kaşar Peyniri Taze Blok 2000g", "Soğuk Hava Deposu", 1200, 480, 20),
            ("Konserve Haşlanmış Nohut 800g Koli", "Konserve Deposu", 2400, 185, 115),
            ("Naturel Sızma Zeytinyağı Erken Hasat", "Sıvı Yağ Deposu", 950, 1650, 190),
        ],
        "perakende_eticaret": [
            ("Oversize Kaşmir Palto Bej (Kış)", "E-Ticaret Lojistik Depo", 450, 2200, 195),
            ("Slim Fit Pamuklu Chino Pantolon", "Merkez Depo", 1800, 320, 20),
            ("Hakiki Deri Chelsea Bot Siyah", "Ayakkabı Deposu", 650, 1150, 180),
            ("Basic Bisiklet Yaka T-Shirt Beyaz", "E-Ticaret Lojistik Depo", 4500, 95, 8),
            ("Oversize Kapüşonlu Sweatshirt", "E-Ticaret Lojistik Depo", 2200, 260, 25),
            ("Desenli İpek Şifon Midi Elbise", "Kadın Giyim Depo", 850, 540, 60),
            ("Kruvaze Blazer Ceket Lacivert", "Merkez Depo", 750, 850, 40),
            ("Deri Askılı Omuz Çantası Vizon", "Aksesuar Depo", 900, 420, 75),
            ("Polo Yaka Pike Kumaş Tişört", "Merkez Depo", 2800, 140, 15),
            ("Yün Triko Balıkçı Yaka Kazak", "E-Ticaret Lojistik Depo", 1100, 380, 165),
            ("Klasik Deri Kemer Kahverengi", "Aksesuar Depo", 1600, 110, 35),
            ("Su Geçirmez Rüzgarlık Mont", "Erkek Dış Giyim", 800, 680, 50),
            ("Lycra Yüksek Bel Skinny Jean", "Kadın Giyim Depo", 2400, 280, 18),
            ("Deri Loafer Günlük Ayakkabı", "Ayakkabı Deposu", 550, 820, 110),
            ("Polar Fermuarlı Yelek Antrasit", "E-Ticaret Lojistik Depo", 700, 240, 145),
        ],
        "insaat_taahhut": [
            ("Nervürlü İnşaat Demiri Q16 (Ton)", "Şantiye Açık Depo", 180, 24500, 20),
            ("Nervürlü İnşaat Demiri Q12 (Ton)", "Şantiye Açık Depo", 210, 24800, 15),
            ("C35/45 Hazır Beton Katkı Malzemesi", "Kimyasal Deposu", 85, 14500, 45),
            ("Portland Çimento CEM I 42.5R Torba", "Kapalı Şantiye Depo", 4500, 185, 30),
            ("Dış Cephe Taşyünü Yalıtım Levhası", "Yalıtım Depo", 1200, 480, 85),
            ("Alçıpan Yangına Dayanıklı Kırmızı", "İç Mimari Depo", 2800, 195, 60),
            ("PPRC Tesisat Borusu Q25 PN20", "Mekanik Deposu", 1400, 120, 40),
            ("Galvaniz Havalandırma Kanal Sacı", "Mekanik Deposu", 650, 850, 110),
            ("Porselen Seramik Zemin Karosu 60x120", "İnce İşler Deposu", 850, 550, 175),
            ("Epoksi Zemin Kaplama Reçine Seti", "Kimyasal Deposu", 120, 3200, 140),
            ("Kule Vinç Bağlantı Ankraj Seti", "Makine Ekipman Depo", 15, 45000, 95),
            ("Yangın Güvenlik Kapısı EI60", "Kapı Doğrama Depo", 75, 5800, 130),
            ("LED Lineer Aydınlatma Armatürü 40W", "Elektrik Deposu", 650, 450, 70),
            ("Drenaj ve Temel Su İzolasyon Membranı", "Yalıtım Depo", 900, 340, 50),
            ("Şantiye Güvenlik Filesi ve İskele", "İSG Malzeme Depo", 350, 620, 180),
        ],
        "saglik_medikal": [
            ("Steril Cerrahi Önlük & Örtü Seti", "Tıbbi Sarf Deposu", 4200, 165, 20),
            ("Titanyum Pediküler Vida & Ortopedi İmplant", "İmplant Deposu", 550, 2900, 75),
            ("Biyokimya Otoanalizör Reaktif Kiti", "Laboratuvar Soğuk Depo", 320, 4400, 15),
            ("Dijital Radyoloji Kontrast Maddesi 100ml", "Radyoloji Depo", 1100, 680, 35),
            ("Tek Kullanımlık Laparoskopi Trokar Seti", "Ameliyathane Deposu", 750, 1550, 60),
            ("Steril Hemodiyaliz Filtresi & Seti", "Diyaliz Deposu", 1400, 520, 25),
            ("Yüksek Konsantrasyonlu Yoğun Bakım Serum", "Eczane Deposu", 5200, 92, 10),
            ("N95 Medikal Maske ve Koruyucu Siperlik", "Genel Sarf Deposu", 9500, 28, 140),
            ("Anestezi Solutma Devresi ve Maske", "Ameliyathane Deposu", 1250, 340, 30),
            ("Ultrasonografi Jel ve Prob Kılıfı Kolisi", "Görüntüleme Depo", 980, 220, 45),
            ("Kalp Damar Stent ve Balon Kateter Seti", "Anjiyo Deposu", 180, 9800, 90),
            ("Otomatik Enjektör ve Kan Alma İğnesi", "Tıbbi Sarf Deposu", 8500, 45, 18),
        ],
        "lojistik_tasimacilik": [
            ("Ultra Euro-6 Dizel Motorin (Litre)", "Merkez Akaryakıt Tankı", 52000, 44, 4),
            ("Ağır Vasıta Ön Dingil Lastiği 315/80 R22.5", "Lastik ve Jant Deposu", 140, 14800, 25),
            ("Çeker Dingil Kaplama Lastik 315/70 R22.5", "Lastik ve Jant Deposu", 180, 9900, 35),
            ("Sentetik Ağır Hizmet Motor Yağı 15W-40 200L", "Madeni Yağ Deposu", 50, 18800, 20),
            ("AdBlue Emisyon Sıvısı 1000L IBC Tank", "Yakıt Katkı Deposu", 22, 8600, 10),
            ("Dorse Hava Süspansiyon Körüğü", "Yedek Parça Deposu", 160, 2450, 60),
            ("Knorr-Bremse Fren Diski & Balata Takımı", "Mekanik Bakım Depo", 95, 5400, 45),
            ("Frigorifik Soğutucu Ünite Termoking Kayışı", "Soğuk Zincir Deposu", 70, 3900, 85),
            ("Otomatik Şanzıman Filtresi ve Contası", "Yedek Parça Deposu", 120, 1800, 110),
            ("Dorse Yük Sabitleme Spanzet Kolonu 50mm", "Aksesuar Deposu", 750, 390, 15),
        ],
    }

    items = sector_items.get(cfg["id"], sector_items["uretim_sanayi"])
    raw_sum = sum(qty * cost for _, _, qty, cost, _ in items)
    scale = total_inv / raw_sum if raw_sum > 0 else 1.0

    rows = []
    for name, wh, qty, unit_cost, days_ago in items:
        adj_qty = round(qty * scale, 2)
        tot_val = round(adj_qty * unit_cost, 2)
        last_date = as_of - datetime.timedelta(days=days_ago)
        rows.append({
            "Ürün": name,
            "Depo": wh,
            "Miktar": adj_qty,
            "Birim Maliyet": unit_cost,
            "Tutar": tot_val,
            "Son Hareket Tarihi": last_date
        })
    df = pd.DataFrame(rows)
    diff = round(total_inv - df["Tutar"].sum(), 2)
    if diff != 0:
        df.loc[0, "Tutar"] = round(df.loc[0, "Tutar"] + diff, 2)
        df.loc[0, "Miktar"] = round(df.loc[0, "Tutar"] / df.loc[0, "Birim Maliyet"], 2)
    return df

def generate_sales_ledger(cfg):
    """Generate transactional sales ledger matching Mizan GL 600 & 611 down to 0.00 TL."""
    net_sales = round(cfg["revenue"], 2)
    gross_sales = round(net_sales * 1.02, 2)
    contra = round(gross_sales - net_sales, 2)
    as_of = datetime.date(2025, 12, 31)

    sector_products = {
        "uretim_sanayi": [
            ("Ağır Sanayi Redüktörü 15kW", 38500, 26000),
            ("Hidrolik Silindir Pistonu 50T", 18500, 12500),
            ("CNC Talaşlı İmalat Şaft Grubu", 8900, 5900),
            ("Çelik Bağlantı Flanşı Q120", 2400, 1550),
            ("Özel İmalat Pres Gövdesi", 95000, 68000),
            ("Yedek Dişli Takımı Çelik", 4600, 2900),
            ("Talaşlı İmalat Revizyon Paketi", 14500, 9200),
        ],
        "toptan_ticaret": [
            ("Osmancık Baldo Pirinç 25kg", 1150, 980),
            ("Ayçiçek Yağı 5L Koli (4 Adet)", 980, 840),
            ("Kristal Toz Şeker 50kg Torba", 1850, 1600),
            ("Pilavlık Bulgur 25kg", 580, 480),
            ("Domates Salçası 4500g Teneke", 420, 350),
            ("Rize Geleneksel Çay 1000g Koli", 280, 235),
            ("Tam Yağlı Beyaz Peynir 17kg", 3600, 3100),
        ],
        "perakende_eticaret": [
            ("Kaşmir Karışımlı Palto", 3800, 2100),
            ("Slim Fit Chino Pantolon", 650, 320),
            ("Deri Chelsea Bot", 1950, 1050),
            ("Basic Pamuklu T-Shirt 3'lü", 390, 180),
            ("Kruvaze Blazer Ceket", 1650, 820),
            ("Deri Omuz Çantası Vizon", 950, 460),
            ("Polar Fermuarlı Yelek", 520, 250),
        ],
        "hizmet_yazilim": [
            ("Enterprise SaaS Yıllık Lisans", 125000, 42000),
            ("Cloud Altyapı & DevOps Yönetimi", 48000, 16000),
            ("Özel Entegrasyon & API Mühendisliği", 75000, 26000),
            ("7/24 SLA Destek & Bakım Sözleşmesi", 28000, 9500),
            ("Kurumsal Veri Güvenliği Denetimi", 65000, 22000),
            ("Mikroservis Mimari Danışmanlığı", 90000, 31000),
        ],
        "insaat_taahhut": [
            ("Kaba İnşaat Taşeron Hakediş Paketi", 450000, 360000),
            ("Çelik Konstrüksiyon Montaj Paketi", 280000, 225000),
            ("Mekanik ve Havalandırma Tesisatı", 195000, 155000),
            ("Dış Cephe Yalıtım ve Kompozit Giydirme", 165000, 130000),
            ("İnce İşler Zemin Seramik & Şap İşi", 120000, 95000),
            ("Şantiye Altyapı ve Drenaj İşi", 85000, 68000),
        ],
        "saglik_medikal": [
            ("Ortopedi Cerrahi Ameliyat Paketi", 78000, 46000),
            ("Dijital Radyoloji & MR Görüntüleme", 9500, 4800),
            ("Kardiyovasküler Stent & Balon Tedavisi", 115000, 68000),
            ("Biyokimya & Genetik Test Paneli", 6800, 3500),
            ("Laparoskopik Cerrahi Operasyon Paketi", 62000, 36000),
            ("Yoğun Bakım Günlük Tedavi Protokolü", 18500, 10500),
        ],
        "lojistik_tasimacilik": [
            ("FTL Komple Tır Uluslararası Nakliye", 145000, 115000),
            ("Yurtiçi Soğuk Zincir Frigorifik Taşıma", 42000, 33000),
            ("LTL Parsiyel Karayolu Taşımacılığı", 18500, 14200),
            ("Liman Konteyner Transfer Çekici Hizmeti", 12500, 9600),
            ("Gümrüklü Antrepo Depolama & Elleçleme", 28000, 21500),
            ("Express Mikro Dağıtım & Kurye Hattı", 8500, 6500),
        ],
    }

    prods = sector_products.get(cfg["id"], sector_products["uretim_sanayi"])
    customer_names = [
        f"Müşteri Grubu A - {cfg['name'].split()[0]}",
        f"Müşteri Grubu B - {cfg['name'].split()[0]}",
        f"Bölge Bayi C - {cfg['name'].split()[0]}",
        f"Kurumsal Müşteri D - {cfg['name'].split()[0]}",
        f"Stratejik Ortak E - {cfg['name'].split()[0]}",
        f"Toptan Müşteri F - {cfg['name'].split()[0]}",
        f"Ticari Kanal G - {cfg['name'].split()[0]}",
        f"Ulusal Hesap H - {cfg['name'].split()[0]}",
    ]

    num_tx = 180
    rows = []
    for i in range(num_tx):
        tx_date = datetime.date(2025, 1, 1) + datetime.timedelta(days=int(i * (364.0 / num_tx)))
        cust = random.choice(customer_names)
        prod, base_price, base_cost = random.choice(prods)
        qty = random.randint(1, 20)
        raw_gross = qty * base_price
        disc_rate = random.choice([0.0, 0.0, 0.02, 0.03, 0.05])
        raw_disc = raw_gross * disc_rate
        raw_cost = qty * base_cost

        rows.append({
            "Müşteri": cust,
            "Ürün": prod,
            "Tarih": tx_date,
            "Miktar": qty,
            "Birim Fiyat": base_price,
            "Brüt Satış Tutarı": raw_gross,
            "İskonto Tutarı": raw_disc,
            "Maliyet": raw_cost,
        })

    df = pd.DataFrame(rows)
    # Scale gross sales exactly to gross_sales
    gross_factor = gross_sales / df["Brüt Satış Tutarı"].sum()
    df["Brüt Satış Tutarı"] = (df["Brüt Satış Tutarı"] * gross_factor).round(2)
    diff_gross = round(gross_sales - df["Brüt Satış Tutarı"].sum(), 2)
    df.loc[0, "Brüt Satış Tutarı"] = round(df.loc[0, "Brüt Satış Tutarı"] + diff_gross, 2)

    # Scale discounts exactly to contra
    disc_factor = contra / df["İskonto Tutarı"].sum() if df["İskonto Tutarı"].sum() > 0 else 0.0
    df["İskonto Tutarı"] = (df["İskonto Tutarı"] * disc_factor).round(2)
    diff_disc = round(contra - df["İskonto Tutarı"].sum(), 2)
    df.loc[0, "İskonto Tutarı"] = round(df.loc[0, "İskonto Tutarı"] + diff_disc, 2)

    # Net Sales is exact difference
    df["Net Satış Tutarı"] = (df["Brüt Satış Tutarı"] - df["İskonto Tutarı"]).round(2)

    # Scale cost proportionally
    df["Maliyet"] = (df["Maliyet"] * gross_factor).round(2)

    # Paid and open balance
    for i, r in df.iterrows():
        tx_date = r["Tarih"]
        net = r["Net Satış Tutarı"]
        is_paid = (as_of - tx_date).days > cfg["dso_target"]
        paid = net if is_paid else round(net * random.choice([0.0, 0.3, 0.5]), 2)
        df.loc[i, "Ödenen Tutar"] = paid
        df.loc[i, "Açık Bakiye"] = round(net - paid, 2)

    return df

def save_sector_package(cfg):
    """Generate and write all 6 Excel files for the sector."""
    sdir = os.path.join(BASE_DIR, cfg["id"])
    os.makedirs(sdir, exist_ok=True)
    print(f"Generating sector: {cfg['id']} -> {sdir}")

    # 1. mizan_cur.xlsx
    df_cur = generate_trial_balance(cfg, is_prior=False)
    with pd.ExcelWriter(os.path.join(sdir, "mizan_cur.xlsx"), engine="openpyxl") as w:
        df_cur.to_excel(w, sheet_name="Mizan_Cari", index=False)

    # 2. mizan_prior.xlsx
    df_prior = generate_trial_balance(cfg, is_prior=True)
    with pd.ExcelWriter(os.path.join(sdir, "mizan_prior.xlsx"), engine="openpyxl") as w:
        df_prior.to_excel(w, sheet_name="Mizan_Onceki", index=False)

    # 3. ar_aging.xlsx
    df_ar = generate_ar_aging(cfg)
    with pd.ExcelWriter(os.path.join(sdir, "ar_aging.xlsx"), engine="openpyxl") as w:
        df_ar.to_excel(w, sheet_name="Sheet1", index=False)

    # 4. ap_aging.xlsx
    df_ap = generate_ap_aging(cfg)
    with pd.ExcelWriter(os.path.join(sdir, "ap_aging.xlsx"), engine="openpyxl") as w:
        df_ap.to_excel(w, sheet_name="Sheet1", index=False)

    # 5. inventory.xlsx
    df_inv = generate_inventory(cfg)
    with pd.ExcelWriter(os.path.join(sdir, "inventory.xlsx"), engine="openpyxl") as w:
        df_inv.to_excel(w, sheet_name="Stok_Envanter", index=False)

    # 6. sales_ledger.xlsx
    df_sales = generate_sales_ledger(cfg)
    with pd.ExcelWriter(os.path.join(sdir, "sales_ledger.xlsx"), engine="openpyxl") as w:
        df_sales.to_excel(w, sheet_name="Satis_Defteri", index=False)

    print(f"  ✓ {cfg['name']} complete. Accounts: {len(df_cur)}, AR: {len(df_ar)}, AP: {len(df_ap)}, Inv: {len(df_inv)}, Sales: {len(df_sales)}")

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    for c in SECTORS:
        save_sector_package(c)
    print("\nAll 7 sector demo datasets successfully generated!")

if __name__ == "__main__":
    main()
