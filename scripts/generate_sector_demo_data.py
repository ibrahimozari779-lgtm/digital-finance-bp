#!/usr/bin/env python3
"""Generate rich, realistic, coherent multi-source demo datasets for 5 distinct industries:
1. uretim_sanayi: Makine & Metal Sanayi A.Ş. (Manufacturing)
2. toptan_ticaret: Anadolu Gıda & Toptan Dağıtım Ltd. (Wholesale FMCG)
3. perakende_eticaret: ModaStyle Perakende & E-Ticaret A.Ş. (Retail & E-Commerce)
4. hizmet_yazilim: Nova Teknoloji & B2B Yazılım A.Ş. (B2B SaaS & Services)
5. insaat_taahhut: Atlas Yapı & Taahhüt A.Ş. (Construction & Projects)

Each sector gets 6 synchronized files in demo_data/sectors/{sector_id}/:
- mizan_cur.xlsx (Balanced current period trial balance with 50-120 accounts)
- mizan_prior.xlsx (Balanced prior period trial balance for trend & cash bridge)
- ar_aging.xlsx (Customer receivables aging with 30-50 real companies)
- ap_aging.xlsx (Supplier payables aging with 20-40 real vendors)
- inventory.xlsx (Detailed inventory stock ledger with SKUs, warehouses, aging)
- sales_ledger.xlsx (Granular transaction ledger with units, discounts, costs)
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
        "sector_label": "Perakende / Ticaret",
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
        "sector_label": "Üretim / Sanayi",
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
]

# Random seed for deterministic reproducibility
random.seed(42)

def generate_trial_balance(cfg, is_prior=False):
    """Generate coherent, balanced TDHP trial balance matching sector KPIs."""
    rev_mult = 0.88 if is_prior else 1.0
    net_sales = cfg["revenue"] * rev_mult
    cogs = net_sales * cfg["cogs_pct"]
    gross_profit = net_sales - cogs
    opex = net_sales * cfg["opex_pct"]
    fin_exp = net_sales * cfg["fin_pct"]
    pretax_profit = gross_profit - opex - fin_exp
    tax = net_sales * cfg["tax_pct"]
    net_profit = pretax_profit - tax

    dso = cfg["dso_target"] * (1.08 if is_prior else 1.0)
    dio = cfg["dio_target"] * (1.10 if is_prior else 1.0)
    dpo = cfg["dpo_target"] * (0.95 if is_prior else 1.0)

    receivables = (net_sales / 365.0) * dso
    inventory = (cogs / 365.0) * dio if dio > 0 else 0.0
    payables = (cogs / 365.0) * dpo
    cash = net_sales * (0.015 if is_prior else 0.028)
    bank_st_debt = net_sales * 0.12
    bank_lt_debt = net_sales * 0.08
    other_cur_assets = net_sales * 0.04
    fixed_assets = net_sales * (0.40 if cfg["id"] in ("uretim_sanayi", "insaat_taahhut") else 0.15)
    accum_depr = fixed_assets * 0.35
    net_fixed_assets = fixed_assets - accum_depr

    total_assets = cash + receivables + inventory + other_cur_assets + net_fixed_assets
    other_liab = net_sales * 0.03
    total_liab = bank_st_debt + payables + other_liab + bank_lt_debt
    equity = total_assets - total_liab
    capital = equity * 0.50
    prior_retained = equity * 0.50 - net_profit

    # Detailed accounts breakdown
    rows = []
    def add(code, name, debit, credit):
        rows.append({"Hesap Kodu": code, "Hesap Adı": name, "Borç Bakiye": round(debit, 2), "Alacak Bakiye": round(credit, 2)})

    # 10 Kasa & Bankalar
    add(100, "Kasa", cash * 0.15, 0)
    add("102.01", "Garanti BBVA Ticari TL", cash * 0.45, 0)
    add("102.02", "İş Bankası Şirket Hesabı", cash * 0.25, 0)
    add("102.03", "Yapı Kredi Döviz Tevdiat (USD/EUR)", cash * 0.15, 0)
    if cfg["id"] == "perakende_eticaret":
        add("108.01", "Kredi Kartı & POS Tahsilatları", receivables * 0.70, 0)
        rec_share = 0.30
    else:
        rec_share = 1.0

    # 120 Alıcılar
    num_cust = 20
    cust_sum = 0
    for i in range(1, num_cust + 1):
        w = (num_cust - i + 1) ** 1.3
        amt = (receivables * rec_share) * (w / sum((num_cust - j + 1) ** 1.3 for j in range(1, num_cust + 1)))
        cust_sum += amt
        cname = f"Cari Müşteri {i:02d} - {cfg['name'].split()[0]} Portföy"
        add(f"120.{i:02d}", cname, amt, 0)

    # 15 Stoklar (Hizmet sektöründe stok yok)
    if inventory > 0:
        if cfg["id"] == "uretim_sanayi":
            add("150.01", "İlk Madde ve Malzeme - Çelik & Metal", inventory * 0.45, 0)
            add("150.02", "İlk Madde ve Malzeme - Yedek Parça & Rulman", inventory * 0.15, 0)
            add("151.01", "Yarı Mamuller - Talaşlı İmalat Hattı", inventory * 0.15, 0)
            add("152.01", "Mamuller - Sevke Hazır İmalat", inventory * 0.25, 0)
        elif cfg["id"] == "insaat_taahhut":
            add("150.01", "Şantiye Demir & Çelik Stokları", inventory * 0.35, 0)
            add("150.02", "Çimento & Hazır Beton Girdileri", inventory * 0.20, 0)
            add("170.01", "Yıllara Yaygın İnşaat Maliyetleri (Proje A)", inventory * 0.45, 0)
        else:
            add("153.01", "Ticari Mallar - Ana Kategori A", inventory * 0.55, 0)
            add("153.02", "Ticari Mallar - Sezonluk Kategori B", inventory * 0.30, 0)
            add("153.03", "Ticari Mallar - Tali Ürün Grubu C", inventory * 0.15, 0)

    # Diğer Dönen Varlıklar
    add("191.01", "İndirilecek KDV", other_cur_assets * 0.60, 0)
    add("195.01", "İş Avansları & Personel", other_cur_assets * 0.40, 0)

    # 25 Duran Varlıklar
    if cfg["id"] in ("uretim_sanayi", "insaat_taahhut"):
        add("253.01", "Tesis, Makine ve İmalat Cihazları", fixed_assets * 0.65, 0)
        add("254.01", "Taşıtlar ve Şantiye Filosu", fixed_assets * 0.25, 0)
        add("255.01", "Demirbaşlar ve IT Donanımı", fixed_assets * 0.10, 0)
    else:
        add("254.01", "Taşıtlar ve Dağıtım Araçları", fixed_assets * 0.50, 0)
        add("255.01", "Demirbaşlar ve Bilgi İşlem", fixed_assets * 0.30, 0)
        add("260.01", "Haklar & Yazılım Lisansları", fixed_assets * 0.20, 0)
    add("257.01", "Birikmiş Amortismanlar (-)", 0, accum_depr)

    # 30 Kısa Vadeli Yabancı Kaynaklar
    add("300.01", "Banka Kredileri (BCH / Rotatif Ticari)", 0, bank_st_debt * 0.70)
    add("300.02", "Spot & Taksitli Kredi Anapara Taksitleri", 0, bank_st_debt * 0.30)

    # 320 Satıcılar
    num_vend = 15
    for i in range(1, num_vend + 1):
        w = (num_vend - i + 1) ** 1.2
        amt = payables * (w / sum((num_vend - j + 1) ** 1.2 for j in range(1, num_vend + 1)))
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
    add("600.01", "Yurtiçi Satış Gelirleri", 0, net_sales * 1.02)
    add("611.01", "Satış İskontoları (-)", net_sales * 0.02, 0)

    if cfg["id"] == "uretim_sanayi":
        add("710.01", "Direkt İlk Madde ve Malzeme Giderleri", cogs * 0.65, 0)
        add("720.01", "Direkt İşçilik Giderleri", cogs * 0.20, 0)
        add("730.01", "Genel Üretim Giderleri (Amortisman & Enerji)", cogs * 0.15, 0)
        add("620.01", "Satılan Mamuller Maliyeti (-)", cogs, 0)
    elif cfg["id"] == "hizmet_yazilim":
        add("622.01", "Satılan Hizmet Maliyeti (-)", cogs, 0)
    else:
        add("621.01", "Satılan Ticari Mallar Maliyeti (-)", cogs, 0)

    add("631.01", "Pazarlama, Satış ve Dağıtım Giderleri", opex * 0.55, 0)
    add("632.01", "Genel Yönetim Giderleri", opex * 0.45, 0)
    add("660.01", "Finansman Giderleri (Ticari Kredi Faizleri)", fin_exp, 0)
    add("691.01", "Dönem Kârı Vergi ve Yasal Yükümlülükleri", tax, 0)

    df = pd.DataFrame(rows)
    # Ensure trial balance balance
    tot_deb = df["Borç Bakiye"].sum()
    tot_crd = df["Alacak Bakiye"].sum()
    diff = tot_deb - tot_crd
    # Adjust retained earnings to make exact match
    df.loc[df["Hesap Kodu"] == 570, "Alacak Bakiye"] += diff
    return df

def generate_ar_aging(cfg):
    """Generate realistic AR aging ledger with real companies, due dates, and aging buckets."""
    net_sales = cfg["revenue"]
    dso = cfg["dso_target"]
    total_ar = (net_sales / 365.0) * dso
    as_of = datetime.date(2025, 12, 31)

    customer_pool = [
        ("Borusan Lojistik & Sanayi A.Ş.", 0.08, -15),
        ("Kalyon Altyapı Yatırımları A.Ş.", 0.07, 45),
        ("Şişecam Düzcam Pazarlama A.Ş.", 0.06, -5),
        ("Eczacıbaşı Yapı Gereçleri A.Ş.", 0.06, 25),
        ("Vestel Beyaz Eşya Sanayi A.Ş.", 0.05, 10),
        ("Arçelik Pazarlama A.Ş.", 0.05, -30),
        ("Ford Otosan Tedarik Sanayi", 0.05, 65),
        ("Tofaş Türk Otomobil Fabrikası", 0.04, -10),
        ("BİM Birleşik Mağazalar A.Ş.", 0.04, 5),
        ("Migros Ticaret Dağıtım A.Ş.", 0.04, 15),
        ("Anadolu Efes Dağıtım A.Ş.", 0.04, -20),
        ("Ülker Bisküvi Sanayi A.Ş.", 0.035, 35),
        ("Trendyol Pazaryeri Satış A.Ş.", 0.035, -45),
        ("Hepsiburada E-Ticaret A.Ş.", 0.03, -15),
        ("LC Waikiki Mağazacılık A.Ş.", 0.03, 75),
        ("DeFacto Perakende Ticaret A.Ş.", 0.03, 12),
        ("Turkcell İletişim Hizmetleri A.Ş.", 0.025, 90),
        ("Vodafone Telekomünikasyon A.Ş.", 0.025, -5),
        ("Türk Telekomünikasyon A.Ş.", 0.025, 30),
        ("Aselsan Elektronik Sanayi A.Ş.", 0.025, 110),
        ("Havelsan Hava Elektronik Sanayi", 0.02, -10),
        ("Tekfen İnşaat ve Tesisat A.Ş.", 0.02, 125),
        ("Limak İnşaat Sanayi ve Ticaret", 0.02, 40),
        ("Cengiz İnşaat Sanayi A.Ş.", 0.02, 85),
        ("İÇDAŞ Çelik Enerji Tersane A.Ş.", 0.02, -5),
        ("Kardemir Karabük Demir Çelik", 0.015, 20),
        ("Akçansa Çimento Sanayi A.Ş.", 0.015, 60),
        ("Çimsa Çimento Sanayi A.Ş.", 0.015, 15),
        ("Petkim Petrokimya Holding A.Ş.", 0.015, -25),
        ("Tüpraş Türkiye Petrol Rafinerileri", 0.015, 5),
        ("Doğuş Otomotiv Servis ve Ticaret", 0.01, 30),
        ("Koçtaş Yapı Marketleri A.Ş.", 0.01, 45),
        ("Teknosa İç ve Dış Ticaret A.Ş.", 0.01, 70),
        ("CarrefourSA Hipermarketleri A.Ş.", 0.01, -12),
        ("Şok Marketler Ticaret A.Ş.", 0.01, 8),
    ]

    rows = []
    inv_num = 1000
    for name, share, days_offset in customer_pool:
        cust_total = total_ar * share
        # Split customer balance into 1-3 invoices
        num_inv = random.randint(1, 3)
        for sub in range(num_inv):
            inv_num += 1
            inv_amt = round(cust_total / num_inv, 2)
            vade = as_of + datetime.timedelta(days=days_offset + random.randint(-10, 15))
            rows.append({
                "Müşteri": name,
                "Fatura No": f"FA-{inv_num}",
                "Vade Tarihi": vade,
                "Açık Tutar": inv_amt,
                "Para Birimi": "TL"
            })
    return pd.DataFrame(rows)

def generate_ap_aging(cfg):
    """Generate realistic supplier AP aging ledger with vendor names, due dates, amounts."""
    cogs = cfg["revenue"] * cfg["cogs_pct"]
    dpo = cfg["dpo_target"]
    total_ap = (cogs / 365.0) * dpo
    as_of = datetime.date(2025, 12, 31)

    vendor_pool = [
        ("İsdemir İskenderun Demir Çelik A.Ş.", 0.12, 20),
        ("Erdemir Ereğli Demir ve Çelik A.Ş.", 0.10, 35),
        ("Tosyalı Çelik Profil Sanayi A.Ş.", 0.08, -10),
        ("Kordsa Teknik Tekstil A.Ş.", 0.07, 45),
        ("Aksa Akrilik Kimya Sanayii A.Ş.", 0.06, 15),
        ("Sasa Polyester Sanayi A.Ş.", 0.06, 50),
        ("Toros Tarım Sanayi ve Ticaret", 0.05, -5),
        ("Gentaş Kimya Sanayi Pazarlama", 0.05, 25),
        ("Alkim Alkali Kimya A.Ş.", 0.05, 30),
        ("Tat Gıda Sanayi A.Ş.", 0.04, -15),
        ("Pınar Süt Mamülleri Sanayii A.Ş.", 0.04, 10),
        ("Banvit Bandırma Vitaminli Yem", 0.04, 40),
        ("Borusan Mannesmann Boru A.Ş.", 0.035, -20),
        ("Sarkuysan Elektrolitik Bakır Sanayi", 0.035, 60),
        ("Kastamonu Entegre Ağaç Sanayi", 0.03, 15),
        ("Yıldız Entegre Ağaç Sanayi A.Ş.", 0.03, -10),
        ("Çamsan Ağaç Sanayi ve Ticaret", 0.025, 20),
        ("Ege Seramik Sanayi ve Ticaret", 0.025, 35),
        ("Kütahya Porselen Sanayi A.Ş.", 0.02, 45),
        ("Akzo Nobel Boya Sanayi A.Ş.", 0.02, -5),
        ("DYO Boya Fabrikaları Sanayi A.Ş.", 0.015, 10),
        ("Polisan Holding Kimya Sanayi", 0.015, 25),
        ("Filli Boya Betek Boya ve Kimya", 0.015, 30),
    ]

    rows = []
    doc_num = 2000
    for name, share, days_offset in vendor_pool:
        vend_total = total_ap * share
        num_doc = random.randint(1, 2)
        for _ in range(num_doc):
            doc_num += 1
            amt = round(vend_total / num_doc, 2)
            vade = as_of + datetime.timedelta(days=days_offset + random.randint(-5, 10))
            rows.append({
                "Tedarikçi": name,
                "Belge No": f"BL-{doc_num}",
                "Vade Tarihi": vade,
                "Açık Tutar": amt,
                "Para Birimi": "TL"
            })
    return pd.DataFrame(rows)

def generate_inventory(cfg):
    """Generate detailed inventory stock ledger matching sector goods and turnover."""
    cogs = cfg["revenue"] * cfg["cogs_pct"]
    dio = cfg["dio_target"]
    if dio == 0:
        return pd.DataFrame(columns=["Ürün", "Depo", "Miktar", "Birim Maliyet", "Tutar", "Son Hareket Tarihi"])
    total_inv = (cogs / 365.0) * dio
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
            ("Hidrolik Valf Bloğu 4 Yollu", "Hammadde Deposu", 220, 3100, 185), # Atıl stok
            ("Endüstriyel Hidrolik Pres 100T", "Mamul Deposu", 8, 145000, 210), # Ağır stok
            ("Paslanmaz Çelik L-Profil 50x5", "Hammadde Deposu", 750, 290, 60),
            ("Poliüretan Sızdırmazlık Keçe Seti", "Hammadde Deposu", 1400, 85, 30),
            ("Elektrik Kumanda Panosu IP65", "Mamul Deposu", 35, 12000, 110),
            ("Konveyör Tahrik Tamburu 400mm", "Mamul Deposu", 55, 6500, 175), # Yavaş stok
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
            ("Organik Nar Ekşisi 1000ml Koli", "Sos Deposu", 1400, 420, 160), # Atıl stok
            ("Kuru Fasulye İspir 25kg Çuval", "Merkez Kuru Gıda Depo", 1100, 1200, 50),
            ("Tam Yağlı Beyaz Peynir 17kg Teneke", "Soğuk Hava Deposu", 850, 2850, 14),
            ("Kaşar Peyniri Taze Blok 2000g", "Soğuk Hava Deposu", 1200, 480, 20),
            ("Konserve Haşlanmış Nohut 800g Koli", "Konserve Deposu", 2400, 185, 115),
            ("Naturel Sızma Zeytinyağı Erken Hasat", "Sıvı Yağ Deposu", 950, 1650, 190), # Yavaş
        ],
        "perakende_eticaret": [
            ("Oversize Kaşmir Palto Bej (Kış)", "E-Ticaret Lojistik Depo", 450, 2200, 195), # Sezon dışı atıl!
            ("Slim Fit Pamuklu Chino Pantolon", "Merkez Depo", 1800, 320, 20),
            ("Hakiki Deri Chelsea Bot Siyah", "Ayakkabı Deposu", 650, 1150, 180), # Atıl bot!
            ("Basic Bisiklet Yaka T-Shirt Beyaz", "E-Ticaret Lojistik Depo", 4500, 95, 8),
            ("Oversize Kapüşonlu Sweatshirt", "E-Ticaret Lojistik Depo", 2200, 260, 25),
            ("Desenli İpek Şifon Midi Elbise", "Kadın Giyim Depo", 850, 540, 60),
            ("Kruvaze Blazer Ceket Lacivert", "Merkez Depo", 750, 850, 40),
            ("Deri Askılı Omuz Çantası Vizon", "Aksesuar Depo", 900, 420, 75),
            ("Polo Yaka Pike Kumaş Tişört", "Merkez Depo", 2800, 140, 15),
            ("Yün Triko Balıkçı Yaka Kazak", "E-Ticaret Lojistik Depo", 1100, 380, 165), # Atıl
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
            ("Porselen Seramik Zemin Karosu 60x120", "İnce İşler Deposu", 850, 550, 175), # Atıl
            ("Epoksi Zemin Kaplama Reçine Seti", "Kimyasal Deposu", 120, 3200, 140),
            ("Kule Vinç Bağlantı Ankraj Seti", "Makine Ekipman Depo", 15, 45000, 95),
            ("Yangın Güvenlik Kapısı EI60", "Kapı Doğrama Depo", 75, 5800, 130),
            ("LED Lineer Aydınlatma Armatürü 40W", "Elektrik Deposu", 650, 450, 70),
            ("Drenaj ve Temel Su İzolasyon Membranı", "Yalıtım Depo", 900, 340, 50),
            ("Şantiye Güvenlik Filesi ve İskele", "İSG Malzeme Depo", 350, 620, 180),
        ],
    }

    items = sector_items.get(cfg["id"], sector_items["uretim_sanayi"])
    # Calculate scale factor to match total_inv
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
    return pd.DataFrame(rows)

def generate_sales_ledger(cfg):
    """Generate transactional sales ledger with 150-250 rows for multi-source sales engine."""
    net_sales = cfg["revenue"]
    as_of = datetime.date(2025, 12, 31)

    customer_names = [
        "Anadolu Sanayi Grubu A.Ş.", "Ege Dağıtım ve Ticaret Ltd.", "Marmara Perakende Çözümleri",
        "Toroslar Lojistik ve Ticaret", "Karadeniz Toptan Dağıtım A.Ş.", "İç Anadolu Tüketim Malları",
        "Akdeniz Endüstriyel Ürünler", "Güneydoğu Pazarlama Ltd.", "İstanbul Kurumsal Tedarik A.Ş.",
        "Ankara Proje Yönetim ve Satış", "İzmir Ticari Faaliyetler A.Ş.", "Bursa İmalat Tedarik Ltd.",
        "Kocaeli Ağır Sanayi Pazarlama", "Adana Bölge Bayi A.Ş.", "Gaziantep İhracat ve Toptan"
    ]

    product_names = [
        ("Ürün Alpha Standart", 1850, 1250),
        ("Ürün Beta Premium", 4200, 2800),
        ("Ürün Gamma Endüstriyel", 8900, 5900),
        ("Ürün Delta Kompakt", 1200, 820),
        ("Ürün Epsilon Profesyonel", 15400, 9800),
        ("Ürün Zeta Hızlı Tüketim", 650, 440),
        ("Yedek Parça Servis Paketi", 2400, 1500),
        ("Özel Sipariş Modeli X", 21500, 14200),
    ]

    num_tx = 180
    avg_tx_target = net_sales / num_tx

    rows = []
    for i in range(num_tx):
        tx_date = datetime.date(2025, 1, 1) + datetime.timedelta(days=int(i * (364.0 / num_tx)))
        cust = random.choice(customer_names)
        prod, base_price, base_cost = random.choice(product_names)
        # Quantity
        qty = random.randint(1, 25)
        gross = round(qty * base_price, 2)
        disc_pct = random.choice([0.0, 0.0, 0.03, 0.05, 0.08, 0.12])
        disc = round(gross * disc_pct, 2)
        net = round(gross - disc, 2)
        cost = round(qty * base_cost, 2)
        # Payment status
        is_paid = (as_of - tx_date).days > cfg["dso_target"]
        paid = net if is_paid else round(net * random.choice([0.0, 0.3, 0.5]), 2)
        open_bal = round(net - paid, 2)

        rows.append({
            "Müşteri": cust,
            "Ürün": prod,
            "Tarih": tx_date,
            "Miktar": qty,
            "Birim Fiyat": base_price,
            "Brüt Satış Tutarı": gross,
            "İskonto Tutarı": disc,
            "Net Satış Tutarı": net,
            "Maliyet": cost,
            "Ödenen Tutar": paid,
            "Açık Bakiye": open_bal
        })

    df = pd.DataFrame(rows)
    # Scale net sales to match target
    factor = net_sales / df["Net Satış Tutarı"].sum()
    df["Brüt Satış Tutarı"] = (df["Brüt Satış Tutarı"] * factor).round(2)
    df["İskonto Tutarı"] = (df["İskonto Tutarı"] * factor).round(2)
    df["Net Satış Tutarı"] = (df["Net Satış Tutarı"] * factor).round(2)
    df["Maliyet"] = (df["Maliyet"] * factor).round(2)
    df["Ödenen Tutar"] = (df["Ödenen Tutar"] * factor).round(2)
    df["Açık Bakiye"] = (df["Açık Bakiye"] * factor).round(2)
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
    print("\nAll 5 sector demo datasets successfully generated!")

if __name__ == "__main__":
    main()
