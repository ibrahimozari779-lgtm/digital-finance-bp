# dfbp/backend/frontend_template.py
# -*- coding: utf-8 -*-

"""Digital Finance Business Partner — multi-page marketing site + app.

Pages: HOME_HTML (/), PRICING_HTML (/paketler), ABOUT_HTML (/hakkimizda),
CONTACT_HTML (/iletisim), APP_HTML (/uygulama, the actual analysis tool).
All share one nav/footer/CSS design system assembled in build scripts.
"""

# ORTAK CSS VE MODERN TASARIM SİSTEMİ (Tüm Sayfalara Giydirildi)
SHARED_HEAD_ADDITIONS = r'''
<link rel="preconnect" href="https://googleapis.com">
<link rel="preconnect" href="https://gstatic.com" crossorigin>
<link href="https://googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://jsdelivr.net"></script>
<style>
:root {
    --bg: #071120;
    --panel: #12223D;
    --panel2: #1A2E4C;
    --line: #223754;
    --text: #F8FAFC;
    --muted: #94A3B8;
    --accent: #00B77A; /* Zümrüt Yeşili - Finansal Büyüme */
    --accent2: #00D2FF; /* Siber Mavi - Yapay Zeka */
    --red: #FF6B7A;
    --shadow: 0 20px 50px rgba(0,0,0,0.4);
}
body { 
    font-family: 'Plus Jakarta Sans', sans-serif; 
    background: radial-gradient(circle at 15% 0, #0F203C 0%, #071120 50%, #040914 100%); 
}
.premium-card {
    background: linear-gradient(145deg, rgba(18, 34, 61, 0.9), rgba(11, 22, 40, 0.9));
    border: 1px solid var(--line);
    border-radius: 20px;
    box-shadow: var(--shadow);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.premium-card:hover {
    border-color: rgba(0, 183, 122, 0.4);
    transform: translateY(-4px);
}
.glow-green:hover {
    box-shadow: 0 0 25px rgba(0, 183, 122, 0.3);
}
.reveal { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }
.reveal.in { opacity: 1; transform: none; }
</style>
'''

HOME_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Digital Finance Business Partner | Yapay Zeka Tabanlı Finansal Karar Destek Platformu</title>
<link rel="preconnect" href="https://googleapis.com"><link rel="preconnect" href="https://gstatic.com" crossorigin><link href="https://googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://jsdelivr.net"></script>
<style>
:root{--bg:#071120;--panel:#12223D;--line:#223754;--text:#F8FAFC;--muted:#94A3B8;--accent:#00B77A;--accent2:#00D2FF;--red:#FF6B7A;--shadow:0 20px 50px rgba(0,0,0,0.4);}
body{font-family:'Plus Jakarta Sans',sans-serif;background:radial-gradient(circle at 15% 0,#0F203C 0%,#071120 50%,#040914 100%);color:var(--text);line-height:1.5}
.premium-card{background:linear-gradient(145deg,rgba(18,34,61,0.9),rgba(11,22,40,0.9));border:1px solid var(--line);border-radius:24px;box-shadow:var(--shadow);transition:all 0.3s ease;}
.premium-card:hover{border-color:rgba(0,183,122,0.4);transform:translateY(-4px);}
.reveal{opacity:0;transform:translateY(20px);transition:opacity(0.6s) ease,transform(0.6s) ease;}
.reveal.in{opacity:1;transform:none;}
</style></head>
<body class="antialiased min-h-screen">
<header class="border-b border-slate-800 bg-[#071120]/80 backdrop-blur-md sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <div><a href="/" class="no-underline text-white"><h1 class="text-xl font-extrabold tracking-tight">DFBP <span class="text-emerald-500 font-medium text-xs">AI</span></h1><p class="text-xs text-slate-400">Verified financial facts → decision intelligence</p></a></div>
        <div class="flex items-center space-x-6">
            <nav class="hidden md:flex space-x-6 text-sm font-semibold text-slate-400"><a href="/" class="text-emerald-400">Anasayfa</a><a href="/paketler" class="hover:text-white transition">Paketler</a><a href="/hakkimizda" class="hover:text-white transition">Hakkımızda</a><a href="/iletisim" class="hover:text-white transition">İletişim</a><a href="/uygulama" class="hover:text-white transition">Uygulama</a></nav>
            <span class="px-3 py-1 rounded-full bg-slate-800 text-xs font-semibold text-emerald-400 border border-slate-700">Core v3.12</span>
            <div class="flex space-x-3"><a href="/uygulama?auth=login" class="text-sm font-bold text-slate-300 px-4 py-2 hover:text-white transition">Giriş</a><a href="/uygulama?auth=register" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm px-4 py-2 rounded-xl shadow-lg shadow-emerald-600/20 transition">Kayıt Ol</a></div>
        </div>
    </div>
</header>
<main class="max-w-7xl mx-auto px-6 py-12">
    <!-- ULTRA-PREMIUM MARKETING HERO -->
    <section class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center pt-8 pb-16">
        <div class="lg:col-span-7 reveal in">
            <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-bold border border-emerald-500/20 mb-6 uppercase tracking-wider">✨ Stratejik Karar Destek Katmanı</span>
            <h1 class="text-4xl md:text-6xl font-black text-white tracking-tight leading-[1.1] mb-6">Mizan Rakamlarını<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cyan-400">Yönetim Kurulu</span> Kararlarına Dönüştürün</h1>
            <p class="text-lg text-slate-400 max-w-xl leading-relaxed mb-8">Finansal tablolarınızı yükleyin; 33 gelişmiş deterministik analiz motorumuz bütçe sapmalarını, PVM kırılımlarını ve riskleri önceliklendirsin. Yapay zeka destekli CFO asistanınızla kararlarınızı kesin verilerle zırhlandırın.</p>
            <div class="flex flex-wrap gap-4"><a href="/uygulama" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-8 py-4 rounded-xl shadow-xl shadow-emerald-600/20 transition transform hover:-translate-y-0.5">Uygulamayı Ücretsiz Dene</a><a href="/paketler" class="bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold px-8 py-4 rounded-xl border border-slate-700 transition">Paketleri İncele</a></div>
        </div>
        <div class="lg:col-span-5 reveal in relative">
            <div class="absolute -inset-4 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
            <div class="premium-card p-6 border border-slate-700/50 backdrop-blur-sm relative">
                <div class="flex justify-between items-center mb-6"><span class="text-xs text-slate-400 flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> Canlı Gösterge Paneli</span><span class="px-2.5 py-0.5 rounded bg-emerald-500/10 text-emerald-400 text-xs font-bold">Sağlık Skoru: %84</span></div>
                <div class="w-full h-48 bg-slate-950/60 rounded-xl border border-slate-800/80 mb-4 flex flex-col justify-end p-4">
                    <div class="flex items-end gap-3 h-32 justify-center"><div class="w-8 bg-slate-800 h-1/3 rounded-t"></div><div class="w-8 bg-emerald-600 h-3/4 rounded-t shadow-lg shadow-emerald-500/20"></div><div class="w-8 bg-slate-800 h-1/2 rounded-t"></div><div class="w-8 bg-emerald-600 h-full rounded-t shadow-lg shadow-emerald-500/20"></div></div>
                </div>
                <div class="text-xs text-slate-400 italic">"Price-Volume-Mix analiz motoruna göre, bu dönemdeki ciro artışının %64'ü fiyat revizyonlarından kaynaklanmaktadır." — narrative_engine.py</div>
            </div>
        </div>
    </section>

    <!-- EXPLAINER VIDEO SECTION (YÖNETİCİ İKNA KATMANI) -->
    <section class="py-16 border-t border-slate-800/60 reveal">
        <div class="text-center max-w-3xl mx-auto mb-12">
            <h2 class="text-3xl font-extrabold text-white mb-4">Her Ay Excel Tablolarında Kaybolmaya Son Verin</h2>
            <p class="text-slate-400 text-base">Geleneksel raporlama geçmişi anlatır; DFBP AI ise şirketinizin geleceğini kesin kararlarla yönetmenizi sağlar. 30 saniyede sistemin nasıl çalıştığını izleyin.</p>
        </div>
        <div class="max-w-4xl mx-auto rounded-3xl overflow-hidden border border-slate-700/50 shadow-2xl relative bg-slate-950/80 aspect-video flex items-center justify-center group">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 to-transparent opacity-60"></div>
            <div class="z-10 text-center p-6"><button class="w-20 h-20 rounded-full bg-emerald-600 text-white flex items-center justify-center font-bold text-2xl shadow-xl shadow-emerald-600/40 group-hover:scale-110 transition-transform mx-auto mb-4">▶</button><p class="text-sm font-semibold text-emerald-400 tracking-wider uppercase">Platform Tanıtım Videosu & Demo Akışı</p></div>
        </div>
    </section>

    <!-- CORE ENGINES SHOWCASE -->
    <section id="features" class="py-16 border-t border-slate-800/60 reveal">
        <div class="text-center max-w-3xl mx-auto mb-16">
            <h2 class="text-3xl font-extrabold text-white">Gelişmiş Finansal Mimari (Core Engines)</h2>
            <p class="text-slate-400 mt-3">Arka planda çalışan 33 deterministik finans mühendisliği algoritmasının gücünü keşfedin.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="premium-card p-8 group"><div class="w-12 h-12 rounded-xl bg-emerald-500/10 text-emerald-400 font-bold text-lg flex items-center justify-center mb-6 group-hover:bg-emerald-600 group-hover:text-white transition-colors">PVM</div><h3 class="text-xl font-bold text-white mb-2">Price-Volume-Mix Engine</h3><p class="text-slate-400 text-sm leading-relaxed">Fiyat artışları, satış hacmi ve ürün karması değişimlerinin kârlılığınız üzerindeki net etkisini kuruşu kuruşuna ayrıştırır.</p></div>
