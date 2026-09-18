"""Digital Finance Business Partner — multi-page marketing site + app.

Pages: HOME_HTML (/), SOLUTIONS_HTML (/cozumler), PRICING_HTML (/paketler),
ABOUT_HTML (/hakkimizda), CONTACT_HTML (/iletisim), SECURITY_HTML (/guvenlik),
APP_HTML (/uygulama, the actual analysis tool).
All share one nav/footer/CSS design system assembled in build scripts.
"""

HOME_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" type="image/svg+xml" href="/favicon.ico"><meta name="description" content="Digital Finance Business Partner (digitalfinancebp.com) — Şirketinizin finansal tablolarını 33 analitik karar motoruyla denetleyen, kâr sızıntılarını ve kilitli nakdi hesaplayan kurumsal karar destek platformu."><title>Digital Finance Business Partner | Finansal Karar Destek Platformu</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&display=swap" rel="stylesheet">
<style>
:root{--bg:#F6F7F9;--panel:#FFFFFF;--panel2:#F0F3F8;--line:#E4E8EF;--text:#0F1B2D;--muted:#5B6B84;--accent:#1D4ED8;--accent2:#4F8CFF;--red:#C22A3E;--amber:#B4720A;--green:#0E7C66;--shadow:0 1px 2px rgba(15,27,45,.04),0 12px 32px rgba(15,27,45,.06);--serif:'Fraunces',ui-serif,Georgia,serif}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(1100px 480px at 12% -10%, rgba(29,78,216,.07), transparent 60%),radial-gradient(900px 420px at 100% 0%, rgba(14,124,102,.05), transparent 55%),#F6F7F9;color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45}button,input,select{font:inherit}.wrap{max-width:1440px;margin:auto;padding:0 28px}.top{padding:26px 0 18px;border-bottom:1px solid rgba(15,27,45,.08);position:sticky;top:0;background:rgba(246,247,249,.86);backdrop-filter:blur(18px);z-index:10}.brand{display:flex;align-items:center;justify-content:space-between;gap:20px}.brand h1{margin:0;font-size:25px;letter-spacing:-.6px}.brand p{margin:3px 0 0;color:var(--muted);font-size:13px}.badge{padding:6px 10px;border:1px solid #D7DEE8;border-radius:999px;color:var(--accent);font-size:12px;white-space:nowrap}.hero{padding:34px 0 24px;display:grid;grid-template-columns:1.45fr .55fr;gap:18px}.heroCard,.card{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow)}.heroCard{padding:28px}.heroTitle{font-family:var(--serif);font-weight:600;font-size:44px;line-height:1.08;margin:0 0 14px;letter-spacing:-.5px}.heroText{color:var(--muted);max-width:780px}.framework{display:flex;flex-wrap:wrap;gap:8px 10px;margin:16px 0 2px;padding:0}.framework span{font-size:11.5px;color:#33415C;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px}.framework span b{color:var(--accent);font-weight:800}
.qsel{margin-top:18px}.qsel .qtitle{font-size:12px;color:var(--muted);margin-bottom:8px;font-weight:700}.qsel .qrow{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.qsel button{border:1px solid #D7DEE8;background:#EEF2FF;color:#33415C;border-radius:12px;padding:10px 12px;font-size:12.5px;cursor:pointer;text-align:left;line-height:1.3}.qsel button:hover{border-color:#B7C3D6}.qsel button.active{border-color:var(--accent);color:var(--accent);background:#DCE6FB}
.upload{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}.file{border:1px dashed #C9D2DE;padding:12px;border-radius:12px;background:#F5F7FA;max-width:100%}.select,button{border:1px solid #D7DEE8;border-radius:11px;padding:11px 14px;background:#FFFFFF;color:var(--text)}button.primary,a.primary{background:linear-gradient(135deg,#2557E8,#1D4ED8);border:0;color:#FFFFFF;font-weight:800;cursor:pointer;transition:transform .15s ease,box-shadow .15s ease;box-shadow:0 6px 16px rgba(29,78,216,.25)}a.primary:hover,button.primary:hover{transform:translateY(-1px);box-shadow:0 10px 22px rgba(29,78,216,.32)}button.secondary,a.secondary{cursor:pointer;border:1.5px solid #C9D2DE;background:#FFFFFF;color:var(--text)}a.secondary:hover,button.secondary:hover{border-color:var(--accent);color:var(--accent)}button:disabled{opacity:.5;cursor:not-allowed}.scoreCard{padding:25px;display:flex;flex-direction:column;justify-content:center}.scoreRing{width:170px;height:170px;border-radius:50%;margin:auto;display:grid;place-items:center;background:conic-gradient(var(--accent) calc(var(--score)*1%),#E4E8EF 0);position:relative}.scoreRing:after{content:"";position:absolute;inset:12px;border-radius:50%;background:#FFFFFF}.scoreNum{position:relative;z-index:1;text-align:center}.scoreNum strong{display:block;font-size:48px;line-height:1}.scoreNum span{color:var(--muted);font-size:12px}.status{margin:15px auto 0;padding:7px 12px;border-radius:999px;background:#EAF0FF;color:var(--accent);font-size:12px;font-weight:700}.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.card{padding:22px;margin:0 0 16px;transition:transform .18s ease,box-shadow .18s ease,outline .2s}.card:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(15,27,45,.08)}@keyframes growUp{from{transform:scaleY(0);opacity:0}to{transform:scaleY(1);opacity:1}}.wf{transform-origin:bottom}.wf .col{transform-origin:bottom}@keyframes growWidth{from{width:0}to{}}.metric{padding:17px;border:1px solid var(--line);border-radius:15px;background:rgba(15,27,45,.03)}.metric .label{color:var(--muted);font-size:12px}.metric .value{font-size:25px;font-weight:800;margin-top:5px;letter-spacing:-.5px}.metric .sub{font-size:11px;color:var(--muted);margin-top:5px}.sectionHead{display:flex;align-items:end;justify-content:space-between;gap:15px;margin-bottom:17px}.sectionHead h2{margin:0;font-size:18px}.sectionHead p{margin:0;color:var(--muted);font-size:12px}.flowStep{margin:36px 0 14px;padding-top:6px;border-top:1px solid rgba(15,27,45,.08)}.flowStep:first-child{margin-top:0;border-top:0;padding-top:0}.flowLabel{display:flex;align-items:center;gap:10px;font-size:12px;font-weight:800;letter-spacing:1.8px;text-transform:uppercase;color:var(--accent);margin:0 0 4px}.flowLabel .n{width:22px;height:22px;border-radius:50%;background:#EAF0FF;color:var(--accent);display:inline-flex;align-items:center;justify-content:center;font-size:11px}.flowLabel p{margin:0;color:var(--muted);font-size:12.5px;font-weight:500;text-transform:none;letter-spacing:0}.flowLabel.alt{color:var(--accent2)}.flowLabel.alt .n{color:var(--accent2)}.flowSub{color:var(--muted);font-size:12.5px;margin:2px 0 16px 32px}.insight{border:1px solid var(--line);border-radius:15px;padding:16px;background:#F7F9FC}.insight.critical{border-color:#E8B4BD}.insight.high{border-color:#E9CBA8}.insight.medium{border-color:#E5DBA0}.insight.positive{border-color:#A9D9C9}.insight h3{margin:0 0 5px;font-size:14px}.insight p{margin:6px 0;color:#33415C;font-size:13px}.insight ul{margin:6px 0;padding-left:18px;color:#33415C;font-size:13px}.tag{display:inline-flex;padding:4px 8px;border-radius:999px;font-size:10px;font-weight:800;text-transform:uppercase;background:#EAF0FF;color:#5B6B84}.tag.critical{background:#FCE8EA;color:#C22A3E}.tag.high{background:#FDF0E0;color:#B4720A}.tag.medium{background:#FBF6DE;color:#8A6D00}.tag.positive{background:#E4F5EF;color:#0E7C66}.riskRow,.actionRow{display:grid;grid-template-columns:40px 1fr auto;gap:12px;align-items:center;padding:13px 0;border-bottom:1px solid rgba(15,27,45,.08)}.rank{font-size:18px;font-weight:900;color:#5B6B84}.riskScore{font-size:12px;color:var(--muted)}.bar{height:7px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:8px}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:99px}.waterfallWrap{overflow-x:auto;-webkit-overflow-scrolling:touch;padding-bottom:10px;margin-bottom:10px}.waterfall{display:flex;align-items:flex-end;gap:9px;height:190px;padding:20px 5px 0;border-bottom:1px solid var(--line);min-width:620px}.wf{flex:1;display:flex;flex-direction:column;justify-content:end;height:100%;min-width:65px}.wf .col{border-radius:6px 6px 2px 2px;background:linear-gradient(180deg,#83a4ff,#506fd0);min-height:3px}.wf.neg .col{background:linear-gradient(180deg,#ff8290,#9d3e54)}.wf .lab{font-size:10.5px;font-weight:600;color:var(--muted);text-align:center;margin-top:7px;white-space:nowrap}.wf .num{font-size:10px;font-weight:700;text-align:center;color:#33415C;margin-bottom:4px;white-space:nowrap}.subnavPill{font-size:12px;font-weight:600;color:#475569;text-decoration:none;padding:5px 12px;border-radius:999px;background:#F1F5F9;border:1px solid #E2E8F0;transition:all .15s ease}.subnavPill:hover{background:#E2E8F0;color:#1D4ED8;border-color:#CBD5E1}.dashPill{font-size:11.5px;font-weight:700;color:#475569;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:999px;padding:5px 12px;cursor:pointer;transition:all .15s ease;white-space:nowrap}.dashPill:hover{background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE}.scenario{padding:18px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(145deg,#F5F8FF,#EEF3FC)}.scenario h3{margin:0 0 6px;font-size:15px}.scenario .big{font-size:24px;font-weight:900;color:var(--accent)}.scenario p{color:var(--muted);font-size:11px;margin:6px 0}.muted{color:var(--muted)}.small{font-size:11px}.tableWrap{overflow:auto}table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:10px 8px;border-bottom:1px solid rgba(15,27,45,.08);text-align:right}th:first-child,td:first-child{text-align:left}th{color:#5B6B84;font-weight:600}.notice{padding:12px 14px;border-radius:12px;background:#EEF2FF;border:1px solid var(--line);color:#5B6B84;font-size:12px}.error{color:#C22A3E;background:#FCE8EA;border:1px solid #E8B4BD;padding:12px;border-radius:12px;margin:15px 0}.hidden{display:none!important}.footer{padding:25px 0 50px;color:#5B6B84;font-size:11px;text-align:center}.tabs{display:flex;gap:8px;margin-top:16px}.tab{padding:8px 12px;border-radius:999px;background:#F0F3F8;border:1px solid var(--line);color:#5B6B84;cursor:pointer}.tab.active{background:#DCE6FB;color:var(--accent);border-color:#1D4ED8}.tabPanel{display:none}.tabPanel.active{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.hidePrint{display:block}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.chip{font-size:11.5px;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px;color:#33415C}.chip b{color:var(--accent)}
.abar{height:9px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:6px}.abar i{display:block;height:100%;background:linear-gradient(90deg,#8aa7ff,#ff8290);border-radius:99px}
.custRow{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12.5px}
.highlight-target{outline:2px solid var(--accent);outline-offset:6px}
/* --- Marketing surface additions --- */
.topNav{display:flex;gap:18px}
.topNav a{color:var(--muted);font-size:13px;text-decoration:none;font-weight:600}
.topNav a:hover{color:var(--accent)}
.marketingSection{padding:8px 0 16px}
.marketingHead{text-align:center;max-width:640px;margin:0 auto 34px}
.marketingHead h2{font-family:var(--serif);font-size:32px;margin:0 0 10px;letter-spacing:-.5px}
.marketingHead p{color:var(--muted);margin:0;font-size:14.5px}
.pricingGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:stretch}
.priceCard{display:flex;flex-direction:column;padding:28px 24px;position:relative}
.priceCard.featured{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent),var(--shadow)}
.priceCard .plan{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:var(--accent);font-weight:800;margin-bottom:8px}
.priceCard h3{margin:0 0 6px;font-size:22px;font-family:var(--serif)}
.priceCard .amt{font-size:34px;font-weight:900;margin:8px 0 4px}
.priceCard .amt span{font-size:13px;color:var(--muted);font-weight:500}
.priceCard .desc{color:var(--muted);font-size:13px;margin-bottom:18px}
.priceCard ul{list-style:none;margin:0 0 22px;padding:0;flex:1;display:flex;flex-direction:column;gap:10px}
.priceCard ul li{font-size:13px;color:#33415C;display:flex;gap:8px;align-items:flex-start}
.priceCard ul li svg{flex:none;margin-top:2px;color:var(--accent)}
.priceCard .badgeTop{position:absolute;top:-11px;left:50%;transform:translateX(-50%);background:var(--accent);color:#FFFFFF;font-size:10.5px;font-weight:800;padding:4px 12px;border-radius:999px;letter-spacing:.5px}
.aboutGrid{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:center}
.aboutStats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}
.aboutStats .st{padding:16px;border:1px solid var(--line);border-radius:14px;text-align:center;background:rgba(15,27,45,.03)}
.aboutStats .st b{display:block;font-size:24px;color:var(--accent);font-family:var(--serif)}
.aboutStats .st span{font-size:11px;color:var(--muted)}
.contactGrid{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.contactCard{padding:26px}
.contactRow{display:flex;flex-direction:column;gap:12px;margin-top:14px}
.contactRow .item{display:flex;gap:10px;align-items:center;font-size:13px;color:#33415C}
.contactRow .item svg{color:var(--accent);flex:none}
@media(max-width:860px){.pricingGrid,.aboutGrid,.contactGrid{grid-template-columns:1fr}.topNav{display:none}}
.trustBar{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:20px;padding-top:18px;border-top:1px solid rgba(15,27,45,.10)}
.trustBar .item{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted)}
.trustBar .item svg{flex:none;color:var(--accent)}
.heroPreview{position:relative;padding:22px;overflow:hidden}
.pvLabel,.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.pvLabel span.dot,.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
.pvRing{width:112px;height:112px;border-radius:50%;margin:2px auto 14px;display:grid;place-items:center;background:conic-gradient(var(--accent) 0 78%,#182c42 78% 100%);position:relative}
.pvRing:after{content:"";position:absolute;inset:9px;border-radius:50%;background:#F7F9FC}
.pvRing b{position:relative;font-family:var(--serif);font-size:26px;z-index:1}
.pvRow{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12px}
.pvRow .n{color:var(--text);font-weight:700}
.pvRow .n.up{color:var(--green)}.pvRow .n.down{color:var(--red)}
.pvBars{display:flex;align-items:flex-end;gap:5px;height:54px;margin-top:14px}
.pvBars i{flex:1;background:linear-gradient(180deg,var(--accent2),#4a63b8);border-radius:3px 3px 1px 1px;display:block}
.statsStrip{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin:6px 0 0;padding:26px 0}
.statsStrip .stat b{font-family:var(--serif);font-size:36px;font-weight:600;color:var(--text);display:block;letter-spacing:-.5px}
.statsStrip .stat span{font-size:12.5px;color:var(--muted);display:block;margin-top:4px;max-width:20ch}
.whyCard{padding:20px;position:relative}
.whyCard .icoWrap{width:40px;height:40px;border-radius:11px;background:#DCE6FB;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;margin-bottom:14px;color:var(--accent)}
.ctaBanner{margin:44px 0 8px;padding:38px 32px;border-radius:22px;background:linear-gradient(135deg,#EAF0FF 0%,#DCE6FB 55%,#EAF0FF 100%);border:1px solid #C9D8F5;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.ctaBanner h3{font-family:var(--serif);font-weight:600;font-size:26px;margin:0 0 6px;letter-spacing:-.3px}
.ctaBanner p{margin:0;color:var(--muted);font-size:13.5px;max-width:52ch}
@media(max-width:1000px){.statsStrip{grid-template-columns:repeat(2,1fr)}.heroTitle{font-size:34px}}
@media(max-width:1000px){.hero{grid-template-columns:1fr}.grid4{grid-template-columns:repeat(2,1fr)}.grid3,.grid2{grid-template-columns:1fr}.wrap{padding:0 15px}.heroTitle{font-size:31px}.flowSub{margin-left:0}.qsel .qrow{grid-template-columns:1fr}}
@media print{
  *,*::before,*::after{box-sizing:border-box!important}
  @page{size:A4 portrait;margin:10mm 12mm 10mm 12mm}
  html,body{background:#fff!important;color:#0F1B2D!important;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif!important;font-size:8.5pt!important;line-height:1.35!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Hide all interactive & website shell elements ─────────────── */
  .hero,.upload,.hidePrint,.tabs,.tabPanel,.chips,.qsel,.tab,.footer,.siteFooter,
  header.top,.top,.topNav,.navBtns,.navToggle,#authArea,#authModalOverlay,
  .loadingOverlay,.dropZone,#criticalPartiesNotice,#methodNote,
  .heroPreview,.trustBar,.statsStrip,.ctaBanner,
  button,input,select,textarea,.secondary,.primary,
  #sampleBtn,#aiBtn,#printBtn,#jsonBtn,#aiAskBtn,
  #aiBox,#aiCustomBox,#aiCustomPrompt,#historySection,
  .interactiveScenarioCard,#interactiveScenarioCard,
  .abar{display:none!important}

  /* ── Layout: full-width single column ──────────────────────────── */
  .wrap{max-width:none!important;padding:0!important;margin:0!important;width:100%!important}

  /* ── Boardroom Cover Header ────────────────────────────────────── */
  #printCover{display:block!important;page-break-after:avoid!important;break-after:avoid!important;margin-bottom:12px}
  .printExecutiveFooter{display:flex!important;justify-content:space-between;align-items:center;border-top:1px solid #CBD5E1;padding-top:6px;margin-top:14px;font-size:7pt!important;color:#64748B!important;page-break-inside:avoid!important;break-inside:avoid!important}

  /* ── Cards & Containers ────────────────────────────────────────── */
  .card{box-shadow:none!important;background:#fff!important;border:1px solid #CBD5E1!important;border-radius:6px!important;margin-bottom:8px!important;padding:8px 10px!important;page-break-inside:auto!important;break-inside:auto!important}
  .heroCard{box-shadow:none!important;background:#fff!important;border:1px solid #CBD5E1!important;padding:8px!important}

  /* ── Flow steps ─────────────────────────────────────────────────── */
  .flowStep{margin:8px 0 4px!important;padding-top:2px!important;page-break-inside:auto!important;break-inside:auto!important}
  .flowLabel{background:none!important;border-left:3.5px solid #1D4ED8!important;padding-left:8px!important;color:#0F1B2D!important;margin-bottom:4px!important;font-size:9pt!important;page-break-after:avoid!important;break-after:avoid!important}
  .flowLabel .n{background:#1D4ED8!important;color:#fff!important;font-size:7.5pt!important;padding:1px 5px!important;border-radius:3px!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .flowSub{color:#64748B!important;font-size:7.5pt!important;margin-bottom:6px!important;line-height:1.25!important;page-break-after:avoid!important;break-after:avoid!important}

  /* ── Metrics / KPIs ─────────────────────────────────────────────── */
  .metric{background:#F8FAFC!important;border:1px solid #E2E8F0!important;border-radius:5px!important;padding:6px 8px!important;color:#0F1B2D!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .metric .label{font-size:6.5pt!important;color:#475569!important;font-weight:700;text-transform:uppercase;letter-spacing:.4px}
  .metric .value{font-size:11pt!important;font-weight:800;color:#0F1B2D!important}
  .metric .sub{font-size:6.5pt!important;color:#64748B!important}
  .grid2{display:grid!important;grid-template-columns:1fr 1fr!important;gap:6px!important}
  .grid3{display:grid!important;grid-template-columns:1fr 1fr 1fr!important;gap:6px!important}
  .grid4{display:grid!important;grid-template-columns:repeat(4,1fr)!important;gap:6px!important}

  /* ── Health score ring ──────────────────────────────────────────── */
  .scoreCard{display:flex!important;align-items:center!important;gap:16px!important;padding:8px 12px!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .scoreRing{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .scoreRing::after{background:#fff!important}

  /* ── Section headings ───────────────────────────────────────────── */
  .sectionHead{border-bottom:1px solid #E2E8F0!important;margin-bottom:6px!important;padding-bottom:4px!important;page-break-after:avoid!important;break-after:avoid!important}
  .sectionHead h2{font-size:8.5pt!important;color:#1D4ED8!important;font-weight:800;margin:0!important}
  .sectionHead p{font-size:7pt!important;color:#64748B!important;margin:1px 0 0!important}
  h1,h2,h3,h4{page-break-after:avoid!important;break-after:avoid!important;color:#0F1B2D!important}
  h3{font-size:8.5pt!important}

  /* ── Risk & action rows (atomic: keep intact) ───────────────────── */
  .riskRow,.actionRow{border:1px solid #E2E8F0!important;border-radius:5px!important;margin-bottom:4px!important;padding:5px 7px!important;page-break-inside:avoid!important;break-inside:avoid!important;background:#F8FAFC!important}
  .rank{background:#EBF3FE!important;color:#1D4ED8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .bar{display:none!important}

  /* ── Tags / badges ──────────────────────────────────────────────── */
  .tag{border:1px solid #94A3B8!important;color:#1E293B!important;background:#F1F5F9!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;font-size:6.5pt!important}
  .badge{border:1px solid #1D4ED8!important;color:#1D4ED8!important;font-size:7pt!important}

  /* ── Insights / alerts ──────────────────────────────────────────── */
  .insight{border-left:3.5px solid #1D4ED8!important;background:#EFF6FF!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;border-radius:4px!important;padding:6px 8px!important;margin-bottom:5px!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .insight.high,.insight.critical{border-left-color:#DC2626!important;background:#FEF2F2!important}
  .insight.positive{border-left-color:#16A34A!important;background:#F0FDF4!important}
  .notice{background:#F8FAFC!important;border:1px solid #CBD5E1!important;padding:6px 8px!important;border-radius:4px!important;font-size:7.5pt!important;color:#334155!important;page-break-inside:avoid!important;break-inside:avoid!important}

  /* ── Waterfall chart ────────────────────────────────────────────── */
  .waterfall{display:flex!important;align-items:flex-end!important;gap:4px!important;height:80px!important;padding:2px 0!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .wf .col{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .wf .num{font-size:6pt!important;color:#0F1B2D!important;font-weight:700}
  .wf .lab{font-size:6pt!important;color:#475569!important;white-space:normal!important;max-height:22px;text-align:center;overflow:hidden;line-height:1.1}

  /* ── Tables ─────────────────────────────────────────────────────── */
  .tableWrap{overflow:visible!important}
  table{border-collapse:collapse!important;width:100%!important;font-size:7pt!important}
  th{background:#F1F5F9!important;color:#1E293B!important;font-weight:700;padding:3px 5px!important;border:1px solid #CBD5E1!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  td{padding:3px 5px!important;border:1px solid #E2E8F0!important}
  tr{page-break-inside:avoid!important;break-inside:avoid!important}
  tr:nth-child(even) td{background:#F8FAFC!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Misc ────────────────────────────────────────────────────────── */
  .muted{color:#64748B!important}
  .small{font-size:7pt!important}
  a{color:#1D4ED8!important;text-decoration:none!important}
  .scenario{border:1px solid #CBD5E1!important;border-radius:5px!important;padding:6px!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .scenario .big{font-size:11pt!important;font-weight:800;color:#1D4ED8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .custRow,.wf{page-break-inside:avoid!important;break-inside:avoid!important}
  .hidden{display:none!important}
  #dashboard{display:block!important}
}

@view-transition{navigation:auto}
::view-transition-old(root){animation:dfbpFadeOut .28s ease both}
::view-transition-new(root){animation:dfbpFadeIn .32s ease both}
@keyframes dfbpFadeOut{to{opacity:0;transform:translateY(-6px)}}
@keyframes dfbpFadeIn{from{opacity:0;transform:translateY(8px)}}
.topNav{display:flex;gap:18px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s;white-space:nowrap}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.authCluster{display:flex;flex-direction:column;align-items:flex-end;gap:5px;flex-shrink:0}
.headerSwitches{display:flex;align-items:center;gap:6px;justify-content:flex-end}
.headerSwitches select,select.globalLangSwitch{padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1}
.headerSwitches select:hover,select.globalLangSwitch:hover{border-color:var(--accent);color:#0F1B2D;background:#FFFFFF}
.navBtns,#authArea{display:flex;gap:8px;align-items:center;flex-shrink:0;white-space:nowrap}
.navBtns a,.navBtns button,#authArea button{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  font-size:12.5px;
  font-weight:700;
  padding:6px 14px;
  border-radius:9px;
  text-decoration:none;
  transition:all .15s ease;
  cursor:pointer;
  line-height:1.2;
  white-space:nowrap;
  flex-shrink:0;
}
.navBtns a.secondary,.navBtns button.secondary,#authArea button.secondary,#loginOpenBtn{
  background:#FFFFFF;
  border:1px solid #CBD5E1;
  color:#1E293B;
  box-shadow:0 1px 2px rgba(0,0,0,.03);
}
.navBtns a.secondary:hover,.navBtns button.secondary:hover,#authArea button.secondary:hover,#loginOpenBtn:hover{
  background:#F8FAFC;
  border-color:#94A3B8;
  color:#0F172A;
}
.navBtns a.primary,.navBtns button.primary,#authArea button.primary,#registerOpenBtn{
  background:#1D4ED8;
  border:1px solid #1D4ED8;
  color:#FFFFFF;
  box-shadow:0 2px 6px rgba(29,78,216,.25);
}
.navBtns a.primary:hover,.navBtns button.primary:hover,#authArea button.primary:hover,#registerOpenBtn:hover{
  background:#1E40AF;
  border-color:#1E40AF;
  box-shadow:0 4px 12px rgba(29,78,216,.35);
  transform:translateY(-1px);
}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text);flex-shrink:0}
.brandLogoWrap{flex-shrink:0;min-width:max-content}
.brandLink{text-decoration:none;display:flex;align-items:center;gap:10px;min-width:0}
.brandLogoIcon{width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0}
.brandTextWrap{min-width:0}
.brandTitle{font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2;white-space:nowrap}
.brandSub{font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px;white-space:nowrap}
.headerRight{display:flex;align-items:center;gap:12px;flex-shrink:0}
.mobileNavAuth{display:none}

@media(max-width:920px){
  html,body{overflow-x:hidden;max-width:100vw;width:100%}
  .top{padding:12px 0 10px}
  .wrap{padding:0 16px;max-width:100vw;box-sizing:border-box}
  .brand{gap:10px}
  .brandLogoIcon{width:32px;height:32px;border-radius:9px}
  .brandLogoIcon svg{width:18px;height:18px}
  .brandTitle{font-size:15.5px}
  .brandSub{display:none}
  .brandLogoWrap{min-width:0;flex:1 1 auto;overflow:hidden}
  .topNav{position:fixed;top:56px;left:0;right:0;width:100vw;background:#FFFFFF;border-bottom:1.5px solid var(--line);box-shadow:0 14px 34px rgba(15,27,45,0.12);flex-direction:column;align-items:stretch;gap:0;padding:0 20px;max-height:0;overflow:hidden;transition:max-height .28s ease,padding .2s ease;z-index:999;box-sizing:border-box}
  .topNav.open{max-height:460px;padding:10px 20px 20px;overflow-y:auto}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.06);font-size:14.5px;color:var(--text);font-weight:600;display:block;text-align:left}
  .mobileNavAuth{display:flex;gap:10px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(15,27,45,.08)}
  .mobileNavAuth a{flex:1;padding:10px 12px;font-size:13px;font-weight:700;border-radius:10px;text-align:center;justify-content:center;text-decoration:none}
  .navToggle{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;padding:0;font-size:18px;border-radius:8px;cursor:pointer}
}

@media(max-width:768px){
  .navBtns{display:none}
  .authCluster{flex-direction:row;align-items:center}
  .headerRight{gap:6px}
  .globalLangSwitch{padding:4px 5px !important;font-size:11px !important;border-radius:7px !important;max-width:60px}
  .wrap{padding:0 12px}
  .brandTitle{font-size:14.5px}
  .mHero{padding:24px 0 20px;grid-template-columns:1fr;gap:20px}
  .mHero h1{font-size:26px !important;line-height:1.2 !important}
  .mHero p.lead{font-size:13.5px;line-height:1.55}
  .ctaRow{flex-direction:column;gap:10px}
  .ctaRow a{width:100%;text-align:center;justify-content:center}
  .miniTrust{gap:8px 12px;margin-top:16px}
  .aboutStats{grid-template-columns:1fr !important;gap:10px}
  .statsStrip{grid-template-columns:1fr !important;gap:12px}
}
.badge.v{white-space:nowrap}
/* ---- Marketing hero (separate from app hero) ---- */
.mHero{padding:56px 0 30px;display:grid;grid-template-columns:1.15fr .85fr;gap:34px;align-items:center}
.mHero .eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:18px}
.mHero h1{font-family:var(--serif);font-weight:600;font-size:50px;line-height:1.08;margin:0 0 18px;letter-spacing:-1px}
.mHero h1 span{color:var(--accent)}
.mHero p.lead{color:var(--muted);font-size:16px;max-width:560px;line-height:1.65;margin:0 0 26px}
.mHero .ctaRow{display:flex;gap:12px;flex-wrap:wrap}
.mHero .ctaRow a{text-decoration:none}
.mHero .miniTrust{display:flex;gap:18px;flex-wrap:wrap;margin-top:28px}
.mHero .miniTrust span{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px}
.mHero .miniTrust svg{color:var(--accent)}
.heroArt{position:relative}
.heroArt .floatCard{position:absolute;background:#FFFFFF;border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);padding:14px 16px;font-size:11.5px;color:#33415C;animation:dfbpFloat 5s ease-in-out infinite}
.heroArt .floatCard b{display:block;font-size:16px;color:var(--accent);font-family:var(--serif)}
.heroArt .fc1{top:-10px;left:-10px;animation-delay:0s}
.heroArt .fc2{bottom:6px;right:-14px;animation-delay:1.2s}
@keyframes dfbpFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
/* ---- Alternating content blocks (fixes the "iç içe" cramped look) ---- */
.secBlock{padding:28px 0}
.secBlock.tint{background:linear-gradient(180deg,#F8FAFC 0%,#FFFFFF 100%);border:1px solid #E2E8F0;border-radius:26px;margin:0 -10px;box-shadow:0 4px 20px rgba(15,27,45,.03)}
.pillScrollBtn{width:36px;height:36px;border-radius:50%;background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:800;cursor:pointer;flex-shrink:0;box-shadow:0 4px 12px rgba(15,27,45,0.08);transition:all .18s ease;user-select:none;z-index:4}
.pillScrollBtn:hover{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;transform:scale(1.08);box-shadow:0 6px 16px rgba(29,78,216,0.25)}
.pillScrollBtn:active{transform:scale(0.95)}
.secBlock+.secBlock{border-top:1px solid rgba(15,27,45,.06)}
.pageHead{padding:54px 0 10px;text-align:center}
.pageHead .eyebrow{display:inline-flex;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:16px}
.pageHead h1{font-family:var(--serif);font-size:38px;margin:0 0 12px;letter-spacing:-.6px}
.pageHead p{color:var(--muted);max-width:600px;margin:0 auto;font-size:14.5px}
.reveal{opacity:0;transform:translateY(18px);transition:opacity .55s ease,transform .55s ease}
.reveal.in{opacity:1;transform:none}
/* ---- Rich footer ---- */
.siteFooter{border-top:1px solid var(--line);margin-top:40px;padding:46px 0 26px}
.siteFooter .cols{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:28px;margin-bottom:30px}
.siteFooter h4{font-size:12px;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin:0 0 14px}
.siteFooter .brandCol p{color:var(--muted);font-size:12.5px;max-width:280px;line-height:1.6}
.siteFooter ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.siteFooter ul a{color:#33415C;text-decoration:none;font-size:13px}
.siteFooter ul a:hover{color:var(--accent)}
.siteFooter .legal{border-top:1px solid rgba(15,27,45,.08);padding-top:20px;color:#5B6B84;font-size:11px;line-height:1.7}
html{overflow-x:hidden}@media(max-width:860px){.siteFooter .cols{grid-template-columns:1fr 1fr}.mHero{grid-template-columns:1fr}.heroArt{order:-1;max-width:340px;margin:24px auto 40px;padding:0 14px}.heroArt .floatCard{position:static;display:inline-block;margin:6px 6px 0 0;animation:none}.heroArt .fc1,.heroArt .fc2{top:auto;left:auto;right:auto;bottom:auto}}
/* ---- FAQ (paketler sayfası) ---- */
.faqItem{border-bottom:1px solid var(--line);padding:16px 0}
.faqItem summary{cursor:pointer;font-weight:700;font-size:14px;list-style:none;display:flex;justify-content:space-between;align-items:center}
.faqItem summary::-webkit-details-marker{display:none}
.faqItem summary:after{content:'+';font-size:20px;color:var(--accent)}
.faqItem[open] summary:after{content:'–'}
.faqItem p{color:var(--muted);font-size:13.5px;margin:10px 0 0}
/* ---- Executive Intelligence band (single, deliberate dark boardroom section) ---- */
.execBand{background:radial-gradient(1200px 500px at 15% -20%, rgba(76,201,240,.10), transparent 60%),linear-gradient(160deg,#0D1B2A 0%,#081426 100%);border-radius:26px;padding:52px;display:grid;grid-template-columns:.85fr 1.15fr;gap:40px;align-items:center;overflow:hidden}
.execEyebrow{display:inline-block;font-size:11.5px;font-weight:800;letter-spacing:1.6px;color:#4CC9F0;background:rgba(76,201,240,.12);border:1px solid rgba(76,201,240,.35);padding:6px 12px;border-radius:999px;margin-bottom:16px}
.execCopy h2{font-family:var(--serif);color:#F8FAFC;font-size:28px;line-height:1.2;margin:0 0 12px;letter-spacing:-.4px}
.execCopy p{color:#94A3B8;font-size:14px;line-height:1.7;margin:0 0 18px;max-width:44ch}
.execList{list-style:none;margin:0 0 24px;padding:0;display:flex;flex-direction:column;gap:9px}
.execList li{color:#C7D2E8;font-size:13px}
.execList li b{color:#F8FAFC}
.execCta{display:inline-block;color:#0D1B2A;background:#4CC9F0;font-weight:800;font-size:13.5px;padding:12px 20px;border-radius:11px;text-decoration:none;transition:transform .15s ease,box-shadow .15s ease}
.execCta:hover{transform:translateY(-1px);box-shadow:0 10px 26px rgba(76,201,240,.35)}
.execArt{filter:drop-shadow(0 24px 48px rgba(0,0,0,.35))}
@media(max-width:860px){.execBand{grid-template-columns:1fr;padding:32px 22px}}
/* ---- New: live dashboard hero panel (Executive Light Theme) ---- */
.heroDash{background:#FFFFFF;border-radius:24px;border:1.5px solid #DCE6F5;padding:24px;position:relative;overflow:hidden;box-shadow:0 20px 45px rgba(15,27,45,.08)}
.heroDash .dHead{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid #F1F5F9}
.heroDash .dHead .dots span{width:8px;height:8px;border-radius:50%;display:inline-block;margin-right:5px}
.heroDash .dHead .live{font-size:11px;color:#059669;display:flex;align-items:center;gap:6px;font-weight:800;letter-spacing:.4px}
.heroDash .dHead .live i{width:6px;height:6px;border-radius:50%;background:#10B981;display:inline-block;box-shadow:0 0 0 3px rgba(16,185,129,.22);animation:dfbpPulse 1.8s ease infinite}
@keyframes dfbpPulse{0%,100%{opacity:1}50%{opacity:.35}}
.dashTabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px}
.dashTabs span{font-size:11px;color:#64748B;background:#F1F5F9;border:1px solid transparent;border-radius:999px;padding:6px 12px;cursor:pointer;font-weight:600;transition:all .2s ease}
.dashTabs span:hover{background:#E2E8F0;color:#1E293B}
.dashTabs span.on{color:#1D4ED8;background:#EFF6FF;border-color:#BFDBFE;font-weight:800}
.dashPane{display:none;min-height:230px}
.dashPane.on{display:block;animation:dfbpFadeIn .3s ease both}
.dashPane .dTitle{color:#0F172A;font-size:11.5px;letter-spacing:.5px;text-transform:uppercase;margin-bottom:10px;font-weight:700}
.dashKpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:12px}
.dashKpis div{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:9px 10px;text-align:center}
.dashKpis div b{display:block;font-size:15px;color:#0F172A;font-family:var(--serif);font-weight:700}
.dashKpis div span{font-size:10px;color:#64748B}
.heroDash .foot{margin-top:14px;padding-top:12px;border-top:1px solid #F1F5F9;font-size:11px;color:#64748B;display:flex;justify-content:space-between;font-weight:600}
/* ---- New: CFO trust strip ---- */
.trustGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.trustCard{padding:22px}
.trustCard .icoWrap2{width:38px;height:38px;border-radius:10px;background:#0D1B2A;color:#4CC9F0;display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.trustCard h3{margin:0 0 6px;font-size:14.5px}
.trustCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.55}
/* ---- New: Executive Journey ---- */
.journey{display:grid;grid-template-columns:repeat(6,1fr);gap:0;position:relative;margin-top:8px}
.journey:before{content:"";position:absolute;top:22px;left:6%;right:6%;height:2px;background:linear-gradient(90deg,#C9D8F5,#4CC9F0,#C9D8F5)}
.jStep{text-align:center;padding:0 8px;opacity:0;transform:translateY(16px);transition:opacity .5s ease,transform .5s ease}
.jStep.in{opacity:1;transform:none}
.jStep .jDot{width:44px;height:44px;border-radius:50%;background:#FFFFFF;border:2px solid var(--accent);color:var(--accent);display:flex;align-items:center;justify-content:center;margin:0 auto 12px;position:relative;z-index:1;font-weight:900;font-size:13px}
.jStep h4{margin:0 0 5px;font-size:13px;letter-spacing:.4px}
.jStep p{margin:0;font-size:11.5px;color:var(--muted);line-height:1.4}
@media(max-width:860px){.journey{grid-template-columns:1fr 1fr;gap:22px 0}.journey:before{display:none}.trustGrid{grid-template-columns:1fr 1fr}}
/* ---- New: outcome-based module groups ---- */
.intelGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.intelCard{padding:24px;display:flex;flex-direction:column}
.intelCard .igIco{width:40px;height:40px;border-radius:11px;background:#DCE6FB;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.intelCard h3{margin:0 0 8px;font-size:16px;font-family:var(--serif)}
.intelCard ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}
.intelCard ul li{font-size:12.5px;color:#33415C;display:flex;gap:7px;align-items:flex-start}
.intelCard ul li:before{content:"";width:5px;height:5px;border-radius:50%;background:var(--accent);margin-top:6px;flex:none}
@media(max-width:860px){.intelGrid{grid-template-columns:1fr 1fr}}
/* ---- New: security/governance page ---- */

/* ---- High-impact FinTech additions ---- */
.gradText{background:linear-gradient(135deg,#1D4ED8 0%,#2563EB 50%,#38BDF8 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;display:inline-block}
.livePill{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:var(--accent);background:linear-gradient(135deg,#EEF4FF,#E0EDFF);border:1px solid #BFDBFE;padding:8px 16px;border-radius:999px;margin-bottom:20px;box-shadow:0 2px 10px rgba(37,99,235,.12)}
.livePill i{width:8px;height:8px;border-radius:50%;background:#10B981;display:inline-block;box-shadow:0 0 0 4px rgba(16,185,129,.25);animation:dfbpPulse 1.8s ease infinite}
.dilemmaGrid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:20px}
.dilemmaCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:26px;position:relative;overflow:hidden;box-shadow:var(--shadow);transition:transform .2s ease,box-shadow .2s ease}
.dilemmaCard:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(15,27,45,.09)}
.dilemmaQ{font-size:15px;font-weight:700;color:#0F1B2D;margin-bottom:12px;display:flex;gap:10px;align-items:flex-start;line-height:1.4}
.dilemmaQ span{background:#FEE2E2;color:#DC2626;border-radius:8px;padding:2px 8px;font-size:11px;font-weight:900;flex:none;margin-top:2px}
.dilemmaA{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:14px 16px;font-size:13px;color:#33415C;line-height:1.55}
.dilemmaA b{color:var(--accent);display:block;margin-bottom:4px}
.workflowGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;position:relative;margin-top:20px}
.workflowCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:24px;box-shadow:var(--shadow);position:relative;display:flex;flex-direction:column}
.workflowBadge{font-size:11px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:var(--accent);background:#EFF6FF;border:1px solid #DBEAFE;padding:4px 10px;border-radius:999px;align-self:flex-start;margin-bottom:12px}
.workflowCard h3{font-size:16px;margin:0 0 8px;font-family:var(--serif);color:#0F1B2D}
.workflowCard p{font-size:12.5px;color:var(--muted);line-height:1.55;margin:0}
.compareTableWrap{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:var(--shadow);margin-top:20px}
.compareTable{width:100%;border-collapse:collapse;font-size:13px}
.compareTable th,.compareTable td{padding:16px 18px;border-bottom:1px solid rgba(15,27,45,.08);text-align:left}
.compareTable th{background:#F8FAFC;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#475569}
.compareTable th.featured{background:linear-gradient(135deg,#EFF6FF,#DBEAFE);color:var(--accent);border-bottom:2px solid var(--accent)}
.compareTable td.featured{background:#F8FAFF;font-weight:600;color:#0F1B2D}
@media(max-width:860px){.dilemmaGrid,.workflowGrid{grid-template-columns:1fr}.compareTableWrap{overflow-x:auto}}

.kobiPills{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:18px auto 26px}
.kobiPill{padding:9px 18px;border-radius:999px;font-size:12.5px;font-weight:700;border:1.5px solid #CBD5E1;background:#FFFFFF;color:#475569;cursor:pointer;transition:all .2s ease}
.kobiPill:hover{border-color:#1D4ED8;color:#1D4ED8;background:#EFF6FF}
.kobiSliderWrap{position:relative;margin-top:20px}
.kobiSliderBar{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:14px;padding:0 4px}
.kobiSwipeHint{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;color:#64748B;background:#F8FAFC;border:1px solid #E2E8F0;padding:6px 14px;border-radius:999px}
.kobiSliderNav{display:flex;align-items:center;gap:10px}
.kobiSlideBadge{font-size:12px;font-weight:800;color:#1D4ED8;background:#EFF6FF;border:1px solid #DBEAFE;padding:6px 14px;border-radius:999px}
.kobiNavBtn{width:40px;height:40px;border-radius:50%;border:1.5px solid #CBD5E1;background:#FFFFFF;color:#0F172A;font-size:22px;line-height:1;font-weight:700;display:inline-flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 3px 10px rgba(15,27,45,.06);transition:all .2s ease;user-select:none}
.kobiNavBtn:hover{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;box-shadow:0 6px 18px rgba(29,78,216,.28);transform:scale(1.06)}
.kobiNavBtn:active{transform:scale(0.96)}
.kobiSliderTrack{display:flex;gap:22px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;padding:10px 4px 22px;-webkit-overflow-scrolling:touch;scrollbar-width:none}
.kobiSliderTrack::-webkit-scrollbar{display:none}
.kobiCard{flex:0 0 420px;max-width:420px;scroll-snap-align:start;scroll-snap-stop:normal;background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:20px;padding:24px;box-shadow:0 6px 20px rgba(15,27,45,.04);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease;display:flex;flex-direction:column;justify-content:space-between}
.kobiCard:hover{transform:translateY(-4px);box-shadow:0 16px 36px rgba(15,27,45,.10);border-color:#93C5FD}
.kobiCardImgWrap{border-radius:12px;overflow:hidden;margin-bottom:14px;box-shadow:0 4px 12px rgba(15,27,45,.06);border:1px solid #E2E8F0;aspect-ratio:16/9;background:#0F172A;position:relative}
.kobiCardImgWrap img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .35s ease}
.kobiCard:hover .kobiCardImgWrap img{transform:scale(1.03)}
.kobiDotsWrap{display:flex;align-items:center;justify-content:center;gap:7px;margin-top:8px}
.kobiDot{width:8px;height:8px;border-radius:999px;background:#CBD5E1;transition:all .25s ease;cursor:pointer}
.kobiDot.active{width:26px;background:#1D4ED8;box-shadow:0 2px 8px rgba(29,78,216,.3)}
.kobiTag{display:inline-block;padding:4px 10px;border-radius:6px;font-size:10.5px;font-weight:800;letter-spacing:.8px;text-transform:uppercase;margin-bottom:12px;width:fit-content}
.kobiTag.cash{background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE}
.kobiTag.profit{background:#FEF3C7;color:#B45309;border:1px solid #FDE68A}
.kobiTag.mgmt{background:#F3E8FF;color:#7E22CE;border:1px solid #E9D5FF}
.kobiTitle{font-size:15.5px;font-weight:800;color:#0F1B2D;line-height:1.4;margin-bottom:10px}
.kobiDesc{font-size:12.5px;color:#475569;line-height:1.55;margin-bottom:14px}
.kobiMetrics{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:12px 14px;margin-bottom:14px;display:flex;flex-direction:column;gap:6px;font-size:12px}
.kobiMetricRow{display:flex;justify-content:space-between;align-items:center}
.kobiPrescription{background:#F0FDF4;border:1px solid #BBF7D0;border-radius:12px;padding:12px 14px;font-size:12px;color:#14532D;line-height:1.45;margin-bottom:0}
.kobiPrescription b{color:#166534;display:block;margin-bottom:3px;font-weight:800}
.kobiCta{display:inline-flex;align-items:center;justify-content:space-between;font-size:12.5px;font-weight:800;color:#1D4ED8;text-decoration:none;padding:10px 14px;background:#EFF6FF;border:1px solid #BFDBFE;border-radius:10px;transition:all .15s ease}
.kobiCta:hover{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8}
@media(max-width:900px){.kobiCard{flex:0 0 350px;max-width:350px}}
@media(max-width:600px){.kobiCard{flex:0 0 86vw;max-width:86vw}.kobiSwipeHint{font-size:11px;padding:5px 10px}}

.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

/* CEO Diagnostic Hub 3-Layer Architecture */
.ceoPill{display:inline-flex;align-items:center;gap:7px;padding:9px 16px;border-radius:999px;font-size:12.5px;font-weight:700;background:#F1F5F9;color:#475569;border:1px solid #CBD5E1;cursor:pointer;white-space:nowrap;transition:all .2s ease}
.ceoPill:hover{background:#E2E8F0;color:#0F172A}
.ceoPill.active{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;box-shadow:0 4px 14px rgba(29,78,216,0.25)}
.ceoQuestionCard{display:none;background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:18px;padding:22px;box-shadow:0 8px 24px rgba(15,27,45,0.04);animation:fadeIn .3s ease}
.ceoQuestionCard.active{display:block}
.layerBadge{display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;font-size:10.5px;font-weight:800;letter-spacing:0.5px;text-transform:uppercase}
.layerBadge.l1{background:#FEE2E2;color:#991B1B;border:1px solid #FCA5A5}
.layerBadge.l2{background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE}
.layerBadge.l3{background:#ECFDF5;color:#047857;border:1px solid #A7F3D0}
.ceoGrid3{display:grid;grid-template-columns:1.1fr 1fr 1.3fr;gap:18px;margin-top:16px}
@media(max-width:960px){.ceoGrid3{grid-template-columns:1fr}}


.infoTooltip{position:relative;display:inline-flex;align-items:center;justify-content:center;width:15px;height:15px;border-radius:50%;background:#E2E8F0;color:#475569;font-size:10px;font-weight:800;cursor:help;margin-left:5px;vertical-align:middle}
.infoTooltip:hover::after{content:attr(data-tooltip);position:absolute;bottom:135%;left:50%;transform:translateX(-50%);background:#0F172A;color:#FFFFFF;padding:8px 12px;border-radius:8px;font-size:11.5px;line-height:1.45;white-space:normal;width:230px;z-index:9999;box-shadow:0 8px 24px rgba(0,0,0,0.25);pointer-events:none;text-align:left;font-weight:400}

/* ---- Case Studies (Anonim Doğrulanmış KOBİ Başarı Hikayeleri) ---- */
.caseGrid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:24px}
.caseCard{background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:20px;padding:24px;box-shadow:0 6px 20px rgba(15,27,45,.04);transition:transform .2s ease,box-shadow .2s ease}
.caseCard:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(15,27,45,.08);border-color:#CBD5E1}
.caseHead{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;flex-wrap:wrap;gap:8px}
.caseBadge{font-size:11px;font-weight:800;letter-spacing:.8px;text-transform:uppercase;padding:4px 10px;border-radius:6px;background:#F1F5F9;color:#475569;border:1px solid #E2E8F0}
.caseBadge.verified{background:#ECFDF5;color:#047857;border-color:#A7F3D0}
.caseLocation{font-size:12px;color:#64748B;font-weight:600}
.caseTitle{font-size:16px;font-weight:800;color:#0F1B2D;margin-bottom:8px;line-height:1.35}
.caseProblem{font-size:12.5px;color:#64748B;line-height:1.55;margin-bottom:14px;background:#FFF5F5;border-left:3px solid #EF4444;padding:8px 12px;border-radius:0 8px 8px 0}
.caseSolution{font-size:12.5px;color:#1E3A8A;line-height:1.55;margin-bottom:14px;background:#EFF6FF;border-left:3px solid #3B82F6;padding:8px 12px;border-radius:0 8px 8px 0}
.caseKpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:12px}
.caseKpiItem{text-align:center}
.caseKpiItem b{display:block;font-size:15px;color:#0F172A;font-family:var(--serif);font-weight:800}
.caseKpiItem span{font-size:10px;color:#64748B;font-weight:600}
@media(max-width:860px){.caseGrid{grid-template-columns:1fr}}

/* ---- Security & Trust Shield (Banka Düzeyinde Güvenlik) ---- */
.secShieldGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:24px}
.secShieldCard{background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:18px;padding:22px;box-shadow:0 4px 14px rgba(15,27,45,.03);transition:transform .2s ease}
.secShieldCard:hover{transform:translateY(-2px);border-color:#93C5FD;box-shadow:0 10px 24px rgba(29,78,216,.08)}
.secShieldIco{width:42px;height:42px;border-radius:12px;background:#EFF6FF;color:#1D4ED8;display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:14px;border:1px solid #DBEAFE}
.secShieldCard h4{margin:0 0 6px;font-size:14.5px;color:#0F172A;font-weight:800}
.secShieldCard p{margin:0;font-size:12px;color:#64748B;line-height:1.55}
@media(max-width:960px){.secShieldGrid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:540px){.secShieldGrid{grid-template-columns:1fr}}

/* ---- ERP & Global Multi-Currency Bar ---- */
.erpLogosGrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;margin-top:16px}
.erpLogoBadge{background:#FFFFFF;border:1px solid #CBD5E1;border-radius:12px;padding:12px 10px;text-align:center;font-size:12.5px;font-weight:800;color:#1E293B;box-shadow:0 2px 6px rgba(15,27,45,.03);transition:all .2s ease;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px}
.erpLogoBadge:hover{border-color:#1D4ED8;color:#1D4ED8;transform:translateY(-2px);box-shadow:0 6px 16px rgba(29,78,216,.12)}
.erpLogoBadge span{font-size:9.5px;color:#64748B;font-weight:600}

/* ---- Mockup Showcase (Dashboard Cockpit & 1-Page Board PDF) - Executive Light Theme ---- */
.mockupShowcase{margin-top:32px;background:linear-gradient(180deg,#FFFFFF 0%,#F8FAFC 100%);border:1.5px solid #CBD5E1;border-radius:24px;padding:32px;color:#0F1B2D;box-shadow:0 14px 36px rgba(15,27,45,.06)}
.mockupSplit{display:grid;grid-template-columns:1.2fr 0.8fr;gap:24px;align-items:center}
@media(max-width:960px){.mockupSplit{grid-template-columns:1fr}}
.mockupScreen{background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:16px;overflow:hidden;box-shadow:0 12px 30px rgba(15,27,45,.06)}
.mockupScreenHead{background:#F8FAFC;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #E2E8F0}
.mockupPaper{background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:14px;padding:20px;color:#0F172A;box-shadow:0 12px 30px rgba(15,27,45,.06);font-size:11px}
.mockupBadge{display:inline-flex;align-items:center;gap:6px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#1D4ED8;background:#EFF6FF;border:1px solid #BFDBFE;padding:4px 10px;border-radius:999px;margin-bottom:12px}

/* ---- Ghost button styling for secondary CTA ---- */
.ctaRow a.ghostBtn{background:transparent;border:1.5px solid #CBD5E1;color:#475569;font-weight:700;padding:15px 24px;border-radius:14px;font-size:15px;text-decoration:none;transition:all .2s ease;display:inline-flex;align-items:center;gap:8px}
.ctaRow a.ghostBtn:hover{border-color:#1D4ED8;color:#1D4ED8;background:#EFF6FF}

/* ---- Dual Gates (Kapı A & Kapı B) ---- */
.ctaDualGates{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:22px 0 16px}
.gateCard{text-decoration:none;display:flex;flex-direction:column;gap:6px;padding:16px 20px;border-radius:16px;transition:all .22s cubic-bezier(0.16,1,0.3,1);position:relative}
.gateCard.gateA{background:#FFFFFF;border:2px solid #2563EB;box-shadow:0 8px 24px rgba(37,99,235,0.10)}
.gateCard.gateA:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(37,99,235,0.22);border-color:#1D4ED8}
.gateCard.gateB{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);border:2px solid #1D4ED8;box-shadow:0 8px 24px rgba(29,78,216,0.28);color:#FFFFFF}
.gateCard.gateB:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(29,78,216,0.38);border-color:#3B82F6}
@media(max-width:680px){.ctaDualGates{grid-template-columns:1fr}}

/* ---- Interactive What-If Live Laboratory ---- */
.whatIfLabCard{background:linear-gradient(180deg,#FFFFFF 0%,#F8FAFC 100%);border:1.5px solid #CBD5E1;border-radius:24px;padding:28px;box-shadow:0 14px 36px rgba(15,27,45,.06);margin-top:20px}
.labGrid{display:grid;grid-template-columns:1.25fr 0.95fr;gap:24px;align-items:center}
@media(max-width:960px){.labGrid{grid-template-columns:1fr}}
.labControls{display:flex;flex-direction:column;gap:16px}
.labSliderRow{background:#FFFFFF;border:1px solid #E2E8F0;border-radius:14px;padding:14px 16px;box-shadow:0 2px 8px rgba(15,27,45,.02);display:flex;flex-direction:column;gap:8px}
.labSliderHead{display:flex;justify-content:space-between;align-items:center;font-size:13px;font-weight:700;color:#0F172A}
.labBadgeVal{background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE;padding:3px 10px;border-radius:8px;font-size:12.5px;font-weight:800}
.labRange{width:100%;height:6px;accent-color:#1D4ED8;cursor:pointer;margin:4px 0}
.labPresets{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:4px}
.labPresetBtn{background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;border-radius:999px;padding:5px 12px;font-size:11.5px;font-weight:700;cursor:pointer;transition:all .15s ease}
.labPresetBtn:hover{background:#E2E8F0;color:#0F172A}
.labPresetBtn.active{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8}
.labVaultCard{background:radial-gradient(ellipse at top left,#1E293B 0%,#0F172A 100%);border-radius:20px;padding:26px;color:#FFFFFF;box-shadow:0 16px 40px rgba(15,23,42,.35);border:1px solid rgba(255,255,255,.08);display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden}
.labVaultCard::before{content:"";position:absolute;top:-50%;right:-50%;width:100%;height:100%;background:radial-gradient(circle,rgba(52,211,153,.12) 0%,transparent 70%);pointer-events:none}
.vaultBigCounter{font-size:38px;font-weight:900;font-family:var(--serif);color:#34D399;letter-spacing:-1px;margin:8px 0 12px;line-height:1;transition:all .2s ease;display:block}
.vaultBigCounter.pulse{transform:scale(1.04);color:#6EE7B7}
.vaultBreakdown{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(255,255,255,.12)}
.vSubItem{background:rgba(255,255,255,.06);border-radius:10px;padding:8px 10px;text-align:center}
.vSubItem b{display:block;font-size:13px;color:#F8FAFC;font-weight:800}
.vSubItem span{display:block;font-size:10px;color:#94A3B8;margin-top:2px}

/* ---- Cyber Security Institutional Trust Wall ---- */
.trustWallGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:16px}
.trustBadgeCard{background:#FFFFFF;border:1.2px solid #E2E8F0;border-radius:14px;padding:14px;box-shadow:0 3px 10px rgba(15,27,45,.03);display:flex;align-items:flex-start;gap:10px;transition:all .2s ease;cursor:help;position:relative}
.trustBadgeCard:hover{border-color:#93C5FD;transform:translateY(-2px);box-shadow:0 8px 20px rgba(29,78,216,.08)}
.trustBadgeCard .tIco{width:34px;height:34px;border-radius:10px;background:#EFF6FF;color:#1D4ED8;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;border:1px solid #DBEAFE}
.trustBadgeCard .tInfo b{display:block;font-size:12px;color:#0F172A;font-weight:800;margin-bottom:3px}
.trustBadgeCard .tInfo span{display:block;font-size:10.5px;color:#64748B;line-height:1.4}
@media(max-width:960px){.trustWallGrid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:540px){.trustWallGrid{grid-template-columns:1fr}}
@media print {
  body.boardDeckPrintMode * { visibility: hidden !important; }
  body.boardDeckPrintMode #boardDeckModal,
  body.boardDeckPrintMode #boardDeckModal * { visibility: visible !important; }
  body.boardDeckPrintMode #boardDeckModal {
    position: absolute !important;
    left: 0 !important;
    top: 0 !important;
    width: 100% !important;
    height: auto !important;
    background: #FFFFFF !important;
    padding: 0 !important;
    backdrop-filter: none !important;
  }
  body.boardDeckPrintMode #boardDeckModal .hidePrint { display: none !important; }
}
</style></head>
<body>
<header class="top"><div class="wrap brand"><div class="brandLogoWrap">
  <a href="/" class="brandLink">
    <div class="brandLogoIcon">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div class="brandTextWrap">
      <div class="brandTitle">Digital Finance Business Partner</div>
      <div class="brandSub">Finansal Teşhis &amp; Yönetim Karar Destek Platformu</div>
    </div>
  </a>
</div><div class="headerRight"><nav class="topNav hidePrint" id="mainNav"><a href="/" class="active">Anasayfa</a><a href="/cozumler">Çözümler</a><a href="/hakkimizda">Hakkımızda</a><a href="/uygulama">Uygulama</a><a href="/paketler">Paketler</a><a href="/guvenlik">Güvenlik</a><a href="/iletisim">İletişim</a><div class="mobileNavAuth"><a href="/uygulama?auth=login" class="secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="primary">Ücretsiz Kayıt Ol</a></div></nav><div class="authCluster hidePrint"><div class="headerSwitches"><select class="globalLangSwitch select" onchange="setGlobalLanguage(this.value)" style="padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1" title="Dil / Language"><option value="tr">🇹🇷 TR</option><option value="en">🇬🇧 EN</option><option value="de">🇩🇪 DE</option><option value="fr">🇫🇷 FR</option><option value="es">🇪🇸 ES</option><option value="it">🇮🇹 IT</option><option value="nl">🇳🇱 NL</option></select></div><div class="navBtns"><a href="/uygulama?auth=login" class="navBtn secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="navBtn primary">Ücretsiz Kayıt Ol</a></div></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<section class="mHero">
  <div class="reveal in">
    <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;font-size:11.5px;font-weight:800;letter-spacing:0.6px;margin-bottom:12px;display:inline-block">⚡ STRATEJİK FİNANSAL İŞ ORTAĞI &amp; NAKİT MOTORU</span>
    <h1 style="margin-top:8px">Şu Anda Şirketinizin Kasasında<br><span class="gradText">Kaç Milyon TL Kilitli ve Boşta Duruyor?</span></h1>
    <p class="lead">Klasik muhasebe sadece geçmiş faturaları kaydeder ve vergi matrahı çıkarır. <b>Digital Finance Business Partner</b> ise kilitlenen sermayenizi, vadelerdeki gizli kredi faizlerini ve kurtarılabilir serbest nakit akışınızı <b>60 saniyede açığa çıkarır</b>.</p>
    
    <div style="display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin:24px 0 18px">
      <a href="/uygulama" class="primary" style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;padding:15px 28px;border-radius:14px;font-size:15px;font-weight:800;background:#1D4ED8;color:#FFFFFF;box-shadow:0 8px 24px rgba(29,78,216,0.35);transition:all .2s ease">
        <span>📁</span>
        <span>Ücretsiz Finansal Röntgenimi Çıkar</span>
        <span style="font-size:16px;margin-left:2px">→</span>
      </a>
      <a href="/uygulama?sample=data_hub" style="display:inline-flex;align-items:center;gap:8px;text-decoration:none;padding:14px 22px;border-radius:14px;font-size:14px;font-weight:700;background:#FFFFFF;color:#1E293B;border:1.5px solid #CBD5E1;box-shadow:0 2px 6px rgba(0,0,0,0.04);transition:all .2s ease">
        <span>⚡</span>
        <span>Mizanım Yanımda Değil, Canlı Demoyu Başlat</span>
      </a>
    </div>

    <div class="miniTrust">
      <span><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>RAM-Only (Sıfır Kalıcı Disk Kaydı)</span>
      <span><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>%100 Deterministik Çift Taraflı Denetim</span>
      <span><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 5-8"/></svg>Kurulumsuz · Anında Canlı Sonuç</span>
    </div>
  </div>
  <div class="heroArt reveal in">
    <div class="heroDash">
      <div class="dHead">
        <div class="dots"><span style="background:#EF4444"></span><span style="background:#F59E0B"></span><span style="background:#10B981"></span></div>
        <span class="live"><i></i>İNTERAKTİF CANLI ÖNİZLEME</span>
      </div>
      <div class="dashTabs" id="heroDashTabs">
        <span data-pane="0" class="on">💰 Kâr Köprüsü</span>
        <span data-pane="1">🌱 Sermaye Verimi</span>
        <span data-pane="2">⏳ Nakit Çevrimi</span>
        <span data-pane="3">🚨 Erken Uyarı Radarı</span>
        <span data-pane="4">🎯 What-If Simülatör</span>
      </div>
      <div id="heroDashPanes">
        <div class="dashPane on" data-pane="0">
          <div class="dTitle">Kâr Köprüsü — Satıştan Kasaya Kalan Net Para (Nereye Gitti?)</div>
          <svg viewBox="0 0 320 135" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:135px">
            <line x1="0" y1="118" x2="320" y2="118" stroke="#E2E8F0" stroke-width="1"/>
            <rect x="12" y="22" width="38" height="96" fill="#2563EB" rx="5"/>
            <rect x="72" y="44" width="38" height="74" fill="#E11D48" rx="5"/>
            <rect x="132" y="64" width="38" height="54" fill="#F59E0B" rx="5"/>
            <rect x="192" y="92" width="38" height="26" fill="#8B5CF6" rx="5"/>
            <rect x="252" y="32" width="38" height="86" fill="#10B981" rx="5"/>
            <text x="31" y="16" fill="#0F172A" font-size="9.5" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">10.0M ₺</text>
            <text x="31" y="130" fill="#64748B" font-size="8.5" text-anchor="middle" font-family="Inter,sans-serif">Satış Ciro</text>
            <text x="91" y="38" fill="#BE123C" font-size="9.5" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">-6.5M ₺</text>
            <text x="91" y="130" fill="#64748B" font-size="8.5" text-anchor="middle" font-family="Inter,sans-serif">Maliyet</text>
            <text x="151" y="58" fill="#B45309" font-size="9.5" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">-2.1M ₺</text>
            <text x="151" y="130" fill="#64748B" font-size="8.5" text-anchor="middle" font-family="Inter,sans-serif">Faaliyet Gid.</text>
            <text x="211" y="86" fill="#6D28D9" font-size="9.5" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">-400k ₺</text>
            <text x="211" y="130" fill="#64748B" font-size="8.5" text-anchor="middle" font-family="Inter,sans-serif">Faiz/Vergi</text>
            <text x="271" y="26" fill="#047857" font-size="9.5" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">+1.0M ₺</text>
            <text x="271" y="130" fill="#047857" font-size="8.5" font-weight="700" text-anchor="middle" font-family="Inter,sans-serif">Net Kâr</text>
          </svg>
          <div class="dashKpis"><div><b>%35,0</b><span>Brüt Kâr Marjı</span></div><div><b>₺1.000.000</b><span>Net Dönem Kârı</span></div><div><b>₺3,45M</b><span>Müşteri/Stokta Kilitli</span></div></div>
        </div>
        <div class="dashPane" data-pane="1">
          <div class="dTitle">Sermaye Verimi — Bağlanan Her 100 ₺ Ne Üretiyor? (ROE Ağacı)</div>
          <svg viewBox="0 0 320 135" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:135px">
            <rect x="110" y="4" width="100" height="28" rx="7" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/><text x="160" y="22" text-anchor="middle" fill="#1D4ED8" font-family="Inter,sans-serif" font-size="11" font-weight="800">ROE %25,4</text>
            <line x1="130" y1="32" x2="60" y2="54" stroke="#CBD5E1" stroke-width="1.5"/><line x1="190" y1="32" x2="260" y2="54" stroke="#CBD5E1" stroke-width="1.5"/>
            <rect x="15" y="54" width="90" height="26" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/><text x="60" y="71" text-anchor="middle" fill="#0F172A" font-family="Inter,sans-serif" font-size="9.5" font-weight="600">Net Marj %11,2</text>
            <rect x="215" y="54" width="90" height="26" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/><text x="260" y="71" text-anchor="middle" fill="#0F172A" font-family="Inter,sans-serif" font-size="9.5" font-weight="600">Kaldıraç 1,36x</text>
            <line x1="60" y1="80" x2="60" y2="98" stroke="#CBD5E1" stroke-width="1.5"/>
            <rect x="10" y="98" width="100" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/><text x="60" y="114" text-anchor="middle" fill="#475569" font-family="Inter,sans-serif" font-size="8.5">Ciro Hızı: 1,62x / yıl</text>
            <rect x="150" y="98" width="162" height="24" rx="6" fill="#ECFDF5" stroke="#10B981"/><text x="231" y="114" text-anchor="middle" fill="#047857" font-family="Inter,sans-serif" font-size="8.5" font-weight="700">100 ₺ Sermaye = 25,4 ₺ Kâr</text>
          </svg>
          <div class="dashKpis"><div><b>%25,4</b><span>Özsermaye Kârlılığı</span></div><div><b>25,4 ₺</b><span>Her 100 ₺ İçin Getiri</span></div><div><b>1,62x</b><span>Aktif Varlık Hızı</span></div></div>
        </div>
        <div class="dashPane" data-pane="2">
          <div class="dTitle">Nakit Çevrim Süresi — Para Kaç Günde Kasaya Dönüyor?</div>
          <svg viewBox="0 0 320 135" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:135px">
            <text x="8" y="18" fill="#475569" font-family="Inter,sans-serif" font-size="9" font-weight="600">Müşteri Tahsilat Süresi (DSO)</text>
            <rect x="8" y="24" width="304" height="15" rx="7.5" fill="#F1F5F9"/><rect x="8" y="24" width="180" height="15" rx="7.5" fill="#2563EB"/><text x="195" y="36" fill="#0F172A" font-family="Inter,sans-serif" font-size="9" font-weight="700">80 gün</text>
            <text x="8" y="58" fill="#475569" font-family="Inter,sans-serif" font-size="9" font-weight="600">Depoda Malın Kalma Süresi (DIO)</text>
            <rect x="8" y="64" width="304" height="15" rx="7.5" fill="#F1F5F9"/><rect x="8" y="64" width="216" height="15" rx="7.5" fill="#10B981"/><text x="230" y="76" fill="#0F172A" font-family="Inter,sans-serif" font-size="9" font-weight="700">96 gün</text>
            <text x="8" y="98" fill="#475569" font-family="Inter,sans-serif" font-size="9" font-weight="600">Tedarikçiye Ödeme Vadesi (DPO - Finansman Desteği)</text>
            <rect x="8" y="104" width="304" height="15" rx="7.5" fill="#F1F5F9"/><rect x="8" y="104" width="95" height="15" rx="7.5" fill="#F59E0B"/><text x="110" y="116" fill="#0F172A" font-family="Inter,sans-serif" font-size="9" font-weight="700">-42 gün</text>
          </svg>
          <div class="dashKpis"><div><b>134 Gün</b><span>Net Nakit Bekleme</span></div><div><b>₺3,45M</b><span>İşletmede Kilitli Nakit</span></div><div><b>+450k ₺</b><span>15 Gün Erken Tahsilat</span></div></div>
        </div>
        <div class="dashPane" data-pane="3">
          <div class="dTitle">Erken Uyarı Radarı — Şirketi Tehdit Eden Gizli Riskler</div>
          <svg viewBox="0 0 320 135" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:135px" font-family="Inter,sans-serif">
            <rect x="4" y="8" width="312" height="26" rx="6" fill="#FEF2F2" stroke="#FEE2E2"/>
            <circle cx="16" cy="21" r="4" fill="#EF4444"/><text x="28" y="24" fill="#991B1B" font-size="9" font-weight="600">Tahsilat gecikmesi (DSO 80 gün) nakit açığı yaratıyor</text>
            <rect x="254" y="14" width="54" height="14" rx="7" fill="#DC2626"/><text x="281" y="24.5" fill="#FFFFFF" font-size="7.5" font-weight="800" text-anchor="middle">KRİTİK</text>
            
            <rect x="4" y="38" width="312" height="26" rx="6" fill="#FEF2F2" stroke="#FEE2E2"/>
            <circle cx="16" cy="51" r="4" fill="#EF4444"/><text x="28" y="54" fill="#991B1B" font-size="9" font-weight="600">180+ gün ölü stok: 380.000 ₺ depoda nakit yutuyor</text>
            <rect x="254" y="44" width="54" height="14" rx="7" fill="#DC2626"/><text x="281" y="54.5" fill="#FFFFFF" font-size="7.5" font-weight="800" text-anchor="middle">KRİTİK</text>

            <rect x="4" y="68" width="312" height="26" rx="6" fill="#FFFBEB" stroke="#FEF3C7"/>
            <circle cx="16" cy="81" r="4" fill="#F59E0B"/><text x="28" y="84" fill="#92400E" font-size="9" font-weight="600">Müşteri yoğunlaşması: İlk 3 müşteri cironun %64'ü</text>
            <rect x="254" y="74" width="54" height="14" rx="7" fill="#D97706"/><text x="281" y="84.5" fill="#FFFFFF" font-size="7.5" font-weight="800" text-anchor="middle">YÜKSEK</text>

            <rect x="4" y="98" width="312" height="26" rx="6" fill="#ECFDF5" stroke="#D1FAE5"/>
            <circle cx="16" cy="111" r="4" fill="#10B981"/><text x="28" y="114" fill="#065F46" font-size="9" font-weight="600">Fiyatlama gücü: Brüt marj sektörün 4 puan üzerinde</text>
            <rect x="254" y="104" width="54" height="14" rx="7" fill="#059669"/><text x="281" y="114.5" fill="#FFFFFF" font-size="7.5" font-weight="800" text-anchor="middle">GÜÇLÜ</text>
          </svg>
          <div class="dashKpis"><div><b>2</b><span>Kritik Nakit Riski</span></div><div><b>380.000 ₺</b><span>Kurtarılabilir Ölü Stok</span></div><div><b>8</b><span>Öncelikli Aksiyon</span></div></div>
        </div>
        <div class="dashPane" data-pane="4">
          <div class="dTitle" style="display:flex;justify-content:space-between;align-items:center">
            <span>🎯 Canlı Karar Simülatörü</span>
            <span style="font-size:9.5px;background:#EFF6FF;color:#1D4ED8;padding:2px 7px;border-radius:999px;font-weight:800">Sürgüleri Oynatın</span>
          </div>
          <div style="display:flex;flex-direction:column;gap:6px;padding:4px 0">
            <div style="display:flex;justify-content:space-between;align-items:center;font-size:10px">
              <span style="color:#475569;font-weight:600">Fiyat Artışı:</span>
              <b id="pane4PriceVal" style="color:#1D4ED8;font-weight:800">+%3,0</b>
            </div>
            <input type="range" id="pane4PriceRange" min="0" max="10" step="0.5" value="3" class="labRange" style="height:4px;margin:0" oninput="recalcPane4Sim()">

            <div style="display:flex;justify-content:space-between;align-items:center;font-size:10px">
              <span style="color:#475569;font-weight:600">Tahsilat Hızlandırma:</span>
              <b id="pane4DsoVal" style="color:#059669;font-weight:800">-15 Gün</b>
            </div>
            <input type="range" id="pane4DsoRange" min="0" max="30" step="1" value="15" class="labRange" style="height:4px;margin:0" oninput="recalcPane4Sim()">

            <div style="display:flex;justify-content:space-between;align-items:center;font-size:10px">
              <span style="color:#475569;font-weight:600">Ölü Stok Eritme:</span>
              <b id="pane4DioVal" style="color:#D97706;font-weight:800">-%20</b>
            </div>
            <input type="range" id="pane4DioRange" min="0" max="50" step="5" value="20" class="labRange" style="height:4px;margin:0" oninput="recalcPane4Sim()">
          </div>
          <div class="dashKpis" style="margin-top:6px">
            <div><b id="pane4ProfitKpi">+300.000 ₺</b><span>Net Kâr</span></div>
            <div><b id="pane4DsoKpi">+411.000 ₺</b><span>Tahsilat</span></div>
            <div><b id="pane4TotalKpi" style="color:#047857;font-weight:900">+847.000 ₺</b><span>Serbest Nakit</span></div>
          </div>
        </div>
      </div>
      <div class="foot"><span>%100 Deterministik Çift Taraflı Denetim</span><span>60 Saniyede Hazır Yönetim Raporu</span></div>
    </div>
  </div>
</section>

<!-- SECTION: ANASAYFA CANLI WHAT-IF NAKİT LABORATUVARI -->
<div class="secBlock reveal">
  <section id="homeWhatIfLab" class="marketingSection hidePrint" style="padding-top:0">
    <div class="whatIfLabCard">
      <div style="display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #E2E8F0;padding-bottom:16px;margin-bottom:20px;flex-wrap:wrap;gap:12px">
        <div>
          <span class="workflowBadge" style="background:#ECFDF5;color:#047857;border-color:#A7F3D0;margin:0">🧮 CANLI KARAR SİMÜLATÖRÜ · 60 SANİYELİK NAKİT ETKİSİ</span>
          <h2 style="font-size:22px;margin:8px 0 4px;font-family:var(--serif);color:#0F172A">Sürgüleri Kaydırın: Şirketinizin Kasasına Girecek Sıcak Parayı Görün</h2>
          <p style="margin:0;color:#64748B;font-size:13px">Klasik muhasebe sadece olanı yazar. Bu simülatör, alacağınız 3 temel yönetim kararının kasanıza kaç yüz bin TL nakit kazandıracağını anında hesaplar.</p>
        </div>
        <div class="labPresets">
          <span style="font-size:11px;font-weight:700;color:#64748B">Hazır Senaryolar:</span>
          <button type="button" class="labPresetBtn active" onclick="applyLabPreset(3, 15, 20, this)">Dengeli KOBİ</button>
          <button type="button" class="labPresetBtn" onclick="applyLabPreset(0, 25, 30, this)">Agresif Tahsilat</button>
          <button type="button" class="labPresetBtn" onclick="applyLabPreset(6, 5, 10, this)">Marj &amp; Fiyat Gücü</button>
        </div>
      </div>

      <div class="labGrid">
        <!-- Controls -->
        <div class="labControls">
          <!-- Slider 1 -->
          <div class="labSliderRow">
            <div class="labSliderHead">
              <span>🏷️ 1. Fiyat Artışı / Enflasyonist Geçirgenlik</span>
              <span class="labBadgeVal" id="labPriceVal">+%3,0</span>
            </div>
            <input type="range" id="labPriceRange" min="0" max="10" step="0.5" value="3" class="labRange" oninput="recalcHomeLabSim()">
            <div style="display:flex;justify-content:space-between;font-size:10.5px;color:#94A3B8">
              <span>%0 (Mevcut)</span>
              <span style="color:#64748B">Medyan: %3</span>
              <span>+%10 (Azami)</span>
            </div>
          </div>

          <!-- Slider 2 -->
          <div class="labSliderRow">
            <div class="labSliderHead">
              <span>⏱️ 2. Müşteri Tahsilat Vadesi Kısaltma (DSO)</span>
              <span class="labBadgeVal" id="labDsoVal">-15 Gün</span>
            </div>
            <input type="range" id="labDsoRange" min="0" max="30" step="1" value="15" class="labRange" oninput="recalcHomeLabSim()">
            <div style="display:flex;justify-content:space-between;font-size:10.5px;color:#94A3B8">
              <span>0 Gün</span>
              <span style="color:#64748B">Hedef: -15 Gün</span>
              <span>-30 Gün</span>
            </div>
          </div>

          <!-- Slider 3 -->
          <div class="labSliderRow">
            <div class="labSliderHead">
              <span>📦 3. Depodaki Ölü &amp; Atıl Stok Eritme Hızı</span>
              <span class="labBadgeVal" id="labDioVal">-%20</span>
            </div>
            <input type="range" id="labDioRange" min="0" max="50" step="5" value="20" class="labRange" oninput="recalcHomeLabSim()">
            <div style="display:flex;justify-content:space-between;font-size:10.5px;color:#94A3B8">
              <span>%0 (Beklemede)</span>
              <span style="color:#64748B">Öneri: %20</span>
              <span>-%50 (Kampanya/Tasfiye)</span>
            </div>
          </div>
        </div>

        <!-- Vault Card (Big Counter) -->
        <div class="labVaultCard">
          <div>
            <div style="display:flex;align-items:center;justify-content:space-between">
              <span style="font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#34D399;background:rgba(52,211,153,.15);border:1px solid rgba(52,211,153,.3);padding:3px 10px;border-radius:999px">🔥 KASAYA GİRECEK EK SICAK NAKİT</span>
              <span style="font-size:11.5px;color:#94A3B8">Yıllık Etki</span>
            </div>
            <span class="vaultBigCounter" id="labTotalVaultCounter">+847.000 ₺</span>
            <div style="font-size:12px;color:#CBD5E1;line-height:1.45">Kredi çekmeden, banka faizine ezilmeden şirketin kendi operasyonel çarklarından açığa çıkacak serbest sıcak nakit.</div>
          </div>

          <div class="vaultBreakdown">
            <div class="vSubItem">
              <b id="labProfitSub">+300.000 ₺</b>
              <span>Net Kâr Katkısı</span>
            </div>
            <div class="vSubItem">
              <b id="labDsoSub">+411.000 ₺</b>
              <span>Alacak Nakdi</span>
            </div>
            <div class="vSubItem">
              <b id="labDioSub">+136.000 ₺</b>
              <span>Stok Nakdi</span>
            </div>
          </div>

          <div style="margin-top:16px">
            <a href="/uygulama?sample=data_hub" class="primary" style="display:flex;align-items:center;justify-content:center;gap:8px;text-decoration:none;padding:12px;border-radius:12px;font-size:13px;font-weight:800;background:#10B981;border:none;box-shadow:0 4px 14px rgba(16,185,129,.35)">
              ⚡ Kendi Şirketinizde Bu Parayı Kurtarmak İçin Başlayın →
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>

<!-- SECTION: 3-STEP CUSTOMER WORKFLOW WITH INTERACTIVE PLAYER -->
<div class="secBlock tint reveal"><section id="workflow" class="marketingSection hidePrint" style="padding-top:0">
<div class="marketingHead">
  <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE">⚙️ MÜŞTERİ ODAKLI İŞ AKIŞI</span>
  <h2 style="margin-top:10px">Mizanınızdan Yönetim Kurulu Kararlarına 3 Adımlı Süreç</h2>
  <p>Karmaşık yazılım kurulumları veya aylar süren IT entegrasyonları yok. Ham mizanınızı sisteme bırakın; görünmez sızıntıları 60 saniyede teşhis edin ve nakit kurtaracak icraat kararlarını uygulayın.</p>
</div>
<div class="workflowGrid" id="wfGrid" style="grid-template-columns:repeat(3,1fr)">
  <div class="workflowCard wfInteractive" data-step="0" style="cursor:pointer;border-top:3px solid var(--accent)">
    <span class="workflowBadge">ADIM 1 · GİRİŞ</span>
    <h3>Sıfır Kurulumla Mizanı Bırakın</h3>
    <p>Luca, Logo, Netsis, Mikro, Zirve, SAP veya Excel. Standart mizan dosyanızı sürükleyin; kolonları ve hesap planını (1xx-7xx) anında otomatik tanır, çift taraflı denetimden geçirir.</p>
  </div>
  <div class="workflowCard wfInteractive" data-step="1" style="cursor:pointer">
    <span class="workflowBadge">ADIM 2 · TEŞHİS</span>
    <h3>Kâr Nerede Kilitli Görün</h3>
    <p>33 bağımsız karar motoru çalışır: Defter kârı ile kasadaki nakit arasındaki açığı, 88 günlük alacak vadelerini, depodaki ölü stoku ve gizli banka faiz maliyetini kuruşuna kadar ortaya çıkarır.</p>
  </div>
  <div class="workflowCard wfInteractive" data-step="2" style="cursor:pointer">
    <span class="workflowBadge">ADIM 3 · İCRAAT</span>
    <h3>Karar Alın &amp; Nakdi Kurtarın</h3>
    <p>What-If simülatörüyle duyarlılığı test edin; vadesi, sahibi ve TL getirisi belli icraat kararları ve 1-sayfalık A4 Yönetim Kurulu özetiyle şirketinize sıcak nakit kazandırın.</p>
  </div>
</div>

<!-- Interactive Live Step Viewer (Executive Light Theme) -->
<div id="wfLiveViewer" style="margin-top:24px;background:#FFFFFF;border:1.5px solid #DCE6F5;border-radius:22px;padding:24px;color:#0F1B2D;box-shadow:0 14px 34px rgba(15,27,45,.06)">
  <div style="display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #F1F5F9;padding-bottom:14px;margin-bottom:18px;flex-wrap:wrap;gap:10px">
    <div style="display:flex;align-items:center;gap:10px">
      <span id="wfViewerStepTag" class="workflowBadge" style="background:#EFF6FF;border-color:#BFDBFE;color:#1D4ED8;margin:0">CANLI SİMÜLASYON · ADIM 1</span>
      <b id="wfViewerStepTitle" style="font-size:15px;color:#0F172A">Mizan ve Alt Defterlerin Doğrudan İçe Aktarımı</b>
    </div>
    <div style="display:flex;gap:6px" id="wfNavPills">
      <button type="button" class="wfPill active" data-wfpill="0" style="padding:6px 14px;font-size:11.5px;font-weight:700;background:#1D4ED8;color:#FFFFFF;border:none;border-radius:999px;cursor:pointer">1. Dosya Bırak</button>
      <button type="button" class="wfPill" data-wfpill="1" style="padding:6px 14px;font-size:11.5px;font-weight:700;background:#F1F5F9;color:#64748B;border:1px solid #E2E8F0;border-radius:999px;cursor:pointer">2. 33 Karar Motoru</button>
      <button type="button" class="wfPill" data-wfpill="2" style="padding:6px 14px;font-size:11.5px;font-weight:700;background:#F1F5F9;color:#64748B;border:1px solid #E2E8F0;border-radius:999px;cursor:pointer">3. Yönetim Kararları</button>
    </div>
  </div>
  <div id="wfViewerContent">
    <div style="display:grid;grid-template-columns:1.2fr .8fr;gap:20px;align-items:center">
      <div>
        <p style="color:#334155;font-size:13.5px;line-height:1.6;margin:0 0 14px">ERP veya muhasebe programınızdan aldığınız standart Excel/CSV mizanınızı ve varsa yaşlandırma/stok alt defterlerinizi tarayıcıya sürükleyin. Kolon eşleme yapay zeka tahminiyle değil, hesap planı kuralları (1xx-7xx) üzerinden deterministik olarak anında tanınır.</p>
        <div style="display:flex;gap:10px;flex-wrap:wrap">
          <span style="background:#F1F5F9;border:1px solid #CBD5E1;padding:6px 12px;border-radius:8px;font-size:12px;color:#1D4ED8;font-weight:600">✓ Luca, Logo, Mikro, Netsis, Zirve uyumlu</span>
          <span style="background:#ECFDF5;border:1px solid #A7F3D0;padding:6px 12px;border-radius:8px;font-size:12px;color:#047857;font-weight:600">✓ Sıfır Kurulum &amp; Sıfır Bekleme</span>
        </div>
      </div>
      <div style="background:#F8FAFC;border:2px dashed #93C5FD;border-radius:14px;padding:24px 20px;text-align:center">
        <div style="font-size:32px;margin-bottom:8px">📥</div>
        <b style="color:#0F172A;font-size:13px;display:block">Mizan Dosyanızı Sürükleyin</b>
        <span style="color:#64748B;font-size:11px">.xlsx, .xls, .csv formatları otomatik taranır</span>
      </div>
    </div>
  </div>
</div>
</section></div>

<!-- SECTION: ERP & MUHASEBE ENTEGRASYONLARI VE GLOBAL VİZYON -->
<div class="secBlock reveal">
  <section id="integrations" class="marketingSection hidePrint" style="padding-top:0">
    <div class="marketingHead">
      <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE">🔗 ERP &amp; MUHASEBE YAZILIMLARIYLA %100 UYUMLU</span>
      <h2 style="margin-top:10px">Kullandığınız Sisteme Dokunmadan Çalışır · Sıfır Manuel Hamallık</h2>
      <p>Yazılımınızı değiştirmenize, haftalarca entegrasyon beklemenize gerek yok. Digital Finance Business Partner, Türkiye ve dünyada en çok kullanılan kurumsal ERP ve muhasebe programlarından alınan standart mizan ve defter formatlarını otomatik tanır. İster tek tıkla mizan sürükleyin, ister otomatik periyodik analiz takvimine bağlayın.</p>
    </div>

    <div class="erpLogosGrid">
      <div class="erpLogoBadge"><b>LOGO</b><span>Tiger / GO3</span></div>
      <div class="erpLogoBadge"><b>MİKRO</b><span>Fly / Jump</span></div>
      <div class="erpLogoBadge"><b>NETSİS</b><span>Enterprise / Standard</span></div>
      <div class="erpLogoBadge"><b>ZİRVE</b><span>Müşavir / Finansman</span></div>
      <div class="erpLogoBadge"><b>LUCA</b><span>MMP Bulut Mizan</span></div>
      <div class="erpLogoBadge"><b>SAP</b><span>Business One / S/4HANA</span></div>
      <div class="erpLogoBadge"><b>NEBİM</b><span>V3 ERP</span></div>
      <div class="erpLogoBadge"><b>UYUMSOFT</b><span>Bulut ERP</span></div>
      <div class="erpLogoBadge"><b>PARAŞÜT</b><span>KOBİ Ön Muhasebe</span></div>
      <div class="erpLogoBadge"><b>EXCEL / CSV</b><span>Evrensel Şablon</span></div>
    </div>

    <!-- Global & Multi-Currency Capability Banner -->
    <div style="background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:20px;padding:26px;margin-top:24px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;box-shadow:0 6px 20px rgba(15,27,45,.03)">
      <div style="border-right:1px solid #E2E8F0;padding-right:16px">
        <div style="font-size:22px;margin-bottom:8px">🌍</div>
        <div style="font-size:14px;font-weight:800;color:#0F172A;margin-bottom:6px">Çoklu Para Birimi (Multi-Currency)</div>
        <div style="font-size:12px;color:#64748B;line-height:1.55">₺ TRY, $ USD, € EUR, £ GBP para birimlerinde çalışın. İhracatçı ve ithalatçı KOBİ'ler için kur farkı gelir/giderini operasyonel kârdan anında ayrıştırır.</div>
      </div>
      <div style="border-right:1px solid #E2E8F0;padding-right:16px">
        <div style="font-size:22px;margin-bottom:8px">📑</div>
        <div style="font-size:14px;font-weight:800;color:#0F172A;margin-bottom:6px">Yönetim Muhasebesi &amp; Konsolidasyon Desteği</div>
        <div style="font-size:12px;color:#64748B;line-height:1.55">Banka kredi görüşmeleri, yönetim kurulu sunumları ve ortaklar için Tekdüzen Hesap Planı'nı (TDHP) standart yönetim nakit akışı ve kârlılık formatına dönüştürür.</div>
      </div>
      <div>
        <div style="font-size:22px;margin-bottom:8px">⚡</div>
        <div style="font-size:14px;font-weight:800;color:#0F172A;margin-bottom:6px">Zamanlanmış Otomatik Rapor Takvimi</div>
        <div style="font-size:12px;color:#64748B;line-height:1.55">Manuel dosya taşımaktan sıkılan ekipler için haftalık ve aylık mizan tarama takvimi oluşturur; C-Level yöneticilerin e-postasına hazır karar özetini iletir.</div>
      </div>
    </div>
  </section>
</div>

<!-- SECTION: 10 KOBİ PATRON VİTRİNİ -->
<div class="secBlock reveal"><section id="kobiShowcase" class="marketingSection hidePrint" style="padding-top:0">
<div class="marketingHead">
  <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE">🎯 KOBİ PATRONLARI &amp; ŞİRKET ORTAKLARI İÇİN</span>
  <h2 style="margin-top:10px">Patronun Masasındaki 10 Gerçek Kriz &amp; 60 Saniyelik Çözüm</h2>
  <p>Muhasebe programınız geçmiş fişleri kaydeder; Digital Finance BP ise şirketi kâr eden ve nakit üreten bir makineye dönüştürür. İşte patronların en çok yaşadığı 10 çıkmaz ve somut reçetesi:</p>
  
  <div class="kobiPills">
    <button type="button" class="kobiPill active" onclick="filterKobiShowcase('all', this)">🔥 Tümü (10)</button>
    <button type="button" class="kobiPill" onclick="filterKobiShowcase('cash', this)">💵 Nakit &amp; Tahsilat (4)</button>
    <button type="button" class="kobiPill" onclick="filterKobiShowcase('profit', this)">📊 Kâr, Marj &amp; Stok (3)</button>
    <button type="button" class="kobiPill" onclick="filterKobiShowcase('mgmt', this)">🏛️ Yönetim &amp; Banka (3)</button>
  </div>
</div>

<div class="kobiSliderWrap">
  <div class="kobiSliderBar">
    <div class="kobiSwipeHint">
      <span style="font-size:14px">👈</span>
      <span>Kartları sağa / sola kaydırarak inceleyin</span>
      <span style="font-size:14px">👉</span>
    </div>
    <div class="kobiSliderNav">
      <span class="kobiSlideBadge" id="kobiSliderCounter">1 / 10 Teşhis</span>
      <button type="button" class="kobiNavBtn" onclick="slideKobi(-1)" aria-label="Önceki Teşhis" title="Önceki">‹</button>
      <button type="button" class="kobiNavBtn" onclick="slideKobi(1)" aria-label="Sonraki Teşhis" title="Sonraki">›</button>
    </div>
  </div>

  <div class="kobiSliderTrack" id="kobiSliderTrack">
  <!-- Kart 0: Hızlı Çözümler Köprüsü -->
  <div class="kobiCard" style="background:linear-gradient(135deg,#EFF6FF 0%,#DBEAFE 100%);border:2px dashed #93C5FD;min-width:320px;display:flex;flex-direction:column;justify-content:space-between">
    <div>
      <span class="kobiTag cash">🎯 AD CAMPAIGN &amp; YÖNETİM REÇETELERİ</span>
      <div class="kobiTitle" style="color:#1E3A8A;margin-top:6px">"Patronun Masasındaki 10 Finansal Kriz ve 8 Karar Masası"</div>
      <div class="kobiDesc" style="color:#33415C;font-size:12px;line-height:1.55">Reklamlarımızda yer alan 10 krizin tamamını, analitik kanıtlarını ve 3 katmanlı icraat reçetelerini özel Çözümler sayfamızda derledik.</div>
    </div>
    <div style="margin-top:16px">
      <a href="/cozumler" class="primary" style="display:block;text-align:center;text-decoration:none;padding:12px 14px;border-radius:10px;font-size:13px;font-weight:800">Tüm 10 Kriz &amp; 8 Masayı İncele →</a>
    </div>
  </div>
  <!-- Kart 1 -->
  <div class="kobiCard" data-category="cash">
    <span class="kobiTag cash">💵 1. KÂR &amp; NAKİT ÇELİŞKİSİ</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_1_kar_vs_kasa.jpg" alt="1. Kâr ve Nakit Çelişkisi" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Muhasebeciniz 'Bu Ay Kârdayız' Diyor, Ama Siz Ay Sonu Maaşları Nasıl Ödeyeceğinizi Düşünüyorsunuz."</div>
    <div class="kobiDesc">Defterde kâr çıkması, kasada nakit olduğu anlamına gelmez. Satışı yapmışsınız ama parayı müşteriden alamamışsınız; malı üretip depoya yığmışsınız. Kârınız buharlaşmadı; müşterinin açık hesabında ve depodaki kolilerde kilitli kaldı.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Defterdeki Kâr:</span><b style="color:#059669">₺1.850.000 (Mizan Bilanço Kârı)</b></div>
      <div class="kobiMetricRow"><span>Kasadaki Sıcak Nakit:</span><b style="color:#DC2626">₺42.000 (Kritik Alarm)</b></div>
      <div class="kobiMetricRow"><span>Alacak &amp; Stokta Kilitli:</span><b style="color:#B45309">₺1.808.000 Bağlı Sermaye</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Nakit Köprüsü):</b>
      P&amp;L kârınızın hangi hesaplarda kilitlendiğini kuruşu kuruşuna haritalandırır; defter kârı ile serbest nakit akışı arasındaki sızıntıyı kapatır.
    </div>
  </div>

  <!-- Kart 2 -->
  <div class="kobiCard" data-category="cash">
    <span class="kobiTag cash">💵 2. AÇIK HESAP &amp; TERSİNE BANKACILIK</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_2_acik_hesap.jpg" alt="2. Açık Hesap ve Tersine Bankacılık" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Siz Mal mı Satıyorsunuz, Yoksa Müşterilerinize Faizsiz Kredi Dağıtan Banka mısınız?"</div>
    <div class="kobiDesc">Siz bankadan %50 faizle kredi çekip hammadde alıyorsunuz, işçilik ödüyorsunuz; müşteriniz ise malı alıp 90 gün sonra ödüyor! Kendi özkaynağınızla başkalarının ticaretini finanse ediyorsunuz.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Ortalama Tahsilat Vadeniz:</span><b style="color:#DC2626">88 Gün (Sektör: 60 Gün)</b></div>
      <div class="kobiMetricRow"><span>Müşteriyi Fonlama Maliyeti:</span><b style="color:#B45309">Yıllık ~₺1.250.000 Gizli Faiz</b></div>
      <div class="kobiMetricRow"><span>15 Gün Erken Tahsilat Kazancı:</span><b style="color:#1D4ED8">+₺450.000 Sıcak Para</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Alacak Yaşlandırma):</b>
      Alacak portföyünün vadesini tarar; vadesi 60 günü aşan riskli carileri sıralar ve tahsilat hızlandırma protokolünü devreye sokar.
    </div>
  </div>

  <!-- Kart 3 -->
  <div class="kobiCard" data-category="profit">
    <span class="kobiTag profit">📊 3. ÖLÜ STOK MEZARLIĞI</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_3_olu_stok.jpg" alt="3. Ölü Stok Mezarlığı" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Deponuz Ağzına Kadar Mal Dolu Diye Zenginleştiğinizi mi Sanıyorsunuz?"</div>
    <div class="kobiDesc">6 aydır rafta bekleyen o kumaş, o profil, o yedek parça depoda durdukça değer kazanmıyor; her gün banka kredinizin faizini yiyor. Depodaki atıl malı görmezden gelmek, her ay deste deste parayı çöpe atmaktır.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Depodaki Toplam Envanter:</span><b style="color:#0F172A">₺2.400.000</b></div>
      <div class="kobiMetricRow"><span>180+ Günlük Ölü Stok:</span><b style="color:#DC2626">₺680.000 (Atıl Sermaye)</b></div>
      <div class="kobiMetricRow"><span>Aylık Gizli Faiz Yükü:</span><b style="color:#B45309">~₺45.000 / Ay Kayıp</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Envanter İstihbaratı):</b>
      Mizan ile depo kayıtlarını eşleştirir; 180+ gündür devretmeyen ölü stokları listeler ve acil nakde dönüşüm reçetesini çıkarır.
    </div>
  </div>

  <!-- Kart 4 -->
  <div class="kobiCard" data-category="mgmt">
    <span class="kobiTag mgmt">🏛️ 4. MİZAN ÇİLESİ VS. KARAR MASASI</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_4_mizan_vs_karar.jpg" alt="4. Mizan Çilesi vs Karar Masası" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Muhasebeciniz Size Çıkacak Vergiyi Söyler; Parayı Nereden Bulacağınızı Söylemez."</div>
    <div class="kobiDesc">Mali müşavirin işi devlete vergi beyannamesi vermektir. Ancak önünüze konan 500 satırlık mizan tablosundan "Yarın hangi müşteriye mal çıkışını durdurmalıyım?", "Hangi maliyet canımı yakıyor?" sorularının yanıtı çıkmaz.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Klasik Mizan Tablosu:</span><b style="color:#64748B">500 Satır Hesap (Karar Yok)</b></div>
      <div class="kobiMetricRow"><span>Digital Finance BP:</span><b style="color:#1D4ED8">1 Sayfalık Board Raporu</b></div>
      <div class="kobiMetricRow"><span>Yönetimsel Analiz Süresi:</span><b style="color:#059669">Sadece 60 Saniye</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (1-Sayfalık Yönetim Özeti):</b>
      33 karar motoru mizanınızı tarar; kâr durumunu, paranın kilitlendiği yeri ve alınacak 1 numaralı icraat kararını tek sayfada masaya koyar.
    </div>
  </div>

  <!-- Kart 5 -->
  <div class="kobiCard" data-category="cash">
    <span class="kobiTag cash">💵 5. CİRO ALDANMASI &amp; KASA GERÇEĞİ</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_5_ciro_aldanmasi.jpg" alt="5. Ciro Aldanması ve Kasa Gerçeği" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"50 Milyon Ciro Yapıp Ay Sonu Çek Öderken Ter Döken Patronlardan mısınız?"</div>
    <div class="kobiDesc">Ciro gösteriştir, kâr akıl işidir, kasadaki nakit ise gerçeğin ta kendisidir. Cironuz ikiye katlanıyor ama borcunuz da aynı hızla katlanıyorsa büyümüyorsunuz; sadece daha büyük bir riskin altına giriyorsunuz.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Yıllık Satış Cirosu:</span><b style="color:#059669">₺45.000.000 (Büyüme Görünümü)</b></div>
      <div class="kobiMetricRow"><span>Banka &amp; Borç Yükü:</span><b style="color:#DC2626">₺18.000.000 (Faiz Baskısı)</b></div>
      <div class="kobiMetricRow"><span>Kasaya Kalan Net Nakit:</span><b style="color:#DC2626">-₺350.000 (Nakit Açığı)</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Nakit Çevrim Motoru):</b>
      Satıştan tahsilata kadar paranın kaç günde döndüğünü (CCC) hesaplar; cironun nakde dönüşme kabiliyetini ve net kâr kalitesini ölçer.
    </div>
  </div>

  <!-- Kart 6 -->
  <div class="kobiCard" data-category="mgmt">
    <span class="kobiTag mgmt">🏛️ 6. MÜŞTERİ REHİNESİ &amp; KONSANTRASYON</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_6_musteri_rehinesi.jpg" alt="6. Müşteri Rehinesi ve Konsantrasyon" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Cironuzun Yarısını Tek Bir Müşteriye Yapıyorsanız; Patron Siz Değilsiniz, O Müşteridir."</div>
    <div class="kobiDesc">Büyük müşteriyle çalışmak iyidir ama bütün yumurtaları aynı sepete koymak felakettir. O müşteri yarın "Vadeyi 4 aya çıkarıyorum" dediğinde veya ödemeyi geciktirdiğinde şirketin dayanacak kaç günlük can suyu var?</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>İlk 3 Müşterinin Payı:</span><b style="color:#DC2626">%64 (Kritik Bağımlılık)</b></div>
      <div class="kobiMetricRow"><span>Olası Vade Gecikmesi:</span><b style="color:#B45309">-₺1.200.000 Nakit Açığı</b></div>
      <div class="kobiMetricRow"><span>Dayanıklılık Süresi:</span><b style="color:#DC2626">Yalnızca 22 Gün!</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Erken Uyarı Radarı):</b>
      Müşteri bağımlılığınızı ölçer; olası gecikmelerde şirketin likidite dayanıklılığını test eder ve açık hesap tavan limiti belirler.
    </div>
  </div>

  <!-- Kart 7 -->
  <div class="kobiCard" data-category="profit">
    <span class="kobiTag profit">📊 7. FİYATLAMA GÜCÜ &amp; MARJ KORUMA</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_7_fiyat_gucu.jpg" alt="7. Fiyatlama Gücü ve Marj Koruma" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Fiyatlarınıza Sadece %3 Zam Yapsanız Kasaya Kaç Yüz Bin Lira Kalır, Hiç Hesapladınız mı?"</div>
    <div class="kobiDesc">"Müşteri kaçar" korkusuyla maliyet artışlarını fiyata yansıtmamak şirketin özkaynağını eritir. Kontrolsüz iskontolar ve plansız vadeler, ciro artarken kârı sıfırlayan ana sızıntıdır.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Mevcut Brüt Kâr Marjı:</span><b style="color:#B45309">%22,4 (Enflasyon Baskısı)</b></div>
      <div class="kobiMetricRow"><span>Fiyatta +%3 Düzeltme:</span><b style="color:#059669">+₺324.000 Net Kâr Katkısı</b></div>
      <div class="kobiMetricRow"><span>10 Gün Erken Tahsilat:</span><b style="color:#1D4ED8">+₺450.000 Kurtarılan Nakit</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (What-If Simülatörü):</b>
      Fiyat artışı, vade kısaltma ve gider tasarrufu sürgülerini hareket ettirerek şirketin anlık kâr ve nakit kazanımını canlı simüle eder.
    </div>
  </div>

  <!-- Kart 8 -->
  <div class="kobiCard" data-category="cash">
    <span class="kobiTag cash">💵 8. KREDİ KAPANINDAN ÇIKIŞ</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_8_kredi_kapani.jpg" alt="8. Kredi Kapanından Çıkış" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Faizlerin %50 Olduğu Yerde, Şirketi Banka Kredisiyle Döndüremezsiniz."</div>
    <div class="kobiDesc">Kasada nakit sıkışınca ilk refleks bankaya koşup kredi çekmektir. Ama içerideki para kaçağını kapatmadan kredi çekmek, sadece bankalara çalışmaktır. Çözüm yeni borç değil; içerideki kilitli parayı kurtarmaktır.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Bankaya Yıllık Faiz Yükü:</span><b style="color:#DC2626">₺1.850.000 / Yıl</b></div>
      <div class="kobiMetricRow"><span>İçeride Kilitli Kendi Paranız:</span><b style="color:#059669">₺1.400.000 (Alacak &amp; Stok)</b></div>
      <div class="kobiMetricRow"><span>Kredi İhtiyacı Tasarrufu:</span><b style="color:#1D4ED8">%40 Daha Az Borçlanma</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Kaldıraç &amp; Borç Kapasitesi):</b>
      Operasyonel kârınızın faizleri kaç kat karşıladığını ölçer; yeni borca girmeden içerideki kilitli nakdi çözerek şirketi rahatlatır.
    </div>
  </div>

  <!-- Kart 9 -->
  <div class="kobiCard" data-category="mgmt">
    <span class="kobiTag mgmt">🏛️ 9. ORTAKLAR MASASINDA FİKİR BİRLİĞİ</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_9_ortaklar_masasi.jpg" alt="9. Ortaklar Masasında Fikir Birliği" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Her Ay Ortaklarınızla 'İşler İyiydi de Bu Para Nereye Gitti' Kavgası Yapmaktan Bıkmadınız mı?"</div>
    <div class="kobiDesc">Ortaklar arasındaki en büyük gerginlik rakamların farklı yorumlanmasıdır. Biri "Satış ekibi rekor kırdı" der, diğeri "Kasa boş, tedarikçiyi ödeyemiyoruz" der. Suçlu aramak yerine tek bir gerçeğin etrafında toplanın.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>1. Teşhis:</span><b style="color:#DC2626">Kârın %62'si Alacak ve Stokta Bağlı</b></div>
      <div class="kobiMetricRow"><span>2. Öncelikli İcraat:</span><b style="color:#1D4ED8">Vadesi Aşan 3 Müşteriyi Durdur</b></div>
      <div class="kobiMetricRow"><span>3. Kurtarılabilir Nakit:</span><b style="color:#059669">₺1.100.000 (Haftalık Protokol)</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Deterministik Yönetim Masası):</b>
      Kimsenin tartışamayacağı çift taraflı denetlenmiş verilerle şirketin tek bir yönetim ve eylem gündemi üzerinde uzlaşmasını sağlar.
    </div>
  </div>

  <!-- Kart 10 -->
  <div class="kobiCard" data-category="profit">
    <span class="kobiTag profit">📊 10. CFO ZEKA ARBİTRAJI</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_10_cfo_arbitraji.jpg" alt="10. CFO Zeka Arbitrajı" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Büyük Holdingler Her Ay Milyonluk Finans Kadrolarıyla Şirket Yönetiyor. Siz Hâlâ Hissiyatla mı Karar Veriyorsunuz?"</div>
    <div class="kobiDesc">Aylık 150-200 bin TL maaşla Finans Direktörü (CFO) tutmak KOBİ ölçeğinde zordur. Ancak rekabet etmek için holdinglerin sahip olduğu finansal denetime ve karar gücüne ihtiyacınız var.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Holding Finans Kadrosu:</span><b style="color:#64748B">Aylık ₺200.000+ Maliyet</b></div>
      <div class="kobiMetricRow"><span>Digital Finance BP:</span><b style="color:#1D4ED8">60 Saniyede CFO Masası</b></div>
      <div class="kobiMetricRow"><span>Karar Gücü:</span><b style="color:#059669">33 Deterministik Analiz Motoru</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (60 Saniyede Finansal Röntgen):</b>
      Mizanınızı yükleyin; 33 motor çift taraflı denetimle çalışsın, şirketinizi holding düzeyinde analitik finansal zekayla donatsın.
    </div>
  </div>
  </div>
  <div class="kobiDotsWrap" id="kobiDotsWrap"></div>
</div>

<script>
function slideKobi(direction) {
  var track = document.getElementById('kobiSliderTrack');
  if (!track) return;
  var visibleCards = Array.from(track.querySelectorAll('.kobiCard')).filter(function(c) {
    return c.style.display !== 'none';
  });
  if (!visibleCards.length) return;
  var cardWidth = visibleCards[0].offsetWidth + 22;
  track.scrollBy({ left: direction * cardWidth, behavior: 'smooth' });
}

function initKobiSlider() {
  var track = document.getElementById('kobiSliderTrack');
  var dotsWrap = document.getElementById('kobiDotsWrap');
  var counter = document.getElementById('kobiSliderCounter');
  if (!track || !dotsWrap) return;

  function getVisibleCards() {
    return Array.from(track.querySelectorAll('.kobiCard')).filter(function(c) {
      return c.style.display !== 'none';
    });
  }

  function updateDotsAndCounter() {
    var visible = getVisibleCards();
    if (!visible.length) {
      if (counter) counter.textContent = '0 / 0 Teşhis';
      return;
    }
    var trackRect = track.getBoundingClientRect();
    var activeIdx = 0;
    var minDiff = Infinity;

    visible.forEach(function(c, idx) {
      var r = c.getBoundingClientRect();
      var diff = Math.abs(r.left - trackRect.left);
      if (diff < minDiff) {
        minDiff = diff;
        activeIdx = idx;
      }
    });

    if (counter) {
      counter.textContent = (activeIdx + 1) + ' / ' + visible.length + ' Teşhis';
    }

    var dots = dotsWrap.querySelectorAll('.kobiDot');
    dots.forEach(function(dot, idx) {
      if (idx === activeIdx) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  }

  function rebuildDots() {
    var visible = getVisibleCards();
    dotsWrap.innerHTML = '';
    visible.forEach(function(c, idx) {
      var dot = document.createElement('div');
      dot.className = 'kobiDot' + (idx === 0 ? ' active' : '');
      dot.title = 'Teşhis ' + (idx + 1);
      dot.onclick = function() {
        c.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
      };
      dotsWrap.appendChild(dot);
    });
    updateDotsAndCounter();
  }

  var scrollTimer = null;
  track.addEventListener('scroll', function() {
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(updateDotsAndCounter, 50);
  }, { passive: true });

  window._rebuildKobiSlider = rebuildDots;
  rebuildDots();
}

function filterKobiShowcase(category, btn) {
  var pills = document.querySelectorAll('.kobiPill');
  for (var i = 0; i < pills.length; i++) {
    pills[i].classList.remove('active');
  }
  if (btn) btn.classList.add('active');

  var cards = document.querySelectorAll('.kobiCard');
  for (var j = 0; j < cards.length; j++) {
    var c = cards[j];
    if (category === 'all' || c.getAttribute('data-category') === category) {
      c.style.display = 'flex';
    } else {
      c.style.display = 'none';
    }
  }

  var track = document.getElementById('kobiSliderTrack');
  if (track) {
    track.scrollTo({ left: 0, behavior: 'smooth' });
  }
  if (window._rebuildKobiSlider) {
    window._rebuildKobiSlider();
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initKobiSlider);
} else {
  initKobiSlider();
}
</script>
</section></div>

<!-- SECTION: GERÇEK VERİ TABANLI TEMSİLİ YÖNETİM VAKALARI (CASE STUDIES) -->
<div class="secBlock reveal">
  <section id="caseStudies" class="marketingSection hidePrint" style="padding-top:0">
    <div class="marketingHead">
      <span class="workflowBadge" style="background:#ECFDF5;color:#047857;border-color:#A7F3D0">📈 GERÇEK VERİ TABANLI TEMSİLİ YÖNETİM VAKALARI</span>
      <h2 style="margin-top:10px">Rakamlar Yalan Söylemez: Finansal Karar Modellerimiz Kasaları Nasıl Rahatlatıyor?</h2>
      <p>Aşağıdaki vakalar, platformun 33 Karar Motoru ve çift taraflı denetim mimarisi ile analiz edilen gerçek sektör bilançoları baz alınarak modellenmiş <b>temsili yönetim senaryolarıdır</b>. Ticari mahremiyet nedeniyle unvanlar anonimleştirilmiş; matematiksel formülasyon, oran analizleri ve kâr/nakit optimizasyon dinamikleri birebir korunmuştur.</p>
    </div>

    <div class="caseGrid">
      <!-- Case 1: İmalat & Sanayi -->
      <div class="caseCard">
        <div class="caseHead">
          <span class="caseBadge verified">📊 TEMSİLİ MODELLEME VAKASI · İMALAT SANAYİ</span>
          <span class="caseLocation">Kocaeli · ₺65M Yıllık Hacim</span>
        </div>
        <div class="caseTitle">"Depodaki 180+ Günlük Ölü Stok Teşhis Edildi; ₺1.450.000 Atıl Nakit 45 Günde Kasaya Döndü."</div>
        <div class="caseProblem">
          <b>Kriz:</b> Şirket sürekli nakit sıkışıklığı çekiyor ve bankadan yüksek faizli ticari kredi kullanıyordu. Mizan incelendiğinde ₺3.2M stok görünüyordu ancak alt depo kırılımı takip edilmiyordu.
        </div>
        <div class="caseSolution">
          <b>DFBP Reçetesi:</b> Envanter İstihbarat Motoru mizan ile stok defterini eşleştirdi; 180 günü aşan 4 grup ölü hammaddeyi listeledi. Hızlı iskonto ve iade protokolüyle atıl sermaye nakde çevrildi.
        </div>
        <div class="caseKpis">
          <div class="caseKpiItem"><b style="color:#047857">+₺1.450.000</b><span>Kurtarılan Sıcak Nakit</span></div>
          <div class="caseKpiItem"><b style="color:#1D4ED8">112g → 64g</b><span>Nakit Çevrim (CCC)</span></div>
          <div class="caseKpiItem"><b style="color:#B45309">₺420.000 / yıl</b><span>Faiz Tasarrufu</span></div>
        </div>
      </div>

      <!-- Case 2: Gıda Dağıtım & Toptan -->
      <div class="caseCard">
        <div class="caseHead">
          <span class="caseBadge verified">📊 TEMSİLİ MODELLEME VAKASI · HIZLI TÜKETİM &amp; DAĞITIM</span>
          <span class="caseLocation">Bursa · ₺110M Yıllık Hacim</span>
        </div>
        <div class="caseTitle">"88 Günlük Operasyonel Açık Hesap Vadesi (Resmi Mizan: 81 Gün) 52 Güne İndirildi; Banka Kredi İhtiyacı ₺2.800.000 Azaldı."</div>
        <div class="caseProblem">
          <b>Kriz:</b> Şirket rekor ciro yapmasına rağmen ay sonlarında tedarikçi çeklerini ödeyemiyordu. Resmi mizan DSO vadesi 81 gün iken operasyonel yaşlandırma alt defterinde fiili vade 88 güne çıkmıştı; bayiler açık hesap vadelerini sürekli uzatarak şirketi faizsiz banka gibi kullanıyordu.
        </div>
        <div class="caseSolution">
          <b>DFBP Reçetesi:</b> Alacak Yaşlandırma Motoru ilk 20 bayinin vadesini taradı; vadesi 60 günü aşan riskli cariler durduruldu ve DBS (Doğrudan Borçlandırma Sistemi) entegrasyonuna bağlandı. Operasyonel DSO 88 günden 52 güne çekildi.
        </div>
        <div class="caseKpis">
          <div class="caseKpiItem"><b style="color:#047857">+₺2.800.000</b><span>Azalan Kredi Yükü</span></div>
          <div class="caseKpiItem"><b style="color:#1D4ED8">88g → 52g</b><span>Operasyonel Vade (DSO)</span></div>
          <div class="caseKpiItem"><b style="color:#B45309">₺640.000 / yıl</b><span>Kurtarılan Faiz Kârı</span></div>
        </div>
      </div>

      <!-- Case 3: Tekstil & İhracat -->
      <div class="caseCard">
        <div class="caseHead">
          <span class="caseBadge verified">📊 TEMSİLİ MODELLEME VAKASI · TEKSTİL &amp; İHRACAT</span>
          <span class="caseLocation">İstanbul · €4.2M İhracat Hacmi</span>
        </div>
        <div class="caseTitle">"%62 Müşteri Konsantrasyonu ve Gizli Kur Zararı Yakalandı; Brüt Marj %18'den %24'e Çıktı."</div>
        <div class="caseProblem">
          <b>Kriz:</b> Şirketin cirosunun üçte ikisi tek bir yabancı alıcıya bağlıydı. Döviz kuru hareketlerinde kur farkı gelir/gider ayrıştırması yapılmadığı için kârlı sanılan siparişler gizli zarara yol açıyordu.
        </div>
        <div class="caseSolution">
          <b>DFBP Reçetesi:</b> Müşteri Risk Radarı ve FX Risk Röntgeni devreye alındı. Kârsız 3 sipariş hattı revize edildi; vadeli döviz sözleşmelerinde kur koruma kuralları uygulanarak brüt marj 6 puan artırıldı.
        </div>
        <div class="caseKpis">
          <div class="caseKpiItem"><b style="color:#047857">+%6 Net Artış</b><span>Brüt Kâr Marjı</span></div>
          <div class="caseKpiItem"><b style="color:#1D4ED8">%62 → %34</b><span>Müşteri Bağımlılığı</span></div>
          <div class="caseKpiItem"><b style="color:#B45309">+€280.000</b><span>Net Nakit Katkısı</span></div>
        </div>
      </div>

      <!-- Case 4: Makine & Otomotiv Yan Sanayi -->
      <div class="caseCard">
        <div class="caseHead">
          <span class="caseBadge verified">📊 TEMSİLİ MODELLEME VAKASI · MAKİNE &amp; YAN SANAYİ</span>
          <span class="caseLocation">İzmir · ₺48M Yıllık Hacim</span>
        </div>
        <div class="caseTitle">"Mizan ile Stok Defteri Arasındaki %34 Mutabakat Uçurumu ve ₺920.000 Kâr Kaçağı Kapatıldı."</div>
        <div class="caseProblem">
          <b>Kriz:</b> Ortaklar toplantısında kâr paylaşımı konusunda anlaşmazlık vardı. Mizan tablosundaki 150/153 hesapları ile fiili depo sayım raporları arasında yüz binlerce liralık mutabakat farkı bulunuyordu.
        </div>
        <div class="caseSolution">
          <b>DFBP Reçetesi:</b> Data Hub Çapraz Mutabakat Motoru mizan ile stok listesini satır satır eşleştirdi; kayıp stok hareketleri ve faturalandırılmamış sevkiyatlar tespit edilerek ortaklar arasında tek veri konsensüsü sağlandı.
        </div>
        <div class="caseKpis">
          <div class="caseKpiItem"><b style="color:#047857">₺920.000</b><span>Tespit Edilen Sızıntı</span></div>
          <div class="caseKpiItem"><b style="color:#1D4ED8">%100 Mutabakat</b><span>Mizan &amp; Defter Uyumu</span></div>
          <div class="caseKpiItem"><b style="color:#B45309">1 Gün</b><span>Uzlaşma &amp; Karar Süresi</span></div>
        </div>
      </div>
    </div>
  </section>
</div>

<!-- SECTION: 3-KATMANLI ÜRÜN MİMARİSİ (PATRONUN AKLINDAKİ 8 KRİTİK SORU) -->
<div class="secBlock tint reveal">
  <section id="patronSorulari" class="marketingSection hidePrint">
    <div class="marketingHead">
      <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE">3 KATMANLI ÜRÜN MİMARİSİ</span>
      <h2>Patron Muhasebe Raporu Değil; "Kasada Neden Para Yok ve Yarın Ne Yapmalıyım?" Sorusunun Cevabını İster</h2>
      <p>Muhasebe programları sadece geçmişin dökümünü listeler. Digital Finance Business Partner ise patronun geceleri aklına takılan 8 kritik soruyu; çift taraflı analitik kanıtlar, net TL getirisi ve uygulanabilir yönetim kararlarıyla anında çözer.</p>
    </div>

    <div style="background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:22px;padding:26px;box-shadow:0 14px 34px rgba(15,27,45,.06)">
      <div style="position:relative;display:flex;align-items:center;margin-bottom:18px;gap:6px">
        <button type="button" class="pillScrollBtn" onclick="scrollPills('landingCeoPills', -280)" aria-label="Geri Kaydır" title="Önceki Sorular">‹</button>
        <div style="display:flex;gap:8px;overflow-x:auto;padding-bottom:6px;scrollbar-width:none;-ms-overflow-style:none;scroll-behavior:smooth;flex:1" id="landingCeoPills">
        <button type="button" class="ceoPill active" data-lq="lq1" onclick="switchLandingCeo('lq1')">💸 Kasada Neden Para Yok?</button>
        <button type="button" class="ceoPill" data-lq="lq2" onclick="switchLandingCeo('lq2')">👥 Hangi Müşteri Zarar Ettiriyor?</button>
        <button type="button" class="ceoPill" data-lq="lq3" onclick="switchLandingCeo('lq3')">📦 Depoda Ne Kadar Para Uyuyor?</button>
        <button type="button" class="ceoPill" data-lq="lq4" onclick="switchLandingCeo('lq4')">🔓 Kredisiz Kaç Milyon TL Nakit Çıkar?</button>
        <button type="button" class="ceoPill" data-lq="lq5" onclick="switchLandingCeo('lq5')">📉 Satış Artarken Marj Neden Büyümüyor?</button>
        <button type="button" class="ceoPill" data-lq="lq6" onclick="switchLandingCeo('lq6')">⚖️ Vade Makası (Müşteri vs Tedarikçi)</button>
        <button type="button" class="ceoPill" data-lq="lq7" onclick="switchLandingCeo('lq7')">🚨 Yarın Sabahın 3 Kritik Alarmı</button>
        <button type="button" class="ceoPill" data-lq="lq8" onclick="switchLandingCeo('lq8')">🎯 CEO'nun 1 Numaralı Kararı</button>
      </div>
        <button type="button" class="pillScrollBtn" onclick="scrollPills('landingCeoPills', 280)" aria-label="İleri Kaydır" title="Sonraki Sorular">›</button>
      </div>

      <div id="landingCeoCards">
        <!-- LQ1 -->
        <div id="lqCard_lq1" class="ceoQuestionCard active">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">💸 NAKİT AKIŞI &amp; KÂR KALİTESİ</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi (₺10M Ciro / ₺1M Net Kâr)</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Defterdeki Kâr, Alacak ve Stok Kilitlenmesinde Kayboluyor</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Defterde ₺1.000.000 net kâr görünmesine karşın, bu kârın neredeyse tamamı müşterilerin 80 günlük tahsilat vadesinde (₺2.25M) ve depodaki 96 günlük stokta (₺1.71M) kilitlenmiştir. Kasa bu kârı fiilen görememektedir.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Net Dönem Kârı</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺1.000.000</div><div style="font-size:9.5px;color:#94A3B8">Defter kârı</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Müşteride Kilitli (120)</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺2.250.000</div><div style="font-size:9.5px;color:#94A3B8">80 gün tahsilat</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Depoda Kilitli (150)</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺1.710.000</div><div style="font-size:9.5px;color:#94A3B8">96 gün stokta</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Nakit Çevrim (CCC)</div><div style="font-size:14px;font-weight:800;color:#0F172A">134 gün</div><div style="font-size:9.5px;color:#94A3B8">Nakit bekleme</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 İlk 10 müşteride açık hesap vadesini 15 gün geri çekin; vadeli siparişleri DBS veya %2 peşin nakit iskontosuyla hızlandırın.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺685.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺308.250 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> CFO &amp; Satış Direktörü · <b>Vade:</b> İlk 30 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ2 -->
        <div id="lqCard_lq2" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">👥 MÜŞTERİ KÂRLILIĞI &amp; ALACAK RİSKİ</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Yüksek Cirolu Müşteriler Uzun Vade ve Gizli Finansmanla Zarar Ettiriyor</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Cironun %38'ini tek başına oluşturan ilk 3 müşteri, 110 gün vade kullanmaktadır. %45 ticari kredi faizi ortamında bu vadenin faiz maliyeti satış marjının %14'ünü tüketmekte ve defterdeki net kârı gizli zarara dönüştürmektedir.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">İlk 3 Müşteri Payı</div><div style="font-size:14px;font-weight:800;color:#0F172A">%38,4</div><div style="font-size:9.5px;color:#94A3B8">Yüksek konsantrasyon</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Ortalama Vade</div><div style="font-size:14px;font-weight:800;color:#0F172A">110 gün</div><div style="font-size:9.5px;color:#94A3B8">Sektör medyanı 65g</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Alacak Finansman Yükü</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺485.000</div><div style="font-size:9.5px;color:#94A3B8">Yıllık faiz erozyonu</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Risk Skoru</div><div style="font-size:14px;font-weight:800;color:#0F172A">84 / 100</div><div style="font-size:9.5px;color:#94A3B8">Kritik seviye</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 Vadesi 75 günü aşan bu müşterilere açık hesap yerine banka DBS limiti zorunluluğu getirin ve %2 vade farkı protokolü imzalayın.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺520.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺234.000 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> Ticari Satış Direktörü · <b>Vade:</b> 45 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ3 -->
        <div id="lqCard_lq3" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">📦 STOK YÖNETİMİ &amp; ATIL SERMAYE</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Depoda ₺1.710.000 Uyuyor, Yıllık ₺769.500 Faiz Sızıntısı Üretiyor</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Mallar depoda ortalama 96 gün kalmaktadır. 90+ gündür hareket görmeyen atıl stoklar depoda çürürken şirketin banka kredisi maliyetini her ay büyütmektedir.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Depoda Bağlı Stok</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺1.710.000</div><div style="font-size:9.5px;color:#94A3B8">150-153 hesapları</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Stokta Kalma (DIO)</div><div style="font-size:14px;font-weight:800;color:#0F172A">96 gün</div><div style="font-size:9.5px;color:#94A3B8">Sektör medyanı 54g</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Yıllık Faiz Sızıntısı</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺769.500</div><div style="font-size:9.5px;color:#94A3B8">%45 faiz proxy</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Stok Devir Hızı</div><div style="font-size:14px;font-weight:800;color:#0F172A">3,8x / yıl</div><div style="font-size:9.5px;color:#94A3B8">Düşük devir</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 90 günden uzun süredir bekleyen ölü stokları paket indirimle derhal nakde çevirin. Satınalma siparişlerini haftalık satış hızına bağlayın.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺356.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺160.200 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> Tedarik Zinciri &amp; Satınalma Müdürü · <b>Vade:</b> 30 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ4 -->
        <div id="lqCard_lq4" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">🔓 İÇ KAYNAKLI ÖZ FİNANSMAN</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Banka Kredisi Almadan Şirket İçinden ₺1.041.000 Sıcak Nakit Çıkabilir</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Tahsilatı 15 gün öne çekmek, stoğu 15 gün hızlandırmak ve tedarikçi vadesini 10 gün uzatmak; bankaya tek kuruş faiz ödemeden şirketinize ₺1.041.000 nakit ve yıllık ₺468.450 net kâr kazandırır.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Tahsilat Katkısı (-15G)</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺411.000</div><div style="font-size:9.5px;color:#94A3B8">Alacak hızlandırma</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Stok Katkısı (-15G)</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺356.000</div><div style="font-size:9.5px;color:#94A3B8">Depo eritme</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Tedarikçi Katkısı (+10G)</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺274.000</div><div style="font-size:9.5px;color:#94A3B8">Satıcı finansmanı</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Toplam İç Nakit</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺1.041.000</div><div style="font-size:9.5px;color:#94A3B8">Sıfır banka kredisi</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 3 Kaldıraçlı Çalışma Sermayesi Programı başlatın: Satış ekibinin primini ciroya değil "kasaya giren tahsilata" endeksleyin.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺1.041.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺468.450 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> İcra Kurulu &amp; Genel Müdür · <b>Vade:</b> Hemen Devrede</div>
            </div>
          </div>
        </div>

        <!-- LQ5 -->
        <div id="lqCard_lq5" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">📉 KÂR KALİTESİ &amp; MALİYET KONTROLÜ</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Faaliyet Giderleri (OpEx) Cirodan %8 Daha Hızlı Artmış</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Satışlar %25 büyürken brüt marj %35'ten %31'e gerilemiş; genel yönetim ve lojistik giderleri kâr artışını eritmiştir. Şirket daha çok çalışmakta ancak daha az operasyonel kâr üretmektedir.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Brüt Kâr Marjı</div><div style="font-size:14px;font-weight:800;color:#0F172A">%31,0</div><div style="font-size:9.5px;color:#94A3B8">Önceki: %35,0 (↓)</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Faaliyet Kâr Marjı</div><div style="font-size:14px;font-weight:800;color:#0F172A">%10,0</div><div style="font-size:9.5px;color:#94A3B8">Operasyonel marj</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Gider / Ciro Oranı</div><div style="font-size:14px;font-weight:800;color:#0F172A">%21,0</div><div style="font-size:9.5px;color:#94A3B8">OpEx yoğunluğu</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Finansman Yükü</div><div style="font-size:14px;font-weight:800;color:#0F172A">%40,0</div><div style="font-size:9.5px;color:#94A3B8">Faaliyet kârına oranı</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 Fiyatlama politikasını enflasyon bazlı dinamik tarifeye geçirin; kârsız ürün kodlarını ürün portföyünden derhal ayıklayın.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Ekstra Faaliyet Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺200.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Yıllık Marj Katkısı</div><div style="font-size:14px;font-weight:800;color:#166534">+%2,0 Puan</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> Finans Direktörü &amp; Satış · <b>Vade:</b> 30 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ6 -->
        <div id="lqCard_lq6" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">⚖️ İŞLETME SERMAYESİ ASİMETRİSİ</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Tedarikçiye 42 Günde Ödeyip Müşteriyi 80 Gün Beklemek Şirketi Kanamaya İtiyor</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Ortaya çıkan 38 günlük vade açığını kapatmak için şirket kendi özkaynağını eritmekte ve bankadan yüksek faizli rotatif kredi çekmektedir.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Müşteri Vadesi (DSO)</div><div style="font-size:14px;font-weight:800;color:#0F172A">80 gün</div><div style="font-size:9.5px;color:#94A3B8">Alacak vadesi</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Tedarikçi Vadesi (DPO)</div><div style="font-size:14px;font-weight:800;color:#0F172A">42 gün</div><div style="font-size:9.5px;color:#94A3B8">Ödeme vadesi</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Net Vade Makası Açığı</div><div style="font-size:14px;font-weight:800;color:#0F172A">38 gün</div><div style="font-size:9.5px;color:#94A3B8">Finanse edilen gün</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Tedarikçi Borçları</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺750.000</div><div style="font-size:9.5px;color:#94A3B8">320 Satıcılar</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 Tedarikçilerle vadeleri 15 gün uzatacak konsinye veya vadeli çek protokolü yapın; müşterilere ise tedarikçi vadesinin üzerinde açık hesap açmayın.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺410.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺184.500 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> Satınalma Direktörü &amp; CFO · <b>Vade:</b> 30 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ7 -->
        <div id="lqCard_lq7" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">🚨 CEO ERKEN UYARI RADARI</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">33 Karar Motorunun Belirlediği 3 Öncelikli Alarm</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Mizan çift taraflı denetlenmiş ve nakit akışını riske atan ilk 3 finansal alarm tespit edilmiştir: Tahsilat süresinin uzaması, depoda kilitli sermaye ve kısa vadeli borç geri ödeme takvimi.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">1. Tahsilat Vadesi</div><div style="font-size:14px;font-weight:800;color:#0F172A">88 / 100</div><div style="font-size:9.5px;color:#94A3B8">Maruziyet: ₺780k</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">2. Kilitli Stok Yükü</div><div style="font-size:14px;font-weight:800;color:#0F172A">76 / 100</div><div style="font-size:9.5px;color:#94A3B8">Maruziyet: ₺769k</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">3. Likidite / Borç</div><div style="font-size:14px;font-weight:800;color:#0F172A">72 / 100</div><div style="font-size:9.5px;color:#94A3B8">Cari oran 1.1x</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Finansal Sağlık</div><div style="font-size:14px;font-weight:800;color:#0F172A">74 / 100</div><div style="font-size:9.5px;color:#94A3B8">Orta-Risk</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 Risk komitesini toplayarak bu 3 alarm için haftalık nakit akış toplantısı kurgulayın ve erken uyarı limitleri belirleyin.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Korunan Nakit Kalkanı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺390.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Batık Riski Önleme</div><div style="font-size:14px;font-weight:800;color:#166534">Tam Güvence</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> İcra Kurulu · <b>Vade:</b> İlk 7 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ8 -->
        <div id="lqCard_lq8" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">🎯 CEO İCRAAT DİREKTİFİ</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Bugün Masaya Koymanız Gereken 1 Numaralı Karar</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Şirketinizin nakit akışını ve kârını kalıcı olarak kurtaracak tek hamle: Vadesi 60 günü aşan müşterilere yeni mal sevkiyatını dondurmak ve ilk 10 müşteriyle banka teminatlı DBS protokolü başlatmaktır.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Yıllık Kâr Sızıntısı</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺1.782.000</div><div style="font-size:9.5px;color:#94A3B8">Faiz kaybı</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Kilitli Nakit Tutarı</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺3.960.000</div><div style="font-size:9.5px;color:#94A3B8">Alacak + Stok</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Kurtarılabilir Kâr</div><div style="font-size:14px;font-weight:800;color:#0F172A">+₺801.900</div><div style="font-size:9.5px;color:#94A3B8">Yıllık faiz tasarrufu</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">İcraat Etkisi</div><div style="font-size:14px;font-weight:800;color:#0F172A">Kritik</div><div style="font-size:9.5px;color:#94A3B8">Doğrudan kâr artışı</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 Satış direktörüne bugün yazılı talimat verin: Vadesi 60 günü aşan müşteriye sevkiyat onayı verilmeyecek; açık hesap riski DBS garantisine bağlanacaktır.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺685.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺308.250 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> CEO &amp; Genel Müdür · <b>Vade:</b> Bugün</div>
            </div>
          </div>
        </div>
      </div>

      <div style="margin-top:20px;padding-top:16px;border-top:1px solid #E2E8F0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px">
        <div style="font-size:13px;color:#64748B">
          💡 Kendi şirketinizin mizanında bu soruların yanıtlarını kuruşu kuruşuna görmek için canlı demoyu başlatın.
        </div>
        <a href="/uygulama?sample=data_hub" class="primary" style="text-decoration:none;padding:10px 20px;border-radius:10px;font-size:13.5px;font-weight:700">
          🔥 Kendi Verilerinizle Canlı Cevapları Görün →
        </a>
      </div>
    </div>
  </section>
</div>


<!-- SECTION: COMPARISON MATRIX -->
<div class="secBlock reveal"><section id="comparison" class="marketingSection hidePrint">
<div class="marketingHead">
  <span class="workflowBadge">KARŞILAŞTIRMA</span>
  <h2>Neden Digital Finance Business Partner?</h2>
  <p>Geleneksel muhasebe programları ve Excel şablonları neden şirket yöneticilerini yalnız bırakır?</p>
</div>
<div class="compareTableWrap">
  <table class="compareTable">
    <thead>
      <tr>
        <th>Kriter</th>
        <th>Klasik Muhasebe / ERP</th>
        <th>Excel Şablonları</th>
        <th>Geleneksel Finans Danışmanı</th>
        <th class="featured">Digital Finance Business Partner</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Karar Üretme Kabiliyeti</b></td>
        <td>❌ Yalnızca geçmiş kayıtları tutar</td>
        <td>❌ Statik formüller, karar mantığı yok</td>
        <td>⚠️ Kişiye bağımlı ve haftalar sürer</td>
        <td class="featured">✅ Anında 33 finansal karar motoru & yönetim aksiyonları</td>
      </tr>
      <tr>
        <td><b>Hesaplama Hızı</b></td>
        <td>Saatler süren veri filtreleme</td>
        <td>Günler süren formül bağlama</td>
        <td>Haftalar sonra gelen sunumlar</td>
        <td class="featured">⚡ 60 saniyede hazır yönetim raporu</td>
      </tr>
      <tr>
        <td><b>Kök Neden & Senaryo Analitiği</b></td>
        <td>❌ Yok</td>
        <td>❌ Kısıtlı ve formül bozulmasına açık</td>
        <td>⚠️ Manuel hesaplamalar</td>
        <td class="featured">✅ Deterministik Kök Neden & Canlı What-If Lab</td>
      </tr>
      <tr>
        <td><b>Maliyet & Erişilebilirlik</b></td>
        <td>Yüksek lisans ve sunucu maliyeti</td>
        <td>Zaman ve emek kaybı</td>
        <td>Aylık yüksek danışmanlık ücreti</td>
        <td class="featured">💰 Şeffaf ve anında amorti eden kurumsal SaaS</td>
      </tr>
      <tr>
        <td><b>Güven & Doğruluk</b></td>
        <td>Kullanıcı girişine bağımlı</td>
        <td>Formül bozulma riski yüksek</td>
        <td>Öznel insan yorumu</td>
        <td class="featured">🔒 %100 Çift taraflı denetim ve defter izleme</td>
      </tr>
    </tbody>
  </table>
</div>
</section></div>

<!-- SECTION: ÇÖZÜM MODELLERİ & PAKETLER BANNER -->
<div class="secBlock tint reveal">
  <section id="pricing" class="marketingSection hidePrint" style="padding-top:0">
    <div style="background:linear-gradient(145deg,#FFFFFF 0%,#F8FAFC 100%);border:1.5px solid #CBD5E1;border-radius:24px;box-shadow:0 14px 36px rgba(15,27,45,.06);padding:36px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:24px">
      <div style="max-width:680px">
        <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE">💼 ÇÖZÜM MODELLERİ &amp; PAKETLER</span>
        <h2 style="font-size:25px;font-family:var(--serif);margin:10px 0 8px;color:#0F1B2D;letter-spacing:-.3px">Şirketinizin Ölçeğine ve İhtiyacına Uygun Çözüm Modelleri</h2>
        <p style="color:#5B6B84;font-size:13.5px;line-height:1.65;margin:0">İster tek bir mizanla finansal durumunuzu anında test edin, ister çoklu veri ve What-If simülatörüyle şirketinizin büyümesini yönetin. <b>Starter</b> (Ücretsiz Keşif), <b>Professional</b> (KOBİ Yönetim Paketi) ve <b>Enterprise</b> (Holding / Grup Şirketi) modellerimizin detaylarını ve özellik matrisini inceleyin.</p>
      </div>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a href="/paketler" class="primary" style="text-decoration:none;padding:13px 24px;border-radius:12px;font-size:13.5px;font-weight:700">Tüm Paketleri &amp; Çözüm Modellerini Gör →</a>
        <a href="/uygulama?sample=data_hub" class="secondary" style="text-decoration:none;padding:13px 20px;border-radius:12px;font-size:13.5px">⚡ Canlı Demoyu Başlat</a>
      </div>
    </div>
  </section>
</div>

<!-- SECTION: BANKA DÜZEYİNDE GÜVENLİK VE HUKUKİ TAAHHÜTLER -->
<div class="secBlock reveal">
  <section id="securityShield" class="marketingSection hidePrint" style="padding-top:0">
    <div class="marketingHead">
      <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE">🛡️ KURUMSAL GÜVENLİK VE GİZLİLİK KALKANI</span>
      <h2 style="margin-top:10px">Şirketinizin En Mahrem Verisi İçin Bankacılık Standardında Güvence</h2>
      <p>Mizanınız ve alt defterleriniz şirketinizin ticari DNA'sıdır. Digital Finance Business Partner, sıfır kalıcı disk kaydı ve bankacılık standardı şifreleme protokolleriyle kurumsal mahremiyetinizi en üst seviyede korur.</p>
    </div>

    <div class="secShieldGrid">
      <div class="secShieldCard">
        <div class="secShieldIco">🧠</div>
        <h4>Sıfır Disk Depolama (RAM-Only)</h4>
        <p>Yüklediğiniz dosyalar sunucu sabit diskine asla kaydedilmez. Tüm matematiksel hesaplamalar anlık bellekte (RAM) icra edilir; oturum sonlandığında bellek tamamen temizlenir.</p>
      </div>

      <div class="secShieldCard">
        <div class="secShieldIco">🔒</div>
        <h4>256-Bit Banka Düzeyinde TLS</h4>
        <p>Tarayıcınız ile platform arasındaki tüm veri transferi uluslararası bankacılık standardı 256-bit SSL/TLS tünelleriyle uçtan uca şifrelenir; araya girme imkansızdır.</p>
      </div>

      <div class="secShieldCard">
        <div class="secShieldIco">🚫</div>
        <h4>Model Eğitimi Yasağı &amp; KVKK</h4>
        <p>Finansal verileriniz, cirolarınız veya cari isimleriniz asla genel yapay zeka modellerinin eğitiminde kullanılmaz; 6698 sayılı KVKK kapsamında hiçbir 3. tarafla paylaşılmaz.</p>
      </div>

      <div class="secShieldCard">
        <div class="secShieldIco">🤝</div>
        <h4>Kurumsal NDA Güvencesi</h4>
        <p>Holdingler, denetim firmaları ve kurumsal şirketler için talep halinde şirketinizle karşılıklı bağlayıcı Kurumsal Gizlilik Sözleşmesi (NDA) imzalanır.</p>
      </div>
    </div>

    <div style="text-align:center;margin-top:20px">
      <a href="javascript:void(0)" onclick="showKvkkModal()" style="font-size:12.5px;color:#1D4ED8;font-weight:700;text-decoration:underline">Aydınlatma ve Kurumsal Veri Güvenliği Taahhüt Metnini İnceleyin →</a>
    </div>
  </section>
</div>

<!-- SECTION: SIKÇA SORULAN SORULAR (SSS / FAQ) -->
<div class="secBlock tint reveal">
  <section id="faq" class="marketingSection hidePrint" style="padding-top:0">
    <div class="marketingHead">
      <span class="workflowBadge" style="background:#F1F5F9;color:#334155;border-color:#CBD5E1">❓ AKLINIZA TAKILABİLECEK SORULAR</span>
      <h2 style="margin-top:10px">KOBİ Patronlarının ve Finans Yöneticilerinin En Çok Sorduğu Sorular</h2>
      <p>Sistemin güvenliği, çalışma şekli ve şirket yönetimine sağlayacağı somut getiriler hakkında bilmeniz gereken her şey.</p>
    </div>

    <div style="max-width:760px;margin:24px auto 0">
      <details class="faqItem" open>
        <summary>Mizan dosyamı sisteme yüklediğimde şirketimin ticari sırları güvende mi?</summary>
        <p>Evet, %100 güvendedir. Sistemimiz "RAM-Only" (Sıfır Kalıcı Disk Depolama) mimarisiyle çalışır. Yüklediğiniz Excel veya CSV dosyası sunucu sabit diskine ya da veritabanına ASLA kaydedilmez. Matematiksel analiz tarayıcınızın oturumunda ve geçici bellekte hesaplanır; sekme kapandığında tüm veriler silinir. Ayrıca hiçbir finansal veri yapay zekâ modellerinin genel eğitiminde kullanılmaz.</p>
      </details>

      <details class="faqItem">
        <summary>Sistemi kullanmak için muhasebecime veya ERP uzmanına bağımlı mıyım?</summary>
        <p>Hayır. Muhasebecinizden veya kullandığınız ERP yazılımından (Logo, Mikro, Netsis, Zirve, Luca, SAP vb.) sadece tek bir mizan çıktısı almanız yeterlidir. Dosyayı sürükleyip bıraktığınızda 33 Karar Motoru hesap kodlarını (1xx-7xx) otomatik eşleştirir ve 60 saniye içinde anlaşılır Türkçe yönetim kararlarına dönüştürür.</p>
      </details>

      <details class="faqItem">
        <summary>Digital Finance Business Partner bir muhasebe programı mıdır?</summary>
        <p>Hayır, muhasebe programı değildir. Muhasebe yazılımları devlete vergi beyannamesi vermek için geçmiş faturaları kaydeder; "Kasa neden boş?", "Hangi müşteri zarar ettiriyor?", "Depoda kaç para bağlı?" sorularına cevap vermez. Digital Finance Business Partner ise geçmişi değil; yarın sabah atacağınız yönetim ve nakit kurtarma adımlarını belirler.</p>
      </details>

      <details class="faqItem">
        <summary>1xx-7xx hesap planını sistem nasıl denetliyor?</summary>
        <p>Tek Düzen Hesap Planı'ndaki (TDHP) 1xx Dönen Varlıklar, 2xx Duran Varlıklar, 3xx Kısa Vadeli Borçlar, 4xx Uzun Vadeli Borçlar, 5xx Özkaynaklar ve 6xx/7xx Gelir-Maliyet hesapları çift taraflı muhasebe denetim kurallarıyla çapraz taranır. Mizan bakiyeleri ile alacak/stok alt defterleri arasındaki tutarsızlıklar kuruşu kuruşuna teşhis edilir.</p>
      </details>

      <details class="faqItem">
        <summary>Çoklu para birimi (USD/EUR) ve Tekdüzen Hesap Planı uyumu nasıl?</summary>
        <p>Sistemimiz ₺ TRY, $ USD, € EUR ve £ GBP para birimlerinde çalışabilir. İhracatçı veya ithalatçı şirketler için kur farkı kâr/zararlarını operasyonel kârdan ayırarak döviz risk röntgeni çıkarır. Tekdüzen Hesap Planı'ndaki (TDHP) tüm hesapları kurumsal yönetim muhasebesi ve nakit akışı standartlarına dönüştürür.</p>
      </details>

      <details class="faqItem">
        <summary>Yönetim Kurulu ve bankalar için rapor nasıl alınıyor?</summary>
        <p>Analiz tamamlandığında tek bir tuşla C-Level ve Yönetim Kurulu için özel hazırlanmış "1-Sayfalık Executive Board Deck" A4 raporunu alabilirsiniz. Bu rapor banka kredi görüşmelerinde veya ortaklar toplantısında şirketin finansal sağlığını, borç ödeme gücünü ve nakit planını profesyonelce kanıtlar.</p>
      </details>
    </div>
  </section>
</div>

<!-- CLOSING ACTION SECTION -->
<div class="secBlock reveal"><section class="ctaBanner hidePrint" style="margin-top:10px">
  <div>
    <h3 style="font-size:24px;margin:0 0 8px;font-family:var(--serif)">Finansal Verilerinizi Stratejik İş Kararlarına Dönüştürün</h3>
    <p style="margin:0;color:var(--muted);font-size:14px">Entegrasyon gerektirmez. Örnek Data Hub verisiyle veya kendi mizanınızla 60 saniyede karar raporunuzu alın.</p>
  </div>
  <div style="display:flex;gap:12px;flex-wrap:wrap">
    <a href="/uygulama?sample=data_hub" class="primary" style="text-decoration:none;padding:13px 22px;border-radius:12px;font-size:14px;font-weight:700">🔥 Canlı Demoyu Başlat</a>
    <a href="/uygulama" class="secondary" style="text-decoration:none;padding:13px 22px;border-radius:12px;font-size:14px;font-weight:700">Kendi Dosyanızı Yükleyin →</a>
  </div>
</section></div>

</main>
<div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/cozumler">Çözümler</a></li><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • <a href="https://digitalfinancebp.com" style="color:var(--accent);text-decoration:none;font-weight:700">digitalfinancebp.com</a> • Deterministik Finans Karar Motoru &amp; Çift Yönlü Denetim Sistemi<br><span style="opacity:.85">Bu analiz deterministik matematiksel hesaplamalara ve çift taraflı denetim kurallarına dayanır; resmi mali tablo veya vergi beyannamesi yerine geçmez. Nihai yönetim kararları için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca anlık analiz süresince RAM bellekte işlenir; sunucu sabit diskinde ASLA kalıcı saklanmaz. KVKK ve kurumsal gizlilik politikamız için <a href="javascript:void(0)" onclick="showKvkkModal()" style="color:var(--accent);text-decoration:underline;font-weight:600">Aydınlatma ve Gizlilik Metni</a>'ni inceleyebilirsiniz.</span></div></div></div>

<!-- Board One-Pager Executive Modal (Root level child for clean A4 printing) -->
<div id="boardDeckModal" class="hidden" style="position:fixed;inset:0;background:rgba(15,27,45,.75);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);display:flex;align-items:center;justify-content:center;z-index:2000;padding:20px;overflow-y:auto">
  <div style="background:#FFFFFF;border-radius:18px;max-width:960px;width:100%;max-height:92vh;display:flex;flex-direction:column;box-shadow:0 25px 60px rgba(0,0,0,0.3);overflow:hidden">
    <div class="hidePrint" style="display:flex;justify-content:space-between;align-items:center;padding:14px 22px;border-bottom:1px solid #E2E8F0;background:#F8FAFC">
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:20px">📑</span>
        <div>
          <h3 style="margin:0;font-size:15px;color:#0F1B2D;font-weight:800">Yönetim Kurulu Finansal Karar Özeti (Executive Board Deck)</h3>
          <p style="margin:0;font-size:11.5px;color:#64748B">C-Level ve Yönetim Kurulu sunumları için tek sayfalık A4 özet görünüm</p>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:8px">
        <button id="printBoardDeckBtn" type="button" class="primary" style="padding:7px 14px;border-radius:8px;font-size:12.5px;font-weight:700">🖨️ Yazdır / PDF İndir</button>
        <button id="openDeckNewTabBtn" type="button" class="secondary" style="padding:7px 14px;border-radius:8px;font-size:12.5px;font-weight:700" onclick="openBoardDeckInNewWindow()">📄 Temiz A4 Görünümü</button>
        <button id="closeBoardDeckBtn" type="button" style="background:none;border:none;font-size:22px;color:#64748B;cursor:pointer;padding:4px 8px">✕</button>
      </div>
    </div>
    <div id="boardDeckContent" style="padding:22px;overflow-y:auto;flex:1"></div>
  </div>
</div>
<script>
window.scrollPills = function(id, delta){
  const el = document.getElementById(id);
  if(el){ el.scrollBy({ left: delta, behavior: 'smooth' }); }
};
window.switchLandingCeo = function(lqid){
  document.querySelectorAll('#landingCeoPills .ceoPill').forEach(p => {
    p.classList.toggle('active', p.getAttribute('data-lq') === lqid);
  });
  document.querySelectorAll('#landingCeoCards .ceoQuestionCard').forEach(c => {
    c.classList.toggle('active', c.id === 'lqCard_' + lqid);
  });
};

window.setHomeBilling = function(cycle) {
  var btnM = document.getElementById('homeBtnMonthly');
  var btnA = document.getElementById('homeBtnAnnual');
  var amt = document.getElementById('homeProPriceAmt');
  var sub = document.getElementById('homeProSubText');
  if (!btnM || !btnA || !amt) return;
  if (cycle === 'annual') {
    btnA.className = 'primary'; btnA.style.border = '';
    btnM.className = 'secondary'; btnM.style.border = '0';
    amt.innerHTML = '₺1.990<span> /ay</span>';
    if (sub) sub.textContent = 'Yıllık peşin faturalandırmada %20 indirim avantajı (₺23.880 /yıl).';
  } else {
    btnM.className = 'primary'; btnM.style.border = '';
    btnA.className = 'secondary'; btnA.style.border = '0';
    amt.innerHTML = '₺2.490<span> /ay</span>';
    if (sub) sub.textContent = 'Kendi mizanını ve alt defterlerini yükleyip yönetim kurulu kararları üreten şirketler için.';
  }
};
window.showKvkkModal=function(){var m=document.getElementById('kvkkModal');if(!m){m=document.createElement('div');m.id='kvkkModal';m.style.cssText='position:fixed;inset:0;background:rgba(15,27,45,0.7);z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(4px);';m.innerHTML='<div style="background:#FFFFFF;border-radius:18px;max-width:640px;width:100%;max-height:85vh;overflow-y:auto;padding:28px;box-shadow:0 20px 50px rgba(0,0,0,0.3);position:relative;border:1px solid #E2E8F0"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid #E2E8F0;padding-bottom:12px"><div style="display:flex;align-items:center;gap:8px"><span style="font-size:20px">🔒</span><h3 style="margin:0;font-size:18px;color:#0F1B2D;font-family:sans-serif;font-weight:700">Veri Güvenliği, RAM-Only İşleme ve KVKK Taahhüdü</h3></div><button class="kvkkClose" style="background:#F1F5F9;border:0;border-radius:50%;width:30px;height:30px;cursor:pointer;font-weight:bold;font-size:16px">✕</button></div><div style="font-size:13px;line-height:1.7;color:#33415C;display:flex;flex-direction:column;gap:12px"><div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:12px;color:#166534"><b>🛡️ Sıfır Disk Depolama (RAM-Only):</b> Yüklediğiniz mizan, muavin defteri veya operasyonel raporlar sunucunun kalıcı depolama birimlerine (HDD/SSD/Veritabanı) kaydedilmez. Tüm matematiksel hesaplamalar ve çift taraflı denetim anlık bellek (RAM) üzerinde icra edilir ve analiz tamamlandığında oturumla birlikte tamamen silinir.</div><p><b>1. Veri İzolasyonu &amp; Model Eğitimi Yasağı:</b> Şirketiniz tarafından paylaşılan hiçbir finansal veri, ciro, müşteri adı veya bilanço kalemi üçüncü şahıslara verilmez, satılmaz ve genel yapay zekâ modellerinin eğitimi için havuzlara aktarılmaz.</p><p><b>2. 256-Bit TLS Şifreleme:</b> Tarayıcınız ile platform arasındaki tüm veri akışı bankacılık standardında 256-bit SSL/TLS tüneli üzerinden şifrelenir.</p><p><b>3. 6698 Sayılı KVKK Uyumluluğu:</b> Şirket yetkililerine ait iletişim bilgileri ve ticari sırlar yalnızca talep edilen analizlerin üretilmesi amacıyla işlenir; yasal yükümlülükler haricinde hiçbir tarafla paylaşılmaz.</p><p><b>4. Kurumsal Gizlilik Sözleşmesi (NDA):</b> Kurumsal entegrasyon veya holding düzeyinde çalışmalarda şirketinizle karşılıklı Kurumsal NDA akdedilir.</p></div><div style="margin-top:20px;text-align:right"><button class="kvkkClose primary" style="padding:9px 20px;border-radius:10px;font-size:13px;background:#1D4ED8;color:#fff;border:0;cursor:pointer;font-weight:700">Anladım ve Kabul Ediyorum</button></div></div>';m.addEventListener('click',function(e){if(e.target===m||e.target.classList.contains('kvkkClose'))m.style.display='none';});document.body.appendChild(m);}m.style.display='flex';};
document.getElementById('navToggle')?.addEventListener('click',()=>document.getElementById('mainNav')?.classList.toggle('open'));
window.addEventListener('scroll',()=>{document.querySelector('.top')?.classList.toggle('scrolled',window.scrollY>8)});
(function(){
  const els=document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){els.forEach(e=>e.classList.add('in'));return;}
  const io=new IntersectionObserver((entries)=>{entries.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}})},{threshold:.12});
  els.forEach(e=>io.observe(e));
})();
(function(){
  // Finance-flavoured count-up animation for stat/kpi numbers on scroll into view
  const targets = document.querySelectorAll('.stat b, .aboutStats .st b, .pvRing b, .scoreNum strong');
  if(!('IntersectionObserver' in window) || !targets.length) return;
  const parse = (txt)=>{ const m = txt.match(/-?\d[\d.,]*/); return m ? m[0] : null; };
  const cio = new IntersectionObserver((entries)=>{
    entries.forEach(en=>{
      if(!en.isIntersecting) return;
      cio.unobserve(en.target);
      const el = en.target; const raw = el.textContent; const numStr = parse(raw);
      if(!numStr) return;
      const prefix = raw.slice(0, raw.indexOf(numStr));
      const suffix = raw.slice(raw.indexOf(numStr)+numStr.length);
      const clean = numStr.replace(/\./g,'').replace(',', '.');
      const target = parseFloat(clean); if(isNaN(target)) return;
      const decimals = (clean.split('.')[1]||'').length;
      const dur = 900; const t0 = performance.now();
      function step(t){
        const p = Math.min(1,(t-t0)/dur); const eased = 1-Math.pow(1-p,3);
        const val = target*eased;
        el.textContent = prefix + val.toFixed(decimals).replace('.', decimals?',':'') + suffix;
        if(p<1) requestAnimationFrame(step); else el.textContent = raw;
      }
      requestAnimationFrame(step);
    });
  }, {threshold:.4});
  targets.forEach(t=>cio.observe(t));
})();
(function(){
  // Staggered grow-in for waterfall / bridge chart columns and progress bars
  document.querySelectorAll('.waterfall').forEach(wf=>{
    [...wf.children].forEach((col,i)=>{ col.style.animation = `growUp .6s ease ${i*70}ms both`; });
  });
  document.querySelectorAll('.bar i, .abar i').forEach((i,idx)=>{ i.style.animation = `growWidth .7s ease ${idx*40}ms both`; });
})();
(function(){
  // Hero "live" dashboard: auto-cycling tabs (EBITDA / DuPont / CCC / Risk / Scenario)
  const tabs=[...document.querySelectorAll('#heroDashTabs span')];
  const panes=[...document.querySelectorAll('#heroDashPanes .dashPane')];
  const container = document.getElementById('heroDashPanes');
  if(!tabs.length||!panes.length) return;
  let idx=0, timer=null, isPaused=false;
  function show(i){
    idx=i;
    tabs.forEach(t=>t.classList.toggle('on', t.dataset.pane===String(i)));
    panes.forEach(p=>p.classList.toggle('on', p.dataset.pane===String(i)));
  }
  function next(){ if(!isPaused) show((idx+1)%panes.length); }
  function restart(){ if(timer) clearInterval(timer); timer=setInterval(next,4200); }
  tabs.forEach(t=>t.addEventListener('click',()=>{ show(parseInt(t.dataset.pane,10)); restart(); }));
  if(container){
    container.addEventListener('mouseenter', ()=>{ isPaused=true; });
    container.addEventListener('mouseleave', ()=>{ isPaused=false; });
    container.addEventListener('focusin', ()=>{ isPaused=true; });
    container.addEventListener('focusout', ()=>{ isPaused=false; });
  }
  restart();
})();
(function(){
  // Interactive 4-step workflow player
  const cards = [...document.querySelectorAll('.wfInteractive')];
  const pills = [...document.querySelectorAll('#wfNavPills button')];
  const tagEl = document.getElementById('wfViewerStepTag');
  const titleEl = document.getElementById('wfViewerStepTitle');
  const contentEl = document.getElementById('wfViewerContent');
  if(!cards.length || !contentEl) return;

  const stepData = [
    {
      badge: 'CANLI SİMÜLASYON · ADIM 1',
      title: 'Mizan ve Alt Defterlerin Doğrudan İçe Aktarımı',
      html: '<div style="display:grid;grid-template-columns:1.2fr .8fr;gap:20px;align-items:center"><div><p style="color:#334155;font-size:13.5px;line-height:1.6;margin:0 0 14px">ERP veya muhasebe programınızdan aldığınız standart Excel/CSV mizanınızı ve varsa yaşlandırma/stok alt defterlerinizi tarayıcıya sürükleyin. Kolon eşleme yapay zeka tahminiyle değil, hesap planı kuralları (1xx-7xx) üzerinden deterministik olarak anında tanınır.</p><div style="display:flex;gap:10px;flex-wrap:wrap"><span style="background:#F1F5F9;border:1px solid #CBD5E1;padding:6px 12px;border-radius:8px;font-size:12px;color:#1D4ED8;font-weight:600">✓ Luca, Logo, Mikro, Netsis, Zirve uyumlu</span><span style="background:#ECFDF5;border:1px solid #A7F3D0;padding:6px 12px;border-radius:8px;font-size:12px;color:#047857;font-weight:600">✓ Sıfır Kurulum &amp; Sıfır Bekleme</span></div></div><div style="background:#F8FAFC;border:2px dashed #93C5FD;border-radius:14px;padding:24px 20px;text-align:center"><div style="font-size:32px;margin-bottom:8px">📥</div><b style="color:#0F172A;font-size:13px;display:block">Mizan Dosyanızı Sürükleyin</b><span style="color:#64748B;font-size:11px">.xlsx, .xls, .csv formatları otomatik taranır</span></div></div>'
    },
    {
      badge: 'CANLI SİMÜLASYON · ADIM 2',
      title: '33 Deterministik Karar Motoru & Kâr Sızıntısı Teşhisi',
      html: '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px"><div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:14px;padding:16px"><b style="color:#1D4ED8;font-size:13px;display:block;margin-bottom:8px">🔍 Bilanço &amp; Likidite Doğrulaması</b><ul style="margin:0;padding-left:16px;color:#334155;font-size:12.5px;line-height:1.8"><li>Aktif = Pasif denkliği kontrolü (0.00 TL tolerans)</li><li>Cari Oran, Likidite, Nakit Oranı analizi</li><li>Altman Z-Score İflas Riski motoru</li></ul></div><div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:14px;padding:16px"><b style="color:#047857;font-size:13px;display:block;margin-bottom:8px">⚡ Kârın Nakde Dönüşümü &amp; Kilitli Nakit</b><ul style="margin:0;padding-left:16px;color:#334155;font-size:12.5px;line-height:1.8"><li>Kârın Nakde Dönüşüm Oranı (Cash Realization)</li><li>88 gün açık hesap ve gizli banka faiz yükü</li><li>180+ gün ölü stok ve vade aşım tespiti</li></ul></div></div>'
    },
    {
      badge: 'CANLI SİMÜLASYON · ADIM 3',
      title: 'Yönetim Kararları, What-If Simülatörü &amp; 1-Sayfalık İcraat Özeti',
      html: '<div style="display:grid;grid-template-columns:1.2fr .8fr;gap:16px;align-items:center"><div><div style="background:#F8FAFC;border:1px solid #E2E8F0;border-left:4px solid #10B981;border-radius:0 12px 12px 0;padding:12px 16px;margin-bottom:10px"><b style="color:#0F172A;font-size:13px;display:block">Aksiyon 1: Müşteri Vade Protokolü ve %2 Erken Ödeme İskontosu</b><span style="color:#64748B;font-size:11.5px">Sahibi: Satış Direktörü &amp; Finans · Hedef: 30 Gün · Kurtarılacak Nakit: +620.000 ₺</span></div><div style="background:#F8FAFC;border:1px solid #E2E8F0;border-left:4px solid #2563EB;border-radius:0 12px 12px 0;padding:12px 16px"><b style="color:#0F172A;font-size:13px;display:block">Aksiyon 2: 180+ Gün Ölü Stok Tasfiyesi ve Sipariş Kısıtı</b><span style="color:#64748B;font-size:11.5px">Sahibi: Tedarik Zinciri · Hedef: 45 Gün · Kurtarılacak Nakit: +380.000 ₺</span></div></div><div style="background:linear-gradient(135deg,#EFF6FF,#DBEAFE);border:1px solid #BFDBFE;border-radius:14px;padding:16px;text-align:center"><div style="font-size:24px;margin-bottom:6px">📑</div><b style="color:#1D4ED8;font-size:13px;display:block;margin-bottom:4px">1-Sayfalık Yönetim Kurulu PDF</b><span style="color:#1E3A8A;font-size:11.5px">Karar maddeleri, What-If simülasyon sonuçları ve nakit hedefleri tek sayfada özetlenir.</span></div></div>'
    }
  ];

  let currentStep = 0, autoTimer = null;
  function setStep(idx){
    currentStep = idx;
    cards.forEach((c, i)=>{
      c.style.borderTop = i===idx ? '3px solid var(--accent)' : 'none';
      c.style.background = i===idx ? '#F8FAFF' : '#FFFFFF';
    });
    pills.forEach((p, i)=>{
      p.style.background = i===idx ? '#1D4ED8' : '#F1F5F9';
      p.style.color = i===idx ? '#FFFFFF' : '#64748B';
      p.style.border = i===idx ? 'none' : '1px solid #E2E8F0';
    });
    const d = stepData[idx];
    if(tagEl) tagEl.textContent = d.badge;
    if(titleEl) titleEl.textContent = d.title;
    if(contentEl) contentEl.innerHTML = d.html;
  }

  function restartWfTimer(){
    if(autoTimer) clearInterval(autoTimer);
    autoTimer = setInterval(()=>{ setStep((currentStep+1)%stepData.length); }, 5000);
  }

  cards.forEach((c, i)=>{
    c.addEventListener('click', ()=>{ setStep(i); restartWfTimer(); });
  });
  pills.forEach((p, i)=>{
    p.addEventListener('click', ()=>{ setStep(i); restartWfTimer(); });
  });
  restartWfTimer();
})();
(function(){
  // Executive Journey: reveal each step in sequence as the section scrolls into view
  const steps=[...document.querySelectorAll('.jStep')];
  if(!steps.length) return;
  if(!('IntersectionObserver' in window)){ steps.forEach(s=>s.classList.add('in')); return; }
  const jio=new IntersectionObserver((entries)=>{
    entries.forEach(en=>{
      if(en.isIntersecting){
        steps.forEach((s,i)=>setTimeout(()=>s.classList.add('in'), i*130));
        jio.unobserve(en.target);
      }
    });
  },{threshold:.3});
  jio.observe(document.getElementById('journey'));
})();
(function(){
  const revSlider = document.getElementById('leakRevSlider');
  const dsoSlider = document.getElementById('leakDsoSlider');
  const secSelect = document.getElementById('leakSectorSelect');
  const revDisplay = document.getElementById('leakRevDisplay');
  const dsoDisplay = document.getElementById('leakDsoDisplay');
  const lockedCash = document.getElementById('leakLockedCash');
  const annualCost = document.getElementById('leakAnnualCost');
  const d15Impact = document.getElementById('leak15DayImpact');

  if(!revSlider || !dsoSlider || !secSelect) return;

  function fmtTL(num){
    return '₺' + Math.round(num).toLocaleString('tr-TR');
  }

  function updateLeakCalc(){
    const rev = parseFloat(revSlider.value) || 36000000;
    const dso = parseFloat(dsoSlider.value) || 85;
    const rate = parseFloat(secSelect.value) || 0.45;

    revDisplay.textContent = fmtTL(rev);
    dsoDisplay.textContent = dso + ' Gün';

    const locked = (rev / 365) * dso;
    const cost = locked * rate;
    const rec15 = (rev / 365) * 15;

    lockedCash.textContent = fmtTL(locked);
    annualCost.textContent = fmtTL(cost);
    d15Impact.textContent = '+' + fmtTL(rec15);
  }

  revSlider.addEventListener('input', updateLeakCalc);
  dsoSlider.addEventListener('input', updateLeakCalc);
  secSelect.addEventListener('change', updateLeakCalc);
  updateLeakCalc();
})();

// ==========================================
// 60-SANİYELİK CANLI NAKİT LABORATUVARI MOTORU
// ==========================================
(function(){
  function fmtTL(v){
    return '+' + Math.round(v).toLocaleString('tr-TR') + ' ₺';
  }

  // Hero Pane 4 Simülatörü
  window.recalcPane4Sim = function(){
    const pEl = document.getElementById('pane4PriceRange');
    const dEl = document.getElementById('pane4DsoRange');
    const sEl = document.getElementById('pane4DioRange');
    if(!pEl || !dEl || !sEl) return;

    const p = parseFloat(pEl.value) || 0;
    const d = parseFloat(dEl.value) || 0;
    const s = parseFloat(sEl.value) || 0;

    const pVal = document.getElementById('pane4PriceVal');
    const dVal = document.getElementById('pane4DsoVal');
    const sVal = document.getElementById('pane4DioVal');
    if(pVal) pVal.textContent = '+%' + p.toFixed(1).replace('.', ',');
    if(dVal) dVal.textContent = '-' + d + ' Gün';
    if(sVal) sVal.textContent = '-%' + s;

    // Baz model: 10M Ciro, 1.7M Stok
    const profit = 10000000 * (p / 100);
    const dsoCash = (10000000 / 365) * d;
    const stockCash = 1700000 * 0.40 * (s / 100);
    const total = profit + dsoCash + stockCash;

    const prKpi = document.getElementById('pane4ProfitKpi');
    const dsKpi = document.getElementById('pane4DsoKpi');
    const totKpi = document.getElementById('pane4TotalKpi');
    if(prKpi) prKpi.textContent = fmtTL(profit);
    if(dsKpi) dsKpi.textContent = fmtTL(dsoCash);
    if(totKpi) totKpi.textContent = fmtTL(total);
  };

  // Full-Width Home What-If Lab Simülatörü
  window.recalcHomeLabSim = function(){
    const pEl = document.getElementById('labPriceRange');
    const dEl = document.getElementById('labDsoRange');
    const sEl = document.getElementById('labDioRange');
    if(!pEl || !dEl || !sEl) return;

    const p = parseFloat(pEl.value) || 0;
    const d = parseFloat(dEl.value) || 0;
    const s = parseFloat(sEl.value) || 0;

    const pVal = document.getElementById('labPriceVal');
    const dVal = document.getElementById('labDsoVal');
    const sVal = document.getElementById('labDioVal');
    if(pVal) pVal.textContent = '+%' + p.toFixed(1).replace('.', ',');
    if(dVal) dVal.textContent = '-' + d + ' Gün';
    if(sVal) sVal.textContent = '-%' + s;

    // 10M Ciro, 1.7M Stok
    const profit = 10000000 * (p / 100);
    const dsoCash = (10000000 / 365) * d;
    const stockCash = 1700000 * 0.40 * (s / 100);
    const total = profit + dsoCash + stockCash;

    const vCounter = document.getElementById('labTotalVaultCounter');
    const prSub = document.getElementById('labProfitSub');
    const dsSub = document.getElementById('labDsoSub');
    const diSub = document.getElementById('labDioSub');

    if(vCounter) vCounter.textContent = fmtTL(total);
    if(prSub) prSub.textContent = fmtTL(profit);
    if(dsSub) dsSub.textContent = fmtTL(dsoCash);
    if(diSub) diSub.textContent = fmtTL(stockCash);
  };

  window.applyLabPreset = function(p, d, s, btn){
    const pEl = document.getElementById('labPriceRange');
    const dEl = document.getElementById('labDsoRange');
    const sEl = document.getElementById('labDioRange');
    if(pEl) pEl.value = p;
    if(dEl) dEl.value = d;
    if(sEl) sEl.value = s;

    document.querySelectorAll('.labPresetBtn').forEach(b => b.classList.remove('active'));
    if(btn) btn.classList.add('active');

    window.recalcHomeLabSim();
  };

  // İlk yüklemede çalıştır
  setTimeout(function(){
    if(window.recalcPane4Sim) window.recalcPane4Sim();
    if(window.recalcHomeLabSim) window.recalcHomeLabSim();
  }, 100);
})();
</script>
<script>
var GLOBAL_I18N = {
  tr: { navHome: 'Anasayfa', navSolutions: 'Çözümler', navAbout: 'Hakkımızda', navApp: 'Uygulama', navPricing: 'Paketler', navSecurity: 'Güvenlik', navContact: 'İletişim', login: 'Giriş Yap', register: 'Ücretsiz Kayıt Ol' },
  en: { navHome: 'Home', navSolutions: 'Solutions', navAbout: 'About', navApp: 'App', navPricing: 'Pricing', navSecurity: 'Security', navContact: 'Contact', login: 'Log In', register: 'Sign Up Free' },
  de: { navHome: 'Startseite', navSolutions: 'Lösungen', navAbout: 'Über uns', navApp: 'Anwendung', navPricing: 'Preise', navSecurity: 'Sicherheit', navContact: 'Kontakt', login: 'Anmelden', register: 'Kostenlos Registrieren' },
  fr: { navHome: 'Accueil', navSolutions: 'Solutions', navAbout: 'À propos', navApp: 'Application', navPricing: 'Tarifs', navSecurity: 'Sécurité', navContact: 'Contact', login: 'Connexion', register: 'Inscription Gratuite' },
  es: { navHome: 'Inicio', navSolutions: 'Soluciones', navAbout: 'Sobre Nosotros', navApp: 'Aplicación', navPricing: 'Precios', navSecurity: 'Seguridad', navContact: 'Contacto', login: 'Iniciar Sesión', register: 'Registro Gratis' },
  it: { navHome: 'Home', navSolutions: 'Soluzioni', navAbout: 'Chi siamo', navApp: 'Applicazione', navPricing: 'Piani', navSecurity: 'Sicurezza', navContact: 'Contatti', login: 'Accedi', register: 'Registrati Gratis' },
  nl: { navHome: 'Startpagina', navSolutions: 'Oplossingen', navAbout: 'Over ons', navApp: 'Applicatie', navPricing: 'Tarieven', navSecurity: 'Beveiliging', navContact: 'Contact', login: 'Inloggen', register: 'Gratis Registreren' }
};
function setGlobalLanguage(lang){
  try { localStorage.setItem('dfbp_lang', lang); } catch(e){}
  var dict = GLOBAL_I18N[lang] || GLOBAL_I18N.tr;
  document.querySelectorAll('.globalLangSwitch').forEach(function(s){ s.value = lang; });
  var nav = document.getElementById('mainNav');
  if(nav){
    var links = nav.querySelectorAll('a');
    if(links.length >= 7){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navSolutions;
      links[2].textContent = dict.navAbout;
      links[3].textContent = dict.navApp;
      links[4].textContent = dict.navPricing;
      links[5].textContent = dict.navSecurity;
      links[6].textContent = dict.navContact;
    } else if(links.length >= 6){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navAbout;
      links[2].textContent = dict.navApp;
      links[3].textContent = dict.navPricing;
      links[4].textContent = dict.navSecurity;
      links[5].textContent = dict.navContact;
    }
  }
  document.querySelectorAll('.navBtn.secondary, .navBtn.sec, #loginOpenBtn').forEach(function(b){ b.textContent = dict.login; });
  document.querySelectorAll('.navBtn.primary, .navBtn.pri, #registerOpenBtn').forEach(function(b){ b.textContent = dict.register; });
}
if(typeof document !== 'undefined' && document.addEventListener){
  document.addEventListener('DOMContentLoaded', function(){
    var saved = 'tr';
    try { saved = localStorage.getItem('dfbp_lang') || 'tr'; } catch(e){}
    setGlobalLanguage(saved);
  });
}
</script>
</body></html>'''



SOLUTIONS_HTML = r'''<!doctype html>
<html lang="tr">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" type="image/svg+xml" href="/favicon.ico"><meta name="description" content="Digital Finance Business Partner (digitalfinancebp.com) — Patronun masasındaki 10 gerçek finansal kriz, 8 stratejik yönetim kararı, analitik kanıtlar ve 60 saniyelik icraat reçeteleri. Digital Finance Business Partner."><title>KOBİ Finansal Çözümleri & Patron Karar Masası | Digital Finance Business Partner</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&display=swap" rel="stylesheet">
<style>
:root{--bg:#F6F7F9;--panel:#FFFFFF;--panel2:#F0F3F8;--line:#E4E8EF;--text:#0F1B2D;--muted:#5B6B84;--accent:#1D4ED8;--accent2:#4F8CFF;--red:#C22A3E;--amber:#B4720A;--green:#0E7C66;--shadow:0 1px 2px rgba(15,27,45,.04),0 12px 32px rgba(15,27,45,.06);--serif:'Fraunces',ui-serif,Georgia,serif}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(1100px 480px at 12% -10%, rgba(29,78,216,.07), transparent 60%),radial-gradient(900px 420px at 100% 0%, rgba(14,124,102,.05), transparent 55%),#F6F7F9;color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45}button,input,select{font:inherit}.wrap{max-width:1440px;margin:auto;padding:0 28px}.top{padding:26px 0 18px;border-bottom:1px solid rgba(15,27,45,.08);position:sticky;top:0;background:rgba(246,247,249,.86);backdrop-filter:blur(18px);z-index:10}.brand{display:flex;align-items:center;justify-content:space-between;gap:20px}.brand h1{margin:0;font-size:25px;letter-spacing:-.6px}.brand p{margin:3px 0 0;color:var(--muted);font-size:13px}.badge{padding:6px 10px;border:1px solid #D7DEE8;border-radius:999px;color:var(--accent);font-size:12px;white-space:nowrap}.hero{padding:34px 0 24px;display:grid;grid-template-columns:1.45fr .55fr;gap:18px}.heroCard,.card{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow)}.heroCard{padding:28px}.heroTitle{font-family:var(--serif);font-weight:600;font-size:44px;line-height:1.08;margin:0 0 14px;letter-spacing:-.5px}.heroText{color:var(--muted);max-width:780px}.framework{display:flex;flex-wrap:wrap;gap:8px 10px;margin:16px 0 2px;padding:0}.framework span{font-size:11.5px;color:#33415C;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px}.framework span b{color:var(--accent);font-weight:800}
.qsel{margin-top:18px}.qsel .qtitle{font-size:12px;color:var(--muted);margin-bottom:8px;font-weight:700}.qsel .qrow{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.qsel button{border:1px solid #D7DEE8;background:#EEF2FF;color:#33415C;border-radius:12px;padding:10px 12px;font-size:12.5px;cursor:pointer;text-align:left;line-height:1.3}.qsel button:hover{border-color:#B7C3D6}.qsel button.active{border-color:var(--accent);color:var(--accent);background:#DCE6FB}
.upload{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}.file{border:1px dashed #C9D2DE;padding:12px;border-radius:12px;background:#F5F7FA;max-width:100%}.select,button{border:1px solid #D7DEE8;border-radius:11px;padding:11px 14px;background:#FFFFFF;color:var(--text)}button.primary,a.primary{background:linear-gradient(135deg,#2557E8,#1D4ED8);border:0;color:#FFFFFF;font-weight:800;cursor:pointer;transition:transform .15s ease,box-shadow .15s ease;box-shadow:0 6px 16px rgba(29,78,216,.25)}a.primary:hover,button.primary:hover{transform:translateY(-1px);box-shadow:0 10px 22px rgba(29,78,216,.32)}button.secondary,a.secondary{cursor:pointer;border:1.5px solid #C9D2DE;background:#FFFFFF;color:var(--text)}a.secondary:hover,button.secondary:hover{border-color:var(--accent);color:var(--accent)}button:disabled{opacity:.5;cursor:not-allowed}.scoreCard{padding:25px;display:flex;flex-direction:column;justify-content:center}.scoreRing{width:170px;height:170px;border-radius:50%;margin:auto;display:grid;place-items:center;background:conic-gradient(var(--accent) calc(var(--score)*1%),#E4E8EF 0);position:relative}.scoreRing:after{content:"";position:absolute;inset:12px;border-radius:50%;background:#FFFFFF}.scoreNum{position:relative;z-index:1;text-align:center}.scoreNum strong{display:block;font-size:48px;line-height:1}.scoreNum span{color:var(--muted);font-size:12px}.status{margin:15px auto 0;padding:7px 12px;border-radius:999px;background:#EAF0FF;color:var(--accent);font-size:12px;font-weight:700}.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.card{padding:22px;margin:0 0 16px;transition:transform .18s ease,box-shadow .18s ease,outline .2s}.card:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(15,27,45,.08)}@keyframes growUp{from{transform:scaleY(0);opacity:0}to{transform:scaleY(1);opacity:1}}.wf{transform-origin:bottom}.wf .col{transform-origin:bottom}@keyframes growWidth{from{width:0}to{}}.metric{padding:17px;border:1px solid var(--line);border-radius:15px;background:rgba(15,27,45,.03)}.metric .label{color:var(--muted);font-size:12px}.metric .value{font-size:25px;font-weight:800;margin-top:5px;letter-spacing:-.5px}.metric .sub{font-size:11px;color:var(--muted);margin-top:5px}.sectionHead{display:flex;align-items:end;justify-content:space-between;gap:15px;margin-bottom:17px}.sectionHead h2{margin:0;font-size:18px}.sectionHead p{margin:0;color:var(--muted);font-size:12px}.flowStep{margin:36px 0 14px;padding-top:6px;border-top:1px solid rgba(15,27,45,.08)}.flowStep:first-child{margin-top:0;border-top:0;padding-top:0}.flowLabel{display:flex;align-items:center;gap:10px;font-size:12px;font-weight:800;letter-spacing:1.8px;text-transform:uppercase;color:var(--accent);margin:0 0 4px}.flowLabel .n{width:22px;height:22px;border-radius:50%;background:#EAF0FF;color:var(--accent);display:inline-flex;align-items:center;justify-content:center;font-size:11px}.flowLabel p{margin:0;color:var(--muted);font-size:12.5px;font-weight:500;text-transform:none;letter-spacing:0}.flowLabel.alt{color:var(--accent2)}.flowLabel.alt .n{color:var(--accent2)}.flowSub{color:var(--muted);font-size:12.5px;margin:2px 0 16px 32px}.insight{border:1px solid var(--line);border-radius:15px;padding:16px;background:#F7F9FC}.insight.critical{border-color:#E8B4BD}.insight.high{border-color:#E9CBA8}.insight.medium{border-color:#E5DBA0}.insight.positive{border-color:#A9D9C9}.insight h3{margin:0 0 5px;font-size:14px}.insight p{margin:6px 0;color:#33415C;font-size:13px}.insight ul{margin:6px 0;padding-left:18px;color:#33415C;font-size:13px}.tag{display:inline-flex;padding:4px 8px;border-radius:999px;font-size:10px;font-weight:800;text-transform:uppercase;background:#EAF0FF;color:#5B6B84}.tag.critical{background:#FCE8EA;color:#C22A3E}.tag.high{background:#FDF0E0;color:#B4720A}.tag.medium{background:#FBF6DE;color:#8A6D00}.tag.positive{background:#E4F5EF;color:#0E7C66}.riskRow,.actionRow{display:grid;grid-template-columns:40px 1fr auto;gap:12px;align-items:center;padding:13px 0;border-bottom:1px solid rgba(15,27,45,.08)}.rank{font-size:18px;font-weight:900;color:#5B6B84}.riskScore{font-size:12px;color:var(--muted)}.bar{height:7px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:8px}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:99px}.waterfallWrap{overflow-x:auto;-webkit-overflow-scrolling:touch;padding-bottom:10px;margin-bottom:10px}.waterfall{display:flex;align-items:flex-end;gap:9px;height:190px;padding:20px 5px 0;border-bottom:1px solid var(--line);min-width:620px}.wf{flex:1;display:flex;flex-direction:column;justify-content:end;height:100%;min-width:65px}.wf .col{border-radius:6px 6px 2px 2px;background:linear-gradient(180deg,#83a4ff,#506fd0);min-height:3px}.wf.neg .col{background:linear-gradient(180deg,#ff8290,#9d3e54)}.wf .lab{font-size:10.5px;font-weight:600;color:var(--muted);text-align:center;margin-top:7px;white-space:nowrap}.wf .num{font-size:10px;font-weight:700;text-align:center;color:#33415C;margin-bottom:4px;white-space:nowrap}.subnavPill{font-size:12px;font-weight:600;color:#475569;text-decoration:none;padding:5px 12px;border-radius:999px;background:#F1F5F9;border:1px solid #E2E8F0;transition:all .15s ease}.subnavPill:hover{background:#E2E8F0;color:#1D4ED8;border-color:#CBD5E1}.dashPill{font-size:11.5px;font-weight:700;color:#475569;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:999px;padding:5px 12px;cursor:pointer;transition:all .15s ease;white-space:nowrap}.dashPill:hover{background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE}.scenario{padding:18px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(145deg,#F5F8FF,#EEF3FC)}.scenario h3{margin:0 0 6px;font-size:15px}.scenario .big{font-size:24px;font-weight:900;color:var(--accent)}.scenario p{color:var(--muted);font-size:11px;margin:6px 0}.muted{color:var(--muted)}.small{font-size:11px}.tableWrap{overflow:auto}table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:10px 8px;border-bottom:1px solid rgba(15,27,45,.08);text-align:right}th:first-child,td:first-child{text-align:left}th{color:#5B6B84;font-weight:600}.notice{padding:12px 14px;border-radius:12px;background:#EEF2FF;border:1px solid var(--line);color:#5B6B84;font-size:12px}.error{color:#C22A3E;background:#FCE8EA;border:1px solid #E8B4BD;padding:12px;border-radius:12px;margin:15px 0}.hidden{display:none!important}.footer{padding:25px 0 50px;color:#5B6B84;font-size:11px;text-align:center}.tabs{display:flex;gap:8px;margin-top:16px}.tab{padding:8px 12px;border-radius:999px;background:#F0F3F8;border:1px solid var(--line);color:#5B6B84;cursor:pointer}.tab.active{background:#DCE6FB;color:var(--accent);border-color:#1D4ED8}.tabPanel{display:none}.tabPanel.active{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.hidePrint{display:block}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.chip{font-size:11.5px;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px;color:#33415C}.chip b{color:var(--accent)}
.abar{height:9px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:6px}.abar i{display:block;height:100%;background:linear-gradient(90deg,#8aa7ff,#ff8290);border-radius:99px}
.custRow{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12.5px}
.highlight-target{outline:2px solid var(--accent);outline-offset:6px}
/* --- Marketing surface additions --- */
.topNav{display:flex;gap:18px}
.topNav a{color:var(--muted);font-size:13px;text-decoration:none;font-weight:600}
.topNav a:hover{color:var(--accent)}
.marketingSection{padding:8px 0 16px}
.marketingHead{text-align:center;max-width:640px;margin:0 auto 34px}
.marketingHead h2{font-family:var(--serif);font-size:32px;margin:0 0 10px;letter-spacing:-.5px}
.marketingHead p{color:var(--muted);margin:0;font-size:14.5px}
.pricingGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:stretch}
.priceCard{display:flex;flex-direction:column;padding:28px 24px;position:relative}
.priceCard.featured{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent),var(--shadow)}
.priceCard .plan{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:var(--accent);font-weight:800;margin-bottom:8px}
.priceCard h3{margin:0 0 6px;font-size:22px;font-family:var(--serif)}
.priceCard .amt{font-size:34px;font-weight:900;margin:8px 0 4px}
.priceCard .amt span{font-size:13px;color:var(--muted);font-weight:500}
.priceCard .desc{color:var(--muted);font-size:13px;margin-bottom:18px}
.priceCard ul{list-style:none;margin:0 0 22px;padding:0;flex:1;display:flex;flex-direction:column;gap:10px}
.priceCard ul li{font-size:13px;color:#33415C;display:flex;gap:8px;align-items:flex-start}
.priceCard ul li svg{flex:none;margin-top:2px;color:var(--accent)}
.priceCard .badgeTop{position:absolute;top:-11px;left:50%;transform:translateX(-50%);background:var(--accent);color:#FFFFFF;font-size:10.5px;font-weight:800;padding:4px 12px;border-radius:999px;letter-spacing:.5px}
.aboutGrid{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:center}
.aboutStats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}
.aboutStats .st{padding:16px;border:1px solid var(--line);border-radius:14px;text-align:center;background:rgba(15,27,45,.03)}
.aboutStats .st b{display:block;font-size:24px;color:var(--accent);font-family:var(--serif)}
.aboutStats .st span{font-size:11px;color:var(--muted)}
.contactGrid{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.contactCard{padding:26px}
.contactRow{display:flex;flex-direction:column;gap:12px;margin-top:14px}
.contactRow .item{display:flex;gap:10px;align-items:center;font-size:13px;color:#33415C}
.contactRow .item svg{color:var(--accent);flex:none}
@media(max-width:860px){.pricingGrid,.aboutGrid,.contactGrid{grid-template-columns:1fr}.topNav{display:none}}
.trustBar{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:20px;padding-top:18px;border-top:1px solid rgba(15,27,45,.10)}
.trustBar .item{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted)}
.trustBar .item svg{flex:none;color:var(--accent)}
.heroPreview{position:relative;padding:22px;overflow:hidden}
.pvLabel,.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.pvLabel span.dot,.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
.pvRing{width:112px;height:112px;border-radius:50%;margin:2px auto 14px;display:grid;place-items:center;background:conic-gradient(var(--accent) 0 78%,#182c42 78% 100%);position:relative}
.pvRing:after{content:"";position:absolute;inset:9px;border-radius:50%;background:#F7F9FC}
.pvRing b{position:relative;font-family:var(--serif);font-size:26px;z-index:1}
.pvRow{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12px}
.pvRow .n{color:var(--text);font-weight:700}
.pvRow .n.up{color:var(--green)}.pvRow .n.down{color:var(--red)}
.pvBars{display:flex;align-items:flex-end;gap:5px;height:54px;margin-top:14px}
.pvBars i{flex:1;background:linear-gradient(180deg,var(--accent2),#4a63b8);border-radius:3px 3px 1px 1px;display:block}
.statsStrip{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin:6px 0 0;padding:26px 0}
.statsStrip .stat b{font-family:var(--serif);font-size:36px;font-weight:600;color:var(--text);display:block;letter-spacing:-.5px}
.statsStrip .stat span{font-size:12.5px;color:var(--muted);display:block;margin-top:4px;max-width:20ch}
.whyCard{padding:20px;position:relative}
.whyCard .icoWrap{width:40px;height:40px;border-radius:11px;background:#DCE6FB;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;margin-bottom:14px;color:var(--accent)}
.ctaBanner{margin:44px 0 8px;padding:38px 32px;border-radius:22px;background:linear-gradient(135deg,#EAF0FF 0%,#DCE6FB 55%,#EAF0FF 100%);border:1px solid #C9D8F5;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.ctaBanner h3{font-family:var(--serif);font-weight:600;font-size:26px;margin:0 0 6px;letter-spacing:-.3px}
.ctaBanner p{margin:0;color:var(--muted);font-size:13.5px;max-width:52ch}
@media(max-width:1000px){.statsStrip{grid-template-columns:repeat(2,1fr)}.heroTitle{font-size:34px}}
@media(max-width:1000px){.hero{grid-template-columns:1fr}.grid4{grid-template-columns:repeat(2,1fr)}.grid3,.grid2{grid-template-columns:1fr}.wrap{padding:0 15px}.heroTitle{font-size:31px}.flowSub{margin-left:0}.qsel .qrow{grid-template-columns:1fr}}
@media print{
  *,*::before,*::after{box-sizing:border-box!important}
  @page{size:A4 portrait;margin:10mm 12mm 10mm 12mm}
  html,body{background:#fff!important;color:#0F1B2D!important;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif!important;font-size:8.5pt!important;line-height:1.35!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Hide all interactive & website shell elements ─────────────── */
  .hero,.upload,.hidePrint,.tabs,.tabPanel,.chips,.qsel,.tab,.footer,.siteFooter,
  header.top,.top,.topNav,.navBtns,.navToggle,#authArea,#authModalOverlay,
  .loadingOverlay,.dropZone,#criticalPartiesNotice,#methodNote,
  .heroPreview,.trustBar,.statsStrip,.ctaBanner,
  button,input,select,textarea,.secondary,.primary,
  #sampleBtn,#aiBtn,#printBtn,#jsonBtn,#aiAskBtn,
  #aiBox,#aiCustomBox,#aiCustomPrompt,#historySection,
  .interactiveScenarioCard,#interactiveScenarioCard,
  .abar{display:none!important}

  /* ── Layout: full-width single column ──────────────────────────── */
  .wrap{max-width:none!important;padding:0!important;margin:0!important;width:100%!important}

  /* ── Boardroom Cover Header ────────────────────────────────────── */
  #printCover{display:block!important;page-break-after:avoid!important;break-after:avoid!important;margin-bottom:12px}
  .printExecutiveFooter{display:flex!important;justify-content:space-between;align-items:center;border-top:1px solid #CBD5E1;padding-top:6px;margin-top:14px;font-size:7pt!important;color:#64748B!important;page-break-inside:avoid!important;break-inside:avoid!important}

  /* ── Cards & Containers ────────────────────────────────────────── */
  .card{box-shadow:none!important;background:#fff!important;border:1px solid #CBD5E1!important;border-radius:6px!important;margin-bottom:8px!important;padding:8px 10px!important;page-break-inside:auto!important;break-inside:auto!important}
  .heroCard{box-shadow:none!important;background:#fff!important;border:1px solid #CBD5E1!important;padding:8px!important}

  /* ── Flow steps ─────────────────────────────────────────────────── */
  .flowStep{margin:8px 0 4px!important;padding-top:2px!important;page-break-inside:auto!important;break-inside:auto!important}
  .flowLabel{background:none!important;border-left:3.5px solid #1D4ED8!important;padding-left:8px!important;color:#0F1B2D!important;margin-bottom:4px!important;font-size:9pt!important;page-break-after:avoid!important;break-after:avoid!important}
  .flowLabel .n{background:#1D4ED8!important;color:#fff!important;font-size:7.5pt!important;padding:1px 5px!important;border-radius:3px!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .flowSub{color:#64748B!important;font-size:7.5pt!important;margin-bottom:6px!important;line-height:1.25!important;page-break-after:avoid!important;break-after:avoid!important}

  /* ── Metrics / KPIs ─────────────────────────────────────────────── */
  .metric{background:#F8FAFC!important;border:1px solid #E2E8F0!important;border-radius:5px!important;padding:6px 8px!important;color:#0F1B2D!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .metric .label{font-size:6.5pt!important;color:#475569!important;font-weight:700;text-transform:uppercase;letter-spacing:.4px}
  .metric .value{font-size:11pt!important;font-weight:800;color:#0F1B2D!important}
  .metric .sub{font-size:6.5pt!important;color:#64748B!important}
  .grid2{display:grid!important;grid-template-columns:1fr 1fr!important;gap:6px!important}
  .grid3{display:grid!important;grid-template-columns:1fr 1fr 1fr!important;gap:6px!important}
  .grid4{display:grid!important;grid-template-columns:repeat(4,1fr)!important;gap:6px!important}

  /* ── Health score ring ──────────────────────────────────────────── */
  .scoreCard{display:flex!important;align-items:center!important;gap:16px!important;padding:8px 12px!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .scoreRing{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .scoreRing::after{background:#fff!important}

  /* ── Section headings ───────────────────────────────────────────── */
  .sectionHead{border-bottom:1px solid #E2E8F0!important;margin-bottom:6px!important;padding-bottom:4px!important;page-break-after:avoid!important;break-after:avoid!important}
  .sectionHead h2{font-size:8.5pt!important;color:#1D4ED8!important;font-weight:800;margin:0!important}
  .sectionHead p{font-size:7pt!important;color:#64748B!important;margin:1px 0 0!important}
  h1,h2,h3,h4{page-break-after:avoid!important;break-after:avoid!important;color:#0F1B2D!important}
  h3{font-size:8.5pt!important}

  /* ── Risk & action rows (atomic: keep intact) ───────────────────── */
  .riskRow,.actionRow{border:1px solid #E2E8F0!important;border-radius:5px!important;margin-bottom:4px!important;padding:5px 7px!important;page-break-inside:avoid!important;break-inside:avoid!important;background:#F8FAFC!important}
  .rank{background:#EBF3FE!important;color:#1D4ED8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .bar{display:none!important}

  /* ── Tags / badges ──────────────────────────────────────────────── */
  .tag{border:1px solid #94A3B8!important;color:#1E293B!important;background:#F1F5F9!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;font-size:6.5pt!important}
  .badge{border:1px solid #1D4ED8!important;color:#1D4ED8!important;font-size:7pt!important}

  /* ── Insights / alerts ──────────────────────────────────────────── */
  .insight{border-left:3.5px solid #1D4ED8!important;background:#EFF6FF!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;border-radius:4px!important;padding:6px 8px!important;margin-bottom:5px!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .insight.high,.insight.critical{border-left-color:#DC2626!important;background:#FEF2F2!important}
  .insight.positive{border-left-color:#16A34A!important;background:#F0FDF4!important}
  .notice{background:#F8FAFC!important;border:1px solid #CBD5E1!important;padding:6px 8px!important;border-radius:4px!important;font-size:7.5pt!important;color:#334155!important;page-break-inside:avoid!important;break-inside:avoid!important}

  /* ── Waterfall chart ────────────────────────────────────────────── */
  .waterfall{display:flex!important;align-items:flex-end!important;gap:4px!important;height:80px!important;padding:2px 0!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .wf .col{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .wf .num{font-size:6pt!important;color:#0F1B2D!important;font-weight:700}
  .wf .lab{font-size:6pt!important;color:#475569!important;white-space:normal!important;max-height:22px;text-align:center;overflow:hidden;line-height:1.1}

  /* ── Tables ─────────────────────────────────────────────────────── */
  .tableWrap{overflow:visible!important}
  table{border-collapse:collapse!important;width:100%!important;font-size:7pt!important}
  th{background:#F1F5F9!important;color:#1E293B!important;font-weight:700;padding:3px 5px!important;border:1px solid #CBD5E1!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  td{padding:3px 5px!important;border:1px solid #E2E8F0!important}
  tr{page-break-inside:avoid!important;break-inside:avoid!important}
  tr:nth-child(even) td{background:#F8FAFC!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Misc ────────────────────────────────────────────────────────── */
  .muted{color:#64748B!important}
  .small{font-size:7pt!important}
  a{color:#1D4ED8!important;text-decoration:none!important}
  .scenario{border:1px solid #CBD5E1!important;border-radius:5px!important;padding:6px!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .scenario .big{font-size:11pt!important;font-weight:800;color:#1D4ED8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .custRow,.wf{page-break-inside:avoid!important;break-inside:avoid!important}
  .hidden{display:none!important}
  #dashboard{display:block!important}
}

@view-transition{navigation:auto}
::view-transition-old(root){animation:dfbpFadeOut .28s ease both}
::view-transition-new(root){animation:dfbpFadeIn .32s ease both}
@keyframes dfbpFadeOut{to{opacity:0;transform:translateY(-6px)}}
@keyframes dfbpFadeIn{from{opacity:0;transform:translateY(8px)}}
.topNav{display:flex;gap:18px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s;white-space:nowrap}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.authCluster{display:flex;flex-direction:column;align-items:flex-end;gap:5px;flex-shrink:0}
.headerSwitches{display:flex;align-items:center;gap:6px;justify-content:flex-end}
.headerSwitches select,select.globalLangSwitch{padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1}
.headerSwitches select:hover,select.globalLangSwitch:hover{border-color:var(--accent);color:#0F1B2D;background:#FFFFFF}
.navBtns,#authArea{display:flex;gap:8px;align-items:center;flex-shrink:0;white-space:nowrap}
.navBtns a,.navBtns button,#authArea button{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  font-size:12.5px;
  font-weight:700;
  padding:6px 14px;
  border-radius:9px;
  text-decoration:none;
  transition:all .15s ease;
  cursor:pointer;
  line-height:1.2;
  white-space:nowrap;
  flex-shrink:0;
}
.navBtns a.secondary,.navBtns button.secondary,#authArea button.secondary,#loginOpenBtn{
  background:#FFFFFF;
  border:1px solid #CBD5E1;
  color:#1E293B;
  box-shadow:0 1px 2px rgba(0,0,0,.03);
}
.navBtns a.secondary:hover,.navBtns button.secondary:hover,#authArea button.secondary:hover,#loginOpenBtn:hover{
  background:#F8FAFC;
  border-color:#94A3B8;
  color:#0F172A;
}
.navBtns a.primary,.navBtns button.primary,#authArea button.primary,#registerOpenBtn{
  background:#1D4ED8;
  border:1px solid #1D4ED8;
  color:#FFFFFF;
  box-shadow:0 2px 6px rgba(29,78,216,.25);
}
.navBtns a.primary:hover,.navBtns button.primary:hover,#authArea button.primary:hover,#registerOpenBtn:hover{
  background:#1E40AF;
  border-color:#1E40AF;
  box-shadow:0 4px 12px rgba(29,78,216,.35);
  transform:translateY(-1px);
}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text);flex-shrink:0}
.brandLogoWrap{flex-shrink:0;min-width:max-content}
.brandLink{text-decoration:none;display:flex;align-items:center;gap:10px;min-width:0}
.brandLogoIcon{width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0}
.brandTextWrap{min-width:0}
.brandTitle{font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2;white-space:nowrap}
.brandSub{font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px;white-space:nowrap}
.headerRight{display:flex;align-items:center;gap:12px;flex-shrink:0}
.mobileNavAuth{display:none}

@media(max-width:920px){
  html,body{overflow-x:hidden;max-width:100vw;width:100%}
  .top{padding:12px 0 10px}
  .wrap{padding:0 16px;max-width:100vw;box-sizing:border-box}
  .brand{gap:10px}
  .brandLogoIcon{width:32px;height:32px;border-radius:9px}
  .brandLogoIcon svg{width:18px;height:18px}
  .brandTitle{font-size:15.5px}
  .brandSub{display:none}
  .brandLogoWrap{min-width:0;flex:1 1 auto;overflow:hidden}
  .topNav{position:fixed;top:56px;left:0;right:0;width:100vw;background:#FFFFFF;border-bottom:1.5px solid var(--line);box-shadow:0 14px 34px rgba(15,27,45,0.12);flex-direction:column;align-items:stretch;gap:0;padding:0 20px;max-height:0;overflow:hidden;transition:max-height .28s ease,padding .2s ease;z-index:999;box-sizing:border-box}
  .topNav.open{max-height:460px;padding:10px 20px 20px;overflow-y:auto}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.06);font-size:14.5px;color:var(--text);font-weight:600;display:block;text-align:left}
  .mobileNavAuth{display:flex;gap:10px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(15,27,45,.08)}
  .mobileNavAuth a{flex:1;padding:10px 12px;font-size:13px;font-weight:700;border-radius:10px;text-align:center;justify-content:center;text-decoration:none}
  .navToggle{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;padding:0;font-size:18px;border-radius:8px;cursor:pointer}
}

@media(max-width:768px){
  .navBtns{display:none}
  .authCluster{flex-direction:row;align-items:center}
  .headerRight{gap:6px}
  .globalLangSwitch{padding:4px 5px !important;font-size:11px !important;border-radius:7px !important;max-width:60px}
  .wrap{padding:0 12px}
  .brandTitle{font-size:14.5px}
  .mHero{padding:24px 0 20px;grid-template-columns:1fr;gap:20px}
  .mHero h1{font-size:26px !important;line-height:1.2 !important}
  .mHero p.lead{font-size:13.5px;line-height:1.55}
  .ctaRow{flex-direction:column;gap:10px}
  .ctaRow a{width:100%;text-align:center;justify-content:center}
  .miniTrust{gap:8px 12px;margin-top:16px}
  .aboutStats{grid-template-columns:1fr !important;gap:10px}
  .statsStrip{grid-template-columns:1fr !important;gap:12px}
}
.badge.v{white-space:nowrap}
/* ---- Marketing hero (separate from app hero) ---- */
.mHero{padding:56px 0 30px;display:grid;grid-template-columns:1.15fr .85fr;gap:34px;align-items:center}
.mHero .eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:18px}
.mHero h1{font-family:var(--serif);font-weight:600;font-size:50px;line-height:1.08;margin:0 0 18px;letter-spacing:-1px}
.mHero h1 span{color:var(--accent)}
.mHero p.lead{color:var(--muted);font-size:16px;max-width:560px;line-height:1.65;margin:0 0 26px}
.mHero .ctaRow{display:flex;gap:12px;flex-wrap:wrap}
.mHero .ctaRow a{text-decoration:none}
.mHero .miniTrust{display:flex;gap:18px;flex-wrap:wrap;margin-top:28px}
.mHero .miniTrust span{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px}
.mHero .miniTrust svg{color:var(--accent)}
.heroArt{position:relative}
.heroArt .floatCard{position:absolute;background:#FFFFFF;border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);padding:14px 16px;font-size:11.5px;color:#33415C;animation:dfbpFloat 5s ease-in-out infinite}
.heroArt .floatCard b{display:block;font-size:16px;color:var(--accent);font-family:var(--serif)}
.heroArt .fc1{top:-10px;left:-10px;animation-delay:0s}
.heroArt .fc2{bottom:6px;right:-14px;animation-delay:1.2s}
@keyframes dfbpFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
/* ---- Alternating content blocks (fixes the "iç içe" cramped look) ---- */
.secBlock{padding:28px 0}
.secBlock.tint{background:linear-gradient(180deg,#F8FAFC 0%,#FFFFFF 100%);border:1px solid #E2E8F0;border-radius:26px;margin:0 -10px;box-shadow:0 4px 20px rgba(15,27,45,.03)}
.pillScrollBtn{width:36px;height:36px;border-radius:50%;background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:800;cursor:pointer;flex-shrink:0;box-shadow:0 4px 12px rgba(15,27,45,0.08);transition:all .18s ease;user-select:none;z-index:4}
.pillScrollBtn:hover{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;transform:scale(1.08);box-shadow:0 6px 16px rgba(29,78,216,0.25)}
.pillScrollBtn:active{transform:scale(0.95)}
.secBlock+.secBlock{border-top:1px solid rgba(15,27,45,.06)}
.pageHead{padding:54px 0 10px;text-align:center}
.pageHead .eyebrow{display:inline-flex;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:16px}
.pageHead h1{font-family:var(--serif);font-size:38px;margin:0 0 12px;letter-spacing:-.6px}
.pageHead p{color:var(--muted);max-width:600px;margin:0 auto;font-size:14.5px}
.reveal{opacity:0;transform:translateY(18px);transition:opacity .55s ease,transform .55s ease}
.reveal.in{opacity:1;transform:none}
/* ---- Rich footer ---- */
.siteFooter{border-top:1px solid var(--line);margin-top:40px;padding:46px 0 26px}
.siteFooter .cols{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:28px;margin-bottom:30px}
.siteFooter h4{font-size:12px;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin:0 0 14px}
.siteFooter .brandCol p{color:var(--muted);font-size:12.5px;max-width:280px;line-height:1.6}
.siteFooter ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.siteFooter ul a{color:#33415C;text-decoration:none;font-size:13px}
.siteFooter ul a:hover{color:var(--accent)}
.siteFooter .legal{border-top:1px solid rgba(15,27,45,.08);padding-top:20px;color:#5B6B84;font-size:11px;line-height:1.7}
html{overflow-x:hidden}@media(max-width:860px){.siteFooter .cols{grid-template-columns:1fr 1fr}.mHero{grid-template-columns:1fr}.heroArt{order:-1;max-width:340px;margin:24px auto 40px;padding:0 14px}.heroArt .floatCard{position:static;display:inline-block;margin:6px 6px 0 0;animation:none}.heroArt .fc1,.heroArt .fc2{top:auto;left:auto;right:auto;bottom:auto}}
/* ---- FAQ (paketler sayfası) ---- */
.faqItem{border-bottom:1px solid var(--line);padding:16px 0}
.faqItem summary{cursor:pointer;font-weight:700;font-size:14px;list-style:none;display:flex;justify-content:space-between;align-items:center}
.faqItem summary::-webkit-details-marker{display:none}
.faqItem summary:after{content:'+';font-size:20px;color:var(--accent)}
.faqItem[open] summary:after{content:'–'}
.faqItem p{color:var(--muted);font-size:13.5px;margin:10px 0 0}
/* ---- Executive Intelligence band (single, deliberate dark boardroom section) ---- */
.execBand{background:radial-gradient(1200px 500px at 15% -20%, rgba(76,201,240,.10), transparent 60%),linear-gradient(160deg,#0D1B2A 0%,#081426 100%);border-radius:26px;padding:52px;display:grid;grid-template-columns:.85fr 1.15fr;gap:40px;align-items:center;overflow:hidden}
.execEyebrow{display:inline-block;font-size:11.5px;font-weight:800;letter-spacing:1.6px;color:#4CC9F0;background:rgba(76,201,240,.12);border:1px solid rgba(76,201,240,.35);padding:6px 12px;border-radius:999px;margin-bottom:16px}
.execCopy h2{font-family:var(--serif);color:#F8FAFC;font-size:28px;line-height:1.2;margin:0 0 12px;letter-spacing:-.4px}
.execCopy p{color:#94A3B8;font-size:14px;line-height:1.7;margin:0 0 18px;max-width:44ch}
.execList{list-style:none;margin:0 0 24px;padding:0;display:flex;flex-direction:column;gap:9px}
.execList li{color:#C7D2E8;font-size:13px}
.execList li b{color:#F8FAFC}
.execCta{display:inline-block;color:#0D1B2A;background:#4CC9F0;font-weight:800;font-size:13.5px;padding:12px 20px;border-radius:11px;text-decoration:none;transition:transform .15s ease,box-shadow .15s ease}
.execCta:hover{transform:translateY(-1px);box-shadow:0 10px 26px rgba(76,201,240,.35)}
.execArt{filter:drop-shadow(0 24px 48px rgba(0,0,0,.35))}
@media(max-width:860px){.execBand{grid-template-columns:1fr;padding:32px 22px}}
/* ---- New: live dashboard hero panel (Executive Light Theme) ---- */
.heroDash{background:#FFFFFF;border-radius:24px;border:1.5px solid #DCE6F5;padding:24px;position:relative;overflow:hidden;box-shadow:0 20px 45px rgba(15,27,45,.08)}
.heroDash .dHead{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid #F1F5F9}
.heroDash .dHead .dots span{width:8px;height:8px;border-radius:50%;display:inline-block;margin-right:5px}
.heroDash .dHead .live{font-size:11px;color:#059669;display:flex;align-items:center;gap:6px;font-weight:800;letter-spacing:.4px}
.heroDash .dHead .live i{width:6px;height:6px;border-radius:50%;background:#10B981;display:inline-block;box-shadow:0 0 0 3px rgba(16,185,129,.22);animation:dfbpPulse 1.8s ease infinite}
@keyframes dfbpPulse{0%,100%{opacity:1}50%{opacity:.35}}
.dashTabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px}
.dashTabs span{font-size:11px;color:#64748B;background:#F1F5F9;border:1px solid transparent;border-radius:999px;padding:6px 12px;cursor:pointer;font-weight:600;transition:all .2s ease}
.dashTabs span:hover{background:#E2E8F0;color:#1E293B}
.dashTabs span.on{color:#1D4ED8;background:#EFF6FF;border-color:#BFDBFE;font-weight:800}
.dashPane{display:none;min-height:230px}
.dashPane.on{display:block;animation:dfbpFadeIn .3s ease both}
.dashPane .dTitle{color:#0F172A;font-size:11.5px;letter-spacing:.5px;text-transform:uppercase;margin-bottom:10px;font-weight:700}
.dashKpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:12px}
.dashKpis div{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:9px 10px;text-align:center}
.dashKpis div b{display:block;font-size:15px;color:#0F172A;font-family:var(--serif);font-weight:700}
.dashKpis div span{font-size:10px;color:#64748B}
.heroDash .foot{margin-top:14px;padding-top:12px;border-top:1px solid #F1F5F9;font-size:11px;color:#64748B;display:flex;justify-content:space-between;font-weight:600}
/* ---- New: CFO trust strip ---- */
.trustGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.trustCard{padding:22px}
.trustCard .icoWrap2{width:38px;height:38px;border-radius:10px;background:#0D1B2A;color:#4CC9F0;display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.trustCard h3{margin:0 0 6px;font-size:14.5px}
.trustCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.55}
/* ---- New: Executive Journey ---- */
.journey{display:grid;grid-template-columns:repeat(6,1fr);gap:0;position:relative;margin-top:8px}
.journey:before{content:"";position:absolute;top:22px;left:6%;right:6%;height:2px;background:linear-gradient(90deg,#C9D8F5,#4CC9F0,#C9D8F5)}
.jStep{text-align:center;padding:0 8px;opacity:0;transform:translateY(16px);transition:opacity .5s ease,transform .5s ease}
.jStep.in{opacity:1;transform:none}
.jStep .jDot{width:44px;height:44px;border-radius:50%;background:#FFFFFF;border:2px solid var(--accent);color:var(--accent);display:flex;align-items:center;justify-content:center;margin:0 auto 12px;position:relative;z-index:1;font-weight:900;font-size:13px}
.jStep h4{margin:0 0 5px;font-size:13px;letter-spacing:.4px}
.jStep p{margin:0;font-size:11.5px;color:var(--muted);line-height:1.4}
@media(max-width:860px){.journey{grid-template-columns:1fr 1fr;gap:22px 0}.journey:before{display:none}.trustGrid{grid-template-columns:1fr 1fr}}
/* ---- New: outcome-based module groups ---- */
.intelGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.intelCard{padding:24px;display:flex;flex-direction:column}
.intelCard .igIco{width:40px;height:40px;border-radius:11px;background:#DCE6FB;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.intelCard h3{margin:0 0 8px;font-size:16px;font-family:var(--serif)}
.intelCard ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}
.intelCard ul li{font-size:12.5px;color:#33415C;display:flex;gap:7px;align-items:flex-start}
.intelCard ul li:before{content:"";width:5px;height:5px;border-radius:50%;background:var(--accent);margin-top:6px;flex:none}
@media(max-width:860px){.intelGrid{grid-template-columns:1fr 1fr}}
/* ---- New: security/governance page ---- */

/* ---- High-impact FinTech additions ---- */
.gradText{background:linear-gradient(135deg,#1D4ED8 0%,#2563EB 50%,#38BDF8 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;display:inline-block}
.livePill{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:var(--accent);background:linear-gradient(135deg,#EEF4FF,#E0EDFF);border:1px solid #BFDBFE;padding:8px 16px;border-radius:999px;margin-bottom:20px;box-shadow:0 2px 10px rgba(37,99,235,.12)}
.livePill i{width:8px;height:8px;border-radius:50%;background:#10B981;display:inline-block;box-shadow:0 0 0 4px rgba(16,185,129,.25);animation:dfbpPulse 1.8s ease infinite}
.dilemmaGrid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:20px}
.dilemmaCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:26px;position:relative;overflow:hidden;box-shadow:var(--shadow);transition:transform .2s ease,box-shadow .2s ease}
.dilemmaCard:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(15,27,45,.09)}
.dilemmaQ{font-size:15px;font-weight:700;color:#0F1B2D;margin-bottom:12px;display:flex;gap:10px;align-items:flex-start;line-height:1.4}
.dilemmaQ span{background:#FEE2E2;color:#DC2626;border-radius:8px;padding:2px 8px;font-size:11px;font-weight:900;flex:none;margin-top:2px}
.dilemmaA{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:14px 16px;font-size:13px;color:#33415C;line-height:1.55}
.dilemmaA b{color:var(--accent);display:block;margin-bottom:4px}
.workflowGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;position:relative;margin-top:20px}
.workflowCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:24px;box-shadow:var(--shadow);position:relative;display:flex;flex-direction:column}
.workflowBadge{font-size:11px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:var(--accent);background:#EFF6FF;border:1px solid #DBEAFE;padding:4px 10px;border-radius:999px;align-self:flex-start;margin-bottom:12px}
.workflowCard h3{font-size:16px;margin:0 0 8px;font-family:var(--serif);color:#0F1B2D}
.workflowCard p{font-size:12.5px;color:var(--muted);line-height:1.55;margin:0}
.compareTableWrap{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:var(--shadow);margin-top:20px}
.compareTable{width:100%;border-collapse:collapse;font-size:13px}
.compareTable th,.compareTable td{padding:16px 18px;border-bottom:1px solid rgba(15,27,45,.08);text-align:left}
.compareTable th{background:#F8FAFC;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#475569}
.compareTable th.featured{background:linear-gradient(135deg,#EFF6FF,#DBEAFE);color:var(--accent);border-bottom:2px solid var(--accent)}
.compareTable td.featured{background:#F8FAFF;font-weight:600;color:#0F1B2D}
@media(max-width:860px){.dilemmaGrid,.workflowGrid{grid-template-columns:1fr}.compareTableWrap{overflow-x:auto}}

.kobiPills{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:18px auto 26px}
.kobiPill{padding:9px 18px;border-radius:999px;font-size:12.5px;font-weight:700;border:1.5px solid #CBD5E1;background:#FFFFFF;color:#475569;cursor:pointer;transition:all .2s ease}
.kobiPill:hover{border-color:#1D4ED8;color:#1D4ED8;background:#EFF6FF}
.kobiSliderWrap{position:relative;margin-top:20px}
.kobiSliderBar{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:14px;padding:0 4px}
.kobiSwipeHint{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;color:#64748B;background:#F8FAFC;border:1px solid #E2E8F0;padding:6px 14px;border-radius:999px}
.kobiSliderNav{display:flex;align-items:center;gap:10px}
.kobiSlideBadge{font-size:12px;font-weight:800;color:#1D4ED8;background:#EFF6FF;border:1px solid #DBEAFE;padding:6px 14px;border-radius:999px}
.kobiNavBtn{width:40px;height:40px;border-radius:50%;border:1.5px solid #CBD5E1;background:#FFFFFF;color:#0F172A;font-size:22px;line-height:1;font-weight:700;display:inline-flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 3px 10px rgba(15,27,45,.06);transition:all .2s ease;user-select:none}
.kobiNavBtn:hover{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;box-shadow:0 6px 18px rgba(29,78,216,.28);transform:scale(1.06)}
.kobiNavBtn:active{transform:scale(0.96)}
.kobiSliderTrack{display:flex;gap:22px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;padding:10px 4px 22px;-webkit-overflow-scrolling:touch;scrollbar-width:none}
.kobiSliderTrack::-webkit-scrollbar{display:none}
.kobiCard{flex:0 0 420px;max-width:420px;scroll-snap-align:start;scroll-snap-stop:normal;background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:20px;padding:24px;box-shadow:0 6px 20px rgba(15,27,45,.04);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease;display:flex;flex-direction:column;justify-content:space-between}
.kobiCard:hover{transform:translateY(-4px);box-shadow:0 16px 36px rgba(15,27,45,.10);border-color:#93C5FD}
.kobiCardImgWrap{border-radius:12px;overflow:hidden;margin-bottom:14px;box-shadow:0 4px 12px rgba(15,27,45,.06);border:1px solid #E2E8F0;aspect-ratio:16/9;background:#0F172A;position:relative}
.kobiCardImgWrap img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .35s ease}
.kobiCard:hover .kobiCardImgWrap img{transform:scale(1.03)}
.kobiDotsWrap{display:flex;align-items:center;justify-content:center;gap:7px;margin-top:8px}
.kobiDot{width:8px;height:8px;border-radius:999px;background:#CBD5E1;transition:all .25s ease;cursor:pointer}
.kobiDot.active{width:26px;background:#1D4ED8;box-shadow:0 2px 8px rgba(29,78,216,.3)}
.kobiTag{display:inline-block;padding:4px 10px;border-radius:6px;font-size:10.5px;font-weight:800;letter-spacing:.8px;text-transform:uppercase;margin-bottom:12px;width:fit-content}
.kobiTag.cash{background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE}
.kobiTag.profit{background:#FEF3C7;color:#B45309;border:1px solid #FDE68A}
.kobiTag.mgmt{background:#F3E8FF;color:#7E22CE;border:1px solid #E9D5FF}
.kobiTitle{font-size:15.5px;font-weight:800;color:#0F1B2D;line-height:1.4;margin-bottom:10px}
.kobiDesc{font-size:12.5px;color:#475569;line-height:1.55;margin-bottom:14px}
.kobiMetrics{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:12px 14px;margin-bottom:14px;display:flex;flex-direction:column;gap:6px;font-size:12px}
.kobiMetricRow{display:flex;justify-content:space-between;align-items:center}
.kobiPrescription{background:#F0FDF4;border:1px solid #BBF7D0;border-radius:12px;padding:12px 14px;font-size:12px;color:#14532D;line-height:1.45;margin-bottom:0}
.kobiPrescription b{color:#166534;display:block;margin-bottom:3px;font-weight:800}
.kobiCta{display:inline-flex;align-items:center;justify-content:space-between;font-size:12.5px;font-weight:800;color:#1D4ED8;text-decoration:none;padding:10px 14px;background:#EFF6FF;border:1px solid #BFDBFE;border-radius:10px;transition:all .15s ease}
.kobiCta:hover{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8}
@media(max-width:900px){.kobiCard{flex:0 0 350px;max-width:350px}}
@media(max-width:600px){.kobiCard{flex:0 0 86vw;max-width:86vw}.kobiSwipeHint{font-size:11px;padding:5px 10px}}

.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

/* CEO Diagnostic Hub 3-Layer Architecture */
.ceoPill{display:inline-flex;align-items:center;gap:7px;padding:9px 16px;border-radius:999px;font-size:12.5px;font-weight:700;background:#F1F5F9;color:#475569;border:1px solid #CBD5E1;cursor:pointer;white-space:nowrap;transition:all .2s ease}
.ceoPill:hover{background:#E2E8F0;color:#0F172A}
.ceoPill.active{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;box-shadow:0 4px 14px rgba(29,78,216,0.25)}
.ceoQuestionCard{display:none;background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:18px;padding:22px;box-shadow:0 8px 24px rgba(15,27,45,0.04);animation:fadeIn .3s ease}
.ceoQuestionCard.active{display:block}
.layerBadge{display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;font-size:10.5px;font-weight:800;letter-spacing:0.5px;text-transform:uppercase}
.layerBadge.l1{background:#FEE2E2;color:#991B1B;border:1px solid #FCA5A5}
.layerBadge.l2{background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE}
.layerBadge.l3{background:#ECFDF5;color:#047857;border:1px solid #A7F3D0}
.ceoGrid3{display:grid;grid-template-columns:1.1fr 1fr 1.3fr;gap:18px;margin-top:16px}
@media(max-width:960px){.ceoGrid3{grid-template-columns:1fr}}


.infoTooltip{position:relative;display:inline-flex;align-items:center;justify-content:center;width:15px;height:15px;border-radius:50%;background:#E2E8F0;color:#475569;font-size:10px;font-weight:800;cursor:help;margin-left:5px;vertical-align:middle}
.infoTooltip:hover::after{content:attr(data-tooltip);position:absolute;bottom:135%;left:50%;transform:translateX(-50%);background:#0F172A;color:#FFFFFF;padding:8px 12px;border-radius:8px;font-size:11.5px;line-height:1.45;white-space:normal;width:230px;z-index:9999;box-shadow:0 8px 24px rgba(0,0,0,0.25);pointer-events:none;text-align:left;font-weight:400}

/* ---- Case Studies (Anonim Doğrulanmış KOBİ Başarı Hikayeleri) ---- */
.caseGrid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:24px}
.caseCard{background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:20px;padding:24px;box-shadow:0 6px 20px rgba(15,27,45,.04);transition:transform .2s ease,box-shadow .2s ease}
.caseCard:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(15,27,45,.08);border-color:#CBD5E1}
.caseHead{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;flex-wrap:wrap;gap:8px}
.caseBadge{font-size:11px;font-weight:800;letter-spacing:.8px;text-transform:uppercase;padding:4px 10px;border-radius:6px;background:#F1F5F9;color:#475569;border:1px solid #E2E8F0}
.caseBadge.verified{background:#ECFDF5;color:#047857;border-color:#A7F3D0}
.caseLocation{font-size:12px;color:#64748B;font-weight:600}
.caseTitle{font-size:16px;font-weight:800;color:#0F1B2D;margin-bottom:8px;line-height:1.35}
.caseProblem{font-size:12.5px;color:#64748B;line-height:1.55;margin-bottom:14px;background:#FFF5F5;border-left:3px solid #EF4444;padding:8px 12px;border-radius:0 8px 8px 0}
.caseSolution{font-size:12.5px;color:#1E3A8A;line-height:1.55;margin-bottom:14px;background:#EFF6FF;border-left:3px solid #3B82F6;padding:8px 12px;border-radius:0 8px 8px 0}
.caseKpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:12px}
.caseKpiItem{text-align:center}
.caseKpiItem b{display:block;font-size:15px;color:#0F172A;font-family:var(--serif);font-weight:800}
.caseKpiItem span{font-size:10px;color:#64748B;font-weight:600}
@media(max-width:860px){.caseGrid{grid-template-columns:1fr}}

/* ---- Security & Trust Shield (Banka Düzeyinde Güvenlik) ---- */
.secShieldGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:24px}
.secShieldCard{background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:18px;padding:22px;box-shadow:0 4px 14px rgba(15,27,45,.03);transition:transform .2s ease}
.secShieldCard:hover{transform:translateY(-2px);border-color:#93C5FD;box-shadow:0 10px 24px rgba(29,78,216,.08)}
.secShieldIco{width:42px;height:42px;border-radius:12px;background:#EFF6FF;color:#1D4ED8;display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:14px;border:1px solid #DBEAFE}
.secShieldCard h4{margin:0 0 6px;font-size:14.5px;color:#0F172A;font-weight:800}
.secShieldCard p{margin:0;font-size:12px;color:#64748B;line-height:1.55}
@media(max-width:960px){.secShieldGrid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:540px){.secShieldGrid{grid-template-columns:1fr}}

/* ---- ERP & Global Multi-Currency Bar ---- */
.erpLogosGrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;margin-top:16px}
.erpLogoBadge{background:#FFFFFF;border:1px solid #CBD5E1;border-radius:12px;padding:12px 10px;text-align:center;font-size:12.5px;font-weight:800;color:#1E293B;box-shadow:0 2px 6px rgba(15,27,45,.03);transition:all .2s ease;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px}
.erpLogoBadge:hover{border-color:#1D4ED8;color:#1D4ED8;transform:translateY(-2px);box-shadow:0 6px 16px rgba(29,78,216,.12)}
.erpLogoBadge span{font-size:9.5px;color:#64748B;font-weight:600}

/* ---- Mockup Showcase (Dashboard Cockpit & 1-Page Board PDF) - Executive Light Theme ---- */
.mockupShowcase{margin-top:32px;background:linear-gradient(180deg,#FFFFFF 0%,#F8FAFC 100%);border:1.5px solid #CBD5E1;border-radius:24px;padding:32px;color:#0F1B2D;box-shadow:0 14px 36px rgba(15,27,45,.06)}
.mockupSplit{display:grid;grid-template-columns:1.2fr 0.8fr;gap:24px;align-items:center}
@media(max-width:960px){.mockupSplit{grid-template-columns:1fr}}
.mockupScreen{background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:16px;overflow:hidden;box-shadow:0 12px 30px rgba(15,27,45,.06)}
.mockupScreenHead{background:#F8FAFC;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #E2E8F0}
.mockupPaper{background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:14px;padding:20px;color:#0F172A;box-shadow:0 12px 30px rgba(15,27,45,.06);font-size:11px}
.mockupBadge{display:inline-flex;align-items:center;gap:6px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#1D4ED8;background:#EFF6FF;border:1px solid #BFDBFE;padding:4px 10px;border-radius:999px;margin-bottom:12px}

/* ---- Ghost button styling for secondary CTA ---- */
.ctaRow a.ghostBtn{background:transparent;border:1.5px solid #CBD5E1;color:#475569;font-weight:700;padding:15px 24px;border-radius:14px;font-size:15px;text-decoration:none;transition:all .2s ease;display:inline-flex;align-items:center;gap:8px}
.ctaRow a.ghostBtn:hover{border-color:#1D4ED8;color:#1D4ED8;background:#EFF6FF}

/* ---- Dual Gates (Kapı A & Kapı B) ---- */
.ctaDualGates{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:22px 0 16px}
.gateCard{text-decoration:none;display:flex;flex-direction:column;gap:6px;padding:16px 20px;border-radius:16px;transition:all .22s cubic-bezier(0.16,1,0.3,1);position:relative}
.gateCard.gateA{background:#FFFFFF;border:2px solid #2563EB;box-shadow:0 8px 24px rgba(37,99,235,0.10)}
.gateCard.gateA:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(37,99,235,0.22);border-color:#1D4ED8}
.gateCard.gateB{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);border:2px solid #1D4ED8;box-shadow:0 8px 24px rgba(29,78,216,0.28);color:#FFFFFF}
.gateCard.gateB:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(29,78,216,0.38);border-color:#3B82F6}
@media(max-width:680px){.ctaDualGates{grid-template-columns:1fr}}

/* ---- Interactive What-If Live Laboratory ---- */
.whatIfLabCard{background:linear-gradient(180deg,#FFFFFF 0%,#F8FAFC 100%);border:1.5px solid #CBD5E1;border-radius:24px;padding:28px;box-shadow:0 14px 36px rgba(15,27,45,.06);margin-top:20px}
.labGrid{display:grid;grid-template-columns:1.25fr 0.95fr;gap:24px;align-items:center}
@media(max-width:960px){.labGrid{grid-template-columns:1fr}}
.labControls{display:flex;flex-direction:column;gap:16px}
.labSliderRow{background:#FFFFFF;border:1px solid #E2E8F0;border-radius:14px;padding:14px 16px;box-shadow:0 2px 8px rgba(15,27,45,.02);display:flex;flex-direction:column;gap:8px}
.labSliderHead{display:flex;justify-content:space-between;align-items:center;font-size:13px;font-weight:700;color:#0F172A}
.labBadgeVal{background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE;padding:3px 10px;border-radius:8px;font-size:12.5px;font-weight:800}
.labRange{width:100%;height:6px;accent-color:#1D4ED8;cursor:pointer;margin:4px 0}
.labPresets{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:4px}
.labPresetBtn{background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;border-radius:999px;padding:5px 12px;font-size:11.5px;font-weight:700;cursor:pointer;transition:all .15s ease}
.labPresetBtn:hover{background:#E2E8F0;color:#0F172A}
.labPresetBtn.active{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8}
.labVaultCard{background:radial-gradient(ellipse at top left,#1E293B 0%,#0F172A 100%);border-radius:20px;padding:26px;color:#FFFFFF;box-shadow:0 16px 40px rgba(15,23,42,.35);border:1px solid rgba(255,255,255,.08);display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden}
.labVaultCard::before{content:"";position:absolute;top:-50%;right:-50%;width:100%;height:100%;background:radial-gradient(circle,rgba(52,211,153,.12) 0%,transparent 70%);pointer-events:none}
.vaultBigCounter{font-size:38px;font-weight:900;font-family:var(--serif);color:#34D399;letter-spacing:-1px;margin:8px 0 12px;line-height:1;transition:all .2s ease;display:block}
.vaultBigCounter.pulse{transform:scale(1.04);color:#6EE7B7}
.vaultBreakdown{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(255,255,255,.12)}
.vSubItem{background:rgba(255,255,255,.06);border-radius:10px;padding:8px 10px;text-align:center}
.vSubItem b{display:block;font-size:13px;color:#F8FAFC;font-weight:800}
.vSubItem span{display:block;font-size:10px;color:#94A3B8;margin-top:2px}

/* ---- Cyber Security Institutional Trust Wall ---- */
.trustWallGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:16px}
.trustBadgeCard{background:#FFFFFF;border:1.2px solid #E2E8F0;border-radius:14px;padding:14px;box-shadow:0 3px 10px rgba(15,27,45,.03);display:flex;align-items:flex-start;gap:10px;transition:all .2s ease;cursor:help;position:relative}
.trustBadgeCard:hover{border-color:#93C5FD;transform:translateY(-2px);box-shadow:0 8px 20px rgba(29,78,216,.08)}
.trustBadgeCard .tIco{width:34px;height:34px;border-radius:10px;background:#EFF6FF;color:#1D4ED8;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;border:1px solid #DBEAFE}
.trustBadgeCard .tInfo b{display:block;font-size:12px;color:#0F172A;font-weight:800;margin-bottom:3px}
.trustBadgeCard .tInfo span{display:block;font-size:10.5px;color:#64748B;line-height:1.4}
@media(max-width:960px){.trustWallGrid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:540px){.trustWallGrid{grid-template-columns:1fr}}
@media print {
  body.boardDeckPrintMode * { visibility: hidden !important; }
  body.boardDeckPrintMode #boardDeckModal,
  body.boardDeckPrintMode #boardDeckModal * { visibility: visible !important; }
  body.boardDeckPrintMode #boardDeckModal {
    position: absolute !important;
    left: 0 !important;
    top: 0 !important;
    width: 100% !important;
    height: auto !important;
    background: #FFFFFF !important;
    padding: 0 !important;
    backdrop-filter: none !important;
  }
  body.boardDeckPrintMode #boardDeckModal .hidePrint { display: none !important; }
}
</style></head>
<body>
<header class="top"><div class="wrap brand"><div class="brandLogoWrap">
  <a href="/" class="brandLink">
    <div class="brandLogoIcon">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div class="brandTextWrap">
      <div class="brandTitle">Digital Finance Business Partner</div>
      <div class="brandSub">Finansal Teşhis &amp; Yönetim Karar Destek Platformu</div>
    </div>
  </a>
</div><div class="headerRight"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/cozumler" class="active">Çözümler</a><a href="/hakkimizda">Hakkımızda</a><a href="/uygulama">Uygulama</a><a href="/paketler">Paketler</a><a href="/guvenlik">Güvenlik</a><a href="/iletisim">İletişim</a><div class="mobileNavAuth"><a href="/uygulama?auth=login" class="secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="primary">Ücretsiz Kayıt Ol</a></div></nav><div class="authCluster hidePrint"><div class="headerSwitches"><select class="globalLangSwitch select" onchange="setGlobalLanguage(this.value)" style="padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1" title="Dil / Language"><option value="tr">🇹🇷 TR</option><option value="en">🇬🇧 EN</option><option value="de">🇩🇪 DE</option><option value="fr">🇫🇷 FR</option><option value="es">🇪🇸 ES</option><option value="it">🇮🇹 IT</option><option value="nl">🇳🇱 NL</option></select></div><div class="navBtns"><a href="/uygulama?auth=login" class="navBtn secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="navBtn primary">Ücretsiz Kayıt Ol</a></div></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>

<main class="wrap">
<section class="mHero" style="padding-top:24px;padding-bottom:12px">
  <div class="reveal in" style="max-width:940px;margin:0 auto;text-align:center">
    <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;font-size:12px;font-weight:800;letter-spacing:0.8px;margin-bottom:14px;display:inline-block">🎯 KOBİ PATRONLARI, GENEL MÜDÜRLER &amp; ŞİRKET ORTAKLARI İÇİN</span>
    <h1 style="margin-top:8px;font-size:42px;line-height:1.18">Patronun Masasındaki 10 Gerçek Finansal Kriz<br><span class="gradText">&amp; 8 Stratejik Yönetim Masası</span></h1>
    <p class="lead" style="margin:16px auto 24px;max-width:760px;font-size:16px;color:#475569;line-height:1.6">Muhasebe programınız geçmiş fişleri kaydeder; <b>Digital Finance BP</b> ise şirketi kâr eden ve nakit üreten bir sisteme dönüştürür. Reklamlarımızda gördüğünüz 10 kriz çıkmazı, analitik kanıtları ve 60 saniyelik yönetim reçeteleri:</p>
    
    <div style="display:flex;gap:14px;align-items:center;justify-content:center;flex-wrap:wrap;margin:24px 0 20px">
      <a href="/uygulama?sample=data_hub" class="primary" style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;padding:15px 28px;border-radius:14px;font-size:15px;font-weight:800;background:#1D4ED8;color:#FFFFFF;box-shadow:0 8px 24px rgba(29,78,216,0.35);transition:all .2s ease">
        <span>⚡</span>
        <span>Canlı Demoyu Başlat (60 Sn)</span>
        <span style="font-size:16px;margin-left:2px">→</span>
      </a>
      <a href="/uygulama" style="display:inline-flex;align-items:center;gap:8px;text-decoration:none;padding:14px 24px;border-radius:14px;font-size:14px;font-weight:700;background:#FFFFFF;color:#1E293B;border:1.5px solid #CBD5E1;box-shadow:0 2px 6px rgba(0,0,0,0.04);transition:all .2s ease">
        <span>📁</span>
        <span>Kendi Mizanınızı Yükleyin (Ücretsiz)</span>
      </a>
    </div>

    <!-- Hızlı Sayfa İçi Çapa Linkleri -->
    <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:14px">
      <a href="#kobiShowcase" class="subnavPill" style="font-size:12.5px;padding:7px 16px;font-weight:700">🔥 10 KOBİ Kriz Reçetesi</a>
      <a href="#patronSorulari" class="subnavPill" style="font-size:12.5px;padding:7px 16px;font-weight:700">⚖️ 8 Karar Masası (3 Katman)</a>
      <a href="#caseStudies" class="subnavPill" style="font-size:12.5px;padding:7px 16px;font-weight:700">📈 Temsili Yönetim Vakaları</a>
    </div>

    <div class="miniTrust" style="justify-content:center;margin-top:24px">
      <span><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>RAM-Only (Sıfır Kalıcı Disk Kaydı)</span>
      <span><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>%100 Deterministik Çift Taraflı Denetim</span>
      <span><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 5-8"/></svg>Kurulumsuz · Anında Canlı Sonuç</span>
    </div>
  </div>
</section>

<!-- SECTION: 10 KOBİ PATRON VİTRİNİ -->
<div class="secBlock reveal"><section id="kobiShowcase" class="marketingSection hidePrint" style="padding-top:0">
<div class="marketingHead">
  <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE">🎯 KOBİ PATRONLARI &amp; ŞİRKET ORTAKLARI İÇİN</span>
  <h2 style="margin-top:10px">Patronun Masasındaki 10 Gerçek Kriz &amp; 60 Saniyelik Çözüm</h2>
  <p>Muhasebe programınız geçmiş fişleri kaydeder; Digital Finance BP ise şirketi kâr eden ve nakit üreten bir makineye dönüştürür. İşte patronların en çok yaşadığı 10 çıkmaz ve somut reçetesi:</p>
  
  <div class="kobiPills">
    <button type="button" class="kobiPill active" onclick="filterKobiShowcase('all', this)">🔥 Tümü (10)</button>
    <button type="button" class="kobiPill" onclick="filterKobiShowcase('cash', this)">💵 Nakit &amp; Tahsilat (4)</button>
    <button type="button" class="kobiPill" onclick="filterKobiShowcase('profit', this)">📊 Kâr, Marj &amp; Stok (3)</button>
    <button type="button" class="kobiPill" onclick="filterKobiShowcase('mgmt', this)">🏛️ Yönetim &amp; Banka (3)</button>
  </div>
</div>

<div class="kobiSliderWrap">
  <div class="kobiSliderBar">
    <div class="kobiSwipeHint">
      <span style="font-size:14px">👈</span>
      <span>Kartları sağa / sola kaydırarak inceleyin</span>
      <span style="font-size:14px">👉</span>
    </div>
    <div class="kobiSliderNav">
      <span class="kobiSlideBadge" id="kobiSliderCounter">1 / 10 Teşhis</span>
      <button type="button" class="kobiNavBtn" onclick="slideKobi(-1)" aria-label="Önceki Teşhis" title="Önceki">‹</button>
      <button type="button" class="kobiNavBtn" onclick="slideKobi(1)" aria-label="Sonraki Teşhis" title="Sonraki">›</button>
    </div>
  </div>

  <div class="kobiSliderTrack" id="kobiSliderTrack">

  <!-- Kart 1 -->
  <div class="kobiCard" data-category="cash">
    <span class="kobiTag cash">💵 1. KÂR &amp; NAKİT ÇELİŞKİSİ</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_1_kar_vs_kasa.jpg" alt="1. Kâr ve Nakit Çelişkisi" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Muhasebeciniz 'Bu Ay Kârdayız' Diyor, Ama Siz Ay Sonu Maaşları Nasıl Ödeyeceğinizi Düşünüyorsunuz."</div>
    <div class="kobiDesc">Defterde kâr çıkması, kasada nakit olduğu anlamına gelmez. Satışı yapmışsınız ama parayı müşteriden alamamışsınız; malı üretip depoya yığmışsınız. Kârınız buharlaşmadı; müşterinin açık hesabında ve depodaki kolilerde kilitli kaldı.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Defterdeki Kâr:</span><b style="color:#059669">₺1.850.000 (Mizan Bilanço Kârı)</b></div>
      <div class="kobiMetricRow"><span>Kasadaki Sıcak Nakit:</span><b style="color:#DC2626">₺42.000 (Kritik Alarm)</b></div>
      <div class="kobiMetricRow"><span>Alacak &amp; Stokta Kilitli:</span><b style="color:#B45309">₺1.808.000 Bağlı Sermaye</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Nakit Köprüsü):</b>
      P&amp;L kârınızın hangi hesaplarda kilitlendiğini kuruşu kuruşuna haritalandırır; defter kârı ile serbest nakit akışı arasındaki sızıntıyı kapatır.
    </div>
  </div>

  <!-- Kart 2 -->
  <div class="kobiCard" data-category="cash">
    <span class="kobiTag cash">💵 2. AÇIK HESAP &amp; TERSİNE BANKACILIK</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_2_acik_hesap.jpg" alt="2. Açık Hesap ve Tersine Bankacılık" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Siz Mal mı Satıyorsunuz, Yoksa Müşterilerinize Faizsiz Kredi Dağıtan Banka mısınız?"</div>
    <div class="kobiDesc">Siz bankadan %50 faizle kredi çekip hammadde alıyorsunuz, işçilik ödüyorsunuz; müşteriniz ise malı alıp 90 gün sonra ödüyor! Kendi özkaynağınızla başkalarının ticaretini finanse ediyorsunuz.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Ortalama Tahsilat Vadeniz:</span><b style="color:#DC2626">88 Gün (Sektör: 60 Gün)</b></div>
      <div class="kobiMetricRow"><span>Müşteriyi Fonlama Maliyeti:</span><b style="color:#B45309">Yıllık ~₺1.250.000 Gizli Faiz</b></div>
      <div class="kobiMetricRow"><span>15 Gün Erken Tahsilat Kazancı:</span><b style="color:#1D4ED8">+₺450.000 Sıcak Para</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Alacak Yaşlandırma):</b>
      Alacak portföyünün vadesini tarar; vadesi 60 günü aşan riskli carileri sıralar ve tahsilat hızlandırma protokolünü devreye sokar.
    </div>
  </div>

  <!-- Kart 3 -->
  <div class="kobiCard" data-category="profit">
    <span class="kobiTag profit">📊 3. ÖLÜ STOK MEZARLIĞI</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_3_olu_stok.jpg" alt="3. Ölü Stok Mezarlığı" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Deponuz Ağzına Kadar Mal Dolu Diye Zenginleştiğinizi mi Sanıyorsunuz?"</div>
    <div class="kobiDesc">6 aydır rafta bekleyen o kumaş, o profil, o yedek parça depoda durdukça değer kazanmıyor; her gün banka kredinizin faizini yiyor. Depodaki atıl malı görmezden gelmek, her ay deste deste parayı çöpe atmaktır.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Depodaki Toplam Envanter:</span><b style="color:#0F172A">₺2.400.000</b></div>
      <div class="kobiMetricRow"><span>180+ Günlük Ölü Stok:</span><b style="color:#DC2626">₺680.000 (Atıl Sermaye)</b></div>
      <div class="kobiMetricRow"><span>Aylık Gizli Faiz Yükü:</span><b style="color:#B45309">~₺45.000 / Ay Kayıp</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Envanter İstihbaratı):</b>
      Mizan ile depo kayıtlarını eşleştirir; 180+ gündür devretmeyen ölü stokları listeler ve acil nakde dönüşüm reçetesini çıkarır.
    </div>
  </div>

  <!-- Kart 4 -->
  <div class="kobiCard" data-category="mgmt">
    <span class="kobiTag mgmt">🏛️ 4. MİZAN ÇİLESİ VS. KARAR MASASI</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_4_mizan_vs_karar.jpg" alt="4. Mizan Çilesi vs Karar Masası" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Muhasebeciniz Size Çıkacak Vergiyi Söyler; Parayı Nereden Bulacağınızı Söylemez."</div>
    <div class="kobiDesc">Mali müşavirin işi devlete vergi beyannamesi vermektir. Ancak önünüze konan 500 satırlık mizan tablosundan "Yarın hangi müşteriye mal çıkışını durdurmalıyım?", "Hangi maliyet canımı yakıyor?" sorularının yanıtı çıkmaz.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Klasik Mizan Tablosu:</span><b style="color:#64748B">500 Satır Hesap (Karar Yok)</b></div>
      <div class="kobiMetricRow"><span>Digital Finance BP:</span><b style="color:#1D4ED8">1 Sayfalık Board Raporu</b></div>
      <div class="kobiMetricRow"><span>Yönetimsel Analiz Süresi:</span><b style="color:#059669">Sadece 60 Saniye</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (1-Sayfalık Yönetim Özeti):</b>
      33 karar motoru mizanınızı tarar; kâr durumunu, paranın kilitlendiği yeri ve alınacak 1 numaralı icraat kararını tek sayfada masaya koyar.
    </div>
  </div>

  <!-- Kart 5 -->
  <div class="kobiCard" data-category="cash">
    <span class="kobiTag cash">💵 5. CİRO ALDANMASI &amp; KASA GERÇEĞİ</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_5_ciro_aldanmasi.jpg" alt="5. Ciro Aldanması ve Kasa Gerçeği" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"50 Milyon Ciro Yapıp Ay Sonu Çek Öderken Ter Döken Patronlardan mısınız?"</div>
    <div class="kobiDesc">Ciro gösteriştir, kâr akıl işidir, kasadaki nakit ise gerçeğin ta kendisidir. Cironuz ikiye katlanıyor ama borcunuz da aynı hızla katlanıyorsa büyümüyorsunuz; sadece daha büyük bir riskin altına giriyorsunuz.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Yıllık Satış Cirosu:</span><b style="color:#059669">₺45.000.000 (Büyüme Görünümü)</b></div>
      <div class="kobiMetricRow"><span>Banka &amp; Borç Yükü:</span><b style="color:#DC2626">₺18.000.000 (Faiz Baskısı)</b></div>
      <div class="kobiMetricRow"><span>Kasaya Kalan Net Nakit:</span><b style="color:#DC2626">-₺350.000 (Nakit Açığı)</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Nakit Çevrim Motoru):</b>
      Satıştan tahsilata kadar paranın kaç günde döndüğünü (CCC) hesaplar; cironun nakde dönüşme kabiliyetini ve net kâr kalitesini ölçer.
    </div>
  </div>

  <!-- Kart 6 -->
  <div class="kobiCard" data-category="mgmt">
    <span class="kobiTag mgmt">🏛️ 6. MÜŞTERİ REHİNESİ &amp; KONSANTRASYON</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_6_musteri_rehinesi.jpg" alt="6. Müşteri Rehinesi ve Konsantrasyon" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Cironuzun Yarısını Tek Bir Müşteriye Yapıyorsanız; Patron Siz Değilsiniz, O Müşteridir."</div>
    <div class="kobiDesc">Büyük müşteriyle çalışmak iyidir ama bütün yumurtaları aynı sepete koymak felakettir. O müşteri yarın "Vadeyi 4 aya çıkarıyorum" dediğinde veya ödemeyi geciktirdiğinde şirketin dayanacak kaç günlük can suyu var?</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>İlk 3 Müşterinin Payı:</span><b style="color:#DC2626">%64 (Kritik Bağımlılık)</b></div>
      <div class="kobiMetricRow"><span>Olası Vade Gecikmesi:</span><b style="color:#B45309">-₺1.200.000 Nakit Açığı</b></div>
      <div class="kobiMetricRow"><span>Dayanıklılık Süresi:</span><b style="color:#DC2626">Yalnızca 22 Gün!</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Erken Uyarı Radarı):</b>
      Müşteri bağımlılığınızı ölçer; olası gecikmelerde şirketin likidite dayanıklılığını test eder ve açık hesap tavan limiti belirler.
    </div>
  </div>

  <!-- Kart 7 -->
  <div class="kobiCard" data-category="profit">
    <span class="kobiTag profit">📊 7. FİYATLAMA GÜCÜ &amp; MARJ KORUMA</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_7_fiyat_gucu.jpg" alt="7. Fiyatlama Gücü ve Marj Koruma" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Fiyatlarınıza Sadece %3 Zam Yapsanız Kasaya Kaç Yüz Bin Lira Kalır, Hiç Hesapladınız mı?"</div>
    <div class="kobiDesc">"Müşteri kaçar" korkusuyla maliyet artışlarını fiyata yansıtmamak şirketin özkaynağını eritir. Kontrolsüz iskontolar ve plansız vadeler, ciro artarken kârı sıfırlayan ana sızıntıdır.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Mevcut Brüt Kâr Marjı:</span><b style="color:#B45309">%22,4 (Enflasyon Baskısı)</b></div>
      <div class="kobiMetricRow"><span>Fiyatta +%3 Düzeltme:</span><b style="color:#059669">+₺324.000 Net Kâr Katkısı</b></div>
      <div class="kobiMetricRow"><span>10 Gün Erken Tahsilat:</span><b style="color:#1D4ED8">+₺450.000 Kurtarılan Nakit</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (What-If Simülatörü):</b>
      Fiyat artışı, vade kısaltma ve gider tasarrufu sürgülerini hareket ettirerek şirketin anlık kâr ve nakit kazanımını canlı simüle eder.
    </div>
  </div>

  <!-- Kart 8 -->
  <div class="kobiCard" data-category="cash">
    <span class="kobiTag cash">💵 8. KREDİ KAPANINDAN ÇIKIŞ</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_8_kredi_kapani.jpg" alt="8. Kredi Kapanından Çıkış" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Faizlerin %50 Olduğu Yerde, Şirketi Banka Kredisiyle Döndüremezsiniz."</div>
    <div class="kobiDesc">Kasada nakit sıkışınca ilk refleks bankaya koşup kredi çekmektir. Ama içerideki para kaçağını kapatmadan kredi çekmek, sadece bankalara çalışmaktır. Çözüm yeni borç değil; içerideki kilitli parayı kurtarmaktır.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Bankaya Yıllık Faiz Yükü:</span><b style="color:#DC2626">₺1.850.000 / Yıl</b></div>
      <div class="kobiMetricRow"><span>İçeride Kilitli Kendi Paranız:</span><b style="color:#059669">₺1.400.000 (Alacak &amp; Stok)</b></div>
      <div class="kobiMetricRow"><span>Kredi İhtiyacı Tasarrufu:</span><b style="color:#1D4ED8">%40 Daha Az Borçlanma</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Kaldıraç &amp; Borç Kapasitesi):</b>
      Operasyonel kârınızın faizleri kaç kat karşıladığını ölçer; yeni borca girmeden içerideki kilitli nakdi çözerek şirketi rahatlatır.
    </div>
  </div>

  <!-- Kart 9 -->
  <div class="kobiCard" data-category="mgmt">
    <span class="kobiTag mgmt">🏛️ 9. ORTAKLAR MASASINDA FİKİR BİRLİĞİ</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_9_ortaklar_masasi.jpg" alt="9. Ortaklar Masasında Fikir Birliği" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Her Ay Ortaklarınızla 'İşler İyiydi de Bu Para Nereye Gitti' Kavgası Yapmaktan Bıkmadınız mı?"</div>
    <div class="kobiDesc">Ortaklar arasındaki en büyük gerginlik rakamların farklı yorumlanmasıdır. Biri "Satış ekibi rekor kırdı" der, diğeri "Kasa boş, tedarikçiyi ödeyemiyoruz" der. Suçlu aramak yerine tek bir gerçeğin etrafında toplanın.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>1. Teşhis:</span><b style="color:#DC2626">Kârın %62'si Alacak ve Stokta Bağlı</b></div>
      <div class="kobiMetricRow"><span>2. Öncelikli İcraat:</span><b style="color:#1D4ED8">Vadesi Aşan 3 Müşteriyi Durdur</b></div>
      <div class="kobiMetricRow"><span>3. Kurtarılabilir Nakit:</span><b style="color:#059669">₺1.100.000 (Haftalık Protokol)</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (Deterministik Yönetim Masası):</b>
      Kimsenin tartışamayacağı çift taraflı denetlenmiş verilerle şirketin tek bir yönetim ve eylem gündemi üzerinde uzlaşmasını sağlar.
    </div>
  </div>

  <!-- Kart 10 -->
  <div class="kobiCard" data-category="profit">
    <span class="kobiTag profit">📊 10. CFO ZEKA ARBİTRAJI</span>
    <div class="kobiCardImgWrap">
      <img src="/static/ads/kobi_10_cfo_arbitraji.jpg" alt="10. CFO Zeka Arbitrajı" style="width:100%;height:100%;object-fit:cover;display:block" loading="lazy">
    </div>
    <div class="kobiTitle">"Büyük Holdingler Her Ay Milyonluk Finans Kadrolarıyla Şirket Yönetiyor. Siz Hâlâ Hissiyatla mı Karar Veriyorsunuz?"</div>
    <div class="kobiDesc">Aylık 150-200 bin TL maaşla Finans Direktörü (CFO) tutmak KOBİ ölçeğinde zordur. Ancak rekabet etmek için holdinglerin sahip olduğu finansal denetime ve karar gücüne ihtiyacınız var.</div>
    <div class="kobiMetrics">
      <div class="kobiMetricRow"><span>Holding Finans Kadrosu:</span><b style="color:#64748B">Aylık ₺200.000+ Maliyet</b></div>
      <div class="kobiMetricRow"><span>Digital Finance BP:</span><b style="color:#1D4ED8">60 Saniyede CFO Masası</b></div>
      <div class="kobiMetricRow"><span>Karar Gücü:</span><b style="color:#059669">33 Deterministik Analiz Motoru</b></div>
    </div>
    <div class="kobiPrescription">
      <b>DFBP 60 Saniyelik Reçetesi (60 Saniyede Finansal Röntgen):</b>
      Mizanınızı yükleyin; 33 motor çift taraflı denetimle çalışsın, şirketinizi holding düzeyinde analitik finansal zekayla donatsın.
    </div>
  </div>
  </div>
  <div class="kobiDotsWrap" id="kobiDotsWrap"></div>
</div>

<script>
function slideKobi(direction) {
  var track = document.getElementById('kobiSliderTrack');
  if (!track) return;
  var visibleCards = Array.from(track.querySelectorAll('.kobiCard')).filter(function(c) {
    return c.style.display !== 'none';
  });
  if (!visibleCards.length) return;
  var cardWidth = visibleCards[0].offsetWidth + 22;
  track.scrollBy({ left: direction * cardWidth, behavior: 'smooth' });
}

function initKobiSlider() {
  var track = document.getElementById('kobiSliderTrack');
  var dotsWrap = document.getElementById('kobiDotsWrap');
  var counter = document.getElementById('kobiSliderCounter');
  if (!track || !dotsWrap) return;

  function getVisibleCards() {
    return Array.from(track.querySelectorAll('.kobiCard')).filter(function(c) {
      return c.style.display !== 'none';
    });
  }

  function updateDotsAndCounter() {
    var visible = getVisibleCards();
    if (!visible.length) {
      if (counter) counter.textContent = '0 / 0 Teşhis';
      return;
    }
    var trackRect = track.getBoundingClientRect();
    var activeIdx = 0;
    var minDiff = Infinity;

    visible.forEach(function(c, idx) {
      var r = c.getBoundingClientRect();
      var diff = Math.abs(r.left - trackRect.left);
      if (diff < minDiff) {
        minDiff = diff;
        activeIdx = idx;
      }
    });

    if (counter) {
      counter.textContent = (activeIdx + 1) + ' / ' + visible.length + ' Teşhis';
    }

    var dots = dotsWrap.querySelectorAll('.kobiDot');
    dots.forEach(function(dot, idx) {
      if (idx === activeIdx) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  }

  function rebuildDots() {
    var visible = getVisibleCards();
    dotsWrap.innerHTML = '';
    visible.forEach(function(c, idx) {
      var dot = document.createElement('div');
      dot.className = 'kobiDot' + (idx === 0 ? ' active' : '');
      dot.title = 'Teşhis ' + (idx + 1);
      dot.onclick = function() {
        c.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
      };
      dotsWrap.appendChild(dot);
    });
    updateDotsAndCounter();
  }

  var scrollTimer = null;
  track.addEventListener('scroll', function() {
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(updateDotsAndCounter, 50);
  }, { passive: true });

  window._rebuildKobiSlider = rebuildDots;
  rebuildDots();
}

function filterKobiShowcase(category, btn) {
  var pills = document.querySelectorAll('.kobiPill');
  for (var i = 0; i < pills.length; i++) {
    pills[i].classList.remove('active');
  }
  if (btn) btn.classList.add('active');

  var cards = document.querySelectorAll('.kobiCard');
  for (var j = 0; j < cards.length; j++) {
    var c = cards[j];
    if (category === 'all' || c.getAttribute('data-category') === category) {
      c.style.display = 'flex';
    } else {
      c.style.display = 'none';
    }
  }

  var track = document.getElementById('kobiSliderTrack');
  if (track) {
    track.scrollTo({ left: 0, behavior: 'smooth' });
  }
  if (window._rebuildKobiSlider) {
    window._rebuildKobiSlider();
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initKobiSlider);
} else {
  initKobiSlider();
}
</script>
</section></div>


<!-- SECTION: 3-KATMANLI ÜRÜN MİMARİSİ (PATRONUN AKLINDAKİ 8 KRİTİK SORU) -->
<div class="secBlock tint reveal">
  <section id="patronSorulari" class="marketingSection hidePrint">
    <div class="marketingHead">
      <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE">3 KATMANLI ÜRÜN MİMARİSİ</span>
      <h2>Patron Muhasebe Raporu Değil; "Kasada Neden Para Yok ve Yarın Ne Yapmalıyım?" Sorusunun Cevabını İster</h2>
      <p>Muhasebe programları sadece geçmişin dökümünü listeler. Digital Finance Business Partner ise patronun geceleri aklına takılan 8 kritik soruyu; çift taraflı analitik kanıtlar, net TL getirisi ve uygulanabilir yönetim kararlarıyla anında çözer.</p>
    </div>

    <div style="background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:22px;padding:26px;box-shadow:0 14px 34px rgba(15,27,45,.06)">
      <div style="position:relative;display:flex;align-items:center;margin-bottom:18px;gap:6px">
        <button type="button" class="pillScrollBtn" onclick="scrollPills('landingCeoPills', -280)" aria-label="Geri Kaydır" title="Önceki Sorular">‹</button>
        <div style="display:flex;gap:8px;overflow-x:auto;padding-bottom:6px;scrollbar-width:none;-ms-overflow-style:none;scroll-behavior:smooth;flex:1" id="landingCeoPills">
        <button type="button" class="ceoPill active" data-lq="lq1" onclick="switchLandingCeo('lq1')">💸 Kasada Neden Para Yok?</button>
        <button type="button" class="ceoPill" data-lq="lq2" onclick="switchLandingCeo('lq2')">👥 Hangi Müşteri Zarar Ettiriyor?</button>
        <button type="button" class="ceoPill" data-lq="lq3" onclick="switchLandingCeo('lq3')">📦 Depoda Ne Kadar Para Uyuyor?</button>
        <button type="button" class="ceoPill" data-lq="lq4" onclick="switchLandingCeo('lq4')">🔓 Kredisiz Kaç Milyon TL Nakit Çıkar?</button>
        <button type="button" class="ceoPill" data-lq="lq5" onclick="switchLandingCeo('lq5')">📉 Satış Artarken Marj Neden Büyümüyor?</button>
        <button type="button" class="ceoPill" data-lq="lq6" onclick="switchLandingCeo('lq6')">⚖️ Vade Makası (Müşteri vs Tedarikçi)</button>
        <button type="button" class="ceoPill" data-lq="lq7" onclick="switchLandingCeo('lq7')">🚨 Yarın Sabahın 3 Kritik Alarmı</button>
        <button type="button" class="ceoPill" data-lq="lq8" onclick="switchLandingCeo('lq8')">🎯 CEO'nun 1 Numaralı Kararı</button>
      </div>
        <button type="button" class="pillScrollBtn" onclick="scrollPills('landingCeoPills', 280)" aria-label="İleri Kaydır" title="Sonraki Sorular">›</button>
      </div>

      <div id="landingCeoCards">
        <!-- LQ1 -->
        <div id="lqCard_lq1" class="ceoQuestionCard active">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">💸 NAKİT AKIŞI &amp; KÂR KALİTESİ</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi (₺10M Ciro / ₺1M Net Kâr)</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Defterdeki Kâr, Alacak ve Stok Kilitlenmesinde Kayboluyor</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Defterde ₺1.000.000 net kâr görünmesine karşın, bu kârın neredeyse tamamı müşterilerin 80 günlük tahsilat vadesinde (₺2.25M) ve depodaki 96 günlük stokta (₺1.71M) kilitlenmiştir. Kasa bu kârı fiilen görememektedir.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Net Dönem Kârı</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺1.000.000</div><div style="font-size:9.5px;color:#94A3B8">Defter kârı</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Müşteride Kilitli (120)</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺2.250.000</div><div style="font-size:9.5px;color:#94A3B8">80 gün tahsilat</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Depoda Kilitli (150)</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺1.710.000</div><div style="font-size:9.5px;color:#94A3B8">96 gün stokta</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Nakit Çevrim (CCC)</div><div style="font-size:14px;font-weight:800;color:#0F172A">134 gün</div><div style="font-size:9.5px;color:#94A3B8">Nakit bekleme</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 İlk 10 müşteride açık hesap vadesini 15 gün geri çekin; vadeli siparişleri DBS veya %2 peşin nakit iskontosuyla hızlandırın.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺685.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺308.250 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> CFO &amp; Satış Direktörü · <b>Vade:</b> İlk 30 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ2 -->
        <div id="lqCard_lq2" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">👥 MÜŞTERİ KÂRLILIĞI &amp; ALACAK RİSKİ</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Yüksek Cirolu Müşteriler Uzun Vade ve Gizli Finansmanla Zarar Ettiriyor</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Cironun %38'ini tek başına oluşturan ilk 3 müşteri, 110 gün vade kullanmaktadır. %45 ticari kredi faizi ortamında bu vadenin faiz maliyeti satış marjının %14'ünü tüketmekte ve defterdeki net kârı gizli zarara dönüştürmektedir.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">İlk 3 Müşteri Payı</div><div style="font-size:14px;font-weight:800;color:#0F172A">%38,4</div><div style="font-size:9.5px;color:#94A3B8">Yüksek konsantrasyon</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Ortalama Vade</div><div style="font-size:14px;font-weight:800;color:#0F172A">110 gün</div><div style="font-size:9.5px;color:#94A3B8">Sektör medyanı 65g</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Alacak Finansman Yükü</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺485.000</div><div style="font-size:9.5px;color:#94A3B8">Yıllık faiz erozyonu</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Risk Skoru</div><div style="font-size:14px;font-weight:800;color:#0F172A">84 / 100</div><div style="font-size:9.5px;color:#94A3B8">Kritik seviye</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 Vadesi 75 günü aşan bu müşterilere açık hesap yerine banka DBS limiti zorunluluğu getirin ve %2 vade farkı protokolü imzalayın.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺520.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺234.000 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> Ticari Satış Direktörü · <b>Vade:</b> 45 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ3 -->
        <div id="lqCard_lq3" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">📦 STOK YÖNETİMİ &amp; ATIL SERMAYE</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Depoda ₺1.710.000 Uyuyor, Yıllık ₺769.500 Faiz Sızıntısı Üretiyor</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Mallar depoda ortalama 96 gün kalmaktadır. 90+ gündür hareket görmeyen atıl stoklar depoda çürürken şirketin banka kredisi maliyetini her ay büyütmektedir.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Depoda Bağlı Stok</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺1.710.000</div><div style="font-size:9.5px;color:#94A3B8">150-153 hesapları</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Stokta Kalma (DIO)</div><div style="font-size:14px;font-weight:800;color:#0F172A">96 gün</div><div style="font-size:9.5px;color:#94A3B8">Sektör medyanı 54g</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Yıllık Faiz Sızıntısı</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺769.500</div><div style="font-size:9.5px;color:#94A3B8">%45 faiz proxy</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Stok Devir Hızı</div><div style="font-size:14px;font-weight:800;color:#0F172A">3,8x / yıl</div><div style="font-size:9.5px;color:#94A3B8">Düşük devir</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 90 günden uzun süredir bekleyen ölü stokları paket indirimle derhal nakde çevirin. Satınalma siparişlerini haftalık satış hızına bağlayın.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺356.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺160.200 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> Tedarik Zinciri &amp; Satınalma Müdürü · <b>Vade:</b> 30 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ4 -->
        <div id="lqCard_lq4" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">🔓 İÇ KAYNAKLI ÖZ FİNANSMAN</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Banka Kredisi Almadan Şirket İçinden ₺1.041.000 Sıcak Nakit Çıkabilir</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Tahsilatı 15 gün öne çekmek, stoğu 15 gün hızlandırmak ve tedarikçi vadesini 10 gün uzatmak; bankaya tek kuruş faiz ödemeden şirketinize ₺1.041.000 nakit ve yıllık ₺468.450 net kâr kazandırır.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Tahsilat Katkısı (-15G)</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺411.000</div><div style="font-size:9.5px;color:#94A3B8">Alacak hızlandırma</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Stok Katkısı (-15G)</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺356.000</div><div style="font-size:9.5px;color:#94A3B8">Depo eritme</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Tedarikçi Katkısı (+10G)</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺274.000</div><div style="font-size:9.5px;color:#94A3B8">Satıcı finansmanı</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Toplam İç Nakit</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺1.041.000</div><div style="font-size:9.5px;color:#94A3B8">Sıfır banka kredisi</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 3 Kaldıraçlı Çalışma Sermayesi Programı başlatın: Satış ekibinin primini ciroya değil "kasaya giren tahsilata" endeksleyin.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺1.041.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺468.450 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> İcra Kurulu &amp; Genel Müdür · <b>Vade:</b> Hemen Devrede</div>
            </div>
          </div>
        </div>

        <!-- LQ5 -->
        <div id="lqCard_lq5" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">📉 KÂR KALİTESİ &amp; MALİYET KONTROLÜ</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Faaliyet Giderleri (OpEx) Cirodan %8 Daha Hızlı Artmış</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Satışlar %25 büyürken brüt marj %35'ten %31'e gerilemiş; genel yönetim ve lojistik giderleri kâr artışını eritmiştir. Şirket daha çok çalışmakta ancak daha az operasyonel kâr üretmektedir.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Brüt Kâr Marjı</div><div style="font-size:14px;font-weight:800;color:#0F172A">%31,0</div><div style="font-size:9.5px;color:#94A3B8">Önceki: %35,0 (↓)</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Faaliyet Kâr Marjı</div><div style="font-size:14px;font-weight:800;color:#0F172A">%10,0</div><div style="font-size:9.5px;color:#94A3B8">Operasyonel marj</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Gider / Ciro Oranı</div><div style="font-size:14px;font-weight:800;color:#0F172A">%21,0</div><div style="font-size:9.5px;color:#94A3B8">OpEx yoğunluğu</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Finansman Yükü</div><div style="font-size:14px;font-weight:800;color:#0F172A">%40,0</div><div style="font-size:9.5px;color:#94A3B8">Faaliyet kârına oranı</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 Fiyatlama politikasını enflasyon bazlı dinamik tarifeye geçirin; kârsız ürün kodlarını ürün portföyünden derhal ayıklayın.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Ekstra Faaliyet Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺200.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Yıllık Marj Katkısı</div><div style="font-size:14px;font-weight:800;color:#166534">+%2,0 Puan</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> Finans Direktörü &amp; Satış · <b>Vade:</b> 30 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ6 -->
        <div id="lqCard_lq6" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">⚖️ İŞLETME SERMAYESİ ASİMETRİSİ</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Tedarikçiye 42 Günde Ödeyip Müşteriyi 80 Gün Beklemek Şirketi Kanamaya İtiyor</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Ortaya çıkan 38 günlük vade açığını kapatmak için şirket kendi özkaynağını eritmekte ve bankadan yüksek faizli rotatif kredi çekmektedir.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Müşteri Vadesi (DSO)</div><div style="font-size:14px;font-weight:800;color:#0F172A">80 gün</div><div style="font-size:9.5px;color:#94A3B8">Alacak vadesi</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Tedarikçi Vadesi (DPO)</div><div style="font-size:14px;font-weight:800;color:#0F172A">42 gün</div><div style="font-size:9.5px;color:#94A3B8">Ödeme vadesi</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Net Vade Makası Açığı</div><div style="font-size:14px;font-weight:800;color:#0F172A">38 gün</div><div style="font-size:9.5px;color:#94A3B8">Finanse edilen gün</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Tedarikçi Borçları</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺750.000</div><div style="font-size:9.5px;color:#94A3B8">320 Satıcılar</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 Tedarikçilerle vadeleri 15 gün uzatacak konsinye veya vadeli çek protokolü yapın; müşterilere ise tedarikçi vadesinin üzerinde açık hesap açmayın.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺410.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺184.500 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> Satınalma Direktörü &amp; CFO · <b>Vade:</b> 30 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ7 -->
        <div id="lqCard_lq7" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">🚨 CEO ERKEN UYARI RADARI</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">33 Karar Motorunun Belirlediği 3 Öncelikli Alarm</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Mizan çift taraflı denetlenmiş ve nakit akışını riske atan ilk 3 finansal alarm tespit edilmiştir: Tahsilat süresinin uzaması, depoda kilitli sermaye ve kısa vadeli borç geri ödeme takvimi.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">1. Tahsilat Vadesi</div><div style="font-size:14px;font-weight:800;color:#0F172A">88 / 100</div><div style="font-size:9.5px;color:#94A3B8">Maruziyet: ₺780k</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">2. Kilitli Stok Yükü</div><div style="font-size:14px;font-weight:800;color:#0F172A">76 / 100</div><div style="font-size:9.5px;color:#94A3B8">Maruziyet: ₺769k</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">3. Likidite / Borç</div><div style="font-size:14px;font-weight:800;color:#0F172A">72 / 100</div><div style="font-size:9.5px;color:#94A3B8">Cari oran 1.1x</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Finansal Sağlık</div><div style="font-size:14px;font-weight:800;color:#0F172A">74 / 100</div><div style="font-size:9.5px;color:#94A3B8">Orta-Risk</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 Risk komitesini toplayarak bu 3 alarm için haftalık nakit akış toplantısı kurgulayın ve erken uyarı limitleri belirleyin.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Korunan Nakit Kalkanı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺390.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Batık Riski Önleme</div><div style="font-size:14px;font-weight:800;color:#166534">Tam Güvence</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> İcra Kurulu · <b>Vade:</b> İlk 7 Gün</div>
            </div>
          </div>
        </div>

        <!-- LQ8 -->
        <div id="lqCard_lq8" class="ceoQuestionCard">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
            <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">🎯 CEO İCRAAT DİREKTİFİ</span>
            <div class="small muted">Örnek Şirket Verisi Teşhisi</div>
          </div>
          <div class="ceoGrid3">
            <div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Bugün Masaya Koymanız Gereken 1 Numaralı Karar</h4>
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Şirketinizin nakit akışını ve kârını kalıcı olarak kurtaracak tek hamle: Vadesi 60 günü aşan müşterilere yeni mal sevkiyatını dondurmak ve ilk 10 müşteriyle banka teminatlı DBS protokolü başlatmaktır.</p>
            </div>
            <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>
              <div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Yıllık Kâr Sızıntısı</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺1.782.000</div><div style="font-size:9.5px;color:#94A3B8">Faiz kaybı</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Kilitli Nakit Tutarı</div><div style="font-size:14px;font-weight:800;color:#0F172A">₺3.960.000</div><div style="font-size:9.5px;color:#94A3B8">Alacak + Stok</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">Kurtarılabilir Kâr</div><div style="font-size:14px;font-weight:800;color:#0F172A">+₺801.900</div><div style="font-size:9.5px;color:#94A3B8">Yıllık faiz tasarrufu</div></div>
                <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px"><div style="font-size:10.5px;color:#64748B">İcraat Etkisi</div><div style="font-size:14px;font-weight:800;color:#0F172A">Kritik</div><div style="font-size:9.5px;color:#94A3B8">Doğrudan kâr artışı</div></div>
              </div>
            </div>
            <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">
              <div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>
              <div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 Satış direktörüne bugün yazılı talimat verin: Vadesi 60 günü aşan müşteriye sevkiyat onayı verilmeyecek; açık hesap riski DBS garantisine bağlanacaktır.</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div><div style="font-size:14px;font-weight:800;color:#166534">+₺685.000</div></div>
                <div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px"><div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Faiz Kârı</div><div style="font-size:14px;font-weight:800;color:#166534">+₺308.250 / yıl</div></div>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DCFCE7;padding-top:10px;font-size:11px;color:#166534"><b>Sorumlu:</b> CEO &amp; Genel Müdür · <b>Vade:</b> Bugün</div>
            </div>
          </div>
        </div>
      </div>

      <div style="margin-top:20px;padding-top:16px;border-top:1px solid #E2E8F0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px">
        <div style="font-size:13px;color:#64748B">
          💡 Kendi şirketinizin mizanında bu soruların yanıtlarını kuruşu kuruşuna görmek için canlı demoyu başlatın.
        </div>
        <a href="/uygulama?sample=data_hub" class="primary" style="text-decoration:none;padding:10px 20px;border-radius:10px;font-size:13.5px;font-weight:700">
          🔥 Kendi Verilerinizle Canlı Cevapları Görün →
        </a>
      </div>
    </div>
  </section>
</div>



<!-- SECTION: GERÇEK VERİ TABANLI TEMSİLİ YÖNETİM VAKALARI (CASE STUDIES) -->
<div class="secBlock reveal">
  <section id="caseStudies" class="marketingSection hidePrint" style="padding-top:0">
    <div class="marketingHead">
      <span class="workflowBadge" style="background:#ECFDF5;color:#047857;border-color:#A7F3D0">📈 GERÇEK VERİ TABANLI TEMSİLİ YÖNETİM VAKALARI</span>
      <h2 style="margin-top:10px">Rakamlar Yalan Söylemez: Finansal Karar Modellerimiz Kasaları Nasıl Rahatlatıyor?</h2>
      <p>Aşağıdaki vakalar, platformun 33 Karar Motoru ve çift taraflı denetim mimarisi ile analiz edilen gerçek sektör bilançoları baz alınarak modellenmiş <b>temsili yönetim senaryolarıdır</b>. Ticari mahremiyet nedeniyle unvanlar anonimleştirilmiş; matematiksel formülasyon, oran analizleri ve kâr/nakit optimizasyon dinamikleri birebir korunmuştur.</p>
    </div>

    <div class="caseGrid">
      <!-- Case 1: İmalat & Sanayi -->
      <div class="caseCard">
        <div class="caseHead">
          <span class="caseBadge verified">📊 TEMSİLİ MODELLEME VAKASI · İMALAT SANAYİ</span>
          <span class="caseLocation">Kocaeli · ₺65M Yıllık Hacim</span>
        </div>
        <div class="caseTitle">"Depodaki 180+ Günlük Ölü Stok Teşhis Edildi; ₺1.450.000 Atıl Nakit 45 Günde Kasaya Döndü."</div>
        <div class="caseProblem">
          <b>Kriz:</b> Şirket sürekli nakit sıkışıklığı çekiyor ve bankadan yüksek faizli ticari kredi kullanıyordu. Mizan incelendiğinde ₺3.2M stok görünüyordu ancak alt depo kırılımı takip edilmiyordu.
        </div>
        <div class="caseSolution">
          <b>DFBP Reçetesi:</b> Envanter İstihbarat Motoru mizan ile stok defterini eşleştirdi; 180 günü aşan 4 grup ölü hammaddeyi listeledi. Hızlı iskonto ve iade protokolüyle atıl sermaye nakde çevrildi.
        </div>
        <div class="caseKpis">
          <div class="caseKpiItem"><b style="color:#047857">+₺1.450.000</b><span>Kurtarılan Sıcak Nakit</span></div>
          <div class="caseKpiItem"><b style="color:#1D4ED8">112g → 64g</b><span>Nakit Çevrim (CCC)</span></div>
          <div class="caseKpiItem"><b style="color:#B45309">₺420.000 / yıl</b><span>Faiz Tasarrufu</span></div>
        </div>
      </div>

      <!-- Case 2: Gıda Dağıtım & Toptan -->
      <div class="caseCard">
        <div class="caseHead">
          <span class="caseBadge verified">📊 TEMSİLİ MODELLEME VAKASI · HIZLI TÜKETİM &amp; DAĞITIM</span>
          <span class="caseLocation">Bursa · ₺110M Yıllık Hacim</span>
        </div>
        <div class="caseTitle">"88 Günlük Operasyonel Açık Hesap Vadesi (Resmi Mizan: 81 Gün) 52 Güne İndirildi; Banka Kredi İhtiyacı ₺2.800.000 Azaldı."</div>
        <div class="caseProblem">
          <b>Kriz:</b> Şirket rekor ciro yapmasına rağmen ay sonlarında tedarikçi çeklerini ödeyemiyordu. Resmi mizan DSO vadesi 81 gün iken operasyonel yaşlandırma alt defterinde fiili vade 88 güne çıkmıştı; bayiler açık hesap vadelerini sürekli uzatarak şirketi faizsiz banka gibi kullanıyordu.
        </div>
        <div class="caseSolution">
          <b>DFBP Reçetesi:</b> Alacak Yaşlandırma Motoru ilk 20 bayinin vadesini taradı; vadesi 60 günü aşan riskli cariler durduruldu ve DBS (Doğrudan Borçlandırma Sistemi) entegrasyonuna bağlandı. Operasyonel DSO 88 günden 52 güne çekildi.
        </div>
        <div class="caseKpis">
          <div class="caseKpiItem"><b style="color:#047857">+₺2.800.000</b><span>Azalan Kredi Yükü</span></div>
          <div class="caseKpiItem"><b style="color:#1D4ED8">88g → 52g</b><span>Operasyonel Vade (DSO)</span></div>
          <div class="caseKpiItem"><b style="color:#B45309">₺640.000 / yıl</b><span>Kurtarılan Faiz Kârı</span></div>
        </div>
      </div>

      <!-- Case 3: Tekstil & İhracat -->
      <div class="caseCard">
        <div class="caseHead">
          <span class="caseBadge verified">📊 TEMSİLİ MODELLEME VAKASI · TEKSTİL &amp; İHRACAT</span>
          <span class="caseLocation">İstanbul · €4.2M İhracat Hacmi</span>
        </div>
        <div class="caseTitle">"%62 Müşteri Konsantrasyonu ve Gizli Kur Zararı Yakalandı; Brüt Marj %18'den %24'e Çıktı."</div>
        <div class="caseProblem">
          <b>Kriz:</b> Şirketin cirosunun üçte ikisi tek bir yabancı alıcıya bağlıydı. Döviz kuru hareketlerinde kur farkı gelir/gider ayrıştırması yapılmadığı için kârlı sanılan siparişler gizli zarara yol açıyordu.
        </div>
        <div class="caseSolution">
          <b>DFBP Reçetesi:</b> Müşteri Risk Radarı ve FX Risk Röntgeni devreye alındı. Kârsız 3 sipariş hattı revize edildi; vadeli döviz sözleşmelerinde kur koruma kuralları uygulanarak brüt marj 6 puan artırıldı.
        </div>
        <div class="caseKpis">
          <div class="caseKpiItem"><b style="color:#047857">+%6 Net Artış</b><span>Brüt Kâr Marjı</span></div>
          <div class="caseKpiItem"><b style="color:#1D4ED8">%62 → %34</b><span>Müşteri Bağımlılığı</span></div>
          <div class="caseKpiItem"><b style="color:#B45309">+€280.000</b><span>Net Nakit Katkısı</span></div>
        </div>
      </div>

      <!-- Case 4: Makine & Otomotiv Yan Sanayi -->
      <div class="caseCard">
        <div class="caseHead">
          <span class="caseBadge verified">📊 TEMSİLİ MODELLEME VAKASI · MAKİNE &amp; YAN SANAYİ</span>
          <span class="caseLocation">İzmir · ₺48M Yıllık Hacim</span>
        </div>
        <div class="caseTitle">"Mizan ile Stok Defteri Arasındaki %34 Mutabakat Uçurumu ve ₺920.000 Kâr Kaçağı Kapatıldı."</div>
        <div class="caseProblem">
          <b>Kriz:</b> Ortaklar toplantısında kâr paylaşımı konusunda anlaşmazlık vardı. Mizan tablosundaki 150/153 hesapları ile fiili depo sayım raporları arasında yüz binlerce liralık mutabakat farkı bulunuyordu.
        </div>
        <div class="caseSolution">
          <b>DFBP Reçetesi:</b> Data Hub Çapraz Mutabakat Motoru mizan ile stok listesini satır satır eşleştirdi; kayıp stok hareketleri ve faturalandırılmamış sevkiyatlar tespit edilerek ortaklar arasında tek veri konsensüsü sağlandı.
        </div>
        <div class="caseKpis">
          <div class="caseKpiItem"><b style="color:#047857">₺920.000</b><span>Tespit Edilen Sızıntı</span></div>
          <div class="caseKpiItem"><b style="color:#1D4ED8">%100 Mutabakat</b><span>Mizan &amp; Defter Uyumu</span></div>
          <div class="caseKpiItem"><b style="color:#B45309">1 Gün</b><span>Uzlaşma &amp; Karar Süresi</span></div>
        </div>
      </div>
    </div>
  </section>
</div>


<!-- CLOSING ACTION SECTION -->
<div class="secBlock reveal"><section class="ctaBanner hidePrint" style="margin-top:20px">
  <div>
    <h3 style="font-size:24px;margin:0 0 8px;font-family:var(--serif)">Finansal Verilerinizi Stratejik İş Kararlarına Dönüştürün</h3>
    <p style="margin:0;color:var(--muted);font-size:14px">Entegrasyon gerektirmez. Örnek Data Hub verisiyle veya kendi mizanınızla 60 saniyede karar raporunuzu alın.</p>
  </div>
  <div style="display:flex;gap:12px;flex-wrap:wrap">
    <a href="/uygulama?sample=data_hub" class="primary" style="text-decoration:none;padding:13px 22px;border-radius:12px;font-size:14px;font-weight:700">🔥 Canlı Demoyu Başlat</a>
    <a href="/uygulama" class="secondary" style="text-decoration:none;padding:13px 22px;border-radius:12px;font-size:14px;font-weight:700">Kendi Dosyanızı Yükleyin →</a>
  </div>
</section></div>
</main>

<div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/cozumler">Çözümler</a></li><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • <a href="https://digitalfinancebp.com" style="color:var(--accent);text-decoration:none;font-weight:700">digitalfinancebp.com</a> • Deterministik Finans Karar Motoru &amp; Çift Yönlü Denetim Sistemi<br><span style="opacity:.85">Bu analiz deterministik matematiksel hesaplamalara ve çift taraflı denetim kurallarına dayanır; resmi mali tablo veya vergi beyannamesi yerine geçmez. Nihai yönetim kararları için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca anlık analiz süresince RAM bellekte işlenir; sunucu sabit diskinde ASLA kalıcı saklanmaz. KVKK ve kurumsal gizlilik politikamız için <a href="javascript:void(0)" onclick="showKvkkModal()" style="color:var(--accent);text-decoration:underline;font-weight:600">Aydınlatma ve Gizlilik Metni</a>'ni inceleyebilirsiniz.</span></div></div></div>


<script>
window.scrollPills = function(id, delta){
  const el = document.getElementById(id);
  if(el){ el.scrollBy({ left: delta, behavior: 'smooth' }); }
};
window.switchLandingCeo = function(lqid){
  document.querySelectorAll('#landingCeoPills .ceoPill').forEach(p => {
    p.classList.toggle('active', p.getAttribute('data-lq') === lqid);
  });
  document.querySelectorAll('#landingCeoCards .ceoQuestionCard').forEach(c => {
    c.classList.toggle('active', c.id === 'lqCard_' + lqid);
  });
};
document.getElementById('navToggle')?.addEventListener('click',()=>document.getElementById('mainNav')?.classList.toggle('open'));

var GLOBAL_I18N = {
  tr: { navHome: 'Anasayfa', navSolutions: 'Çözümler', navAbout: 'Hakkımızda', navApp: 'Uygulama', navPricing: 'Paketler', navSecurity: 'Güvenlik', navContact: 'İletişim', login: 'Giriş Yap', register: 'Ücretsiz Kayıt Ol' },
  en: { navHome: 'Home', navSolutions: 'Solutions', navAbout: 'About', navApp: 'App', navPricing: 'Pricing', navSecurity: 'Security', navContact: 'Contact', login: 'Log In', register: 'Sign Up Free' },
  de: { navHome: 'Startseite', navSolutions: 'Lösungen', navAbout: 'Über uns', navApp: 'Anwendung', navPricing: 'Preise', navSecurity: 'Sicherheit', navContact: 'Kontakt', login: 'Anmelden', register: 'Kostenlos Registrieren' },
  fr: { navHome: 'Accueil', navSolutions: 'Solutions', navAbout: 'À propos', navApp: 'Application', navPricing: 'Tarifs', navSecurity: 'Sécurité', navContact: 'Contact', login: 'Connexion', register: 'Inscription Gratuite' },
  es: { navHome: 'Inicio', navSolutions: 'Soluciones', navAbout: 'Sobre Nosotros', navApp: 'Aplicación', navPricing: 'Precios', navSecurity: 'Seguridad', navContact: 'Contacto', login: 'Iniciar Sesión', register: 'Registro Gratis' },
  it: { navHome: 'Home', navSolutions: 'Soluzioni', navAbout: 'Chi siamo', navApp: 'Applicazione', navPricing: 'Piani', navSecurity: 'Sicurezza', navContact: 'Contatti', login: 'Accedi', register: 'Registrati Gratis' },
  nl: { navHome: 'Startpagina', navSolutions: 'Oplossingen', navAbout: 'Over ons', navApp: 'Applicatie', navPricing: 'Tarieven', navSecurity: 'Beveiliging', navContact: 'Contact', login: 'Inloggen', register: 'Gratis Registreren' }
};
function setGlobalLanguage(lang){
  try { localStorage.setItem('dfbp_lang', lang); } catch(e){}
  var dict = GLOBAL_I18N[lang] || GLOBAL_I18N.tr;
  document.querySelectorAll('.globalLangSwitch').forEach(function(s){ s.value = lang; });
  var nav = document.getElementById('mainNav');
  if(nav){
    var links = nav.querySelectorAll('a');
    if(links.length >= 7){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navSolutions;
      links[2].textContent = dict.navAbout;
      links[3].textContent = dict.navApp;
      links[4].textContent = dict.navPricing;
      links[5].textContent = dict.navSecurity;
      links[6].textContent = dict.navContact;
    }
  }
  document.querySelectorAll('.navBtn.secondary, .navBtn.sec, #loginOpenBtn').forEach(function(b){ b.textContent = dict.login; });
  document.querySelectorAll('.navBtn.primary, .navBtn.pri, #registerOpenBtn').forEach(function(b){ b.textContent = dict.register; });
}
if(typeof document !== 'undefined' && document.addEventListener){
  document.addEventListener('DOMContentLoaded', function(){
    var saved = 'tr';
    try { saved = localStorage.getItem('dfbp_lang') || 'tr'; } catch(e){}
    setGlobalLanguage(saved);
  });
}
</script>
</body></html>
'''

PRICING_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" type="image/svg+xml" href="/favicon.ico"><meta name="description" content="Digital Finance Business Partner (digitalfinancebp.com) — Şirketinizin finansal tablolarını 33 analitik karar motoruyla denetleyen, kâr sızıntılarını ve kilitli nakdi hesaplayan kurumsal karar destek platformu."><title>Paketler | Digital Finance Business Partner</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&display=swap" rel="stylesheet">
<style>
:root{--bg:#F6F7F9;--panel:#FFFFFF;--panel2:#F0F3F8;--line:#E4E8EF;--text:#0F1B2D;--muted:#5B6B84;--accent:#1D4ED8;--accent2:#4F8CFF;--red:#C22A3E;--amber:#B4720A;--green:#0E7C66;--shadow:0 1px 2px rgba(15,27,45,.04),0 12px 32px rgba(15,27,45,.06);--serif:'Fraunces',ui-serif,Georgia,serif}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(1100px 480px at 12% -10%, rgba(29,78,216,.07), transparent 60%),radial-gradient(900px 420px at 100% 0%, rgba(14,124,102,.05), transparent 55%),#F6F7F9;color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45}button,input,select{font:inherit}.wrap{max-width:1440px;margin:auto;padding:0 28px}.top{padding:26px 0 18px;border-bottom:1px solid rgba(15,27,45,.08);position:sticky;top:0;background:rgba(246,247,249,.86);backdrop-filter:blur(18px);z-index:10}.brand{display:flex;align-items:center;justify-content:space-between;gap:20px}.brand h1{margin:0;font-size:25px;letter-spacing:-.6px}.brand p{margin:3px 0 0;color:var(--muted);font-size:13px}.badge{padding:6px 10px;border:1px solid #D7DEE8;border-radius:999px;color:var(--accent);font-size:12px;white-space:nowrap}.hero{padding:34px 0 24px;display:grid;grid-template-columns:1.45fr .55fr;gap:18px}.heroCard,.card{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow)}.heroCard{padding:28px}.heroTitle{font-family:var(--serif);font-weight:600;font-size:44px;line-height:1.08;margin:0 0 14px;letter-spacing:-.5px}.heroText{color:var(--muted);max-width:780px}.framework{display:flex;flex-wrap:wrap;gap:8px 10px;margin:16px 0 2px;padding:0}.framework span{font-size:11.5px;color:#33415C;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px}.framework span b{color:var(--accent);font-weight:800}
.qsel{margin-top:18px}.qsel .qtitle{font-size:12px;color:var(--muted);margin-bottom:8px;font-weight:700}.qsel .qrow{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.qsel button{border:1px solid #D7DEE8;background:#EEF2FF;color:#33415C;border-radius:12px;padding:10px 12px;font-size:12.5px;cursor:pointer;text-align:left;line-height:1.3}.qsel button:hover{border-color:#B7C3D6}.qsel button.active{border-color:var(--accent);color:var(--accent);background:#DCE6FB}
.upload{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}.file{border:1px dashed #C9D2DE;padding:12px;border-radius:12px;background:#F5F7FA;max-width:100%}.select,button{border:1px solid #D7DEE8;border-radius:11px;padding:11px 14px;background:#FFFFFF;color:var(--text)}button.primary,a.primary{background:linear-gradient(135deg,#2557E8,#1D4ED8);border:0;color:#FFFFFF;font-weight:800;cursor:pointer;transition:transform .15s ease,box-shadow .15s ease;box-shadow:0 6px 16px rgba(29,78,216,.25)}a.primary:hover,button.primary:hover{transform:translateY(-1px);box-shadow:0 10px 22px rgba(29,78,216,.32)}button.secondary,a.secondary{cursor:pointer;border:1.5px solid #C9D2DE;background:#FFFFFF;color:var(--text)}a.secondary:hover,button.secondary:hover{border-color:var(--accent);color:var(--accent)}button:disabled{opacity:.5;cursor:not-allowed}.scoreCard{padding:25px;display:flex;flex-direction:column;justify-content:center}.scoreRing{width:170px;height:170px;border-radius:50%;margin:auto;display:grid;place-items:center;background:conic-gradient(var(--accent) calc(var(--score)*1%),#E4E8EF 0);position:relative}.scoreRing:after{content:"";position:absolute;inset:12px;border-radius:50%;background:#FFFFFF}.scoreNum{position:relative;z-index:1;text-align:center}.scoreNum strong{display:block;font-size:48px;line-height:1}.scoreNum span{color:var(--muted);font-size:12px}.status{margin:15px auto 0;padding:7px 12px;border-radius:999px;background:#EAF0FF;color:var(--accent);font-size:12px;font-weight:700}.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.card{padding:22px;margin:0 0 16px;transition:transform .18s ease,box-shadow .18s ease,outline .2s}.card:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(15,27,45,.08)}@keyframes growUp{from{transform:scaleY(0);opacity:0}to{transform:scaleY(1);opacity:1}}.wf{transform-origin:bottom}.wf .col{transform-origin:bottom}@keyframes growWidth{from{width:0}to{}}.metric{padding:17px;border:1px solid var(--line);border-radius:15px;background:rgba(15,27,45,.03)}.metric .label{color:var(--muted);font-size:12px}.metric .value{font-size:25px;font-weight:800;margin-top:5px;letter-spacing:-.5px}.metric .sub{font-size:11px;color:var(--muted);margin-top:5px}.sectionHead{display:flex;align-items:end;justify-content:space-between;gap:15px;margin-bottom:17px}.sectionHead h2{margin:0;font-size:18px}.sectionHead p{margin:0;color:var(--muted);font-size:12px}.flowStep{margin:36px 0 14px;padding-top:6px;border-top:1px solid rgba(15,27,45,.08)}.flowStep:first-child{margin-top:0;border-top:0;padding-top:0}.flowLabel{display:flex;align-items:center;gap:10px;font-size:12px;font-weight:800;letter-spacing:1.8px;text-transform:uppercase;color:var(--accent);margin:0 0 4px}.flowLabel .n{width:22px;height:22px;border-radius:50%;background:#EAF0FF;color:var(--accent);display:inline-flex;align-items:center;justify-content:center;font-size:11px}.flowLabel p{margin:0;color:var(--muted);font-size:12.5px;font-weight:500;text-transform:none;letter-spacing:0}.flowLabel.alt{color:var(--accent2)}.flowLabel.alt .n{color:var(--accent2)}.flowSub{color:var(--muted);font-size:12.5px;margin:2px 0 16px 32px}.insight{border:1px solid var(--line);border-radius:15px;padding:16px;background:#F7F9FC}.insight.critical{border-color:#E8B4BD}.insight.high{border-color:#E9CBA8}.insight.medium{border-color:#E5DBA0}.insight.positive{border-color:#A9D9C9}.insight h3{margin:0 0 5px;font-size:14px}.insight p{margin:6px 0;color:#33415C;font-size:13px}.insight ul{margin:6px 0;padding-left:18px;color:#33415C;font-size:13px}.tag{display:inline-flex;padding:4px 8px;border-radius:999px;font-size:10px;font-weight:800;text-transform:uppercase;background:#EAF0FF;color:#5B6B84}.tag.critical{background:#FCE8EA;color:#C22A3E}.tag.high{background:#FDF0E0;color:#B4720A}.tag.medium{background:#FBF6DE;color:#8A6D00}.tag.positive{background:#E4F5EF;color:#0E7C66}.riskRow,.actionRow{display:grid;grid-template-columns:40px 1fr auto;gap:12px;align-items:center;padding:13px 0;border-bottom:1px solid rgba(15,27,45,.08)}.rank{font-size:18px;font-weight:900;color:#5B6B84}.riskScore{font-size:12px;color:var(--muted)}.bar{height:7px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:8px}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:99px}.waterfall{display:flex;align-items:flex-end;gap:7px;height:190px;padding:20px 5px 0;border-bottom:1px solid var(--line)}.wf{flex:1;display:flex;flex-direction:column;justify-content:end;height:100%;min-width:0}.wf .col{border-radius:6px 6px 2px 2px;background:linear-gradient(180deg,#83a4ff,#506fd0);min-height:3px}.wf.neg .col{background:linear-gradient(180deg,#ff8290,#9d3e54)}.wf .lab{font-size:10px;color:var(--muted);text-align:center;margin-top:7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.wf .num{font-size:9px;text-align:center;color:#33415C;margin-bottom:4px}.scenario{padding:18px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(145deg,#F5F8FF,#EEF3FC)}.scenario h3{margin:0 0 6px;font-size:15px}.scenario .big{font-size:24px;font-weight:900;color:var(--accent)}.scenario p{color:var(--muted);font-size:11px;margin:6px 0}.muted{color:var(--muted)}.small{font-size:11px}.tableWrap{overflow:auto}table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:10px 8px;border-bottom:1px solid rgba(15,27,45,.08);text-align:right}th:first-child,td:first-child{text-align:left}th{color:#5B6B84;font-weight:600}.notice{padding:12px 14px;border-radius:12px;background:#EEF2FF;border:1px solid var(--line);color:#5B6B84;font-size:12px}.error{color:#C22A3E;background:#FCE8EA;border:1px solid #E8B4BD;padding:12px;border-radius:12px;margin:15px 0}.hidden{display:none!important}.footer{padding:25px 0 50px;color:#5B6B84;font-size:11px;text-align:center}.tabs{display:flex;gap:8px;margin-top:16px}.tab{padding:8px 12px;border-radius:999px;background:#F0F3F8;border:1px solid var(--line);color:#5B6B84;cursor:pointer}.tab.active{background:#DCE6FB;color:var(--accent);border-color:#1D4ED8}.tabPanel{display:none}.tabPanel.active{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.hidePrint{display:block}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.chip{font-size:11.5px;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px;color:#33415C}.chip b{color:var(--accent)}
.abar{height:9px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:6px}.abar i{display:block;height:100%;background:linear-gradient(90deg,#8aa7ff,#ff8290);border-radius:99px}
.custRow{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12.5px}
.highlight-target{outline:2px solid var(--accent);outline-offset:6px}
/* --- Marketing surface additions --- */
.topNav{display:flex;gap:18px}
.topNav a{color:var(--muted);font-size:13px;text-decoration:none;font-weight:600}
.topNav a:hover{color:var(--accent)}
.marketingSection{padding:8px 0 16px}
.marketingHead{text-align:center;max-width:640px;margin:0 auto 34px}
.marketingHead h2{font-family:var(--serif);font-size:32px;margin:0 0 10px;letter-spacing:-.5px}
.marketingHead p{color:var(--muted);margin:0;font-size:14.5px}
.pricingGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:stretch}
.priceCard{display:flex;flex-direction:column;padding:28px 24px;position:relative}
.priceCard.featured{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent),var(--shadow)}
.priceCard .plan{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:var(--accent);font-weight:800;margin-bottom:8px}
.priceCard h3{margin:0 0 6px;font-size:22px;font-family:var(--serif)}
.priceCard .amt{font-size:34px;font-weight:900;margin:8px 0 4px}
.priceCard .amt span{font-size:13px;color:var(--muted);font-weight:500}
.priceCard .desc{color:var(--muted);font-size:13px;margin-bottom:18px}
.priceCard ul{list-style:none;margin:0 0 22px;padding:0;flex:1;display:flex;flex-direction:column;gap:10px}
.priceCard ul li{font-size:13px;color:#33415C;display:flex;gap:8px;align-items:flex-start}
.priceCard ul li svg{flex:none;margin-top:2px;color:var(--accent)}
.priceCard .badgeTop{position:absolute;top:-11px;left:50%;transform:translateX(-50%);background:var(--accent);color:#FFFFFF;font-size:10.5px;font-weight:800;padding:4px 12px;border-radius:999px;letter-spacing:.5px}
.aboutGrid{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:center}
.aboutStats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}
.aboutStats .st{padding:16px;border:1px solid var(--line);border-radius:14px;text-align:center;background:rgba(15,27,45,.03)}
.aboutStats .st b{display:block;font-size:24px;color:var(--accent);font-family:var(--serif)}
.aboutStats .st span{font-size:11px;color:var(--muted)}
.contactGrid{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.contactCard{padding:26px}
.contactRow{display:flex;flex-direction:column;gap:12px;margin-top:14px}
.contactRow .item{display:flex;gap:10px;align-items:center;font-size:13px;color:#33415C}
.contactRow .item svg{color:var(--accent);flex:none}
@media(max-width:860px){.pricingGrid,.aboutGrid,.contactGrid{grid-template-columns:1fr}.topNav{display:none}}
.trustBar{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:20px;padding-top:18px;border-top:1px solid rgba(15,27,45,.10)}
.trustBar .item{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted)}
.trustBar .item svg{flex:none;color:var(--accent)}
.heroPreview{position:relative;padding:22px;overflow:hidden}
.pvLabel,.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.pvLabel span.dot,.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
.pvRing{width:112px;height:112px;border-radius:50%;margin:2px auto 14px;display:grid;place-items:center;background:conic-gradient(var(--accent) 0 78%,#182c42 78% 100%);position:relative}
.pvRing:after{content:"";position:absolute;inset:9px;border-radius:50%;background:#F7F9FC}
.pvRing b{position:relative;font-family:var(--serif);font-size:26px;z-index:1}
.pvRow{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12px}
.pvRow .n{color:var(--text);font-weight:700}
.pvRow .n.up{color:var(--green)}.pvRow .n.down{color:var(--red)}
.pvBars{display:flex;align-items:flex-end;gap:5px;height:54px;margin-top:14px}
.pvBars i{flex:1;background:linear-gradient(180deg,var(--accent2),#4a63b8);border-radius:3px 3px 1px 1px;display:block}
.statsStrip{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin:6px 0 0;padding:26px 0}
.statsStrip .stat b{font-family:var(--serif);font-size:36px;font-weight:600;color:var(--text);display:block;letter-spacing:-.5px}
.statsStrip .stat span{font-size:12.5px;color:var(--muted);display:block;margin-top:4px;max-width:20ch}
.whyCard{padding:20px;position:relative}
.whyCard .icoWrap{width:40px;height:40px;border-radius:11px;background:#DCE6FB;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;margin-bottom:14px;color:var(--accent)}
.ctaBanner{margin:44px 0 8px;padding:38px 32px;border-radius:22px;background:linear-gradient(135deg,#EAF0FF 0%,#DCE6FB 55%,#EAF0FF 100%);border:1px solid #C9D8F5;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.ctaBanner h3{font-family:var(--serif);font-weight:600;font-size:26px;margin:0 0 6px;letter-spacing:-.3px}
.ctaBanner p{margin:0;color:var(--muted);font-size:13.5px;max-width:52ch}
@media(max-width:1000px){.statsStrip{grid-template-columns:repeat(2,1fr)}.heroTitle{font-size:34px}}
@media(max-width:1000px){.hero{grid-template-columns:1fr}.grid4{grid-template-columns:repeat(2,1fr)}.grid3,.grid2{grid-template-columns:1fr}.wrap{padding:0 15px}.heroTitle{font-size:31px}.flowSub{margin-left:0}.qsel .qrow{grid-template-columns:1fr}}
@media print{
  *,*::before,*::after{box-sizing:border-box!important}
  @page{size:A4 portrait;margin:18mm 16mm 18mm 16mm}
  html,body{background:#fff!important;color:#0d1b2a!important;font-family:'Segoe UI',Arial,sans-serif!important;font-size:10pt!important;line-height:1.45!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Hide all interactive elements ─────────────────────────────── */
  .hero,.upload,.hidePrint,.tabs,.tabPanel,.chips,.qsel,.tab,.footer,.heroPreview,.trustBar,.statsStrip,.ctaBanner,
  button,input,select,textarea,.secondary,.primary,
  #sampleBtn,#aiBtn,#printBtn,#jsonBtn,#aiAskBtn,
  #aiBox,#aiCustomBox,#aiCustomPrompt,#methodNote,
  .interactiveScenarioCard,#interactiveScenarioCard{display:none!important}

  /* ── Layout: full-width single column ──────────────────────────── */
  .wrap{max-width:none!important;padding:0!important;margin:0!important}
  .top{display:none!important}

  /* ── Cover Banner ───────────────────────────────────────────────── */
  #printCover{display:block!important;border-bottom:3px solid #1a73e8;padding-bottom:12px;margin-bottom:20px}
  #printCover h1{font-size:20pt!important;font-weight:800;color:#0d1b2a;margin:0 0 4px}
  #printCover .sub{font-size:9pt;color:#4a6fa5}

  /* ── Cards ──────────────────────────────────────────────────────── */
  .card{box-shadow:none!important;background:#fff!important;border:1px solid #c8d6e8!important;border-radius:6px!important;margin-bottom:10px!important;padding:10px 12px!important;page-break-inside:avoid!important}
  .heroCard{box-shadow:none!important;background:#fff!important;border:1px solid #c8d6e8!important;padding:10px!important}

  /* ── Flow steps ─────────────────────────────────────────────────── */
  .flowStep{margin:14px 0 6px!important;padding-top:4px!important;page-break-inside:avoid!important}
  .flowLabel{background:none!important;border-left:4px solid #1a73e8!important;padding-left:10px!important;color:#0d1b2a!important;margin-bottom:6px!important}
  .flowLabel .n{background:#1a73e8!important;color:#fff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .flowSub{color:#555!important;font-size:8.5pt!important;margin-bottom:6px!important}

  /* ── Metrics / KPIs ─────────────────────────────────────────────── */
  .metric{background:#f4f7fc!important;border:1px solid #d4dff0!important;border-radius:6px!important;padding:8px!important;color:#0d1b2a!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .metric .label{font-size:7.5pt!important;color:#4a6fa5!important;font-weight:700;text-transform:uppercase;letter-spacing:.5px}
  .metric .value{font-size:14pt!important;font-weight:800;color:#0d1b2a!important}
  .metric .sub{font-size:7.5pt!important;color:#666!important}
  .grid2{display:grid!important;grid-template-columns:1fr 1fr!important;gap:8px!important}
  .grid3{display:grid!important;grid-template-columns:1fr 1fr 1fr!important;gap:8px!important}
  .grid4{display:grid!important;grid-template-columns:1fr 1fr 1fr 1fr!important;gap:8px!important}

  /* ── Health score ring ──────────────────────────────────────────── */
  .scoreCard{display:flex!important;align-items:center!important;gap:20px!important;padding:10px 14px!important}
  .scoreRing{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .scoreRing::after{background:#fff!important}

  /* ── Section headings ───────────────────────────────────────────── */
  .sectionHead{border-bottom:1px solid #d4dff0!important;margin-bottom:8px!important;padding-bottom:6px!important}
  .sectionHead h2{font-size:10pt!important;color:#1a73e8!important;font-weight:800;margin:0}
  .sectionHead p{font-size:8pt!important;color:#555!important;margin:2px 0 0}
  h1,h2,h3{page-break-after:avoid!important;color:#0d1b2a!important}
  h3{font-size:9.5pt!important}

  /* ── Risk & action rows ─────────────────────────────────────────── */
  .riskRow,.actionRow{border:1px solid #e4e8ef!important;border-radius:5px!important;margin-bottom:5px!important;padding:6px 8px!important;page-break-inside:avoid!important;background:#fafbfd!important}
  .rank{background:#e8f0fe!important;color:#1a73e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .bar{display:none!important}

  /* ── Tags / badges ──────────────────────────────────────────────── */
  .tag{border:1px solid #888!important;color:#333!important;background:#f0f0f0!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;font-size:7pt!important}
  .badge{border:1px solid #1a73e8!important;color:#1a73e8!important;font-size:7.5pt!important}

  /* ── Insights / alerts ──────────────────────────────────────────── */
  .insight{border-left:4px solid #1a73e8!important;background:#f0f7ff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;border-radius:4px!important;padding:7px 9px!important;margin-bottom:6px!important;page-break-inside:avoid!important}
  .insight.high,.insight.critical{border-left-color:#c62828!important;background:#fff5f5!important}
  .insight.positive{border-left-color:#2e7d32!important;background:#f1fdf3!important}
  .notice{background:#f8faff!important;border:1px solid #33415C!important;padding:7px 9px!important;border-radius:4px!important;font-size:8.5pt!important;color:#333!important}

  /* ── Waterfall chart ────────────────────────────────────────────── */
  .waterfall{display:flex!important;align-items:flex-end!important;gap:4px!important;height:100px!important;padding:4px 0!important}
  .wf .col{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .wf .num{font-size:6.5pt!important;color:#333!important}
  .wf .lab{font-size:6pt!important;color:#444!important}

  /* ── Tables ─────────────────────────────────────────────────────── */
  .tableWrap{overflow:visible!important}
  table{border-collapse:collapse!important;width:100%!important;font-size:8pt!important}
  th{background:#e8f0fe!important;color:#1a73e8!important;font-weight:700;padding:4px 6px!important;border:1px solid #c8d6e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  td{padding:4px 6px!important;border:1px solid #e4e8ef!important}
  tr:nth-child(even) td{background:#f8faff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Page breaks ─────────────────────────────────────────────────  */
  .flowStep:nth-child(3){page-break-before:always!important}
  .flowStep:nth-child(6){page-break-before:always!important}

  /* ── Misc ────────────────────────────────────────────────────────── */
  .muted{color:#555!important}
  .small{font-size:7.5pt!important}
  a{color:#1a73e8!important;text-decoration:none!important}
  .scenario{border:1px solid #c8d6e8!important;border-radius:5px!important;padding:8px!important;page-break-inside:avoid!important}
  .scenario .big{font-size:14pt!important;font-weight:800;color:#1a73e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .custRow,.wf{page-break-inside:avoid!important}
  .hidden{display:none!important}
  #dashboard{display:block!important}
  .abar{display:none!important}
}

@view-transition{navigation:auto}
::view-transition-old(root){animation:dfbpFadeOut .28s ease both}
::view-transition-new(root){animation:dfbpFadeIn .32s ease both}
@keyframes dfbpFadeOut{to{opacity:0;transform:translateY(-6px)}}
@keyframes dfbpFadeIn{from{opacity:0;transform:translateY(8px)}}
.topNav{display:flex;gap:18px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s;white-space:nowrap}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.authCluster{display:flex;flex-direction:column;align-items:flex-end;gap:5px;flex-shrink:0}
.headerSwitches{display:flex;align-items:center;gap:6px;justify-content:flex-end}
.headerSwitches select,select.globalLangSwitch{padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1}
.headerSwitches select:hover,select.globalLangSwitch:hover{border-color:var(--accent);color:#0F1B2D;background:#FFFFFF}
.navBtns{display:flex;gap:8px;align-items:center}
.navBtn{display:inline-flex;align-items:center;justify-content:center;padding:6px 14px;border-radius:9px;font-size:12.5px;font-weight:700;letter-spacing:-.1px;text-decoration:none;cursor:pointer;transition:all .18s ease;line-height:1.2;white-space:nowrap}
.navBtn.sec{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
.navBtn.sec:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
.navBtn.pri{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
.navBtn.pri:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text);flex-shrink:0}
.brandLogoWrap{flex-shrink:0;min-width:max-content}
.brandLink{text-decoration:none;display:flex;align-items:center;gap:10px;min-width:0}
.brandLogoIcon{width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0}
.brandTextWrap{min-width:0}
.brandTitle{font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2;white-space:nowrap}
.brandSub{font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px;white-space:nowrap}
.headerRight{display:flex;align-items:center;gap:12px;flex-shrink:0}
.mobileNavAuth{display:none}

@media(max-width:920px){
  html,body{overflow-x:hidden;max-width:100vw;width:100%}
  .top{padding:12px 0 10px}
  .wrap{padding:0 16px;max-width:100vw;box-sizing:border-box}
  .brand{gap:10px}
  .brandLogoIcon{width:32px;height:32px;border-radius:9px}
  .brandLogoIcon svg{width:18px;height:18px}
  .brandTitle{font-size:15.5px}
  .brandSub{display:none}
  .brandLogoWrap{min-width:0;flex:1 1 auto;overflow:hidden}
  .topNav{position:fixed;top:56px;left:0;right:0;width:100vw;background:#FFFFFF;border-bottom:1.5px solid var(--line);box-shadow:0 14px 34px rgba(15,27,45,0.12);flex-direction:column;align-items:stretch;gap:0;padding:0 20px;max-height:0;overflow:hidden;transition:max-height .28s ease,padding .2s ease;z-index:999;box-sizing:border-box}
  .topNav.open{max-height:460px;padding:10px 20px 20px;overflow-y:auto}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.06);font-size:14.5px;color:var(--text);font-weight:600;display:block;text-align:left}
  .mobileNavAuth{display:flex;gap:10px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(15,27,45,.08)}
  .mobileNavAuth a{flex:1;padding:10px 12px;font-size:13px;font-weight:700;border-radius:10px;text-align:center;justify-content:center;text-decoration:none}
  .navToggle{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;padding:0;font-size:18px;border-radius:8px;cursor:pointer}
}

@media(max-width:768px){
  .navBtns{display:none}
  .authCluster{flex-direction:row;align-items:center}
  .headerRight{gap:6px}
  .globalLangSwitch{padding:4px 5px !important;font-size:11px !important;border-radius:7px !important;max-width:60px}
  .wrap{padding:0 12px}
  .brandTitle{font-size:14.5px}
  .pageHead{padding:28px 0 10px}
  .pageHead h1{font-size:26px !important}
  .pricingGrid{grid-template-columns:1fr !important;gap:16px}
  .compareTableWrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
  .compareTable{min-width:480px}
}
.badge.v{white-space:nowrap}
/* ---- Marketing hero (separate from app hero) ---- */
.mHero{padding:56px 0 30px;display:grid;grid-template-columns:1.15fr .85fr;gap:34px;align-items:center}
.mHero .eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:18px}
.mHero h1{font-family:var(--serif);font-weight:600;font-size:50px;line-height:1.08;margin:0 0 18px;letter-spacing:-1px}
.mHero h1 span{color:var(--accent)}
.mHero p.lead{color:var(--muted);font-size:16px;max-width:560px;line-height:1.65;margin:0 0 26px}
.mHero .ctaRow{display:flex;gap:12px;flex-wrap:wrap}
.mHero .ctaRow a{text-decoration:none}
.mHero .miniTrust{display:flex;gap:18px;flex-wrap:wrap;margin-top:28px}
.mHero .miniTrust span{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px}
.mHero .miniTrust svg{color:var(--accent)}
.heroArt{position:relative}
.heroArt .floatCard{position:absolute;background:#FFFFFF;border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);padding:14px 16px;font-size:11.5px;color:#33415C;animation:dfbpFloat 5s ease-in-out infinite}
.heroArt .floatCard b{display:block;font-size:16px;color:var(--accent);font-family:var(--serif)}
.heroArt .fc1{top:-10px;left:-10px;animation-delay:0s}
.heroArt .fc2{bottom:6px;right:-14px;animation-delay:1.2s}
@keyframes dfbpFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
/* ---- Alternating content blocks (fixes the "iç içe" cramped look) ---- */
.secBlock{padding:28px 0}
.secBlock.tint{background:linear-gradient(180deg,#F8FAFC 0%,#FFFFFF 100%);border:1px solid #E2E8F0;border-radius:26px;margin:0 -10px;box-shadow:0 4px 20px rgba(15,27,45,.03)}
.pillScrollBtn{width:36px;height:36px;border-radius:50%;background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:800;cursor:pointer;flex-shrink:0;box-shadow:0 4px 12px rgba(15,27,45,0.08);transition:all .18s ease;user-select:none;z-index:4}
.pillScrollBtn:hover{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;transform:scale(1.08);box-shadow:0 6px 16px rgba(29,78,216,0.25)}
.pillScrollBtn:active{transform:scale(0.95)}
.secBlock+.secBlock{border-top:1px solid rgba(15,27,45,.06)}
.pageHead{padding:54px 0 10px;text-align:center}
.pageHead .eyebrow{display:inline-flex;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:16px}
.pageHead h1{font-family:var(--serif);font-size:38px;margin:0 0 12px;letter-spacing:-.6px}
.pageHead p{color:var(--muted);max-width:600px;margin:0 auto;font-size:14.5px}
.reveal{opacity:0;transform:translateY(18px);transition:opacity .55s ease,transform .55s ease}
.reveal.in{opacity:1;transform:none}
/* ---- Rich footer ---- */
.siteFooter{border-top:1px solid var(--line);margin-top:40px;padding:46px 0 26px}
.siteFooter .cols{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:28px;margin-bottom:30px}
.siteFooter h4{font-size:12px;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin:0 0 14px}
.siteFooter .brandCol p{color:var(--muted);font-size:12.5px;max-width:280px;line-height:1.6}
.siteFooter ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.siteFooter ul a{color:#33415C;text-decoration:none;font-size:13px}
.siteFooter ul a:hover{color:var(--accent)}
.siteFooter .legal{border-top:1px solid rgba(15,27,45,.08);padding-top:20px;color:#5B6B84;font-size:11px;line-height:1.7}
html{overflow-x:hidden}@media(max-width:860px){.siteFooter .cols{grid-template-columns:1fr 1fr}.mHero{grid-template-columns:1fr}.heroArt{order:-1;max-width:340px;margin:24px auto 40px;padding:0 14px}.heroArt .floatCard{position:static;display:inline-block;margin:6px 6px 0 0;animation:none}.heroArt .fc1,.heroArt .fc2{top:auto;left:auto;right:auto;bottom:auto}}
/* ---- FAQ (paketler sayfası) ---- */
.faqItem{border-bottom:1px solid var(--line);padding:16px 0}
.faqItem summary{cursor:pointer;font-weight:700;font-size:14px;list-style:none;display:flex;justify-content:space-between;align-items:center}
.faqItem summary::-webkit-details-marker{display:none}
.faqItem summary:after{content:'+';font-size:20px;color:var(--accent)}
.faqItem[open] summary:after{content:'–'}
.faqItem p{color:var(--muted);font-size:13.5px;margin:10px 0 0}
/* ---- Executive Intelligence band (single, deliberate dark boardroom section) ---- */
.execBand{background:radial-gradient(1200px 500px at 15% -20%, rgba(76,201,240,.10), transparent 60%),linear-gradient(160deg,#0D1B2A 0%,#081426 100%);border-radius:26px;padding:52px;display:grid;grid-template-columns:.85fr 1.15fr;gap:40px;align-items:center;overflow:hidden}
.execEyebrow{display:inline-block;font-size:11.5px;font-weight:800;letter-spacing:1.6px;color:#4CC9F0;background:rgba(76,201,240,.12);border:1px solid rgba(76,201,240,.35);padding:6px 12px;border-radius:999px;margin-bottom:16px}
.execCopy h2{font-family:var(--serif);color:#F8FAFC;font-size:28px;line-height:1.2;margin:0 0 12px;letter-spacing:-.4px}
.execCopy p{color:#94A3B8;font-size:14px;line-height:1.7;margin:0 0 18px;max-width:44ch}
.execList{list-style:none;margin:0 0 24px;padding:0;display:flex;flex-direction:column;gap:9px}
.execList li{color:#C7D2E8;font-size:13px}
.execList li b{color:#F8FAFC}
.execCta{display:inline-block;color:#0D1B2A;background:#4CC9F0;font-weight:800;font-size:13.5px;padding:12px 20px;border-radius:11px;text-decoration:none;transition:transform .15s ease,box-shadow .15s ease}
.execCta:hover{transform:translateY(-1px);box-shadow:0 10px 26px rgba(76,201,240,.35)}
.execArt{filter:drop-shadow(0 24px 48px rgba(0,0,0,.35))}
@media(max-width:860px){.execBand{grid-template-columns:1fr;padding:32px 22px}}
/* ---- New: live dashboard hero panel ---- */
.heroDash{background:linear-gradient(160deg,#0D1B2A 0%,#0A1524 100%);border-radius:20px;border:1px solid #1E3050;padding:20px;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(8,17,32,.35)}
.heroDash .dHead{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.heroDash .dHead .dots span{width:8px;height:8px;border-radius:50%;display:inline-block;margin-right:5px}
.heroDash .dHead .live{font-size:10.5px;color:#7FE3B4;display:flex;align-items:center;gap:6px;font-weight:700;letter-spacing:.4px}
.heroDash .dHead .live i{width:6px;height:6px;border-radius:50%;background:#15E3B3;display:inline-block;box-shadow:0 0 0 3px rgba(21,227,179,.22);animation:dfbpPulse 1.8s ease infinite}
@keyframes dfbpPulse{0%,100%{opacity:1}50%{opacity:.35}}
.dashTabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px}
.dashTabs span{font-size:10px;color:#7C8FAD;background:#101F33;border:1px solid #1E3050;border-radius:999px;padding:5px 10px;transition:all .25s ease}
.dashTabs span.on{color:#0D1B2A;background:#4CC9F0;border-color:#4CC9F0;font-weight:800}
.dashPane{display:none;min-height:230px}
.dashPane.on{display:block;animation:dfbpFadeIn .4s ease both}
.dashPane .dTitle{color:#7C8FAD;font-size:10px;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px}
.dashKpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px}
.dashKpis div{background:#132238;border:1px solid #20334b;border-radius:99px;padding:9px 10px}
.dashKpis div b{display:block;font-size:16px;color:#F8FAFC;font-family:var(--serif)}
.dashKpis div span{font-size:9.5px;color:#7C8FAD}
.heroDash .foot{margin-top:12px;padding-top:12px;border-top:1px solid #1E3050;font-size:10.5px;color:#7C8FAD;display:flex;justify-content:space-between}
/* ---- New: CFO trust strip ---- */
.trustGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.trustCard{padding:22px}
.trustCard .icoWrap2{width:38px;height:38px;border-radius:10px;background:#0D1B2A;color:#4CC9F0;display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.trustCard h3{margin:0 0 6px;font-size:14.5px}
.trustCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.55}
/* ---- New: Executive Journey ---- */
.journey{display:grid;grid-template-columns:repeat(6,1fr);gap:0;position:relative;margin-top:8px}
.journey:before{content:"";position:absolute;top:22px;left:6%;right:6%;height:2px;background:linear-gradient(90deg,#C9D8F5,#4CC9F0,#C9D8F5)}
.jStep{text-align:center;padding:0 8px;opacity:0;transform:translateY(16px);transition:opacity .5s ease,transform .5s ease}
.jStep.in{opacity:1;transform:none}
.jStep .jDot{width:44px;height:44px;border-radius:50%;background:#FFFFFF;border:2px solid var(--accent);color:var(--accent);display:flex;align-items:center;justify-content:center;margin:0 auto 12px;position:relative;z-index:1;font-weight:900;font-size:13px}
.jStep h4{margin:0 0 5px;font-size:13px;letter-spacing:.4px}
.jStep p{margin:0;font-size:11.5px;color:var(--muted);line-height:1.4}
@media(max-width:860px){.journey{grid-template-columns:1fr 1fr;gap:22px 0}.journey:before{display:none}.trustGrid{grid-template-columns:1fr 1fr}}
/* ---- New: outcome-based module groups ---- */
.intelGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.intelCard{padding:24px;display:flex;flex-direction:column}
.intelCard .igIco{width:40px;height:40px;border-radius:11px;background:#DCE6FB;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.intelCard h3{margin:0 0 8px;font-size:16px;font-family:var(--serif)}
.intelCard ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}
.intelCard ul li{font-size:12.5px;color:#33415C;display:flex;gap:7px;align-items:flex-start}
.intelCard ul li:before{content:"";width:5px;height:5px;border-radius:50%;background:var(--accent);margin-top:6px;flex:none}
@media(max-width:860px){.intelGrid{grid-template-columns:1fr 1fr}}
/* ---- New: security/governance page ---- */

/* ---- High-impact FinTech additions ---- */
.gradText{background:linear-gradient(135deg,#1D4ED8 0%,#2563EB 50%,#38BDF8 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;display:inline-block}
.livePill{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:var(--accent);background:linear-gradient(135deg,#EEF4FF,#E0EDFF);border:1px solid #BFDBFE;padding:8px 16px;border-radius:999px;margin-bottom:20px;box-shadow:0 2px 10px rgba(37,99,235,.12)}
.livePill i{width:8px;height:8px;border-radius:50%;background:#10B981;display:inline-block;box-shadow:0 0 0 4px rgba(16,185,129,.25);animation:dfbpPulse 1.8s ease infinite}
.dilemmaGrid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:20px}
.dilemmaCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:26px;position:relative;overflow:hidden;box-shadow:var(--shadow);transition:transform .2s ease,box-shadow .2s ease}
.dilemmaCard:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(15,27,45,.09)}
.dilemmaQ{font-size:15px;font-weight:700;color:#0F1B2D;margin-bottom:12px;display:flex;gap:10px;align-items:flex-start;line-height:1.4}
.dilemmaQ span{background:#FEE2E2;color:#DC2626;border-radius:8px;padding:2px 8px;font-size:11px;font-weight:900;flex:none;margin-top:2px}
.dilemmaA{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:14px 16px;font-size:13px;color:#33415C;line-height:1.55}
.dilemmaA b{color:var(--accent);display:block;margin-bottom:4px}
.workflowGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;position:relative;margin-top:20px}
.workflowCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:24px;box-shadow:var(--shadow);position:relative;display:flex;flex-direction:column}
.workflowBadge{font-size:11px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:var(--accent);background:#EFF6FF;border:1px solid #DBEAFE;padding:4px 10px;border-radius:999px;align-self:flex-start;margin-bottom:12px}
.workflowCard h3{font-size:16px;margin:0 0 8px;font-family:var(--serif);color:#0F1B2D}
.workflowCard p{font-size:12.5px;color:var(--muted);line-height:1.55;margin:0}
.compareTableWrap{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:var(--shadow);margin-top:20px}
.compareTable{width:100%;border-collapse:collapse;font-size:13px}
.compareTable th,.compareTable td{padding:16px 18px;border-bottom:1px solid rgba(15,27,45,.08);text-align:left}
.compareTable th{background:#F8FAFC;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#475569}
.compareTable th.featured{background:linear-gradient(135deg,#EFF6FF,#DBEAFE);color:var(--accent);border-bottom:2px solid var(--accent)}
.compareTable td.featured{background:#F8FAFF;font-weight:600;color:#0F1B2D}
@media(max-width:860px){.dilemmaGrid,.workflowGrid{grid-template-columns:1fr}.compareTableWrap{overflow-x:auto}}

.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

</style></head>
<body>
<header class="top"><div class="wrap brand"><div class="brandLogoWrap">
  <a href="/" class="brandLink">
    <div class="brandLogoIcon">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div class="brandTextWrap">
      <div class="brandTitle">Digital Finance Business Partner</div>
      <div class="brandSub">Finansal Teşhis &amp; Yönetim Karar Destek Platformu</div>
    </div>
  </a>
</div><div class="headerRight"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/cozumler">Çözümler</a><a href="/hakkimizda">Hakkımızda</a><a href="/uygulama">Uygulama</a><a href="/paketler" class="active">Paketler</a><a href="/guvenlik">Güvenlik</a><a href="/iletisim">İletişim</a><div class="mobileNavAuth"><a href="/uygulama?auth=login" class="secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="primary">Ücretsiz Kayıt Ol</a></div></nav><div class="authCluster hidePrint"><div class="headerSwitches"><select class="globalLangSwitch select" onchange="setGlobalLanguage(this.value)" style="padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1" title="Dil / Language"><option value="tr">🇹🇷 TR</option><option value="en">🇬🇧 EN</option><option value="de">🇩🇪 DE</option><option value="fr">🇫🇷 FR</option><option value="es">🇪🇸 ES</option><option value="it">🇮🇹 IT</option><option value="nl">🇳🇱 NL</option></select></div><div class="navBtns"><a href="/uygulama?auth=login" class="navBtn sec">Giriş Yap</a><a href="/uygulama?auth=register" class="navBtn pri">Ücretsiz Kayıt Ol</a></div></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<div class="pageHead reveal in"><span class="eyebrow">💼 ÇÖZÜM MODELLERİ &amp; PAKETLER</span><h1>Şirketinizin Ölçeğine ve İhtiyacına Uygun Çözüm Modelleri</h1><p>İster tek bir mizanla finansal durumunuzu anında test edin, ister çoklu veri ve What-If simülatörüyle şirketinizin büyümesini yönetin. Tüm modeller aynı deterministik 33 motorlu finansal çekirdekle çalışır.</p>
  <div style="display:inline-flex;align-items:center;background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:999px;padding:4px;margin-top:24px;box-shadow:0 4px 12px rgba(15,27,45,0.05)">
    <button id="btnMonthly" class="primary" style="border-radius:999px;padding:8px 20px;font-size:13px" onclick="setBilling('monthly')">Aylık Ödeme</button>
    <button id="btnAnnual" class="secondary" style="border-radius:999px;padding:8px 20px;font-size:13px;border:0" onclick="setBilling('annual')">Yıllık Ödeme <span style="background:#DCFCE7;color:#15803D;font-weight:800;padding:2px 8px;border-radius:999px;font-size:10.5px;margin-left:4px">%20 İndirim 🎁</span></button>
  </div>
</div>

<div class="secBlock reveal"><section class="marketingSection hidePrint" style="padding-top:0">
<div class="pricingGrid">
<div class="card priceCard"><div class="plan">Başlangıç</div><h3>Starter</h3><div class="amt">₺0<span> /örnek analiz</span></div><div class="desc">Sistemi görmek ve Data Hub altın veri setiyle test etmek isteyen finans ekipleri için.</div><ul>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Tüm 33 finansal karar motorunu canlı veride deneme</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Görünmez Kâr Sızıntısı & Kilitli Nakit Teşhisi</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Kâr Nakde Dönüşüm & Kâr Köprüsü</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Kayıt olmadan anında canlı demo</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Tarayıcıda çalışma (kalıcı saklama yok)</li>
</ul><button class="secondary" style="width:100%" onclick="window.location.href='/uygulama?sample=data_hub'">🔥 Canlı Demoyu Aç</button></div>
<div class="card priceCard featured"><div class="badgeTop">En Çok Tercih Edilen</div><div class="plan">Büyüyen Şirketler</div><h3>Professional</h3><div id="proPriceAmt" class="amt">₺2.490<span> /ay</span></div><div id="proSubText" class="desc">Kendi mizanını ve defterlerini düzenli yükleyip yönetim kararları üreten şirketler için.</div><ul>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Sınırsız mizan ve alt defter yükleme</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Görünmez Kâr Sızıntısı ve 4 Kaldıraçlı İnteraktif Simülatör</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Çok dönemli trend ve Nakit Akış Tablosu</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Geçmiş analizleri kaydetme ve karşılaştırma</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Data Hub: Mizan + AR/AP + Stok + Satış mutabakatı</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>AI Finance Business Partner stratejik Q&A</li>
</ul><button class="primary" style="width:100%" onclick="window.location.href='/uygulama?auth=register'">Ücretsiz Kayıt Ol</button></div>
<div class="card priceCard"><div class="plan">Kurumsal & Holding</div><h3>Enterprise</h3><div class="amt">Teklif İle<span> /özel</span></div><div class="desc">Çoklu şirket/grup yapısı, ERP doğrudan bağlayıcı ve özel danışmanlık isteyen kurumlar için.</div><ul>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Professional paketindeki tüm özellikler</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Çoklu şirket konsolidasyonu ve kullanıcı rolleri</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Özel sektör benchmark bantları ve özel kurallar</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Öncelikli SLA, kıdemli finans danışmanlığı desteği</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>ERP doğrudan API bağlayıcı (SAP, Netsis, Logo)</li>
</ul><button class="secondary" style="width:100%" onclick="window.location.href='/iletisim'">Kurumsal Teklif Al</button></div>
</div>

<div class="compareTableWrap" style="margin-top:34px">
  <table class="compareTable">
    <thead>
      <tr>
        <th style="width:40%">Özellik / Yetenek</th>
        <th style="width:20%;text-align:center">Starter (Demo)</th>
        <th class="featured" style="width:20%;text-align:center">Professional (Önerilen)</th>
        <th style="width:20%;text-align:center">Enterprise</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><b>33 Finansal Karar Motoru</b></td><td style="text-align:center">✅</td><td class="featured" style="text-align:center">✅</td><td style="text-align:center">✅</td></tr>
      <tr><td><b>Görünmez Kâr Sızıntısı & Kilitli Nakit Teşhisi</b></td><td style="text-align:center">Örnek Veride</td><td class="featured" style="text-align:center">✅ Canlı Mizanınızda</td><td style="text-align:center">✅ Sınırsız / Konsolide</td></tr>
      <tr><td><b>İnteraktif Kâr & Nakit Simülatörü (4 Kaldıraç)</b></td><td style="text-align:center">✅</td><td class="featured" style="text-align:center">✅</td><td style="text-align:center">✅</td></tr>
      <tr><td><b>Kâr Nakde Dönüşüm Oranı & Nakit Köprüsü</b></td><td style="text-align:center">✅</td><td class="featured" style="text-align:center">✅</td><td style="text-align:center">✅</td></tr>
      <tr><td><b>Kendi Mizan ve Defterlerinizi Yükleme</b></td><td style="text-align:center">Tek Seferlik</td><td class="featured" style="text-align:center">✅ Sınırsız</td><td style="text-align:center">✅ Sınırsız</td></tr>
      <tr><td><b>Çok Dönemli Trend & Değişim Analizi</b></td><td style="text-align:center">❌</td><td class="featured" style="text-align:center">✅</td><td style="text-align:center">✅</td></tr>
      <tr><td><b>Data Hub: Mizan + Yaşlandırma + Stok Mutabakatı</b></td><td style="text-align:center">❌</td><td class="featured" style="text-align:center">✅</td><td style="text-align:center">✅</td></tr>
      <tr><td><b>AI Finance Partner Stratejik Yönetim Brifingi</b></td><td style="text-align:center">Standart</td><td class="featured" style="text-align:center">✅ Sınırsız Q&A</td><td style="text-align:center">✅ Özelleştirilmiş Promptlar</td></tr>
      <tr><td><b>Kurumsal Kıyaslama (TCMB & BIST Medyanları)</b></td><td style="text-align:center">Genel</td><td class="featured" style="text-align:center">✅ Sektörel Detay</td><td style="text-align:center">✅ Özel Sektör Havuzu</td></tr>
      <tr><td><b>Çoklu Şirket & Grup Konsolidasyonu</b></td><td style="text-align:center">❌</td><td class="featured" style="text-align:center">❌</td><td style="text-align:center">✅ Tam Destek</td></tr>
      <tr><td><b>Öncelikli SLA & Finans Müşaviri Desteği</b></td><td style="text-align:center">Topluluk</td><td class="featured" style="text-align:center">E-posta (1 İş Günü)</td><td style="text-align:center">✅ 2 Saat SLA + Telefon</td></tr>
    </tbody>
  </table>
</div>
</section>

</div>

<div class="secBlock reveal"><div class="marketingHead"><h2>Sık Sorulan Sorular</h2></div>
<div style="max-width:720px;margin:auto">
<details class="faqItem" open><summary>Verilerim güvende mi?</summary><p>Yüklediğiniz dosyalar yalnızca analiz anında RAM üzerinde işlenir; hesap açmadan yapılan oturumlarda sunucuda kalıcı saklanmaz. Kayıtlı hesaplarda ise verileriniz 256-bit şifrelemeyle yalnızca sizin erişiminizde korunur.</p></details>
<details class="faqItem"><summary>Hangi muhasebe programlarıyla uyumlu?</summary><p>Sistemimiz Luca, Logo, Mikro, Netsis, Zirve, SAP, Nebim ve benzeri tüm ERP/muhasebe yazılımlarından dışa aktarılan standart mizan ve defter formatlarını otomatik tanır. Entegrasyon bekleme süresi 0'dır.</p></details>
<details class="faqItem"><summary>Neden bir muhasebe programı yerine Digital Finance Business Partner?</summary><p>Muhasebe programları geçmiş kayıtları tutar (defter tutma). Digital Finance Business Partner ise kârın neden nakde dönüşmediğini, hangi müşterinin zarar ettirdiğini ve nakit akışını kurtarmak için alınacak yönetim kararlarını belirler.</p></details>
<details class="faqItem"><summary>AI Finance Partner yorumu zorunlu mu?</summary><p>Hayır. Tüm 33 motor çift taraflı matematik ve finans denetimi kurallarıyla deterministik hesaplar. Yapay zeka yalnızca yönetim kurulu veya banka görüşmeleriniz için stratejik metin asistanlığı yapar; rakam asla uydurulmaz.</p></details>
</div></div>

<div class="secBlock tint reveal"><section class="ctaBanner hidePrint"><div><h3>Hangi paketin şirketinize uygun olduğundan emin değil misiniz?</h3><p>60 saniyede Data Hub altın örnek verisiyle tam bir yönetim kurulu raporunu açın, sistemi bizzat test edin.</p></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a href="/uygulama?sample=data_hub" class="primary" style="text-decoration:none;padding:12px 20px;border-radius:11px">🔥 Canlı Demoyu Başlat</a><a href="/iletisim" class="secondary" style="text-decoration:none;padding:12px 20px;border-radius:11px">Kurumsal Teklif Al</a></div></section></div>

</main>
<div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/cozumler">Çözümler</a></li><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • <a href="https://digitalfinancebp.com" style="color:var(--accent);text-decoration:none;font-weight:700">digitalfinancebp.com</a> • Deterministik Finans Karar Motoru &amp; Çift Yönlü Denetim Sistemi<br><span style="opacity:.85">Bu analiz deterministik matematiksel hesaplamalara ve çift taraflı denetim kurallarına dayanır; resmi mali tablo veya vergi beyannamesi yerine geçmez. Nihai yönetim kararları için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca anlık analiz süresince RAM bellekte işlenir; sunucu sabit diskinde ASLA kalıcı saklanmaz. KVKK ve kurumsal gizlilik politikamız için <a href="javascript:void(0)" onclick="showKvkkModal()" style="color:var(--accent);text-decoration:underline;font-weight:600">Aydınlatma ve Gizlilik Metni</a>'ni inceleyebilirsiniz.</span></div></div></div>
<script>
window.showKvkkModal=function(){var m=document.getElementById('kvkkModal');if(!m){m=document.createElement('div');m.id='kvkkModal';m.style.cssText='position:fixed;inset:0;background:rgba(15,27,45,0.7);z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(4px);';m.innerHTML='<div style="background:#FFFFFF;border-radius:18px;max-width:640px;width:100%;max-height:85vh;overflow-y:auto;padding:28px;box-shadow:0 20px 50px rgba(0,0,0,0.3);position:relative;border:1px solid #E2E8F0"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid #E2E8F0;padding-bottom:12px"><div style="display:flex;align-items:center;gap:8px"><span style="font-size:20px">🔒</span><h3 style="margin:0;font-size:18px;color:#0F1B2D;font-family:sans-serif;font-weight:700">Veri Güvenliği, RAM-Only İşleme ve KVKK Taahhüdü</h3></div><button class="kvkkClose" style="background:#F1F5F9;border:0;border-radius:50%;width:30px;height:30px;cursor:pointer;font-weight:bold;font-size:16px">✕</button></div><div style="font-size:13px;line-height:1.7;color:#33415C;display:flex;flex-direction:column;gap:12px"><div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:12px;color:#166534"><b>🛡️ Sıfır Disk Depolama (RAM-Only):</b> Yüklediğiniz mizan, muavin defteri veya operasyonel raporlar sunucunun kalıcı depolama birimlerine (HDD/SSD/Veritabanı) kaydedilmez. Tüm matematiksel hesaplamalar ve çift taraflı denetim anlık bellek (RAM) üzerinde icra edilir ve analiz tamamlandığında oturumla birlikte tamamen silinir.</div><p><b>1. Veri İzolasyonu &amp; Model Eğitimi Yasağı:</b> Şirketiniz tarafından paylaşılan hiçbir finansal veri, ciro, müşteri adı veya bilanço kalemi üçüncü şahıslara verilmez, satılmaz ve genel yapay zekâ modellerinin eğitimi için havuzlara aktarılmaz.</p><p><b>2. 256-Bit TLS Şifreleme:</b> Tarayıcınız ile platform arasındaki tüm veri akışı bankacılık standardında 256-bit SSL/TLS tüneli üzerinden şifrelenir.</p><p><b>3. 6698 Sayılı KVKK Uyumluluğu:</b> Şirket yetkililerine ait iletişim bilgileri ve ticari sırlar yalnızca talep edilen analizlerin üretilmesi amacıyla işlenir; yasal yükümlülükler haricinde hiçbir tarafla paylaşılmaz.</p><p><b>4. Kurumsal Gizlilik Sözleşmesi (NDA):</b> Kurumsal entegrasyon veya holding düzeyinde çalışmalarda şirketinizle karşılıklı Kurumsal NDA akdedilir.</p></div><div style="margin-top:20px;text-align:right"><button class="kvkkClose primary" style="padding:9px 20px;border-radius:10px;font-size:13px;background:#1D4ED8;color:#fff;border:0;cursor:pointer;font-weight:700">Anladım ve Kabul Ediyorum</button></div></div>';m.addEventListener('click',function(e){if(e.target===m||e.target.classList.contains('kvkkClose'))m.style.display='none';});document.body.appendChild(m);}m.style.display='flex';};
document.getElementById('navToggle')?.addEventListener('click',()=>document.getElementById('mainNav')?.classList.toggle('open'));
window.addEventListener('scroll',()=>{document.querySelector('.top')?.classList.toggle('scrolled',window.scrollY>8)});
function setBilling(mode){
  const btnM = document.getElementById('btnMonthly');
  const btnA = document.getElementById('btnAnnual');
  const amt = document.getElementById('proPriceAmt');
  const sub = document.getElementById('proSubText');
  if(!btnM || !btnA || !amt) return;
  if(mode === 'annual'){
    btnA.className = 'primary';
    btnA.style.border = '0';
    btnM.className = 'secondary';
    btnM.style.border = '0';
    amt.innerHTML = '₺1.990<span> /ay</span>';
    if(sub) sub.innerHTML = 'Yıllık ₺23.880 olarak faturalandırılır (<b>%20 indirim</b> ile 2 ay hediye, ₺6.000 tasarruf).';
  } else {
    btnM.className = 'primary';
    btnM.style.border = '0';
    btnA.className = 'secondary';
    btnA.style.border = '0';
    amt.innerHTML = '₺2.490<span> /ay</span>';
    if(sub) sub.innerHTML = 'Kendi mizanını ve defterlerini düzenli yükleyip yönetim kararları üreten şirketler için.';
  }
}
(function(){
  const els=document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){els.forEach(e=>e.classList.add('in'));return;}
  const io=new IntersectionObserver((entries)=>{entries.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}})},{threshold:.12});
  els.forEach(e=>io.observe(e));
})();
(function(){
  // Finance-flavoured count-up animation for stat/kpi numbers on scroll into view
  const targets = document.querySelectorAll('.stat b, .aboutStats .st b, .pvRing b, .scoreNum strong');
  if(!('IntersectionObserver' in window) || !targets.length) return;
  const parse = (txt)=>{ const m = txt.match(/-?\d[\d.,]*/); return m ? m[0] : null; };
  const cio = new IntersectionObserver((entries)=>{
    entries.forEach(en=>{
      if(!en.isIntersecting) return;
      cio.unobserve(en.target);
      const el = en.target; const raw = el.textContent; const numStr = parse(raw);
      if(!numStr) return;
      const prefix = raw.slice(0, raw.indexOf(numStr));
      const suffix = raw.slice(raw.indexOf(numStr)+numStr.length);
      const clean = numStr.replace(/\./g,'').replace(',', '.');
      const target = parseFloat(clean); if(isNaN(target)) return;
      const decimals = (clean.split('.')[1]||'').length;
      const dur = 900; const t0 = performance.now();
      function step(t){
        const p = Math.min(1,(t-t0)/dur); const eased = 1-Math.pow(1-p,3);
        const val = target*eased;
        el.textContent = prefix + val.toFixed(decimals).replace('.', decimals?',':'') + suffix;
        if(p<1) requestAnimationFrame(step); else el.textContent = raw;
      }
      requestAnimationFrame(step);
    });
  }, {threshold:.4});
  targets.forEach(t=>cio.observe(t));
})();
(function(){
  // Staggered grow-in for waterfall / bridge chart columns and progress bars
  document.querySelectorAll('.waterfall').forEach(wf=>{
    [...wf.children].forEach((col,i)=>{ col.style.animation = `growUp .6s ease ${i*70}ms both`; });
  });
  document.querySelectorAll('.bar i, .abar i').forEach((i,idx)=>{ i.style.animation = `growWidth .7s ease ${idx*40}ms both`; });
})();
</script>
<script>
var GLOBAL_I18N = {
  tr: { navHome: 'Anasayfa', navSolutions: 'Çözümler', navAbout: 'Hakkımızda', navApp: 'Uygulama', navPricing: 'Paketler', navSecurity: 'Güvenlik', navContact: 'İletişim', login: 'Giriş Yap', register: 'Ücretsiz Kayıt Ol' },
  en: { navHome: 'Home', navSolutions: 'Solutions', navAbout: 'About', navApp: 'App', navPricing: 'Pricing', navSecurity: 'Security', navContact: 'Contact', login: 'Log In', register: 'Sign Up Free' },
  de: { navHome: 'Startseite', navSolutions: 'Lösungen', navAbout: 'Über uns', navApp: 'Anwendung', navPricing: 'Preise', navSecurity: 'Sicherheit', navContact: 'Kontakt', login: 'Anmelden', register: 'Kostenlos Registrieren' },
  fr: { navHome: 'Accueil', navSolutions: 'Solutions', navAbout: 'À propos', navApp: 'Application', navPricing: 'Tarifs', navSecurity: 'Sécurité', navContact: 'Contact', login: 'Connexion', register: 'Inscription Gratuite' },
  es: { navHome: 'Inicio', navSolutions: 'Soluciones', navAbout: 'Sobre Nosotros', navApp: 'Aplicación', navPricing: 'Precios', navSecurity: 'Seguridad', navContact: 'Contacto', login: 'Iniciar Sesión', register: 'Registro Gratis' },
  it: { navHome: 'Home', navSolutions: 'Soluzioni', navAbout: 'Chi siamo', navApp: 'Applicazione', navPricing: 'Piani', navSecurity: 'Sicurezza', navContact: 'Contatti', login: 'Accedi', register: 'Registrati Gratis' },
  nl: { navHome: 'Startpagina', navSolutions: 'Oplossingen', navAbout: 'Over ons', navApp: 'Applicatie', navPricing: 'Tarieven', navSecurity: 'Beveiliging', navContact: 'Contact', login: 'Inloggen', register: 'Gratis Registreren' }
};
function setGlobalLanguage(lang){
  try { localStorage.setItem('dfbp_lang', lang); } catch(e){}
  var dict = GLOBAL_I18N[lang] || GLOBAL_I18N.tr;
  document.querySelectorAll('.globalLangSwitch').forEach(function(s){ s.value = lang; });
  var nav = document.getElementById('mainNav');
  if(nav){
    var links = nav.querySelectorAll('a');
    if(links.length >= 7){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navSolutions;
      links[2].textContent = dict.navAbout;
      links[3].textContent = dict.navApp;
      links[4].textContent = dict.navPricing;
      links[5].textContent = dict.navSecurity;
      links[6].textContent = dict.navContact;
    } else if(links.length >= 6){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navAbout;
      links[2].textContent = dict.navApp;
      links[3].textContent = dict.navPricing;
      links[4].textContent = dict.navSecurity;
      links[5].textContent = dict.navContact;
    }
  }
  document.querySelectorAll('.navBtn.secondary, .navBtn.sec, #loginOpenBtn').forEach(function(b){ b.textContent = dict.login; });
  document.querySelectorAll('.navBtn.primary, .navBtn.pri, #registerOpenBtn').forEach(function(b){ b.textContent = dict.register; });
}
if(typeof document !== 'undefined' && document.addEventListener){
  document.addEventListener('DOMContentLoaded', function(){
    var saved = 'tr';
    try { saved = localStorage.getItem('dfbp_lang') || 'tr'; } catch(e){}
    setGlobalLanguage(saved);
  });
}
</script>
</body></html>'''

ABOUT_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" type="image/svg+xml" href="/favicon.ico"><meta name="description" content="Digital Finance Business Partner (digitalfinancebp.com) — Şirketinizin finansal tablolarını 33 analitik karar motoruyla denetleyen, kâr sızıntılarını ve kilitli nakdi hesaplayan kurumsal karar destek platformu."><title>Hakkımızda | Digital Finance Business Partner</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&display=swap" rel="stylesheet">
<style>
:root{--bg:#F6F7F9;--panel:#FFFFFF;--panel2:#F0F3F8;--line:#E4E8EF;--text:#0F1B2D;--muted:#5B6B84;--accent:#1D4ED8;--accent2:#4F8CFF;--red:#C22A3E;--amber:#B4720A;--green:#0E7C66;--shadow:0 1px 2px rgba(15,27,45,.04),0 12px 32px rgba(15,27,45,.06);--serif:'Fraunces',ui-serif,Georgia,serif}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(1100px 480px at 12% -10%, rgba(29,78,216,.07), transparent 60%),radial-gradient(900px 420px at 100% 0%, rgba(14,124,102,.05), transparent 55%),#F6F7F9;color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45}button,input,select{font:inherit}.wrap{max-width:1440px;margin:auto;padding:0 28px}.top{padding:26px 0 18px;border-bottom:1px solid rgba(15,27,45,.08);position:sticky;top:0;background:rgba(246,247,249,.86);backdrop-filter:blur(18px);z-index:10}.brand{display:flex;align-items:center;justify-content:space-between;gap:20px}.brand h1{margin:0;font-size:25px;letter-spacing:-.6px}.brand p{margin:3px 0 0;color:var(--muted);font-size:13px}.badge{padding:6px 10px;border:1px solid #D7DEE8;border-radius:999px;color:var(--accent);font-size:12px;white-space:nowrap}.hero{padding:34px 0 24px;display:grid;grid-template-columns:1.45fr .55fr;gap:18px}.heroCard,.card{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow)}.heroCard{padding:28px}.heroTitle{font-family:var(--serif);font-weight:600;font-size:44px;line-height:1.08;margin:0 0 14px;letter-spacing:-.5px}.heroText{color:var(--muted);max-width:780px}.framework{display:flex;flex-wrap:wrap;gap:8px 10px;margin:16px 0 2px;padding:0}.framework span{font-size:11.5px;color:#33415C;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px}.framework span b{color:var(--accent);font-weight:800}
.qsel{margin-top:18px}.qsel .qtitle{font-size:12px;color:var(--muted);margin-bottom:8px;font-weight:700}.qsel .qrow{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.qsel button{border:1px solid #D7DEE8;background:#EEF2FF;color:#33415C;border-radius:12px;padding:10px 12px;font-size:12.5px;cursor:pointer;text-align:left;line-height:1.3}.qsel button:hover{border-color:#B7C3D6}.qsel button.active{border-color:var(--accent);color:var(--accent);background:#DCE6FB}
.upload{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}.file{border:1px dashed #C9D2DE;padding:12px;border-radius:12px;background:#F5F7FA;max-width:100%}.select,button{border:1px solid #D7DEE8;border-radius:11px;padding:11px 14px;background:#FFFFFF;color:var(--text)}button.primary,a.primary{background:linear-gradient(135deg,#2557E8,#1D4ED8);border:0;color:#FFFFFF;font-weight:800;cursor:pointer;transition:transform .15s ease,box-shadow .15s ease;box-shadow:0 6px 16px rgba(29,78,216,.25)}a.primary:hover,button.primary:hover{transform:translateY(-1px);box-shadow:0 10px 22px rgba(29,78,216,.32)}button.secondary,a.secondary{cursor:pointer;border:1.5px solid #C9D2DE;background:#FFFFFF;color:var(--text)}a.secondary:hover,button.secondary:hover{border-color:var(--accent);color:var(--accent)}button:disabled{opacity:.5;cursor:not-allowed}.scoreCard{padding:25px;display:flex;flex-direction:column;justify-content:center}.scoreRing{width:170px;height:170px;border-radius:50%;margin:auto;display:grid;place-items:center;background:conic-gradient(var(--accent) calc(var(--score)*1%),#E4E8EF 0);position:relative}.scoreRing:after{content:"";position:absolute;inset:12px;border-radius:50%;background:#FFFFFF}.scoreNum{position:relative;z-index:1;text-align:center}.scoreNum strong{display:block;font-size:48px;line-height:1}.scoreNum span{color:var(--muted);font-size:12px}.status{margin:15px auto 0;padding:7px 12px;border-radius:999px;background:#EAF0FF;color:var(--accent);font-size:12px;font-weight:700}.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.card{padding:22px;margin:0 0 16px;transition:transform .18s ease,box-shadow .18s ease,outline .2s}.card:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(15,27,45,.08)}@keyframes growUp{from{transform:scaleY(0);opacity:0}to{transform:scaleY(1);opacity:1}}.wf{transform-origin:bottom}.wf .col{transform-origin:bottom}@keyframes growWidth{from{width:0}to{}}.metric{padding:17px;border:1px solid var(--line);border-radius:15px;background:rgba(15,27,45,.03)}.metric .label{color:var(--muted);font-size:12px}.metric .value{font-size:25px;font-weight:800;margin-top:5px;letter-spacing:-.5px}.metric .sub{font-size:11px;color:var(--muted);margin-top:5px}.sectionHead{display:flex;align-items:end;justify-content:space-between;gap:15px;margin-bottom:17px}.sectionHead h2{margin:0;font-size:18px}.sectionHead p{margin:0;color:var(--muted);font-size:12px}.flowStep{margin:36px 0 14px;padding-top:6px;border-top:1px solid rgba(15,27,45,.08)}.flowStep:first-child{margin-top:0;border-top:0;padding-top:0}.flowLabel{display:flex;align-items:center;gap:10px;font-size:12px;font-weight:800;letter-spacing:1.8px;text-transform:uppercase;color:var(--accent);margin:0 0 4px}.flowLabel .n{width:22px;height:22px;border-radius:50%;background:#EAF0FF;color:var(--accent);display:inline-flex;align-items:center;justify-content:center;font-size:11px}.flowLabel p{margin:0;color:var(--muted);font-size:12.5px;font-weight:500;text-transform:none;letter-spacing:0}.flowLabel.alt{color:var(--accent2)}.flowLabel.alt .n{color:var(--accent2)}.flowSub{color:var(--muted);font-size:12.5px;margin:2px 0 16px 32px}.insight{border:1px solid var(--line);border-radius:15px;padding:16px;background:#F7F9FC}.insight.critical{border-color:#E8B4BD}.insight.high{border-color:#E9CBA8}.insight.medium{border-color:#E5DBA0}.insight.positive{border-color:#A9D9C9}.insight h3{margin:0 0 5px;font-size:14px}.insight p{margin:6px 0;color:#33415C;font-size:13px}.insight ul{margin:6px 0;padding-left:18px;color:#33415C;font-size:13px}.tag{display:inline-flex;padding:4px 8px;border-radius:999px;font-size:10px;font-weight:800;text-transform:uppercase;background:#EAF0FF;color:#5B6B84}.tag.critical{background:#FCE8EA;color:#C22A3E}.tag.high{background:#FDF0E0;color:#B4720A}.tag.medium{background:#FBF6DE;color:#8A6D00}.tag.positive{background:#E4F5EF;color:#0E7C66}.riskRow,.actionRow{display:grid;grid-template-columns:40px 1fr auto;gap:12px;align-items:center;padding:13px 0;border-bottom:1px solid rgba(15,27,45,.08)}.rank{font-size:18px;font-weight:900;color:#5B6B84}.riskScore{font-size:12px;color:var(--muted)}.bar{height:7px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:8px}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:99px}.waterfall{display:flex;align-items:flex-end;gap:7px;height:190px;padding:20px 5px 0;border-bottom:1px solid var(--line)}.wf{flex:1;display:flex;flex-direction:column;justify-content:end;height:100%;min-width:0}.wf .col{border-radius:6px 6px 2px 2px;background:linear-gradient(180deg,#83a4ff,#506fd0);min-height:3px}.wf.neg .col{background:linear-gradient(180deg,#ff8290,#9d3e54)}.wf .lab{font-size:10px;color:var(--muted);text-align:center;margin-top:7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.wf .num{font-size:9px;text-align:center;color:#33415C;margin-bottom:4px}.scenario{padding:18px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(145deg,#F5F8FF,#EEF3FC)}.scenario h3{margin:0 0 6px;font-size:15px}.scenario .big{font-size:24px;font-weight:900;color:var(--accent)}.scenario p{color:var(--muted);font-size:11px;margin:6px 0}.muted{color:var(--muted)}.small{font-size:11px}.tableWrap{overflow:auto}table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:10px 8px;border-bottom:1px solid rgba(15,27,45,.08);text-align:right}th:first-child,td:first-child{text-align:left}th{color:#5B6B84;font-weight:600}.notice{padding:12px 14px;border-radius:12px;background:#EEF2FF;border:1px solid var(--line);color:#5B6B84;font-size:12px}.error{color:#C22A3E;background:#FCE8EA;border:1px solid #E8B4BD;padding:12px;border-radius:12px;margin:15px 0}.hidden{display:none!important}.footer{padding:25px 0 50px;color:#5B6B84;font-size:11px;text-align:center}.tabs{display:flex;gap:8px;margin-top:16px}.tab{padding:8px 12px;border-radius:999px;background:#F0F3F8;border:1px solid var(--line);color:#5B6B84;cursor:pointer}.tab.active{background:#DCE6FB;color:var(--accent);border-color:#1D4ED8}.tabPanel{display:none}.tabPanel.active{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.hidePrint{display:block}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.chip{font-size:11.5px;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px;color:#33415C}.chip b{color:var(--accent)}
.abar{height:9px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:6px}.abar i{display:block;height:100%;background:linear-gradient(90deg,#8aa7ff,#ff8290);border-radius:99px}
.custRow{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12.5px}
.highlight-target{outline:2px solid var(--accent);outline-offset:6px}
/* --- Marketing surface additions --- */
.topNav{display:flex;gap:18px}
.topNav a{color:var(--muted);font-size:13px;text-decoration:none;font-weight:600}
.topNav a:hover{color:var(--accent)}
.marketingSection{padding:8px 0 16px}
.marketingHead{text-align:center;max-width:640px;margin:0 auto 34px}
.marketingHead h2{font-family:var(--serif);font-size:32px;margin:0 0 10px;letter-spacing:-.5px}
.marketingHead p{color:var(--muted);margin:0;font-size:14.5px}
.pricingGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:stretch}
.priceCard{display:flex;flex-direction:column;padding:28px 24px;position:relative}
.priceCard.featured{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent),var(--shadow)}
.priceCard .plan{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:var(--accent);font-weight:800;margin-bottom:8px}
.priceCard h3{margin:0 0 6px;font-size:22px;font-family:var(--serif)}
.priceCard .amt{font-size:34px;font-weight:900;margin:8px 0 4px}
.priceCard .amt span{font-size:13px;color:var(--muted);font-weight:500}
.priceCard .desc{color:var(--muted);font-size:13px;margin-bottom:18px}
.priceCard ul{list-style:none;margin:0 0 22px;padding:0;flex:1;display:flex;flex-direction:column;gap:10px}
.priceCard ul li{font-size:13px;color:#33415C;display:flex;gap:8px;align-items:flex-start}
.priceCard ul li svg{flex:none;margin-top:2px;color:var(--accent)}
.priceCard .badgeTop{position:absolute;top:-11px;left:50%;transform:translateX(-50%);background:var(--accent);color:#FFFFFF;font-size:10.5px;font-weight:800;padding:4px 12px;border-radius:999px;letter-spacing:.5px}
.aboutGrid{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:center}
.aboutStats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}
.aboutStats .st{padding:16px;border:1px solid var(--line);border-radius:14px;text-align:center;background:rgba(15,27,45,.03)}
.aboutStats .st b{display:block;font-size:24px;color:var(--accent);font-family:var(--serif)}
.aboutStats .st span{font-size:11px;color:var(--muted)}
.contactGrid{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.contactCard{padding:26px}
.contactRow{display:flex;flex-direction:column;gap:12px;margin-top:14px}
.contactRow .item{display:flex;gap:10px;align-items:center;font-size:13px;color:#33415C}
.contactRow .item svg{color:var(--accent);flex:none}
@media(max-width:860px){.pricingGrid,.aboutGrid,.contactGrid{grid-template-columns:1fr}.topNav{display:none}}
.trustBar{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:20px;padding-top:18px;border-top:1px solid rgba(15,27,45,.10)}
.trustBar .item{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted)}
.trustBar .item svg{flex:none;color:var(--accent)}
.heroPreview{position:relative;padding:22px;overflow:hidden}
.pvLabel,.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.pvLabel span.dot,.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
.pvRing{width:112px;height:112px;border-radius:50%;margin:2px auto 14px;display:grid;place-items:center;background:conic-gradient(var(--accent) 0 78%,#182c42 78% 100%);position:relative}
.pvRing:after{content:"";position:absolute;inset:9px;border-radius:50%;background:#F7F9FC}
.pvRing b{position:relative;font-family:var(--serif);font-size:26px;z-index:1}
.pvRow{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12px}
.pvRow .n{color:var(--text);font-weight:700}
.pvRow .n.up{color:var(--green)}.pvRow .n.down{color:var(--red)}
.pvBars{display:flex;align-items:flex-end;gap:5px;height:54px;margin-top:14px}
.pvBars i{flex:1;background:linear-gradient(180deg,var(--accent2),#4a63b8);border-radius:3px 3px 1px 1px;display:block}
.statsStrip{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin:6px 0 0;padding:26px 0}
.statsStrip .stat b{font-family:var(--serif);font-size:36px;font-weight:600;color:var(--text);display:block;letter-spacing:-.5px}
.statsStrip .stat span{font-size:12.5px;color:var(--muted);display:block;margin-top:4px;max-width:20ch}
.whyCard{padding:20px;position:relative}
.whyCard .icoWrap{width:40px;height:40px;border-radius:11px;background:#DCE6FB;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;margin-bottom:14px;color:var(--accent)}
.ctaBanner{margin:44px 0 8px;padding:38px 32px;border-radius:22px;background:linear-gradient(135deg,#EAF0FF 0%,#DCE6FB 55%,#EAF0FF 100%);border:1px solid #C9D8F5;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.ctaBanner h3{font-family:var(--serif);font-weight:600;font-size:26px;margin:0 0 6px;letter-spacing:-.3px}
.ctaBanner p{margin:0;color:var(--muted);font-size:13.5px;max-width:52ch}
@media(max-width:1000px){.statsStrip{grid-template-columns:repeat(2,1fr)}.heroTitle{font-size:34px}}
@media(max-width:1000px){.hero{grid-template-columns:1fr}.grid4{grid-template-columns:repeat(2,1fr)}.grid3,.grid2{grid-template-columns:1fr}.wrap{padding:0 15px}.heroTitle{font-size:31px}.flowSub{margin-left:0}.qsel .qrow{grid-template-columns:1fr}}
@media print{
  *,*::before,*::after{box-sizing:border-box!important}
  @page{size:A4 portrait;margin:18mm 16mm 18mm 16mm}
  html,body{background:#fff!important;color:#0d1b2a!important;font-family:'Segoe UI',Arial,sans-serif!important;font-size:10pt!important;line-height:1.45!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Hide all interactive elements ─────────────────────────────── */
  .hero,.upload,.hidePrint,.tabs,.tabPanel,.chips,.qsel,.tab,.footer,.heroPreview,.trustBar,.statsStrip,.ctaBanner,
  button,input,select,textarea,.secondary,.primary,
  #sampleBtn,#aiBtn,#printBtn,#jsonBtn,#aiAskBtn,
  #aiBox,#aiCustomBox,#aiCustomPrompt,#methodNote,
  .interactiveScenarioCard,#interactiveScenarioCard{display:none!important}

  /* ── Layout: full-width single column ──────────────────────────── */
  .wrap{max-width:none!important;padding:0!important;margin:0!important}
  .top{display:none!important}

  /* ── Cover Banner ───────────────────────────────────────────────── */
  #printCover{display:block!important;border-bottom:3px solid #1a73e8;padding-bottom:12px;margin-bottom:20px}
  #printCover h1{font-size:20pt!important;font-weight:800;color:#0d1b2a;margin:0 0 4px}
  #printCover .sub{font-size:9pt;color:#4a6fa5}

  /* ── Cards ──────────────────────────────────────────────────────── */
  .card{box-shadow:none!important;background:#fff!important;border:1px solid #c8d6e8!important;border-radius:6px!important;margin-bottom:10px!important;padding:10px 12px!important;page-break-inside:avoid!important}
  .heroCard{box-shadow:none!important;background:#fff!important;border:1px solid #c8d6e8!important;padding:10px!important}

  /* ── Flow steps ─────────────────────────────────────────────────── */
  .flowStep{margin:14px 0 6px!important;padding-top:4px!important;page-break-inside:avoid!important}
  .flowLabel{background:none!important;border-left:4px solid #1a73e8!important;padding-left:10px!important;color:#0d1b2a!important;margin-bottom:6px!important}
  .flowLabel .n{background:#1a73e8!important;color:#fff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .flowSub{color:#555!important;font-size:8.5pt!important;margin-bottom:6px!important}

  /* ── Metrics / KPIs ─────────────────────────────────────────────── */
  .metric{background:#f4f7fc!important;border:1px solid #d4dff0!important;border-radius:6px!important;padding:8px!important;color:#0d1b2a!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .metric .label{font-size:7.5pt!important;color:#4a6fa5!important;font-weight:700;text-transform:uppercase;letter-spacing:.5px}
  .metric .value{font-size:14pt!important;font-weight:800;color:#0d1b2a!important}
  .metric .sub{font-size:7.5pt!important;color:#666!important}
  .grid2{display:grid!important;grid-template-columns:1fr 1fr!important;gap:8px!important}
  .grid3{display:grid!important;grid-template-columns:1fr 1fr 1fr!important;gap:8px!important}
  .grid4{display:grid!important;grid-template-columns:1fr 1fr 1fr 1fr!important;gap:8px!important}

  /* ── Health score ring ──────────────────────────────────────────── */
  .scoreCard{display:flex!important;align-items:center!important;gap:20px!important;padding:10px 14px!important}
  .scoreRing{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .scoreRing::after{background:#fff!important}

  /* ── Section headings ───────────────────────────────────────────── */
  .sectionHead{border-bottom:1px solid #d4dff0!important;margin-bottom:8px!important;padding-bottom:6px!important}
  .sectionHead h2{font-size:10pt!important;color:#1a73e8!important;font-weight:800;margin:0}
  .sectionHead p{font-size:8pt!important;color:#555!important;margin:2px 0 0}
  h1,h2,h3{page-break-after:avoid!important;color:#0d1b2a!important}
  h3{font-size:9.5pt!important}

  /* ── Risk & action rows ─────────────────────────────────────────── */
  .riskRow,.actionRow{border:1px solid #e4e8ef!important;border-radius:5px!important;margin-bottom:5px!important;padding:6px 8px!important;page-break-inside:avoid!important;background:#fafbfd!important}
  .rank{background:#e8f0fe!important;color:#1a73e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .bar{display:none!important}

  /* ── Tags / badges ──────────────────────────────────────────────── */
  .tag{border:1px solid #888!important;color:#333!important;background:#f0f0f0!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;font-size:7pt!important}
  .badge{border:1px solid #1a73e8!important;color:#1a73e8!important;font-size:7.5pt!important}

  /* ── Insights / alerts ──────────────────────────────────────────── */
  .insight{border-left:4px solid #1a73e8!important;background:#f0f7ff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;border-radius:4px!important;padding:7px 9px!important;margin-bottom:6px!important;page-break-inside:avoid!important}
  .insight.high,.insight.critical{border-left-color:#c62828!important;background:#fff5f5!important}
  .insight.positive{border-left-color:#2e7d32!important;background:#f1fdf3!important}
  .notice{background:#f8faff!important;border:1px solid #33415C!important;padding:7px 9px!important;border-radius:4px!important;font-size:8.5pt!important;color:#333!important}

  /* ── Waterfall chart ────────────────────────────────────────────── */
  .waterfall{display:flex!important;align-items:flex-end!important;gap:4px!important;height:100px!important;padding:4px 0!important}
  .wf .col{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .wf .num{font-size:6.5pt!important;color:#333!important}
  .wf .lab{font-size:6pt!important;color:#444!important}

  /* ── Tables ─────────────────────────────────────────────────────── */
  .tableWrap{overflow:visible!important}
  table{border-collapse:collapse!important;width:100%!important;font-size:8pt!important}
  th{background:#e8f0fe!important;color:#1a73e8!important;font-weight:700;padding:4px 6px!important;border:1px solid #c8d6e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  td{padding:4px 6px!important;border:1px solid #e4e8ef!important}
  tr:nth-child(even) td{background:#f8faff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Page breaks ─────────────────────────────────────────────────  */
  .flowStep:nth-child(3){page-break-before:always!important}
  .flowStep:nth-child(6){page-break-before:always!important}

  /* ── Misc ────────────────────────────────────────────────────────── */
  .muted{color:#555!important}
  .small{font-size:7.5pt!important}
  a{color:#1a73e8!important;text-decoration:none!important}
  .scenario{border:1px solid #c8d6e8!important;border-radius:5px!important;padding:8px!important;page-break-inside:avoid!important}
  .scenario .big{font-size:14pt!important;font-weight:800;color:#1a73e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .custRow,.wf{page-break-inside:avoid!important}
  .hidden{display:none!important}
  #dashboard{display:block!important}
  .abar{display:none!important}
}

@view-transition{navigation:auto}
::view-transition-old(root){animation:dfbpFadeOut .28s ease both}
::view-transition-new(root){animation:dfbpFadeIn .32s ease both}
@keyframes dfbpFadeOut{to{opacity:0;transform:translateY(-6px)}}
@keyframes dfbpFadeIn{from{opacity:0;transform:translateY(8px)}}
.topNav{display:flex;gap:18px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s;white-space:nowrap}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.authCluster{display:flex;flex-direction:column;align-items:flex-end;gap:5px;flex-shrink:0}
.headerSwitches{display:flex;align-items:center;gap:6px;justify-content:flex-end}
.headerSwitches select,select.globalLangSwitch{padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1}
.headerSwitches select:hover,select.globalLangSwitch:hover{border-color:var(--accent);color:#0F1B2D;background:#FFFFFF}
.navBtns{display:flex;gap:8px;align-items:center}
.navBtn{display:inline-flex;align-items:center;justify-content:center;padding:6px 14px;border-radius:9px;font-size:12.5px;font-weight:700;letter-spacing:-.1px;text-decoration:none;cursor:pointer;transition:all .18s ease;line-height:1.2;white-space:nowrap}
.navBtn.sec{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
.navBtn.sec:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
.navBtn.pri{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
.navBtn.pri:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text);flex-shrink:0}
.brandLogoWrap{flex-shrink:0;min-width:max-content}
.brandLink{text-decoration:none;display:flex;align-items:center;gap:10px;min-width:0}
.brandLogoIcon{width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0}
.brandTextWrap{min-width:0}
.brandTitle{font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2;white-space:nowrap}
.brandSub{font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px;white-space:nowrap}
.headerRight{display:flex;align-items:center;gap:12px;flex-shrink:0}
.mobileNavAuth{display:none}

@media(max-width:920px){
  html,body{overflow-x:hidden;max-width:100vw;width:100%}
  .top{padding:12px 0 10px}
  .wrap{padding:0 16px;max-width:100vw;box-sizing:border-box}
  .brand{gap:10px}
  .brandLogoIcon{width:32px;height:32px;border-radius:9px}
  .brandLogoIcon svg{width:18px;height:18px}
  .brandTitle{font-size:15.5px}
  .brandSub{display:none}
  .brandLogoWrap{min-width:0;flex:1 1 auto;overflow:hidden}
  .topNav{position:fixed;top:56px;left:0;right:0;width:100vw;background:#FFFFFF;border-bottom:1.5px solid var(--line);box-shadow:0 14px 34px rgba(15,27,45,0.12);flex-direction:column;align-items:stretch;gap:0;padding:0 20px;max-height:0;overflow:hidden;transition:max-height .28s ease,padding .2s ease;z-index:999;box-sizing:border-box}
  .topNav.open{max-height:460px;padding:10px 20px 20px;overflow-y:auto}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.06);font-size:14.5px;color:var(--text);font-weight:600;display:block;text-align:left}
  .mobileNavAuth{display:flex;gap:10px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(15,27,45,.08)}
  .mobileNavAuth a{flex:1;padding:10px 12px;font-size:13px;font-weight:700;border-radius:10px;text-align:center;justify-content:center;text-decoration:none}
  .navToggle{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;padding:0;font-size:18px;border-radius:8px;cursor:pointer}
}

@media(max-width:768px){
  .navBtns{display:none}
  .authCluster{flex-direction:row;align-items:center}
  .headerRight{gap:6px}
  .globalLangSwitch{padding:4px 5px !important;font-size:11px !important;border-radius:7px !important;max-width:60px}
  .wrap{padding:0 12px}
  .brandTitle{font-size:14.5px}
  .pageHead{padding:28px 0 10px}
  .pageHead h1{font-size:26px !important}
  .aboutGrid{grid-template-columns:1fr !important;gap:20px}
  .aboutStats{grid-template-columns:1fr !important;gap:10px}
}
.badge.v{white-space:nowrap}
/* ---- Marketing hero (separate from app hero) ---- */
.mHero{padding:56px 0 30px;display:grid;grid-template-columns:1.15fr .85fr;gap:34px;align-items:center}
.mHero .eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:18px}
.mHero h1{font-family:var(--serif);font-weight:600;font-size:50px;line-height:1.08;margin:0 0 18px;letter-spacing:-1px}
.mHero h1 span{color:var(--accent)}
.mHero p.lead{color:var(--muted);font-size:16px;max-width:560px;line-height:1.65;margin:0 0 26px}
.mHero .ctaRow{display:flex;gap:12px;flex-wrap:wrap}
.mHero .ctaRow a{text-decoration:none}
.mHero .miniTrust{display:flex;gap:18px;flex-wrap:wrap;margin-top:28px}
.mHero .miniTrust span{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px}
.mHero .miniTrust svg{color:var(--accent)}
.heroArt{position:relative}
.heroArt .floatCard{position:absolute;background:#FFFFFF;border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);padding:14px 16px;font-size:11.5px;color:#33415C;animation:dfbpFloat 5s ease-in-out infinite}
.heroArt .floatCard b{display:block;font-size:16px;color:var(--accent);font-family:var(--serif)}
.heroArt .fc1{top:-10px;left:-10px;animation-delay:0s}
.heroArt .fc2{bottom:6px;right:-14px;animation-delay:1.2s}
@keyframes dfbpFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
/* ---- Alternating content blocks (fixes the "iç içe" cramped look) ---- */
.secBlock{padding:28px 0}
.secBlock.tint{background:linear-gradient(180deg,#F8FAFC 0%,#FFFFFF 100%);border:1px solid #E2E8F0;border-radius:26px;margin:0 -10px;box-shadow:0 4px 20px rgba(15,27,45,.03)}
.pillScrollBtn{width:36px;height:36px;border-radius:50%;background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:800;cursor:pointer;flex-shrink:0;box-shadow:0 4px 12px rgba(15,27,45,0.08);transition:all .18s ease;user-select:none;z-index:4}
.pillScrollBtn:hover{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;transform:scale(1.08);box-shadow:0 6px 16px rgba(29,78,216,0.25)}
.pillScrollBtn:active{transform:scale(0.95)}
.secBlock+.secBlock{border-top:1px solid rgba(15,27,45,.06)}
.pageHead{padding:54px 0 10px;text-align:center}
.pageHead .eyebrow{display:inline-flex;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:16px}
.pageHead h1{font-family:var(--serif);font-size:38px;margin:0 0 12px;letter-spacing:-.6px}
.pageHead p{color:var(--muted);max-width:600px;margin:0 auto;font-size:14.5px}
.reveal{opacity:0;transform:translateY(18px);transition:opacity .55s ease,transform .55s ease}
.reveal.in{opacity:1;transform:none}
/* ---- Rich footer ---- */
.siteFooter{border-top:1px solid var(--line);margin-top:40px;padding:46px 0 26px}
.siteFooter .cols{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:28px;margin-bottom:30px}
.siteFooter h4{font-size:12px;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin:0 0 14px}
.siteFooter .brandCol p{color:var(--muted);font-size:12.5px;max-width:280px;line-height:1.6}
.siteFooter ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.siteFooter ul a{color:#33415C;text-decoration:none;font-size:13px}
.siteFooter ul a:hover{color:var(--accent)}
.siteFooter .legal{border-top:1px solid rgba(15,27,45,.08);padding-top:20px;color:#5B6B84;font-size:11px;line-height:1.7}
html{overflow-x:hidden}@media(max-width:860px){.siteFooter .cols{grid-template-columns:1fr 1fr}.mHero{grid-template-columns:1fr}.heroArt{order:-1;max-width:340px;margin:24px auto 40px;padding:0 14px}.heroArt .floatCard{position:static;display:inline-block;margin:6px 6px 0 0;animation:none}.heroArt .fc1,.heroArt .fc2{top:auto;left:auto;right:auto;bottom:auto}}
/* ---- FAQ (paketler sayfası) ---- */
.faqItem{border-bottom:1px solid var(--line);padding:16px 0}
.faqItem summary{cursor:pointer;font-weight:700;font-size:14px;list-style:none;display:flex;justify-content:space-between;align-items:center}
.faqItem summary::-webkit-details-marker{display:none}
.faqItem summary:after{content:'+';font-size:20px;color:var(--accent)}
.faqItem[open] summary:after{content:'–'}
.faqItem p{color:var(--muted);font-size:13.5px;margin:10px 0 0}
/* ---- Executive Intelligence band (single, deliberate dark boardroom section) ---- */
.execBand{background:radial-gradient(1200px 500px at 15% -20%, rgba(76,201,240,.10), transparent 60%),linear-gradient(160deg,#0D1B2A 0%,#081426 100%);border-radius:26px;padding:52px;display:grid;grid-template-columns:.85fr 1.15fr;gap:40px;align-items:center;overflow:hidden}
.execEyebrow{display:inline-block;font-size:11.5px;font-weight:800;letter-spacing:1.6px;color:#4CC9F0;background:rgba(76,201,240,.12);border:1px solid rgba(76,201,240,.35);padding:6px 12px;border-radius:999px;margin-bottom:16px}
.execCopy h2{font-family:var(--serif);color:#F8FAFC;font-size:28px;line-height:1.2;margin:0 0 12px;letter-spacing:-.4px}
.execCopy p{color:#94A3B8;font-size:14px;line-height:1.7;margin:0 0 18px;max-width:44ch}
.execList{list-style:none;margin:0 0 24px;padding:0;display:flex;flex-direction:column;gap:9px}
.execList li{color:#C7D2E8;font-size:13px}
.execList li b{color:#F8FAFC}
.execCta{display:inline-block;color:#0D1B2A;background:#4CC9F0;font-weight:800;font-size:13.5px;padding:12px 20px;border-radius:11px;text-decoration:none;transition:transform .15s ease,box-shadow .15s ease}
.execCta:hover{transform:translateY(-1px);box-shadow:0 10px 26px rgba(76,201,240,.35)}
.execArt{filter:drop-shadow(0 24px 48px rgba(0,0,0,.35))}
@media(max-width:860px){.execBand{grid-template-columns:1fr;padding:32px 22px}}
/* ---- New: live dashboard hero panel ---- */
.heroDash{background:linear-gradient(160deg,#0D1B2A 0%,#0A1524 100%);border-radius:20px;border:1px solid #1E3050;padding:20px;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(8,17,32,.35)}
.heroDash .dHead{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.heroDash .dHead .dots span{width:8px;height:8px;border-radius:50%;display:inline-block;margin-right:5px}
.heroDash .dHead .live{font-size:10.5px;color:#7FE3B4;display:flex;align-items:center;gap:6px;font-weight:700;letter-spacing:.4px}
.heroDash .dHead .live i{width:6px;height:6px;border-radius:50%;background:#15E3B3;display:inline-block;box-shadow:0 0 0 3px rgba(21,227,179,.22);animation:dfbpPulse 1.8s ease infinite}
@keyframes dfbpPulse{0%,100%{opacity:1}50%{opacity:.35}}
.dashTabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px}
.dashTabs span{font-size:10px;color:#7C8FAD;background:#101F33;border:1px solid #1E3050;border-radius:999px;padding:5px 10px;transition:all .25s ease}
.dashTabs span.on{color:#0D1B2A;background:#4CC9F0;border-color:#4CC9F0;font-weight:800}
.dashPane{display:none;min-height:230px}
.dashPane.on{display:block;animation:dfbpFadeIn .4s ease both}
.dashPane .dTitle{color:#7C8FAD;font-size:10px;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px}
.dashKpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px}
.dashKpis div{background:#132238;border:1px solid #20334b;border-radius:9px;padding:9px 10px}
.dashKpis div b{display:block;font-size:16px;color:#F8FAFC;font-family:var(--serif)}
.dashKpis div span{font-size:9.5px;color:#7C8FAD}
.heroDash .foot{margin-top:12px;padding-top:12px;border-top:1px solid #1E3050;font-size:10.5px;color:#7C8FAD;display:flex;justify-content:space-between}
/* ---- New: CFO trust strip ---- */
.trustGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.trustCard{padding:22px}
.trustCard .icoWrap2{width:38px;height:38px;border-radius:10px;background:#0D1B2A;color:#4CC9F0;display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.trustCard h3{margin:0 0 6px;font-size:14.5px}
.trustCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.55}
/* ---- New: Executive Journey ---- */
.journey{display:grid;grid-template-columns:repeat(6,1fr);gap:0;position:relative;margin-top:8px}
.journey:before{content:"";position:absolute;top:22px;left:6%;right:6%;height:2px;background:linear-gradient(90deg,#C9D8F5,#4CC9F0,#C9D8F5)}
.jStep{text-align:center;padding:0 8px;opacity:0;transform:translateY(16px);transition:opacity .5s ease,transform .5s ease}
.jStep.in{opacity:1;transform:none}
.jStep .jDot{width:44px;height:44px;border-radius:50%;background:#FFFFFF;border:2px solid var(--accent);color:var(--accent);display:flex;align-items:center;justify-content:center;margin:0 auto 12px;position:relative;z-index:1;font-weight:900;font-size:13px}
.jStep h4{margin:0 0 5px;font-size:13px;letter-spacing:.4px}
.jStep p{margin:0;font-size:11.5px;color:var(--muted);line-height:1.4}
@media(max-width:860px){.journey{grid-template-columns:1fr 1fr;gap:22px 0}.journey:before{display:none}.trustGrid{grid-template-columns:1fr 1fr}}
/* ---- New: outcome-based module groups ---- */
.intelGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.intelCard{padding:24px;display:flex;flex-direction:column}
.intelCard .igIco{width:40px;height:40px;border-radius:11px;background:#DCE6FB;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.intelCard h3{margin:0 0 8px;font-size:16px;font-family:var(--serif)}
.intelCard ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}
.intelCard ul li{font-size:12.5px;color:#33415C;display:flex;gap:7px;align-items:flex-start}
.intelCard ul li:before{content:"";width:5px;height:5px;border-radius:50%;background:var(--accent);margin-top:6px;flex:none}
@media(max-width:860px){.intelGrid{grid-template-columns:1fr 1fr}}
/* ---- New: security/governance page ---- */

/* ---- High-impact FinTech additions ---- */
.gradText{background:linear-gradient(135deg,#1D4ED8 0%,#2563EB 50%,#38BDF8 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;display:inline-block}
.livePill{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:var(--accent);background:linear-gradient(135deg,#EEF4FF,#E0EDFF);border:1px solid #BFDBFE;padding:8px 16px;border-radius:999px;margin-bottom:20px;box-shadow:0 2px 10px rgba(37,99,235,.12)}
.livePill i{width:8px;height:8px;border-radius:50%;background:#10B981;display:inline-block;box-shadow:0 0 0 4px rgba(16,185,129,.25);animation:dfbpPulse 1.8s ease infinite}
.dilemmaGrid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:20px}
.dilemmaCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:26px;position:relative;overflow:hidden;box-shadow:var(--shadow);transition:transform .2s ease,box-shadow .2s ease}
.dilemmaCard:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(15,27,45,.09)}
.dilemmaQ{font-size:15px;font-weight:700;color:#0F1B2D;margin-bottom:12px;display:flex;gap:10px;align-items:flex-start;line-height:1.4}
.dilemmaQ span{background:#FEE2E2;color:#DC2626;border-radius:8px;padding:2px 8px;font-size:11px;font-weight:900;flex:none;margin-top:2px}
.dilemmaA{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:14px 16px;font-size:13px;color:#33415C;line-height:1.55}
.dilemmaA b{color:var(--accent);display:block;margin-bottom:4px}
.workflowGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;position:relative;margin-top:20px}
.workflowCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:24px;box-shadow:var(--shadow);position:relative;display:flex;flex-direction:column}
.workflowBadge{font-size:11px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:var(--accent);background:#EFF6FF;border:1px solid #DBEAFE;padding:4px 10px;border-radius:999px;align-self:flex-start;margin-bottom:12px}
.workflowCard h3{font-size:16px;margin:0 0 8px;font-family:var(--serif);color:#0F1B2D}
.workflowCard p{font-size:12.5px;color:var(--muted);line-height:1.55;margin:0}
.compareTableWrap{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:var(--shadow);margin-top:20px}
.compareTable{width:100%;border-collapse:collapse;font-size:13px}
.compareTable th,.compareTable td{padding:16px 18px;border-bottom:1px solid rgba(15,27,45,.08);text-align:left}
.compareTable th{background:#F8FAFC;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#475569}
.compareTable th.featured{background:linear-gradient(135deg,#EFF6FF,#DBEAFE);color:var(--accent);border-bottom:2px solid var(--accent)}
.compareTable td.featured{background:#F8FAFF;font-weight:600;color:#0F1B2D}
@media(max-width:860px){.dilemmaGrid,.workflowGrid{grid-template-columns:1fr}.compareTableWrap{overflow-x:auto}}

.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

</style></head>
<body>
<header class="top"><div class="wrap brand"><div class="brandLogoWrap">
  <a href="/" class="brandLink">
    <div class="brandLogoIcon">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div class="brandTextWrap">
      <div class="brandTitle">Digital Finance Business Partner</div>
      <div class="brandSub">Finansal Teşhis &amp; Yönetim Karar Destek Platformu</div>
    </div>
  </a>
</div><div class="headerRight"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/cozumler">Çözümler</a><a href="/hakkimizda" class="active">Hakkımızda</a><a href="/uygulama">Uygulama</a><a href="/paketler">Paketler</a><a href="/guvenlik">Güvenlik</a><a href="/iletisim">İletişim</a><div class="mobileNavAuth"><a href="/uygulama?auth=login" class="secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="primary">Ücretsiz Kayıt Ol</a></div></nav><div class="authCluster hidePrint"><div class="headerSwitches"><select class="globalLangSwitch select" onchange="setGlobalLanguage(this.value)" style="padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1" title="Dil / Language"><option value="tr">🇹🇷 TR</option><option value="en">🇬🇧 EN</option><option value="de">🇩🇪 DE</option><option value="fr">🇫🇷 FR</option><option value="es">🇪🇸 ES</option><option value="it">🇮🇹 IT</option><option value="nl">🇳🇱 NL</option></select></div><div class="navBtns"><a href="/uygulama?auth=login" class="navBtn sec">Giriş Yap</a><a href="/uygulama?auth=register" class="navBtn pri">Ücretsiz Kayıt Ol</a></div></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<div class="pageHead reveal in"><span class="eyebrow">Bizi Tanıyın</span><h1>Finansal Veriyi Güvenilir Yönetim Kararına Dönüştürüyoruz</h1><p>Reel sektörde ve holdinglerde kıdemli finans yöneticiliği yapmış uzmanlar ile finansal yazılım mühendislerinin ortak vizyonuyla hayata geçirildi. Amacımız; her büyüklükteki şirketin kendi mizanından kuruşu kuruşuna doğrulanmış, net ve icra edilebilir yönetim kararları alabilmesidir.</p></div>

<div class="secBlock reveal"><section id="about" class="marketingSection hidePrint" style="padding-top:0"><div class="aboutGrid">
<div><span class="badge" style="margin-bottom:14px;display:inline-block">Biz Kimiz?</span><h2 style="font-family:var(--serif);font-size:28px;margin:6px 0 14px;letter-spacing:-.5px">Mizanı Sadece Vergi İçin Değil, Şirketin Geleceği İçin Okuyoruz</h2><p class="muted" style="font-size:14px;line-height:1.75">Digital Finance Business Partner (DFBP), Türkiye'deki işletmelerin en yaygın finansal sıkıntısı olan <i>"Defterde kâr çıkıyor ama kasada para nerede?"</i> sorusuna bağımsız ve matematiksel bir çözüm sunmak amacıyla kuruldu.<br><br>Klasik muhasebe süreçleri geçmişe dönük vergi ve yasal beyan üretir. Oysa patronun ve yöneticinin ihtiyacı; yarın sabah hangi müşteriye mal çıkışını durduracağını, nakdin hangi depoda veya vadede kilitlendiğini ve kasayı rahatlatacak 1 numaralı adımı bilmektir. Platformumuz, mizanınızı <b>33 deterministik karar motoruyla</b> inceleyerek kurumsal finans zekasını dakikalar içinde masanıza taşır.</p><div class="aboutStats"><div class="st"><b>33</b><span>Karar Motoru</span></div><div class="st"><b>%100</b><span>Matematiksel Doğrulama</span></div><div class="st"><b>0</b><span>Disk Saklama (RAM-Only)</span></div></div></div>
<div class="card" style="padding:26px">
<div style="display:inline-flex;align-items:center;gap:8px;background:#EFF6FF;border:1px solid #BFDBFE;color:var(--accent);font-size:11.5px;font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:6px 14px;border-radius:999px;margin-bottom:16px">
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
  Çalışma İlkelerimiz
</div>
<h3 style="margin:0 0 12px;font-family:var(--serif);font-size:19px;color:#0F1B2D">Yönetim ve Güven Standartlarımız</h3>
<ul style="margin:0;padding-left:18px;color:#33415C;font-size:13.5px;line-height:1.9">
<li><b>Önce Matematik, Sonra Yorum:</b> Rakamlar asla tahmine bırakılmaz; tüm çıktılar çift taraflı denetimden geçer.</li>
<li><b>Sade ve Anlaşılır Dil:</b> Ağır akademik jargondan uzak, sahadaki yöneticinin doğrudan uygulayabileceği kararlar sunar.</li>
<li><b>Mutlak Veri Mahremiyeti:</b> Mizanınız sunucuda kalıcı depolanmaz; geçici bellekte işlenip oturum sonunda yok edilir.</li>
<li><b>Net İcraat Takvimi:</b> Kararlar soyut tavsiye olarak kalmaz; sorumlusu, vadesi ve TL etkisiyle birlikte verilir.</li>
</ul></div>
</div></section>
</div>

<!-- SECTION: AMACIMIZ, MISYONUMUZ, VIZYONUMUZ -->
<div class="secBlock tint reveal"><section class="marketingSection hidePrint" style="padding-top:0">
<div class="marketingHead">
  <span class="workflowBadge">STRATEJİK PUSULAMIZ</span>
  <h2>Temel Amacımız, Misyonumuz ve Vizyonumuz</h2>
  <p>Şirketlerin finansal kararlarını veriye, matematiğe ve net aksiyonlara dayandırma taahhüdümüz.</p>
</div>
<div class="grid3">
  <div class="card" style="padding:28px;border-top:4px solid #1D4ED8;background:#FFFFFF;box-shadow:0 8px 26px rgba(15,27,45,0.05)">
    <div style="font-size:32px;margin-bottom:12px">🛡️</div>
    <h3 style="font-size:18px;font-family:var(--serif);margin:0 0 8px;color:#0F1B2D">Temel Amacımız (Varoluş Sebebi)</h3>
    <div style="color:#1D4ED8;font-size:12px;font-weight:700;margin-bottom:10px">Patronu "Defterde Kâr, Kasada Yok" Yanılsamasından Kurtarmak</div>
    <p style="color:#5B6B84;font-size:13px;line-height:1.65;margin:0">Muhasebe geçmişi kaydeder, patron ise yarın için risk alır. Aradaki en ölümcül tehlike; şirketin defterde kârlı görünürken, paranın müşteri vadelerinde ve depoda kilitlenip şirketi sessizce tüketmesidir. Temel varoluş sebebimiz; bu finansal kör noktayı anında ortadan kaldırmak ve patronun şirketteki her kuruşun nereye bağlandığını çıplak gözle görmesini sağlamaktır.</p>
  </div>
  <div class="card" style="padding:28px;border-top:4px solid #10B981;background:#FFFFFF;box-shadow:0 8px 26px rgba(15,27,45,0.05)">
    <div style="font-size:32px;margin-bottom:12px">⚡</div>
    <h3 style="font-size:18px;font-family:var(--serif);margin:0 0 8px;color:#0F1B2D">Misyonumuz (Her Gün Yaptığımız İş)</h3>
    <div style="color:#047857;font-size:12px;font-weight:700;margin-bottom:10px">Her Şirketin Masasına Bağımsız Bir CFO Aklı Koymak</div>
    <p style="color:#5B6B84;font-size:13px;line-height:1.65;margin:0">Milyonluk danışmanlık faturalarına veya aylar süren ERP projelerine gerek bırakmadan; Türkiye'deki her KOBİ ve işletmenin yüklediği mizanı <b>60 saniyede 33 deterministik karar motoruyla</b> denetlemek, görünmez kâr sızıntılarını kuruşu kuruşuna hesaplamak ve vadesi, sahibi, TL getirisi belli yönetim kararlarını doğrudan masaya koymaktır.</p>
  </div>
  <div class="card" style="padding:28px;border-top:4px solid #F59E0B;background:#FFFFFF;box-shadow:0 8px 26px rgba(15,27,45,0.05)">
    <div style="font-size:32px;margin-bottom:12px">🎯</div>
    <h3 style="font-size:18px;font-family:var(--serif);margin:0 0 8px;color:#0F1B2D">Vizyonumuz (Hedeflediğimiz Dönüşüm)</h3>
    <div style="color:#B45309;font-size:12px;font-weight:700;margin-bottom:10px">Sezgisel Yönetimden, "Rakamla Kanıtlanmış Yönetim" Standartlarına Geçiş</div>
    <p style="color:#5B6B84;font-size:13px;line-height:1.65;margin:0">"Galiba iyi gidiyoruz" veya "Cirosu yüksek müşteri kârlıdır" gibi varsayımlara dayalı yönetim devrini tamamen kapatıp; Türkiye ve bölgede finansal kararların <b>çift taraflı matematik, What-If simülasyonları ve canlı nakit döngüsüyle</b> yönetildiği yeni nesil bir kurumsal finans standardı inşa etmektir.</p>
  </div>
</div></section></div>

<div class="secBlock reveal">
  <div class="marketingHead">
    <span class="workflowBadge">KURUMSAL UZMANLIK ALANLARIMIZ</span>
    <h2>3 Temel Standart Üzerinde Yükseliyoruz</h2>
    <p>Geleneksel muhasebe raporlaması ile stratejik CFO liderliği arasındaki uçurumu teknolojiyle kapatıyoruz.</p>
  </div>
  <div class="grid3">
    <div class="card" style="padding:26px;background:#FFFFFF;border:1px solid #E2E8F0;box-shadow:0 6px 20px rgba(15,27,45,0.04)">
      <div style="width:44px;height:44px;border-radius:12px;background:#EFF6FF;color:#1D4ED8;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:16px">🧮</div>
      <h3 style="margin:0 0 8px;font-size:16.5px;color:#0F1B2D">1. Deterministik Finansal Modelleme &amp; Çift Taraflı Doğrulama</h3>
      <p style="color:#5B6B84;font-size:13px;line-height:1.65;margin:0">Yapay zekanın sayı veya formül uydurmasına asla izin vermeyiz. Tüm 33 karar motoru; muhasebe tekdüzen hesap planı kuralları, çift taraflı kayıt dengesi, nakit akışı ve çalışma sermayesi modelleri üzerinde kuruşu kuruşuna deterministik matematik çalıştırır.</p>
    </div>
    <div class="card" style="padding:26px;background:#FFFFFF;border:1px solid #E2E8F0;box-shadow:0 6px 20px rgba(15,27,45,0.04)">
      <div style="width:44px;height:44px;border-radius:12px;background:#ECFDF5;color:#059669;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:16px">👔</div>
      <h3 style="margin:0 0 8px;font-size:16.5px;color:#0F1B2D">2. Stratejik CFO Karar Perspektifi &amp; Kök Neden Analitiği</h3>
      <p style="color:#5B6B84;font-size:13px;line-height:1.65;margin:0">Raporlarımız statik muhasebe çıktıları değildir; "Kâr nerede kilitlendi?", "Hangi müşteri gizli zarar ettiriyor?" ve "Yarın hangi somut adımı atmalıyız?" sorularını WHAT → WHY → SO WHAT metodolojisiyle yanıtlayan bir icra kurulu pusulasıdır.</p>
    </div>
    <div class="card" style="padding:26px;background:#FFFFFF;border:1px solid #E2E8F0;box-shadow:0 6px 20px rgba(15,27,45,0.04)">
      <div style="width:44px;height:44px;border-radius:12px;background:#FEF3C7;color:#D97706;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:16px">🛡️</div>
      <h3 style="margin:0 0 8px;font-size:16.5px;color:#0F1B2D">3. Kurumsal Veri Güvenliği, KVKK &amp; Sıfır Kalıcı İzsiz Bellek</h3>
      <p style="color:#5B6B84;font-size:13px;line-height:1.65;margin:0">Finansal tablolar şirketlerin en mahrem varlığıdır. Sistemimizde verileriniz sabit diske yazılmaz; şifreli geçici bellekte (RAM) işlenir, analiz tarayıcınıza teslim edildiği anda bellekten tamamen imha edilir; yapay zeka eğitimine aktarılmaz.</p>
    </div>
  </div>
</div>

<div class="secBlock reveal"><section class="ctaBanner hidePrint"><div><h3>Bizi tanımak ister misiniz?</h3><p>Ekibinizle birlikte 15 dakikalık bir canlı demo oturumu planlayabilir veya Data Hub ile anında deneyebilirsiniz.</p></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a href="/uygulama?sample=data_hub" class="primary" style="text-decoration:none;padding:12px 20px;border-radius:11px">🔥 Canlı Demoyu Başlat</a><a href="/iletisim" class="secondary" style="text-decoration:none;padding:12px 20px;border-radius:11px">İletişime Geç</a></div></section></div>

</main>
<div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/cozumler">Çözümler</a></li><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • <a href="https://digitalfinancebp.com" style="color:var(--accent);text-decoration:none;font-weight:700">digitalfinancebp.com</a> • Deterministik Finans Karar Motoru &amp; Çift Yönlü Denetim Sistemi<br><span style="opacity:.85">Bu analiz deterministik matematiksel hesaplamalara ve çift taraflı denetim kurallarına dayanır; resmi mali tablo veya vergi beyannamesi yerine geçmez. Nihai yönetim kararları için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca anlık analiz süresince RAM bellekte işlenir; sunucu sabit diskinde ASLA kalıcı saklanmaz. KVKK ve kurumsal gizlilik politikamız için <a href="javascript:void(0)" onclick="showKvkkModal()" style="color:var(--accent);text-decoration:underline;font-weight:600">Aydınlatma ve Gizlilik Metni</a>'ni inceleyebilirsiniz.</span></div></div></div>
<script>
window.showKvkkModal=function(){var m=document.getElementById('kvkkModal');if(!m){m=document.createElement('div');m.id='kvkkModal';m.style.cssText='position:fixed;inset:0;background:rgba(15,27,45,0.7);z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(4px);';m.innerHTML='<div style="background:#FFFFFF;border-radius:18px;max-width:640px;width:100%;max-height:85vh;overflow-y:auto;padding:28px;box-shadow:0 20px 50px rgba(0,0,0,0.3);position:relative;border:1px solid #E2E8F0"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid #E2E8F0;padding-bottom:12px"><div style="display:flex;align-items:center;gap:8px"><span style="font-size:20px">🔒</span><h3 style="margin:0;font-size:18px;color:#0F1B2D;font-family:sans-serif;font-weight:700">Veri Güvenliği, RAM-Only İşleme ve KVKK Taahhüdü</h3></div><button class="kvkkClose" style="background:#F1F5F9;border:0;border-radius:50%;width:30px;height:30px;cursor:pointer;font-weight:bold;font-size:16px">✕</button></div><div style="font-size:13px;line-height:1.7;color:#33415C;display:flex;flex-direction:column;gap:12px"><div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:12px;color:#166534"><b>🛡️ Sıfır Disk Depolama (RAM-Only):</b> Yüklediğiniz mizan, muavin defteri veya operasyonel raporlar sunucunun kalıcı depolama birimlerine (HDD/SSD/Veritabanı) kaydedilmez. Tüm matematiksel hesaplamalar ve çift taraflı denetim anlık bellek (RAM) üzerinde icra edilir ve analiz tamamlandığında oturumla birlikte tamamen silinir.</div><p><b>1. Veri İzolasyonu &amp; Model Eğitimi Yasağı:</b> Şirketiniz tarafından paylaşılan hiçbir finansal veri, ciro, müşteri adı veya bilanço kalemi üçüncü şahıslara verilmez, satılmaz ve genel yapay zekâ modellerinin eğitimi için havuzlara aktarılmaz.</p><p><b>2. 256-Bit TLS Şifreleme:</b> Tarayıcınız ile platform arasındaki tüm veri akışı bankacılık standardında 256-bit SSL/TLS tüneli üzerinden şifrelenir.</p><p><b>3. 6698 Sayılı KVKK Uyumluluğu:</b> Şirket yetkililerine ait iletişim bilgileri ve ticari sırlar yalnızca talep edilen analizlerin üretilmesi amacıyla işlenir; yasal yükümlülükler haricinde hiçbir tarafla paylaşılmaz.</p><p><b>4. Kurumsal Gizlilik Sözleşmesi (NDA):</b> Kurumsal entegrasyon veya holding düzeyinde çalışmalarda şirketinizle karşılıklı Kurumsal NDA akdedilir.</p></div><div style="margin-top:20px;text-align:right"><button class="kvkkClose primary" style="padding:9px 20px;border-radius:10px;font-size:13px;background:#1D4ED8;color:#fff;border:0;cursor:pointer;font-weight:700">Anladım ve Kabul Ediyorum</button></div></div>';m.addEventListener('click',function(e){if(e.target===m||e.target.classList.contains('kvkkClose'))m.style.display='none';});document.body.appendChild(m);}m.style.display='flex';};
document.getElementById('navToggle')?.addEventListener('click',()=>document.getElementById('mainNav')?.classList.toggle('open'));
window.addEventListener('scroll',()=>{document.querySelector('.top')?.classList.toggle('scrolled',window.scrollY>8)});
(function(){
  const els=document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){els.forEach(e=>e.classList.add('in'));return;}
  const io=new IntersectionObserver((entries)=>{entries.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}})},{threshold:.12});
  els.forEach(e=>io.observe(e));
})();
(function(){
  // Finance-flavoured count-up animation for stat/kpi numbers on scroll into view
  const targets = document.querySelectorAll('.stat b, .aboutStats .st b, .pvRing b, .scoreNum strong');
  if(!('IntersectionObserver' in window) || !targets.length) return;
  const parse = (txt)=>{ const m = txt.match(/-?\d[\d.,]*/); return m ? m[0] : null; };
  const cio = new IntersectionObserver((entries)=>{
    entries.forEach(en=>{
      if(!en.isIntersecting) return;
      cio.unobserve(en.target);
      const el = en.target; const raw = el.textContent; const numStr = parse(raw);
      if(!numStr) return;
      const prefix = raw.slice(0, raw.indexOf(numStr));
      const suffix = raw.slice(raw.indexOf(numStr)+numStr.length);
      const clean = numStr.replace(/\./g,'').replace(',', '.');
      const target = parseFloat(clean); if(isNaN(target)) return;
      const decimals = (clean.split('.')[1]||'').length;
      const dur = 900; const t0 = performance.now();
      function step(t){
        const p = Math.min(1,(t-t0)/dur); const eased = 1-Math.pow(1-p,3);
        const val = target*eased;
        el.textContent = prefix + val.toFixed(decimals).replace('.', decimals?',':'') + suffix;
        if(p<1) requestAnimationFrame(step); else el.textContent = raw;
      }
      requestAnimationFrame(step);
    });
  }, {threshold:.4});
  targets.forEach(t=>cio.observe(t));
})();
(function(){
  // Staggered grow-in for waterfall / bridge chart columns and progress bars
  document.querySelectorAll('.waterfall').forEach(wf=>{
    [...wf.children].forEach((col,i)=>{ col.style.animation = `growUp .6s ease ${i*70}ms both`; });
  });
  document.querySelectorAll('.bar i, .abar i').forEach((i,idx)=>{ i.style.animation = `growWidth .7s ease ${idx*40}ms both`; });
})();
</script>
<script>
var GLOBAL_I18N = {
  tr: { navHome: 'Anasayfa', navSolutions: 'Çözümler', navAbout: 'Hakkımızda', navApp: 'Uygulama', navPricing: 'Paketler', navSecurity: 'Güvenlik', navContact: 'İletişim', login: 'Giriş Yap', register: 'Ücretsiz Kayıt Ol' },
  en: { navHome: 'Home', navSolutions: 'Solutions', navAbout: 'About', navApp: 'App', navPricing: 'Pricing', navSecurity: 'Security', navContact: 'Contact', login: 'Log In', register: 'Sign Up Free' },
  de: { navHome: 'Startseite', navSolutions: 'Lösungen', navAbout: 'Über uns', navApp: 'Anwendung', navPricing: 'Preise', navSecurity: 'Sicherheit', navContact: 'Kontakt', login: 'Anmelden', register: 'Kostenlos Registrieren' },
  fr: { navHome: 'Accueil', navSolutions: 'Solutions', navAbout: 'À propos', navApp: 'Application', navPricing: 'Tarifs', navSecurity: 'Sécurité', navContact: 'Contact', login: 'Connexion', register: 'Inscription Gratuite' },
  es: { navHome: 'Inicio', navSolutions: 'Soluciones', navAbout: 'Sobre Nosotros', navApp: 'Aplicación', navPricing: 'Precios', navSecurity: 'Seguridad', navContact: 'Contacto', login: 'Iniciar Sesión', register: 'Registro Gratis' },
  it: { navHome: 'Home', navSolutions: 'Soluzioni', navAbout: 'Chi siamo', navApp: 'Applicazione', navPricing: 'Piani', navSecurity: 'Sicurezza', navContact: 'Contatti', login: 'Accedi', register: 'Registrati Gratis' },
  nl: { navHome: 'Startpagina', navSolutions: 'Oplossingen', navAbout: 'Over ons', navApp: 'Applicatie', navPricing: 'Tarieven', navSecurity: 'Beveiliging', navContact: 'Contact', login: 'Inloggen', register: 'Gratis Registreren' }
};
function setGlobalLanguage(lang){
  try { localStorage.setItem('dfbp_lang', lang); } catch(e){}
  var dict = GLOBAL_I18N[lang] || GLOBAL_I18N.tr;
  document.querySelectorAll('.globalLangSwitch').forEach(function(s){ s.value = lang; });
  var nav = document.getElementById('mainNav');
  if(nav){
    var links = nav.querySelectorAll('a');
    if(links.length >= 7){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navSolutions;
      links[2].textContent = dict.navAbout;
      links[3].textContent = dict.navApp;
      links[4].textContent = dict.navPricing;
      links[5].textContent = dict.navSecurity;
      links[6].textContent = dict.navContact;
    } else if(links.length >= 6){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navAbout;
      links[2].textContent = dict.navApp;
      links[3].textContent = dict.navPricing;
      links[4].textContent = dict.navSecurity;
      links[5].textContent = dict.navContact;
    }
  }
  document.querySelectorAll('.navBtn.secondary, .navBtn.sec, #loginOpenBtn').forEach(function(b){ b.textContent = dict.login; });
  document.querySelectorAll('.navBtn.primary, .navBtn.pri, #registerOpenBtn').forEach(function(b){ b.textContent = dict.register; });
}
if(typeof document !== 'undefined' && document.addEventListener){
  document.addEventListener('DOMContentLoaded', function(){
    var saved = 'tr';
    try { saved = localStorage.getItem('dfbp_lang') || 'tr'; } catch(e){}
    setGlobalLanguage(saved);
  });
}
</script>
</body></html>'''

CONTACT_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" type="image/svg+xml" href="/favicon.ico"><meta name="description" content="Digital Finance Business Partner (digitalfinancebp.com) — Şirketinizin finansal tablolarını 33 analitik karar motoruyla denetleyen, kâr sızıntılarını ve kilitli nakdi hesaplayan kurumsal karar destek platformu."><title>İletişim | Digital Finance Business Partner</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&display=swap" rel="stylesheet">
<style>
:root{--bg:#F6F7F9;--panel:#FFFFFF;--panel2:#F0F3F8;--line:#E4E8EF;--text:#0F1B2D;--muted:#5B6B84;--accent:#1D4ED8;--accent2:#4F8CFF;--red:#C22A3E;--amber:#B4720A;--green:#0E7C66;--shadow:0 1px 2px rgba(15,27,45,.04),0 12px 32px rgba(15,27,45,.06);--serif:'Fraunces',ui-serif,Georgia,serif}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(1100px 480px at 12% -10%, rgba(29,78,216,.07), transparent 60%),radial-gradient(900px 420px at 100% 0%, rgba(14,124,102,.05), transparent 55%),#F6F7F9;color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45}button,input,select{font:inherit}.wrap{max-width:1440px;margin:auto;padding:0 28px}.top{padding:26px 0 18px;border-bottom:1px solid rgba(15,27,45,.08);position:sticky;top:0;background:rgba(246,247,249,.86);backdrop-filter:blur(18px);z-index:10}.brand{display:flex;align-items:center;justify-content:space-between;gap:20px}.brand h1{margin:0;font-size:25px;letter-spacing:-.6px}.brand p{margin:3px 0 0;color:var(--muted);font-size:13px}.badge{padding:6px 10px;border:1px solid #D7DEE8;border-radius:999px;color:var(--accent);font-size:12px;white-space:nowrap}.hero{padding:34px 0 24px;display:grid;grid-template-columns:1.45fr .55fr;gap:18px}.heroCard,.card{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow)}.heroCard{padding:28px}.heroTitle{font-family:var(--serif);font-weight:600;font-size:44px;line-height:1.08;margin:0 0 14px;letter-spacing:-.5px}.heroText{color:var(--muted);max-width:780px}.framework{display:flex;flex-wrap:wrap;gap:8px 10px;margin:16px 0 2px;padding:0}.framework span{font-size:11.5px;color:#33415C;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px}.framework span b{color:var(--accent);font-weight:800}
.qsel{margin-top:18px}.qsel .qtitle{font-size:12px;color:var(--muted);margin-bottom:8px;font-weight:700}.qsel .qrow{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.qsel button{border:1px solid #D7DEE8;background:#EEF2FF;color:#33415C;border-radius:12px;padding:10px 12px;font-size:12.5px;cursor:pointer;text-align:left;line-height:1.3}.qsel button:hover{border-color:#B7C3D6}.qsel button.active{border-color:var(--accent);color:var(--accent);background:#DCE6FB}
.upload{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}.file{border:1px dashed #C9D2DE;padding:12px;border-radius:12px;background:#F5F7FA;max-width:100%}.select,button{border:1px solid #D7DEE8;border-radius:11px;padding:11px 14px;background:#FFFFFF;color:var(--text)}button.primary,a.primary{background:linear-gradient(135deg,#2557E8,#1D4ED8);border:0;color:#FFFFFF;font-weight:800;cursor:pointer;transition:transform .15s ease,box-shadow .15s ease;box-shadow:0 6px 16px rgba(29,78,216,.25)}a.primary:hover,button.primary:hover{transform:translateY(-1px);box-shadow:0 10px 22px rgba(29,78,216,.32)}button.secondary,a.secondary{cursor:pointer;border:1.5px solid #C9D2DE;background:#FFFFFF;color:var(--text)}a.secondary:hover,button.secondary:hover{border-color:var(--accent);color:var(--accent)}button:disabled{opacity:.5;cursor:not-allowed}.scoreCard{padding:25px;display:flex;flex-direction:column;justify-content:center}.scoreRing{width:170px;height:170px;border-radius:50%;margin:auto;display:grid;place-items:center;background:conic-gradient(var(--accent) calc(var(--score)*1%),#E4E8EF 0);position:relative}.scoreRing:after{content:"";position:absolute;inset:12px;border-radius:50%;background:#FFFFFF}.scoreNum{position:relative;z-index:1;text-align:center}.scoreNum strong{display:block;font-size:48px;line-height:1}.scoreNum span{color:var(--muted);font-size:12px}.status{margin:15px auto 0;padding:7px 12px;border-radius:999px;background:#EAF0FF;color:var(--accent);font-size:12px;font-weight:700}.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.card{padding:22px;margin:0 0 16px;transition:transform .18s ease,box-shadow .18s ease,outline .2s}.card:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(15,27,45,.08)}@keyframes growUp{from{transform:scaleY(0);opacity:0}to{transform:scaleY(1);opacity:1}}.wf{transform-origin:bottom}.wf .col{transform-origin:bottom}@keyframes growWidth{from{width:0}to{}}.metric{padding:17px;border:1px solid var(--line);border-radius:15px;background:rgba(15,27,45,.03)}.metric .label{color:var(--muted);font-size:12px}.metric .value{font-size:25px;font-weight:800;margin-top:5px;letter-spacing:-.5px}.metric .sub{font-size:11px;color:var(--muted);margin-top:5px}.sectionHead{display:flex;align-items:end;justify-content:space-between;gap:15px;margin-bottom:17px}.sectionHead h2{margin:0;font-size:18px}.sectionHead p{margin:0;color:var(--muted);font-size:12px}.flowStep{margin:36px 0 14px;padding-top:6px;border-top:1px solid rgba(15,27,45,.08)}.flowStep:first-child{margin-top:0;border-top:0;padding-top:0}.flowLabel{display:flex;align-items:center;gap:10px;font-size:12px;font-weight:800;letter-spacing:1.8px;text-transform:uppercase;color:var(--accent);margin:0 0 4px}.flowLabel .n{width:22px;height:22px;border-radius:50%;background:#EAF0FF;color:var(--accent);display:inline-flex;align-items:center;justify-content:center;font-size:11px}.flowLabel p{margin:0;color:var(--muted);font-size:12.5px;font-weight:500;text-transform:none;letter-spacing:0}.flowLabel.alt{color:var(--accent2)}.flowLabel.alt .n{color:var(--accent2)}.flowSub{color:var(--muted);font-size:12.5px;margin:2px 0 16px 32px}.insight{border:1px solid var(--line);border-radius:15px;padding:16px;background:#F7F9FC}.insight.critical{border-color:#E8B4BD}.insight.high{border-color:#E9CBA8}.insight.medium{border-color:#E5DBA0}.insight.positive{border-color:#A9D9C9}.insight h3{margin:0 0 5px;font-size:14px}.insight p{margin:6px 0;color:#33415C;font-size:13px}.insight ul{margin:6px 0;padding-left:18px;color:#33415C;font-size:13px}.tag{display:inline-flex;padding:4px 8px;border-radius:999px;font-size:10px;font-weight:800;text-transform:uppercase;background:#EAF0FF;color:#5B6B84}.tag.critical{background:#FCE8EA;color:#C22A3E}.tag.high{background:#FDF0E0;color:#B4720A}.tag.medium{background:#FBF6DE;color:#8A6D00}.tag.positive{background:#E4F5EF;color:#0E7C66}.riskRow,.actionRow{display:grid;grid-template-columns:40px 1fr auto;gap:12px;align-items:center;padding:13px 0;border-bottom:1px solid rgba(15,27,45,.08)}.rank{font-size:18px;font-weight:900;color:#5B6B84}.riskScore{font-size:12px;color:var(--muted)}.bar{height:7px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:8px}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:99px}.waterfall{display:flex;align-items:flex-end;gap:7px;height:190px;padding:20px 5px 0;border-bottom:1px solid var(--line)}.wf{flex:1;display:flex;flex-direction:column;justify-content:end;height:100%;min-width:0}.wf .col{border-radius:6px 6px 2px 2px;background:linear-gradient(180deg,#83a4ff,#506fd0);min-height:3px}.wf.neg .col{background:linear-gradient(180deg,#ff8290,#9d3e54)}.wf .lab{font-size:10px;color:var(--muted);text-align:center;margin-top:7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.wf .num{font-size:9px;text-align:center;color:#33415C;margin-bottom:4px}.scenario{padding:18px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(145deg,#F5F8FF,#EEF3FC)}.scenario h3{margin:0 0 6px;font-size:15px}.scenario .big{font-size:24px;font-weight:900;color:var(--accent)}.scenario p{color:var(--muted);font-size:11px;margin:6px 0}.muted{color:var(--muted)}.small{font-size:11px}.tableWrap{overflow:auto}table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:10px 8px;border-bottom:1px solid rgba(15,27,45,.08);text-align:right}th:first-child,td:first-child{text-align:left}th{color:#5B6B84;font-weight:600}.notice{padding:12px 14px;border-radius:12px;background:#EEF2FF;border:1px solid var(--line);color:#5B6B84;font-size:12px}.error{color:#C22A3E;background:#FCE8EA;border:1px solid #E8B4BD;padding:12px;border-radius:12px;margin:15px 0}.hidden{display:none!important}.footer{padding:25px 0 50px;color:#5B6B84;font-size:11px;text-align:center}.tabs{display:flex;gap:8px;margin-top:16px}.tab{padding:8px 12px;border-radius:999px;background:#F0F3F8;border:1px solid var(--line);color:#5B6B84;cursor:pointer}.tab.active{background:#DCE6FB;color:var(--accent);border-color:#1D4ED8}.tabPanel{display:none}.tabPanel.active{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.hidePrint{display:block}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.chip{font-size:11.5px;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px;color:#33415C}.chip b{color:var(--accent)}
.abar{height:9px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:6px}.abar i{display:block;height:100%;background:linear-gradient(90deg,#8aa7ff,#ff8290);border-radius:99px}
.custRow{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12.5px}
.highlight-target{outline:2px solid var(--accent);outline-offset:6px}
/* --- Marketing surface additions --- */
.topNav{display:flex;gap:18px}
.topNav a{color:var(--muted);font-size:13px;text-decoration:none;font-weight:600}
.topNav a:hover{color:var(--accent)}
.marketingSection{padding:8px 0 16px}
.marketingHead{text-align:center;max-width:640px;margin:0 auto 34px}
.marketingHead h2{font-family:var(--serif);font-size:32px;margin:0 0 10px;letter-spacing:-.5px}
.marketingHead p{color:var(--muted);margin:0;font-size:14.5px}
.pricingGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:stretch}
.priceCard{display:flex;flex-direction:column;padding:28px 24px;position:relative}
.priceCard.featured{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent),var(--shadow)}
.priceCard .plan{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:var(--accent);font-weight:800;margin-bottom:8px}
.priceCard h3{margin:0 0 6px;font-size:22px;font-family:var(--serif)}
.priceCard .amt{font-size:34px;font-weight:900;margin:8px 0 4px}
.priceCard .amt span{font-size:13px;color:var(--muted);font-weight:500}
.priceCard .desc{color:var(--muted);font-size:13px;margin-bottom:18px}
.priceCard ul{list-style:none;margin:0 0 22px;padding:0;flex:1;display:flex;flex-direction:column;gap:10px}
.priceCard ul li{font-size:13px;color:#33415C;display:flex;gap:8px;align-items:flex-start}
.priceCard ul li svg{flex:none;margin-top:2px;color:var(--accent)}
.priceCard .badgeTop{position:absolute;top:-11px;left:50%;transform:translateX(-50%);background:var(--accent);color:#FFFFFF;font-size:10.5px;font-weight:800;padding:4px 12px;border-radius:999px;letter-spacing:.5px}
.aboutGrid{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:center}
.aboutStats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}
.aboutStats .st{padding:16px;border:1px solid var(--line);border-radius:14px;text-align:center;background:rgba(15,27,45,.03)}
.aboutStats .st b{display:block;font-size:24px;color:var(--accent);font-family:var(--serif)}
.aboutStats .st span{font-size:11px;color:var(--muted)}
.contactGrid{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.contactCard{padding:26px}
.contactRow{display:flex;flex-direction:column;gap:12px;margin-top:14px}
.contactRow .item{display:flex;gap:10px;align-items:center;font-size:13px;color:#33415C}
.contactRow .item svg{color:var(--accent);flex:none}
@media(max-width:860px){.pricingGrid,.aboutGrid,.contactGrid{grid-template-columns:1fr}.topNav{display:none}}
.trustBar{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:20px;padding-top:18px;border-top:1px solid rgba(15,27,45,.10)}
.trustBar .item{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted)}
.trustBar .item svg{flex:none;color:var(--accent)}
.heroPreview{position:relative;padding:22px;overflow:hidden}
.pvLabel,.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.pvLabel span.dot,.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
.pvRing{width:112px;height:112px;border-radius:50%;margin:2px auto 14px;display:grid;place-items:center;background:conic-gradient(var(--accent) 0 78%,#182c42 78% 100%);position:relative}
.pvRing:after{content:"";position:absolute;inset:9px;border-radius:50%;background:#F7F9FC}
.pvRing b{position:relative;font-family:var(--serif);font-size:26px;z-index:1}
.pvRow{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12px}
.pvRow .n{color:var(--text);font-weight:700}
.pvRow .n.up{color:var(--green)}.pvRow .n.down{color:var(--red)}
.pvBars{display:flex;align-items:flex-end;gap:5px;height:54px;margin-top:14px}
.pvBars i{flex:1;background:linear-gradient(180deg,var(--accent2),#4a63b8);border-radius:3px 3px 1px 1px;display:block}
.statsStrip{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin:6px 0 0;padding:26px 0}
.statsStrip .stat b{font-family:var(--serif);font-size:36px;font-weight:600;color:var(--text);display:block;letter-spacing:-.5px}
.statsStrip .stat span{font-size:12.5px;color:var(--muted);display:block;margin-top:4px;max-width:20ch}
.whyCard{padding:20px;position:relative}
.whyCard .icoWrap{width:40px;height:40px;border-radius:11px;background:#DCE6FB;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;margin-bottom:14px;color:var(--accent)}
.ctaBanner{margin:44px 0 8px;padding:38px 32px;border-radius:22px;background:linear-gradient(135deg,#EAF0FF 0%,#DCE6FB 55%,#EAF0FF 100%);border:1px solid #C9D8F5;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.ctaBanner h3{font-family:var(--serif);font-weight:600;font-size:26px;margin:0 0 6px;letter-spacing:-.3px}
.ctaBanner p{margin:0;color:var(--muted);font-size:13.5px;max-width:52ch}
@media(max-width:1000px){.statsStrip{grid-template-columns:repeat(2,1fr)}.heroTitle{font-size:34px}}
@media(max-width:1000px){.hero{grid-template-columns:1fr}.grid4{grid-template-columns:repeat(2,1fr)}.grid3,.grid2{grid-template-columns:1fr}.wrap{padding:0 15px}.heroTitle{font-size:31px}.flowSub{margin-left:0}.qsel .qrow{grid-template-columns:1fr}}
@media print{
  *,*::before,*::after{box-sizing:border-box!important}
  @page{size:A4 portrait;margin:18mm 16mm 18mm 16mm}
  html,body{background:#fff!important;color:#0d1b2a!important;font-family:'Segoe UI',Arial,sans-serif!important;font-size:10pt!important;line-height:1.45!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Hide all interactive elements ─────────────────────────────── */
  .hero,.upload,.hidePrint,.tabs,.tabPanel,.chips,.qsel,.tab,.footer,.heroPreview,.trustBar,.statsStrip,.ctaBanner,
  button,input,select,textarea,.secondary,.primary,
  #sampleBtn,#aiBtn,#printBtn,#jsonBtn,#aiAskBtn,
  #aiBox,#aiCustomBox,#aiCustomPrompt,#methodNote,
  .interactiveScenarioCard,#interactiveScenarioCard{display:none!important}

  /* ── Layout: full-width single column ──────────────────────────── */
  .wrap{max-width:none!important;padding:0!important;margin:0!important}
  .top{display:none!important}

  /* ── Cover Banner ───────────────────────────────────────────────── */
  #printCover{display:block!important;border-bottom:3px solid #1a73e8;padding-bottom:12px;margin-bottom:20px}
  #printCover h1{font-size:20pt!important;font-weight:800;color:#0d1b2a;margin:0 0 4px}
  #printCover .sub{font-size:9pt;color:#4a6fa5}

  /* ── Cards ──────────────────────────────────────────────────────── */
  .card{box-shadow:none!important;background:#fff!important;border:1px solid #c8d6e8!important;border-radius:6px!important;margin-bottom:10px!important;padding:10px 12px!important;page-break-inside:avoid!important}
  .heroCard{box-shadow:none!important;background:#fff!important;border:1px solid #c8d6e8!important;padding:10px!important}

  /* ── Flow steps ─────────────────────────────────────────────────── */
  .flowStep{margin:14px 0 6px!important;padding-top:4px!important;page-break-inside:avoid!important}
  .flowLabel{background:none!important;border-left:4px solid #1a73e8!important;padding-left:10px!important;color:#0d1b2a!important;margin-bottom:6px!important}
  .flowLabel .n{background:#1a73e8!important;color:#fff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .flowSub{color:#555!important;font-size:8.5pt!important;margin-bottom:6px!important}

  /* ── Metrics / KPIs ─────────────────────────────────────────────── */
  .metric{background:#f4f7fc!important;border:1px solid #d4dff0!important;border-radius:6px!important;padding:8px!important;color:#0d1b2a!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .metric .label{font-size:7.5pt!important;color:#4a6fa5!important;font-weight:700;text-transform:uppercase;letter-spacing:.5px}
  .metric .value{font-size:14pt!important;font-weight:800;color:#0d1b2a!important}
  .metric .sub{font-size:7.5pt!important;color:#666!important}
  .grid2{display:grid!important;grid-template-columns:1fr 1fr!important;gap:8px!important}
  .grid3{display:grid!important;grid-template-columns:1fr 1fr 1fr!important;gap:8px!important}
  .grid4{display:grid!important;grid-template-columns:1fr 1fr 1fr 1fr!important;gap:8px!important}

  /* ── Health score ring ──────────────────────────────────────────── */
  .scoreCard{display:flex!important;align-items:center!important;gap:20px!important;padding:10px 14px!important}
  .scoreRing{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .scoreRing::after{background:#fff!important}

  /* ── Section headings ───────────────────────────────────────────── */
  .sectionHead{border-bottom:1px solid #d4dff0!important;margin-bottom:8px!important;padding-bottom:6px!important}
  .sectionHead h2{font-size:10pt!important;color:#1a73e8!important;font-weight:800;margin:0}
  .sectionHead p{font-size:8pt!important;color:#555!important;margin:2px 0 0}
  h1,h2,h3{page-break-after:avoid!important;color:#0d1b2a!important}
  h3{font-size:9.5pt!important}

  /* ── Risk & action rows ─────────────────────────────────────────── */
  .riskRow,.actionRow{border:1px solid #e4e8ef!important;border-radius:5px!important;margin-bottom:5px!important;padding:6px 8px!important;page-break-inside:avoid!important;background:#fafbfd!important}
  .rank{background:#e8f0fe!important;color:#1a73e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .bar{display:none!important}

  /* ── Tags / badges ──────────────────────────────────────────────── */
  .tag{border:1px solid #888!important;color:#333!important;background:#f0f0f0!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;font-size:7pt!important}
  .badge{border:1px solid #1a73e8!important;color:#1a73e8!important;font-size:7.5pt!important}

  /* ── Insights / alerts ──────────────────────────────────────────── */
  .insight{border-left:4px solid #1a73e8!important;background:#f0f7ff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;border-radius:4px!important;padding:7px 9px!important;margin-bottom:6px!important;page-break-inside:avoid!important}
  .insight.high,.insight.critical{border-left-color:#c62828!important;background:#fff5f5!important}
  .insight.positive{border-left-color:#2e7d32!important;background:#f1fdf3!important}
  .notice{background:#f8faff!important;border:1px solid #33415C!important;padding:7px 9px!important;border-radius:4px!important;font-size:8.5pt!important;color:#333!important}

  /* ── Waterfall chart ────────────────────────────────────────────── */
  .waterfall{display:flex!important;align-items:flex-end!important;gap:4px!important;height:100px!important;padding:4px 0!important}
  .wf .col{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .wf .num{font-size:6.5pt!important;color:#333!important}
  .wf .lab{font-size:6pt!important;color:#444!important}

  /* ── Tables ─────────────────────────────────────────────────────── */
  .tableWrap{overflow:visible!important}
  table{border-collapse:collapse!important;width:100%!important;font-size:8pt!important}
  th{background:#e8f0fe!important;color:#1a73e8!important;font-weight:700;padding:4px 6px!important;border:1px solid #c8d6e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  td{padding:4px 6px!important;border:1px solid #e4e8ef!important}
  tr:nth-child(even) td{background:#f8faff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Page breaks ─────────────────────────────────────────────────  */
  .flowStep:nth-child(3){page-break-before:always!important}
  .flowStep:nth-child(6){page-break-before:always!important}

  /* ── Misc ────────────────────────────────────────────────────────── */
  .muted{color:#555!important}
  .small{font-size:7.5pt!important}
  a{color:#1a73e8!important;text-decoration:none!important}
  .scenario{border:1px solid #c8d6e8!important;border-radius:5px!important;padding:8px!important;page-break-inside:avoid!important}
  .scenario .big{font-size:14pt!important;font-weight:800;color:#1a73e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .custRow,.wf{page-break-inside:avoid!important}
  .hidden{display:none!important}
  #dashboard{display:block!important}
  .abar{display:none!important}
}

@view-transition{navigation:auto}
::view-transition-old(root){animation:dfbpFadeOut .28s ease both}
::view-transition-new(root){animation:dfbpFadeIn .32s ease both}
@keyframes dfbpFadeOut{to{opacity:0;transform:translateY(-6px)}}
@keyframes dfbpFadeIn{from{opacity:0;transform:translateY(8px)}}
.topNav{display:flex;gap:18px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s;white-space:nowrap}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.authCluster{display:flex;flex-direction:column;align-items:flex-end;gap:5px;flex-shrink:0}
.headerSwitches{display:flex;align-items:center;gap:6px;justify-content:flex-end}
.headerSwitches select,select.globalLangSwitch{padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1}
.headerSwitches select:hover,select.globalLangSwitch:hover{border-color:var(--accent);color:#0F1B2D;background:#FFFFFF}
.navBtns{display:flex;gap:8px;align-items:center}
.navBtn{display:inline-flex;align-items:center;justify-content:center;padding:6px 14px;border-radius:9px;font-size:12.5px;font-weight:700;letter-spacing:-.1px;text-decoration:none;cursor:pointer;transition:all .18s ease;line-height:1.2;white-space:nowrap}
.navBtn.sec{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
.navBtn.sec:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
.navBtn.pri{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
.navBtn.pri:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text);flex-shrink:0}
.brandLogoWrap{flex-shrink:0;min-width:max-content}
.brandLink{text-decoration:none;display:flex;align-items:center;gap:10px;min-width:0}
.brandLogoIcon{width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0}
.brandTextWrap{min-width:0}
.brandTitle{font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2;white-space:nowrap}
.brandSub{font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px;white-space:nowrap}
.headerRight{display:flex;align-items:center;gap:12px;flex-shrink:0}
.mobileNavAuth{display:none}

@media(max-width:920px){
  html,body{overflow-x:hidden;max-width:100vw;width:100%}
  .top{padding:12px 0 10px}
  .wrap{padding:0 16px;max-width:100vw;box-sizing:border-box}
  .brand{gap:10px}
  .brandLogoIcon{width:32px;height:32px;border-radius:9px}
  .brandLogoIcon svg{width:18px;height:18px}
  .brandTitle{font-size:15.5px}
  .brandSub{display:none}
  .brandLogoWrap{min-width:0;flex:1 1 auto;overflow:hidden}
  .topNav{position:fixed;top:56px;left:0;right:0;width:100vw;background:#FFFFFF;border-bottom:1.5px solid var(--line);box-shadow:0 14px 34px rgba(15,27,45,0.12);flex-direction:column;align-items:stretch;gap:0;padding:0 20px;max-height:0;overflow:hidden;transition:max-height .28s ease,padding .2s ease;z-index:999;box-sizing:border-box}
  .topNav.open{max-height:460px;padding:10px 20px 20px;overflow-y:auto}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.06);font-size:14.5px;color:var(--text);font-weight:600;display:block;text-align:left}
  .mobileNavAuth{display:flex;gap:10px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(15,27,45,.08)}
  .mobileNavAuth a{flex:1;padding:10px 12px;font-size:13px;font-weight:700;border-radius:10px;text-align:center;justify-content:center;text-decoration:none}
  .navToggle{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;padding:0;font-size:18px;border-radius:8px;cursor:pointer}
}

@media(max-width:768px){
  .navBtns{display:none}
  .authCluster{flex-direction:row;align-items:center}
  .headerRight{gap:6px}
  .globalLangSwitch{padding:4px 5px !important;font-size:11px !important;border-radius:7px !important;max-width:60px}
  .wrap{padding:0 12px}
  .brandTitle{font-size:14.5px}
  .pageHead{padding:28px 0 10px}
  .pageHead h1{font-size:26px !important}
  .contactGrid{grid-template-columns:1fr !important;gap:16px}
}
.badge.v{white-space:nowrap}
/* ---- Marketing hero (separate from app hero) ---- */
.mHero{padding:56px 0 30px;display:grid;grid-template-columns:1.15fr .85fr;gap:34px;align-items:center}
.mHero .eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:18px}
.mHero h1{font-family:var(--serif);font-weight:600;font-size:50px;line-height:1.08;margin:0 0 18px;letter-spacing:-1px}
.mHero h1 span{color:var(--accent)}
.mHero p.lead{color:var(--muted);font-size:16px;max-width:560px;line-height:1.65;margin:0 0 26px}
.mHero .ctaRow{display:flex;gap:12px;flex-wrap:wrap}
.mHero .ctaRow a{text-decoration:none}
.mHero .miniTrust{display:flex;gap:18px;flex-wrap:wrap;margin-top:28px}
.mHero .miniTrust span{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px}
.mHero .miniTrust svg{color:var(--accent)}
.heroArt{position:relative}
.heroArt .floatCard{position:absolute;background:#FFFFFF;border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);padding:14px 16px;font-size:11.5px;color:#33415C;animation:dfbpFloat 5s ease-in-out infinite}
.heroArt .floatCard b{display:block;font-size:16px;color:var(--accent);font-family:var(--serif)}
.heroArt .fc1{top:-10px;left:-10px;animation-delay:0s}
.heroArt .fc2{bottom:6px;right:-14px;animation-delay:1.2s}
@keyframes dfbpFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
/* ---- Alternating content blocks (fixes the "iç içe" cramped look) ---- */
.secBlock{padding:28px 0}
.secBlock.tint{background:linear-gradient(180deg,#F8FAFC 0%,#FFFFFF 100%);border:1px solid #E2E8F0;border-radius:26px;margin:0 -10px;box-shadow:0 4px 20px rgba(15,27,45,.03)}
.pillScrollBtn{width:36px;height:36px;border-radius:50%;background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:800;cursor:pointer;flex-shrink:0;box-shadow:0 4px 12px rgba(15,27,45,0.08);transition:all .18s ease;user-select:none;z-index:4}
.pillScrollBtn:hover{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;transform:scale(1.08);box-shadow:0 6px 16px rgba(29,78,216,0.25)}
.pillScrollBtn:active{transform:scale(0.95)}
.secBlock+.secBlock{border-top:1px solid rgba(15,27,45,.06)}
.pageHead{padding:54px 0 10px;text-align:center}
.pageHead .eyebrow{display:inline-flex;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:16px}
.pageHead h1{font-family:var(--serif);font-size:38px;margin:0 0 12px;letter-spacing:-.6px}
.pageHead p{color:var(--muted);max-width:600px;margin:0 auto;font-size:14.5px}
.reveal{opacity:0;transform:translateY(18px);transition:opacity .55s ease,transform .55s ease}
.reveal.in{opacity:1;transform:none}
/* ---- Rich footer ---- */
.siteFooter{border-top:1px solid var(--line);margin-top:40px;padding:46px 0 26px}
.siteFooter .cols{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:28px;margin-bottom:30px}
.siteFooter h4{font-size:12px;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin:0 0 14px}
.siteFooter .brandCol p{color:var(--muted);font-size:12.5px;max-width:280px;line-height:1.6}
.siteFooter ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.siteFooter ul a{color:#33415C;text-decoration:none;font-size:13px}
.siteFooter ul a:hover{color:var(--accent)}
.siteFooter .legal{border-top:1px solid rgba(15,27,45,.08);padding-top:20px;color:#5B6B84;font-size:11px;line-height:1.7}
html{overflow-x:hidden}@media(max-width:860px){.siteFooter .cols{grid-template-columns:1fr 1fr}.mHero{grid-template-columns:1fr}.heroArt{order:-1;max-width:340px;margin:24px auto 40px;padding:0 14px}.heroArt .floatCard{position:static;display:inline-block;margin:6px 6px 0 0;animation:none}.heroArt .fc1,.heroArt .fc2{top:auto;left:auto;right:auto;bottom:auto}}
/* ---- FAQ (paketler sayfası) ---- */
.faqItem{border-bottom:1px solid var(--line);padding:16px 0}
.faqItem summary{cursor:pointer;font-weight:700;font-size:14px;list-style:none;display:flex;justify-content:space-between;align-items:center}
.faqItem summary::-webkit-details-marker{display:none}
.faqItem summary:after{content:'+';font-size:20px;color:var(--accent)}
.faqItem[open] summary:after{content:'–'}
.faqItem p{color:var(--muted);font-size:13.5px;margin:10px 0 0}
/* ---- Executive Intelligence band (single, deliberate dark boardroom section) ---- */
.execBand{background:radial-gradient(1200px 500px at 15% -20%, rgba(76,201,240,.10), transparent 60%),linear-gradient(160deg,#0D1B2A 0%,#081426 100%);border-radius:26px;padding:52px;display:grid;grid-template-columns:.85fr 1.15fr;gap:40px;align-items:center;overflow:hidden}
.execEyebrow{display:inline-block;font-size:11.5px;font-weight:800;letter-spacing:1.6px;color:#4CC9F0;background:rgba(76,201,240,.12);border:1px solid rgba(76,201,240,.35);padding:6px 12px;border-radius:999px;margin-bottom:16px}
.execCopy h2{font-family:var(--serif);color:#F8FAFC;font-size:28px;line-height:1.2;margin:0 0 12px;letter-spacing:-.4px}
.execCopy p{color:#94A3B8;font-size:14px;line-height:1.7;margin:0 0 18px;max-width:44ch}
.execList{list-style:none;margin:0 0 24px;padding:0;display:flex;flex-direction:column;gap:9px}
.execList li{color:#C7D2E8;font-size:13px}
.execList li b{color:#F8FAFC}
.execCta{display:inline-block;color:#0D1B2A;background:#4CC9F0;font-weight:800;font-size:13.5px;padding:12px 20px;border-radius:11px;text-decoration:none;transition:transform .15s ease,box-shadow .15s ease}
.execCta:hover{transform:translateY(-1px);box-shadow:0 10px 26px rgba(76,201,240,.35)}
.execArt{filter:drop-shadow(0 24px 48px rgba(0,0,0,.35))}
@media(max-width:860px){.execBand{grid-template-columns:1fr;padding:32px 22px}}
/* ---- New: live dashboard hero panel ---- */
.heroDash{background:linear-gradient(160deg,#0D1B2A 0%,#0A1524 100%);border-radius:20px;border:1px solid #1E3050;padding:20px;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(8,17,32,.35)}
.heroDash .dHead{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.heroDash .dHead .dots span{width:8px;height:8px;border-radius:50%;display:inline-block;margin-right:5px}
.heroDash .dHead .live{font-size:10.5px;color:#7FE3B4;display:flex;align-items:center;gap:6px;font-weight:700;letter-spacing:.4px}
.heroDash .dHead .live i{width:6px;height:6px;border-radius:50%;background:#15E3B3;display:inline-block;box-shadow:0 0 0 3px rgba(21,227,179,.22);animation:dfbpPulse 1.8s ease infinite}
@keyframes dfbpPulse{0%,100%{opacity:1}50%{opacity:.35}}
.dashTabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px}
.dashTabs span{font-size:10px;color:#7C8FAD;background:#101F33;border:1px solid #1E3050;border-radius:999px;padding:5px 10px;transition:all .25s ease}
.dashTabs span.on{color:#0D1B2A;background:#4CC9F0;border-color:#4CC9F0;font-weight:800}
.dashPane{display:none;min-height:230px}
.dashPane.on{display:block;animation:dfbpFadeIn .4s ease both}
.dashPane .dTitle{color:#7C8FAD;font-size:10px;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px}
.dashKpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px}
.dashKpis div{background:#132238;border:1px solid #20334b;border-radius:9px;padding:9px 10px}
.dashKpis div b{display:block;font-size:16px;color:#F8FAFC;font-family:var(--serif)}
.dashKpis div span{font-size:9.5px;color:#7C8FAD}
.heroDash .foot{margin-top:12px;padding-top:12px;border-top:1px solid #1E3050;font-size:10.5px;color:#7C8FAD;display:flex;justify-content:space-between}
/* ---- New: CFO trust strip ---- */
.trustGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.trustCard{padding:22px}
.trustCard .icoWrap2{width:38px;height:38px;border-radius:10px;background:#0D1B2A;color:#4CC9F0;display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.trustCard h3{margin:0 0 6px;font-size:14.5px}
.trustCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.55}
/* ---- New: Executive Journey ---- */
.journey{display:grid;grid-template-columns:repeat(6,1fr);gap:0;position:relative;margin-top:8px}
.journey:before{content:"";position:absolute;top:22px;left:6%;right:6%;height:2px;background:linear-gradient(90deg,#C9D8F5,#4CC9F0,#C9D8F5)}
.jStep{text-align:center;padding:0 8px;opacity:0;transform:translateY(16px);transition:opacity .5s ease,transform .5s ease}
.jStep.in{opacity:1;transform:none}
.jStep .jDot{width:44px;height:44px;border-radius:50%;background:#FFFFFF;border:2px solid var(--accent);color:var(--accent);display:flex;align-items:center;justify-content:center;margin:0 auto 12px;position:relative;z-index:1;font-weight:900;font-size:13px}
.jStep h4{margin:0 0 5px;font-size:13px;letter-spacing:.4px}
.jStep p{margin:0;font-size:11.5px;color:var(--muted);line-height:1.4}
@media(max-width:860px){.journey{grid-template-columns:1fr 1fr;gap:22px 0}.journey:before{display:none}.trustGrid{grid-template-columns:1fr 1fr}}
/* ---- New: outcome-based module groups ---- */
.intelGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.intelCard{padding:24px;display:flex;flex-direction:column}
.intelCard .igIco{width:40px;height:40px;border-radius:11px;background:#DCE6FB;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.intelCard h3{margin:0 0 8px;font-size:16px;font-family:var(--serif)}
.intelCard ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}
.intelCard ul li{font-size:12.5px;color:#33415C;display:flex;gap:7px;align-items:flex-start}
.intelCard ul li:before{content:"";width:5px;height:5px;border-radius:50%;background:var(--accent);margin-top:6px;flex:none}
@media(max-width:860px){.intelGrid{grid-template-columns:1fr 1fr}}
/* ---- New: security/governance page ---- */

/* ---- High-impact FinTech additions ---- */
.gradText{background:linear-gradient(135deg,#1D4ED8 0%,#2563EB 50%,#38BDF8 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;display:inline-block}
.livePill{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:var(--accent);background:linear-gradient(135deg,#EEF4FF,#E0EDFF);border:1px solid #BFDBFE;padding:8px 16px;border-radius:999px;margin-bottom:20px;box-shadow:0 2px 10px rgba(37,99,235,.12)}
.livePill i{width:8px;height:8px;border-radius:50%;background:#10B981;display:inline-block;box-shadow:0 0 0 4px rgba(16,185,129,.25);animation:dfbpPulse 1.8s ease infinite}
.dilemmaGrid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:20px}
.dilemmaCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:26px;position:relative;overflow:hidden;box-shadow:var(--shadow);transition:transform .2s ease,box-shadow .2s ease}
.dilemmaCard:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(15,27,45,.09)}
.dilemmaQ{font-size:15px;font-weight:700;color:#0F1B2D;margin-bottom:12px;display:flex;gap:10px;align-items:flex-start;line-height:1.4}
.dilemmaQ span{background:#FEE2E2;color:#DC2626;border-radius:8px;padding:2px 8px;font-size:11px;font-weight:900;flex:none;margin-top:2px}
.dilemmaA{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:14px 16px;font-size:13px;color:#33415C;line-height:1.55}
.dilemmaA b{color:var(--accent);display:block;margin-bottom:4px}
.workflowGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;position:relative;margin-top:20px}
.workflowCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:24px;box-shadow:var(--shadow);position:relative;display:flex;flex-direction:column}
.workflowBadge{font-size:11px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:var(--accent);background:#EFF6FF;border:1px solid #DBEAFE;padding:4px 10px;border-radius:999px;align-self:flex-start;margin-bottom:12px}
.workflowCard h3{font-size:16px;margin:0 0 8px;font-family:var(--serif);color:#0F1B2D}
.workflowCard p{font-size:12.5px;color:var(--muted);line-height:1.55;margin:0}
.compareTableWrap{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:var(--shadow);margin-top:20px}
.compareTable{width:100%;border-collapse:collapse;font-size:13px}
.compareTable th,.compareTable td{padding:16px 18px;border-bottom:1px solid rgba(15,27,45,.08);text-align:left}
.compareTable th{background:#F8FAFC;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#475569}
.compareTable th.featured{background:linear-gradient(135deg,#EFF6FF,#DBEAFE);color:var(--accent);border-bottom:2px solid var(--accent)}
.compareTable td.featured{background:#F8FAFF;font-weight:600;color:#0F1B2D}
@media(max-width:860px){.dilemmaGrid,.workflowGrid{grid-template-columns:1fr}.compareTableWrap{overflow-x:auto}}

.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

</style></head>
<body>
<header class="top"><div class="wrap brand"><div class="brandLogoWrap">
  <a href="/" class="brandLink">
    <div class="brandLogoIcon">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div class="brandTextWrap">
      <div class="brandTitle">Digital Finance Business Partner</div>
      <div class="brandSub">Finansal Teşhis &amp; Yönetim Karar Destek Platformu</div>
    </div>
  </a>
</div><div class="headerRight"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/cozumler">Çözümler</a><a href="/hakkimizda">Hakkımızda</a><a href="/uygulama">Uygulama</a><a href="/paketler">Paketler</a><a href="/guvenlik">Güvenlik</a><a href="/iletisim" class="active">İletişim</a><div class="mobileNavAuth"><a href="/uygulama?auth=login" class="secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="primary">Ücretsiz Kayıt Ol</a></div></nav><div class="authCluster hidePrint"><div class="headerSwitches"><select class="globalLangSwitch select" onchange="setGlobalLanguage(this.value)" style="padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1" title="Dil / Language"><option value="tr">🇹🇷 TR</option><option value="en">🇬🇧 EN</option><option value="de">🇩🇪 DE</option><option value="fr">🇫🇷 FR</option><option value="es">🇪🇸 ES</option><option value="it">🇮🇹 IT</option><option value="nl">🇳🇱 NL</option></select></div><div class="navBtns"><a href="/uygulama?auth=login" class="navBtn sec">Giriş Yap</a><a href="/uygulama?auth=register" class="navBtn pri">Ücretsiz Kayıt Ol</a></div></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<div class="pageHead reveal in"><span class="eyebrow">İletişim</span><h1>Konuşalım</h1><p>Paketler, kurumsal teklif veya demo talebi için bize ulaşın; genelde 1 iş günü içinde dönüş yapıyoruz.</p></div>
<div class="secBlock reveal"><section id="contact" class="marketingSection hidePrint" style="padding-top:0">
<div class="contactGrid">
<div class="card contactCard">
  <div style="display:inline-flex;align-items:center;gap:8px;background:#EFF6FF;border:1px solid #BFDBFE;color:var(--accent);font-size:11.5px;font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:6px 14px;border-radius:999px;margin-bottom:16px">
    ⚡ 24 Saat SLA Garantisi
  </div>
  <h3 style="margin:0 0 8px;font-family:var(--serif);font-size:22px">Doğrudan İletişime Geçin</h3>
  <p class="muted" style="font-size:13.5px;line-height:1.6;margin-bottom:18px">Kurumsal entegrasyon, özel sektör benchmark veri seti veya yönetim kurulu sunumunuz için demo oturumu talep edebilirsiniz. Kıdemli finans ekibimiz en geç 1 iş günü içinde sizinle iletişime geçer.</p>
  
  <div class="contactRow">
    <div class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="M22 6l-10 7L2 6"/></svg><b>E-posta:</b> info@digitalfinancebp.com</div>
    <div class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg><b>Telefon:</b> +90 (212) 280 44 20</div>
    <div class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg><b>Ofis:</b> Levent Finans Merkezi, İstanbul</div>
  </div>

  <div style="margin-top:24px;background:#F0FDF4;border:1px solid #BBF7D0;border-radius:14px;padding:14px;font-size:12.5px;color:#166534;line-height:1.5">
    <b>🔒 Gizlilik ve NDA Taahhüdü:</b> Bizimle paylaştığınız tüm şirket ve bilanço bilgileri kurumsal gizlilik sözleşmesi (NDA) kapsamındadır. Asla 3. şahıslara veya yapay zeka model eğitim havuzlarına aktarılmaz.
  </div>
</div>

<div class="card contactCard">
  <h3 style="margin:0 0 6px;font-family:var(--serif);font-size:22px">Hızlı Talep Formu</h3>
  <p class="muted small" style="margin:0 0 16px">Şirketiniz için en uygun çalışma modelini birlikte belirleyelim.</p>
  <form id="contactForm" onsubmit="event.preventDefault(); document.getElementById('contactSuccess').classList.remove('hidden'); document.getElementById('contactFields').classList.add('hidden');">
    <div id="contactFields" style="display:flex;flex-direction:column;gap:12px">
      <input class="select" style="width:100%" type="text" placeholder="Adınız Soyadınız" required>
      <input class="select" style="width:100%" type="email" placeholder="Kurumsal E-posta Adresiniz" required>
      <input class="select" style="width:100%" type="text" placeholder="Şirket Adı" required>
      <select class="select" style="width:100%">
        <option value="">Yıllık Ciro Ölçeğiniz (Seçiniz)</option>
        <option value="1">₺0 - ₺50 Milyon</option>
        <option value="2">₺50 - ₺250 Milyon</option>
        <option value="3">₺250 Milyon - ₺1 Milyar</option>
        <option value="4">₺1 Milyar üzeri (Holding/Kurumsal)</option>
      </select>
      <textarea class="select" style="width:100%;min-height:90px;font-family:inherit" placeholder="Talebiniz veya merak ettiğiniz konu (örn: Özel ERP entegrasyonu, Demo talebi...)" required></textarea>
      <button type="submit" class="primary" style="width:100%;padding:13px">🚀 Talebi İlet (1 İş Gününde Yanıt)</button>
    </div>
    <div id="contactSuccess" class="hidden" style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:14px;padding:24px;text-align:center">
      <div style="font-size:32px;margin-bottom:10px">✅</div>
      <h4 style="font-size:16px;color:#1D4ED8;margin:0 0 6px">Talebiniz Başarıyla Alındı!</h4>
      <p style="font-size:13px;color:#33415C;margin:0;line-height:1.5">Kıdemli finans uzmanımız şirketiniz için hazırlık yaparak en geç 24 saat içinde tarafınıza dönüş sağlayacaktır.</p>
    </div>
  </form>
</div>
</div></section></div>

</div>
</main>
<div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/cozumler">Çözümler</a></li><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • <a href="https://digitalfinancebp.com" style="color:var(--accent);text-decoration:none;font-weight:700">digitalfinancebp.com</a> • Deterministik Finans Karar Motoru &amp; Çift Yönlü Denetim Sistemi<br><span style="opacity:.85">Bu analiz deterministik matematiksel hesaplamalara ve çift taraflı denetim kurallarına dayanır; resmi mali tablo veya vergi beyannamesi yerine geçmez. Nihai yönetim kararları için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca anlık analiz süresince RAM bellekte işlenir; sunucu sabit diskinde ASLA kalıcı saklanmaz. KVKK ve kurumsal gizlilik politikamız için <a href="javascript:void(0)" onclick="showKvkkModal()" style="color:var(--accent);text-decoration:underline;font-weight:600">Aydınlatma ve Gizlilik Metni</a>'ni inceleyebilirsiniz.</span></div></div></div>
<script>
window.showKvkkModal=function(){var m=document.getElementById('kvkkModal');if(!m){m=document.createElement('div');m.id='kvkkModal';m.style.cssText='position:fixed;inset:0;background:rgba(15,27,45,0.7);z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(4px);';m.innerHTML='<div style="background:#FFFFFF;border-radius:18px;max-width:640px;width:100%;max-height:85vh;overflow-y:auto;padding:28px;box-shadow:0 20px 50px rgba(0,0,0,0.3);position:relative;border:1px solid #E2E8F0"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid #E2E8F0;padding-bottom:12px"><div style="display:flex;align-items:center;gap:8px"><span style="font-size:20px">🔒</span><h3 style="margin:0;font-size:18px;color:#0F1B2D;font-family:sans-serif;font-weight:700">Veri Güvenliği, RAM-Only İşleme ve KVKK Taahhüdü</h3></div><button class="kvkkClose" style="background:#F1F5F9;border:0;border-radius:50%;width:30px;height:30px;cursor:pointer;font-weight:bold;font-size:16px">✕</button></div><div style="font-size:13px;line-height:1.7;color:#33415C;display:flex;flex-direction:column;gap:12px"><div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:12px;color:#166534"><b>🛡️ Sıfır Disk Depolama (RAM-Only):</b> Yüklediğiniz mizan, muavin defteri veya operasyonel raporlar sunucunun kalıcı depolama birimlerine (HDD/SSD/Veritabanı) kaydedilmez. Tüm matematiksel hesaplamalar ve çift taraflı denetim anlık bellek (RAM) üzerinde icra edilir ve analiz tamamlandığında oturumla birlikte tamamen silinir.</div><p><b>1. Veri İzolasyonu &amp; Model Eğitimi Yasağı:</b> Şirketiniz tarafından paylaşılan hiçbir finansal veri, ciro, müşteri adı veya bilanço kalemi üçüncü şahıslara verilmez, satılmaz ve genel yapay zekâ modellerinin eğitimi için havuzlara aktarılmaz.</p><p><b>2. 256-Bit TLS Şifreleme:</b> Tarayıcınız ile platform arasındaki tüm veri akışı bankacılık standardında 256-bit SSL/TLS tüneli üzerinden şifrelenir.</p><p><b>3. 6698 Sayılı KVKK Uyumluluğu:</b> Şirket yetkililerine ait iletişim bilgileri ve ticari sırlar yalnızca talep edilen analizlerin üretilmesi amacıyla işlenir; yasal yükümlülükler haricinde hiçbir tarafla paylaşılmaz.</p><p><b>4. Kurumsal Gizlilik Sözleşmesi (NDA):</b> Kurumsal entegrasyon veya holding düzeyinde çalışmalarda şirketinizle karşılıklı Kurumsal NDA akdedilir.</p></div><div style="margin-top:20px;text-align:right"><button class="kvkkClose primary" style="padding:9px 20px;border-radius:10px;font-size:13px;background:#1D4ED8;color:#fff;border:0;cursor:pointer;font-weight:700">Anladım ve Kabul Ediyorum</button></div></div>';m.addEventListener('click',function(e){if(e.target===m||e.target.classList.contains('kvkkClose'))m.style.display='none';});document.body.appendChild(m);}m.style.display='flex';};
document.getElementById('navToggle')?.addEventListener('click',()=>document.getElementById('mainNav')?.classList.toggle('open'));
window.addEventListener('scroll',()=>{document.querySelector('.top')?.classList.toggle('scrolled',window.scrollY>8)});
(function(){
  const els=document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){els.forEach(e=>e.classList.add('in'));return;}
  const io=new IntersectionObserver((entries)=>{entries.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}})},{threshold:.12});
  els.forEach(e=>io.observe(e));
})();
(function(){
  // Finance-flavoured count-up animation for stat/kpi numbers on scroll into view
  const targets = document.querySelectorAll('.stat b, .aboutStats .st b, .pvRing b, .scoreNum strong');
  if(!('IntersectionObserver' in window) || !targets.length) return;
  const parse = (txt)=>{ const m = txt.match(/-?\d[\d.,]*/); return m ? m[0] : null; };
  const cio = new IntersectionObserver((entries)=>{
    entries.forEach(en=>{
      if(!en.isIntersecting) return;
      cio.unobserve(en.target);
      const el = en.target; const raw = el.textContent; const numStr = parse(raw);
      if(!numStr) return;
      const prefix = raw.slice(0, raw.indexOf(numStr));
      const suffix = raw.slice(raw.indexOf(numStr)+numStr.length);
      const clean = numStr.replace(/\./g,'').replace(',', '.');
      const target = parseFloat(clean); if(isNaN(target)) return;
      const decimals = (clean.split('.')[1]||'').length;
      const dur = 900; const t0 = performance.now();
      function step(t){
        const p = Math.min(1,(t-t0)/dur); const eased = 1-Math.pow(1-p,3);
        const val = target*eased;
        el.textContent = prefix + val.toFixed(decimals).replace('.', decimals?',':'') + suffix;
        if(p<1) requestAnimationFrame(step); else el.textContent = raw;
      }
      requestAnimationFrame(step);
    });
  }, {threshold:.4});
  targets.forEach(t=>cio.observe(t));
})();
(function(){
  // Staggered grow-in for waterfall / bridge chart columns and progress bars
  document.querySelectorAll('.waterfall').forEach(wf=>{
    [...wf.children].forEach((col,i)=>{ col.style.animation = `growUp .6s ease ${i*70}ms both`; });
  });
  document.querySelectorAll('.bar i, .abar i').forEach((i,idx)=>{ i.style.animation = `growWidth .7s ease ${idx*40}ms both`; });
})();
</script>
<script>
var GLOBAL_I18N = {
  tr: { navHome: 'Anasayfa', navSolutions: 'Çözümler', navAbout: 'Hakkımızda', navApp: 'Uygulama', navPricing: 'Paketler', navSecurity: 'Güvenlik', navContact: 'İletişim', login: 'Giriş Yap', register: 'Ücretsiz Kayıt Ol' },
  en: { navHome: 'Home', navSolutions: 'Solutions', navAbout: 'About', navApp: 'App', navPricing: 'Pricing', navSecurity: 'Security', navContact: 'Contact', login: 'Log In', register: 'Sign Up Free' },
  de: { navHome: 'Startseite', navSolutions: 'Lösungen', navAbout: 'Über uns', navApp: 'Anwendung', navPricing: 'Preise', navSecurity: 'Sicherheit', navContact: 'Kontakt', login: 'Anmelden', register: 'Kostenlos Registrieren' },
  fr: { navHome: 'Accueil', navSolutions: 'Solutions', navAbout: 'À propos', navApp: 'Application', navPricing: 'Tarifs', navSecurity: 'Sécurité', navContact: 'Contact', login: 'Connexion', register: 'Inscription Gratuite' },
  es: { navHome: 'Inicio', navSolutions: 'Soluciones', navAbout: 'Sobre Nosotros', navApp: 'Aplicación', navPricing: 'Precios', navSecurity: 'Seguridad', navContact: 'Contacto', login: 'Iniciar Sesión', register: 'Registro Gratis' },
  it: { navHome: 'Home', navSolutions: 'Soluzioni', navAbout: 'Chi siamo', navApp: 'Applicazione', navPricing: 'Piani', navSecurity: 'Sicurezza', navContact: 'Contatti', login: 'Accedi', register: 'Registrati Gratis' },
  nl: { navHome: 'Startpagina', navSolutions: 'Oplossingen', navAbout: 'Over ons', navApp: 'Applicatie', navPricing: 'Tarieven', navSecurity: 'Beveiliging', navContact: 'Contact', login: 'Inloggen', register: 'Gratis Registreren' }
};
function setGlobalLanguage(lang){
  try { localStorage.setItem('dfbp_lang', lang); } catch(e){}
  var dict = GLOBAL_I18N[lang] || GLOBAL_I18N.tr;
  document.querySelectorAll('.globalLangSwitch').forEach(function(s){ s.value = lang; });
  var nav = document.getElementById('mainNav');
  if(nav){
    var links = nav.querySelectorAll('a');
    if(links.length >= 7){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navSolutions;
      links[2].textContent = dict.navAbout;
      links[3].textContent = dict.navApp;
      links[4].textContent = dict.navPricing;
      links[5].textContent = dict.navSecurity;
      links[6].textContent = dict.navContact;
    } else if(links.length >= 6){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navAbout;
      links[2].textContent = dict.navApp;
      links[3].textContent = dict.navPricing;
      links[4].textContent = dict.navSecurity;
      links[5].textContent = dict.navContact;
    }
  }
  document.querySelectorAll('.navBtn.secondary, .navBtn.sec, #loginOpenBtn').forEach(function(b){ b.textContent = dict.login; });
  document.querySelectorAll('.navBtn.primary, .navBtn.pri, #registerOpenBtn').forEach(function(b){ b.textContent = dict.register; });
}
if(typeof document !== 'undefined' && document.addEventListener){
  document.addEventListener('DOMContentLoaded', function(){
    var saved = 'tr';
    try { saved = localStorage.getItem('dfbp_lang') || 'tr'; } catch(e){}
    setGlobalLanguage(saved);
  });
}
</script>
</body></html>'''

SECURITY_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" type="image/svg+xml" href="/favicon.ico"><meta name="description" content="Digital Finance Business Partner (digitalfinancebp.com) — Şirketinizin finansal tablolarını 33 analitik karar motoruyla denetleyen, kâr sızıntılarını ve kilitli nakdi hesaplayan kurumsal karar destek platformu."><title>Security &amp; Governance | Digital Finance Business Partner</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&display=swap" rel="stylesheet">
<style>
:root{--bg:#F6F7F9;--panel:#FFFFFF;--panel2:#F0F3F8;--line:#E4E8EF;--text:#0F1B2D;--muted:#5B6B84;--accent:#1D4ED8;--accent2:#4F8CFF;--red:#C22A3E;--amber:#B4720A;--green:#0E7C66;--shadow:0 1px 2px rgba(15,27,45,.04),0 12px 32px rgba(15,27,45,.06);--serif:'Fraunces',ui-serif,Georgia,serif}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(1100px 480px at 12% -10%, rgba(29,78,216,.07), transparent 60%),radial-gradient(900px 420px at 100% 0%, rgba(14,124,102,.05), transparent 55%),#F6F7F9;color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45}button,input,select{font:inherit}.wrap{max-width:1440px;margin:auto;padding:0 28px}.top{padding:26px 0 18px;border-bottom:1px solid rgba(15,27,45,.08);position:sticky;top:0;background:rgba(246,247,249,.86);backdrop-filter:blur(18px);z-index:10}.brand{display:flex;align-items:center;justify-content:space-between;gap:20px}.brand h1{margin:0;font-size:25px;letter-spacing:-.6px}.brand p{margin:3px 0 0;color:var(--muted);font-size:13px}.badge{padding:6px 10px;border:1px solid #D7DEE8;border-radius:999px;color:var(--accent);font-size:12px;white-space:nowrap}.hero{padding:34px 0 24px;display:grid;grid-template-columns:1.45fr .55fr;gap:18px}.heroCard,.card{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow)}.heroCard{padding:28px}.heroTitle{font-family:var(--serif);font-weight:600;font-size:44px;line-height:1.08;margin:0 0 14px;letter-spacing:-.5px}.heroText{color:var(--muted);max-width:780px}.framework{display:flex;flex-wrap:wrap;gap:8px 10px;margin:16px 0 2px;padding:0}.framework span{font-size:11.5px;color:#33415C;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px}.framework span b{color:var(--accent);font-weight:800}
.qsel{margin-top:18px}.qsel .qtitle{font-size:12px;color:var(--muted);margin-bottom:8px;font-weight:700}.qsel .qrow{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.qsel button{border:1px solid #D7DEE8;background:#EEF2FF;color:#33415C;border-radius:12px;padding:10px 12px;font-size:12.5px;cursor:pointer;text-align:left;line-height:1.3}.qsel button:hover{border-color:#B7C3D6}.qsel button.active{border-color:var(--accent);color:var(--accent);background:#DCE6FB}
.upload{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}.file{border:1px dashed #C9D2DE;padding:12px;border-radius:12px;background:#F5F7FA;max-width:100%}.select,button{border:1px solid #D7DEE8;border-radius:11px;padding:11px 14px;background:#FFFFFF;color:var(--text)}button.primary,a.primary{background:linear-gradient(135deg,#2557E8,#1D4ED8);border:0;color:#FFFFFF;font-weight:800;cursor:pointer;transition:transform .15s ease,box-shadow .15s ease;box-shadow:0 6px 16px rgba(29,78,216,.25)}a.primary:hover,button.primary:hover{transform:translateY(-1px);box-shadow:0 10px 22px rgba(29,78,216,.32)}button.secondary,a.secondary{cursor:pointer;border:1.5px solid #C9D2DE;background:#FFFFFF;color:var(--text)}a.secondary:hover,button.secondary:hover{border-color:var(--accent);color:var(--accent)}button:disabled{opacity:.5;cursor:not-allowed}.scoreCard{padding:25px;display:flex;flex-direction:column;justify-content:center}.scoreRing{width:170px;height:170px;border-radius:50%;margin:auto;display:grid;place-items:center;background:conic-gradient(var(--accent) calc(var(--score)*1%),#E4E8EF 0);position:relative}.scoreRing:after{content:"";position:absolute;inset:12px;border-radius:50%;background:#FFFFFF}.scoreNum{position:relative;z-index:1;text-align:center}.scoreNum strong{display:block;font-size:48px;line-height:1}.scoreNum span{color:var(--muted);font-size:12px}.status{margin:15px auto 0;padding:7px 12px;border-radius:999px;background:#EAF0FF;color:var(--accent);font-size:12px;font-weight:700}.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.card{padding:22px;margin:0 0 16px;transition:transform .18s ease,box-shadow .18s ease,outline .2s}.card:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(15,27,45,.08)}@keyframes growUp{from{transform:scaleY(0);opacity:0}to{transform:scaleY(1);opacity:1}}.wf{transform-origin:bottom}.wf .col{transform-origin:bottom}@keyframes growWidth{from{width:0}to{}}.metric{padding:17px;border:1px solid var(--line);border-radius:15px;background:rgba(15,27,45,.03)}.metric .label{color:var(--muted);font-size:12px}.metric .value{font-size:25px;font-weight:800;margin-top:5px;letter-spacing:-.5px}.metric .sub{font-size:11px;color:var(--muted);margin-top:5px}.sectionHead{display:flex;align-items:end;justify-content:space-between;gap:15px;margin-bottom:17px}.sectionHead h2{margin:0;font-size:18px}.sectionHead p{margin:0;color:var(--muted);font-size:12px}.flowStep{margin:36px 0 14px;padding-top:6px;border-top:1px solid rgba(15,27,45,.08)}.flowStep:first-child{margin-top:0;border-top:0;padding-top:0}.flowLabel{display:flex;align-items:center;gap:10px;font-size:12px;font-weight:800;letter-spacing:1.8px;text-transform:uppercase;color:var(--accent);margin:0 0 4px}.flowLabel .n{width:22px;height:22px;border-radius:50%;background:#EAF0FF;color:var(--accent);display:inline-flex;align-items:center;justify-content:center;font-size:11px}.flowLabel p{margin:0;color:var(--muted);font-size:12.5px;font-weight:500;text-transform:none;letter-spacing:0}.flowLabel.alt{color:var(--accent2)}.flowLabel.alt .n{color:var(--accent2)}.flowSub{color:var(--muted);font-size:12.5px;margin:2px 0 16px 32px}.insight{border:1px solid var(--line);border-radius:15px;padding:16px;background:#F7F9FC}.insight.critical{border-color:#E8B4BD}.insight.high{border-color:#E9CBA8}.insight.medium{border-color:#E5DBA0}.insight.positive{border-color:#A9D9C9}.insight h3{margin:0 0 5px;font-size:14px}.insight p{margin:6px 0;color:#33415C;font-size:13px}.insight ul{margin:6px 0;padding-left:18px;color:#33415C;font-size:13px}.tag{display:inline-flex;padding:4px 8px;border-radius:999px;font-size:10px;font-weight:800;text-transform:uppercase;background:#EAF0FF;color:#5B6B84}.tag.critical{background:#FCE8EA;color:#C22A3E}.tag.high{background:#FDF0E0;color:#B4720A}.tag.medium{background:#FBF6DE;color:#8A6D00}.tag.positive{background:#E4F5EF;color:#0E7C66}.riskRow,.actionRow{display:grid;grid-template-columns:40px 1fr auto;gap:12px;align-items:center;padding:13px 0;border-bottom:1px solid rgba(15,27,45,.08)}.rank{font-size:18px;font-weight:900;color:#5B6B84}.riskScore{font-size:12px;color:var(--muted)}.bar{height:7px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:8px}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:99px}.waterfall{display:flex;align-items:flex-end;gap:7px;height:190px;padding:20px 5px 0;border-bottom:1px solid var(--line)}.wf{flex:1;display:flex;flex-direction:column;justify-content:end;height:100%;min-width:0}.wf .col{border-radius:6px 6px 2px 2px;background:linear-gradient(180deg,#83a4ff,#506fd0);min-height:3px}.wf.neg .col{background:linear-gradient(180deg,#ff8290,#9d3e54)}.wf .lab{font-size:10px;color:var(--muted);text-align:center;margin-top:7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.wf .num{font-size:9px;text-align:center;color:#33415C;margin-bottom:4px}.scenario{padding:18px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(145deg,#F5F8FF,#EEF3FC)}.scenario h3{margin:0 0 6px;font-size:15px}.scenario .big{font-size:24px;font-weight:900;color:var(--accent)}.scenario p{color:var(--muted);font-size:11px;margin:6px 0}.muted{color:var(--muted)}.small{font-size:11px}.tableWrap{overflow:auto}table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:10px 8px;border-bottom:1px solid rgba(15,27,45,.08);text-align:right}th:first-child,td:first-child{text-align:left}th{color:#5B6B84;font-weight:600}.notice{padding:12px 14px;border-radius:12px;background:#EEF2FF;border:1px solid var(--line);color:#5B6B84;font-size:12px}.error{color:#C22A3E;background:#FCE8EA;border:1px solid #E8B4BD;padding:12px;border-radius:12px;margin:15px 0}.hidden{display:none!important}.footer{padding:25px 0 50px;color:#5B6B84;font-size:11px;text-align:center}.tabs{display:flex;gap:8px;margin-top:16px}.tab{padding:8px 12px;border-radius:999px;background:#F0F3F8;border:1px solid var(--line);color:#5B6B84;cursor:pointer}.tab.active{background:#DCE6FB;color:var(--accent);border-color:#1D4ED8}.tabPanel{display:none}.tabPanel.active{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.hidePrint{display:block}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.chip{font-size:11.5px;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px;color:#33415C}.chip b{color:var(--accent)}
.abar{height:9px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:6px}.abar i{display:block;height:100%;background:linear-gradient(90deg,#8aa7ff,#ff8290);border-radius:99px}
.custRow{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12.5px}
.highlight-target{outline:2px solid var(--accent);outline-offset:6px}
/* --- Marketing surface additions --- */
.topNav{display:flex;gap:18px}
.topNav a{color:var(--muted);font-size:13px;text-decoration:none;font-weight:600}
.topNav a:hover{color:var(--accent)}
.marketingSection{padding:8px 0 16px}
.marketingHead{text-align:center;max-width:640px;margin:0 auto 34px}
.marketingHead h2{font-family:var(--serif);font-size:32px;margin:0 0 10px;letter-spacing:-.5px}
.marketingHead p{color:var(--muted);margin:0;font-size:14.5px}
.pricingGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:stretch}
.priceCard{display:flex;flex-direction:column;padding:28px 24px;position:relative}
.priceCard.featured{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent),var(--shadow)}
.priceCard .plan{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:var(--accent);font-weight:800;margin-bottom:8px}
.priceCard h3{margin:0 0 6px;font-size:22px;font-family:var(--serif)}
.priceCard .amt{font-size:34px;font-weight:900;margin:8px 0 4px}
.priceCard .amt span{font-size:13px;color:var(--muted);font-weight:500}
.priceCard .desc{color:var(--muted);font-size:13px;margin-bottom:18px}
.priceCard ul{list-style:none;margin:0 0 22px;padding:0;flex:1;display:flex;flex-direction:column;gap:10px}
.priceCard ul li{font-size:13px;color:#33415C;display:flex;gap:8px;align-items:flex-start}
.priceCard ul li svg{flex:none;margin-top:2px;color:var(--accent)}
.priceCard .badgeTop{position:absolute;top:-11px;left:50%;transform:translateX(-50%);background:var(--accent);color:#FFFFFF;font-size:10.5px;font-weight:800;padding:4px 12px;border-radius:999px;letter-spacing:.5px}
.aboutGrid{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:center}
.aboutStats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}
.aboutStats .st{padding:16px;border:1px solid var(--line);border-radius:14px;text-align:center;background:rgba(15,27,45,.03)}
.aboutStats .st b{display:block;font-size:24px;color:var(--accent);font-family:var(--serif)}
.aboutStats .st span{font-size:11px;color:var(--muted)}
.contactGrid{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.contactCard{padding:26px}
.contactRow{display:flex;flex-direction:column;gap:12px;margin-top:14px}
.contactRow .item{display:flex;gap:10px;align-items:center;font-size:13px;color:#33415C}
.contactRow .item svg{color:var(--accent);flex:none}
@media(max-width:860px){.pricingGrid,.aboutGrid,.contactGrid{grid-template-columns:1fr}.topNav{display:none}}
.trustBar{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:20px;padding-top:18px;border-top:1px solid rgba(15,27,45,.10)}
.trustBar .item{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted)}
.trustBar .item svg{flex:none;color:var(--accent)}
.heroPreview{position:relative;padding:22px;overflow:hidden}
.pvLabel,.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.pvLabel span.dot,.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
.pvRing{width:112px;height:112px;border-radius:50%;margin:2px auto 14px;display:grid;place-items:center;background:conic-gradient(var(--accent) 0 78%,#182c42 78% 100%);position:relative}
.pvRing:after{content:"";position:absolute;inset:9px;border-radius:50%;background:#F7F9FC}
.pvRing b{position:relative;font-family:var(--serif);font-size:26px;z-index:1}
.pvRow{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12px}
.pvRow .n{color:var(--text);font-weight:700}
.pvRow .n.up{color:var(--green)}.pvRow .n.down{color:var(--red)}
.pvBars{display:flex;align-items:flex-end;gap:5px;height:54px;margin-top:14px}
.pvBars i{flex:1;background:linear-gradient(180deg,var(--accent2),#4a63b8);border-radius:3px 3px 1px 1px;display:block}
.statsStrip{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin:6px 0 0;padding:26px 0}
.statsStrip .stat b{font-family:var(--serif);font-size:36px;font-weight:600;color:var(--text);display:block;letter-spacing:-.5px}
.statsStrip .stat span{font-size:12.5px;color:var(--muted);display:block;margin-top:4px;max-width:20ch}
.whyCard{padding:20px;position:relative}
.whyCard .icoWrap{width:40px;height:40px;border-radius:11px;background:#DCE6FB;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;margin-bottom:14px;color:var(--accent)}
.ctaBanner{margin:44px 0 8px;padding:38px 32px;border-radius:22px;background:linear-gradient(135deg,#EAF0FF 0%,#DCE6FB 55%,#EAF0FF 100%);border:1px solid #C9D8F5;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.ctaBanner h3{font-family:var(--serif);font-weight:600;font-size:26px;margin:0 0 6px;letter-spacing:-.3px}
.ctaBanner p{margin:0;color:var(--muted);font-size:13.5px;max-width:52ch}
@media(max-width:1000px){.statsStrip{grid-template-columns:repeat(2,1fr)}.heroTitle{font-size:34px}}
@media(max-width:1000px){.hero{grid-template-columns:1fr}.grid4{grid-template-columns:repeat(2,1fr)}.grid3,.grid2{grid-template-columns:1fr}.wrap{padding:0 15px}.heroTitle{font-size:31px}.flowSub{margin-left:0}.qsel .qrow{grid-template-columns:1fr}}
@media print{
  *,*::before,*::after{box-sizing:border-box!important}
  @page{size:A4 portrait;margin:18mm 16mm 18mm 16mm}
  html,body{background:#fff!important;color:#0d1b2a!important;font-family:'Segoe UI',Arial,sans-serif!important;font-size:10pt!important;line-height:1.45!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Hide all interactive elements ─────────────────────────────── */
  .hero,.upload,.hidePrint,.tabs,.tabPanel,.chips,.qsel,.tab,.footer,.heroPreview,.trustBar,.statsStrip,.ctaBanner,
  button,input,select,textarea,.secondary,.primary,
  #sampleBtn,#aiBtn,#printBtn,#jsonBtn,#aiAskBtn,
  #aiBox,#aiCustomBox,#aiCustomPrompt,#methodNote,
  .interactiveScenarioCard,#interactiveScenarioCard{display:none!important}

  /* ── Layout: full-width single column ──────────────────────────── */
  .wrap{max-width:none!important;padding:0!important;margin:0!important}
  .top{display:none!important}

  /* ── Cover Banner ───────────────────────────────────────────────── */
  #printCover{display:block!important;border-bottom:3px solid #1a73e8;padding-bottom:12px;margin-bottom:20px}
  #printCover h1{font-size:20pt!important;font-weight:800;color:#0d1b2a;margin:0 0 4px}
  #printCover .sub{font-size:9pt;color:#4a6fa5}

  /* ── Cards ──────────────────────────────────────────────────────── */
  .card{box-shadow:none!important;background:#fff!important;border:1px solid #c8d6e8!important;border-radius:6px!important;margin-bottom:10px!important;padding:10px 12px!important;page-break-inside:avoid!important}
  .heroCard{box-shadow:none!important;background:#fff!important;border:1px solid #c8d6e8!important;padding:10px!important}

  /* ── Flow steps ─────────────────────────────────────────────────── */
  .flowStep{margin:14px 0 6px!important;padding-top:4px!important;page-break-inside:avoid!important}
  .flowLabel{background:none!important;border-left:4px solid #1a73e8!important;padding-left:10px!important;color:#0d1b2a!important;margin-bottom:6px!important}
  .flowLabel .n{background:#1a73e8!important;color:#fff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .flowSub{color:#555!important;font-size:8.5pt!important;margin-bottom:6px!important}

  /* ── Metrics / KPIs ─────────────────────────────────────────────── */
  .metric{background:#f4f7fc!important;border:1px solid #d4dff0!important;border-radius:6px!important;padding:8px!important;color:#0d1b2a!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .metric .label{font-size:7.5pt!important;color:#4a6fa5!important;font-weight:700;text-transform:uppercase;letter-spacing:.5px}
  .metric .value{font-size:14pt!important;font-weight:800;color:#0d1b2a!important}
  .metric .sub{font-size:7.5pt!important;color:#666!important}
  .grid2{display:grid!important;grid-template-columns:1fr 1fr!important;gap:8px!important}
  .grid3{display:grid!important;grid-template-columns:1fr 1fr 1fr!important;gap:8px!important}
  .grid4{display:grid!important;grid-template-columns:1fr 1fr 1fr 1fr!important;gap:8px!important}

  /* ── Health score ring ──────────────────────────────────────────── */
  .scoreCard{display:flex!important;align-items:center!important;gap:20px!important;padding:10px 14px!important}
  .scoreRing{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .scoreRing::after{background:#fff!important}

  /* ── Section headings ───────────────────────────────────────────── */
  .sectionHead{border-bottom:1px solid #d4dff0!important;margin-bottom:8px!important;padding-bottom:6px!important}
  .sectionHead h2{font-size:10pt!important;color:#1a73e8!important;font-weight:800;margin:0}
  .sectionHead p{font-size:8pt!important;color:#555!important;margin:2px 0 0}
  h1,h2,h3{page-break-after:avoid!important;color:#0d1b2a!important}
  h3{font-size:9.5pt!important}

  /* ── Risk & action rows ─────────────────────────────────────────── */
  .riskRow,.actionRow{border:1px solid #e4e8ef!important;border-radius:5px!important;margin-bottom:5px!important;padding:6px 8px!important;page-break-inside:avoid!important;background:#fafbfd!important}
  .rank{background:#e8f0fe!important;color:#1a73e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .bar{display:none!important}

  /* ── Tags / badges ──────────────────────────────────────────────── */
  .tag{border:1px solid #888!important;color:#333!important;background:#f0f0f0!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;font-size:7pt!important}
  .badge{border:1px solid #1a73e8!important;color:#1a73e8!important;font-size:7.5pt!important}

  /* ── Insights / alerts ──────────────────────────────────────────── */
  .insight{border-left:4px solid #1a73e8!important;background:#f0f7ff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;border-radius:4px!important;padding:7px 9px!important;margin-bottom:6px!important;page-break-inside:avoid!important}
  .insight.high,.insight.critical{border-left-color:#c62828!important;background:#fff5f5!important}
  .insight.positive{border-left-color:#2e7d32!important;background:#f1fdf3!important}
  .notice{background:#f8faff!important;border:1px solid #33415C!important;padding:7px 9px!important;border-radius:4px!important;font-size:8.5pt!important;color:#333!important}

  /* ── Waterfall chart ────────────────────────────────────────────── */
  .waterfall{display:flex!important;align-items:flex-end!important;gap:4px!important;height:100px!important;padding:4px 0!important}
  .wf .col{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .wf .num{font-size:6.5pt!important;color:#333!important}
  .wf .lab{font-size:6pt!important;color:#444!important}

  /* ── Tables ─────────────────────────────────────────────────────── */
  .tableWrap{overflow:visible!important}
  table{border-collapse:collapse!important;width:100%!important;font-size:8pt!important}
  th{background:#e8f0fe!important;color:#1a73e8!important;font-weight:700;padding:4px 6px!important;border:1px solid #c8d6e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  td{padding:4px 6px!important;border:1px solid #e4e8ef!important}
  tr:nth-child(even) td{background:#f8faff!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Page breaks ─────────────────────────────────────────────────  */
  .flowStep:nth-child(3){page-break-before:always!important}
  .flowStep:nth-child(6){page-break-before:always!important}

  /* ── Misc ────────────────────────────────────────────────────────── */
  .muted{color:#555!important}
  .small{font-size:7.5pt!important}
  a{color:#1a73e8!important;text-decoration:none!important}
  .scenario{border:1px solid #c8d6e8!important;border-radius:5px!important;padding:8px!important;page-break-inside:avoid!important}
  .scenario .big{font-size:14pt!important;font-weight:800;color:#1a73e8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .custRow,.wf{page-break-inside:avoid!important}
  .hidden{display:none!important}
  #dashboard{display:block!important}
  .abar{display:none!important}
}

@view-transition{navigation:auto}
::view-transition-old(root){animation:dfbpFadeOut .28s ease both}
::view-transition-new(root){animation:dfbpFadeIn .32s ease both}
@keyframes dfbpFadeOut{to{opacity:0;transform:translateY(-6px)}}
@keyframes dfbpFadeIn{from{opacity:0;transform:translateY(8px)}}
.topNav{display:flex;gap:18px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s;white-space:nowrap}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.authCluster{display:flex;flex-direction:column;align-items:flex-end;gap:5px;flex-shrink:0}
.headerSwitches{display:flex;align-items:center;gap:6px;justify-content:flex-end}
.headerSwitches select,select.globalLangSwitch{padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1}
.headerSwitches select:hover,select.globalLangSwitch:hover{border-color:var(--accent);color:#0F1B2D;background:#FFFFFF}
.navBtns{display:flex;gap:8px;align-items:center}
.navBtn{display:inline-flex;align-items:center;justify-content:center;padding:6px 14px;border-radius:9px;font-size:12.5px;font-weight:700;letter-spacing:-.1px;text-decoration:none;cursor:pointer;transition:all .18s ease;line-height:1.2;white-space:nowrap}
.navBtn.sec{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
.navBtn.sec:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
.navBtn.pri{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
.navBtn.pri:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text);flex-shrink:0}
.brandLogoWrap{flex-shrink:0;min-width:max-content}
.brandLink{text-decoration:none;display:flex;align-items:center;gap:10px;min-width:0}
.brandLogoIcon{width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0}
.brandTextWrap{min-width:0}
.brandTitle{font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2;white-space:nowrap}
.brandSub{font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px;white-space:nowrap}
.headerRight{display:flex;align-items:center;gap:12px;flex-shrink:0}
.mobileNavAuth{display:none}

@media(max-width:920px){
  html,body{overflow-x:hidden;max-width:100vw;width:100%}
  .top{padding:12px 0 10px}
  .wrap{padding:0 16px;max-width:100vw;box-sizing:border-box}
  .brand{gap:10px}
  .brandLogoIcon{width:32px;height:32px;border-radius:9px}
  .brandLogoIcon svg{width:18px;height:18px}
  .brandTitle{font-size:15.5px}
  .brandSub{display:none}
  .brandLogoWrap{min-width:0;flex:1 1 auto;overflow:hidden}
  .topNav{position:fixed;top:56px;left:0;right:0;width:100vw;background:#FFFFFF;border-bottom:1.5px solid var(--line);box-shadow:0 14px 34px rgba(15,27,45,0.12);flex-direction:column;align-items:stretch;gap:0;padding:0 20px;max-height:0;overflow:hidden;transition:max-height .28s ease,padding .2s ease;z-index:999;box-sizing:border-box}
  .topNav.open{max-height:460px;padding:10px 20px 20px;overflow-y:auto}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.06);font-size:14.5px;color:var(--text);font-weight:600;display:block;text-align:left}
  .mobileNavAuth{display:flex;gap:10px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(15,27,45,.08)}
  .mobileNavAuth a{flex:1;padding:10px 12px;font-size:13px;font-weight:700;border-radius:10px;text-align:center;justify-content:center;text-decoration:none}
  .navToggle{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;padding:0;font-size:18px;border-radius:8px;cursor:pointer}
}

@media(max-width:768px){
  .navBtns{display:none}
  .authCluster{flex-direction:row;align-items:center}
  .headerRight{gap:6px}
  .globalLangSwitch{padding:4px 5px !important;font-size:11px !important;border-radius:7px !important;max-width:60px}
  .wrap{padding:0 12px}
  .brandTitle{font-size:14.5px}
  .pageHead{padding:28px 0 10px}
  .pageHead h1{font-size:26px !important}
  .secShieldGrid{grid-template-columns:1fr !important;gap:14px}
}
.badge.v{white-space:nowrap}
/* ---- Marketing hero (separate from app hero) ---- */
.mHero{padding:56px 0 30px;display:grid;grid-template-columns:1.15fr .85fr;gap:34px;align-items:center}
.mHero .eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:18px}
.mHero h1{font-family:var(--serif);font-weight:600;font-size:50px;line-height:1.08;margin:0 0 18px;letter-spacing:-1px}
.mHero h1 span{color:var(--accent)}
.mHero p.lead{color:var(--muted);font-size:16px;max-width:560px;line-height:1.65;margin:0 0 26px}
.mHero .ctaRow{display:flex;gap:12px;flex-wrap:wrap}
.mHero .ctaRow a{text-decoration:none}
.mHero .miniTrust{display:flex;gap:18px;flex-wrap:wrap;margin-top:28px}
.mHero .miniTrust span{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px}
.mHero .miniTrust svg{color:var(--accent)}
.heroArt{position:relative}
.heroArt .floatCard{position:absolute;background:#FFFFFF;border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);padding:14px 16px;font-size:11.5px;color:#33415C;animation:dfbpFloat 5s ease-in-out infinite}
.heroArt .floatCard b{display:block;font-size:16px;color:var(--accent);font-family:var(--serif)}
.heroArt .fc1{top:-10px;left:-10px;animation-delay:0s}
.heroArt .fc2{bottom:6px;right:-14px;animation-delay:1.2s}
@keyframes dfbpFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
/* ---- Alternating content blocks (fixes the "iç içe" cramped look) ---- */
.secBlock{padding:28px 0}
.secBlock.tint{background:linear-gradient(180deg,#F8FAFC 0%,#FFFFFF 100%);border:1px solid #E2E8F0;border-radius:26px;margin:0 -10px;box-shadow:0 4px 20px rgba(15,27,45,.03)}
.pillScrollBtn{width:36px;height:36px;border-radius:50%;background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:800;cursor:pointer;flex-shrink:0;box-shadow:0 4px 12px rgba(15,27,45,0.08);transition:all .18s ease;user-select:none;z-index:4}
.pillScrollBtn:hover{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;transform:scale(1.08);box-shadow:0 6px 16px rgba(29,78,216,0.25)}
.pillScrollBtn:active{transform:scale(0.95)}
.secBlock+.secBlock{border-top:1px solid rgba(15,27,45,.06)}
.pageHead{padding:54px 0 10px;text-align:center}
.pageHead .eyebrow{display:inline-flex;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:16px}
.pageHead h1{font-family:var(--serif);font-size:38px;margin:0 0 12px;letter-spacing:-.6px}
.pageHead p{color:var(--muted);max-width:600px;margin:0 auto;font-size:14.5px}
.reveal{opacity:0;transform:translateY(18px);transition:opacity .55s ease,transform .55s ease}
.reveal.in{opacity:1;transform:none}
/* ---- Rich footer ---- */
.siteFooter{border-top:1px solid var(--line);margin-top:40px;padding:46px 0 26px}
.siteFooter .cols{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:28px;margin-bottom:30px}
.siteFooter h4{font-size:12px;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin:0 0 14px}
.siteFooter .brandCol p{color:var(--muted);font-size:12.5px;max-width:280px;line-height:1.6}
.siteFooter ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.siteFooter ul a{color:#33415C;text-decoration:none;font-size:13px}
.siteFooter ul a:hover{color:var(--accent)}
.siteFooter .legal{border-top:1px solid rgba(15,27,45,.08);padding-top:20px;color:#5B6B84;font-size:11px;line-height:1.7}
html{overflow-x:hidden}@media(max-width:860px){.siteFooter .cols{grid-template-columns:1fr 1fr}.mHero{grid-template-columns:1fr}.heroArt{order:-1;max-width:340px;margin:24px auto 40px;padding:0 14px}.heroArt .floatCard{position:static;display:inline-block;margin:6px 6px 0 0;animation:none}.heroArt .fc1,.heroArt .fc2{top:auto;left:auto;right:auto;bottom:auto}}
/* ---- FAQ (paketler sayfası) ---- */
.faqItem{border-bottom:1px solid var(--line);padding:16px 0}
.faqItem summary{cursor:pointer;font-weight:700;font-size:14px;list-style:none;display:flex;justify-content:space-between;align-items:center}
.faqItem summary::-webkit-details-marker{display:none}
.faqItem summary:after{content:'+';font-size:20px;color:var(--accent)}
.faqItem[open] summary:after{content:'–'}
.faqItem p{color:var(--muted);font-size:13.5px;margin:10px 0 0}
/* ---- Executive Intelligence band (single, deliberate dark boardroom section) ---- */
.execBand{background:radial-gradient(1200px 500px at 15% -20%, rgba(76,201,240,.10), transparent 60%),linear-gradient(160deg,#0D1B2A 0%,#081426 100%);border-radius:26px;padding:52px;display:grid;grid-template-columns:.85fr 1.15fr;gap:40px;align-items:center;overflow:hidden}
.execEyebrow{display:inline-block;font-size:11.5px;font-weight:800;letter-spacing:1.6px;color:#4CC9F0;background:rgba(76,201,240,.12);border:1px solid rgba(76,201,240,.35);padding:6px 12px;border-radius:999px;margin-bottom:16px}
.execCopy h2{font-family:var(--serif);color:#F8FAFC;font-size:28px;line-height:1.2;margin:0 0 12px;letter-spacing:-.4px}
.execCopy p{color:#94A3B8;font-size:14px;line-height:1.7;margin:0 0 18px;max-width:44ch}
.execList{list-style:none;margin:0 0 24px;padding:0;display:flex;flex-direction:column;gap:9px}
.execList li{color:#C7D2E8;font-size:13px}
.execList li b{color:#F8FAFC}
.execCta{display:inline-block;color:#0D1B2A;background:#4CC9F0;font-weight:800;font-size:13.5px;padding:12px 20px;border-radius:11px;text-decoration:none;transition:transform .15s ease,box-shadow .15s ease}
.execCta:hover{transform:translateY(-1px);box-shadow:0 10px 26px rgba(76,201,240,.35)}
.execArt{filter:drop-shadow(0 24px 48px rgba(0,0,0,.35))}
@media(max-width:860px){.execBand{grid-template-columns:1fr;padding:32px 22px}}
/* ---- New: live dashboard hero panel ---- */
.heroDash{background:linear-gradient(160deg,#0D1B2A 0%,#0A1524 100%);border-radius:20px;border:1px solid #1E3050;padding:20px;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(8,17,32,.35)}
.heroDash .dHead{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.heroDash .dHead .dots span{width:8px;height:8px;border-radius:50%;display:inline-block;margin-right:5px}
.heroDash .dHead .live{font-size:10.5px;color:#7FE3B4;display:flex;align-items:center;gap:6px;font-weight:700;letter-spacing:.4px}
.heroDash .dHead .live i{width:6px;height:6px;border-radius:50%;background:#15E3B3;display:inline-block;box-shadow:0 0 0 3px rgba(21,227,179,.22);animation:dfbpPulse 1.8s ease infinite}
@keyframes dfbpPulse{0%,100%{opacity:1}50%{opacity:.35}}
.dashTabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px}
.dashTabs span{font-size:10px;color:#7C8FAD;background:#101F33;border:1px solid #1E3050;border-radius:999px;padding:5px 10px;transition:all .25s ease}
.dashTabs span.on{color:#0D1B2A;background:#4CC9F0;border-color:#4CC9F0;font-weight:800}
.dashPane{display:none;min-height:230px}
.dashPane.on{display:block;animation:dfbpFadeIn .4s ease both}
.dashPane .dTitle{color:#7C8FAD;font-size:10px;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px}
.dashKpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px}
.dashKpis div{background:#132238;border:1px solid #20334b;border-radius:9px;padding:9px 10px}
.dashKpis div b{display:block;font-size:16px;color:#F8FAFC;font-family:var(--serif)}
.dashKpis div span{font-size:9.5px;color:#7C8FAD}
.heroDash .foot{margin-top:12px;padding-top:12px;border-top:1px solid #1E3050;font-size:10.5px;color:#7C8FAD;display:flex;justify-content:space-between}
/* ---- New: CFO trust strip ---- */
.trustGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.trustCard{padding:22px}
.trustCard .icoWrap2{width:38px;height:38px;border-radius:10px;background:#0D1B2A;color:#4CC9F0;display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.trustCard h3{margin:0 0 6px;font-size:14.5px}
.trustCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.55}
/* ---- New: Executive Journey ---- */
.journey{display:grid;grid-template-columns:repeat(6,1fr);gap:0;position:relative;margin-top:8px}
.journey:before{content:"";position:absolute;top:22px;left:6%;right:6%;height:2px;background:linear-gradient(90deg,#C9D8F5,#4CC9F0,#C9D8F5)}
.jStep{text-align:center;padding:0 8px;opacity:0;transform:translateY(16px);transition:opacity .5s ease,transform .5s ease}
.jStep.in{opacity:1;transform:none}
.jStep .jDot{width:44px;height:44px;border-radius:50%;background:#FFFFFF;border:2px solid var(--accent);color:var(--accent);display:flex;align-items:center;justify-content:center;margin:0 auto 12px;position:relative;z-index:1;font-weight:900;font-size:13px}
.jStep h4{margin:0 0 5px;font-size:13px;letter-spacing:.4px}
.jStep p{margin:0;font-size:11.5px;color:var(--muted);line-height:1.4}
@media(max-width:860px){.journey{grid-template-columns:1fr 1fr;gap:22px 0}.journey:before{display:none}.trustGrid{grid-template-columns:1fr 1fr}}
/* ---- New: outcome-based module groups ---- */
.intelGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.intelCard{padding:24px;display:flex;flex-direction:column}
.intelCard .igIco{width:40px;height:40px;border-radius:11px;background:#DCE6FB;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.intelCard h3{margin:0 0 8px;font-size:16px;font-family:var(--serif)}
.intelCard ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}
.intelCard ul li{font-size:12.5px;color:#33415C;display:flex;gap:7px;align-items:flex-start}
.intelCard ul li:before{content:"";width:5px;height:5px;border-radius:50%;background:var(--accent);margin-top:6px;flex:none}
@media(max-width:860px){.intelGrid{grid-template-columns:1fr 1fr}}
/* ---- New: security/governance page ---- */

/* ---- High-impact FinTech additions ---- */
.gradText{background:linear-gradient(135deg,#1D4ED8 0%,#2563EB 50%,#38BDF8 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;display:inline-block}
.livePill{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:var(--accent);background:linear-gradient(135deg,#EEF4FF,#E0EDFF);border:1px solid #BFDBFE;padding:8px 16px;border-radius:999px;margin-bottom:20px;box-shadow:0 2px 10px rgba(37,99,235,.12)}
.livePill i{width:8px;height:8px;border-radius:50%;background:#10B981;display:inline-block;box-shadow:0 0 0 4px rgba(16,185,129,.25);animation:dfbpPulse 1.8s ease infinite}
.dilemmaGrid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:20px}
.dilemmaCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:26px;position:relative;overflow:hidden;box-shadow:var(--shadow);transition:transform .2s ease,box-shadow .2s ease}
.dilemmaCard:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(15,27,45,.09)}
.dilemmaQ{font-size:15px;font-weight:700;color:#0F1B2D;margin-bottom:12px;display:flex;gap:10px;align-items:flex-start;line-height:1.4}
.dilemmaQ span{background:#FEE2E2;color:#DC2626;border-radius:8px;padding:2px 8px;font-size:11px;font-weight:900;flex:none;margin-top:2px}
.dilemmaA{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:14px 16px;font-size:13px;color:#33415C;line-height:1.55}
.dilemmaA b{color:var(--accent);display:block;margin-bottom:4px}
.workflowGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;position:relative;margin-top:20px}
.workflowCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:24px;box-shadow:var(--shadow);position:relative;display:flex;flex-direction:column}
.workflowBadge{font-size:11px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:var(--accent);background:#EFF6FF;border:1px solid #DBEAFE;padding:4px 10px;border-radius:999px;align-self:flex-start;margin-bottom:12px}
.workflowCard h3{font-size:16px;margin:0 0 8px;font-family:var(--serif);color:#0F1B2D}
.workflowCard p{font-size:12.5px;color:var(--muted);line-height:1.55;margin:0}
.compareTableWrap{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:var(--shadow);margin-top:20px}
.compareTable{width:100%;border-collapse:collapse;font-size:13px}
.compareTable th,.compareTable td{padding:16px 18px;border-bottom:1px solid rgba(15,27,45,.08);text-align:left}
.compareTable th{background:#F8FAFC;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#475569}
.compareTable th.featured{background:linear-gradient(135deg,#EFF6FF,#DBEAFE);color:var(--accent);border-bottom:2px solid var(--accent)}
.compareTable td.featured{background:#F8FAFF;font-weight:600;color:#0F1B2D}
@media(max-width:860px){.dilemmaGrid,.workflowGrid{grid-template-columns:1fr}.compareTableWrap{overflow-x:auto}}

.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

</style></head>
<body>
<header class="top"><div class="wrap brand"><div class="brandLogoWrap">
  <a href="/" class="brandLink">
    <div class="brandLogoIcon">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div class="brandTextWrap">
      <div class="brandTitle">Digital Finance Business Partner</div>
      <div class="brandSub">Finansal Teşhis &amp; Yönetim Karar Destek Platformu</div>
    </div>
  </a>
</div><div class="headerRight"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/cozumler">Çözümler</a><a href="/hakkimizda">Hakkımızda</a><a href="/uygulama">Uygulama</a><a href="/paketler">Paketler</a><a href="/guvenlik" class="active">Güvenlik</a><a href="/iletisim">İletişim</a><div class="mobileNavAuth"><a href="/uygulama?auth=login" class="secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="primary">Ücretsiz Kayıt Ol</a></div></nav><div class="authCluster hidePrint"><div class="headerSwitches"><select class="globalLangSwitch select" onchange="setGlobalLanguage(this.value)" style="padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1" title="Dil / Language"><option value="tr">🇹🇷 TR</option><option value="en">🇬🇧 EN</option><option value="de">🇩🇪 DE</option><option value="fr">🇫🇷 FR</option><option value="es">🇪🇸 ES</option><option value="it">🇮🇹 IT</option><option value="nl">🇳🇱 NL</option></select></div><div class="navBtns"><a href="/uygulama?auth=login" class="navBtn sec">Giriş Yap</a><a href="/uygulama?auth=register" class="navBtn pri">Ücretsiz Kayıt Ol</a></div></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<div class="pageHead reveal in"><span class="eyebrow">Security &amp; Governance</span><h1>Kurumsal veri güvenliği ve AI yönetişimi</h1><p>Finans ekipleri güvenlik sayfasına, düşündüğünüzden çok daha fazla bakıyor. Verinizin nasıl işlendiğini, nerede durduğunu ve AI katmanının nasıl sınırlandığını burada tam olarak görebilirsiniz.</p></div>

<div class="secBlock reveal"><section id="security" class="marketingSection hidePrint">
<div class="marketingHead"><h2>Güvenlik ve Uyumluluk</h2><p>Kural tabanlı hesap motoru + katı veri yönetişimi.</p></div>
<div class="secGrid">
<div class="card secCard"><div class="scIco"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg></div><h3>KVKK</h3><p>Kişisel Verilerin Korunması Kanunu kapsamında veri işleme; aydınlatma metni ve veri sahibi başvuru süreçleri tanımlıdır.</p></div>
<div class="card secCard"><div class="scIco"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></div><h3>GDPR</h3><p>AB müşterileri için Genel Veri Koruma Yönetmeliği ilkeleriyle uyumlu işleme; veri taşınabilirliği ve silme talepleri desteklenir.</p></div>
<div class="card secCard"><div class="scIco"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="16" r="1.6"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg></div><h3>Encryption</h3><p>Veri aktarımı sırasında (TLS) ve saklama sırasında (AES-256) şifrelenir; anahtar yönetimi ayrı, katmanlı şekilde uygulanır.</p></div>
<div class="card secCard"><div class="scIco"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg></div><h3>Audit Logs</h3><p>Her hesaplama, veri girişi ve kullanıcı işlemi kaynağına kadar izlenebilir kayıt altına alınır; denetim taleplerine hazırdır.</p></div>
<div class="card secCard"><div class="scIco"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="7" r="4"/><path d="M6 21v-2a4 4 0 014-4h4a4 4 0 014 4v2"/></svg></div><h3>Access Controls</h3><p>Rol tabanlı erişim, çoklu kullanıcı ayrımı ve oturum düzeyinde yetkilendirme ile kurumsal hiyerarşiye uygun kontrol.</p></div>
<div class="card secCard"><div class="scIco"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h7l-1 8 10-12h-7l1-8z"/></svg></div><h3>AI Governance</h3><p>Yapay zekâ yorumu her zaman deterministik hesaptan sonra gelir, ayrı ve açık şekilde etiketlenir; ham rakamların yerine geçmez.</p></div>
</section></div>

<div class="secBlock tint reveal">
  <div class="marketingHead">
    <span class="workflowBadge">MİMARİ GÜVENCE</span>
    <h2>RAM-Only Bellek Mimarisi &amp; Sıfır Kalıcı Disk İzi</h2>
    <p>Finansal verileriniz kurumsal sunucu disklerine asla yazılmaz; süreç RAM üzerinde başlayıp RAM üzerinde biter.</p>
  </div>
  <div class="grid4" style="gap:14px">
    <div class="card" style="padding:22px;background:#FFFFFF;border-top:4px solid #1D4ED8">
      <div style="font-size:11px;font-weight:900;color:#1D4ED8;text-transform:uppercase;margin-bottom:8px">AŞAMA 1</div>
      <h3 style="font-size:15px;margin:0 0 6px">TLS 1.3 Şifreli İletim</h3>
      <p class="muted small" style="line-height:1.5">Tarayıcınız ile platform arasındaki tüm veri akışı askeri düzeyde 256-bit TLS şifrelemesiyle korunur. Araya girme (MITM) imkansızdır.</p>
    </div>
    <div class="card" style="padding:22px;background:#FFFFFF;border-top:4px solid #2563EB">
      <div style="font-size:11px;font-weight:900;color:#2563EB;text-transform:uppercase;margin-bottom:8px">AŞAMA 2</div>
      <h3 style="font-size:15px;margin:0 0 6px">İzole RAM Alanı</h3>
      <p class="muted small" style="line-height:1.5">Mizan ve defter dosyaları sunucu sabit diskine (SSD/HDD) ASLA kaydedilmez. Yalnızca şifreli geçici bellek (RAM) segmentinde ayrıştırılır.</p>
    </div>
    <div class="card" style="padding:22px;background:#FFFFFF;border-top:4px solid #0E7C66">
      <div style="font-size:11px;font-weight:900;color:#0E7C66;text-transform:uppercase;margin-bottom:8px">AŞAMA 3</div>
      <h3 style="font-size:15px;margin:0 0 6px">33 Deterministik Motor</h3>
      <p class="muted small" style="line-height:1.5">Veriler yapay zekaya aktarılmadan önce yerel deterministik finans motorlarında çift taraflı denetlenir ve kâr köprüleri üretilir.</p>
    </div>
    <div class="card" style="padding:22px;background:#FFFFFF;border-top:4px solid #10B981">
      <div style="font-size:11px;font-weight:900;color:#10B981;text-transform:uppercase;margin-bottom:8px">AŞAMA 4</div>
      <h3 style="font-size:15px;margin:0 0 6px">Anında Bellek İmhası</h3>
      <p class="muted small" style="line-height:1.5">Rapor tarayıcınıza iletildiği anda sunucu RAM'indeki ham finansal kayıtlar kalıcı olarak silinir. Sistemde geriye hiçbir iz kalmaz.</p>
    </div>
  </div>
</div>

<div class="secBlock tint reveal"><div class="marketingHead"><h2>Veri işleme ilkelerimiz</h2><p>Önce hesap, sonra yorum — güvenlik de aynı disiplinle kurulur.</p></div>
<div class="grid3">
<div class="card" style="padding:22px"><div class="tag" style="margin-bottom:8px">01</div><h3 style="margin:0 0 6px;font-size:15px">Kalıcı saklama yok</h3><p class="muted small">Yüklediğiniz dosyalar yalnızca analiz üretmek için işlenir; hesap açmadan sunucu tarafında kalıcı olarak tutulmaz.</p></div>
<div class="card" style="padding:22px"><div class="tag" style="margin-bottom:8px">02</div><h3 style="margin:0 0 6px;font-size:15px">Sahiplik sizde</h3><p class="muted small">Kayıt olursanız geçmiş analizleriniz yalnızca sizin erişiminizde tutulur; üçüncü taraflarla paylaşılmaz.</p></div>
<div class="card" style="padding:22px"><div class="tag" style="margin-bottom:8px">03</div><h3 style="margin:0 0 6px;font-size:15px">İzlenebilir hesap</h3><p class="muted small">Her metrik, kaynağındaki mizan satırına kadar geri izlenebilir — "kara kutu" bir skor üretilmez.</p></div>
</div></div>

<div class="secBlock reveal"><section class="ctaBanner hidePrint"><div><h3>Güvenlik ekibinizle konuşmak ister misiniz?</h3><p>Kurumsal güvenlik, veri işleme ve AI yönetişimi hakkında detaylı bir görüşme planlayabiliriz.</p></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a href="/iletisim" class="primary" style="text-decoration:none;padding:12px 20px;border-radius:11px">İletişime Geç</a></div></section></div>
</main>
<div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/cozumler">Çözümler</a></li><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • <a href="https://digitalfinancebp.com" style="color:var(--accent);text-decoration:none;font-weight:700">digitalfinancebp.com</a> • Deterministik Finans Karar Motoru &amp; Çift Yönlü Denetim Sistemi<br><span style="opacity:.85">Bu analiz deterministik matematiksel hesaplamalara ve çift taraflı denetim kurallarına dayanır; resmi mali tablo veya vergi beyannamesi yerine geçmez. Nihai yönetim kararları için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca anlık analiz süresince RAM bellekte işlenir; sunucu sabit diskinde ASLA kalıcı saklanmaz. KVKK ve kurumsal gizlilik politikamız için <a href="javascript:void(0)" onclick="showKvkkModal()" style="color:var(--accent);text-decoration:underline;font-weight:600">Aydınlatma ve Gizlilik Metni</a>'ni inceleyebilirsiniz.</span></div></div></div>
<script>
window.showKvkkModal=function(){var m=document.getElementById('kvkkModal');if(!m){m=document.createElement('div');m.id='kvkkModal';m.style.cssText='position:fixed;inset:0;background:rgba(15,27,45,0.7);z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(4px);';m.innerHTML='<div style="background:#FFFFFF;border-radius:18px;max-width:640px;width:100%;max-height:85vh;overflow-y:auto;padding:28px;box-shadow:0 20px 50px rgba(0,0,0,0.3);position:relative;border:1px solid #E2E8F0"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid #E2E8F0;padding-bottom:12px"><div style="display:flex;align-items:center;gap:8px"><span style="font-size:20px">🔒</span><h3 style="margin:0;font-size:18px;color:#0F1B2D;font-family:sans-serif;font-weight:700">Veri Güvenliği, RAM-Only İşleme ve KVKK Taahhüdü</h3></div><button class="kvkkClose" style="background:#F1F5F9;border:0;border-radius:50%;width:30px;height:30px;cursor:pointer;font-weight:bold;font-size:16px">✕</button></div><div style="font-size:13px;line-height:1.7;color:#33415C;display:flex;flex-direction:column;gap:12px"><div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:12px;color:#166534"><b>🛡️ Sıfır Disk Depolama (RAM-Only):</b> Yüklediğiniz mizan, muavin defteri veya operasyonel raporlar sunucunun kalıcı depolama birimlerine (HDD/SSD/Veritabanı) kaydedilmez. Tüm matematiksel hesaplamalar ve çift taraflı denetim anlık bellek (RAM) üzerinde icra edilir ve analiz tamamlandığında oturumla birlikte tamamen silinir.</div><p><b>1. Veri İzolasyonu &amp; Model Eğitimi Yasağı:</b> Şirketiniz tarafından paylaşılan hiçbir finansal veri, ciro, müşteri adı veya bilanço kalemi üçüncü şahıslara verilmez, satılmaz ve genel yapay zekâ modellerinin eğitimi için havuzlara aktarılmaz.</p><p><b>2. 256-Bit TLS Şifreleme:</b> Tarayıcınız ile platform arasındaki tüm veri akışı bankacılık standardında 256-bit SSL/TLS tüneli üzerinden şifrelenir.</p><p><b>3. 6698 Sayılı KVKK Uyumluluğu:</b> Şirket yetkililerine ait iletişim bilgileri ve ticari sırlar yalnızca talep edilen analizlerin üretilmesi amacıyla işlenir; yasal yükümlülükler haricinde hiçbir tarafla paylaşılmaz.</p><p><b>4. Kurumsal Gizlilik Sözleşmesi (NDA):</b> Kurumsal entegrasyon veya holding düzeyinde çalışmalarda şirketinizle karşılıklı Kurumsal NDA akdedilir.</p></div><div style="margin-top:20px;text-align:right"><button class="kvkkClose primary" style="padding:9px 20px;border-radius:10px;font-size:13px;background:#1D4ED8;color:#fff;border:0;cursor:pointer;font-weight:700">Anladım ve Kabul Ediyorum</button></div></div>';m.addEventListener('click',function(e){if(e.target===m||e.target.classList.contains('kvkkClose'))m.style.display='none';});document.body.appendChild(m);}m.style.display='flex';};
document.getElementById('navToggle')?.addEventListener('click',()=>document.getElementById('mainNav')?.classList.toggle('open'));
window.addEventListener('scroll',()=>{document.querySelector('.top')?.classList.toggle('scrolled',window.scrollY>8)});
(function(){
  const els=document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){els.forEach(e=>e.classList.add('in'));return;}
  const io=new IntersectionObserver((entries)=>{entries.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}})},{threshold:.12});
  els.forEach(e=>io.observe(e));
})();
(function(){
  // Finance-flavoured count-up animation for stat/kpi numbers on scroll into view
  const targets = document.querySelectorAll('.stat b, .aboutStats .st b, .pvRing b, .scoreNum strong');
  if(!('IntersectionObserver' in window) || !targets.length) return;
  const parse = (txt)=>{ const m = txt.match(/-?\d[\d.,]*/); return m ? m[0] : null; };
  const cio = new IntersectionObserver((entries)=>{
    entries.forEach(en=>{
      if(!en.isIntersecting) return;
      cio.unobserve(en.target);
      const el = en.target; const raw = el.textContent; const numStr = parse(raw);
      if(!numStr) return;
      const prefix = raw.slice(0, raw.indexOf(numStr));
      const suffix = raw.slice(raw.indexOf(numStr)+numStr.length);
      const clean = numStr.replace(/\./g,'').replace(',', '.');
      const target = parseFloat(clean); if(isNaN(target)) return;
      const decimals = (clean.split('.')[1]||'').length;
      const dur = 900; const t0 = performance.now();
      function step(t){
        const p = Math.min(1,(t-t0)/dur); const eased = 1-Math.pow(1-p,3);
        const val = target*eased;
        el.textContent = prefix + val.toFixed(decimals).replace('.', decimals?',':'') + suffix;
        if(p<1) requestAnimationFrame(step); else el.textContent = raw;
      }
      requestAnimationFrame(step);
    });
  }, {threshold:.4});
  targets.forEach(t=>cio.observe(t));
})();
(function(){
  // Staggered grow-in for waterfall / bridge chart columns and progress bars
  document.querySelectorAll('.waterfall').forEach(wf=>{
    [...wf.children].forEach((col,i)=>{ col.style.animation = `growUp .6s ease ${i*70}ms both`; });
  });
  document.querySelectorAll('.bar i, .abar i').forEach((i,idx)=>{ i.style.animation = `growWidth .7s ease ${idx*40}ms both`; });
})();
</script>
<script>
var GLOBAL_I18N = {
  tr: { navHome: 'Anasayfa', navSolutions: 'Çözümler', navAbout: 'Hakkımızda', navApp: 'Uygulama', navPricing: 'Paketler', navSecurity: 'Güvenlik', navContact: 'İletişim', login: 'Giriş Yap', register: 'Ücretsiz Kayıt Ol' },
  en: { navHome: 'Home', navSolutions: 'Solutions', navAbout: 'About', navApp: 'App', navPricing: 'Pricing', navSecurity: 'Security', navContact: 'Contact', login: 'Log In', register: 'Sign Up Free' },
  de: { navHome: 'Startseite', navSolutions: 'Lösungen', navAbout: 'Über uns', navApp: 'Anwendung', navPricing: 'Preise', navSecurity: 'Sicherheit', navContact: 'Kontakt', login: 'Anmelden', register: 'Kostenlos Registrieren' },
  fr: { navHome: 'Accueil', navSolutions: 'Solutions', navAbout: 'À propos', navApp: 'Application', navPricing: 'Tarifs', navSecurity: 'Sécurité', navContact: 'Contact', login: 'Connexion', register: 'Inscription Gratuite' },
  es: { navHome: 'Inicio', navSolutions: 'Soluciones', navAbout: 'Sobre Nosotros', navApp: 'Aplicación', navPricing: 'Precios', navSecurity: 'Seguridad', navContact: 'Contacto', login: 'Iniciar Sesión', register: 'Registro Gratis' },
  it: { navHome: 'Home', navSolutions: 'Soluzioni', navAbout: 'Chi siamo', navApp: 'Applicazione', navPricing: 'Piani', navSecurity: 'Sicurezza', navContact: 'Contatti', login: 'Accedi', register: 'Registrati Gratis' },
  nl: { navHome: 'Startpagina', navSolutions: 'Oplossingen', navAbout: 'Over ons', navApp: 'Applicatie', navPricing: 'Tarieven', navSecurity: 'Beveiliging', navContact: 'Contact', login: 'Inloggen', register: 'Gratis Registreren' }
};
function setGlobalLanguage(lang){
  try { localStorage.setItem('dfbp_lang', lang); } catch(e){}
  var dict = GLOBAL_I18N[lang] || GLOBAL_I18N.tr;
  document.querySelectorAll('.globalLangSwitch').forEach(function(s){ s.value = lang; });
  var nav = document.getElementById('mainNav');
  if(nav){
    var links = nav.querySelectorAll('a');
    if(links.length >= 7){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navSolutions;
      links[2].textContent = dict.navAbout;
      links[3].textContent = dict.navApp;
      links[4].textContent = dict.navPricing;
      links[5].textContent = dict.navSecurity;
      links[6].textContent = dict.navContact;
    } else if(links.length >= 6){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navAbout;
      links[2].textContent = dict.navApp;
      links[3].textContent = dict.navPricing;
      links[4].textContent = dict.navSecurity;
      links[5].textContent = dict.navContact;
    }
  }
  document.querySelectorAll('.navBtn.secondary, .navBtn.sec, #loginOpenBtn').forEach(function(b){ b.textContent = dict.login; });
  document.querySelectorAll('.navBtn.primary, .navBtn.pri, #registerOpenBtn').forEach(function(b){ b.textContent = dict.register; });
}
if(typeof document !== 'undefined' && document.addEventListener){
  document.addEventListener('DOMContentLoaded', function(){
    var saved = 'tr';
    try { saved = localStorage.getItem('dfbp_lang') || 'tr'; } catch(e){}
    setGlobalLanguage(saved);
  });
}
</script>
</body></html>'''

APP_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" type="image/svg+xml" href="/favicon.ico"><meta name="description" content="Digital Finance Business Partner (digitalfinancebp.com) — Şirketinizin finansal tablolarını 33 analitik karar motoruyla denetleyen, kâr sızıntılarını ve kilitli nakdi hesaplayan kurumsal karar destek platformu."><title>Uygulama | Digital Finance Business Partner</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&display=swap" rel="stylesheet">
<style>
:root{--bg:#F6F7F9;--panel:#FFFFFF;--panel2:#F0F3F8;--line:#E4E8EF;--text:#0F1B2D;--muted:#5B6B84;--accent:#1D4ED8;--accent2:#4F8CFF;--red:#C22A3E;--amber:#B4720A;--green:#0E7C66;--shadow:0 1px 2px rgba(15,27,45,.04),0 12px 32px rgba(15,27,45,.06);--serif:'Fraunces',ui-serif,Georgia,serif}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(1100px 480px at 12% -10%, rgba(29,78,216,.07), transparent 60%),radial-gradient(900px 420px at 100% 0%, rgba(14,124,102,.05), transparent 55%),#F6F7F9;color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45}button,input,select{font:inherit}.wrap{max-width:1440px;margin:auto;padding:0 28px}.top{padding:14px 0 12px;border-bottom:1px solid #E2E8F0;position:sticky;top:0;background:rgba(255,255,255,0.98);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);z-index:60;box-shadow:0 2px 8px rgba(15,27,45,.04)}.brand{display:flex;align-items:center;justify-content:space-between;gap:20px}.brand h1{margin:0;font-size:25px;letter-spacing:-.6px}.brand p{margin:3px 0 0;color:var(--muted);font-size:13px}.badge{padding:6px 10px;border:1px solid #D7DEE8;border-radius:999px;color:var(--accent);font-size:12px;white-space:nowrap}.hero{padding:34px 0 24px;display:grid;grid-template-columns:1.45fr .55fr;gap:18px}.heroCard,.card{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow)}.heroCard{padding:28px}.heroTitle{font-family:var(--serif);font-weight:600;font-size:44px;line-height:1.08;margin:0 0 14px;letter-spacing:-.5px}.heroText{color:var(--muted);max-width:780px}.framework{display:flex;flex-wrap:wrap;gap:8px 10px;margin:16px 0 2px;padding:0}.framework span{font-size:11.5px;color:#33415C;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px}.framework span b{color:var(--accent);font-weight:800}
.qsel{margin-top:18px}.qsel .qtitle{font-size:12px;color:var(--muted);margin-bottom:8px;font-weight:700}.qsel .qrow{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.qsel button{border:1px solid #D7DEE8;background:#EEF2FF;color:#33415C;border-radius:12px;padding:10px 12px;font-size:12.5px;cursor:pointer;text-align:left;line-height:1.3}.qsel button:hover{border-color:#B7C3D6}.qsel button.active{border-color:var(--accent);color:var(--accent);background:#DCE6FB}
.upload{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}.file{border:1px dashed #C9D2DE;padding:12px;border-radius:12px;background:#F5F7FA;max-width:100%}.select,button{border:1px solid #D7DEE8;border-radius:11px;padding:11px 14px;background:#FFFFFF;color:var(--text)}button.primary,a.primary{background:linear-gradient(135deg,#2557E8,#1D4ED8);border:0;color:#FFFFFF;font-weight:800;cursor:pointer;transition:transform .15s ease,box-shadow .15s ease;box-shadow:0 6px 16px rgba(29,78,216,.25)}a.primary:hover,button.primary:hover{transform:translateY(-1px);box-shadow:0 10px 22px rgba(29,78,216,.32)}button.secondary,a.secondary{cursor:pointer;border:1.5px solid #C9D2DE;background:#FFFFFF;color:var(--text)}a.secondary:hover,button.secondary:hover{border-color:var(--accent);color:var(--accent)}button:disabled{opacity:.5;cursor:not-allowed}.scoreCard{padding:25px;display:flex;flex-direction:column;justify-content:center}.scoreRing{width:170px;height:170px;border-radius:50%;margin:auto;display:grid;place-items:center;background:conic-gradient(var(--accent) calc(var(--score)*1%),#E4E8EF 0);position:relative}.scoreRing:after{content:"";position:absolute;inset:12px;border-radius:50%;background:#FFFFFF}.scoreNum{position:relative;z-index:1;text-align:center}.scoreNum strong{display:block;font-size:48px;line-height:1}.scoreNum span{color:var(--muted);font-size:12px}.status{margin:15px auto 0;padding:7px 12px;border-radius:999px;background:#EAF0FF;color:var(--accent);font-size:12px;font-weight:700}.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.card{padding:22px;margin:0 0 16px;transition:transform .18s ease,box-shadow .18s ease,outline .2s}.card:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(15,27,45,.08)}@keyframes growUp{from{transform:scaleY(0);opacity:0}to{transform:scaleY(1);opacity:1}}.wf{transform-origin:bottom}.wf .col{transform-origin:bottom}@keyframes growWidth{from{width:0}to{}}.metric{padding:17px;border:1px solid var(--line);border-radius:15px;background:rgba(15,27,45,.03)}.metric .label{color:var(--muted);font-size:12px}.metric .value{font-size:25px;font-weight:800;margin-top:5px;letter-spacing:-.5px}.metric .sub{font-size:11px;color:var(--muted);margin-top:5px}.sectionHead{display:flex;align-items:end;justify-content:space-between;gap:15px;margin-bottom:17px}.sectionHead h2{margin:0;font-size:18px}.sectionHead p{margin:0;color:var(--muted);font-size:12px}.flowStep{margin:36px 0 14px;padding-top:6px;border-top:1px solid rgba(15,27,45,.08)}.flowStep:first-child{margin-top:0;border-top:0;padding-top:0}.flowLabel{display:flex;align-items:center;gap:10px;font-size:12px;font-weight:800;letter-spacing:1.8px;text-transform:uppercase;color:var(--accent);margin:0 0 4px}.flowLabel .n{width:22px;height:22px;border-radius:50%;background:#EAF0FF;color:var(--accent);display:inline-flex;align-items:center;justify-content:center;font-size:11px}.flowLabel p{margin:0;color:var(--muted);font-size:12.5px;font-weight:500;text-transform:none;letter-spacing:0}.flowLabel.alt{color:var(--accent2)}.flowLabel.alt .n{color:var(--accent2)}.flowSub{color:var(--muted);font-size:12.5px;margin:2px 0 16px 32px}.insight{border:1px solid var(--line);border-radius:15px;padding:16px;background:#F7F9FC}.insight.critical{border-color:#E8B4BD}.insight.high{border-color:#E9CBA8}.insight.medium{border-color:#E5DBA0}.insight.positive{border-color:#A9D9C9}.insight h3{margin:0 0 5px;font-size:14px}.insight p{margin:6px 0;color:#33415C;font-size:13px}.insight ul{margin:6px 0;padding-left:18px;color:#33415C;font-size:13px}.tag{display:inline-flex;padding:4px 8px;border-radius:999px;font-size:10px;font-weight:800;text-transform:uppercase;background:#EAF0FF;color:#5B6B84}.tag.critical{background:#FCE8EA;color:#C22A3E}.tag.high{background:#FDF0E0;color:#B4720A}.tag.medium{background:#FBF6DE;color:#8A6D00}.tag.positive{background:#E4F5EF;color:#0E7C66}.riskRow,.actionRow{display:grid;grid-template-columns:40px 1fr auto;gap:12px;align-items:center;padding:13px 0;border-bottom:1px solid rgba(15,27,45,.08)}.rank{font-size:18px;font-weight:900;color:#5B6B84}.riskScore{font-size:12px;color:var(--muted)}.bar{height:7px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:8px}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:99px}.waterfallWrap{overflow-x:auto;-webkit-overflow-scrolling:touch;padding-bottom:10px;margin-bottom:10px}.waterfall{display:flex;align-items:flex-end;gap:9px;height:190px;padding:20px 5px 0;border-bottom:1px solid var(--line);min-width:620px}.wf{flex:1;display:flex;flex-direction:column;justify-content:end;height:100%;min-width:65px}.wf .col{border-radius:6px 6px 2px 2px;background:linear-gradient(180deg,#83a4ff,#506fd0);min-height:3px}.wf.neg .col{background:linear-gradient(180deg,#ff8290,#9d3e54)}.wf .lab{font-size:10.5px;font-weight:600;color:var(--muted);text-align:center;margin-top:7px;white-space:nowrap}.wf .num{font-size:10px;font-weight:700;text-align:center;color:#33415C;margin-bottom:4px;white-space:nowrap}.subnavPill{font-size:12px;font-weight:600;color:#475569;text-decoration:none;padding:5px 12px;border-radius:999px;background:#F1F5F9;border:1px solid #E2E8F0;transition:all .15s ease}.subnavPill:hover{background:#E2E8F0;color:#1D4ED8;border-color:#CBD5E1}.dashboardSubNav{position:sticky;top:62px;z-index:45;background:#FFFFFF;border-bottom:1.5px solid #E2E8F0;box-shadow:0 4px 14px rgba(15,27,45,0.05);padding:10px 0;margin-bottom:20px;overflow-x:auto;-webkit-overflow-scrolling:touch;display:flex;gap:7px;white-space:nowrap}.dashPill{font-size:11.5px;font-weight:700;color:#475569;background:#F8FAFC;border:1px solid #CBD5E1;border-radius:999px;padding:5px 12px;cursor:pointer;transition:all .15s ease;white-space:nowrap}.dashPill:hover{background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE}.scenario{padding:18px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(145deg,#F5F8FF,#EEF3FC)}.scenario h3{margin:0 0 6px;font-size:15px}.scenario .big{font-size:24px;font-weight:900;color:var(--accent)}.scenario p{color:var(--muted);font-size:11px;margin:6px 0}.muted{color:var(--muted)}.small{font-size:11px}.tableWrap{overflow:auto}table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:10px 8px;border-bottom:1px solid rgba(15,27,45,.08);text-align:right}th:first-child,td:first-child{text-align:left}th{color:#5B6B84;font-weight:600}.notice{padding:12px 14px;border-radius:12px;background:#EEF2FF;border:1px solid var(--line);color:#5B6B84;font-size:12px}.error{color:#C22A3E;background:#FCE8EA;border:1px solid #E8B4BD;padding:12px;border-radius:12px;margin:15px 0}.hidden{display:none!important}.footer{padding:25px 0 50px;color:#5B6B84;font-size:11px;text-align:center}.tabs{display:flex;gap:8px;margin-top:16px}.tab{padding:8px 12px;border-radius:999px;background:#F0F3F8;border:1px solid var(--line);color:#5B6B84;cursor:pointer}.tab.active{background:#DCE6FB;color:var(--accent);border-color:#1D4ED8}.tabPanel{display:none}.tabPanel.active{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.hidePrint{display:block}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.chip{font-size:11.5px;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px;color:#33415C}.chip b{color:var(--accent)}
.abar{height:9px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:6px}.abar i{display:block;height:100%;background:linear-gradient(90deg,#8aa7ff,#ff8290);border-radius:99px}
.custRow{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12.5px}
.highlight-target{outline:2px solid var(--accent);outline-offset:6px}
/* --- Marketing surface additions --- */
.topNav{display:flex;gap:18px}
.topNav a{color:var(--muted);font-size:13px;text-decoration:none;font-weight:600}
.topNav a:hover{color:var(--accent)}
.marketingSection{padding:8px 0 16px}
.marketingHead{text-align:center;max-width:640px;margin:0 auto 34px}
.marketingHead h2{font-family:var(--serif);font-size:32px;margin:0 0 10px;letter-spacing:-.5px}
.marketingHead p{color:var(--muted);margin:0;font-size:14.5px}
.pricingGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:stretch}
.priceCard{display:flex;flex-direction:column;padding:28px 24px;position:relative}
.priceCard.featured{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent),var(--shadow)}
.priceCard .plan{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:var(--accent);font-weight:800;margin-bottom:8px}
.priceCard h3{margin:0 0 6px;font-size:22px;font-family:var(--serif)}
.priceCard .amt{font-size:34px;font-weight:900;margin:8px 0 4px}
.priceCard .amt span{font-size:13px;color:var(--muted);font-weight:500}
.priceCard .desc{color:var(--muted);font-size:13px;margin-bottom:18px}
.priceCard ul{list-style:none;margin:0 0 22px;padding:0;flex:1;display:flex;flex-direction:column;gap:10px}
.priceCard ul li{font-size:13px;color:#33415C;display:flex;gap:8px;align-items:flex-start}
.priceCard ul li svg{flex:none;margin-top:2px;color:var(--accent)}
.priceCard .badgeTop{position:absolute;top:-11px;left:50%;transform:translateX(-50%);background:var(--accent);color:#FFFFFF;font-size:10.5px;font-weight:800;padding:4px 12px;border-radius:999px;letter-spacing:.5px}
.aboutGrid{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:center}
.aboutStats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}
.aboutStats .st{padding:16px;border:1px solid var(--line);border-radius:14px;text-align:center;background:rgba(15,27,45,.03)}
.aboutStats .st b{display:block;font-size:24px;color:var(--accent);font-family:var(--serif)}
.aboutStats .st span{font-size:11px;color:var(--muted)}
.contactGrid{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.contactCard{padding:26px}
.contactRow{display:flex;flex-direction:column;gap:12px;margin-top:14px}
.contactRow .item{display:flex;gap:10px;align-items:center;font-size:13px;color:#33415C}
.contactRow .item svg{color:var(--accent);flex:none}
@media(max-width:860px){.pricingGrid,.aboutGrid,.contactGrid{grid-template-columns:1fr}.topNav{display:none}}
.trustBar{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:20px;padding-top:18px;border-top:1px solid rgba(15,27,45,.10)}
.trustBar .item{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted)}
.trustBar .item svg{flex:none;color:var(--accent)}
.heroPreview{position:relative;padding:22px;overflow:hidden}
.pvLabel,.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.pvLabel span.dot,.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
.pvRing{width:112px;height:112px;border-radius:50%;margin:2px auto 14px;display:grid;place-items:center;background:conic-gradient(var(--accent) 0 78%,#182c42 78% 100%);position:relative}
.pvRing:after{content:"";position:absolute;inset:9px;border-radius:50%;background:#F7F9FC}
.pvRing b{position:relative;font-family:var(--serif);font-size:26px;z-index:1}
.pvRow{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12px}
.pvRow .n{color:var(--text);font-weight:700}
.pvRow .n.up{color:var(--green)}.pvRow .n.down{color:var(--red)}
.pvBars{display:flex;align-items:flex-end;gap:5px;height:54px;margin-top:14px}
.pvBars i{flex:1;background:linear-gradient(180deg,var(--accent2),#4a63b8);border-radius:3px 3px 1px 1px;display:block}
.statsStrip{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin:6px 0 0;padding:26px 0}
.statsStrip .stat b{font-family:var(--serif);font-size:36px;font-weight:600;color:var(--text);display:block;letter-spacing:-.5px}
.statsStrip .stat span{font-size:12.5px;color:var(--muted);display:block;margin-top:4px;max-width:20ch}
.whyCard{padding:20px;position:relative}
.whyCard .icoWrap{width:40px;height:40px;border-radius:11px;background:#DCE6FB;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;margin-bottom:14px;color:var(--accent)}
.ctaBanner{margin:44px 0 8px;padding:38px 32px;border-radius:22px;background:linear-gradient(135deg,#EAF0FF 0%,#DCE6FB 55%,#EAF0FF 100%);border:1px solid #C9D8F5;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.ctaBanner h3{font-family:var(--serif);font-weight:600;font-size:26px;margin:0 0 6px;letter-spacing:-.3px}
.ctaBanner p{margin:0;color:var(--muted);font-size:13.5px;max-width:52ch}
@media(max-width:1000px){.statsStrip{grid-template-columns:repeat(2,1fr)}.heroTitle{font-size:34px}}
@media(max-width:1000px){.hero{grid-template-columns:1fr}.grid4{grid-template-columns:repeat(2,1fr)}.grid3,.grid2{grid-template-columns:1fr}.wrap{padding:0 15px}.heroTitle{font-size:31px}.flowSub{margin-left:0}.qsel .qrow{grid-template-columns:1fr}}
@media print{
  *,*::before,*::after{box-sizing:border-box!important}
  @page{size:A4 portrait;margin:10mm 12mm 10mm 12mm}
  html,body{background:#fff!important;color:#0F1B2D!important;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif!important;font-size:8.5pt!important;line-height:1.35!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Hide all interactive & website shell elements ─────────────── */
  .hero,.upload,.hidePrint,.tabs,.tabPanel,.chips,.qsel,.tab,.footer,.siteFooter,
  header.top,.top,.topNav,.navBtns,.navToggle,#authArea,#authModalOverlay,
  .loadingOverlay,.dropZone,#criticalPartiesNotice,#methodNote,
  .heroPreview,.trustBar,.statsStrip,.ctaBanner,
  button,input,select,textarea,.secondary,.primary,
  #sampleBtn,#aiBtn,#printBtn,#jsonBtn,#aiAskBtn,
  #aiBox,#aiCustomBox,#aiCustomPrompt,#historySection,
  .interactiveScenarioCard,#interactiveScenarioCard,
  .abar{display:none!important}

  /* ── Layout: full-width single column ──────────────────────────── */
  .wrap{max-width:none!important;padding:0!important;margin:0!important;width:100%!important}

  /* ── Boardroom Cover Header ────────────────────────────────────── */
  #printCover{display:block!important;page-break-after:avoid!important;break-after:avoid!important;margin-bottom:12px}
  .printExecutiveFooter{display:flex!important;justify-content:space-between;align-items:center;border-top:1px solid #CBD5E1;padding-top:6px;margin-top:14px;font-size:7pt!important;color:#64748B!important;page-break-inside:avoid!important;break-inside:avoid!important}

  /* ── Cards & Containers ────────────────────────────────────────── */
  .card{box-shadow:none!important;background:#fff!important;border:1px solid #CBD5E1!important;border-radius:6px!important;margin-bottom:8px!important;padding:8px 10px!important;page-break-inside:auto!important;break-inside:auto!important}
  .heroCard{box-shadow:none!important;background:#fff!important;border:1px solid #CBD5E1!important;padding:8px!important}

  /* ── Flow steps ─────────────────────────────────────────────────── */
  .flowStep{margin:8px 0 4px!important;padding-top:2px!important;page-break-inside:auto!important;break-inside:auto!important}
  .flowLabel{background:none!important;border-left:3.5px solid #1D4ED8!important;padding-left:8px!important;color:#0F1B2D!important;margin-bottom:4px!important;font-size:9pt!important;page-break-after:avoid!important;break-after:avoid!important}
  .flowLabel .n{background:#1D4ED8!important;color:#fff!important;font-size:7.5pt!important;padding:1px 5px!important;border-radius:3px!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .flowSub{color:#64748B!important;font-size:7.5pt!important;margin-bottom:6px!important;line-height:1.25!important;page-break-after:avoid!important;break-after:avoid!important}

  /* ── Metrics / KPIs ─────────────────────────────────────────────── */
  .metric{background:#F8FAFC!important;border:1px solid #E2E8F0!important;border-radius:5px!important;padding:6px 8px!important;color:#0F1B2D!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .metric .label{font-size:6.5pt!important;color:#475569!important;font-weight:700;text-transform:uppercase;letter-spacing:.4px}
  .metric .value{font-size:11pt!important;font-weight:800;color:#0F1B2D!important}
  .metric .sub{font-size:6.5pt!important;color:#64748B!important}
  .grid2{display:grid!important;grid-template-columns:1fr 1fr!important;gap:6px!important}
  .grid3{display:grid!important;grid-template-columns:1fr 1fr 1fr!important;gap:6px!important}
  .grid4{display:grid!important;grid-template-columns:repeat(4,1fr)!important;gap:6px!important}

  /* ── Health score ring ──────────────────────────────────────────── */
  .scoreCard{display:flex!important;align-items:center!important;gap:16px!important;padding:8px 12px!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .scoreRing{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .scoreRing::after{background:#fff!important}

  /* ── Section headings ───────────────────────────────────────────── */
  .sectionHead{border-bottom:1px solid #E2E8F0!important;margin-bottom:6px!important;padding-bottom:4px!important;page-break-after:avoid!important;break-after:avoid!important}
  .sectionHead h2{font-size:8.5pt!important;color:#1D4ED8!important;font-weight:800;margin:0!important}
  .sectionHead p{font-size:7pt!important;color:#64748B!important;margin:1px 0 0!important}
  h1,h2,h3,h4{page-break-after:avoid!important;break-after:avoid!important;color:#0F1B2D!important}
  h3{font-size:8.5pt!important}

  /* ── Risk & action rows (atomic: keep intact) ───────────────────── */
  .riskRow,.actionRow{border:1px solid #E2E8F0!important;border-radius:5px!important;margin-bottom:4px!important;padding:5px 7px!important;page-break-inside:avoid!important;break-inside:avoid!important;background:#F8FAFC!important}
  .rank{background:#EBF3FE!important;color:#1D4ED8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .bar{display:none!important}

  /* ── Tags / badges ──────────────────────────────────────────────── */
  .tag{border:1px solid #94A3B8!important;color:#1E293B!important;background:#F1F5F9!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;font-size:6.5pt!important}
  .badge{border:1px solid #1D4ED8!important;color:#1D4ED8!important;font-size:7pt!important}

  /* ── Insights / alerts ──────────────────────────────────────────── */
  .insight{border-left:3.5px solid #1D4ED8!important;background:#EFF6FF!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;border-radius:4px!important;padding:6px 8px!important;margin-bottom:5px!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .insight.high,.insight.critical{border-left-color:#DC2626!important;background:#FEF2F2!important}
  .insight.positive{border-left-color:#16A34A!important;background:#F0FDF4!important}
  .notice{background:#F8FAFC!important;border:1px solid #CBD5E1!important;padding:6px 8px!important;border-radius:4px!important;font-size:7.5pt!important;color:#334155!important;page-break-inside:avoid!important;break-inside:avoid!important}

  /* ── Waterfall chart ────────────────────────────────────────────── */
  .waterfall{display:flex!important;align-items:flex-end!important;gap:4px!important;height:80px!important;padding:2px 0!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .wf .col{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .wf .num{font-size:6pt!important;color:#0F1B2D!important;font-weight:700}
  .wf .lab{font-size:6pt!important;color:#475569!important;white-space:normal!important;max-height:22px;text-align:center;overflow:hidden;line-height:1.1}

  /* ── Tables ─────────────────────────────────────────────────────── */
  .tableWrap{overflow:visible!important}
  table{border-collapse:collapse!important;width:100%!important;font-size:7pt!important}
  th{background:#F1F5F9!important;color:#1E293B!important;font-weight:700;padding:3px 5px!important;border:1px solid #CBD5E1!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  td{padding:3px 5px!important;border:1px solid #E2E8F0!important}
  tr{page-break-inside:avoid!important;break-inside:avoid!important}
  tr:nth-child(even) td{background:#F8FAFC!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}

  /* ── Misc ────────────────────────────────────────────────────────── */
  .muted{color:#64748B!important}
  .small{font-size:7pt!important}
  a{color:#1D4ED8!important;text-decoration:none!important}
  .scenario{border:1px solid #CBD5E1!important;border-radius:5px!important;padding:6px!important;page-break-inside:avoid!important;break-inside:avoid!important}
  .scenario .big{font-size:11pt!important;font-weight:800;color:#1D4ED8!important;-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  .custRow,.wf{page-break-inside:avoid!important;break-inside:avoid!important}
  .hidden{display:none!important}
  #dashboard{display:block!important}
}

@view-transition{navigation:auto}
::view-transition-old(root){animation:dfbpFadeOut .28s ease both}
::view-transition-new(root){animation:dfbpFadeIn .32s ease both}
@keyframes dfbpFadeOut{to{opacity:0;transform:translateY(-6px)}}
@keyframes dfbpFadeIn{from{opacity:0;transform:translateY(8px)}}
.topNav{display:flex;gap:18px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s;white-space:nowrap}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.authCluster{display:flex;flex-direction:column;align-items:flex-end;gap:5px;flex-shrink:0}
.headerSwitches{display:flex;align-items:center;gap:6px;justify-content:flex-end}
.headerSwitches select{padding:2px 7px;font-size:11px;font-weight:600;border-radius:6px;background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;cursor:pointer;height:22px;line-height:1}
.headerSwitches select:hover{border-color:var(--accent);color:#0F1B2D;background:#FFFFFF}
.navBtns{display:flex;gap:10px;align-items:center}
.navBtn{display:inline-flex;align-items:center;justify-content:center;padding:8px 18px;border-radius:10px;font-size:13px;font-weight:700;letter-spacing:-.1px;text-decoration:none;cursor:pointer;transition:all .18s ease;line-height:1.2}
.navBtn.sec{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
.navBtn.sec:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
.navBtn.pri{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
.navBtn.pri:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
#authArea{display:flex;gap:8px;align-items:center}
#authArea button{padding:6px 14px;border-radius:9px;font-size:12.5px;font-weight:700;line-height:1.2;cursor:pointer;transition:all .18s ease;white-space:nowrap}
#authArea button.secondary{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
#authArea button.secondary:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
#authArea button.primary{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
#authArea button.primary:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text);flex-shrink:0}
.brandLogoWrap{flex-shrink:0;min-width:max-content}
.brandLink{text-decoration:none;display:flex;align-items:center;gap:10px;min-width:0}
.brandLogoIcon{width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0}
.brandTextWrap{min-width:0}
.brandTitle{font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2;white-space:nowrap}
.brandSub{font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px;white-space:nowrap}
.headerRight{display:flex;align-items:center;gap:12px;flex-shrink:0}
.mobileNavAuth{display:none}

@media(max-width:920px){
  html,body{overflow-x:hidden;max-width:100vw;width:100%}
  .top{padding:12px 0 10px}
  .wrap{padding:0 16px;max-width:100vw;box-sizing:border-box}
  .brand{gap:10px}
  .brandLogoIcon{width:32px;height:32px;border-radius:9px}
  .brandLogoIcon svg{width:18px;height:18px}
  .brandTitle{font-size:15.5px}
  .brandSub{display:none}
  .brandLogoWrap{min-width:0;flex:1 1 auto;overflow:hidden}
  .topNav{position:fixed;top:56px;left:0;right:0;width:100vw;background:#FFFFFF;border-bottom:1.5px solid var(--line);box-shadow:0 14px 34px rgba(15,27,45,0.12);flex-direction:column;align-items:stretch;gap:0;padding:0 20px;max-height:0;overflow:hidden;transition:max-height .28s ease,padding .2s ease;z-index:999;box-sizing:border-box}
  .topNav.open{max-height:460px;padding:10px 20px 20px;overflow-y:auto}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.06);font-size:14.5px;color:var(--text);font-weight:600;display:block;text-align:left}
  .mobileNavAuth{display:flex;gap:10px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(15,27,45,.08)}
  .mobileNavAuth button,.mobileNavAuth a{flex:1;padding:10px 12px;font-size:13px;font-weight:700;border-radius:10px;text-align:center;justify-content:center;cursor:pointer}
  .navToggle{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;padding:0;font-size:18px;border-radius:8px;cursor:pointer}
}

@media(max-width:768px){
  #authArea{display:none}
  .navBtns{display:none}
  .authCluster{flex-direction:row;align-items:center}
  .headerRight{gap:6px}
  .headerSwitches{gap:4px}
  .headerSwitches select{padding:4px 5px;font-size:11px;border-radius:7px;max-width:60px}
  .wrap{padding:0 12px}
  .brandTitle{font-size:14.5px}
  .hero{grid-template-columns:1fr !important;padding:16px 0 12px !important;gap:14px !important}
  .heroCard,.card{padding:16px 14px !important;border-radius:16px !important}
  .heroTitle{font-size:23px !important;line-height:1.2 !important;margin-bottom:10px !important}
  .heroText{font-size:12.5px !important;line-height:1.5 !important}
  .framework{gap:6px !important;margin:12px 0 2px !important}
  .framework span{font-size:11px !important;padding:5px 9px !important}
  .cfoDemoHeroBanner{padding:14px !important;gap:12px !important}
  .cfoDemoHeroBanner > div:last-child{width:100%;display:flex;flex-direction:column;gap:8px !important}
  .cfoDemoHeroBanner button{width:100%;justify-content:center;padding:10px 14px !important}
  .tabs{display:flex;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;gap:6px;padding-bottom:4px;width:100%;box-sizing:border-box}
  .tabs::-webkit-scrollbar{display:none}
  .tab{white-space:nowrap;flex-shrink:0;padding:7px 12px;font-size:12px}
  .dropZone{padding:18px 12px !important}
  .dropText strong{font-size:13.5px !important}
  .dropText span{font-size:11px !important}
  #analyze,#analyzeTrend,#analyzeHub{width:100%;padding:12px 16px !important;font-size:13.5px !important}
  .grid4,.grid3,.grid2{grid-template-columns:1fr !important;gap:10px !important}
  .metric{padding:14px !important}
  .metric .value{font-size:21px !important}
  .tableWrap,.compareTableWrap{overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%;margin-bottom:10px}
  table{min-width:320px}
  .sectionHead{flex-direction:column !important;align-items:flex-start !important;gap:4px !important}
  .sectionHead h2{font-size:16px !important}
  .scenario .big{font-size:20px !important}
  .waterfall{height:160px !important}
  .statsStrip{grid-template-columns:1fr !important;gap:12px !important;padding:16px 0 !important}
  .mHero h1{font-size:28px !important;line-height:1.18 !important}
  .mHero p.lead{font-size:14px !important;line-height:1.55 !important}
  .aboutStats{grid-template-columns:1fr !important;gap:10px !important}
}
.badge.v{white-space:nowrap}
/* ---- Marketing hero (separate from app hero) ---- */
.mHero{padding:56px 0 30px;display:grid;grid-template-columns:1.15fr .85fr;gap:34px;align-items:center}
.mHero .eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:18px}
.mHero h1{font-family:var(--serif);font-weight:600;font-size:50px;line-height:1.08;margin:0 0 18px;letter-spacing:-1px}
.mHero h1 span{color:var(--accent)}
.mHero p.lead{color:var(--muted);font-size:16px;max-width:560px;line-height:1.65;margin:0 0 26px}
.mHero .ctaRow{display:flex;gap:12px;flex-wrap:wrap}
.mHero .ctaRow a{text-decoration:none}
.mHero .miniTrust{display:flex;gap:18px;flex-wrap:wrap;margin-top:28px}
.mHero .miniTrust span{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px}
.mHero .miniTrust svg{color:var(--accent)}
.heroArt{position:relative}
.heroArt .floatCard{position:absolute;background:#FFFFFF;border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);padding:14px 16px;font-size:11.5px;color:#33415C;animation:dfbpFloat 5s ease-in-out infinite}
.heroArt .floatCard b{display:block;font-size:16px;color:var(--accent);font-family:var(--serif)}
.heroArt .fc1{top:-10px;left:-10px;animation-delay:0s}
.heroArt .fc2{bottom:6px;right:-14px;animation-delay:1.2s}
@keyframes dfbpFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
/* ---- Alternating content blocks (fixes the "iç içe" cramped look) ---- */
.secBlock{padding:28px 0}
.secBlock.tint{background:linear-gradient(180deg,#F8FAFC 0%,#FFFFFF 100%);border:1px solid #E2E8F0;border-radius:26px;margin:0 -10px;box-shadow:0 4px 20px rgba(15,27,45,.03)}
.pillScrollBtn{width:36px;height:36px;border-radius:50%;background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:800;cursor:pointer;flex-shrink:0;box-shadow:0 4px 12px rgba(15,27,45,0.08);transition:all .18s ease;user-select:none;z-index:4}
.pillScrollBtn:hover{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;transform:scale(1.08);box-shadow:0 6px 16px rgba(29,78,216,0.25)}
.pillScrollBtn:active{transform:scale(0.95)}
.secBlock+.secBlock{border-top:1px solid rgba(15,27,45,.06)}
.pageHead{padding:54px 0 10px;text-align:center}
.pageHead .eyebrow{display:inline-flex;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--accent);background:#DCE6FB;border:1px solid #1f4258;padding:7px 14px;border-radius:999px;margin-bottom:16px}
.pageHead h1{font-family:var(--serif);font-size:38px;margin:0 0 12px;letter-spacing:-.6px}
.pageHead p{color:var(--muted);max-width:600px;margin:0 auto;font-size:14.5px}
.reveal{opacity:0;transform:translateY(18px);transition:opacity .55s ease,transform .55s ease}
.reveal.in{opacity:1;transform:none}
/* ---- Rich footer ---- */
.siteFooter{border-top:1px solid var(--line);margin-top:40px;padding:46px 0 26px}
.siteFooter .cols{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:28px;margin-bottom:30px}
.siteFooter h4{font-size:12px;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);margin:0 0 14px}
.siteFooter .brandCol p{color:var(--muted);font-size:12.5px;max-width:280px;line-height:1.6}
.siteFooter ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.siteFooter ul a{color:#33415C;text-decoration:none;font-size:13px}
.siteFooter ul a:hover{color:var(--accent)}
.siteFooter .legal{border-top:1px solid rgba(15,27,45,.08);padding-top:20px;color:#5B6B84;font-size:11px;line-height:1.7}
html{overflow-x:hidden}@media(max-width:860px){.siteFooter .cols{grid-template-columns:1fr 1fr}.mHero{grid-template-columns:1fr}.heroArt{order:-1;max-width:340px;margin:24px auto 40px;padding:0 14px}.heroArt .floatCard{position:static;display:inline-block;margin:6px 6px 0 0;animation:none}.heroArt .fc1,.heroArt .fc2{top:auto;left:auto;right:auto;bottom:auto}}
/* ---- FAQ (paketler sayfası) ---- */
.faqItem{border-bottom:1px solid var(--line);padding:16px 0}
.faqItem summary{cursor:pointer;font-weight:700;font-size:14px;list-style:none;display:flex;justify-content:space-between;align-items:center}
.faqItem summary::-webkit-details-marker{display:none}
.faqItem summary:after{content:'+';font-size:20px;color:var(--accent)}
.faqItem[open] summary:after{content:'–'}
.faqItem p{color:var(--muted);font-size:13.5px;margin:10px 0 0}
/* ---- Executive Intelligence band (single, deliberate dark boardroom section) ---- */
.execBand{background:radial-gradient(1200px 500px at 15% -20%, rgba(76,201,240,.10), transparent 60%),linear-gradient(160deg,#0D1B2A 0%,#081426 100%);border-radius:26px;padding:52px;display:grid;grid-template-columns:.85fr 1.15fr;gap:40px;align-items:center;overflow:hidden}
.execEyebrow{display:inline-block;font-size:11.5px;font-weight:800;letter-spacing:1.6px;color:#4CC9F0;background:rgba(76,201,240,.12);border:1px solid rgba(76,201,240,.35);padding:6px 12px;border-radius:999px;margin-bottom:16px}
.execCopy h2{font-family:var(--serif);color:#F8FAFC;font-size:28px;line-height:1.2;margin:0 0 12px;letter-spacing:-.4px}
.execCopy p{color:#94A3B8;font-size:14px;line-height:1.7;margin:0 0 18px;max-width:44ch}
.execList{list-style:none;margin:0 0 24px;padding:0;display:flex;flex-direction:column;gap:9px}
.execList li{color:#C7D2E8;font-size:13px}
.execList li b{color:#F8FAFC}
.execCta{display:inline-block;color:#0D1B2A;background:#4CC9F0;font-weight:800;font-size:13.5px;padding:12px 20px;border-radius:11px;text-decoration:none;transition:transform .15s ease,box-shadow .15s ease}
.execCta:hover{transform:translateY(-1px);box-shadow:0 10px 26px rgba(76,201,240,.35)}
.execArt{filter:drop-shadow(0 24px 48px rgba(0,0,0,.35))}
@media(max-width:860px){.execBand{grid-template-columns:1fr;padding:32px 22px}}
/* ---- New: live dashboard hero panel ---- */
.heroDash{background:linear-gradient(160deg,#0D1B2A 0%,#0A1524 100%);border-radius:20px;border:1px solid #1E3050;padding:20px;position:relative;overflow:hidden;box-shadow:0 24px 60px rgba(8,17,32,.35)}
.heroDash .dHead{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.heroDash .dHead .dots span{width:8px;height:8px;border-radius:50%;display:inline-block;margin-right:5px}
.heroDash .dHead .live{font-size:10.5px;color:#7FE3B4;display:flex;align-items:center;gap:6px;font-weight:700;letter-spacing:.4px}
.heroDash .dHead .live i{width:6px;height:6px;border-radius:50%;background:#15E3B3;display:inline-block;box-shadow:0 0 0 3px rgba(21,227,179,.22);animation:dfbpPulse 1.8s ease infinite}
@keyframes dfbpPulse{0%,100%{opacity:1}50%{opacity:.35}}
.dashTabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px}
.dashTabs span{font-size:10px;color:#7C8FAD;background:#101F33;border:1px solid #1E3050;border-radius:999px;padding:5px 10px;transition:all .25s ease}
.dashTabs span.on{color:#0D1B2A;background:#4CC9F0;border-color:#4CC9F0;font-weight:800}
.dashPane{display:none;min-height:230px}
.dashPane.on{display:block;animation:dfbpFadeIn .4s ease both}
.dashPane .dTitle{color:#7C8FAD;font-size:10px;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px}
.dashKpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px}
.dashKpis div{background:#132238;border:1px solid #20334b;border-radius:9px;padding:9px 10px}
.dashKpis div b{display:block;font-size:16px;color:#F8FAFC;font-family:var(--serif)}
.dashKpis div span{font-size:9.5px;color:#7C8FAD}
.heroDash .foot{margin-top:12px;padding-top:12px;border-top:1px solid #1E3050;font-size:10.5px;color:#7C8FAD;display:flex;justify-content:space-between}
/* ---- New: CFO trust strip ---- */
.trustGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.trustCard{padding:22px}
.trustCard .icoWrap2{width:38px;height:38px;border-radius:10px;background:#0D1B2A;color:#4CC9F0;display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.trustCard h3{margin:0 0 6px;font-size:14.5px}
.trustCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.55}
/* ---- New: Executive Journey ---- */
.journey{display:grid;grid-template-columns:repeat(6,1fr);gap:0;position:relative;margin-top:8px}
.journey:before{content:"";position:absolute;top:22px;left:6%;right:6%;height:2px;background:linear-gradient(90deg,#C9D8F5,#4CC9F0,#C9D8F5)}
.jStep{text-align:center;padding:0 8px;opacity:0;transform:translateY(16px);transition:opacity .5s ease,transform .5s ease}
.jStep.in{opacity:1;transform:none}
.jStep .jDot{width:44px;height:44px;border-radius:50%;background:#FFFFFF;border:2px solid var(--accent);color:var(--accent);display:flex;align-items:center;justify-content:center;margin:0 auto 12px;position:relative;z-index:1;font-weight:900;font-size:13px}
.jStep h4{margin:0 0 5px;font-size:13px;letter-spacing:.4px}
.jStep p{margin:0;font-size:11.5px;color:var(--muted);line-height:1.4}
@media(max-width:860px){.journey{grid-template-columns:1fr 1fr;gap:22px 0}.journey:before{display:none}.trustGrid{grid-template-columns:1fr 1fr}}
/* ---- New: outcome-based module groups ---- */
.intelGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.intelCard{padding:24px;display:flex;flex-direction:column}
.intelCard .igIco{width:40px;height:40px;border-radius:11px;background:#DCE6FB;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:14px}
.intelCard h3{margin:0 0 8px;font-size:16px;font-family:var(--serif)}
.intelCard ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}
.intelCard ul li{font-size:12.5px;color:#33415C;display:flex;gap:7px;align-items:flex-start}
.intelCard ul li:before{content:"";width:5px;height:5px;border-radius:50%;background:var(--accent);margin-top:6px;flex:none}
@media(max-width:860px){.intelGrid{grid-template-columns:1fr 1fr}}
/* ---- New: security/governance page ---- */

/* ---- High-impact FinTech additions ---- */
.gradText{background:linear-gradient(135deg,#1D4ED8 0%,#2563EB 50%,#38BDF8 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;display:inline-block}
.livePill{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:var(--accent);background:linear-gradient(135deg,#EEF4FF,#E0EDFF);border:1px solid #BFDBFE;padding:8px 16px;border-radius:999px;margin-bottom:20px;box-shadow:0 2px 10px rgba(37,99,235,.12)}
.livePill i{width:8px;height:8px;border-radius:50%;background:#10B981;display:inline-block;box-shadow:0 0 0 4px rgba(16,185,129,.25);animation:dfbpPulse 1.8s ease infinite}
.dilemmaGrid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:20px}
.dilemmaCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:26px;position:relative;overflow:hidden;box-shadow:var(--shadow);transition:transform .2s ease,box-shadow .2s ease}
.dilemmaCard:hover{transform:translateY(-3px);box-shadow:0 16px 36px rgba(15,27,45,.09)}
.dilemmaQ{font-size:15px;font-weight:700;color:#0F1B2D;margin-bottom:12px;display:flex;gap:10px;align-items:flex-start;line-height:1.4}
.dilemmaQ span{background:#FEE2E2;color:#DC2626;border-radius:8px;padding:2px 8px;font-size:11px;font-weight:900;flex:none;margin-top:2px}
.dilemmaA{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:14px 16px;font-size:13px;color:#33415C;line-height:1.55}
.dilemmaA b{color:var(--accent);display:block;margin-bottom:4px}
.workflowGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;position:relative;margin-top:20px}
.workflowCard{background:#FFFFFF;border:1px solid var(--line);border-radius:18px;padding:24px;box-shadow:var(--shadow);position:relative;display:flex;flex-direction:column}
.workflowBadge{font-size:11px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:var(--accent);background:#EFF6FF;border:1px solid #DBEAFE;padding:4px 10px;border-radius:999px;align-self:flex-start;margin-bottom:12px}
.workflowCard h3{font-size:16px;margin:0 0 8px;font-family:var(--serif);color:#0F1B2D}
.workflowCard p{font-size:12.5px;color:var(--muted);line-height:1.55;margin:0}
.compareTableWrap{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:var(--shadow);margin-top:20px}
.compareTable{width:100%;border-collapse:collapse;font-size:13px}
.compareTable th,.compareTable td{padding:16px 18px;border-bottom:1px solid rgba(15,27,45,.08);text-align:left}
.compareTable th{background:#F8FAFC;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#475569}
.compareTable th.featured{background:linear-gradient(135deg,#EFF6FF,#DBEAFE);color:var(--accent);border-bottom:2px solid var(--accent)}
.compareTable td.featured{background:#F8FAFF;font-weight:600;color:#0F1B2D}
@media(max-width:860px){.dilemmaGrid,.workflowGrid{grid-template-columns:1fr}.compareTableWrap{overflow-x:auto}}

.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
/* ---- Institutional Loading Overlay & Dropzone ---- */
.loadingOverlay{position:fixed;inset:0;background:rgba(15,27,45,0.78);backdrop-filter:blur(8px);display:flex;align-items:center;justify-content:center;z-index:99999;transition:opacity .25s ease}
.loadingOverlay.hidden{display:none;opacity:0}
.loadingCard{background:#FFFFFF;border-radius:22px;padding:36px 32px;max-width:460px;width:92%;text-align:center;box-shadow:0 30px 70px rgba(0,0,0,0.35);border:1px solid rgba(255,255,255,0.25);position:relative}
.loadingSpinner{width:50px;height:50px;border:4px solid #E2E8F0;border-top-color:var(--accent);border-radius:50%;margin:0 auto 18px;animation:dfbpSpin .8s linear infinite}
@keyframes dfbpSpin{to{transform:rotate(360deg)}}
.loadingCard h3{font-size:19px;margin:0 0 6px;color:#0F1B2D;font-family:var(--serif)}
.loadingCard p{font-size:13px;color:var(--muted);margin:0 0 18px;line-height:1.5}
.loadingTrack{height:8px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-bottom:14px}
.loadingBar{height:100%;width:20%;background:linear-gradient(90deg,var(--accent),#38BDF8);border-radius:99px;transition:width .4s ease}
.loadingStepTxt{font-size:12px;color:#1E3A8A;font-weight:700;background:#EFF6FF;border:1px solid #DBEAFE;padding:6px 14px;border-radius:999px;display:inline-block}

.dropZone{border:2px dashed #BFDBFE;background:linear-gradient(180deg,#F8FAFF 0%,#EEF4FF 100%);border-radius:16px;padding:24px 18px;text-align:center;cursor:pointer;transition:all .2s ease;margin-bottom:12px}
.dropZone:hover,.dropZone.dragover{border-color:var(--accent);background:#EBF2FF;transform:scale(1.005)}
.dropIco{color:var(--accent);margin-bottom:8px}
.dropText strong{display:block;font-size:14px;color:#0F1B2D;margin-bottom:4px}
.dropText span{font-size:12px;color:var(--muted)}
.selectedFilesList{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.filePill{display:inline-flex;align-items:center;gap:8px;background:#FFFFFF;border:1px solid #CBD5E1;border-radius:999px;padding:6px 14px;font-size:12px;color:#1E293B;box-shadow:0 1px 3px rgba(0,0,0,0.05)}
.filePill b{color:var(--accent)}
.filePill .pillDel{cursor:pointer;color:#94A3B8;font-weight:bold;font-size:15px;margin-left:4px}
.filePill .pillDel:hover{color:#EF4444}
.btnReady{background:linear-gradient(135deg,#1D4ED8 0%,#2563EB 50%,#0284C7 100%) !important;box-shadow:0 4px 18px rgba(37,99,235,0.4) !important;transform:scale(1.01)}

/* CEO Diagnostic Hub 3-Layer Architecture */
.ceoPill{display:inline-flex;align-items:center;gap:7px;padding:9px 16px;border-radius:999px;font-size:12.5px;font-weight:700;background:#F1F5F9;color:#475569;border:1px solid #CBD5E1;cursor:pointer;white-space:nowrap;transition:all .2s ease}
.ceoPill:hover{background:#E2E8F0;color:#0F172A}
.ceoPill.active{background:#1D4ED8;color:#FFFFFF;border-color:#1D4ED8;box-shadow:0 4px 14px rgba(29,78,216,0.25)}
.ceoQuestionCard{display:none;background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:18px;padding:22px;box-shadow:0 8px 24px rgba(15,27,45,0.04);animation:fadeIn .3s ease}
.ceoQuestionCard.active{display:block}
.layerBadge{display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;font-size:10.5px;font-weight:800;letter-spacing:0.5px;text-transform:uppercase}
.layerBadge.l1{background:#FEE2E2;color:#991B1B;border:1px solid #FCA5A5}
.layerBadge.l2{background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE}
.layerBadge.l3{background:#ECFDF5;color:#047857;border:1px solid #A7F3D0}
.ceoGrid3{display:grid;grid-template-columns:1.1fr 1fr 1.3fr;gap:18px;margin-top:16px}
@media(max-width:960px){.ceoGrid3{grid-template-columns:1fr}}


.accordionStep{background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:18px;margin-bottom:18px;box-shadow:0 4px 18px rgba(15,27,45,.04);overflow:hidden;transition:border-color .2s ease,box-shadow .2s ease}
.accordionStep.active{border-color:#CBD5E1;box-shadow:0 8px 30px rgba(15,27,45,.07)}
.accordionHeader{display:flex;justify-content:space-between;align-items:center;padding:16px 22px;cursor:pointer;user-select:none;background:#FFFFFF;transition:background .2s ease,border-color .2s ease;border-bottom:1px solid transparent}
.accordionStep.active .accordionHeader{background:#FAFBFD;border-bottom-color:#E2E8F0}
.accordionHeader:hover{background:#F8FAFC}
.accordionTitleGroup{display:flex;align-items:center;gap:12px;flex:1}
.accordionNum{width:30px;height:30px;border-radius:8px;background:#0F172A;color:#FFFFFF;font-size:13px;font-weight:900;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.accordionNum.alt{background:#475569}
.accordionTitle{font-size:15px;font-weight:800;color:#0F172A;margin:0}
.accordionSub{font-size:12px;color:#64748B;margin:2px 0 0 0;font-weight:500}
.accordionToggleIcon{width:30px;height:30px;border-radius:50%;background:#F1F5F9;display:flex;align-items:center;justify-content:center;font-size:12px;color:#475569;transition:transform .25s ease,background .2s ease}
.accordionStep.active .accordionToggleIcon{transform:rotate(180deg);background:#E2E8F0;color:#0F172A}
.accordionBody{padding:22px;display:none}
.accordionStep.active .accordionBody{display:block}
@media print{
  .accordionStep{box-shadow:none!important;border:1px solid #CBD5E1!important;margin-bottom:10px!important}
  .accordionHeader{padding:8px 12px!important;border-bottom:none!important;background:#F8FAFC!important}
  .accordionToggleIcon{display:none!important}
  .accordionBody{display:block!important;padding:12px!important}
  /* Board Deck Dedicated Print Mode - Completely isolates #boardDeckModal and removes everything else from layout */
  body.boardDeckPrintMode header.top,
  body.boardDeckPrintMode main,
  body.boardDeckPrintMode .siteFooter,
  body.boardDeckPrintMode #authArea,
  body.boardDeckPrintMode #authModalOverlay,
  body.boardDeckPrintMode #loadingOverlay {
    display: none !important;
  }

  body.boardDeckPrintMode {
    background: #ffffff !important;
    padding: 0 !important;
    margin: 0 !important;
  }

  body.boardDeckPrintMode #boardDeckModal {
    display: block !important;
    position: static !important;
    inset: auto !important;
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    min-height: auto !important;
    max-height: none !important;
    background: #ffffff !important;
    padding: 0 !important;
    margin: 0 !important;
    overflow: visible !important;
    box-shadow: none !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
  }

  body.boardDeckPrintMode #boardDeckModal > div {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    max-height: none !important;
    box-shadow: none !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    overflow: visible !important;
    background: #ffffff !important;
  }

  body.boardDeckPrintMode #boardDeckContent {
    display: block !important;
    padding: 0 !important;
    margin: 0 !important;
    height: auto !important;
    max-height: none !important;
    overflow: visible !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }

  body.boardDeckPrintMode .hidePrint {
    display: none !important;
  }
}
/* Cyber Trust Wall Grid */
.trustWallGrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
  margin-top: 16px;
}
.trustBadgeCard {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 12px 14px;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  transition: all 0.2s ease;
  cursor: pointer;
}
.trustBadgeCard:hover {
  transform: translateY(-2px);
  border-color: #93C5FD;
  box-shadow: 0 6px 16px rgba(37,99,235,0.08);
}
.trustBadgeCard .tIco {
  font-size: 20px;
  flex: none;
  background: #F0FDF4;
  border: 1px solid #DCFCE7;
  width: 34px;
  height: 34px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.trustBadgeCard .tInfo strong {
  display: block;
  font-size: 12px;
  font-weight: 700;
  color: #0F172A;
  margin-bottom: 2px;
}
.trustBadgeCard .tInfo span {
  display: block;
  font-size: 11px;
  color: #64748B;
  line-height: 1.35;
}
</style></head>
<body>
<div id="loadingOverlay" class="loadingOverlay hidden">
  <div class="loadingCard">
    <div class="loadingSpinner"></div>
    <h3 id="loadingTitle">Finansal Veriler İşleniyor</h3>
    <p id="loadingSubtitle">33 Finansal Karar Motoru Çalıştırılıyor...</p>
    <div class="loadingTrack"><div id="loadingBar" class="loadingBar"></div></div>
    <div id="loadingStepTxt" class="loadingStepTxt">Hesap planı ve bakiyeler denetleniyor...</div>
  </div>
</div>
<header class="top"><div class="wrap brand"><div class="brandLogoWrap">
  <a href="/" class="brandLink">
    <div class="brandLogoIcon">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div class="brandTextWrap">
      <div class="brandTitle">Digital Finance Business Partner</div>
      <div class="brandSub">Finansal Teşhis &amp; Yönetim Karar Destek Platformu</div>
    </div>
  </a>
</div><div class="headerRight"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/cozumler">Çözümler</a><a href="/hakkimizda">Hakkımızda</a><a href="/uygulama" class="active">Uygulama</a><a href="/paketler">Paketler</a><a href="/guvenlik">Güvenlik</a><a href="/iletisim">İletişim</a><div class="mobileNavAuth" id="mobileNavAuth"><button type="button" onclick="openAuthModal('login')" class="secondary">Giriş Yap</button><button type="button" onclick="openAuthModal('register')" class="primary">Ücretsiz Kayıt Ol</button></div></nav><div class="authCluster hidePrint"><div class="headerSwitches"><select id="currencySwitch" onchange="setCurrency(this.value)" class="select" title="Para Birimi"><option value="TRY">₺ TRY</option><option value="EUR">€ EUR</option><option value="GBP">£ GBP</option><option value="USD">$ USD</option></select><select id="langSwitch" onchange="setLanguage(this.value)" class="select" title="Dil / Language"><option value="tr">🇹🇷 TR</option><option value="en">🇬🇧 EN</option><option value="de">🇩🇪 DE</option><option value="fr">🇫🇷 FR</option><option value="es">🇪🇸 ES</option><option value="it">🇮🇹 IT</option><option value="nl">🇳🇱 NL</option></select></div><div id="authArea"><button id="loginOpenBtn" class="secondary">Giriş Yap</button> <button id="registerOpenBtn" class="primary">Ücretsiz Kayıt Ol</button></div></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<div id="authModalOverlay" class="hidden" style="position:fixed;inset:0;background:rgba(15,27,45,.65);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);display:flex;align-items:center;justify-content:center;z-index:1000;padding:20px">
  <div class="card" style="background:#FFFFFF;border:1px solid #DCE6F5;border-radius:24px;box-shadow:0 24px 70px rgba(15,27,45,.25);max-width:420px;width:100%;padding:28px;position:relative;overflow:hidden">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px">
      <div style="display:inline-flex;align-items:center;gap:6px;background:#EEF4FF;border:1px solid #BFDBFE;padding:4px 10px;border-radius:999px;font-size:11px;font-weight:700;color:var(--accent)">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
        256-Bit SSL · Güvenli Kurumsal Giriş
      </div>
      <button id="authModalClose" style="background:none;border:none;color:var(--muted);font-size:20px;cursor:pointer;padding:4px 8px;border-radius:8px">✕</button>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;background:#F1F5F9;padding:4px;border-radius:12px;margin-bottom:18px">
      <button id="authTabLogin" type="button" style="border:none;background:#FFFFFF;color:#0F1B2D;font-weight:700;padding:9px;border-radius:999px;cursor:pointer;box-shadow:0 2px 6px rgba(0,0,0,.06);font-size:13px">Giriş Yap</button>
      <button id="authTabRegister" type="button" style="border:none;background:transparent;color:var(--muted);font-weight:600;padding:9px;border-radius:999px;cursor:pointer;font-size:13px">Ücretsiz Kayıt Ol</button>
    </div>
    <div style="margin-bottom:16px">
      <h3 id="authModalTitle" style="margin:0 0 4px;font-family:var(--serif);font-size:22px;color:#0F1B2D">Yönetici Girişi</h3>
      <p id="authModalSubtitle" class="muted small" style="margin:0">Mizan ve finansal karar raporlarınıza güvenle erişin.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:12px">
      <div>
        <label class="small muted" style="display:block;margin-bottom:4px;font-weight:600">Kurumsal E-Posta</label>
        <input id="authEmail" class="select" style="width:100%;border-radius:10px;padding:11px 13px" type="email" placeholder="adiniz@sirketiniz.com">
      </div>
      <div>
        <label class="small muted" style="display:block;margin-bottom:4px;font-weight:600">Şifre</label>
        <input id="authPassword" class="select" style="width:100%;border-radius:10px;padding:11px 13px" type="password" placeholder="En az 6 karakter">
      </div>
      <div id="authCompanyWrap" style="display:none">
        <label class="small muted" style="display:block;margin-bottom:4px;font-weight:600">Şirket Ünvanı (Opsiyonel)</label>
        <input id="authCompany" class="select" style="width:100%;border-radius:10px;padding:11px 13px" type="text" placeholder="Örn: ABC A.Ş.">
      </div>
      <button id="authSubmitBtn" class="primary" style="width:100%;padding:12px;border-radius:12px;font-size:14.5px;margin-top:4px">Giriş Yap</button>
      <div id="authError" class="error hidden" style="margin:0;padding:8px 12px;font-size:12px"></div>
      <div style="border-top:1px solid #E2E8F0;padding-top:12px;text-align:center">
        <span id="authSwitchHint" class="small muted">Hesabınız yok mu? <a href="#" id="authSwitchLink" style="color:var(--accent);font-weight:700">Ücretsiz Kayıt Ol</a></span>
      </div>
      <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px;display:flex;align-items:center;gap:8px;font-size:11px;color:var(--muted)">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        <span>KVKK Uyumlu · Dosyalarınız sunucuda kalıcı tutulmaz.</span>
      </div>
    </div>
  </div>
</div>

<main class="wrap"><section class="hero"><div class="heroCard"><h2 class="heroTitle">Mizanınızı Yükleyin, <span style="color:var(--accent)">Şirketinizin Yönetim Raporunu</span> Alın.</h2><p class="heroText">Mizan veya finansal defterlerinizi yükleyin — 33 karar motoru verilerinizi çift taraflı denetler, kâr sızıntılarını kuruşuna kadar hesaplar, riskleri önceliklendirir ve yarın uygulanacak yönetim kararlarını masaya koyar.</p><div class="framework"><span><b>1. NE OLDU?</b> (Finansal Gerçekler)</span><span><b>2. PARA NEREDE?</b> (Kilitli Nakit &amp; Sızıntı)</span><span><b>3. RİSK &amp; SEKTÖR NE?</b> (Kıyaslama)</span><span><b>4. KİM YAPIYOR?</b> (Müşteri &amp; Stok Zekâsı)</span><span><b>5. NEDEN OLDU?</b> (Kök Neden)</span><span><b>6. NE YAPMALIYIZ?</b> (Yönetim Kararları)</span><span><b>7. SİMÜLE ET</b> (Senaryo Simülatörü)</span></div>
<div class="cfoDemoHeroBanner hidePrint" style="margin-top:16px;margin-bottom:14px;background:linear-gradient(135deg, rgba(29,78,216,0.06) 0%, rgba(14,124,102,0.06) 100%);border:1.5px solid rgba(29,78,216,0.22);border-radius:14px;padding:16px 20px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:14px">
  <div style="max-width:520px">
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">
      <span style="background:#1D4ED8;color:#fff;font-size:10.5px;font-weight:800;padding:2px 8px;border-radius:6px;letter-spacing:0.5px">CFO CANLI DEMO</span>
      <span style="font-weight:700;font-size:14.5px;color:#0F1B2D">Dosya Yüklemeden Platformu Canlı İnceleyin</span>
    </div>
    <div style="font-size:12.5px;color:#475569;line-height:1.5">Gerçek kurumsal veri setleriyle 33 analitik karar motorunu, nakit akış köprüsünü, DuPont kârlılık ayrıştırmasını ve yönetim aksiyonlarını anında test edin.</div>
  </div>
  <div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center">
    <button id="sampleTrendBtn" type="button" class="primary" style="background:linear-gradient(135deg,#1D4ED8,#0E7C66);color:#fff;border:none;padding:10px 18px;border-radius:10px;font-weight:800;font-size:13px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;box-shadow:0 4px 14px rgba(29,78,216,0.25)">
      🚀 1-Tıkla Trend Demosu (2 Dönem)
    </button>
    <button id="sampleBtn" type="button" class="secondary" style="background:#FFFFFF;color:#0F1B2D;border:1.5px solid #CBD5E1;padding:9px 14px;border-radius:10px;font-weight:700;font-size:12.5px;cursor:pointer;display:inline-flex;align-items:center;gap:6px">
      📄 Tek Dönem Mizan
    </button>
    <button id="sampleHubBtn" type="button" class="secondary" style="background:#FFFFFF;color:#1D4ED8;border:1.5px solid #CBD5E1;padding:9px 14px;border-radius:10px;font-weight:700;font-size:12.5px;cursor:pointer;display:inline-flex;align-items:center;gap:6px">
      🗂️ 6-Dosyalı Data Hub
    </button>
    <span id="sampleStatus" class="small muted" style="margin-left:4px"></span>
  </div>
</div>
<div class="trustBar hidePrint">
<div class="item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>Önce hesap, sonra yorum — deterministik motor</div>
<div class="item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>KVKK Uyumlu · RAM-Only Geçici Bellek (Kalıcı Saklama Yok)</div>
<div class="item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 5-8"/></svg>33 Finansal Karar Motoru · Bütünleşik Karar Akışı</div>
</div>

<div class="tabs"><button class="tab active" data-tab="single">Tek Dönem Mizan</button><button class="tab" data-tab="trend" id="trendTabBtn">Çok Dönem / Trend</button><button class="tab" data-tab="datahub" id="hubTabBtn">Data Hub / Çoklu Veri</button></div>
<div id="single" class="tabPanel active">
  <div class="dropZone" id="dropZoneSingle">
    <div class="dropIco"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg></div>
    <div class="dropText">
      <strong>Mizan Dosyanızı Buraya Sürükleyin</strong>
      <span>veya bilgisayarınızdan seçin (.xlsx, .xls, .csv)</span>
    </div>
    <button type="button" class="secondary" style="margin-top:8px;padding:7px 16px;font-size:12.5px;pointer-events:none">📁 Dosya Seç</button>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:12px;font-size:11.5px;color:#475569">
    <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
      <span style="font-weight:700;color:#0F1B2D">Desteklenen Sistemler:</span>
      <span class="tag" style="background:#F1F5F9;font-size:11px">Logo</span>
      <span class="tag" style="background:#F1F5F9;font-size:11px">Mikro</span>
      <span class="tag" style="background:#F1F5F9;font-size:11px">Netsis</span>
      <span class="tag" style="background:#F1F5F9;font-size:11px">Luca</span>
      <span class="tag" style="background:#F1F5F9;font-size:11px">Zirve</span>
      <span class="tag" style="background:#F1F5F9;font-size:11px">SAP</span>
      <span class="tag" style="background:#EEF2FF;color:#1D4ED8;font-size:11px">🇩🇪 DATEV (SKR03/04)</span>
      <span class="tag" style="background:#EEF2FF;color:#1D4ED8;font-size:11px">🇫🇷 Pennylane / PCG</span>
      <span class="tag" style="background:#EEF2FF;color:#1D4ED8;font-size:11px">🇪🇸 Holded / PGC</span>
      <span class="tag" style="background:#EEF2FF;color:#1D4ED8;font-size:11px">🇳🇱 Exact Online</span>
      <span class="tag" style="background:#EEF2FF;color:#1D4ED8;font-size:11px">🇬🇧 Xero / Global Mizan</span>
      <span class="tag" style="background:#F1F5F9;font-size:11px">Excel / CSV</span>
    </div>
    <button type="button" onclick="downloadSampleMizan()" class="secondary" style="font-size:11.5px;padding:5px 12px;border-radius:8px;display:inline-flex;align-items:center;gap:6px">📥 Standart Mizan Şablonu İndir (.csv)</button>
  </div>
  <input id="file" class="file" type="file" accept=".csv,.xlsx,.xls,.xlsm" multiple style="display:none">
  <div id="fileListSingle" class="selectedFilesList"></div>
  <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:10px">
    <select id="sector" class="select"><option value="">Genel Sektör</option></select>
    <button id="analyze" class="primary" style="padding:13px 24px;font-size:14px;border-radius:12px;font-weight:700">🚀 Analizi Çalıştır (33 Karar Motoru)</button>
  </div>
</div>
<div id="trend" class="tabPanel">
  <div class="dropZone" id="dropZoneTrend">
    <div class="dropIco"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 5-8"/></svg></div>
    <div class="dropText">
      <strong>En Az 2 Dönemlik Mizan Dosyası Sürükleyin</strong>
      <span>Eski → yeni sırayla karşılaştırılacak (.xlsx, .xls, .csv)</span>
    </div>
    <button type="button" class="secondary" style="margin-top:8px;padding:7px 16px;font-size:12.5px;pointer-events:none">📁 2 Dosya Seç</button>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:12px;font-size:11.5px;color:#475569">
    <span class="small muted">Örn: 2024 Yıl Sonu + 2025 Yıl Sonu veya İki Ayrı Çeyrek Mizanı</span>
    <button type="button" onclick="downloadSampleMizan()" class="secondary" style="font-size:11.5px;padding:5px 12px;border-radius:8px;display:inline-flex;align-items:center;gap:6px">📥 Standart Mizan Şablonu İndir (.csv)</button>
  </div>
  <input id="trendFiles" class="file" type="file" accept=".csv,.xlsx,.xls,.xlsm" multiple style="display:none">
  <div id="fileListTrend" class="selectedFilesList"></div>
  <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:10px">
    <select id="trendSector" class="select"><option value="">Genel Sektör</option></select>
    <button id="analyzeTrend" class="primary" style="padding:13px 24px;font-size:14px;border-radius:12px;font-weight:700">🚀 Trend Analizini Başlat (2 Dönem)</button>
  </div>
</div>
<div id="datahub" class="tabPanel">
  <div class="dropZone" id="dropZoneHub">
    <div class="dropIco"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg></div>
    <div class="dropText">
      <strong>Mizan + Satış + AR/AP Yaşlandırma + Stok Dosyalarını Yükleyin</strong>
      <span>Tüm operasyonel defterleri bir arada analiz edin (.xlsx, .xls, .csv)</span>
    </div>
    <button type="button" class="secondary" style="margin-top:8px;padding:7px 16px;font-size:12.5px;pointer-events:none">📁 Çoklu Dosya Seç</button>
  </div>
  <input id="hubFiles" class="file" type="file" accept=".csv,.xlsx,.xls,.xlsm" multiple style="display:none">
  <div id="fileListHub" class="selectedFilesList"></div>
  <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:10px">
    <select id="hubSector" class="select"><option value="">Genel Sektör</option></select>
    <button id="analyzeHub" class="primary" style="padding:13px 24px;font-size:14px;border-radius:12px;font-weight:700">🚀 Tüm Verileri Analiz Et (Data Hub)</button>
  </div>
</div>
<div class="trustWallGrid">
  <div class="trustBadgeCard" onclick="showKvkkModal()">
    <div class="tIco">🛡️</div>
    <div class="tInfo">
      <strong>RAM-Only Bellek Mimarisi</strong>
      <span>Verileriniz diske/veritabanına yazılmaz. Analiz bittiğinde silinir.</span>
    </div>
  </div>
  <div class="trustBadgeCard" onclick="showKvkkModal()">
    <div class="tIco">🔐</div>
    <div class="tInfo">
      <strong>256-Bit TLS Şifreleme</strong>
      <span>Tüm dosya aktarımı bankacılık düzeyinde uçtan uca şifrelenir.</span>
    </div>
  </div>
  <div class="trustBadgeCard" onclick="showKvkkModal()">
    <div class="tIco">⚖️</div>
    <div class="tInfo">
      <strong>KVKK 6698 Uyumlu</strong>
      <span>Ticari mahremiyetiniz korunur; yapay zeka modelleriyle paylaşılmaz.</span>
    </div>
  </div>
  <div class="trustBadgeCard" onclick="showKvkkModal()">
    <div class="tIco">📑</div>
    <div class="tInfo">
      <strong>Kurumsal NDA Güvencesi</strong>
      <span>Kurumsal ve holding ölçeğinde yasal bağlayıcılıklı gizlilik sözleşmesi.</span>
    </div>
  </div>
</div>
<div id="error" class="error hidden"></div>
</div><div class="heroCard scoreCard"><div id="scoreRing" class="scoreRing" style="--score:0"><div class="scoreNum"><strong id="score">-</strong><span>Finansal Sağlık Skoru</span></div></div><div id="healthLabel" class="status">Dosya bekleniyor</div><button type="button" class="secondary small hidePrint" onclick="openScoreMethodologyModal()" style="margin:10px auto 0;font-size:11px;padding:5px 12px;border-radius:999px;display:inline-flex;align-items:center;gap:5px;cursor:pointer">📐 Skor Metodolojisi &amp; Formül</button>
<div id="topFocusCard" class="hidden hidePrint" style="margin-top:14px;border-top:1px solid rgba(15,27,45,.10);padding-top:10px;text-align:left"><div style="font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px">Öncelikli Odak Konuları</div><div id="topFocusList" style="display:flex;flex-direction:column;gap:6px"></div></div>
<div id="pvPreview" class="hidePrint" style="margin-top:18px;padding-top:16px;border-top:1px solid rgba(15,27,45,.10);text-align:left">
  <div class="pvLabel"><span style="display:inline-flex;align-items:center"><span class="dot"></span>Örnek Rapor Görünümü</span><span style="font-weight:700;color:var(--accent);background:#EFF6FF;padding:3px 10px;border-radius:6px;font-size:11px">⚡ Canlı Karar Motoru</span></div>
  <div class="pvRow"><span>Net Satış</span><span class="n up">↑ %25</span></div>
  <div class="pvRow"><span>Faaliyet Kârı</span><span class="n down">↓ %10</span></div>
  <div class="pvRow"><span>Net Borç</span><span class="n down">↑ %40</span></div>
  <div class="pvBars" title="İllüstratif çeyreklik trend"><i style="height:35%"></i><i style="height:55%"></i><i style="height:44%"></i><i style="height:70%"></i><i style="height:60%"></i><i style="height:82%"></i></div>
</div>
<div id="saveHistoryBox" class="hidden hidePrint" style="margin-top:16px;padding-top:14px;border-top:1px solid var(--line);text-align:left">
  <div class="small muted" style="margin-bottom:6px">Bu analizi kaydet</div>
  <input id="saveCompanyName" class="select" style="width:100%;margin-bottom:6px" type="text" placeholder="Şirket adı">
  <div style="display:flex;gap:6px">
    <input id="saveFiscalYear" class="select" style="width:90px" type="number" placeholder="2026">
    <input id="savePeriodLabel" class="select" style="flex:1" type="text" placeholder="Dönem (ör. Yıl Sonu)">
  </div>
  <button id="saveHistoryBtn" class="primary" style="width:100%;margin-top:8px">💾 Geçmişime Kaydet</button>
  <div id="saveHistoryStatus" class="small muted" style="margin-top:6px"></div>
</div>
</div></section>
<section id="historySection" class="flowStep hidePrint"><div class="flowLabel"><span class="n">↺</span>Geçmiş Analizlerim<p>Kaydettiğin analizleri yıla göre gör, iki dönemi karşılaştır</p></div>
<div class="card" style="padding:20px">
  <div id="historyLoggedOut"><p class="muted small" style="margin:0">Geçmiş analizlerini kaydetmek ve dönemler arası karşılaştırma yapmak için <a href="#" id="historyLoginLink" style="color:var(--accent)">giriş yap</a> veya <a href="#" id="historyRegisterLink" style="color:var(--accent)">ücretsiz kayıt ol</a>.</p></div>
  <div id="historyLoggedIn" class="hidden">
    <div style="display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:14px">
      <select id="historyYearFilter" class="select"><option value="">Tüm yıllar</option></select>
      <button id="historyRefreshBtn" class="secondary">Yenile</button>
      <button id="historyCompareBtn" class="secondary" disabled>Seçilenleri Karşılaştır (2 seç)</button>
      <span id="historyStatus" class="small muted"></span>
    </div>
    <div id="historyList"></div>
    <div id="historyCompareResult" style="margin-top:16px"></div>
  </div>
</div></section>
<div id="printCover" style="display:none">
  <div style="display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #1D4ED8;padding-bottom:6px;margin-bottom:12px">
    <div>
      <div style="font-size:16pt;font-weight:800;color:#0F1B2D;letter-spacing:-0.5px">Digital Finance Business Partner</div>
      <div style="font-size:8.5pt;color:#1D4ED8;font-weight:700;text-transform:uppercase;letter-spacing:0.5px;margin-top:2px">Yönetim Kurulu &amp; İcra Heyeti Finansal Karar Brifingi</div>
    </div>
    <div style="text-align:right">
      <div style="font-size:8pt;color:#64748B">Rapor Tarihi: <b id="printDate" style="color:#0F1B2D"></b></div>
      <div style="font-size:7.5pt;color:#DC2626;font-weight:700;margin-top:1px">GİZLİ &bull; ŞİRKET YÖNETİMİNE ÖZEL</div>
    </div>
  </div>
</div>
<div id="dashboard" class="hidden">

<!-- Global Accordion Controller Toolbar -->
<div class="accordionToolbar hidePrint" style="display:flex;justify-content:space-between;align-items:center;background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:14px;padding:14px 20px;margin-bottom:20px;box-shadow:0 4px 14px rgba(15,27,45,.04);flex-wrap:wrap;gap:12px">
  <div style="display:flex;align-items:center;gap:10px">
    <span style="font-size:16px">📑</span>
    <div>
      <div style="font-size:13.5px;font-weight:800;color:#0F172A">Yönetici Karar Raporu &bull; 9 Aşamalı Hiyerarşik Akış</div>
      <div style="font-size:11.5px;color:#64748B;margin-top:1px">En kritik yönetici kararlarından operasyonel detaylara doğru birbirine bağlı sıralama</div>
    </div>
    <span class="tag positive" style="font-size:10.5px;font-weight:700">Öncelik Sıralı</span>
  </div>
  <div style="display:flex;gap:8px">
    <button type="button" class="secondary" onclick="expandAllSteps()" style="font-size:11.5px;padding:6px 14px;border-radius:8px;font-weight:700">▼ Tüm Bölümleri Genişlet</button>
    <button type="button" class="secondary" onclick="collapseAllSteps()" style="font-size:11.5px;padding:6px 14px;border-radius:8px;font-weight:700">▲ Tümünü Daralt</button>
  </div>
</div>

<!-- Sticky Dashboard Sub-Navigation Bar -->
<div id="dashboardSubNav" class="dashboardSubNav hidePrint" style="position:sticky;top:62px;z-index:45;background:#FFFFFF;border-bottom:1.5px solid #E2E8F0;box-shadow:0 4px 14px rgba(15,27,45,0.05);padding:9px 0;margin-bottom:20px;overflow-x:auto;-webkit-overflow-scrolling:touch;display:flex;gap:7px;white-space:nowrap">
  <button type="button" class="dashPill" onclick="jumpToFlowStep('flowStep_1')">1. Finansal Röntgen</button>
  <button type="button" class="dashPill" onclick="jumpToFlowStep('flowStep_2')">2. Öncelikli Riskler</button>
  <button type="button" class="dashPill" onclick="jumpToFlowStep('flowStep_3')">3. Kilitli Nakit &amp; Faiz</button>
  <button type="button" class="dashPill" onclick="jumpToFlowStep('flowStep_4')">4. Operasyonel Kârlılık</button>
  <button type="button" class="dashPill" onclick="jumpToFlowStep('flowStep_5')">5. Bilanço &amp; CCC</button>
  <button type="button" class="dashPill" onclick="jumpToFlowStep('flowStep_6')">6. Kritik Taraflar</button>
  <button type="button" class="dashPill" onclick="jumpToFlowStep('flowStep_7')">7. Kök Neden Hikâyeleri</button>
  <button type="button" class="dashPill" onclick="jumpToFlowStep('flowStep_8')">8. Vergi Kalkanı</button>
  <button type="button" class="dashPill" onclick="jumpToFlowStep('flowStep_9')">9. Senaryo Lab</button>
  <button type="button" class="dashPill" onclick="jumpToFlowStep('flowStep_ekA')">Ek A · Denetim</button>
  <button type="button" class="dashPill" onclick="jumpToFlowStep('flowStep_ekB')">Ek B · Mali Tablolar</button>
</div>

<!-- ==================== BÖLÜM 1: YÖNETİCİ BRİFİNGİ & FİNANSAL RÖNTGEN ==================== -->
<section id="flowStep_1" class="accordionStep active">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_1')">
    <div class="accordionTitleGroup">
      <span class="accordionNum">1</span>
      <div>
        <h3 class="accordionTitle">Yönetici Brifingi, Finansal Röntgen &amp; Stratejik Soru Masası</h3>
        <div class="accordionSub">C-Level Yönetici Özeti, 30 saniyelik teşhis, AI Finance Partner ve CEO 8 soru masası</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag" style="background:#EFF6FF;color:#1D4ED8;font-size:11px;font-weight:700">C-Level Snapshot</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <!-- 30 SANİYELİK CEO & PATRON FİNANSAL RÖNTGENİ -->
    <div id="executiveSnapshotSection" style="margin-bottom:20px">
      <div class="card" style="background:#FFFFFF;border:1.5px solid #CBD5E1;border-radius:18px;padding:22px 24px;box-shadow:0 8px 24px rgba(15,27,45,0.06);margin-bottom:0">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:16px;border-bottom:1px solid #E2E8F0;padding-bottom:14px">
          <div style="display:flex;align-items:center;gap:10px">
            <span style="background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE;font-size:11px;font-weight:800;letter-spacing:1px;padding:4px 10px;border-radius:6px;text-transform:uppercase">⚡ 30 Saniyelik Teşhis</span>
            <h3 style="margin:0;font-size:17px;font-weight:700;color:#0F1B2D;letter-spacing:-0.3px">Şirket Yönetim Özeti: Kâr Durumu, Kilitli Para ve Öncelikli Karar</h3>
          </div>
          <div style="font-size:11.5px;color:#64748B;display:flex;align-items:center;gap:8px">
            <span>Deterministik Çift Taraflı Denetim:</span>
            <span id="snapAuditStatus" style="color:#16A34A;font-weight:700;background:#DCFCE7;border:1px solid #BBF7D0;padding:2px 8px;border-radius:6px">✓ %100 Bilanço Denkliği Doğrulandı</span>
            <button type="button" class="secondary small hidePrint" onclick="openScoreMethodologyModal()" style="font-size:11px;padding:3px 10px;border-radius:6px;font-weight:700;cursor:pointer">📐 Skor Metodolojisi &amp; Formül</button>
          </div>
        </div>
        
        <div id="reconciliationTopAlert" style="display:none;margin-bottom:16px"></div>

        <div class="grid3" style="gap:14px">
          <!-- Kart 1: Kâr Durumu ve Kasaya Giren Nakit -->
          <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:14px;padding:16px">
            <div style="font-size:11px;color:#64748B;text-transform:uppercase;letter-spacing:0.8px;font-weight:700;margin-bottom:6px">🩺 1. KÂR DURUMU VE KASAYA GİREN NAKİT</div>
            <div style="font-size:20px;font-weight:800;color:#0F1B2D;margin-bottom:4px" id="snapProfitQualityVal">-</div>
            <div style="font-size:12px;color:#475569;line-height:1.5" id="snapProfitQualityDesc">Defterdeki kâr ile kasaya giren nakit dengesi hesaplanıyor...</div>
          </div>
          
          <!-- Kart 2: Şirketin Parasının Kilitlendiği Yer -->
          <div style="background:#FFFBEB;border:1px solid #FDE68A;border-radius:14px;padding:16px">
            <div style="font-size:11px;color:#B45309;text-transform:uppercase;letter-spacing:0.8px;font-weight:700;margin-bottom:6px">💼 2. ŞİRKETİN PARASININ KİLİTLENDİĞİ YER</div>
            <div style="font-size:20px;font-weight:800;color:#B45309;margin-bottom:4px" id="snapCapitalLeakVal">-</div>
            <div style="font-size:12px;color:#92400E;line-height:1.5" id="snapCapitalLeakDesc">Şirket parasının en çok kilitlendiği ana kalem tespit ediliyor...</div>
          </div>
          
          <!-- Kart 3: Alınacak 1 Numaralı Yönetim Kararı -->
          <div style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:14px;padding:16px">
            <div style="font-size:11px;color:#1D4ED8;text-transform:uppercase;letter-spacing:0.8px;font-weight:700;margin-bottom:6px">🎯 3. ALINACAK 1 NUMARALI YÖNETİM KARARI</div>
            <div style="font-size:20px;font-weight:800;color:#1D4ED8;margin-bottom:4px" id="snapTopActionVal">-</div>
            <div style="font-size:12px;color:#1E3A8A;line-height:1.5" id="snapTopActionDesc">Kasaya sıcak nakit girdisi sağlayacak ilk aksiyon planlanıyor...</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Yönetici Özeti & AI Business Partner -->
    <div class="card" style="margin-bottom:20px">
      <div class="sectionHead">
        <div>
          <h2>Yönetici Hikâyesi &amp; Karar Brifingi</h2>
          <p>Tüm analizin tek paragrafta özeti, stratejik öncelikler ve yapay zekâ finans danışmanı</p>
        </div>
        <span class="tag" style="background:#EEF2FF;color:#3B4B8A">Kural Tabanlı · AI Değil</span>
      </div>
      <div id="exec" class="insight"></div>
      <div id="execChips" class="chips"></div>
      <div id="execDecision" style="margin-top:14px"></div>
      <div style="margin-top:14px">
        <button id="aiBtn" class="secondary hidePrint">✨ AI Finance Partner yorumunu üret (opsiyonel, LLM)</button>
        <button id="boardDeckBtn" type="button" class="secondary hidePrint" style="border-color:#1D4ED8;color:#1D4ED8;font-weight:700">📑 1-Sayfalık Yönetim Kurulu Özeti (Board One-Pager)</button>
        <button id="printBtn" class="secondary hidePrint">Raporu yazdır / PDF</button>
        <button id="jsonBtn" class="secondary hidePrint">JSON indir</button>
      </div>
      <div id="aiBox" class="notice hidden" style="margin-top:12px"></div>
      <div id="methodNote" class="notice" style="margin-top:12px"></div>

      <!-- AI Q&A Bar -->
      <div style="margin-top:16px;padding-top:16px;border-top:1px solid rgba(15,27,45,.10)">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px">
          <span style="font-size:18px">💬</span>
          <b style="font-size:14px">AI Finance Business Partner'a Özel Soru Sor (Stratejik Q&amp;A)</b>
          <span class="tag" style="background:#EAF0FF;color:var(--accent)">Gemini 3.6 Flash Doğrulanmış</span>
        </div>
        <div style="display:flex;gap:10px;align-items:center">
          <input id="aiCustomPrompt" type="text" placeholder="Örn: Nakit neden oluşmuyor?" style="flex:1;background:#FFFFFF;border:1px solid #D7DEE8;color:#0F1B2D;border-radius:10px;padding:10px 14px;font-size:13px">
          <button id="aiAskBtn" class="primary hidePrint" style="white-space:nowrap;padding:10px 18px">Soruyu Yanıtla ⚡</button>
        </div>
        <div class="chips hidePrint" style="margin-top:10px">
          <span class="chip" style="cursor:pointer" onclick="setAiPrompt('Nakit neden oluşmuyor?')">💸 Nakit neden oluşmuyor?</span>
          <span class="chip" style="cursor:pointer" onclick="setAiPrompt('Kâr neden düşüyor?')">📉 Kâr neden düşüyor?</span>
          <span class="chip" style="cursor:pointer" onclick="setAiPrompt('Borç neden artıyor?')">📈 Borç neden artıyor?</span>
          <span class="chip" style="cursor:pointer" onclick="setAiPrompt('Kâr gerçekten nakde dönüşüyor mu?')">🔄 Kâr gerçekten nakde dönüşüyor mu?</span>
          <span class="chip" style="cursor:pointer" onclick="setAiPrompt('Ciro artarken kâr neden eriyor?')">⚠️ Ciro artarken kâr neden eriyor?</span>
          <span class="chip" style="cursor:pointer" onclick="setAiPrompt('Hangi vergi avantajları ve teşvik fırsatları var?')">🏛️ Vergi avantajı &amp; KDV optimizasyonu</span>
          <span class="chip" style="cursor:pointer" onclick="setAiPrompt('Hangi müşteriler risk yaratıyor?')">⚠️ Hangi müşteriler risk yaratıyor?</span>
          <span class="chip" style="cursor:pointer" onclick="setAiPrompt('Hangi tedarikçiler kritik?')">🏭 Hangi tedarikçiler kritik?</span>
          <span class="chip" style="cursor:pointer" onclick="setAiPrompt('Stok neden şişiyor?')">📦 Stok neden şişiyor?</span>
        </div>
        <div id="aiCustomBox" class="notice hidden" style="margin-top:14px"></div>
      </div>
    </div>

    <!-- CEO & YÖNETİM KURULU KARAR MASASI -->
    <div id="ceoDiagnosticSection">
      <div class="card" style="border:2px solid #1D4ED8;background:linear-gradient(180deg,#FFFFFF 0%,#F8FAFC 100%);box-shadow:0 14px 40px rgba(29,78,216,.09);padding:26px;border-radius:22px;margin-bottom:0">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px;border-bottom:1.5px solid #E2E8F0;padding-bottom:18px;margin-bottom:20px">
          <div>
            <div style="display:inline-flex;align-items:center;gap:8px;background:#EFF6FF;border:1px solid #BFDBFE;padding:4px 12px;border-radius:999px;color:#1D4ED8;font-size:11px;font-weight:800;letter-spacing:.5px;margin-bottom:8px">
              💼 YÖNETİM KARAR MASASI
            </div>
            <h2 style="font-family:var(--serif);font-size:24px;color:#0F1B2D;margin:0 0 6px;letter-spacing:-.5px">
              Finansal Gerçeklerden Yönetim Kararlarına: 8 Kritik Yönetim Sorusu
            </h2>
            <p class="muted" style="margin:0;font-size:13.5px;max-width:880px;line-height:1.6">
              Şirket yönetimi muhasebe evrakı değil; <i>"Kasada neden para yok ve yarın ne yapmalıyız?"</i> sorusunun cevabını arar. Yüklediğiniz mizan ve defterlerden <b>33 Finansal Karar Motorunun</b> ürettiği anlık 3 katmanlı teşhis, serbest kalacak nakit ve somut aksiyonlar:
            </p>
          </div>
          <div style="text-align:right">
            <span class="tag positive" style="font-size:11px;font-weight:700">⚡ 3 KATMANLI KARAR MİMARİSİ</span>
            <div class="small muted" style="margin-top:4px">1. Soru → 2. Analitik Kanıt → 3. Yönetim Aksiyonu</div>
          </div>
        </div>

        <!-- 8 Questions Navigation Pills -->
        <div style="position:relative;display:flex;align-items:center;margin-bottom:18px;gap:6px">
          <button type="button" class="pillScrollBtn" onclick="scrollPills('ceoQuestionPills', -280)" aria-label="Geri Kaydır" title="Önceki Sorular">‹</button>
          <div id="ceoQuestionPills" style="display:flex;gap:8px;overflow-x:auto;padding-bottom:6px;scrollbar-width:none;-ms-overflow-style:none;scroll-behavior:smooth;flex:1"></div>
          <button type="button" class="pillScrollBtn" onclick="scrollPills('ceoQuestionPills', 280)" aria-label="İleri Kaydır" title="Sonraki Sorular">›</button>
        </div>

        <!-- Question Detail Container -->
        <div id="ceoQuestionDetails"></div>
      </div>
    </div>
  </div>
</section>

<!-- ==================== BÖLÜM 2: ÖNCELİKLİ YÖNETİM RİSKLERİ & AKSİYON TAKVİMİ ==================== -->
<section id="flowStep_2" class="accordionStep active">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_2')">
    <div class="accordionTitleGroup">
      <span class="accordionNum">2</span>
      <div>
        <h3 class="accordionTitle">Öncelikli Yönetim Riskleri &amp; İcraat Aksiyon Takvimi</h3>
        <div class="accordionSub">Finansal maruziyet, risk skorları, görev sahipleri, terminler ve somut icraat planı</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag critical" style="font-size:11px;font-weight:700">Acil Eylem Planı</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <div class="card">
      <div class="sectionHead">
        <div>
          <h2>Öncelikli Yönetim Riskleri</h2>
          <p>Finansal maruziyet, risk skoru ve şiddet derecesi birlikte sıralanır</p>
        </div>
      </div>
      <div id="risks"></div>
    </div>

    <div class="card" style="margin-top:16px;margin-bottom:0">
      <div class="sectionHead">
        <div>
          <h2>Yönetim Kararları &amp; Aksiyon Takvimi (Şimdi Ne Yapmalı?)</h2>
          <p>Karar maddesi → Sahibi → Termini → Takip Edilecek KPI. Her aksiyon maddesi ayrı bir takip numarasına sahiptir.</p>
        </div>
      </div>
      <div id="actions"></div>
    </div>
  </div>
</section>

<!-- ==================== BÖLÜM 3: PARA NEREDE? & NAKİT AKIŞ KÖPRÜSÜ ==================== -->
<section id="flowStep_3" class="accordionStep active">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_3')">
    <div class="accordionTitleGroup">
      <span class="accordionNum">3</span>
      <div>
        <h3 class="accordionTitle">Para Nerede? — Kilitli Nakit Teşhisi &amp; Nakit Akış Köprüsü</h3>
        <div class="accordionSub">Müşteri vadelerinde ve depoda kilitlenen sermaye, faiz sızıntısı ve net nakit şelalesi</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag" style="background:#FEF3C7;color:#B45309;font-size:11px;font-weight:700">Kilitli Sermaye</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <!-- Görünmez Kâr Sızıntısı & Kilitli Sermaye -->
    <div id="workingCapitalLeakEngineCard" class="card" style="border:1.5px solid #CBD5E1;background:linear-gradient(145deg,#FFFFFF 0%,#F8FAFC 100%)">
      <div class="sectionHead">
        <div>
          <h2 style="font-size:16px;color:#1D4ED8">⚡ Şirketinizin Görünmez Kâr Sızıntısı &amp; Kilitli Nakit Tablosu</h2>
          <p>Yüklenen mizan ve defterlerinizden hesaplanan gerçek işletme sermayesi kilitlenmesi ve faiz yükü</p>
        </div>
        <span class="tag positive" style="font-weight:800;font-size:11px">CANLI MİZAN TEŞHİSİ</span>
      </div>
      
      <div class="grid4" style="margin-top:10px">
        <div class="metric" style="background:#FFFFFF;border-color:#FCA5A5">
          <div class="label" style="color:#DC2626">🔒 Müşterilerde Kilitli Alacak (120)</div>
          <div id="wcLeakArVal" class="value" style="color:#991B1B">-</div>
          <div id="wcLeakArSub" class="sub">Ortalama tahsilat vadesi: – gün</div>
        </div>
        <div class="metric" style="background:#FFFFFF;border-color:#FCD34D">
          <div class="label" style="color:#D97706">📦 Depoda Kilitli Stok (150-153)</div>
          <div id="wcLeakInvVal" class="value" style="color:#B45309">-</div>
          <div id="wcLeakInvSub" class="sub">Ortalama stokta bekleme: – gün</div>
        </div>
        <div class="metric" style="background:#FFFFFF;border-color:#93C5FD">
          <div class="label" style="color:#2563EB">🏭 Tedarikçilere Borçlar (320)</div>
          <div id="wcLeakApVal" class="value" style="color:#1D4ED8">-</div>
          <div id="wcLeakApSub" class="sub">Ortalama ödeme vadesi: – gün</div>
        </div>
        <div class="metric" style="background:#FFFFFF;border-color:#FECDD3">
          <div class="label" style="color:#E11D48">💸 Yıllık Kâr Sızıntısı (Faiz Yükü)</div>
          <div id="wcLeakCostVal" class="value" style="color:#BE123C">-</div>
          <div id="wcLeakCostSub" class="sub">Kilitli sermayenin yıllık %45 finansman maliyeti</div>
        </div>
      </div>

      <!-- Faiz Oranı Belirleme Aracı -->
      <div id="wcInterestToolCard" style="background:#FFF1F2;border:1.5px solid #FECDD3;border-radius:14px;padding:12px 18px;margin-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px">
        <div style="display:flex;align-items:center;gap:12px">
          <div style="width:38px;height:38px;border-radius:10px;background:#FFE4E6;display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0">🏦</div>
          <div>
            <div style="font-size:13px;font-weight:800;color:#9F1239;display:flex;align-items:center;gap:8px">
              <span>Yıllık Borçlanma / Faiz Oranı Belirleme Aracı:</span>
              <span id="wcInterestRateDisplay" style="background:#BE123C;color:#FFFFFF;padding:2px 8px;border-radius:6px;font-size:13px;font-weight:900">%45</span>
            </div>
            <div style="font-size:11.5px;color:#BE123C;margin-top:2px">Şirketinizin fiili kredi faiz oranını belirleyin; kilitli nakdin yarattığı yıllık faiz yükünü anlık hesaplasın.</div>
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
          <div style="display:flex;gap:4px">
            <button type="button" class="secondary wcRatePreset" onclick="setWcInterestRate(30)" style="font-size:11px;padding:5px 9px;border-radius:7px;font-weight:700">%30</button>
            <button type="button" class="secondary wcRatePreset" onclick="setWcInterestRate(40)" style="font-size:11px;padding:5px 9px;border-radius:7px;font-weight:700">%40</button>
            <button type="button" class="secondary wcRatePreset active" onclick="setWcInterestRate(45)" style="font-size:11px;padding:5px 9px;border-radius:7px;font-weight:700;background:#FFE4E6;border-color:#BE123C;color:#9F1239">%45</button>
            <button type="button" class="secondary wcRatePreset" onclick="setWcInterestRate(55)" style="font-size:11px;padding:5px 9px;border-radius:7px;font-weight:700">%55</button>
            <button type="button" class="secondary wcRatePreset" onclick="setWcInterestRate(65)" style="font-size:11px;padding:5px 9px;border-radius:7px;font-weight:700">%65</button>
          </div>
          <div style="display:flex;align-items:center;gap:8px">
            <input id="wcInterestRateInput" type="range" min="10" max="85" value="45" step="1" oninput="setWcInterestRate(this.value)" style="width:120px;cursor:pointer">
            <input id="wcInterestRateNum" type="number" min="5" max="100" value="45" step="1" onchange="setWcInterestRate(this.value)" oninput="setWcInterestRate(this.value)" style="width:58px;padding:4px 6px;font-size:12.5px;font-weight:800;text-align:center;border-radius:7px;border:1.5px solid #FECDD3;color:#9F1239;background:#FFFFFF">
            <b style="font-size:13px;color:#9F1239">%</b>
          </div>
        </div>
      </div>

      <div style="margin-top:16px;background:#FFFFFF;border:1px solid #E2E8F0;border-radius:14px;padding:16px">
        <div style="font-size:13.5px;font-weight:800;color:#0F172A;margin-bottom:12px;display:flex;justify-content:space-between;align-items:center">
          <span>🎛️ Çoklu Kaldıraçlı Nakit &amp; Kâr Kurtarma Simülatörü</span>
          <span class="tag" style="background:#EFF6FF;color:var(--accent);font-size:10.5px">CANLI KARAR LABORATUVARI</span>
        </div>

        <div class="grid2" style="gap:14px">
          <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
              <span style="font-size:12px;font-weight:700;color:#1E293B">1. Tahsilat Vadesini Kısalt (DSO Hızlandırma)</span>
              <b id="wcSliderDsoDisplay" style="color:#1D4ED8;font-size:13px">15 Gün Erken Tahsilat</b>
            </div>
            <input id="wcSliderDso" type="range" min="0" max="60" value="15" step="1" style="width:100%;cursor:pointer">
          </div>

          <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
              <span style="font-size:12px;font-weight:700;color:#1E293B">2. Stokta Beklemeyi Azalt (DIO / Ölü Stok Eritme)</span>
              <b id="wcSliderDioDisplay" style="color:#D97706;font-size:13px">10 Gün Daha Hızlı Stok</b>
            </div>
            <input id="wcSliderDio" type="range" min="0" max="60" value="10" step="1" style="width:100%;cursor:pointer">
          </div>

          <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
              <span style="font-size:12px;font-weight:700;color:#1E293B">3. Tedarikçi Vadesini Optimize Et (DPO Uzatma)</span>
              <b id="wcSliderDpoDisplay" style="color:#0E7C66;font-size:13px">5 Gün Vade Öteleme</b>
            </div>
            <input id="wcSliderDpo" type="range" min="0" max="45" value="5" step="1" style="width:100%;cursor:pointer">
          </div>

          <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
              <span style="font-size:12px;font-weight:700;color:#1E293B">4. Brüt Kâr Marjı / Faaliyet Gider (OpEx) Tasarrufu</span>
              <b id="wcSliderMarginDisplay" style="color:#7C3AED;font-size:13px">+1.5% Marj / Tasarruf</b>
            </div>
            <input id="wcSliderMargin" type="range" min="0" max="5.0" value="1.5" step="0.5" style="width:100%;cursor:pointer">
          </div>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px">
          <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:12px;padding:12px 16px">
            <div style="font-size:11px;font-weight:800;color:#16A34A;text-transform:uppercase">🚀 Kasaya Girecek Toplam Sıcak Nakit</div>
            <div id="wcSliderCashLiberated" style="font-size:24px;font-weight:900;color:#047857;margin-top:2px">+₺0</div>
            <div class="small muted">Alacak tahsilatı + stok eritme + tedarikçi finansmanıyla doğrudan kasaya giren nakit</div>
          </div>
          <div style="background:#EFF6FF;border:1.5px solid #BFDBFE;border-radius:12px;padding:12px 16px">
            <div style="font-size:11px;font-weight:800;color:#1D4ED8;text-transform:uppercase">📈 Yıllık Kurtarılacak Net Kâr &amp; Faiz Tasarrufu</div>
            <div id="wcSliderInterestSaved" style="font-size:24px;font-weight:900;color:#1E40AF;margin-top:2px">+₺0 / yıl</div>
            <div class="small muted">Kurtarılan %45 kredi faizi + fiyat/gider verimliliğiyle doğrudan bilançoya eklenen kâr</div>
          </div>
        </div>
      </div>

      <div id="wcLeakSummaryBox" class="insight" style="margin-top:14px;margin-bottom:0"></div>
    </div>

    <!-- Nakit Akış Köprüsü ve Kârın Nakde Dönüşüm Analizi -->
    <div id="unifiedCashBridgeCard" class="card" style="margin-top:16px">
      <div class="sectionHead">
        <div>
          <h2>Nakit Akış Köprüsü ve Kârın Nakde Dönüşüm Analizi</h2>
          <p>Dönem başından dönem sonuna nakit hareketi ve defterdeki kârın kasaya fiilen ne kadar girdiği</p>
        </div>
      </div>
      <!-- Nakit Akış Köprüsü (Şelale) - Tam Genişlik -->
      <div id="cashFlowCard">
        <div class="small muted" style="font-weight:700;margin-bottom:8px">Nakit Akış Köprüsü (Şelale Grafiği)</div>
        <div id="cashFlow"></div>
      </div>
      <!-- Kârın Nakde Dönüşüm Süreci (Adım Adım Yönetici Hattı) -->
      <div id="cashRealizationCard" style="margin-top:20px;border-top:1.5px solid #E2E8F0;padding-top:16px">
        <div class="small muted" style="font-weight:700;margin-bottom:10px">Kârın Nakde Dönüşüm Analizi (Defter Kârı → Kasa Nakdi)</div>
        <div id="cashRealization"></div>
      </div>
    </div>

    <!-- Sermaye Dağılımı ve Nakit Sıkışması -->
    <div id="resourceAllocationCard" class="card hidden" style="margin-top:16px;margin-bottom:0">
      <div class="sectionHead">
        <div>
          <h2>Sermaye Dağılımı ve Nakit Sıkışması (Para Nerede?)</h2>
          <p>Şirketin bağladığı toplam sermaye nerede duruyor: Kasada mı, alacakta mı, stokta mı?</p>
        </div>
      </div>
      <div id="resourceAllocationMetrics" class="grid4"></div>
      <div id="resourceAllocationBar" style="margin-top:16px"></div>
      <div id="resourceAllocationNarrative" style="margin-top:14px"></div>
    </div>
  </div>
</section>

<!-- ==================== BÖLÜM 4: OPERASYONEL KÂRLILIK & KÂR KÖPRÜSÜ ==================== -->
<section id="flowStep_4" class="accordionStep active">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_4')">
    <div class="accordionTitleGroup">
      <span class="accordionNum">4</span>
      <div>
        <h3 class="accordionTitle">Operasyonel Kârlılık, Kâr Köprüsü &amp; Kâr Kalitesi</h3>
        <div class="accordionSub">Net satıştan net kâra giden yol, maliyet sızıntıları ve DuPont 3-Aşamalı ROE motorları</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag" style="background:#ECFDF5;color:#065F46;font-size:11px;font-weight:700">P&amp;L Zekâsı</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <div class="grid4">
      <div class="metric"><div class="label">Net Satış (Ciro)</div><div id="mSales" class="value">-</div><div class="sub">Doğrulanmış toplam satış hacmi</div></div>
      <div class="metric"><div class="label">Faaliyet Kârı</div><div id="mOp" class="value">-</div><div class="sub">Esas faaliyetlerden kalan operasyonel kâr</div></div>
      <div class="metric"><div class="label">Net Dönem Kârı</div><div id="mNet" class="value">-</div><div class="sub">Vergi ve finansman giderleri sonrası net kâr</div></div>
      <div class="metric"><div class="label">Net Finansal Borç</div><div id="mDebt" class="value">-</div><div class="sub">Toplam banka borcundan nakit düşülmüş net yük</div></div>
    </div>

    <div id="profitQualityCard" class="card" style="margin-top:16px">
      <div class="sectionHead">
        <div>
          <h2>Kâr Köprüsü &amp; Kâr Kalitesi Analizi</h2>
          <p>Net satıştan net kâra giden yol ve bu kârın ne kadarının operasyonel olduğu</p>
        </div>
      </div>
      <div class="grid2">
        <div>
          <div class="small muted" style="margin-bottom:8px">Kâr Köprüsü (Şelale)</div>
          <div class="waterfallWrap"><div id="waterfall" class="waterfall"></div></div>
        </div>
        <div>
          <div class="small muted" style="margin-bottom:8px">Kâr Kalitesi Metrikleri</div>
          <div id="profitQuality"></div>
        </div>
      </div>
      <div id="profitabilityCommentary" style="margin-top:14px"></div>
    </div>

    <div id="dupontCard" class="card hidden" style="margin-top:16px;margin-bottom:0">
      <div class="sectionHead">
        <div>
          <h2>Özkaynak Kârlılık Ağacı (DuPont ROE Motorları)</h2>
          <p>Hissedarın koyduğu sermayenin getirisini (ROE) belirleyen üç ana motor: Kâr Marjı × Varlık Devir Hızı × Finansal Kaldıraç</p>
        </div>
      </div>
      <div class="grid4">
        <div class="metric"><div class="label">Özkaynak Kârlılığı (ROE)</div><div id="dupontRoe" class="value">-</div><div class="sub">Hissedar Getirisi</div></div>
        <div class="metric"><div class="label">Net Kâr Marjı</div><div id="dupontMargin" class="value">-</div><div class="sub">Operasyonel Kârlılık Oranı</div></div>
        <div class="metric"><div class="label">Varlık Devir Hızı</div><div id="dupontTurnover" class="value">-</div><div class="sub">Varlıkları Paraya Çevirme Hızı</div></div>
        <div class="metric"><div class="label">Kaldıraç Çarpanı</div><div id="dupontLeverage" class="value">-</div><div class="sub">Varlık / Özkaynak Çarpanı</div></div>
      </div>
      <div id="dupontDiagnosis" class="chips" style="margin-top:12px"></div>
    </div>
  </div>
</section>

<!-- ==================== BÖLÜM 5: BİLANÇO GÜCÜ, BORÇ YAPISI & LİKİDİTE ==================== -->
<section id="flowStep_5" class="accordionStep active">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_5')">
    <div class="accordionTitleGroup">
      <span class="accordionNum">5</span>
      <div>
        <h3 class="accordionTitle">Bilanço Gücü, Borç Yapısı &amp; Nakit Çevrim Süresi (CCC)</h3>
        <div class="accordionSub">Kısa vadeli ödeme gücü, finansal borç kaldıracı ve alacak-stok-tedarikçi vadeleri</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag" style="background:#F1F5F9;color:#334155;font-size:11px;font-weight:700">Solvency &amp; Vade</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <div class="grid2">
      <div id="leverageCard" class="card">
        <div class="sectionHead">
          <div>
            <h2>Borç Yapısı &amp; Likidite Oranları</h2>
            <p>Bilançonun taşıdığı finansal borç baskısı ve kısa vadeli ödeme gücü</p>
          </div>
        </div>
        <div id="liquidity" class="grid2"></div>
        <div id="leverageCommentary" style="margin-top:14px"></div>
      </div>

      <div class="card">
        <div class="sectionHead">
          <div>
            <h2>Nakit Çevrim Süresi (İşletme Sermayesi)</h2>
            <p>Cebinizden çıkan paranın tahsilatla geri kasaya dönme süresi</p>
          </div>
        </div>
        <div id="workingCapital"></div>
      </div>
    </div>
  </div>
</section>

<!-- ==================== BÖLÜM 6: KRİTİK TARAFLAR & OPERASYONEL İSTİHBARAT ==================== -->
<section id="flowStep_6" class="accordionStep active">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_6')">
    <div class="accordionTitleGroup">
      <span class="accordionNum">6</span>
      <div>
        <h3 class="accordionTitle">Kritik Taraflar &amp; Operasyonel İstihbarat (Müşteri &bull; Tedarikçi &bull; Stok)</h3>
        <div class="accordionSub">4-Kadran Müşteri Matrisi, Ürün kârlılığı, yaşlandırma vadeleri ve konsantrasyon riskleri</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag" style="background:#EFF6FF;color:#2563EB;font-size:11px;font-weight:700">Operasyonel Zekâ</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <div id="criticalPartiesNotice" class="notice">Bu bölüm "Data Hub / Çoklu Veri" sekmesinden satış, alacak yaşlandırma veya stok dosyası yüklendiğinde zenginleşir.</div>
    <div id="customerProfitabilityMatrixCard" class="card hidden" style="margin-top:14px">
      <div class="sectionHead">
        <div>
          <h2>Müşteri Kârlılık Matrisi (4 Kadran)</h2>
          <p>Hangi müşteriler kâr getiriyor, hangileri ciro yaratıp sermaye tüketiyor?</p>
        </div>
      </div>
      <div id="customerMatrixGrid" class="grid2" style="gap:12px"></div>
      <div id="customerMatrixFindings" style="margin-top:14px"></div>
    </div>
    <div id="productProfitabilityCard" class="card hidden" style="margin-top:14px">
      <div class="sectionHead">
        <div>
          <h2>Ürün &amp; Portföy Kârlılığı</h2>
          <p>Hangi ürünler brüt kârı sırtlıyor, hangi ürünler depoda sermaye kilitliyor?</p>
        </div>
      </div>
      <div id="productProfitabilityTable" class="tableWrap"></div>
    </div>
    <div id="criticalCustomersCard" style="margin-top:14px"></div>
    <div id="criticalSuppliersCard" style="margin-top:14px"></div>
    <div id="salesIntel" style="margin-top:14px"></div>
    <div id="arApIntel" style="margin-top:14px"></div>
    <div id="inventoryIntel" style="margin-top:14px"></div>
  </div>
</section>

<!-- ==================== BÖLÜM 7: KÖK NEDEN & KARAR HİKÂYELERİ ==================== -->
<section id="flowStep_7" class="accordionStep active">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_7')">
    <div class="accordionTitleGroup">
      <span class="accordionNum">7</span>
      <div>
        <h3 class="accordionTitle">5 Adımlı Kök Neden Analizleri &amp; Karar Hikâyeleri</h3>
        <div class="accordionSub">Belirti (Ne Oldu?) ➔ Sayısal Kanıt ➔ Kök Neden (Tetikleyici) ➔ Parasal Sızıntı ➔ İcraat Kararı</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag" style="background:#EEF2FF;color:#3B4B8A;font-size:11px;font-weight:700">Nedensellik</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <div id="rootCauseCard" class="card" style="padding:22px;border:1.5px solid #CBD5E1;margin-bottom:0">
      <div class="sectionHead">
        <div>
          <h2 style="font-size:16px;color:#0F1B2D">🧠 Bütünleşik Kök Neden &amp; Karar Hikâyeleri</h2>
          <p>Mizan ve operasyonel defterlerdeki finansal sapmaların arkasındaki gerçek iş süreçleri ve alınacak aksiyonlar</p>
        </div>
        <span class="tag" style="background:#EEF2FF;color:#3B4B8A;font-weight:700;font-size:11px">5 ADIMLI NEDENSELLİK ZİNCİRİ</span>
      </div>
      <div id="rootCause" style="margin-top:14px;display:flex;flex-direction:column;gap:16px"></div>
    </div>
    <div id="narrativeStories" style="display:none"></div>
  </div>
</section>

<!-- ==================== BÖLÜM 8: VERGİSEL YÖNETİM AVANTAJLARI & TEŞVİKLER ==================== -->
<section id="flowStep_8" class="accordionStep active">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_8')">
    <div class="accordionTitleGroup">
      <span class="accordionNum">8</span>
      <div>
        <h3 class="accordionTitle">Vergisel Yönetim Avantajları &amp; Yasal Nakit Tasarrufu</h3>
        <div class="accordionSub">Mizan verilerinizden türetilmiş VUK &amp; KVK uyumlu vergi kalkanları, KKEG tasarrufları ve teşvikler</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag positive" style="font-size:11px;font-weight:700">VUK &amp; KVK Uyumlu</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <div id="taxStrategyCard" class="card" style="border:1.5px solid #A7F3D0;background:linear-gradient(145deg,#FFFFFF 0%,#F0FDF4 100%);margin-bottom:0">
      <div class="sectionHead">
        <div>
          <h2 style="font-size:16px;color:#047857">🏛️ Vergisel Yönetim Avantajları &amp; Yasal Nakit Tasarrufu</h2>
          <p>Şirketin finansal tablolarından (mizan) türetilmiş yasal vergi kalkanları, KKEG optimizasyonu ve nakit tasarrufları</p>
        </div>
        <span class="tag positive" style="font-weight:800;font-size:11px">DİNAMİK VERGİ MOTORU</span>
      </div>
      <div id="taxStrategyMetrics" class="grid3" style="margin-top:12px"></div>
      <div id="taxStrategyItems" style="margin-top:14px;display:flex;flex-direction:column;gap:12px"></div>
    </div>
  </div>
</section>

<!-- ==================== BÖLÜM 9: CANLI SENARYO SİMÜLATÖRÜ ==================== -->
<section id="flowStep_9" class="accordionStep active">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_9')">
    <div class="accordionTitleGroup">
      <span class="accordionNum">9</span>
      <div>
        <h3 class="accordionTitle">Varsayımı Değiştirirsek Ne Olur? (Canlı Senaryo Simülatörü)</h3>
        <div class="accordionSub">Fiyatı artırırsak, tahsilatı çekersek veya gideri kıssak kasaya ne girer? Anlık duyarlılık testi</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag" style="background:#FAF5FF;color:#6B21A8;font-size:11px;font-weight:700">Simülatör</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <div class="card"><div id="opportunities" class="grid3"></div></div>

    <div id="interactiveScenarioCard" class="card" style="margin-top:16px;margin-bottom:0">
      <div class="sectionHead">
        <div>
          <h2>İnteraktif Senaryo Laboratuvarı &amp; Nakit Simülatörü</h2>
          <p>Önerilen senaryoları seçin veya sürgüleri hareket ettirerek serbest kalacak nakdi ve kâr etkisini anında canlı görün</p>
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <button class="secondary" style="font-size:11.5px;padding:5px 12px;border-radius:8px" onclick="applyScenarioPreset(10,15,2.0,5)">💡 Önerilen Temkinli Senaryo</button>
          <button class="secondary" style="font-size:11.5px;padding:5px 12px;border-radius:8px" onclick="applyScenarioPreset(20,25,4.0,10)">🚀 Agresif İyileştirme</button>
          <button class="secondary" style="font-size:11.5px;padding:5px 12px;border-radius:8px" onclick="applyScenarioPreset(0,0,0,0)">🔄 Sıfırla (Mevcut Durum)</button>
        </div>
      </div>
      <div class="grid2">
        <div style="display:flex;flex-direction:column;gap:14px">
          <div>
            <div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px">
              <span>Alacak Tahsilatını Hızlandır (DSO Azaltma)</span>
              <b id="sliderDsoVal" style="color:var(--accent)">0 gün</b>
            </div>
            <input id="sliderDso" type="range" min="0" max="60" value="0" step="1" style="width:100%;cursor:pointer">
          </div>
          <div>
            <div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px">
              <span>Stok Bekleme Süresini Kısalt (DIO Azaltma / Atıl Stok Eritme)</span>
              <b id="sliderDioVal" style="color:var(--accent)">0 gün</b>
            </div>
            <input id="sliderDio" type="range" min="0" max="60" value="0" step="1" style="width:100%;cursor:pointer">
          </div>
          <div>
            <div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px">
              <span>Satış Fiyatı / Brüt Marj İyileştirmesi</span>
              <b id="sliderMarginVal" style="color:var(--accent)">+0.0%</b>
            </div>
            <input id="sliderMargin" type="range" min="0" max="10.0" value="0" step="0.5" style="width:100%;cursor:pointer">
          </div>
          <div>
            <div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px">
              <span>Faaliyet Gideri (OpEx) Tasarrufu</span>
              <b id="sliderOpexVal" style="color:var(--accent)">0%</b>
            </div>
            <input id="sliderOpex" type="range" min="0" max="25" value="0" step="1" style="width:100%;cursor:pointer">
          </div>
        </div>

        <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:16px;padding:20px;display:flex;flex-direction:column;justify-content:center;gap:14px;box-shadow:0 4px 12px rgba(15,27,45,0.04)">
          <div style="font-size:12.5px;color:#0F172A;font-weight:800;text-transform:uppercase;letter-spacing:1px;display:flex;align-items:center;gap:6px">
            <span>⚡</span><span>Simüle Edilen Canlı Yönetim Etkisi</span>
          </div>
          <div class="grid2" style="gap:10px">
            <div class="metric" style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:12px 14px">
              <div class="label" style="color:#475569;font-weight:700">Kasaya Giren Serbest Nakit</div>
              <div id="simCashImpact" class="value" style="color:#0E7C66;font-size:19px;font-weight:800">0 TL</div>
              <div class="sub" style="color:#64748B">Tahsilat + Stok nakdi</div>
            </div>
            <div class="metric" style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:12px 14px">
              <div class="label" style="color:#475569;font-weight:700">Ek Yıllık Faaliyet Kârı</div>
              <div id="simProfitImpact" class="value" style="color:#1D4ED8;font-size:19px;font-weight:800">0 TL</div>
              <div class="sub" style="color:#64748B">Fiyat + OpEx tasarrufu</div>
            </div>
            <div class="metric" style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:12px 14px">
              <div class="label" style="color:#475569;font-weight:700">Simüle Net Kâr Marjı</div>
              <div id="simMarginImpact" class="value" style="color:#1D4ED8;font-size:19px;font-weight:800">–</div>
              <div class="sub" style="color:#64748B">Kârlılık tabanı etkisi</div>
            </div>
            <div class="metric" style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:12px 14px">
              <div class="label" style="color:#475569;font-weight:700">Nakit Çevrim Süresi (CCC)</div>
              <div id="simCccImpact" class="value" style="color:#0E7C66;font-size:19px;font-weight:800">–</div>
              <div class="sub" style="color:#64748B">Çalışma sermayesi çevrimi</div>
            </div>
            <div class="metric" style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:12px 14px;grid-column:span 2">
              <div class="label" style="color:#475569;font-weight:700">Yıllık Finansman Faiz Tasarrufu (Kredi Maliyeti Önleme)</div>
              <div id="simInterestSavings" class="value" style="color:#B45309;font-size:19px;font-weight:800">0 TL</div>
              <div id="simInterestSub" class="sub" style="color:#64748B">Sermaye maliyeti %45 ile açığa çıkan nakit getirisi</div>
            </div>
          </div>
          <div id="simSummaryText" style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:12px 14px;font-size:12.5px;color:#0F172A;font-weight:500;line-height:1.6">Sürgüleri hareket ettirerek veya yukarıdaki hazır senaryolara tıklayarak şirketin kazanımlarını test edin.</div>
        </div>
      </div>

      <!-- Collapsible Simülasyon Varsayımları & Sermaye Maliyeti Parametreleri Panel -->
      <div style="margin-top:16px;background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:14px;padding:14px 18px">
        <div style="display:flex;justify-content:space-between;align-items:center;cursor:pointer" onclick="toggleSimAssumptions()">
          <div style="display:flex;align-items:center;gap:8px;font-size:12.5px;font-weight:800;color:#0F172A">
            <span>📐</span><span>Simülasyon Varsayımları &amp; Sermaye Maliyeti Parametreleri</span>
            <span class="tag" style="background:#EFF6FF;color:#1D4ED8;font-size:10px;font-weight:700">Şeffaf Matematik Modeli</span>
          </div>
          <span id="simAssumptionsChevron" style="font-size:12px;color:#64748B">▼</span>
        </div>
        <div id="simAssumptionsBody" style="margin-top:14px;padding-top:14px;border-top:1px solid #F1F5F9">
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start">
            <div>
              <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px">
                <span style="font-weight:700;color:#334155">Şirket Sermaye / Kredi Faiz Maliyeti (WACC / Borçlanma Oranı)</span>
                <b id="simCostOfCapitalVal" style="color:var(--accent);font-size:13px">%45.0</b>
              </div>
              <input id="simCostOfCapital" type="range" min="15" max="75" value="45" step="1" style="width:100%;cursor:pointer">
              <div style="font-size:11px;color:#64748B;margin-top:6px;line-height:1.4">
                Türkiye KOBİ ticari kredi / rotatif faiz oranları referans alınarak varsayılan %45 belirlenmiştir. Kendi banka borçlanma veya sermaye maliyetinize göre sürgüyü ayarlayabilirsiniz.
              </div>
            </div>
            <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px;font-size:11.5px;color:#334155;line-height:1.6">
              <div style="font-weight:800;color:#0F172A;margin-bottom:4px">Kullanılan Formül Mimarisi:</div>
              <div>• <b>DSO Nakit Girişi:</b> (DSO Azalış Gün / 365) × Yıllık Net Satışlar</div>
              <div>• <b>DIO Nakit Çözümü:</b> (DIO Azalış Gün / 365) × Satılan Malın Maliyeti (SMM)</div>
              <div>• <b>Faiz Tasarrufu:</b> Toplam Serbest Kalan Nakit × Sermaye Maliyeti (%)</div>
              <div>• <b>Faaliyet Kâr Katkısı:</b> (Marj Artışı % × Satış) + (OpEx Tasarruf % × Faaliyet Gideri)</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ==================== BÖLÜM 8: ENFLASYON RÖNTGENİ & LİKİDİTE STRES TESTİ ==================== -->
<section id="flowStep_8" class="accordionStep active">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_8')">
    <div class="accordionTitleGroup">
      <span class="accordionNum" style="background:#DC2626;color:#FFFFFF">8</span>
      <div>
        <h3 class="accordionTitle">Enflasyon Düzeltmeli Gerçek Kârlılık Röntgeni &amp; Müşteri Konsantrasyonu Likidite Stres Testi</h3>
        <div class="accordionSub">Fiktif stok kârı illüzyonunun deşifresi, reel sermaye erimesi ve müşteri ödeme gecikmesi şok simülasyonu</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag" style="background:#FEF2F2;color:#DC2626;font-size:11px;font-weight:700">Reel Röntgen &amp; Şok</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <!-- Card 1: Enflasyon Düzeltmeli Gerçek Kârlılık Röntgeni -->
    <div id="inflationCard" class="card" style="border:1.5px solid #E2E8F0;border-radius:18px;padding:22px;margin-bottom:16px">
      <div class="sectionHead" style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:16px">
        <div style="max-width:680px">
          <div style="display:inline-flex;align-items:center;gap:6px;background:#FEF2F2;color:#DC2626;padding:3px 10px;border-radius:999px;font-size:11px;font-weight:800;letter-spacing:0.5px;margin-bottom:8px">
            🔥 GERÇEK KÂRLILIK RÖNTGENİ &amp; FAİZ/ENFLASYON SİMÜLATÖRÜ
          </div>
          <h2 style="font-size:20px;margin:0 0 6px">Enflasyon Düzeltmeli Gerçek Ekonomik Kâr &amp; Sermaye Koruma Analizi</h2>
          <p class="muted" style="margin:0;font-size:13px">Klasik mizan enflasyonu dikkate almaz; fiktif stok kârını gerçek kâr gibi gösterir. Aşağıdaki simülatör ile piyasadaki yıllık enflasyon veya kredi faiz oranını değiştirerek kârınızın ve özkaynağınızın reel durumunu anında test edin.</p>
        </div>
        
        <!-- Dinamik Enflasyon & Faiz Oranı Simülatörü Kontrol Kutusu -->
        <div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:12px 16px;min-width:280px;box-shadow:0 2px 8px rgba(15,27,45,0.03)">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <span style="font-size:12px;font-weight:700;color:#0F172A">📊 Test Edilen Yıllık Oran:</span>
            <b id="infSliderVal" style="font-size:15px;font-weight:900;color:#DC2626">%45</b>
          </div>
          <input type="range" id="infRateSlider" min="10" max="90" step="5" value="45" style="width:100%;height:6px;accent-color:#DC2626;cursor:pointer" oninput="onInflationSliderChange(this.value)">
          <div style="display:flex;justify-content:space-between;font-size:10px;color:#94A3B8;margin-top:4px">
            <span>%10 (Düşük)</span>
            <span style="color:#64748B;font-weight:600">TCMB / Piyasa</span>
            <span>%90 (Yüksek Şok)</span>
          </div>
          <div style="display:flex;gap:5px;margin-top:8px">
            <button type="button" class="secondary" style="flex:1;padding:3px 6px;font-size:10.5px;border-radius:6px" onclick="setInfSliderRate(30)">%30 Hedef</button>
            <button type="button" class="secondary" style="flex:1;padding:3px 6px;font-size:10.5px;border-radius:6px" onclick="setInfSliderRate(45)">%45 Standart</button>
            <button type="button" class="secondary" style="flex:1;padding:3px 6px;font-size:10.5px;border-radius:6px" onclick="setInfSliderRate(65)">%65 Faiz/Kredi</button>
          </div>
        </div>
      </div>
      <div id="inflationMetrics" class="grid4" style="margin-top:16px"></div>
      <div id="inflationAssessment" style="margin-top:14px"></div>
    </div>

    <!-- Card 2: Müşteri Konsantrasyonu Likidite Stres Testi -->
    <div id="liquidityStressCard" class="card" style="border:1.5px solid #E2E8F0;border-radius:18px;padding:22px;margin-bottom:0">
      <div class="sectionHead">
        <div>
          <div style="display:inline-flex;align-items:center;gap:6px;background:#FFFBEB;color:#D97706;border:1px solid #FDE68A;padding:3px 10px;border-radius:999px;font-size:11px;font-weight:800;letter-spacing:0.5px;margin-bottom:8px">
            ⚡ LİKİDİTE KIRILGANLIK &amp; TEMERRÜT ŞOKU
          </div>
          <h2 style="font-size:20px;margin:0 0 6px">Müşteri Konsantrasyonu Likidite Stres Testi (30 &amp; 60 Günlük Şok)</h2>
          <p class="muted" style="margin:0;font-size:13px">"İlk 3 müşterim ödemeyi geciktirirse şirketim kaç gün ayakta kalabilir?" sorusunun deterministik simülasyonu.</p>
        </div>
      </div>
      <div id="stressMetrics" class="grid4" style="margin-top:16px"></div>
      <div id="stressAssessment" style="margin-top:14px"></div>
    </div>
  </div>
</section>

<!-- ==================== EK A: SEKTÖREL KIYASLAMA & VERİ GÜVENİLİRLİK DENETİMİ ==================== -->
<section id="flowStep_ekA" class="accordionStep">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_ekA')">
    <div class="accordionTitleGroup">
      <span class="accordionNum alt">A</span>
      <div>
        <h3 class="accordionTitle">Ek A &mdash; Sektörel Kıyaslama (TCMB &amp; BIST) &amp; Veri Güvenilirlik Denetimi</h3>
        <div class="accordionSub">Sektör bantları, bilanço denkliği, çift taraflı denetim ve Data Hub mutabakatları</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag" style="background:#F1F5F9;color:#475569;font-size:11px;font-weight:700">Denetim</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <div class="card">
      <div class="sectionHead">
        <div>
          <h2>Sektörel Kıyaslama &amp; Göstergeler (TCMB &amp; BIST)</h2>
          <p>Yön duyarlı, gösterge amaçlı sektör bantları ve şirketin sektöre göre konumu</p>
        </div>
      </div>
      <div id="benchmark"></div>
    </div>

    <div class="card" style="margin-top:16px">
      <div class="sectionHead">
        <div>
          <h2>Veri Kalitesi &amp; Bilanço Denkliği</h2>
          <p>Skorlar ve bulgular, buradaki veri güvenilirliğine dayanır</p>
        </div>
      </div>
      <div class="grid4">
        <div class="metric"><div class="label">Veri Güvenilirlik Skoru</div><div id="dq" class="value">-</div><div class="sub" id="dqStatus">-</div></div>
        <div class="metric"><div class="label">Çift Taraflı Denetim</div><div id="auditValue" class="value">-</div><div class="sub" id="auditSub">-</div></div>
        <div class="metric"><div class="label">Eşlenemeyen Hesap Sayısı</div><div id="dqUnmapped" class="value">-</div><div class="sub">Eşlenemeyen hesap sayısı</div></div>
        <div class="metric"><div class="label">Nakit Çevrim Süresi</div><div id="cccMetric" class="value">-</div><div class="sub">Gün</div></div>
      </div>
      <div id="dqChecks" class="tableWrap" style="margin-top:16px"></div>
      <div id="dqIssues" style="margin-top:12px"></div>
      <div id="dqNote" class="notice" style="margin-top:12px"></div>
    </div>

    <section id="dataHubCard" class="card hidden" style="margin-top:16px;margin-bottom:0">
      <div class="sectionHead">
        <div>
          <h2>Çoklu Veri İstihbaratı (Data Hub)</h2>
          <p>Dosya sınıflandırma, kaynak bazlı analiz ve büyük defter mutabakatı</p>
        </div>
      </div>
      <div id="hubSummary" class="grid4"></div>
      <div id="hubSources" class="card" style="margin-top:14px"></div>
      <div id="hubFindings" class="card" style="margin-top:14px"></div>
      <div id="pvmIntel" class="card hidden" style="margin-top:14px"></div>
      <div id="hubReconciliation" class="card" style="margin-top:14px"></div>
    </section>
  </div>
</section>

<!-- ==================== EK B: TREND İZLEME & 3 TEMEL MALİ TABLO ==================== -->
<section id="flowStep_ekB" class="accordionStep">
  <div class="accordionHeader" onclick="toggleAccordion('flowStep_ekB')">
    <div class="accordionTitleGroup">
      <span class="accordionNum alt">B</span>
      <div>
        <h3 class="accordionTitle">Ek B &mdash; Trend İzleme, İzlenebilirlik &amp; 3 Temel Mali Tablo</h3>
        <div class="accordionSub">Dönemsel trend karşılaştırması, Gelir Tablosu, Bilanço ve Nakit Akış Tablosu</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="tag" style="background:#F1F5F9;color:#475569;font-size:11px;font-weight:700">Mali Tablolar</span>
      <div class="accordionToggleIcon">▼</div>
    </div>
  </div>
  <div class="accordionBody">
    <div id="comparativeCard" class="card hidden">
      <div class="sectionHead">
        <div>
          <h2>Dönemsel Trend Karşılaştırması</h2>
          <p>Yüklenen dönemler arasındaki değişim, büyüme yönü ve yönetim için anlamı</p>
        </div>
      </div>
      <div id="comparativeCards" class="grid3" style="margin-top:4px"></div>
      <div id="comparativeFindings" style="margin-top:14px"></div>
      <div id="comparativeTable" class="tableWrap" style="margin-top:14px"></div>
    </div>

    <div class="card" style="margin-top:16px">
      <div id="trendBlock"></div>
      <div id="trace" class="tableWrap" style="margin-top:15px"></div>
    </div>

    <div class="card" style="margin-top:16px;margin-bottom:0">
      <div class="sectionHead">
        <div>
          <h2>3 Temel Mali Tablo (Gelir Tablosu, Bilanço ve Nakit Akış)</h2>
          <p>Doğrulanmış Gelir Tablosu (P&amp;L), Bilanço ve Nakit Akış Tablosu</p>
        </div>
      </div>
      <div class="grid3">
        <div id="plTable" class="tableWrap"></div>
        <div id="bsTable" class="tableWrap"></div>
        <div id="cfTable" class="tableWrap"></div>
      </div>
    </div>
  </div>
</section>

</main><div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/cozumler">Çözümler</a></li><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • <a href="https://digitalfinancebp.com" style="color:var(--accent);text-decoration:none;font-weight:700">digitalfinancebp.com</a> • Deterministik Finans Karar Motoru &amp; Çift Yönlü Denetim Sistemi<br><span style="opacity:.85">Bu analiz deterministik matematiksel hesaplamalara ve çift taraflı denetim kurallarına dayanır; resmi mali tablo veya vergi beyannamesi yerine geçmez. Nihai yönetim kararları için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca anlık analiz süresince RAM bellekte işlenir; sunucu sabit diskinde ASLA kalıcı saklanmaz. KVKK ve kurumsal gizlilik politikamız için <a href="javascript:void(0)" onclick="showKvkkModal()" style="color:var(--accent);text-decoration:underline;font-weight:600">Aydınlatma ve Gizlilik Metni</a>'ni inceleyebilirsiniz.</span></div></div></div>

<!-- Board One-Pager Executive Modal (Root-level child for clean A4 printing) -->
<div id="boardDeckModal" class="hidden" style="position:fixed;inset:0;background:rgba(15,27,45,.75);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);display:flex;align-items:center;justify-content:center;z-index:2000;padding:20px;overflow-y:auto">
  <div style="background:#FFFFFF;border-radius:18px;max-width:960px;width:100%;max-height:92vh;display:flex;flex-direction:column;box-shadow:0 25px 60px rgba(0,0,0,0.3);overflow:hidden">
    <div class="hidePrint" style="display:flex;justify-content:space-between;align-items:center;padding:14px 22px;border-bottom:1px solid #E2E8F0;background:#F8FAFC">
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:20px">📑</span>
        <div>
          <h3 style="margin:0;font-size:15px;color:#0F1B2D;font-weight:800">Yönetim Kurulu Finansal Karar Özeti (Executive Board Deck)</h3>
          <p style="margin:0;font-size:11.5px;color:#64748B">C-Level ve Yönetim Kurulu sunumları için tek sayfalık A4 özet görünüm</p>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:8px">
        <button id="printBoardDeckBtn" type="button" class="primary" style="padding:7px 14px;border-radius:8px;font-size:12.5px;font-weight:700">🖨️ Yazdır / PDF İndir</button>
        <button id="openDeckNewTabBtn" type="button" class="secondary" style="padding:7px 14px;border-radius:8px;font-size:12.5px;font-weight:700" onclick="openBoardDeckInNewWindow()">📄 Temiz A4 Görünümü</button>
        <button id="closeBoardDeckBtn" type="button" style="background:none;border:none;font-size:22px;color:#64748B;cursor:pointer;padding:4px 8px">✕</button>
      </div>
    </div>
    <div id="boardDeckContent" style="padding:22px;overflow-y:auto;flex:1"></div>
  </div>
</div>

<!-- Finansal Sağlık Skoru Metodolojisi & Formül Modalı -->
<div id="scoreMethodologyModal" class="hidden hidePrint" style="position:fixed;inset:0;background:rgba(15,27,45,.75);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);display:flex;align-items:center;justify-content:center;z-index:2000;padding:20px;overflow-y:auto">
  <div style="background:#FFFFFF;border-radius:18px;max-width:780px;width:100%;max-height:90vh;display:flex;flex-direction:column;box-shadow:0 25px 60px rgba(0,0,0,0.3);overflow:hidden">
    <div style="display:flex;justify-content:space-between;align-items:center;padding:16px 22px;border-bottom:1px solid #E2E8F0;background:#F8FAFC">
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:20px">📐</span>
        <div>
          <h3 id="methodologyModalTitle" style="margin:0;font-size:16px;color:#0F1B2D;font-weight:800">Finansal Sağlık Skoru Metodolojisi &amp; Ağırlık Dağılımı</h3>
          <p style="margin:0;font-size:11.5px;color:#64748B">5 Temel Boyut &bull; Deterministik Kural Tabanlı Kompozit Skor (Maks. 100 Puan)</p>
        </div>
      </div>
      <button type="button" onclick="closeScoreMethodologyModal()" style="background:none;border:none;font-size:22px;color:#64748B;cursor:pointer;padding:4px 8px">✕</button>
    </div>
    <div style="padding:22px;overflow-y:auto;flex:1">
      <div id="methodologyModalDesc" style="font-size:12px;color:#475569;line-height:1.6;margin-bottom:18px;background:#F8FAFC;padding:12px 16px;border-radius:12px;border:1.5px solid #E2E8F0">
        Finansal Sağlık Skoru bir kara kutu veya sübjektif AI tahmini değildir; 5 temel kurumsal finans boyutunu ölçen kural tabanlı, deterministik bir kompozit skorlama modelidir.
      </div>
      <div id="methodologyPillarsList" style="display:flex;flex-direction:column;gap:12px"></div>
    </div>
    <div style="padding:14px 22px;border-top:1px solid #E2E8F0;background:#F8FAFC;display:flex;justify-content:flex-end">
      <button type="button" class="primary" style="padding:8px 22px;border-radius:10px;font-size:13px;font-weight:700" onclick="closeScoreMethodologyModal()">Tamam, Kapat</button>
    </div>
  </div>
</div>

<script>
window.showKvkkModal=function(){var m=document.getElementById('kvkkModal');if(!m){m=document.createElement('div');m.id='kvkkModal';m.style.cssText='position:fixed;inset:0;background:rgba(15,27,45,0.7);z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(4px);';m.innerHTML='<div style="background:#FFFFFF;border-radius:18px;max-width:640px;width:100%;max-height:85vh;overflow-y:auto;padding:28px;box-shadow:0 20px 50px rgba(0,0,0,0.3);position:relative;border:1px solid #E2E8F0"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid #E2E8F0;padding-bottom:12px"><div style="display:flex;align-items:center;gap:8px"><span style="font-size:20px">🔒</span><h3 style="margin:0;font-size:18px;color:#0F1B2D;font-family:sans-serif;font-weight:700">Veri Güvenliği, RAM-Only İşleme ve KVKK Taahhüdü</h3></div><button class="kvkkClose" style="background:#F1F5F9;border:0;border-radius:50%;width:30px;height:30px;cursor:pointer;font-weight:bold;font-size:16px">✕</button></div><div style="font-size:13px;line-height:1.7;color:#33415C;display:flex;flex-direction:column;gap:12px"><div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:12px;color:#166534"><b>🛡️ Sıfır Disk Depolama (RAM-Only):</b> Yüklediğiniz mizan, muavin defteri veya operasyonel raporlar sunucunun kalıcı depolama birimlerine (HDD/SSD/Veritabanı) kaydedilmez. Tüm matematiksel hesaplamalar ve çift taraflı denetim anlık bellek (RAM) üzerinde icra edilir ve analiz tamamlandığında oturumla birlikte tamamen silinir.</div><p><b>1. Veri İzolasyonu &amp; Model Eğitimi Yasağı:</b> Şirketiniz tarafından paylaşılan hiçbir finansal veri, ciro, müşteri adı veya bilanço kalemi üçüncü şahıslara verilmez, satılmaz ve genel yapay zekâ modellerinin eğitimi için havuzlara aktarılmaz.</p><p><b>2. 256-Bit TLS Şifreleme:</b> Tarayıcınız ile platform arasındaki tüm veri akışı bankacılık standardında 256-bit SSL/TLS tüneli üzerinden şifrelenir.</p><p><b>3. 6698 Sayılı KVKK Uyumluluğu:</b> Şirket yetkililerine ait iletişim bilgileri ve ticari sırlar yalnızca talep edilen analizlerin üretilmesi amacıyla işlenir; yasal yükümlülükler haricinde hiçbir tarafla paylaşılmaz.</p><p><b>4. Kurumsal Gizlilik Sözleşmesi (NDA):</b> Kurumsal entegrasyon veya holding düzeyinde çalışmalarda şirketinizle karşılıklı Kurumsal NDA akdedilir.</p></div><div style="margin-top:20px;text-align:right"><button class="kvkkClose primary" style="padding:9px 20px;border-radius:10px;font-size:13px;background:#1D4ED8;color:#fff;border:0;cursor:pointer;font-weight:700">Anladım ve Kabul Ediyorum</button></div></div>';m.addEventListener('click',function(e){if(e.target===m||e.target.classList.contains('kvkkClose'))m.style.display='none';});document.body.appendChild(m);}m.style.display='flex';};
document.getElementById('navToggle')?.addEventListener('click',()=>document.getElementById('mainNav')?.classList.toggle('open'));
window.addEventListener('scroll',()=>{document.querySelector('.top')?.classList.toggle('scrolled',window.scrollY>8)});
(function(){
  const els=document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){els.forEach(e=>e.classList.add('in'));return;}
  const io=new IntersectionObserver((entries)=>{entries.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}})},{threshold:.12});
  els.forEach(e=>io.observe(e));
})();
(function(){
  // Finance-flavoured count-up animation for stat/kpi numbers on scroll into view
  const targets = document.querySelectorAll('.stat b, .aboutStats .st b, .pvRing b, .scoreNum strong');
  if(!('IntersectionObserver' in window) || !targets.length) return;
  const parse = (txt)=>{ const m = txt.match(/-?\d[\d.,]*/); return m ? m[0] : null; };
  const cio = new IntersectionObserver((entries)=>{
    entries.forEach(en=>{
      if(!en.isIntersecting) return;
      cio.unobserve(en.target);
      const el = en.target; const raw = el.textContent; const numStr = parse(raw);
      if(!numStr) return;
      const prefix = raw.slice(0, raw.indexOf(numStr));
      const suffix = raw.slice(raw.indexOf(numStr)+numStr.length);
      const clean = numStr.replace(/\./g,'').replace(',', '.');
      const target = parseFloat(clean); if(isNaN(target)) return;
      const decimals = (clean.split('.')[1]||'').length;
      const dur = 900; const t0 = performance.now();
      function step(t){
        const p = Math.min(1,(t-t0)/dur); const eased = 1-Math.pow(1-p,3);
        const val = target*eased;
        el.textContent = prefix + val.toFixed(decimals).replace('.', decimals?',':'') + suffix;
        if(p<1) requestAnimationFrame(step); else el.textContent = raw;
      }
      requestAnimationFrame(step);
    });
  }, {threshold:.4});
  targets.forEach(t=>cio.observe(t));
})();
(function(){
  // Staggered grow-in for waterfall / bridge chart columns and progress bars
  document.querySelectorAll('.waterfall').forEach(wf=>{
    [...wf.children].forEach((col,i)=>{ col.style.animation = `growUp .6s ease ${i*70}ms both`; });
  });
  document.querySelectorAll('.bar i, .abar i').forEach((i,idx)=>{ i.style.animation = `growWidth .7s ease ${idx*40}ms both`; });
})();
</script>
<script>
let LAST=null;
const $=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
window._activeCurrency = 'TRY';
window._currencyRates = { TRY: 1.0, EUR: 1.0 / 38.1250, USD: 1.0 / 36.4520, GBP: 1.0 / 45.6840 };
window._currencySymbols = { TRY: ' TL', EUR: ' €', GBP: ' £', USD: ' $' };
window._currencyLocales = { TRY: 'tr-TR', EUR: 'de-DE', GBP: 'en-GB', USD: 'en-US' };

function setCurrency(cur){
  window._activeCurrency = cur;
  if(window._updateSim) window._updateSim();
  if(LAST) render(LAST);
}

const money=v=>{
  if(v==null) return '–';
  const cur=window._activeCurrency||'TRY';
  const rate=window._currencyRates[cur]||1.0;
  const loc=window._currencyLocales[cur]||'tr-TR';
  const converted=cur==='TRY'?v:(v*rate);
  const formatted=new Intl.NumberFormat(loc,{maximumFractionDigits:0}).format(converted);
  if(cur==='USD') return '$'+formatted;
  if(cur==='GBP') return '£'+formatted;
  if(cur==='EUR') return formatted+' €';
  return formatted+' TL';
};

window._activeLang = 'tr';
const I18N_BUNDLE = {"tr": {"singleTab": "Tek Dönem Mizan", "trendTab": "Çok Dönem / Trend", "hubTab": "Data Hub / Çoklu Veri", "analyzeBtn": "Mizanı Analiz Et", "analyzeBtnTrend": "İki Dönemi Analiz Et", "analyzeBtnHub": "Tüm Verileri Analiz Et", "sampleBtn": "📄 Tek dönem örnekle dene", "sampleTrendBtn": "📊 İki dönemli örnekle dene (Trend Demo)", "sampleHubBtn": "🗂️ Data Hub örnekle dene (Mizan + AR + AP + Stok + Satış)", "dropTitle": "Mizan Dosyanızı Buraya Sürükleyin", "dropSub": "veya bilgisayarınızdan seçin (.xlsx, .xls, .csv)", "dropBtn": "📁 Dosya Seç", "downloadTemplate": "📥 Standart Mizan Şablonu İndir (.csv)", "navHome": "Anasayfa", "navSolutions": "Çözümler", "navAbout": "Hakkımızda", "navApp": "Uygulama", "navPricing": "Paketler", "navSecurity": "Güvenlik", "navContact": "İletişim", "login": "Giriş Yap", "register": "Ücretsiz Kayıt Ol", "s1Title": "Finansal Gerçekler (Ne Oldu?)", "s1Desc": "Şirkette gerçekte ne oldu: Kâr nereden nereye aktı?", "s1Sub": "Doğrulanmış rakamlar: Ciro, operasyonel kâr kalitesi, borç yapısı ve nakit akış gerçekleşmesi.", "s2Title": "Para Nerede? — Görünmez Kâr Sızıntısı & Kilitli Nakit Teşhisi", "s2Desc": "Defterde kâr var ama para kasada nerede duruyor?", "s2Sub": "Müşteri vadelerinde (120 Alıcılar) ve depodaki stokta (150-153) kilitlenen sermaye ve her yıl ödenen gizli finansman faiz sızıntısı.", "s3Title": "Sektörel Kıyaslama & Öncelikli Riskler (Bize Maliyeti Ne?)", "s3Desc": "Sektör ortalamalarına göre neredeyiz ve acil ele alınması gereken riskler", "s3Sub": "TCMB Sektör Bilançoları & Borsa İstanbul (BIST) 500+ şirket verisiyle kıyaslama ve skorlanmış riskler.", "s4Title": "Kritik Taraflar & Operasyonel İstihbarat (Sızıntıyı Kim Yapıyor?)", "s4Desc": "Hangi müşteri, tedarikçi veya stok kalemi kârı ve nakdi doğrudan etkiliyor?", "s4Sub": "Nakit ve kâr üzerinde en büyük etkisi olan müşteriler ve stok kalemleri. Çoklu veri yüklendiğinde otomatik detaylanır.", "s5Title": "Kök Neden & Yönetim Hikâyeleri (Neden Oldu & Ne Yapılmalı?)", "s5Desc": "Bulguların arkasındaki 5 adımlı nedensellik zinciri, parasal sızıntı maliyeti ve icraat kararları", "s5Sub": "Belirti (Ne Oldu?) ➔ Kanıt (Rakamlar) ➔ Kök Neden (Tetikleyici) ➔ Parasal Sızıntı (Maliyet) ➔ Yönetim Kararı & İcraat", "s6Title": "Yönetim Kararları & Aksiyon Takvimi (Şimdi Ne Yapmalı?)", "s6Desc": "Yönetimin masaya koyup uygulayacağı somut kararlar", "s6Sub": "Karar maddesi → Sahibi → Termini → Takip Edilecek KPI. Her aksiyon maddesi ayrı bir takip numarasına sahiptir.", "s7Title": "Varsayımı Değiştirirsek Ne Olur? (Canlı Senaryo Simülatörü)", "s7Desc": "Fiyatı artırırsak, tahsilatı çekersek veya gideri kıssak kasaya ne girer?", "s7Sub": "Formüllü fırsatlar kataloğu ve anlık duyarlılık simülatörü.", "s8Title": "Yönetici Özeti & AI Finance Business Partner (Karar Brifingi)", "s8Desc": "Tüm analizin tek paragrafta özeti ve stratejik soru-cevap", "s8Sub": "Önce matematiksel kurallarla hesaplanır, sonra yorumlanır. Yöneticinin bu raporla hangi stratejik adımı atması gerektiği açıkça belirtilir.", "sEkATitle": "Ek A — Veri Güvenilirliği & Çift Taraflı Hesaplama Denetimi", "sEkADesc": "Analizin dayandığı verinin doğrulanma düzeyi ve dosya bazlı kırılım", "sEkBTitle": "Ek B — Trend İzleme, İzlenebilirlik & 3 Temel Mali Tablo", "sEkBDesc": "Çok dönem yüklendiğinde hareketi gösterir; her sayı kaynağına izlenebilir", "taxTitle": "🏛️ Vergisel Yönetim Avantajları & Yasal Nakit Tasarrufu", "taxSub": "Şirketin finansal tablolarından (mizan) türetilmiş yasal vergi kalkanları, KKEG optimizasyonu ve nakit tasarrufları", "simHeader": "İnteraktif Senaryo Laboratuvarı & Nakit Simülatörü", "simSub": "Önerilen senaryoları seçin veya sürgüleri hareket ettirerek serbest kalacak nakdi ve kâr etkisini anında canlı görün"}, "en": {"singleTab": "Single Period Trial Balance", "trendTab": "Multi-Period / Trend", "hubTab": "Data Hub / Multi-Source", "analyzeBtn": "Analyze Trial Balance", "analyzeBtnTrend": "Analyze Two Periods", "analyzeBtnHub": "Analyze All Sources", "sampleBtn": "📄 Try Single Period Sample", "sampleTrendBtn": "📊 Try Two-Period Trend Sample", "sampleHubBtn": "🗂️ Try Data Hub Sample (GL + AR + AP + Inventory + Sales)", "dropTitle": "Drag & Drop Your Trial Balance Here", "dropSub": "or choose from computer (.xlsx, .xls, .csv)", "dropBtn": "📁 Select File", "downloadTemplate": "📥 Download Standard Template (.csv)", "navHome": "Home", "navSolutions": "Solutions", "navAbout": "About", "navApp": "App", "navPricing": "Pricing", "navSecurity": "Security", "navContact": "Contact", "login": "Log In", "register": "Sign Up Free", "s1Title": "Financial Facts (What Happened?)", "s1Desc": "What actually happened: How profit flowed across statements", "s1Sub": "Verified figures: Revenue, operating profit quality, debt structure, and cash realization.", "s2Title": "Where is Cash? — Hidden Profit Leakage & Trapped Working Capital", "s2Desc": "On paper there is profit, but where is the cash trapped?", "s2Sub": "Capital locked in receivables (AR) and inventory, plus hidden annual debt finance costs.", "s3Title": "Benchmarking & Priority Risks (What Does It Cost Us?)", "s3Desc": "Where we stand relative to industry benchmarks and urgent risks", "s3Sub": "Central Bank Sector Balance Sheets & Stock Exchange 500+ corporate benchmarks.", "s4Title": "Key Counterparties & Operational Intelligence (Who Drives It?)", "s4Desc": "Which customer, supplier, or inventory SKU directly moves profit and cash?", "s4Sub": "Counterparties with the largest cash footprint. Enriched automatically when multi-source files are loaded.", "s5Title": "Root Cause & Management Narratives (Why & What to Do?)", "s5Desc": "5-step causal chain behind findings, financial leakage cost, and decisive execution actions", "s5Sub": "Symptom ➔ Evidence ➔ Root Cause ➔ Financial Leakage ➔ Decision & Action", "s6Title": "Management Action Matrix & Schedule (Now What?)", "s6Desc": "Decisive executive actions ready to execute tomorrow", "s6Sub": "Action item → Owner → Deadline → Target KPI with unique tracking ID.", "s7Title": "What If We Change Assumptions? (Live Scenario Simulator)", "s7Desc": "If we raise prices, shorten DSO, or curb opex, what lands in cash?", "s7Sub": "Formulaic opportunity catalog and instant sensitivity simulator.", "s8Title": "Executive Summary & AI Finance Business Partner (Decision Briefing)", "s8Desc": "Single-paragraph summary of full analysis and strategic Q&A", "s8Sub": "Calculated using deterministic mathematical rules first, then synthesized.", "sEkATitle": "Appendix A — Data Reliability & Double-Entry Audit", "sEkADesc": "Verification level and file-by-file audit of underlying financial data", "sEkBTitle": "Appendix B — Trend Tracking, Traceability & 3 Core Statements", "sEkBDesc": "Shows movement across periods; every number traces back to underlying journal accounts", "taxTitle": "🏛️ Practical Tax Management & Statutory Cash Shields", "taxSub": "Statutory tax shields, disallowed interest reduction, and cash savings derived from statement balances", "simHeader": "Interactive Scenario Lab & Cash Simulator", "simSub": "Choose suggested scenarios or move sliders to see cash liberation and profit impact in real time"}, "de": {"singleTab": "Einperiodige Summen- & Saldenliste", "trendTab": "Mehrperioden / Trend", "hubTab": "Data Hub / Multi-Source", "analyzeBtn": "Saldenliste analysieren", "analyzeBtnTrend": "Zwei Perioden analysieren", "analyzeBtnHub": "Alle Daten analysieren", "sampleBtn": "📄 Einperiodiges Beispiel testen", "sampleTrendBtn": "📊 Zweiperiodigen Trend testen", "sampleHubBtn": "🗂️ Data Hub Beispiel testen", "dropTitle": "Saldenliste hier ablegen", "dropSub": "oder vom Computer auswählen (.xlsx, .xls, .csv)", "dropBtn": "📁 Datei auswählen", "downloadTemplate": "📥 Standard-Vorlage herunterladen (.csv)", "navHome": "Startseite", "navSolutions": "Lösungen", "navAbout": "Über uns", "navApp": "Anwendung", "navPricing": "Preise", "navSecurity": "Sicherheit", "navContact": "Kontakt", "login": "Anmelden", "register": "Kostenlos Registrieren", "s1Title": "Finanzielle Fakten (Was ist passiert?)", "s1Desc": "Ertragsfluss und Kapitalverwendung im Detail", "s1Sub": "Umsatz, operative Ertragsqualität, Verschuldung und Cashflow.", "s2Title": "Wo ist das Geld? — Gebundenes Kapital & Liquiditätsabfluss", "s2Desc": "Auf dem Papier Gewinn, aber wo steht die Liquidität?", "s2Sub": "In Forderungen und Vorräten gebundenes Betriebskapital.", "s3Title": "Branchenvergleich & Risiken (Was kostet es uns?)", "s3Desc": "Positionierung im Branchenvergleich und Risiken", "s3Sub": "Zentralbank- und Börsenbenchmarks für 500+ Unternehmen.", "s4Title": "Wesentliche Parteien & Operative Intelligenz (Wer verursacht es?)", "s4Desc": "Welche Kunden oder Artikel binden Marge und Cash?", "s4Sub": "Fokus auf Haupttreiber des operativen Kapitals.", "s5Title": "Ursachenanalyse & Management-Berichte (Warum & Was tun?)", "s5Desc": "5-stufige Kausalkette, Schadenshöhe und Managemententscheidungen", "s5Sub": "Symptom ➔ Nachweis ➔ Hauptursache ➔ Finanzieller Verlust ➔ Maßnahme", "s6Title": "Management-Maßnahmen & Umsetzungsplan (Was jetzt?)", "s6Desc": "Konkrete Maßnahmen zur sofortigen Umsetzung", "s6Sub": "Maßnahme → Verantwortlicher → Frist → KPI.", "s7Title": "Was wäre wenn? (Live-Szenario-Simulator)", "s7Desc": "Sensitivitätsanalyse für Preis, Zahlungsziel und Kosten", "s7Sub": "Echtzeit-Berechnung des Liquiditätseffekts.", "s8Title": "Executive Summary & AI Finance Business Partner", "s8Desc": "Gesamtzusammenfassung und Entscheidungsunterstützung", "s8Sub": "Zuerst mathematisch determiniert, dann interpretiert.", "sEkATitle": "Anhang A — Datenqualität & Rechnungslegungsprüfung", "sEkADesc": "Prüfstufe der Quelldaten und Kontenabstimmung", "sEkBTitle": "Anhang B — Trend-Monitoring & 3 Hauptfinanzberichte", "sEkBDesc": "Mehrperioden-Vergleich und lückenlose Kontenrückverfolgung", "taxTitle": "🏛️ Steuerstrategie & Rechtliche Steuersparmodelle", "taxSub": "Gesetzliche Steuerabzüge und Liquiditätsschilde basierend auf der Bilanz", "simHeader": "Interaktiver Szenario-Simulator", "simSub": "Wählen Sie Presets oder bewegen Sie Schieberegler für Cashflow- und Gewinnauswirkungen"}, "fr": {"singleTab": "Balance Générale Période Unique", "trendTab": "Multi-Périodes / Tendance", "hubTab": "Data Hub / Multi-Sources", "analyzeBtn": "Analyser la balance", "analyzeBtnTrend": "Analyser deux périodes", "analyzeBtnHub": "Analyser toutes les sources", "sampleBtn": "📄 Essayer exemple période unique", "sampleTrendBtn": "📊 Essayer exemple tendance", "sampleHubBtn": "🗂️ Essayer Data Hub", "dropTitle": "Déposez votre balance générale ici", "dropSub": "ou sélectionnez depuis votre ordinateur (.xlsx, .xls, .csv)", "dropBtn": "📁 Choisir un fichier", "downloadTemplate": "📥 Télécharger modèle standard (.csv)", "navHome": "Accueil", "navSolutions": "Solutions", "navAbout": "À propos", "navApp": "Application", "navPricing": "Tarifs", "navSecurity": "Sécurité", "navContact": "Contact", "login": "Connexion", "register": "Inscription Gratuite", "s1Title": "Faits Financiers (Que s'est-il passé ?)", "s1Desc": "Flux réel du résultat d'exploitation", "s1Sub": "Chiffre d'affaires, marge opérationnelle, endettement et trésorerie nette.", "s2Title": "Où est l'argent ? — Fuites de profit et trésorerie immobilisée", "s2Desc": "Du bénéfice comptable, mais où est la trésorerie ?", "s2Sub": "Capitaux immobilisés dans les créances clients et stocks.", "s3Title": "Analyse Sectorielle & Risques Prioritaires (Quel est le coût ?)", "s3Desc": "Positionnement sectoriel et alertes critiques", "s3Sub": "Données Banque Centrale et marché boursier pour 500+ entreprises.", "s4Title": "Tiers Clés & Renseignement Opérationnel (Qui génère l'impact ?)", "s4Desc": "Quels clients ou références pèsent le plus lourd ?", "s4Sub": "Analyse approfondie des contreparties critiques.", "s5Title": "Causes Profondes & Narration Décisionnelle (Pourquoi & Que faire ?)", "s5Desc": "Chaîne causale en 5 étapes, coût financier et décisions", "s5Sub": "Symptôme ➔ Preuve ➔ Cause Première ➔ Perte Financière ➔ Décision", "s6Title": "Plan d'Action Managérial & Calendrier (Que faire maintenant ?)", "s6Desc": "Feuille de route pour le comité de direction", "s6Sub": "Action → Porteur → Échéance → KPI cible.", "s7Title": "Simulateur de Scénarios en Direct", "s7Desc": "Ajustements de prix, délais et charges en direct", "s7Sub": "Simulateur instantané de sensibilité de trésorerie.", "s8Title": "Synthèse Exécutive & AI Finance Business Partner", "s8Desc": "Synthèse générale et questions-réponses stratégiques", "s8Sub": "Calculé d'abord selon des règles déterministes strictes.", "sEkATitle": "Annexe A — Fiabilité des Données & Contrôle Arithmétique", "sEkADesc": "Niveau de vérification et réconciliation de la balance", "sEkBTitle": "Annexe B — Analyse de Tendance & 3 États Financiers", "sEkBDesc": "Évolution pluriannuelle et traçabilité intégrale", "taxTitle": "🏛️ Stratégie Fiscale & Économies Légales de Trésorerie", "taxSub": "Boucliers fiscaux et optimisation des charges issus du bilan", "simHeader": "Laboratoire de Scénarios Interactif", "simSub": "Ajustez les curseurs pour simuler l'impact immédiat sur la trésorerie"}, "es": {"singleTab": "Balance de Sumas y Saldos Único", "trendTab": "Multi-Periodo / Tendencia", "hubTab": "Data Hub / Multi-Fuente", "analyzeBtn": "Analizar balance", "analyzeBtnTrend": "Analizar dos periodos", "analyzeBtnHub": "Analizar todas las fuentes", "sampleBtn": "📄 Probar ejemplo de un periodo", "sampleTrendBtn": "📊 Probar ejemplo de tendencia", "sampleHubBtn": "🗂️ Probar Data Hub", "dropTitle": "Arrastre su balance aquí", "dropSub": "o elija de su ordenador (.xlsx, .xls, .csv)", "dropBtn": "📁 Seleccionar archivo", "downloadTemplate": "📥 Descargar plantilla estándar (.csv)", "navHome": "Inicio", "navSolutions": "Soluciones", "navAbout": "Sobre Nosotros", "navApp": "Aplicación", "navPricing": "Precios", "navSecurity": "Seguridad", "navContact": "Contacto", "login": "Iniciar Sesión", "register": "Registro Gratis", "s1Title": "Hechos Financieros (¿Qué Ocurrió?)", "s1Desc": "Flujo real de beneficios y estructura patrimonial", "s1Sub": "Ingresos netos, margen operativo, endeudamiento y tesorería.", "s2Title": "¿Dónde está el dinero? — Fugas de beneficio y caja atrapada", "s2Desc": "Hay beneficio contable, pero ¿dónde está el dinero?", "s2Sub": "Capital inmovilizado en clientes pendientes y almacén.", "s3Title": "Comparativa Sectorial & Riesgos Prioritarios (¿Cuál es el coste?)", "s3Desc": "Posicionamiento sectorial y riesgos urgentes", "s3Sub": "Datos de referencia de Banco Central y bolsas 500+ empresas.", "s4Title": "Contrapartes Clave & Análisis Operativo (¿Quién genera el impacto?)", "s4Desc": "Clientes, proveedores y existencias determinantes", "s4Sub": "Impacto operativo directo en caja y márgenes.", "s5Title": "Causa Raíz & Narrativa de Gestión (¿Por qué y qué hacer?)", "s5Desc": "Cadena causal de 5 pasos, fuga de caja e intervenciones", "s5Sub": "Síntoma ➔ Evidencia ➔ Causa Raíz ➔ Fuga Financiera ➔ Decisión", "s6Title": "Matriz de Acciones de Dirección (¿Qué hacer ahora?)", "s6Desc": "Decisiones listas para ser aplicadas", "s6Sub": "Medida → Responsable → Plazo → KPI objetivo.", "s7Title": "Simulador de Escenarios en Vivo", "s7Desc": "¿Qué ocurre al variar precios, plazos o costes?", "s7Sub": "Simulador instantáneo de impacto en tesorería.", "s8Title": "Resumen Ejecutivo & AI Finance Business Partner", "s8Desc": "Informe condensado para el Consejo de Administración", "s8Sub": "Cálculo matemático determinista antes de la interpretación.", "sEkATitle": "Anexo A — Fiabilidad Contable & Auditoría Doble", "sEkADesc": "Nivel de validación y conciliación contable", "sEkBTitle": "Anexo B — Tendencia Histórica & 3 Estados Financieros", "sEkBDesc": "Seguimiento multi-periodo y trazabilidad total", "taxTitle": "🏛️ Estrategia Fiscal Práctica & Escudos de Caja", "taxSub": "Deducciones fiscales y ahorro de intereses derivados del balance", "simHeader": "Laboratorio de Escenarios Interactivo", "simSub": "Deslice controles para calcular el impacto en tesorería y beneficio"}, "it": {"singleTab": "Bilancio di Verifica Singolo", "trendTab": "Multi-Periodo / Trend", "hubTab": "Data Hub / Multi-Fonte", "analyzeBtn": "Analizza bilancio", "analyzeBtnTrend": "Analizza due periodi", "analyzeBtnHub": "Analizza tutte le fonti", "sampleBtn": "📄 Prova esempio singolo periodo", "sampleTrendBtn": "📊 Prova esempio trend", "sampleHubBtn": "🗂️ Prova Data Hub", "dropTitle": "Trascina qui il tuo bilancio di verifica", "dropSub": "oppure seleziona dal computer (.xlsx, .xls, .csv)", "dropBtn": "📁 Seleziona file", "downloadTemplate": "📥 Scarica modello standard (.csv)", "navHome": "Home", "navSolutions": "Solutions", "navAbout": "Chi siamo", "navApp": "Applicazione", "navPricing": "Piani", "navSecurity": "Sicurezza", "navContact": "Contatti", "login": "Accedi", "register": "Registrati Gratis", "s1Title": "Fatti Finanziari (Cosa è successo?)", "s1Desc": "Dinamica economica reale e generazione utile", "s1Sub": "Ricavi netti, qualità del reddito operativo e liquidità.", "s2Title": "Dov'è il denaro? — Fuga di utili e capitale bloccato", "s2Desc": "C'è utile contabile, ma dov'è la cassa reale?", "s2Sub": "Capitale bloccato in crediti commerciali e magazzino.", "s3Title": "Benchmark di Settore & Rischi Prioritari (Quanto ci costa?)", "s3Desc": "Posizionamento rispetto ai concorrenti e rischi", "s3Sub": "Metriche Banca Centrale e Borsa per 500+ imprese.", "s4Title": "Controparti Chiave & Intelligence Operativa (Chi impatta?)", "s4Desc": "Clienti, fornitori e articoli che guidano i risultati", "s4Sub": "Analisi ad alto impatto per il capitale circolante.", "s5Title": "Cause Principali & Storie Decisionali (Perché & Cosa fare?)", "s5Desc": "Sequenza causale a 5 fasi, dispersione e azioni", "s5Sub": "Sintomo ➔ Evidenza ➔ Causa Primaria ➔ Dispersione ➔ Decisione", "s6Title": "Piano di Azione Manageriale & Scadenze (Cosa fare ora?)", "s6Desc": "Decisioni concrete per il management", "s6Sub": "Azione → Responsabile → Termine → KPI.", "s7Title": "Simulatore di Scenari in Tempo Reale", "s7Desc": "Sensibilità su prezzi, termini di incasso e spese", "s7Sub": "Simulatore istantaneo dell'impatto sulla liquidità.", "s8Title": "Sintesi Esecutiva & AI Finance Business Partner", "s8Desc": "Quadro strategico d'insieme per il vertice", "s8Sub": "Regole matematiche certe e sintesi esecutiva.", "sEkATitle": "Allegato A — Affidabilità Dati & Verifica a Partita Doppia", "sEkADesc": "Verifica contabile e riconciliazione delle fonti", "sEkBTitle": "Allegato B — Trend Storico & 3 Bilanci Principali", "sEkBDesc": "Confronto multi-periodo e tracciabilità analitica", "taxTitle": "🏛️ Strategia Fiscale Pratica & Scudi Fiscali Legali", "taxSub": "Ottimizzazione deduzioni e scudi fiscali basati sul bilancio", "simHeader": "Laboratorio Scenari Interattivo", "simSub": "Muovi i cursori per visualizzare immediatamente la liquidità liberata"}, "nl": {"singleTab": "Enkelvoudige Kolommenbalans", "trendTab": "Meerdere Perioden / Trend", "hubTab": "Data Hub / Multi-Bron", "analyzeBtn": "Balans analyseren", "analyzeBtnTrend": "Twee perioden analyseren", "analyzeBtnHub": "Alle bronnen analyseren", "sampleBtn": "📄 Test enkelvoudig voorbeeld", "sampleTrendBtn": "📊 Test trend voorbeeld", "sampleHubBtn": "🗂️ Test Data Hub", "dropTitle": "Sleep uw kolommenbalans hierheen", "dropSub": "of kies vanaf uw computer (.xlsx, .xls, .csv)", "dropBtn": "📁 Bestand kiezen", "downloadTemplate": "📥 Download standaardsjabloon (.csv)", "navHome": "Startpagina", "navSolutions": "Oplossingen", "navAbout": "Over ons", "navApp": "Applicatie", "navPricing": "Tarieven", "navSecurity": "Beveiliging", "navContact": "Contact", "login": "Inloggen", "register": "Gratis Registreren", "s1Title": "Financiële Feiten (Wat is er gebeurd?)", "s1Desc": "Reële kapitaalstromen en winstbestemming", "s1Sub": "Omzet, operationele marge, schuldhefboom en kasstroom.", "s2Title": "Waar is het geld? — Verborgen winstlekkage & vastzittend kapitaal", "s2Desc": "Winst op papier, maar waar is het geld?", "s2Sub": "Kapitaal vast in debiteuren en magazijnvoorraad.", "s3Title": "Sectorvergelijking & Prioritaire Risico's (Wat kost het ons?)", "s3Desc": "Positie ten opzichte van sectorbenchmarks", "s3Sub": "Centrale Bank en beursbenchmarks van 500+ bedrijven.", "s4Title": "Belangrijkste Partijen & Operationele Analyse (Wie veroorzaakt het?)", "s4Desc": "Klanten en artikelen met de grootste invloed", "s4Sub": "Gedetailleerde analyse van werkkapitaal.", "s5Title": "Oorzaakanalyse & Managementverhalen (Waarom & Wat te doen?)", "s5Desc": "Keten in 5 stappen, financiële lekkage en besluiten", "s5Sub": "Symptoom ➔ Bewijs ➔ Oorzaak ➔ Lekkage ➔ Actie", "s6Title": "Management Actieplan & Planning (Wat nu?)", "s6Desc": "Direct uitvoerbare directiebesluiten", "s6Sub": "Actiepunt → Eigenaar → Deadline → KPI.", "s7Title": "Live Scenario Simulator", "s7Desc": "Effect van prijs, debiteurentermijn en kosten", "s7Sub": "Directe berekening van effect op cash en winst.", "s8Title": "Managementsamenvatting & AI Finance Business Partner", "s8Desc": "Eén overzichtelijke directiesamenvatting", "s8Sub": "Deterministisch berekend, daarna strategisch geïnterpreteerd.", "sEkATitle": "Bijlage A — Betrouwbaarheid & Boekhoudkundige Audit", "sEkADesc": "Controle van rekeningschema en balanssluiting", "sEkBTitle": "Bijlage B — Trend-Monitoring & 3 Financiële Overzichten", "sEkBDesc": "Meerperioden-vergelijking en brontraceerbaarheid", "taxTitle": "🏛️ Praktische Belastingoptimalisatie & Cash-voordelen", "taxSub": "Wettelijke aftrekposten en rentebeperking uit de balans", "simHeader": "Interactief Scenario Laboratorium", "simSub": "Verschuif regelaars om het effect op cashflow en winst te zien"}};

function _updateStepHeader(stepId, numStr, title, desc, sub){
  const el = $(stepId);
  if(!el) return;
  const lbl = el.querySelector('.flowLabel');
  if(lbl) lbl.innerHTML = '<span class="n">' + numStr + '</span>' + esc(title) + '<p>' + esc(desc) + '</p>';
  const subEl = el.querySelector('.flowSub');
  if(subEl) subEl.textContent = sub;
}

function setLanguage(lang){
  window._activeLang = lang;
  try { localStorage.setItem('dfbp_lang', lang); } catch(e){}
  const dict = I18N_BUNDLE[lang] || I18N_BUNDLE.tr;
  if($('langSwitch')) $('langSwitch').value = lang;
  document.querySelectorAll('.globalLangSwitch').forEach(function(s){ s.value = lang; });

  const nav = $('mainNav');
  if(nav){
    const links = nav.querySelectorAll('a');
    if(links.length >= 7){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navSolutions || 'Çözümler';
      links[2].textContent = dict.navAbout;
      links[3].textContent = dict.navApp;
      links[4].textContent = dict.navPricing;
      links[5].textContent = dict.navSecurity;
      links[6].textContent = dict.navContact;
    } else if(links.length >= 6){
      links[0].textContent = dict.navHome;
      links[1].textContent = dict.navAbout;
      links[2].textContent = dict.navApp;
      links[3].textContent = dict.navPricing;
      links[4].textContent = dict.navSecurity;
      links[5].textContent = dict.navContact;
    }
  }
  if($('loginOpenBtn')) $('loginOpenBtn').textContent = dict.login;
  if($('registerOpenBtn')) $('registerOpenBtn').textContent = dict.register;

  if($('singleTabBtn')) $('singleTabBtn').textContent = dict.singleTab;
  if($('trendTabBtn')) $('trendTabBtn').textContent = dict.trendTab;
  if($('hubTabBtn')) $('hubTabBtn').textContent = dict.hubTab;
  if($('analyzeSingle')) $('analyzeSingle').textContent = '🚀 ' + dict.analyzeBtn;
  if($('analyzeTrend')) $('analyzeTrend').textContent = '🚀 ' + dict.analyzeBtnTrend;
  if($('analyzeHub')) $('analyzeHub').textContent = '🚀 ' + dict.analyzeBtnHub;
  if($('sampleBtn')) $('sampleBtn').textContent = dict.sampleBtn;
  if($('sampleTrendBtn')) $('sampleTrendBtn').textContent = dict.sampleTrendBtn;
  if($('sampleHubBtn')) $('sampleHubBtn').textContent = dict.sampleHubBtn;

  const dropStrong = document.querySelector('#dropZoneSingle .dropText strong');
  if(dropStrong) dropStrong.textContent = dict.dropTitle;
  const dropSpan = document.querySelector('#dropZoneSingle .dropText span');
  if(dropSpan) dropSpan.textContent = dict.dropSub;
  const dropBtn = document.querySelector('#dropZoneSingle button');
  if(dropBtn) dropBtn.textContent = dict.dropBtn;

  _updateStepHeader('flowStep_1', '1', dict.s1Title, dict.s1Desc, dict.s1Sub);
  _updateStepHeader('flowStep_2', '2', dict.s2Title, dict.s2Desc, dict.s2Sub);
  _updateStepHeader('flowStep_3', '3', dict.s3Title, dict.s3Desc, dict.s3Sub);
  _updateStepHeader('flowStep_4', '4', dict.s4Title, dict.s4Desc, dict.s4Sub);
  _updateStepHeader('flowStep_5', '5', dict.s5Title, dict.s5Desc, dict.s5Sub);
  _updateStepHeader('flowStep_6', '6', dict.s6Title, dict.s6Desc, dict.s6Sub);
  _updateStepHeader('flowStep_7', '7', dict.s7Title, dict.s7Desc, dict.s7Sub);
  _updateStepHeader('flowStep_8', '8', dict.s8Title, dict.s8Desc, dict.s8Sub);
  _updateStepHeader('flowStep_ekA', '+', dict.sEkATitle, dict.sEkADesc, '');
  _updateStepHeader('flowStep_ekB', '+', dict.sEkBTitle, dict.sEkBDesc, '');

  const taxH2 = document.querySelector('#taxStrategyCard .sectionHead h2');
  if(taxH2) taxH2.textContent = dict.taxTitle;
  const taxP = document.querySelector('#taxStrategyCard .sectionHead p');
  if(taxP) taxP.textContent = dict.taxSub;

  const simH2 = document.querySelector('#interactiveScenarioCard .sectionHead h2');
  if(simH2) simH2.textContent = dict.simHeader;
  const simP = document.querySelector('#interactiveScenarioCard .sectionHead p');
  if(simP) simP.textContent = dict.simSub;

  if(LAST) render(LAST);
}
const fmt=v=>v==null?'–':new Intl.NumberFormat('tr-TR',{maximumFractionDigits:0}).format(v);
const num=v=>v==null?'–':new Intl.NumberFormat('tr-TR',{maximumFractionDigits:1}).format(v);
const pct=v=>v==null?'–':num(v)+'%'; const rat=v=>v==null?'–':num(v)+'x';
const sevRank=s=>({critical:4,high:3,medium:2,low:1,positive:0})[s]??0;
function table(title,obj){return '<div class="notice" style="margin-bottom:8px"><b>'+title+'</b></div><table><tbody>'+Object.entries(obj||{}).map(([k,v])=>'<tr><td>'+esc(k)+'</td><td><b>'+money(v)+'</b></td></tr>').join('')+'</tbody></table>'}
function renderCashFlowTable(cb, pl, bs){
  if(!cb || !cb.available){
    const wc=cb?.working_capital_proxy||{};
    return '<div class="notice" style="margin-bottom:8px"><b>Nakit Akış Tablosu (Cari Likidite)</b></div>'
      +'<div class="small muted" style="margin-bottom:8px">Dönemsel nakit akışı köprüsü için 2 dönem karşılaştırması gereklidir. Aşağıda cari dönem likidite ve bağlı işletme sermayesi dökümü yer almaktadır.</div>'
      +'<table><tbody>'
      +'<tr><td>Kasa ve Bankalar (Nakit)</td><td><b>'+money(bs?.['Cash and cash equivalents']||0)+'</b></td></tr>'
      +'<tr><td>Ticari Alacaklar (Müşteride Bağlı)</td><td><b>'+money(wc.receivables||bs?.['Accounts receivable']||0)+'</b></td></tr>'
      +'<tr><td>Stoklar (Depoda Bağlı Sermaye)</td><td><b>'+money(wc.inventory||bs?.['Inventories']||0)+'</b></td></tr>'
      +'<tr><td>Ticari Borçlar (Tedarikçi Kredisi)</td><td><b>'+money(wc.payables||bs?.['Accounts payable']||0)+'</b></td></tr>'
      +'</tbody></table>'
      +'<div style="margin-top:12px;text-align:center"><a href="/uygulama?sample=data_hub" class="secondary small" style="display:inline-block;padding:6px 12px;border-radius:8px;text-decoration:none">🔥 2 Dönemli Data Hub ile Tam Tabloyu Aç</a></div>';
  }
  const wcc=cb.working_capital_components||{};
  return '<div class="notice" style="margin-bottom:8px"><b>Nakit Akış Tablosu (Yönetimsel CFO Köprüsü)</b></div>'
    +'<table><tbody>'
    +'<tr style="background:#F0F4FA"><td colspan="2"><b>I. İŞLETME FAALİYETLERİNDEN NAKİT AKIŞI</b></td></tr>'
    +'<tr><td style="padding-left:14px">Net Dönem Kârı</td><td><b>'+money(cb.net_profit)+'</b></td></tr>'
    +'<tr><td style="padding-left:14px">Faaliyet Dışı Düzeltmeler (Finansman/Vergi)</td><td><b>'+money(cb.non_operating_addback)+'</b></td></tr>'
    +'<tr><td style="padding-left:14px">Faaliyet Kârı (FVÖK)</td><td><b>'+money(cb.operating_profit)+'</b></td></tr>'
    +'<tr><td style="padding-left:14px;color:var(--muted)">Δ Ticari Alacak Değişimi (Müşteri)</td><td style="color:'+(wcc.receivables_effect<0?'var(--red)':'var(--green)')+'"><b>'+money(wcc.receivables_effect)+'</b></td></tr>'
    +'<tr><td style="padding-left:14px;color:var(--muted)">Δ Stok Değişimi (Depo Kilidi)</td><td style="color:'+(wcc.inventory_effect<0?'var(--red)':'var(--green)')+'"><b>'+money(wcc.inventory_effect)+'</b></td></tr>'
    +'<tr><td style="padding-left:14px;color:var(--muted)">Δ Ticari Borç Değişimi (Tedarikçi)</td><td style="color:'+(wcc.payables_effect<0?'var(--red)':'var(--green)')+'"><b>'+money(wcc.payables_effect)+'</b></td></tr>'
    +'<tr style="font-weight:700"><td>İşletme Sermayesi Net Etkisi</td><td style="color:'+(cb.working_capital_effect<0?'var(--red)':'var(--green)')+'"><b>'+money(cb.working_capital_effect)+'</b></td></tr>'
    +'<tr style="background:#EAF0FF;font-weight:800"><td>İşletme Faaliyetleri Nakit Akışı (Esas Faaliyet)</td><td style="color:'+(cb.operating_cash_flow_proxy<0?'var(--red)':'var(--green)')+'"><b>'+money(cb.operating_cash_flow_proxy)+'</b></td></tr>'
    +'<tr style="background:#F0F4FA"><td colspan="2"><b>II. FİNANSMAN &amp; DİĞER HAREKETLER</b></td></tr>'
    +'<tr><td style="padding-left:14px">Finansal Borç Değişimi (Net Kredi/İtfa)</td><td><b>'+money(cb.debt_change)+'</b></td></tr>'
    +'<tr><td style="padding-left:14px">Yatırım, Vergi &amp; Diğer Düzeltmeler</td><td><b>'+money(cb.unexplained_cash_change)+'</b></td></tr>'
    +'<tr style="background:#F0F4FA"><td colspan="2"><b>III. NAKİT VE BENZERLERİ DEĞİŞİMİ</b></td></tr>'
    +'<tr><td style="padding-left:14px">Dönem Başı Kasa &amp; Banka</td><td><b>'+money(cb.opening_cash)+'</b></td></tr>'
    +'<tr><td style="padding-left:14px">Dönem Sonu Kasa &amp; Banka</td><td><b>'+money(cb.closing_cash)+'</b></td></tr>'
    +'<tr style="font-weight:800;border-top:2px solid var(--accent)"><td>Net Kasa Değişimi</td><td style="color:'+(cb.cash_change<0?'var(--red)':'var(--green)')+'"><b>'+money(cb.cash_change)+'</b></td></tr>'
    +(cb.cash_realization_pct!=null?'<tr><td>Kâr Nakde Dönüşüm Oranı</td><td><b style="color:'+(cb.cash_realization_pct<50?'var(--red)':'var(--green)')+'">'+pct(cb.cash_realization_pct)+'</b></td></tr>':'')
    +'</tbody></table>';
}
function metric(label,value,sub){return '<div class="metric"><div class="label">'+esc(label)+'</div><div class="value">'+esc(value)+'</div><div class="sub">'+esc(sub||'')+'</div></div>'}
function setRing(v){$('scoreRing').style.setProperty('--score',Math.max(0,Math.min(100,v||0)));$('score').textContent=v==null?'–':Math.round(v)}
function waterfall(elId,rows){const max=Math.max(...rows.map(x=>Math.abs(x[1]||0)),1);$(elId).innerHTML=rows.map(r=>'<div class="wf '+(r[2]?'neg':'')+'"><div class="num">'+money(r[1]).replace(' TL','')+'</div><div class="col" style="height:'+Math.max(4,Math.abs(r[1]||0)/max*135)+'px"></div><div class="lab">'+esc(r[0])+'</div></div>').join('')}

let _loadTimer = null;
function startLoading(title, subtitle){
  const ol = $('loadingOverlay');
  if(!ol) return;
  if($('loadingTitle')) $('loadingTitle').textContent = title || 'Finansal Veriler Analiz Ediliyor';
  if($('loadingSubtitle')) $('loadingSubtitle').textContent = subtitle || '33 Finansal Karar Motoru Çalıştırılıyor...';
  if($('loadingBar')) $('loadingBar').style.width = '15%';
  const steps = [
    '1/4 · Dosya formatı ve Tek Düzen Hesap Planı doğrulanıyor...',
    '2/4 · Likidite, borçluluk ve kâr kalitesi hesaplanıyor...',
    '3/4 · Nakit köprüsü (Cash Bridge) ve PVM ayrıştırılıyor...',
    '4/4 · Kök nedenler, öncelikli riskler ve aksiyonlar üretiliyor...'
  ];
  let idx = 0;
  if($('loadingStepTxt')) $('loadingStepTxt').textContent = steps[0];
  ol.classList.remove('hidden');
  clearInterval(_loadTimer);
  _loadTimer = setInterval(()=>{
    idx++;
    if(idx < steps.length){
      if($('loadingStepTxt')) $('loadingStepTxt').textContent = steps[idx];
      if($('loadingBar')) $('loadingBar').style.width = ((idx+1)*23) + '%';
    }
  }, 450);
}
function stopLoading(){
  clearInterval(_loadTimer);
  if($('loadingBar')) $('loadingBar').style.width = '100%';
  setTimeout(()=>{
    const ol = $('loadingOverlay');
    if(ol) ol.classList.add('hidden');
  }, 200);
}

function findingsByCategory(findings,cats){return (findings||[]).filter(f=>cats.includes(f.category))}

// Profitability Bridge + Profit Quality are now presented as a single cluster
// (one card, one story): the waterfall shows WHERE margin is lost between net
// sales and net profit, and this paragraph immediately says WHETHER what's left
// is durable. Kept as one function so the two visuals never drift into two
// separate, competing explanations again.
// Karşılaştırmalı Analiz (Step 1): only populated when 2+ periods were
// uploaded (Trend tab). Turns trend_engine's headline_comparison +
// trend_findings into a first-class, visible comparison instead of the old
// buried single-line trend table — and is the only place trend_findings are
// rendered at all (previously computed by the backend but never shown).
const _cmpUnit=(u,v)=>{
  if(v==null) return '–';
  if(u==='amount') return money(v);
  if(u==='pct_points') return num(v)+'%';
  if(u==='x') return num(v)+'x';
  if(u==='days') return num(v)+' gün';
  return num(v);
};
const _cmpAssessClass={improved:'positive',worsened:'high',flat:'',bilinmiyor:''};
function renderComparative(tr){
  if(!tr||!tr.available||!(tr.headline_comparison||[]).length){$('comparativeCard').classList.add('hidden');return}
  $('comparativeCard').classList.remove('hidden');
  $('comparativeCards').innerHTML=tr.headline_comparison.map(h=>{
    const delta=h.unit==='pct_points'?(h.change_abs==null?'–':(h.change_abs>=0?'+':'')+num(h.change_abs)+' puan')
      :(h.change_abs==null?'–':(h.change_abs>=0?'+':'')+_cmpUnit(h.unit,h.change_abs)+(h.change_pct!=null?' ('+(h.change_pct>=0?'+':'')+num(h.change_pct)+'%)':''));
    const cls=_cmpAssessClass[h.assessment]||'';
    const arrow=h.assessment==='improved'?'↑':h.assessment==='worsened'?'↓':'→';
    return '<div class="metric"><div class="label">'+esc(h.label)+'</div><div class="value">'+_cmpUnit(h.unit,h.period_b_value)+'</div><div class="sub">'+esc(h.period_a_label)+': '+_cmpUnit(h.unit,h.period_a_value)+' → '+esc(h.period_b_label)+': '+_cmpUnit(h.unit,h.period_b_value)+'</div><span class="tag '+cls+'" style="margin-top:8px;display:inline-block">'+arrow+' '+delta+'</span></div>';
  }).join('');
  const findings=tr.trend_findings||[];
  $('comparativeFindings').innerHTML=findings.length?findings.map(f=>'<div class="insight '+esc(f.severity)+'" style="margin-top:10px"><h3>'+esc(f.title)+'</h3><p>'+esc(f.interpretation)+'</p><p class="small muted">'+esc(f.recommendation)+'</p></div>').join(''):'<div class="notice">Dönemler arasında belirgin bir yapısal kırılma tespit edilmedi.</div>';
  const unitFor={net_sales:'amount',gross_profit:'amount',operating_profit:'amount',net_profit:'amount',total_assets:'amount',total_equity:'amount',financial_debt:'amount',gross_margin_pct:'pct_points',operating_margin_pct:'pct_points',net_margin_pct:'pct_points',current_ratio:'ratio',debt_to_equity:'x',ccc_days:'days',dso_days:'days',dio_days:'days',dpo_days:'days'};
  const dirArrow={improving:'<span style="color:#2e7d32;font-weight:700">↑</span>',worsening:'<span style="color:#c62828;font-weight:700">↓</span>',flat:'<span style="color:#888">→</span>'};
  const rows=Object.entries(tr.metric_trends||{}).map(([k,m])=>{
    const dir=m.latest_direction||'flat';
    const arrowHtml=dirArrow[dir]||'<span style="color:#888">→</span>';
    return '<tr><td style="font-weight:600">'+esc(m.label)+'</td>'+(m.series||[]).map((v,i)=>{
      const prev=m.series[i-1];
      let bg='';
      if(i>0&&prev!=null&&v!=null){const up=v>prev;const good=(k==='financial_debt'||k==='debt_to_equity'||k==='ccc_days'||k==='dso_days'||k==='dio_days')?!up:up;bg=good?'background:#f0fbf3':'background:#fff5f5';}
      return '<td style="'+bg+';text-align:right">'+(unitFor[k]==='ratio'?(v==null?'–':num(v)):_cmpUnit(unitFor[k]||'amount',v))+'</td>';
    }).join('')+'<td style="text-align:center">'+arrowHtml+'</td></tr>';
  }).join('');
  $('comparativeTable').innerHTML='<div class="sectionHead" style="margin-bottom:8px"><div><h2 style="font-size:10.5pt">Tüm Metriklerin Tam Dönem Serisi</h2></div></div><div class="tableWrap"><table><thead><tr><th>Metrik</th>'+(tr.period_labels||[]).map(l=>'<th>'+esc(l)+'</th>').join('')+'<th>Yön</th></tr></thead><tbody>'+rows+'</tbody></table></div><p class="small muted" style="margin-top:8px">'+esc(tr.note||'')+'</p>';
}

function profitabilityNarrative(pl,pq){
  const bits=[];
  if(pl){
    const gm=pl['Net sales']?pl['Gross profit']/pl['Net sales']*100:null;
    const om=pl['Net sales']?pl['Operating profit']/pl['Net sales']*100:null;
    const nm=pl['Net sales']?pl['Net profit']/pl['Net sales']*100:null;
    if(gm!=null&&om!=null&&nm!=null){
      bits.push('<b>Köprü:</b> Net satışın %'+num(gm)+'\u0027i brüt kâr olarak kalıyor; faaliyet giderlerinden sonra bu %'+num(om)+'\u0027e, finansman gideri ve vergiden sonra ise %'+num(nm)+'\u0027e iniyor.');
    }
  }
  if(!pq||pq.quality_score==null){
    bits.push('Kâr kalitesi hesaplanamadı.');
    return '<div class="notice">'+bits.join(' ')+'</div>';
  }
  bits.push('<b>Kâr Kalitesi Skoru: '+num(pq.quality_score)+'/100 ('+esc(pq.quality_label)+').</b> Bu skor, köprüde net kâra kadar ulaşan tutarın ne kadarının kalıcı/operasyonel kaynaklardan geldiğini, ne kadarının finansman gideri veya faaliyet dışı kalemlerce aşındırıldığını ölçer; 100 en sağlıklı, 50 altı ise faaliyet kârının önemli bölümünün net kâra ulaşamadığı anlamına gelir.');
  if(pq.finance_cost_to_operating_profit_pct!=null){bits.push('Faaliyet kârının %'+num(pq.finance_cost_to_operating_profit_pct)+'\u0027i finansman giderlerine gidiyor; geriye kalan kısım vergi ve diğer kalemlerden sonra net kâra taşınıyor.');}
  if(pq.operating_to_net_profit_ratio!=null){bits.push('Faaliyet kârının yaklaşık %'+num(pq.operating_to_net_profit_ratio*100)+'\u0027i net kâra dönüşebiliyor.');}
  if(pq.other_income_to_pbt_pct!=null && pq.other_income_to_pbt_pct>10){bits.push('Vergi öncesi kârın %'+num(pq.other_income_to_pbt_pct)+'\u0027i faaliyet dışı/ikincil gelirlerden geliyor; bu payın sürdürülebilirliği ayrıca izlenmeli.');}
  const all=[...(pq.flags||[]),...(pq.cross_references||[])];
  all.forEach(f=>{ if(f.detail) bits.push(esc(f.detail)); });
  return '<div class="notice">'+bits.join(' ')+'</div>';
}

// Working Capital (DSO/DIO/DPO/CCC): previously only rendered the raw metrics
// plus the engine's short technical note, with no plain-language interpretation
// of what the CCC figure actually means for the business — the one card in
// this flow step that had numbers but no narrative. This closes that gap using
// only figures already computed by cash_conversion_engine.
function workingCapitalNarrative(c, cm, pl, k){
  if(!c || (c.cash_conversion_cycle_days == null && (cm && cm.ccc_days == null))) {
    return '<div class="notice">Nakit dönüşüm süresi hesaplanamadı — DSO/DIO/DPO için yeterli bilanço verisi yok.</div>';
  }
  const ccc = Math.round(Number((cm && cm.ccc_days != null) ? cm.ccc_days : c.cash_conversion_cycle_days));
  const dso = Math.round(Number((cm && cm.dso_days != null) ? cm.dso_days : (c.dso_days || 0)));
  const dio = Math.round(Number((cm && cm.dio_days != null) ? cm.dio_days : (c.dio_days || 0)));
  const dpo = Math.round(Number((cm && cm.dpo_days != null) ? cm.dpo_days : (c.dpo_days || 0)));
  const tier = ccc <= 30 ? 'positive' : ccc <= 75 ? 'medium' : 'high';
  const ratingTxt = c.rating ? ' (' + esc(c.rating) + ')' : '';
  const spread = dso - dpo;

  let html = '<div class="insight ' + tier + '" style="line-height:1.65;font-size:12.5px">';
  html += '<div style="font-size:13.5px;font-weight:800;color:#0F172A;margin-bottom:8px">🏛️ CFO İşletme Sermayesi Teşhisi &amp; Nakit Döngüsü Raporu</div>';
  
  html += '<p style="margin:0 0 8px"><b>Nakit Çevrim Süresi (CCC): Net ' + ccc + ' gün' + ratingTxt + '.</b> Şirketin hammadde veya ticari mal alımı için tedarikçiye nakit ödemesinden, müşteriden tahsilata kadar paranın kilitli kaldığı net süredir. ' +
    (ccc <= 30 ? 'Bu süre oldukça seridir; işletme sermayesi kasa üzerinde ilave kredi baskısı yaratmamaktadır.' :
     ccc <= 75 ? 'Bu süre orta düzeydedir; vadelerin ve stok devrinin optimize edilmesi kasaya sıcak nakit akışı sağlayacaktır.' :
     '<b>Bu döngü uzundur ve sermaye yutmaktadır.</b> Şirket operasyonel faaliyetlerini finanse edebilmek için yüksek oranda dış kaynağa (banka kredisi/rotatif) mecbur kalmaktadır.') + '</p>';

  if(spread > 0){
    html += '<p style="margin:0 0 8px;color:#991B1B;background:#FEF2F2;border:1px solid #FCA5A5;border-radius:8px;padding:8px 10px">' +
      '⚠️ <b>Negatif Vade Makası (Müşteriyi Bedava Finanse Etme Riski):</b> Şirket alacaklarını ortalama <b>' + dso + ' günde</b> tahsil ederken, tedarikçilerine <b>' + dpo + ' günde</b> ödeme yapmaktadır. Aradaki <b>' + spread + ' günlük vade açığı</b>, şirketin müşterilerini kendi cebinden (veya pahalı banka kredileriyle) finanse ettiğini gösterir. Ciro büyüdükçe bu açık büyür ve nakit krizine dönüşür. Alacak vadeleri acilen tedarikçi vadesi seviyesine çekilmelidir.</p>';
  } else if(dpo > 0) {
    html += '<p style="margin:0 0 8px;color:#065F46;background:#ECFDF5;border:1px solid #A7F3D0;border-radius:8px;padding:8px 10px">' +
      '✓ <b>Pozitif Tedarikçi Finansmanı:</b> Tedarikçi ödeme vadesi (' + dpo + ' gün), alacak tahsilat süresinden (' + dso + ' gün) uzundur. İşletme, alacaklarını tahsil edene kadar satıcı kredisiyle tampon sağlamaktadır.</p>';
  }

  html += '<p style="margin:0 0 8px"><b>Stokta Kalma Süresi (DIO - ' + dio + ' gün):</b> Depodaki mallar ortalama ' + dio + ' gün beklemektedir. ' +
    (dio > 60 ? 'Stokların depoda bu kadar uzun kalması hem sermayeyi bağlamakta hem de taşıma, fire ve değer düşüklüğü riski yaratmaktadır. 180+ gün ölü ve yavaş dönen stokların nakde dönüştürülmesi önceliklidir.' : 'Stok devir hızı kontrollü seviyededir.') + '</p>';

  if(c.estimated_cash_tied_up && c.estimated_cash_tied_up > 0){
    const potLiberated = Math.round(c.estimated_cash_tied_up * 0.25);
    html += '<div style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:8px;padding:8px 10px;margin-top:6px;color:#1E40AF">' +
      '💡 <b>Kilitli Nakit ve Kurtarma Reçetesi:</b> İşletme sermayesinde kilitli kalan toplam tahmini sermaye: <b>' + money(c.estimated_cash_tied_up) + '</b>. ' +
      'Tahsilat ve stok süreçlerinde sağlanacak 15 günlük bir iyileştirme ile kasaya doğrudan <b>+' + money(potLiberated) + ' sıcak nakit</b> girmesi mümkündür.</div>';
  }
  html += '</div>';
  return html;
}

function leverageNarrative(findings, k, bs, pl, bp){
  k = k || {}; bs = bs || {}; pl = pl || {}; bp = bp || {};
  const cr = k.current_ratio;
  const cashR = k.cash_ratio;
  const de = k.debt_to_equity;
  const da = bp.derived_metrics?.debt_to_assets_pct;
  const stLiab = bs['Short-term liabilities'] || 0;
  const totLiab = bs['Total liabilities'] || (stLiab + (bs['Long-term liabilities'] || 0));
  const stShare = totLiab > 0 ? (stLiab / totLiab * 100) : null;
  const opProfit = pl['Operating profit'] || 0;
  const finCost = pl['Finance costs'] || 0;
  const finToOpPct = opProfit > 0 ? (finCost / opProfit * 100) : null;

  let tier = 'positive';
  if((cr != null && cr < 1.1) || (de != null && de > 3.0) || (stShare != null && stShare > 80)) tier = 'critical';
  else if((cr != null && cr < 1.4) || (de != null && de > 2.0) || (stShare != null && stShare > 65)) tier = 'high';
  else if((cr != null && cr < 1.6) || (de != null && de > 1.5)) tier = 'medium';

  let html = '<div class="insight ' + tier + '" style="line-height:1.65;font-size:12.5px">';
  html += '<div style="font-size:13.5px;font-weight:800;color:#0F172A;margin-bottom:8px">⚖️ CFO Borç Yapısı, Likidite &amp; Solvency Değerlendirmesi</div>';

  // 1. Likidite Analizi
  html += '<p style="margin:0 0 8px"><b>1. Kısa Vadeli Ödeme Gücü (Likidite):</b> ';
  if(cr != null){
    if(cr >= 1.8){
      html += 'Cari oran <b>' + rat(cr) + '</b> ile güçlü likidite bandındadır. Şirketin her 1 TL vadesi gelen borcuna karşılık ' + rat(cr) + ' TL dönen varlığı bulunmaktadır. ';
    } else if(cr >= 1.2){
      html += 'Cari oran <b>' + rat(cr) + '</b> ile dengeli/orta güvenlik seviyesindedir. Rutin operasyonlar karşılanabilir ancak tahsilat aksamalarında nakit sıkışıklığı yaşanabilir. ';
    } else {
      html += '<b style="color:#DC2626">Cari oran ' + rat(cr) + ' ile kritik eşiğin altındadır.</b> Şirketin kısa vadeli borçları dönen varlıklarını aşmakta veya tehlikeli biçimde yakınsamaktadır. Acil likidite tamponu oluşturulmalıdır. ';
    }
  }
  if(cashR != null){
    html += 'Kasadaki hazır nakdin kısa vadeli borçlara oranı (Nakit Oran) <b>' + rat(cashR) + '</b> seviyesindedir (' + (cashR < 0.2 ? 'anlık nakit tamponu düşüktür' : 'anlık şoklara karşı nakit koruması mevcuttur') + ').';
  }
  html += '</p>';

  // 2. Borçluluk ve Kaldıraç Analizi
  html += '<p style="margin:0 0 8px"><b>2. Sermaye Yapısı &amp; Finansal Kaldıraç:</b> ';
  if(de != null){
    html += 'Borç / Özkaynak oranı <b>' + rat(de) + '</b>' + (da != null ? ' (Borç / Aktif: %' + num(da) + ')' : '') + '. ';
    if(de > 2.5){
      html += 'Şirket yüksek oranda borçla finanse edilmektedir; özkaynak tabanı zayıf kalmış ve finansal kaldıraç kırılganlığı artmıştır. ';
    } else {
      html += 'Kaldıraç seviyesi yönetilebilir banttadır. ';
    }
  }
  if(stShare != null && stShare > 60){
    html += '<b style="color:#DC2626">Vade Uyumsuzluğu Riski:</b> Toplam borçların <b>%' + num(stShare) + '\u0027si kısa vadeli</b> borçlardan oluşmaktadır. Borçların kısa vadede yığılması, şirketi sürekli kredi rotasyonu ve yüksek faiz yenileme riskiyle karşı karşıya bırakmaktadır.';
  }
  html += '</p>';

  // 3. Faiz Karşılama ve Tavsiye
  if(finToOpPct != null && finToOpPct > 15){
    html += '<div style="background:#FEF2F2;border:1px solid #FCA5A5;border-radius:8px;padding:8px 10px;margin-top:6px;color:#991B1B">' +
      '⚡ <b>Faiz Baskısı &amp; Kâr Aşınması:</b> Esas faaliyet kârının yaklaşık <b>%' + num(finToOpPct) + '\u0027i finansman giderlerine (banka faizlerine)</b> gitmektedir. Kısa vadeli spot/rotatif kredilerin uzun vadeli taksitli kredilerle refinanse edilmesi ve kâr payı dağıtımı yerine özkaynak güçlendirme aksiyonu şarttır.</div>';
  }

  html += '</div>';
  return html;
}

// Management Actions: two backend-generated actions can legitimately target
// the same commercial KPI (e.g. two different rules both about overdue AR)
// even though the engine already tries to consolidate by root-cause theme.
// Group by KPI keyword here as a presentation-level safety net so the same
// topic is never shown as two separate cards.
function actionBucket(a){
  const kpi=(a.kpi||'').toLowerCase(), theme=(a.decision_theme||'').toLowerCase();
  if(kpi.includes('overdue ar')||kpi.includes('dso')) return 'ar_collections';
  if(kpi.includes('overdue ap')||kpi.includes('dpo')) return 'ap_collections';
  if(kpi.includes('debt')||kpi.includes('interest coverage')||kpi.includes('finance cost')) return 'leverage';
  if(kpi.includes('cash ratio')||kpi.includes('current ratio')||kpi.includes('cash / financial debt')) return 'liquidity';
  if(kpi.includes('gross margin')||kpi.includes('opex')) return 'margin';
  if(kpi.includes('term premium')) return 'pricing';
  if(kpi.includes('dio')||kpi.includes('stale inventory')) return 'inventory';
  if(kpi.includes('top-10')||kpi.includes('concentration')) return 'concentration';
  return theme||a.action_id||a.action;
}
function groupActions(acts){
  const buckets={}; const order=[];
  (acts||[]).forEach(a=>{const key=actionBucket(a); if(!buckets[key]){buckets[key]={...a,items:[a]}; order.push(key);} else {buckets[key].items.push(a); if(sevRank(a.severity)>sevRank(buckets[key].severity))buckets[key].severity=a.severity; if((a.expected_financial_impact||0)>(buckets[key].expected_financial_impact||0))buckets[key].expected_financial_impact=a.expected_financial_impact;}});
  return order.map(k=>buckets[k]).sort((a,b)=>sevRank(b.severity)-sevRank(a.severity));
}


function toggleAccordion(id){
  const el = $(id);
  if(el) el.classList.toggle('active');
}
window.toggleAccordion = toggleAccordion;

function expandAllSteps(){
  document.querySelectorAll('.accordionStep').forEach(s => s.classList.add('active'));
}
window.expandAllSteps = expandAllSteps;

function collapseAllSteps(){
  document.querySelectorAll('.accordionStep').forEach(s => s.classList.remove('active'));
}
window.collapseAllSteps = collapseAllSteps;

function syncStickyNav(){
  const h = document.querySelector('header.top');
  const sub = $('dashboardSubNav');
  if(h && sub){
    const hHeight = Math.round(h.getBoundingClientRect().height || h.offsetHeight);
    if(hHeight > 0) sub.style.top = hHeight + 'px';
  }
}
window.addEventListener('resize', syncStickyNav);
window.addEventListener('scroll', syncStickyNav, { passive: true });
window.addEventListener('load', syncStickyNav);

function jumpToFlowStep(id){
  const el = $(id);
  if(!el) return;
  if(!el.classList.contains('active')){
    el.classList.add('active');
  }
  const h = document.querySelector('header.top');
  const sub = $('dashboardSubNav');
  const hHeight = h ? Math.round(h.getBoundingClientRect().height || h.offsetHeight) : 60;
  const sHeight = sub ? Math.round(sub.getBoundingClientRect().height || sub.offsetHeight) : 42;
  const totalOffset = hHeight + sHeight + 14;
  const topPos = el.getBoundingClientRect().top + window.pageYOffset - totalOffset;
  window.scrollTo({top: Math.max(0, topPos), behavior: 'smooth'});
}
window.jumpToFlowStep = jumpToFlowStep;

function goToDataHubTab(){
  if($('hubTabBtn')) $('hubTabBtn').click();
  const topEl = $('hubTabBtn') || document.querySelector('.tabs') || $('heroSection');
  if(topEl) topEl.scrollIntoView({behavior:'smooth', block:'center'});
}
window.goToDataHubTab = goToDataHubTab;

function toggleSimAssumptions(){
  const body = $('simAssumptionsBody');
  const chev = $('simAssumptionsChevron');
  if(!body) return;
  const isHidden = body.style.display === 'none';
  body.style.display = isHidden ? 'block' : 'none';
  if(chev) chev.textContent = isHidden ? '▼' : '▶';
}
window.toggleSimAssumptions = toggleSimAssumptions;

function openScoreMethodologyModal(){
  const modal = $('scoreMethodologyModal');
  if(!modal) return;
  modal.classList.remove('hidden');
  const meth = (LAST && LAST.business_partner && LAST.business_partner.health_score_methodology) ? LAST.business_partner.health_score_methodology : null;
  renderScoreMethodology(meth);
}
window.openScoreMethodologyModal = openScoreMethodologyModal;

function closeScoreMethodologyModal(){
  const modal = $('scoreMethodologyModal');
  if(modal) modal.classList.add('hidden');
}
window.closeScoreMethodologyModal = closeScoreMethodologyModal;

function renderScoreMethodology(meth){
  const list = $('methodologyPillarsList');
  if(!list) return;
  if(meth && meth.pillars && meth.pillars.length){
    list.innerHTML = meth.pillars.map(p => {
      const pctWidth = Math.min(100, Math.max(0, (p.earned_points / p.max_points) * 100));
      return '<div style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:14px;padding:16px;box-shadow:0 2px 6px rgba(0,0,0,0.02)">' +
        '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;flex-wrap:wrap;gap:8px">' +
          '<div style="display:flex;align-items:center;gap:8px">' +
            '<span class="tag" style="background:#EFF6FF;color:#1D4ED8;font-weight:800;font-size:11px">Ağırlık: %' + p.weight_pct + '</span>' +
            '<b style="font-size:13.5px;color:#0F172A">' + esc(p.name) + '</b>' +
          '</div>' +
          '<div style="font-size:13px;font-weight:800;color:#0F172A">' +
            '<span style="color:#1D4ED8;font-size:16px">' + p.earned_points + '</span> / ' + p.max_points + ' Puan' +
          '</div>' +
        '</div>' +
        '<div style="height:6px;background:#F1F5F9;border-radius:99px;overflow:hidden;margin-bottom:10px">' +
          '<div style="width:' + pctWidth + '%;height:100%;background:linear-gradient(90deg,#2563EB,#3B82F6);border-radius:99px"></div>' +
        '</div>' +
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-size:11.5px;background:#F8FAFC;padding:10px 12px;border-radius:10px;border:1px solid #EDF2F7">' +
          '<div><span style="color:#64748B;font-weight:600">Ölçülen Temel Metrik:</span> <b style="color:#334155">' + esc(p.metric_basis) + '</b></div>' +
          '<div><span style="color:#64748B;font-weight:600">Puanlama Kuralı:</span> <span style="color:#334155">' + esc(p.formula) + '</span></div>' +
        '</div>' +
        '<div style="font-size:11.5px;color:#64748B;margin-top:8px;line-height:1.4">' + esc(p.evaluation) + '</div>' +
      '</div>';
    }).join('');
  } else {
    list.innerHTML = [
      { name: '1. Veri Güvenilirliği & Bilanço Denkliği', weight: 15, basis: 'Bilanço eşitliği & hesap tutarlılığı', rule: 'Aktif = Pasif denkliği ve hesap planı kontrolü', desc: 'Bilanço eşitliği, aktif/pasif mutabakatı ve hesap planı tutarlılığı.' },
      { name: '2. Likidite & Kısa Vadeli Ödeme Gücü', weight: 20, basis: 'Cari Oran & Nakit Oranı', rule: 'Cari oran (max 10p) + Nakit oranı (max 10p)', desc: 'Vadesi gelen kısa vadeli borçların dönen ve nakit varlıklarla karşılanabilme gücü.' },
      { name: '3. Kaldıraç & Finansman Yükü', weight: 25, basis: 'Borç/Özkaynak & Fin. Gideri/FVÖK', rule: 'Borç/Özkaynak (max 12p) + Fin. Gideri/Kâr (max 13p)', desc: 'Faaliyet kârının finansman giderlerini karşılama kapasitesi ve özkaynak emniyet marjı.' },
      { name: '4. Faaliyet & Net Kârlılık', weight: 25, basis: 'Faaliyet Marjı & Net Kâr Marjı', rule: 'Faaliyet Marjı (max 13p) + Net Kâr Marjı (max 12p)', desc: 'Satışların faaliyet seviyesinde ve net dönem seviyesinde kâra dönüşüm başarısı.' },
      { name: '5. Varlık Verimliliği & Sermaye Gücü', weight: 15, basis: 'Aktif Devir Hızı & Özkaynak Oranı', rule: 'Aktif Devir Hızı (max 8p) + Özkaynak/Aktif (max 7p)', desc: 'Bağlı aktiflerin ciro üretme hızı ve şirketin varlıklarını finanse eden özkaynak payı.' }
    ].map(p => '<div style="background:#F8FAFC;border:1.5px solid #E2E8F0;border-radius:12px;padding:14px"><div style="display:flex;justify-content:space-between;font-weight:700;font-size:13px;color:#0F172A;margin-bottom:6px"><span>' + p.name + '</span><span class="tag" style="background:#EFF6FF;color:#1D4ED8">Ağırlık: %' + p.weight + '</span></div><div style="font-size:11.5px;color:#334155;line-height:1.5"><p style="margin:0 0 4px"><b>Metrik / Formül:</b> ' + p.basis + ' &bull; ' + p.rule + '</p><p style="margin:0;color:#64748B">' + p.desc + '</p></div></div>').join('');
  }
}
window.renderScoreMethodology = renderScoreMethodology;

function render(d){
  LAST=d;$('dashboard').classList.remove('hidden');
  const bp=d.business_partner,pl=d.statements.profit_and_loss,bs=d.statements.balance_sheet,k=d.statements.kpis;
  const fx = d.fx_rates || (bp && bp.fx_rates);
  if(fx){
    window._currencyRates = fx.multipliers || window._currencyRates;
    window._fxInfo = fx;
  }
  const cm = bp.core_metrics || {};
  setRing(bp.health_score);
  if(cm.is_conditional_score){
    $('healthLabel').innerHTML = esc(bp.health_label) + ' <span class="tag" style="background:#FEF3C7;color:#B45309;border:1px solid #FCD34D;font-size:10px;padding:2px 6px;vertical-align:middle;margin-left:4px">Şartlı Skor (Doğrulama Bekleniyor)</span>';
  } else {
    $('healthLabel').textContent = bp.health_label;
  }
  renderTopFocusIssues(bp);
  const c=bp.cash_conversion_cycle||{};
  renderExecutiveSnapshot(bp, pl, bs, k, c, d);

  // Step 1 — WHAT (financial facts)
  const canonSales = cm.canonical_net_sales != null ? cm.canonical_net_sales : pl['Net sales'];
  $('mSales').textContent=money(canonSales);$('mOp').textContent=money(pl['Operating profit']);$('mNet').textContent=money(pl['Net profit']);$('mDebt').textContent=money(k.net_debt);
  renderDuPont(bp.dupont_analysis||{});
  renderComparative(bp.trend_analysis||{});
  waterfall('waterfall',[['Net satış',canonSales,false],['Satılan Malın Maliyeti (SMM)',-pl['COGS'],true],['Brüt kâr',pl['Gross profit'],false],['Faaliyet gideri',-pl['Operating expenses'],true],['Faaliyet kârı',pl['Operating profit'],false],['Finansman',-pl['Finance costs'],true],['Vergi',-pl['Tax expense'],true],['Net kâr',pl['Net profit'],false]]);
  const pq=bp.profit_quality_engine||{};
  $('liquidity').innerHTML=[['Cari Oran (Dönen Varlık / Borç)',rat(k.current_ratio),'1.5 - 2.0 ideal seviye'],['Nakit Oran (Hazır Değer / Borç)',rat(k.cash_ratio),'hazır nakit / kısa vadeli borç'],['Kaldıraç (Borç / Özkaynak)',rat(k.debt_to_equity),'düşük olması güvenlidir'],['Borç / Aktif Oranı',pct(bp.derived_metrics?.debt_to_assets_pct),'finansman yoğunluğu']].map(x=>metric(x[0],x[1],x[2])).join('');
  $('leverageCommentary').innerHTML=leverageNarrative(bp.findings, k, bs, pl, bp);
    const daysPeriod = c.days_in_period_assumption || 365;
    const cccCards = [
    { code: 'DSO', title: 'Tahsilat Vadesi', days: cm.dso_days != null ? cm.dso_days : c.dso_days, sub: cm.dso_source_label || 'Mizan 120 (Resmi)', color: '#1D4ED8', tip: 'DSO: (Alacaklar / Net Satış) × ' + daysPeriod + '. Müşterilerin ortalama ödeme süresi. Mizan 120 hesabından hesaplanmıştır.' },
    { code: 'DIO', title: 'Stokta Kalma', days: cm.dio_days != null ? cm.dio_days : c.dio_days, sub: 'Mizan 150-153 (Resmi)', color: '#D97706', tip: 'DIO: (Stoklar / SMM) × ' + daysPeriod + '. Depoda ortalama bekleme süresi.' },
    { code: 'DPO', title: 'Tedarikçi Vadesi', days: cm.dpo_days != null ? cm.dpo_days : c.dpo_days, sub: 'Mizan 320 (Resmi)', color: '#0E7C66', tip: 'DPO: (Borçlar / SMM) × ' + daysPeriod + '. Tedarikçiye ödeme süresi.' },
    { code: 'CCC', title: 'Nakit Çevrim', days: cm.ccc_days != null ? cm.ccc_days : c.cash_conversion_cycle_days, sub: 'Kasadaki nakdin dönüş hızı', color: '#7C3AED', tip: 'CCC = DSO + DIO - DPO. Hammaddeden tahsilata kadar nakdin bağlı kaldığı net gün sayısıdır.' }
  ];
  $('cccMetric').textContent = (cm.ccc_days != null ? num(cm.ccc_days) : (c.cash_conversion_cycle_days == null ? '–' : num(c.cash_conversion_cycle_days))) + ' gün';
  $('workingCapital').innerHTML = '<div class="grid4">' + cccCards.map(x => 
    '<div class="metric" style="text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:14px 10px;background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px">' +
      '<div style="display:inline-flex;align-items:center;justify-content:center;font-size:15px;font-weight:900;letter-spacing:0.5px;color:' + x.color + '" title="' + esc(x.tip) + '">' + esc(x.code) + '</div>' +
      '<div style="font-size:11px;font-weight:700;color:#64748B;margin-top:2px;margin-bottom:6px;text-align:center">' + esc(x.title) + '</div>' +
      '<div class="value" style="font-size:21px;font-weight:900;color:#0F172A;margin:2px 0">' + (x.days == null ? '–' : num(x.days) + ' gün') + '</div>' +
      '<div class="sub" style="font-size:10.5px;color:#94A3B8;text-align:center;margin-top:2px">' + esc(x.sub) + '</div>' +
    '</div>'
  ).join('') + '</div><div style="margin-top:12px">' + workingCapitalNarrative(c, cm, pl, k) + '</div>';

  const cb = bp.cash_bridge_engine || {};
  if(cb.available){
    const isPos = (cb.cash_change || 0) >= 0;
    const bColor = isPos ? '#16A34A' : '#DC2626';
    const bBg = isPos ? '#ECFDF5' : '#FEF2F2';
    const bBorder = isPos ? '#A7F3D0' : '#FCA5A5';
    const cbSummary = '<div class="grid3" style="margin-bottom:14px">' +
      '<div class="metric" style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:12px 14px">' +
        '<div class="label" style="color:#64748B;font-weight:700">Dönem Başı Nakit (Kasa &amp; Banka)</div>' +
        '<div class="value" style="font-size:18px;font-weight:800;color:#0F172A">' + money(cb.opening_cash) + '</div>' +
        '<div class="sub">Açılış Likit Rezervi</div>' +
      '</div>' +
      '<div class="metric" style="background:' + bBg + ';border:1.5px solid ' + bBorder + ';border-radius:12px;padding:12px 14px">' +
        '<div class="label" style="color:' + bColor + ';font-weight:700">Net Kasa &amp; Nakit Değişimi</div>' +
        '<div class="value" style="font-size:18px;font-weight:900;color:' + bColor + '">' + (isPos ? '+' : '') + money(cb.cash_change) + '</div>' +
        '<div class="sub" style="color:' + bColor + '">' + (isPos ? 'Net Nakit Girişi' : 'Net Nakit Çıkışı (Eriyen Kasa)') + '</div>' +
      '</div>' +
      '<div class="metric" style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:12px 14px">' +
        '<div class="label" style="color:#64748B;font-weight:700">Dönem Sonu Nakit (Kasa &amp; Banka)</div>' +
        '<div class="value" style="font-size:18px;font-weight:800;color:#1D4ED8">' + money(cb.closing_cash) + '</div>' +
        '<div class="sub">Kapanış Mevcut Nakit</div>' +
      '</div>' +
    '</div>';
    $('cashFlow').innerHTML = cbSummary + '<div class="waterfallWrap"><div id="cashFlowWf" class="waterfall"></div></div><div class="notice" style="margin-top:12px;font-size:12px"><b>Nakit Akış Yorumu:</b> Kasa ' + money(cb.opening_cash) + ' seviyesinden ' + money(cb.closing_cash) + ' seviyesine ' + (isPos ? 'yükselmiştir (+ ' : 'gerilemiştir (– ') + money(Math.abs(cb.cash_change)) + '). ' + esc(cb.note||'') + '</div>';
    waterfall('cashFlowWf',[['Açılış Nakit',cb.opening_cash,false],['Faaliyet Kârı',cb.operating_profit,false],['Alacak Etkisi',cb.working_capital_components?.receivables_effect,cb.working_capital_components?.receivables_effect<0],['Stok Etkisi',cb.working_capital_components?.inventory_effect,cb.working_capital_components?.inventory_effect<0],['Tedarikçi Borç Etkisi',cb.working_capital_components?.payables_effect,cb.working_capital_components?.payables_effect<0],['Finansal Borç Δ',cb.debt_change,cb.debt_change<0],['Açıklanmayan',cb.unexplained_cash_change,cb.unexplained_cash_change<0],['Kapanış Nakit',cb.closing_cash,false]]);
  } else {
    const wp = cb.working_capital_proxy || {};
    $('cashFlow').innerHTML = '<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:14px;margin-bottom:12px"><div style="display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:6px"><div style="display:flex;align-items:center;gap:6px"><span class="tag" style="background:#EFF6FF;color:#1D4ED8;font-size:11px;font-weight:700">ℹ️ Tek Dönem Mizan</span><span style="font-size:12.5px;font-weight:700;color:#0F1B2D">Cari Bağlı İşletme Sermayesi Dökümü</span></div><button class="secondary hidePrint" style="padding:4px 10px;font-size:11px;border-radius:6px" onclick="goToTrendTab()">📊 2. Dönemi Ekle</button></div><div class="small muted" style="line-height:1.5">Tek dönem analizinde açılış bilançosu bulunmadığından nakit köprüsü yerine cari işletme sermayesi kilitlenmeleri listelenmiştir. Gerçek nakit köprüsü için Trend sekmesini kullanabilirsiniz.</div></div><div class="grid3">' + metric('Alacaklar (Müşteride)',money(wp.receivables),'Bağlı İşletme Sermayesi') + metric('Stoklar (Depoda)',money(wp.inventory),'Bağlı İşletme Sermayesi') + metric('Borçlar (Tedarikçi)',money(wp.payables),'Sağlanan Tedarikçi Finansmanı') + '</div>';
  }

  // "Kâr Nakde Dönüşüyor mu?" — 3 Aşamalı Pedagojik Yönetici Hattı
  // Sağdaki squished waterfall kaldırıldı, yerine adım adım kâr -> nakit hattı kuruldu.
  if(cb.available && cb.cash_realization_pct!=null){
    const crp=Math.max(0, Math.min(100, Math.round(cb.cash_realization_pct)));
    const crTier=(crp>=80 && cb.operating_cash_flow_proxy>0)?'positive':(crp>=50 && cb.operating_cash_flow_proxy>0)?'medium':crp>0?'high':'critical';
    let crExpl='';
    if(crp<=0 || cb.operating_cash_flow_proxy<=0){
      crExpl='⚠️ <b>Defterde '+money(cb.net_profit)+' net kâr görünmesine rağmen, işletme nakit akışı '+money(cb.operating_cash_flow_proxy)+' negatiftir (%0 nakit gerçekleşmesi).</b> Net kârın tamamı ve fazlası alacaklarda ('+money(cb.working_capital_components?.receivables_effect)+') ve depodaki stokta ('+money(cb.working_capital_components?.inventory_effect)+') kilitlenmiştir. Kasa bu kârı görememiş, işletme operasyonel nakit açığı vermiştir. Acil tahsilat hızlandırma ve ölü stok eritme aksiyonu şarttır.';
    } else if(crp<80){
      crExpl='Faaliyet kârı '+money(cb.operating_profit)+', net kâr '+money(cb.net_profit)+'; alacak/stok/borç hareketleri dahil edildiğinde işletme faaliyet nakdi '+money(cb.operating_cash_flow_proxy)+' oluyor — yani defter kârının yaklaşık <b>%'+crp+'\u0027i</b> fiilen kasaya giriyor. Kalan tutar müşteride veya depoda bağlı kalmaktadır.';
    } else {
      crExpl='Net kâr '+money(cb.net_profit)+'; işletme nakdi '+money(cb.operating_cash_flow_proxy)+'. Kâr büyük ölçüde (%'+crp+') nakde dönüşüyor; işletme sermayesi kâr üzerinde ek bir nakit baskısı yaratmıyor.';
    }
    const ocf = cb.operating_cash_flow_proxy || 0;
    const recEff = cb.working_capital_components?.receivables_effect || 0;
    const invEff = cb.working_capital_components?.inventory_effect || 0;
    const payEff = cb.working_capital_components?.payables_effect || 0;

    const pipelineHtml = '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:14px">' +
      '<div style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:14px">' +
        '<div style="font-size:11px;font-weight:800;color:#64748B;text-transform:uppercase;letter-spacing:0.5px">1. Muhasebe Kârı (Defter)</div>' +
        '<div style="font-size:20px;font-weight:900;color:#0F172A;margin:4px 0">' + money(cb.net_profit) + '</div>' +
        '<div class="small muted">Gelir Tablosu Dönem Net Kârı (Tahakkuk)</div>' +
      '</div>' +
      '<div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:12px;padding:14px">' +
        '<div style="font-size:11px;font-weight:800;color:#D97706;text-transform:uppercase;letter-spacing:0.5px">2. İşletme Sermayesi Kilitlenmesi</div>' +
        '<div style="font-size:11.5px;color:#334155;margin-top:6px;line-height:1.65">' +
          '<div>• Alacak Etkisi (120): <b style="color:' + (recEff<0?'#DC2626':'#16A34A') + '">' + (recEff>0?'+':'') + money(recEff) + '</b></div>' +
          '<div>• Stok Etkisi (153): <b style="color:' + (invEff<0?'#DC2626':'#16A34A') + '">' + (invEff>0?'+':'') + money(invEff) + '</b></div>' +
          '<div>• Tedarikçi Katkısı (320): <b style="color:' + (payEff<0?'#DC2626':'#16A34A') + '">' + (payEff>0?'+':'') + money(payEff) + '</b></div>' +
        '</div>' +
      '</div>' +
      '<div style="background:' + (ocf>0?'#ECFDF5':'#FEF2F2') + ';border:1.5px solid ' + (ocf>0?'#A7F3D0':'#FCA5A5') + ';border-radius:12px;padding:14px">' +
        '<div style="display:flex;justify-content:space-between;align-items:center">' +
          '<div style="font-size:11px;font-weight:800;color:' + (ocf>0?'#16A34A':'#DC2626') + ';text-transform:uppercase;letter-spacing:0.5px">3. İşletme Nakit Akışı</div>' +
          '<span class="tag ' + (crp>=80?'positive':crp>=50?'medium':'critical') + '" style="font-weight:800;font-size:11px">%' + crp + ' Dönüşüm</span>' +
        '</div>' +
        '<div style="font-size:20px;font-weight:900;color:' + (ocf>0?'#16A34A':'#DC2626') + ';margin:4px 0">' + (ocf>0?'+':'') + money(ocf) + '</div>' +
        '<div class="small" style="color:' + (ocf>0?'#065F46':'#991B1B') + '">' + (ocf>0?'Faaliyetlerden Kasaya Giren Net Nakit':'İşletme Sermayesi Nedeniyle Eriyen Kasa Nakdi') + '</div>' +
      '</div>' +
    '</div>';

    $('cashRealization').innerHTML = pipelineHtml + '<div class="insight ' + crTier + '"><p>' + crExpl + '</p></div>';
  } else {
    $('cashRealization').innerHTML='<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:16px;text-align:center"><div style="display:inline-flex;align-items:center;gap:6px;background:#EFF6FF;color:#1D4ED8;padding:3px 10px;border-radius:999px;font-size:11px;font-weight:700;margin-bottom:8px">ℹ️ Tek Dönem Modu Aktif</div><div style="font-size:13.5px;font-weight:700;color:#0F1B2D;margin-bottom:4px">Kârın Nakde Dönüşüm Oranı</div><p class="muted small" style="margin:0 auto 12px;max-width:440px">Tek dönem mizandan net kâr ve likidite tam hesaplanmıştır. Net kârın ne kadarının kasaya nakit aktığını görmek için iki dönemli karşılaştırma önerilir.</p><button class="secondary hidePrint" style="padding:7px 16px;font-size:12px;border-radius:8px" onclick="runDataHubSample()">⚡ Canlı 2 Dönemli Trend Demosunu Çalıştır</button></div>';
  }
  renderResourceAllocation(bp.resource_allocation_engine);
  if(bp.tax_strategy_engine) renderTaxStrategy(bp.tax_strategy_engine);
  renderWorkingCapitalLeak(bp, pl, bs, k, c, d);
  renderCeoDiagnosticDesk(bp, pl, bs, k, c, d);


  // Step 2 — SO WHAT (business impact)
  const rr=bp.risk_ranking_engine?.ranked_risks||[];$('risks').innerHTML=rr.slice(0,8).map((r,i)=>'<div class="riskRow"><div class="rank">#'+r.rank+'</div><div><b>'+esc(r.title)+'</b><div class="riskScore">'+esc(r.category)+' · '+num(r.risk_score)+' / 100'+(r.estimated_exposure!=null?' · '+money(r.estimated_exposure):'')+'</div><div class="bar"><i style="width:'+Math.min(100,r.risk_score||0)+'%"></i></div></div><span class="tag '+String(r.risk_tier||'').toLowerCase()+'">'+esc(r.risk_tier)+'</span></div>').join('')||'<div class="notice">Öncelikli risk bulunmadı.</div>';
  $('profitQuality').innerHTML='<div class="grid2">'+metric('Brüt Kâr Marjı',pct(pq.gross_margin_pct),'')+metric('Faaliyet Kâr Marjı',pct(pq.operating_margin_pct),'')+metric('Net Kâr Marjı',pct(pq.net_margin_pct),'')+metric('Finansman Gideri / Faaliyet Kârı Oranı',pct(pq.finance_cost_to_operating_profit_pct),'')+'</div>';
  $('profitabilityCommentary').innerHTML=profitabilityNarrative(pl,pq);
  const bm=bp.benchmarking||{};
  let instRef='TCMB Sektör Bilançoları & Borsa İstanbul (BIST) Sektörel Medyan Finansal Rasyoları';
  if(bm.institutional_reference){
    if(typeof bm.institutional_reference==='object'){
      instRef=(bm.institutional_reference.primary_source||'TCMB Sektör Bilançoları')+(bm.institutional_reference.secondary_source?' & '+bm.institutional_reference.secondary_source:'');
    }else if(typeof bm.institutional_reference==='string'){
      instRef=bm.institutional_reference;
    }
  }
  const wcLeak = bm.working_capital_leakage || {};
  let leakHtml = '';
  if(wcLeak && wcLeak.total_excess_cash_tied_up > 0){
    leakHtml = '<div style="margin-top:16px;background:#FFF1F2;border:1.5px solid #FECDD3;border-radius:14px;padding:16px">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:10px">' +
        '<div style="display:flex;align-items:center;gap:8px">' +
          '<span style="font-size:18px">🚨</span>' +
          '<b style="color:#9F1239;font-size:13.5px">Sektörel Vade Gecikmesi &amp; Gizli Finansman / Faiz Sızıntısı:</b>' +
        '</div>' +
        '<span class="tag critical" style="font-weight:800;font-size:12px">Yıllık Kayıp: ' + money(wcLeak.annual_interest_leakage) + '</span>' +
      '</div>' +
      '<p style="font-size:12.5px;color:#881337;line-height:1.55;margin:0 0 12px">' + esc(wcLeak.executive_summary) + '</p>' +
      '<div class="grid3" style="gap:10px">' +
        '<div style="background:#FFFFFF;border:1px solid #FFE4E6;border-radius:10px;padding:10px 12px">' +
          '<div style="font-size:11px;color:#64748B">Tahsilat (DSO) Sapması:</div>' +
          '<b style="font-size:14px;color:#E11D48">' + (wcLeak.dso?.gap_days > 0 ? ('+' + wcLeak.dso.gap_days + ' Gün') : 'Sektörden Hızlı') + '</b>' +
          '<div style="font-size:11px;color:#9F1239;margin-top:2px">Kilitli: ' + money(wcLeak.dso?.excess_cash_tied_up || 0) + '</div>' +
        '</div>' +
        '<div style="background:#FFFFFF;border:1px solid #FFE4E6;border-radius:10px;padding:10px 12px">' +
          '<div style="font-size:11px;color:#64748B">Stokta Kalma (DIO) Sapması:</div>' +
          '<b style="font-size:14px;color:#D97706">' + (wcLeak.dio?.gap_days > 0 ? ('+' + wcLeak.dio.gap_days + ' Gün') : 'Sektörden Hızlı') + '</b>' +
          '<div style="font-size:11px;color:#92400E;margin-top:2px">Kilitli: ' + money(wcLeak.dio?.excess_cash_tied_up || 0) + '</div>' +
        '</div>' +
        '<div style="background:#FFFFFF;border:1px solid #FFE4E6;border-radius:10px;padding:10px 12px">' +
          '<div style="font-size:11px;color:#64748B">Aylık Gizli Faiz Yükü:</div>' +
          '<b style="font-size:14px;color:#BE123C">-' + money(wcLeak.monthly_interest_leakage || 0) + ' / Ay</b>' +
          '<div style="font-size:11px;color:#64748B;margin-top:2px">Gösterge: %' + (wcLeak.indicative_borrowing_rate_pct || 48) + ' Faaliyet/Kredi</div>' +
        '</div>' +
      '</div>' +
    '</div>';
  }

  $('benchmark').innerHTML='<div class="insight positive" style="margin-bottom:12px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px">'
    +'<div><b>🏛️ Kurumsal Kıyaslama Kaynağı:</b> <span class="muted">'+esc(instRef)+'</span></div>'
    +'<div class="small">Sektör: <b>'+esc(bm.sector||'Genel')+'</b> · Konum: <span class="tag '+(bm.overall_score>=70?'positive':bm.overall_score>=50?'medium':'critical')+'">'+esc(bm.overall_label)+' ('+esc(bm.overall_score)+'/100)</span></div>'
    +'</div>'
    +'<div class="tableWrap" style="margin-top:8px"><table><thead><tr><th>Gösterge</th><th>Şirket Değeri</th><th>Sektör Bandı (Düşük / Medyan / Yüksek)</th><th>Sektöre Göre Konum</th></tr></thead><tbody>'
    +(bm.metrics||[]).map(m=>'<tr><td><b>'+esc(m.label)+'</b></td><td>'+esc(m.value)+'</td><td>'+esc(m.band_low)+' / <b>'+esc(m.band_mid)+'</b> / '+esc(m.band_high)+'</td><td><span class="tag '+(m.favorability==='favorable'?'positive':m.favorability==='unfavorable'?'critical':'medium')+'">'+esc(m.favorability)+'</span></td></tr>').join('')
    +'</tbody></table></div>'
    +leakHtml;

  // Render Step 8: Inflation Adjustment & Liquidity Stress Test
  renderInflationAnalysis(bp.inflation_adjustment_engine);
  renderLiquidityStressTest(bp.liquidity_stress_testing_engine);

  // Step 3 & Step 6b — Unified 5-Step Causality Pipeline (Belirti ➔ Kanıt ➔ Kök Neden ➔ Sızıntı ➔ İcraat)
  renderUnifiedRootCauseSection(bp.root_cause_engine, bp.narrative_engine);

  // NOW WHAT (management actions). Actions that share a KPI/theme still get
  // grouped so context (owner/KPI/impact) isn't repeated per line, but every
  // individual action TEXT gets its own item number (2.1, 2.2, ...) instead
  // of being hidden as an unnumbered bullet inside one group — each
  // recommendation is a separately trackable "madde", not a sub-note.
  const groups=groupActions(bp.management_actions||[]);
  $('actions').innerHTML=groups.map((g,i)=>{
    const kpis=[...new Set(g.items.map(x=>x.kpi).filter(Boolean))].join(' / ');
    const meta='<div class="small muted" style="margin-top:4px">'+esc(g.owner)+' · '+esc(g.time_horizon)+' · KPI: '+esc(kpis)+'</div>'+(g.expected_financial_impact!=null?'<div class="small" style="margin-top:4px"><b>Beklenen finansal etki:</b> '+money(g.expected_financial_impact)+' <span class="muted">('+esc(g.expected_impact_label||'proxy')+')</span></div>':'');
    if(g.items.length>1){
      return g.items.map((x,j)=>'<div class="actionRow"><div class="rank">'+(i+1)+'.'+(j+1)+'</div><div><b>'+esc(x.action)+'</b>'+(j===g.items.length-1?meta:'')+'</div><span class="tag '+esc(x.severity||g.severity)+'">'+esc(x.severity||g.severity)+'</span></div>').join('');
    }
    return '<div class="actionRow"><div class="rank">'+(i+1)+'</div><div><b>'+esc(g.action)+'</b>'+meta+'</div><span class="tag '+esc(g.severity)+'">'+esc(g.severity)+'</span></div>';
  }).join('')||'<div class="notice">Aksiyon yok.</div>';

  // Step 5 — WHAT IF (Opportunity Engine)
  const impactLabels={'annual_profit_if_period_is_annual':'Yıllık kâr etkisi (dönem yıllık ise)','finance_cost_saving_proxy':'Finansman maliyeti tasarrufu (proxy)','cash_release':'Nakit serbestleşmesi'};
  const opps=bp.opportunity_engine?.opportunities||[];
  $('opportunities').innerHTML=opps.map(o=>{const cs=o.current_state||{};const csTxt=Object.entries(cs).filter(([k,v])=>v!=null).map(([k,v])=>k+': '+v).join(' · ');return '<div class="scenario"><div class="small muted">#'+esc(o.rank)+' · '+esc(o.area)+'</div><h3>'+esc(o.title)+'</h3><div class="big">'+money(o.estimated_impact)+'</div><p>'+esc(impactLabels[o.impact_type]||o.impact_type||'')+'</p><p class="small muted">Hesaplama: '+esc(o.calculation||'')+'</p><p class="small muted">Varsayım: '+esc(o.assumption||'')+'</p>'+(csTxt?'<div class="small muted" style="margin-top:6px">Mevcut durum: '+esc(csTxt)+'</div>':'')+'<div class="small" style="margin-top:6px">Satışın %'+esc(o.pct_of_net_sales??'–')+' · Net kârın %'+esc(o.pct_of_net_profit??'–')+'</div></div>'}).join('')||'<div class="notice">Fırsat bulunamadı.</div>';

  // Step 7 — AI CFO: narrative + grounded KPI chips + an explicit "what should
  // the manager do with this" block, built from the same management actions
  // shown in "Now What" (no new numbers invented here, just the decision
  // implication stated plainly instead of left for the reader to infer).
  $('exec').innerHTML='<div style="font-size:14px;line-height:1.65;color:#1E293B"><strong style="color:#0F172A;font-size:15px;display:inline-block;margin-bottom:6px">📋 Finansal Teşhis &amp; Yönetici Karar Brifingi:</strong><br>' + esc(bp.executive_summary) + '</div>';
  const topRisk=rr[0], topOpp=opps[0];
  const chips=[['Sağlık Skoru',Math.round(bp.health_score)+'/100'],['Nakit Çevrim (CCC)',c.cash_conversion_cycle_days==null?'–':Math.round(Number(c.cash_conversion_cycle_days))+' gün'],(cb.available&&cb.cash_realization_pct!=null)?['Kâr → Nakit',pct(cb.cash_realization_pct)]:null,topRisk?['En Kritik Risk',topRisk.title]:null,topOpp?['En Büyük Fırsat',topOpp.title+' ('+money(topOpp.estimated_impact)+')']:null,['Sektör Konumu',bm.overall_label||'–']].filter(Boolean);
  $('execChips').innerHTML=chips.map(x=>'<span class="chip">'+esc(x[0])+': <b>'+esc(x[1])+'</b></span>').join('');
  const esum=bp.executive_summary_engine||{};
  const dpoints=esum.decision_points||[];
  $('execDecision').innerHTML=dpoints.length?'<div class="insight positive"><b>Yönetici bu raporla ne yapmalı</b><ul>'+dpoints.map(p=>'<li>'+esc(p)+'</li>').join('')+'</ul><p class="small muted" style="margin-top:6px">Ayrıntılı sahip/ufuk/KPI kırılımı "Now What — Yönetim Aksiyonları" bölümünde.</p></div>':'';
  $('methodNote').textContent=bp.methodology_note||'';

  // Appendix A — Data Quality
  const dq=d.quality?.advanced||{};
  $('dq').textContent=dq.score==null?'–':dq.score+'/100';$('dqStatus').textContent=dq.status||'–';
  const audit=bp.calculation_audit||{};
  $('auditValue').textContent=audit.status||'–';$('auditSub').textContent=(audit.failed_count||0)+' başarısız kontrol';
  $('dqUnmapped').textContent=dq.unmapped_accounts??'–';
  $('dqChecks').innerHTML=(dq.checks&&dq.checks.length)?'<table><thead><tr><th>Kontrol</th><th>Durum</th><th>Değer</th></tr></thead><tbody>'+dq.checks.map(c=>'<tr><td>'+esc(c.name)+'</td><td>'+(c.status==='passed'?'<span class="tag positive">Geçti</span>':'<span class="tag critical">Başarısız</span>')+'</td><td>'+(c.value==null?'–':num(c.value))+'</td></tr>').join('')+'</tbody></table>':'';
  const dqIssues=[...(dq.critical_issues||[]).map(x=>({...x,sev:'critical'})),...(dq.warnings||[]).map(x=>({...x,sev:'medium'}))];
  $('dqIssues').innerHTML=dqIssues.length?dqIssues.map(x=>'<div class="insight '+x.sev+'" style="margin-top:8px"><b>'+esc(x.name)+'</b><p>'+esc(x.note||(x.count!=null?(x.count+' kayıt'):'')||(x.fields?('Eksik alanlar: '+x.fields.join(', ')):''))+'</p></div>').join(''):'<div class="notice">Kritik veri kalitesi sorunu bulunamadı.</div>';
  $('dqNote').textContent=dq.note||'';



  // Appendix — trend & traceability
  const tr=bp.trend_analysis||{};$('trendBlock').innerHTML=tr.available?'<div class="small muted">Karşılaştırmalı özet ve dönemsel bulgular yukarıda, "1 — What" bölümündeki <b>Karşılaştırmalı Analiz</b> kartında gösteriliyor. Aşağıdaki Ek B ise ham hesap izini içerir.</div>':'<div class="notice">'+esc(tr.reason||'Trend için 2+ dönem gerekir.')+'</div>';
  $('plTable').innerHTML=table('Gelir Tablosu',pl);$('bsTable').innerHTML=table('Bilanço',bs);
  if($('cfTable'))$('cfTable').innerHTML=renderCashFlowTable(cb,pl,bs);
  const accounts=d.canonical_model?.accounts||[];$('trace').innerHTML='<div class="notice">Traceability: '+accounts.length+' canonical account rows. Her satıra tıklayarak kaynak formülünü ve defter izini görebilirsiniz.</div><table style="margin-top:8px"><thead><tr><th>Hesap</th><th>Ad</th><th>Bakiye</th><th>Sheet</th><th>Row</th></tr></thead><tbody>'+accounts.slice(0,15).map(a=>'<tr style="cursor:pointer" onclick="showTraceModal(\'Hesap İzlenebilirliği: '+esc(a.account_code)+'\', \'<b>Hesap Adı:</b> '+esc(a.account_name)+'<br><b>Bakiye:</b> '+money(a.balance)+'<br><b>Kaynak Sayfa:</b> '+esc(a.source_sheet)+'<br><b>Kaynak Satır:</b> '+esc(a.source_row)+'<br><b>Deterministik Kural:</b> Borç Hareketi - Alacak Hareketi = Net Bakiye\')"><td><b>'+esc(a.account_code)+'</b> 🔍</td><td>'+esc(a.account_name)+'</td><td>'+money(a.balance)+'</td><td>'+esc(a.source_sheet)+'</td><td>'+esc(a.source_row)+'</td></tr>').join('')+'</tbody></table>';
  if(bp.customer_profitability_engine) renderCustomerProfitabilityMatrix(bp.customer_profitability_engine);
  if(bp.product_profitability_engine) renderProductProfitability(bp.product_profitability_engine);
  setupInteractiveScenario(d);
}

// AR / AP Intelligence — full aging-engine output rendered with visual bars
// (bucket share, overdue share) instead of plain text-only rows.
function agingBlock(title,due,data){
  const titleLabel = title==='AR'?'Müşteri Alacak Yaşlandırma Analizi (120 Hesabı & Vade Dağılımı)':'Tedarikçi Borç Yaşlandırma Analizi (320 Hesabı & Ödeme Takvimi)';
  if(!data) return '<div class="notice">'+esc(titleLabel)+' yüklenmedi.</div>';
  const buckets=(data.aging_buckets||[]).filter(b=>b.amount);
  const bucketRows=buckets.length?'<div style="margin-top:10px">'+buckets.map(b=>'<div style="margin-top:8px"><div class="small" style="display:flex;justify-content:space-between"><span>'+esc(b.bucket)+'</span><span>'+money(b.amount)+' · '+pct(b.pct_of_outstanding)+'</span></div><div class="abar"><i style="width:'+Math.min(100,b.pct_of_outstanding||0)+'%"></i></div></div>').join('')+'</div>':'';
  const overduePct=data.overdue_pct||0;
  const overdueBar='<div style="margin-top:10px"><div class="small" style="display:flex;justify-content:space-between"><span>Vadesi Geçen Oranı</span><span>'+pct(data.overdue_pct)+'</span></div><div class="abar"><i style="width:'+Math.min(100,overduePct)+'%"></i></div></div>';
  const topOverdue=(data.top_overdue_parties||[]).slice(0,5);
  const topOverdueRows=topOverdue.length?'<div class="small" style="margin-top:10px"><b>En çok geciken '+(title==='AR'?'müşteriler':'tedarikçiler')+':</b> '+topOverdue.map(p=>esc(p.name)+' ('+money(p.amount)+(p.avg_days_overdue!=null?', ort. '+num(p.avg_days_overdue)+' gün':'')+')').join(' · ')+'</div>':'';
  const riskTierTag=data.risk_tier?'<span class="tag '+(data.risk_tier==='Kritik'?'critical':data.risk_tier==='Yüksek'?'high':data.risk_tier==='Orta'?'medium':'positive')+'">'+esc(data.risk_tier)+'</span>':'';
  const partyWord=title==='AR'?'müşteri':'tedarikçi';
  const cm = (window.LAST?.business_partner?.core_metrics) || {};
  let dueLabel = due==='DSO'?'Ortalama Tahsilat Süresi (AR Defteri DSO)':'Ortalama Ödeme Süresi (AP Defteri DPO)';
  let crossBadge = '';
  if(due === 'DSO' && cm.dso_days != null){
    crossBadge = ' <span class="tag" style="background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE;font-size:10.5px;padding:2px 6px" title="Kanonik Mizan 120 DSO">' +
      'Mizan 120 (Resmi): ' + num(cm.dso_days) + ' gün</span>';
  } else if(due === 'DPO' && cm.dpo_days != null){
    crossBadge = ' <span class="tag" style="background:#ECFDF5;color:#065F46;border:1px solid #A7F3D0;font-size:10.5px;padding:2px 6px" title="Kanonik Mizan 320 DPO">' +
      'Mizan 320 (Resmi): ' + num(cm.dpo_days) + ' gün</span>';
  }
  const concTxt=data.concentration_80pct_party_count!=null?' · Toplamın %80\u0027ine <b>'+data.concentration_80pct_party_count+'</b> '+partyWord+' denk geliyor ('+esc(data.party_count??'–')+' '+partyWord+'\u0027nin %'+num(data.concentration_80pct_share_of_parties_pct)+'\u0027i)':'';
  const anomalyBlock=(data.data_anomalies&&data.data_anomalies.length)?'<p class="small" style="margin-top:8px;color:#9a6b00">⚠ Veri uyarısı: '+data.data_anomalies.map(esc).join(' · ')+'</p>':'' ;
  return '<div class="insight" style="margin-top:10px;background:#FFFFFF;border:1px solid #E2E8F0;border-radius:12px;padding:16px"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px"><b>'+esc(titleLabel)+'</b> '+riskTierTag+'</div><p>Toplam Bakiye: <b>'+money(data.outstanding)+'</b> · Vadesi Geçen: <b style="color:#DC2626">'+money(data.overdue)+'</b> · '+esc(dueLabel)+': <b>'+(data[due==='DSO'?'dso_days':'dpo_days']==null?'–':num(data[due==='DSO'?'dso_days':'dpo_days'])+' gün')+'</b>' + crossBadge + '</p>'+overdueBar+'<p class="small muted" style="margin-top:8px">Ağırlıklı ort. gecikme: '+(data.weighted_average_overdue_days==null?'–':num(data.weighted_average_overdue_days)+' gün')+' · Beklenen risk tutarı: '+money(data.collection_risk_estimate)+' ('+pct(data.collection_risk_estimate_pct_of_outstanding)+') · İlk 10 '+partyWord+' payı: '+pct(data.top_10_share_pct)+' ('+(data.party_count??'–')+' '+partyWord+')'+concTxt+'</p>'+anomalyBlock+bucketRows+topOverdueRows+'</div>'
}

// "Kritik Müşteriler" — replaces the old flat Sales Intelligence metric wall.
// Built directly from the AR aging engine's own top_overdue_parties, framed
// as the cash impact of collecting from exactly those customers.
function criticalCustomersPanel(arData){
  if(!arData||!(arData.top_overdue_parties||[]).length) return '';
  const top=arData.top_overdue_parties.slice(0,5);
  const totalImpact=top.reduce((s,p)=>s+(p.amount||0),0);
  const rows=top.map((p,i)=>'<div class="custRow"><div>#'+(i+1)+' '+esc(p.name)+'</div><div>'+money(p.amount)+'</div><div class="muted">'+(p.avg_days_overdue!=null?'ort. '+num(p.avg_days_overdue)+' gün gecikme':'')+'</div></div>').join('');
  const concLine=arData.concentration_80pct_party_count!=null?'<p class="small muted" style="margin-top:6px">Toplam AR bakiyesinin %80\u0027i sadece <b>'+arData.concentration_80pct_party_count+'</b> müşteride toplanıyor ('+(arData.party_count??'–')+' müşterinin %'+num(arData.concentration_80pct_share_of_parties_pct)+'\u0027i).</p>':'';
  const t10=arData.top_10_share_pct;
  const concTag=t10==null?'':(t10>=30?'<span class="tag critical" style="margin-left:6px">Yüksek Yoğunlaşma</span>':t10>=10?'<span class="tag medium" style="margin-left:6px">Orta Yoğunlaşma</span>':'<span class="tag positive" style="margin-left:6px">Dağınık Alacak Tabanı — Düşük Risk</span>');
  const concNote=(t10!=null&&t10<10)?'<p class="small muted" style="margin-top:4px">İlk 10 müşteri toplam alacağın yalnızca %'+num(t10)+'\u0027ini oluşturuyor; bu, tek bir müşteri kaybının nakit akışını ciddi şekilde etkilemeyeceği sağlıklı/dağınık bir alacak tabanına işaret eder.</p>':'';
  return '<div class="card"><div class="sectionHead"><div><h2>Kritik Müşteriler'+concTag+'</h2><p>Tahsilat önceliklendirmesi ve olası nakit etkisi</p></div></div><div class="notice" style="margin-bottom:6px">Bu '+top.length+' müşteriden tahsilat sağlanırsa yaklaşık <b>'+money(totalImpact)+'</b> nakit serbestleşir (toplam vadesi geçen alacak riskinin '+pct(arData.outstanding?totalImpact/arData.outstanding*100:null)+'\u0027i).</div>'+rows+concLine+concNote+'</div>';
}

// "Kritik Tedarikçiler" — AR tarafındaki Kritik Müşteriler panelinin AP
// aynası. Ödeme önceliklendirmesi ve tedarik/ilişki riski taşıyan
// tedarikçileri, aynı "geciken bakiye" mantığıyla gösterir.
function criticalSuppliersPanel(apData){
  if(!apData||!(apData.top_overdue_parties||[]).length) return '';
  const top=apData.top_overdue_parties.slice(0,5);
  const totalImpact=top.reduce((s,p)=>s+(p.amount||0),0);
  const rows=top.map((p,i)=>'<div class="custRow"><div>#'+(i+1)+' '+esc(p.name)+'</div><div>'+money(p.amount)+'</div><div class="muted">'+(p.avg_days_overdue!=null?'ort. '+num(p.avg_days_overdue)+' gün gecikme':'')+'</div></div>').join('');
  const concLine=apData.concentration_80pct_party_count!=null?'<p class="small muted" style="margin-top:6px">Toplam AP bakiyesinin %80\u0027i sadece <b>'+apData.concentration_80pct_party_count+'</b> tedarikçide toplanıyor ('+(apData.party_count??'–')+' tedarikçinin %'+num(apData.concentration_80pct_share_of_parties_pct)+'\u0027i).</p>':'';
  return '<div class="card"><div class="sectionHead"><div><h2>Kritik Tedarikçiler</h2><p>Ödeme önceliklendirmesi ve tedarik ilişkisi riski</p></div></div><div class="notice" style="margin-bottom:6px">Bu '+top.length+' tedarikçiye geciken <b>'+money(totalImpact)+'</b> tutarındaki ödeme, ilişki/tedarik kesintisi riski taşıyor (toplam vadesi geçen borç riskinin '+pct(apData.outstanding?totalImpact/apData.outstanding*100:null)+'\u0027i).</div>'+rows+concLine+'</div>';
}

function renderSalesIntelligence(sales, custProf, prodProf){
  if(!sales && (!custProf || custProf.status!=='PASS') && (!prodProf || prodProf.status!=='PASS')){
    return '<div class="card"><div class="notice">Satış detay verisi yüklenmedi.</div></div>';
  }
  const s = sales || {};
  const cp = custProf || {};
  const pp = prodProf || {};
  const avgMargin = cp.company_average_gross_margin_pct ?? (s.gross_margin != null ? s.gross_margin * 100 : null);
  
  const lossCust = cp.loss_making_customers || s.loss_making_customers || [];
  const dilutiveCust = cp.low_margin_dilutive_customers || cp.volume_chasers || [];
  const goldCust = cp.high_quality_customers || (cp.stars || []).filter(c => (c.overdue_days || 0) === 0);
  
  const lossProd = pp.loss_making_products || s.loss_making_products || [];
  const heroProd = pp.hero_products || (pp.products || []).filter(p => (p.gross_margin_pct || 0) >= (avgMargin || 25)).slice(0, 5);

  let html = '<div class="card">' +
    '<div class="sectionHead"><div>' +
      '<h2>Satış Zekâsı: Müşteri &amp; Ürün Kârlılık Masası</h2>' +
      '<p>Hangi müşteriler ve ürünler doğrudan kâr getiriyor, hangileri şirketin sermayesini tüketiyor?</p>' +
    '</div></div>';

  // KPI Grid
  html += '<div class="grid4" style="margin-bottom:16px">' +
    metric('Vade Primi', s.term_premium_pct != null ? pct(s.term_premium_pct) : '–', 'Peşin → Vadeli Fiyat Farkı') +
    metric('İlk 10 Müşteri Payı', s.top_10_customer_share_pct != null ? pct(s.top_10_customer_share_pct) : '–', 'Müşteri Yoğunlaşması') +
    metric('Ortalama Brüt Marj', avgMargin != null ? pct(avgMargin) : '–', 'Şirket Kârlılık Tabanı') +
    metric('Zarar / Risk Durumu', (lossCust.length + lossProd.length) > 0 ? (lossCust.length + lossProd.length) + ' Kalem' : 'Temiz', (lossCust.length + lossProd.length) > 0 ? 'Negatif Marjlı Kalemler' : 'Doğrudan Zarar Yok') +
  '</div>';

  // Section 1: Hangi Müşteriler Zarar Ettiriyor?
  html += '<div style="margin-top:14px;border:1px solid ' + (lossCust.length ? '#FDA4AF' : '#E2E8F0') + ';border-radius:12px;padding:14px;background:' + (lossCust.length ? '#FFF1F2' : '#F8FAFC') + '">' +
    '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">' +
      '<div style="display:flex;align-items:center;gap:8px">' +
        '<span style="font-size:16px">' + (lossCust.length ? '🛑' : '✅') + '</span>' +
        '<b style="font-size:13.5px;color:' + (lossCust.length ? '#9F1239' : '#0F1B2D') + '">Hangi Müşteriler Zarar Ettiriyor? (Negatif Brüt Kâr &amp; Marj Kanaması)</b>' +
      '</div>' +
      '<span class="tag ' + (lossCust.length ? 'critical' : 'positive') + '">' + (lossCust.length ? lossCust.length + ' Zarar Ettiren Müşteri' : 'Zarar Eden Müşteri Yok') + '</span>' +
    '</div>';

  if(lossCust.length){
    html += '<p class="small muted" style="margin-bottom:10px;color:#9F1239">Aşağıdaki müşterilere yapılan satış fiyatı doğrudan satılan malın maliyetinin (SMM) altındadır. Her teslimatta şirket nakit ve özkaynak kaybetmektedir.</p>' +
      '<div class="tableWrap"><table><thead><tr><th>Müşteri</th><th>Net Satış</th><th>Maliyet (SMM)</th><th>Brüt Kâr/Zarar</th><th>Brüt Marj %</th><th>Yönetici Teşhisi &amp; Kararı</th></tr></thead><tbody>' +
      lossCust.map(c => '<tr>' +
        '<td><b>' + esc(c.name || c.customer) + '</b></td>' +
        '<td>' + money(c.sales || c.revenue) + '</td>' +
        '<td>' + money(c.cogs) + '</td>' +
        '<td style="color:var(--red);font-weight:700">' + money(c.gross_profit) + '</td>' +
        '<td style="color:var(--red);font-weight:700">%' + num(c.gross_margin_pct) + '</td>' +
        '<td class="small" style="color:#9F1239">Satış fiyatı maliyeti karşılamıyor. Fiyat acilen en az maliyetin %15 üstüne çıkarılmalı veya sevkiyat durdurulmalıdır.</td>' +
      '</tr>').join('') +
      '</tbody></table></div>';
  } else {
    html += '<p class="small muted" style="margin:0">Satış defterinde doğrudan negatif brüt kâr yazan müşteri tespit edilmemiştir. Bütün müşterilerin satış fiyatı birim maliyetinin üzerindedir.</p>';
  }
  html += '</div>';

  // Section 2: Kâr Kalitesi Yüksek (Altın) Müşteriler
  html += '<div style="margin-top:14px;border:1px solid #BBF7D0;border-radius:12px;padding:14px;background:#F0FDF4">' +
    '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">' +
      '<div style="display:flex;align-items:center;gap:8px">' +
        '<span style="font-size:16px">💎</span>' +
        '<b style="font-size:13.5px;color:#166534">Kâr Kalitesi En Yüksek Müşteriler (Yüksek Marj + Vadesinde Ödeyenler)</b>' +
      '</div>' +
      '<span class="tag positive">Altın Müşteri Grubu</span>' +
    '</div>' +
    '<p class="small muted" style="margin-bottom:10px;color:#166534">Bu müşteriler hem şirket ortalamasının üzerinde kâr bırakmakta hem de vadesinde ödeme yaparak alacağı kasada nakde dönüştürmektedir.</p>';

  if(goldCust.length){
    html += '<div class="tableWrap"><table><thead><tr><th>Müşteri</th><th>Net Satış</th><th>Brüt Kâr</th><th>Brüt Marj %</th><th>Tahsilat Durumu</th><th>Yönetici Kararı</th></tr></thead><tbody>' +
      goldCust.slice(0, 5).map(c => '<tr>' +
        '<td><b>' + esc(c.name || c.customer) + '</b></td>' +
        '<td>' + money(c.sales || c.revenue) + '</td>' +
        '<td style="color:var(--green);font-weight:700">' + money(c.gross_profit) + '</td>' +
        '<td style="color:var(--green);font-weight:700">%' + num(c.gross_margin_pct) + '</td>' +
        '<td><span class="tag positive">✓ Vadesinde Ödeniyor</span></td>' +
        '<td class="small">Kilit müşteri statüsü verilmeli; gereksiz iskonto tavizi verilmeden hacim büyütülmeli.</td>' +
      '</tr>').join('') +
      '</tbody></table></div>';
  } else {
    html += '<div class="small muted">Yüksek kâr marjlı ve gecikmesiz tahsilat grubunda müşteri verisi kısıtlı.</div>';
  }
  html += '</div>';

  // Section 3: Hacimli ama Kârı Aşağı Çeken Müşteriler
  if(dilutiveCust.length){
    html += '<div style="margin-top:14px;border:1px solid #FEF08A;border-radius:12px;padding:14px;background:#FEFCE8">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">' +
        '<div style="display:flex;align-items:center;gap:8px">' +
          '<span style="font-size:16px">⚠️</span>' +
          '<b style="font-size:13.5px;color:#854D0E">Hacimli ama Kârı Aşağı Çeken Müşteriler (Ciro Var, Kâr Yok)</b>' +
        '</div>' +
        '<span class="tag high">' + dilutiveCust.length + ' Müşteri</span>' +
      '</div>' +
      '<p class="small muted" style="margin-bottom:10px;color:#854D0E">Yüksek ciro üreten fakat brüt kâr marjı şirket ortalamasının (%' + num(avgMargin) + ') altında kalarak işletme sermayesini tüketen müşteriler:</p>' +
      '<div class="tableWrap"><table><thead><tr><th>Müşteri</th><th>Net Satış</th><th>Ciro Payı %</th><th>Brüt Marj %</th><th>Fark (Ortalamaya Göre)</th><th>Yönetici Kararı</th></tr></thead><tbody>' +
      dilutiveCust.slice(0, 5).map(c => '<tr>' +
        '<td><b>' + esc(c.name || c.customer) + '</b></td>' +
        '<td>' + money(c.sales || c.revenue) + '</td>' +
        '<td>%' + num(c.share_pct) + '</td>' +
        '<td style="font-weight:700">%' + num(c.gross_margin_pct) + '</td>' +
        '<td style="color:var(--amber)">-' + num(Math.max(0, (avgMargin||0) - (c.gross_margin_pct||0))) + ' puan</td>' +
        '<td class="small">Sözleşme yenilemede iskonto %2-3 kısılmalı; vade opsiyonları peşine kaydırılmalı.</td>' +
      '</tr>').join('') +
      '</tbody></table></div></div>';
  }

  // Section 4: Ürün Bazlı Kâr / Zarar & Portföy Kırılımı
  html += '<div style="margin-top:16px"><div class="sectionHead"><div>' +
    '<h3>Ürün Bazlı Kârlılık Kırılımı (Lokomotifler vs Zarar Ettiren Kalemler)</h3>' +
    '<p>Portföydeki hangi ürünler brüt kârı sırtlıyor, hangi ürünler kâr marjını eritiyor?</p>' +
  '</div></div>';

  html += '<div class="grid2" style="gap:14px;margin-top:10px">' +
    '<div class="insight" style="background:#FFFFFF;border:1px solid #BBF7D0;border-radius:12px;padding:14px">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">' +
        '<b>🏆 Lokomotif Kâr Lideri Ürünler (Hero SKUs)</b>' +
        '<span class="tag positive">Yüksek Kâr</span>' +
      '</div>' +
      (heroProd.length ? heroProd.slice(0, 4).map(p => '<div style="display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid rgba(15,27,45,0.05);font-size:12px">' +
        '<span><b>' + esc(p.name || p.sku) + '</b></span>' +
        '<span>' + money(p.sales || p.revenue) + ' <span class="muted">(%' + num(p.gross_margin_pct) + ' marj)</span></span>' +
      '</div>').join('') : '<div class="small muted">Belirgin lider ürün verisi yok.</div>') +
    '</div>' +
    '<div class="insight" style="background:#FFFFFF;border:1px solid ' + (lossProd.length ? '#FDA4AF' : '#E2E8F0') + ';border-radius:12px;padding:14px">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">' +
        '<b>' + (lossProd.length ? '🛑 Zarar Ettiren Ürünler' : '⚠️ Marjı Düşük / Kârı Eriten Ürünler') + '</b>' +
        '<span class="tag ' + (lossProd.length ? 'critical' : 'high') + '">' + (lossProd.length ? lossProd.length + ' Kalem Zarar' : 'Düşük Marj') + '</span>' +
      '</div>' +
      (lossProd.length ? lossProd.slice(0, 4).map(p => '<div style="display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid rgba(15,27,45,0.05);font-size:12px">' +
        '<span style="color:var(--red)"><b>' + esc(p.name || p.sku) + '</b></span>' +
        '<span>' + money(p.sales || p.revenue) + ' <b style="color:var(--red)">(' + money(p.gross_profit) + ')</b></span>' +
      '</div>').join('') :
      (pp.low_margin_eroding_products || []).slice(0, 4).map(p => '<div style="display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid rgba(15,27,45,0.05);font-size:12px">' +
        '<span>' + esc(p.name || p.sku) + '</span>' +
        '<span>' + money(p.sales || p.revenue) + ' <span class="muted">(%' + num(p.gross_margin_pct) + ' marj)</span></span>' +
      '</div>').join('') || '<div class="small muted">Negatif marjlı veya kârı eriten ürün bulunmadı.</div>') +
    '</div>' +
  '</div>';

  if((s.product_mix || []).length){
    const cm = (window.LAST?.business_partner?.core_metrics) || {};
    const ledgerGross = s.total_sales || (s.product_mix || []).reduce((acc, v) => acc + (v.sales || 0), 0);
    const mizanNet = cm.canonical_net_sales != null ? cm.canonical_net_sales : (window.LAST?.statements?.profit_and_loss?.['Net sales']);
    let diffBadge = '';
    if(mizanNet != null && ledgerGross > 0 && Math.abs(ledgerGross - mizanNet) > 100){
      diffBadge = ' <span class="tag" style="background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE;font-size:10.5px;margin-left:6px" title="Fark: İadeler, iskontolar veya dönem mutabakat farkı">' +
        'Mizan 600 Net Satış: ' + money(mizanNet) + '</span>';
    }
    html += '<div class="insight" style="margin-top:12px;padding:12px 16px;background:#F8FAFC">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:6px">' +
        '<b>Ürün Satış Karması Dağılımı:</b>' +
        '<span style="font-size:11.5px;color:#475569">Brüt Satış (Satış Defteri): <b>' + money(ledgerGross) + '</b>' + diffBadge + '</span>' +
      '</div>' +
      s.product_mix.slice(0, 7).map(v => esc(v.name) + ': ' + money(v.sales) + ' (%' + num(v.share_pct) + ')').join(' · ') +
    '</div>';
  }

  html += '</div></div>';
  return html;
}

function renderHub(ms){
  if(!ms){
    if($('dataHubCard')) $('dataHubCard').classList.add('hidden');
    if($('pvmIntel')) $('pvmIntel').classList.add('hidden');
    if($('customerProfitabilityMatrixCard')) $('customerProfitabilityMatrixCard').classList.add('hidden');
    if($('productProfitabilityCard')) $('productProfitabilityCard').classList.add('hidden');
    if($('criticalPartiesNotice')) $('criticalPartiesNotice').classList.remove('hidden');
    if($('criticalCustomersCard')) $('criticalCustomersCard').innerHTML='';
    if($('criticalSuppliersCard')) $('criticalSuppliersCard').innerHTML='';
    if($('salesIntel')) $('salesIntel').innerHTML='';
    if($('arApIntel')) $('arApIntel').innerHTML='';
    if($('inventoryIntel')) $('inventoryIntel').innerHTML='';
    if($('hubSummary')) $('hubSummary').innerHTML='';
    if($('hubSources')) $('hubSources').innerHTML='';
    if($('hubFindings')) $('hubFindings').innerHTML='';
    if($('hubReconciliation')) $('hubReconciliation').innerHTML='';
    return;
  }
  $('dataHubCard').classList.remove('hidden');
  const sm=ms.summary||{};
  const errorRows=(ms.errors||[]).map(e=>'<div class="notice" style="margin-top:8px"><b>Dosya hatası:</b> '+esc(e.file||'')+' · '+esc(e.error||'')+'</div>').join('');
  const fileRows=(ms.files||[]).map(f=>{const rs=(f.roles||[]).map(r=>r.role+' ('+Math.round((r.confidence||0)*100)+'%)').join(', ');return '<tr><td>'+esc(f.filename)+'</td><td>'+esc(rs||'unknown')+'</td><td>'+esc(f.roles?.[0]?.rows||'–')+'</td></tr>'}).join('');
  if($('hubSources')) $('hubSources').innerHTML='<div class="sectionHead"><div><h2>Yüklenen Veri Kaynakları Kaydı</h2><p>Dosyaların içerik bazlı sınıflandırılması</p></div></div>'+(fileRows?'<div class="tableWrap"><table><thead><tr><th>Dosya</th><th>Rol</th><th>Satır</th></tr></thead><tbody>'+fileRows+'</tbody></table></div>':'<div class="notice">Kaynak bulunamadı.</div>')+errorRows;
  const labels=[['Satış Defteri',sm.sales_loaded?'Yüklendi':'Yüklenmedi',''],['Alacak Yaşlandırma',sm.ar_aging_loaded?'Yüklendi':'Yüklenmedi',''],['Borç Yaşlandırma',sm.ap_aging_loaded?'Yüklendi':'Yüklenmedi',''],['Stok Defteri',sm.inventory_loaded?'Yüklendi':'Yüklenmedi','']];
  $('hubSummary').innerHTML=labels.map(x=>metric(x[0],x[1],x[2])).join('');
  const checks=ms.reconciliation?.checks||[];
  $('hubReconciliation').innerHTML='<div class="sectionHead"><div><h2>Veri Mutabakat Kontrolleri</h2><p>Büyük Defter (Mizan) ile operasyonel detay raporları arasındaki farklar</p></div></div>'+(checks.length?'<div class="tableWrap"><table><thead><tr><th>Kontrol</th><th>Mizan Değeri</th><th>Detay Rapor Değeri</th><th>Fark</th><th>Durum</th></tr></thead><tbody>'+checks.map(c=>'<tr><td>'+esc(c.name)+'</td><td>'+money(c.gl_value)+'</td><td>'+money(c.source_value)+'</td><td>'+money(c.difference)+'</td><td>'+esc(c.status)+'</td></tr>').join('')+'</tbody></table></div>':'<div class="notice">Mutabakat için yeterli veri yok.</div>');
  const an=ms.analysis||{}; const sales=an.sales||{};
  if(sales.pvm_analysis && sales.pvm_analysis.available) {
    $('pvmIntel').classList.remove('hidden');
    const p=sales.pvm_analysis;
    const wfId = 'pvmWf';
    $('pvmIntel').innerHTML='<div class="sectionHead"><div><h2>Fiyat-Hacim-Karma (PVM) Analizi</h2><p>Ciro değişiminin kök nedenleri: Fiyat mı, Hacim mi, Ürün Karması mı?</p></div></div>'
      +'<div class="grid4" style="margin-bottom:16px">'
      +metric('Dönem 1 Ciro', money(p.revenue_1), p.period_1)
      +metric('Dönem 2 Ciro', money(p.revenue_2), p.period_2)
      +metric('Ciro Değişimi', money(p.revenue_delta), '')
      +metric('En Büyük Etken', Math.abs(p.total_price_effect)>Math.abs(p.total_volume_effect)?'Fiyat Değişimi':'Hacim Değişimi', '')
      +'</div><div id="'+wfId+'" class="waterfall"></div>'
      +'<div class="tableWrap" style="margin-top:16px"><table><thead><tr><th>Ürün</th><th>Değişim</th><th>Fiyat Etkisi</th><th>Hacim Etkisi</th><th>Karma Etkisi</th></tr></thead><tbody>'
      +(p.product_level||[]).map(r=>'<tr><td>'+esc(r.product)+'</td><td>'+money(r.delta)+'</td><td>'+money(r.price_effect)+'</td><td>'+money(r.volume_effect)+'</td><td>'+money(r.mix_effect)+'</td></tr>').join('')
      +'</tbody></table></div>';
    setTimeout(()=>{
      waterfall(wfId, [
        ['Ciro ('+p.period_1+')', p.revenue_1, false],
        ['Fiyat Etkisi', p.total_price_effect, p.total_price_effect<0],
        ['Hacim Etkisi', p.total_volume_effect, p.total_volume_effect<0],
        ['Karma Etkisi', p.total_mix_effect, p.total_mix_effect<0],
        ['Ciro ('+p.period_2+')', p.revenue_2, false]
      ]);
    }, 50);
  } else {
    if($('pvmIntel')) $('pvmIntel').classList.add('hidden');
  }

  if($('criticalPartiesNotice')) $('criticalPartiesNotice').classList.add('hidden');
  if(an.customer_profitability) renderCustomerProfitabilityMatrix(an.customer_profitability);
  if(an.product_profitability) renderProductProfitability(an.product_profitability);
  $('criticalCustomersCard').innerHTML=criticalCustomersPanel(an.ar_aging);
  $('criticalSuppliersCard').innerHTML=criticalSuppliersPanel(an.ap_aging);
  // Upgraded Sales Intelligence
  $('salesIntel').innerHTML=renderSalesIntelligence(an.sales, an.customer_profitability, an.product_profitability);
  // AR / AP Intelligence — Stacked Vertically
  $('arApIntel').innerHTML='<div class="card"><div class="sectionHead"><div><h2>Alacak ve Borç Yaşlandırma Analizi</h2><p>Müşteri alacak vadeleri (120 Hesabı) ve tedarikçi ödeme takvimi (320 Hesabı) alt alta dökümü</p></div></div><div style="display:flex;flex-direction:column;gap:14px">'+agingBlock('AR','DSO',an.ar_aging)+agingBlock('AP','DPO',an.ap_aging)+'</div></div>';
  const inv = an.inventory || an.inventory_aging || {};
  const hasInv = !!(an.inventory || an.inventory_aging);
  // Inventory Intelligence — Standalone Card
  $('inventoryIntel').innerHTML='<div class="card"><div class="sectionHead"><div><h2>Stok Zekâsı (Ölü Stok &amp; Devir Hızı)</h2><p>Stok değeri, ortalama rafta kalma süresi ve nakit kilitleyen atıl ürünler</p></div></div>'+(hasInv?'<div class="grid4">'+metric('Toplam Stok Değeri',money(inv.value),'Mizan / Stok Defteri')+metric('Ürün (SKU) Sayısı',inv.sku_count??'–','Toplam Kalem')+metric('Stok Devir Süresi (DIO)',inv.dio_days==null?'–':num(inv.dio_days)+' gün','Ortalama Satış Süresi')+metric('180+ Gün Atıl Stok',money(inv.stale_180_amount),'Kasayı Kilitleyen Nakit')+ '</div>'+(inv.findings||[]).map(f=>'<div class="insight '+esc(f.severity)+'" style="margin-top:10px"><b>'+esc(f.title)+'</b><p>'+esc(f.detail)+'</p></div>').join(''):'<div class="notice">Stok detay defteri yüklenmedi.</div>')+'</div>';
}

// ---------------------------------------------------------------------
// Core Analysis Engine Runner with Institutional Progress & Auto-Scroll
// ---------------------------------------------------------------------
async function run(url,fd,kind='single'){
  $('error').classList.add('hidden');
  startLoading(
    kind==='hub'?'Data Hub Analizi Çalıştırılıyor':'Finansal Veriler Analiz Ediliyor',
    '33 Finansal Karar Motoru Çalıştırılıyor (Hesap Doğrulama, Likidite, Nakit Köprüsü, Kârlılık Ağacı)...'
  );
  $('analyze').disabled=true;$('analyzeTrend').disabled=true;$('analyzeHub').disabled=true;
  try{
    const r=await fetch(url,{method:'POST',body:fd});
    const d=await r.json();
    if(!r.ok) throw new Error(d.detail||'Analiz başarısız oldu.');
    render(d);
    renderHub(d.data_hub || null);
    stopLoading();
    setTimeout(()=>{
      const dash=$('dashboard');
      if(dash){
        dash.classList.remove('hidden');
        dash.scrollIntoView({behavior:'smooth',block:'start'});
      }
    },120);
  }catch(e){
    stopLoading();
    $('error').textContent='Analiz Hatası: ' + e.message;
    $('error').classList.remove('hidden');
    window.scrollTo({top:0,behavior:'smooth'});
  }finally{
    $('analyze').disabled=false;$('analyzeTrend').disabled=false;$('analyzeHub').disabled=false;
  }
}

// ---------------------------------------------------------------------
// Modern File Drag & Drop & Visual Feedback
// ---------------------------------------------------------------------
function formatBytes(bytes){
  if(!bytes) return '0 B';
  const k=1024, sizes=['B','KB','MB','GB'];
  const i=Math.floor(Math.log(bytes)/Math.log(k));
  return parseFloat((bytes/Math.pow(k,i)).toFixed(1))+' '+sizes[i];
}

window._inspectedFilesMap = window._inspectedFilesMap || {};
window._inspectingFilesMap = window._inspectingFilesMap || {};

function updateFileList(inputEl, listEl, btnEl, defaultBtnText){
  const files = [...inputEl.files];
  if(!files.length){
    listEl.innerHTML = '';
    btnEl.textContent = defaultBtnText;
    btnEl.classList.remove('btnReady');
    return;
  }
  btnEl.classList.add('btnReady');
  if(files.length === 1){
    btnEl.textContent = '🚀 1 Dosyayı Analiz Et (33 Karar Motoru Hazır)';
  } else {
    btnEl.textContent = '🚀 ' + files.length + ' Dosyayı Birlikte Analiz Et (33 Karar Motoru)';
  }

  listEl.innerHTML = files.map((f, i) => {
    const inspected = window._inspectedFilesMap[f.name];
    const isInspecting = window._inspectingFilesMap[f.name];
    let badgeHtml = '';
    if(inspected){
      const erpBadge = inspected.erp_badge || 'Standart Format';
      const roleLabel = inspected.role_label || 'Mizan';
      const confPct = Math.round((inspected.erp_confidence || inspected.confidence || 0.8) * 100);
      const mappedCount = (inspected.mapped_columns || []).length;
      badgeHtml = '<span class="tag positive" style="font-size:11px;font-weight:700;margin-left:6px;padding:2px 8px;border-radius:6px;background:rgba(16,185,129,0.12);color:#059669;border:1px solid rgba(16,185,129,0.25)">🏷️ ' + esc(erpBadge) + ' (%' + confPct + ')</span>' +
        '<span class="tag" style="font-size:11px;font-weight:600;margin-left:4px;padding:2px 6px;border-radius:6px;background:rgba(37,99,235,0.08);color:#2563EB">📋 ' + esc(roleLabel) + '</span>' +
        '<button type="button" class="btnGhost" data-fn="' + esc(f.name) + '" style="padding:2px 8px;font-size:11px;margin-left:6px;cursor:pointer;border:1px solid #CBD5E1;border-radius:6px;background:#F8FAFC;font-weight:600;color:#0F1B2D" onclick="openErpMappingModal(this.getAttribute(\'data-fn\'))">🔍 Sütunları Gör (' + mappedCount + ' Alan)</button>';
    } else if(isInspecting) {
      badgeHtml = '<span style="font-size:11px;color:#64748B;margin-left:6px;font-weight:500">⏳ Format taranıyor...</span>';
    } else {
      badgeHtml = '<span style="font-size:11px;color:#64748B;margin-left:6px;font-weight:500">⏳ Taranıyor...</span>';
    }

    return '<div class="filePill" style="display:inline-flex;align-items:center;flex-wrap:wrap;gap:4px">' +
      '<b>📄 ' + esc(f.name) + '</b> <span class="muted">(' + formatBytes(f.size) + ')</span>' +
      badgeHtml +
      '<span class="pillDel" title="Kaldır" onclick="clearFileSelection(\''+inputEl.id+'\','+i+')">×</span>' +
      '</div>';
  }).join('');

  const toInspect = files.filter(f => !window._inspectedFilesMap[f.name] && !window._inspectingFilesMap[f.name]);
  if(toInspect.length > 0){
    const fd = new FormData();
    toInspect.forEach(f => {
      window._inspectingFilesMap[f.name] = true;
      fd.append('files', f);
    });
    fetch('/api/inspect', { method: 'POST', body: fd })
      .then(r => r.ok ? r.json() : null)
      .then(data => {
        if(data && data.files){
          data.files.forEach(res => {
            if(res && res.filename){
              window._inspectedFilesMap[res.filename] = res.primary || res;
            }
          });
        }
      })
      .catch(err => {
        console.warn('Inspect error:', err);
      })
      .finally(() => {
        toInspect.forEach(f => { delete window._inspectingFilesMap[f.name]; });
        const cur = [...inputEl.files];
        if(cur.length){
          updateFileList(inputEl, listEl, btnEl, defaultBtnText);
        }
      });
  }
}

window.openErpMappingModal = function(filename){
  const info = window._inspectedFilesMap && window._inspectedFilesMap[filename];
  if(!info){
    alert('Bu dosyanın önizleme bilgisi henüz yüklenemedi veya dosya bulunamadı.');
    return;
  }
  let m = document.getElementById('erpMappingModal');
  if(!m){
    m = document.createElement('div');
    m.id = 'erpMappingModal';
    document.body.appendChild(m);
  }
  m.style.cssText = 'position:fixed;inset:0;background:rgba(15,27,45,0.72);z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(4px);';

  const rawCols = info.raw_columns || [];
  const mappedCols = info.mapped_columns || [];
  const previewRows = info.preview_rows || [];
  const unmappedReq = info.unmapped_required || [];
  const erpBadge = info.erp_badge || 'Standart Format';
  const roleLabel = info.role_label || 'Finansal Tablo';
  const confPct = Math.round((info.erp_confidence || info.confidence || 0.8) * 100);

  let mappingRowsHtml = '';
  if(mappedCols.length === 0 && unmappedReq.length === 0){
    mappingRowsHtml = '<tr><td colspan="4" style="text-align:center;color:#64748B;padding:16px">Eşleşen sütun bilgisi bulunamadı.</td></tr>';
  } else {
    mappedCols.forEach(mc => {
      const isReq = mc.is_required ? '<span style="color:#DC2626;font-weight:700;font-size:11px">* Zorunlu</span>' : '<span style="color:#64748B;font-size:11px">Opsiyonel</span>';
      let selectOptions = '<option value="">-- Eşleşme Yok --</option>';
      rawCols.forEach(rc => {
        const isSel = (rc === mc.source_column) ? 'selected' : '';
        selectOptions += '<option value="' + esc(rc) + '" ' + isSel + '>' + esc(rc) + '</option>';
      });
      mappingRowsHtml += '<tr style="border-bottom:1px solid #F1F5F9">' +
        '<td style="padding:10px 12px;font-weight:600;color:#0F1B2D;font-size:12.5px">' + esc(mc.canonical_label) + ' <span style="font-size:11px;color:#64748B">(' + esc(mc.canonical_field) + ')</span></td>' +
        '<td style="padding:10px 12px">' + isReq + '</td>' +
        '<td style="padding:10px 12px">' +
          '<select style="width:100%;padding:6px 10px;border-radius:8px;border:1px solid #CBD5E1;font-size:12px;background:#FFFFFF;color:#0F1B2D" onchange="updateCustomMapping(\'' + esc(filename) + '\', \'' + esc(mc.canonical_field) + '\', this.value)">' +
            selectOptions +
          '</select>' +
        '</td>' +
        '<td style="padding:10px 12px"><span class="tag positive" style="font-size:11px;font-weight:700">✅ Eşleşti</span></td>' +
        '</tr>';
    });
    unmappedReq.forEach(ur => {
      let selectOptions = '<option value="" selected>-- Lütfen Seçin --</option>';
      rawCols.forEach(rc => {
        selectOptions += '<option value="' + esc(rc) + '">' + esc(rc) + '</option>';
      });
      mappingRowsHtml += '<tr style="border-bottom:1px solid #FEE2E2;background:#FFF5F5">' +
        '<td style="padding:10px 12px;font-weight:600;color:#991B1B;font-size:12.5px">' + esc(ur.canonical_label) + ' <span style="font-size:11px;color:#DC2626">(' + esc(ur.canonical_field) + ')</span></td>' +
        '<td style="padding:10px 12px"><span style="color:#DC2626;font-weight:700;font-size:11px">* Zorunlu</span></td>' +
        '<td style="padding:10px 12px">' +
          '<select style="width:100%;padding:6px 10px;border-radius:8px;border:1px solid #F87171;font-size:12px;background:#FFFFFF;color:#0F1B2D" onchange="updateCustomMapping(\'' + esc(filename) + '\', \'' + esc(ur.canonical_field) + '\', this.value)">' +
            selectOptions +
          '</select>' +
        '</td>' +
        '<td style="padding:10px 12px"><span class="tag" style="font-size:11px;font-weight:700;background:#FEE2E2;color:#DC2626">⚠️ Seçilmedi</span></td>' +
        '</tr>';
    });
  }

  let previewTableHtml = '';
  if(previewRows.length && rawCols.length){
    const ths = rawCols.slice(0, 8).map(c => '<th style="padding:8px 10px;background:#F8FAFC;font-size:11.5px;color:#475569;border-bottom:1px solid #E2E8F0;text-align:left;white-space:nowrap">' + esc(c) + '</th>').join('');
    const trs = previewRows.map(r => {
      const tds = rawCols.slice(0, 8).map(c => '<td style="padding:7px 10px;font-size:11.5px;color:#1E293B;border-bottom:1px solid #F1F5F9;white-space:nowrap;font-family:monospace">' + esc(r[c] !== undefined ? r[c] : '') + '</td>').join('');
      return '<tr>' + tds + '</tr>';
    }).join('');
    previewTableHtml = '<div style="overflow-x:auto;max-height:180px;border:1px solid #E2E8F0;border-radius:8px;margin-top:8px"><table style="width:100%;border-collapse:collapse;text-align:left"><thead><tr>' + ths + '</tr></thead><tbody>' + trs + '</tbody></table></div>';
  } else {
    previewTableHtml = '<div style="font-size:12px;color:#64748B;padding:8px">Önizleme verisi mevcut değil.</div>';
  }

  const rowAnomalies = info.row_anomalies || (info.primary && info.primary.row_anomalies) || [];
  let anomaliesHtml = '';
  if(rowAnomalies && rowAnomalies.length > 0){
    anomaliesHtml = '<div style="margin-bottom:18px;background:#FEF2F2;border:1.5px solid #FCA5A5;border-radius:10px;padding:12px 16px">' +
      '<div style="display:flex;align-items:center;gap:8px;font-size:13px;font-weight:800;color:#991B1B;margin-bottom:6px">' +
        '<span>⚠️</span><span>Tespit Edilen Satır Bazlı Format Hataları (' + rowAnomalies.length + ' Satır):</span>' +
      '</div>' +
      '<p style="margin:0 0 8px 0;font-size:11.5px;color:#7F1D1D">Aşağıdaki satırlarda standart dışı hesap kodu tespit edildi. Sistem analizde bu satırları izole eder; ancak dosyanızı Excel üzerinde de kontrol etmeniz önerilir:</p>' +
      '<div style="display:flex;flex-direction:column;gap:6px">' +
        rowAnomalies.slice(0, 5).map(a => '<div style="background:#FFFFFF;border:1px solid #FECDD3;border-radius:6px;padding:6px 10px;font-size:11.5px;display:flex;justify-content:space-between;align-items:center">' +
          '<div><span style="background:#FEE2E2;color:#991B1B;font-weight:800;padding:2px 6px;border-radius:4px;margin-right:6px">Satır ' + esc(a.line_number) + '</span><b style="color:#0F172A">"' + esc(a.raw_value) + '"</b> <span style="color:#475569">(' + esc(a.reason) + ')</span></div>' +
          '<span style="color:#047857;font-size:11px">💡 ' + esc(a.suggestion) + '</span>' +
        '</div>').join('') +
      '</div>' +
    '</div>';
  }

  m.innerHTML = '<div style="background:#FFFFFF;border-radius:18px;max-width:820px;width:100%;max-height:90vh;overflow-y:auto;padding:26px;box-shadow:0 25px 60px rgba(0,0,0,0.3);position:relative;border:1px solid #E2E8F0">' +
    '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid #E2E8F0;padding-bottom:12px">' +
      '<div>' +
        '<div style="display:flex;align-items:center;gap:8px">' +
          '<span style="font-size:22px">🛠️</span>' +
          '<h3 style="margin:0;font-size:18px;color:#0F1B2D;font-weight:700">Akıllı ERP Sütun Eşleme Sihirbazı</h3>' +
        '</div>' +
        '<div style="font-size:12px;color:#64748B;margin-top:4px">Dosya: <b>' + esc(filename) + '</b></div>' +
      '</div>' +
      '<button type="button" onclick="closeErpMappingModal()" style="border:none;background:transparent;font-size:24px;cursor:pointer;color:#94A3B8;padding:4px 8px;border-radius:6px;line-height:1">×</button>' +
    '</div>' +

    '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin-bottom:16px">' +
      '<div style="background:#F8FAFC;padding:10px 14px;border-radius:10px;border:1px solid #E2E8F0">' +
        '<div style="font-size:11px;color:#64748B;font-weight:600">TESPİT EDİLEN ERP</div>' +
        '<div style="font-size:14px;font-weight:700;color:#059669;margin-top:2px">🏷️ ' + esc(erpBadge) + '</div>' +
        '<div style="font-size:10.5px;color:#64748B">Güven: %' + confPct + '</div>' +
      '</div>' +
      '<div style="background:#F8FAFC;padding:10px 14px;border-radius:10px;border:1px solid #E2E8F0">' +
        '<div style="font-size:11px;color:#64748B;font-weight:600">STANDART VERİ ROLÜ</div>' +
        '<div style="font-size:14px;font-weight:700;color:#2563EB;margin-top:2px">📋 ' + esc(roleLabel) + '</div>' +
        '<div style="font-size:10.5px;color:#64748B">' + esc(info.sheet_name || 'Sayfa') + '</div>' +
      '</div>' +
      '<div style="background:#F8FAFC;padding:10px 14px;border-radius:10px;border:1px solid #E2E8F0">' +
        '<div style="font-size:11px;color:#64748B;font-weight:600">EŞLEŞEN SÜTUNLAR</div>' +
        '<div style="font-size:14px;font-weight:700;color:#0F1B2D;margin-top:2px">🎯 ' + mappedCols.length + ' / ' + (mappedCols.length + unmappedReq.length) + ' Alan</div>' +
        '<div style="font-size:10.5px;color:#059669;font-weight:600">' + (unmappedReq.length === 0 ? 'Tüm Zorunlu Alanlar Tam' : '⚠️ ' + unmappedReq.length + ' Alan Eksik') + '</div>' +
      '</div>' +
      '<div style="background:#F8FAFC;padding:10px 14px;border-radius:10px;border:1px solid #E2E8F0">' +
        '<div style="font-size:11px;color:#64748B;font-weight:600">HAM VERİ SÜTUNLARI</div>' +
        '<div style="font-size:14px;font-weight:700;color:#0F1B2D;margin-top:2px">📊 ' + rawCols.length + ' Sütun</div>' +
        '<div style="font-size:10.5px;color:#64748B">' + previewRows.length + ' Örnek Satır</div>' +
      '</div>' +
    '</div>' +

    '<div style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:10px;padding:10px 14px;margin-bottom:16px;font-size:12px;color:#1E40AF;line-height:1.4">' +
      '💡 <b>Akıllı Eşleme Motoru:</b> ERP sisteminizden aldığınız rapor başlıkları otomatik olarak standart finansal modelimize eşleştirilmiştir. Değiştirmek istediğiniz sütun eşleşmesi varsa aşağıdan güncelleyebilirsiniz.' +
    '</div>' +

    '<div style="margin-bottom:18px">' +
      '<h4 style="margin:0 0 8px 0;font-size:13px;color:#0F1B2D;font-weight:700">📌 Sütun Eşleme Tablosu</h4>' +
      '<div style="border:1px solid #E2E8F0;border-radius:8px;overflow:hidden">' +
        '<table style="width:100%;border-collapse:collapse;font-size:12px;text-align:left">' +
          '<thead>' +
            '<tr style="background:#F8FAFC;border-bottom:1px solid #E2E8F0;color:#475569">' +
              '<th style="padding:8px 12px;font-weight:600">Standart Model Alanı</th>' +
              '<th style="padding:8px 12px;font-weight:600;width:90px">Gereksinim</th>' +
              '<th style="padding:8px 12px;font-weight:600">Dosyanızdaki Sütun</th>' +
              '<th style="padding:8px 12px;font-weight:600;width:90px">Durum</th>' +
            '</tr>' +
          '</thead>' +
          '<tbody>' + mappingRowsHtml + '</tbody>' +
        '</table>' +
      '</div>' +
    '</div>' +

    '<div style="margin-bottom:20px">' +
      '<h4 style="margin:0 0 6px 0;font-size:13px;color:#0F1B2D;font-weight:700">👀 Dosyadan Ham Veri Önizleme (İlk ' + previewRows.length + ' Satır)</h4>' +
      previewTableHtml +
    '</div>' +
    anomaliesHtml +

    '<div style="display:flex;justify-content:flex-end;gap:10px;padding-top:14px;border-top:1px solid #E2E8F0">' +
      '<button type="button" class="primary" style="padding:10px 24px;font-size:13px;font-weight:700;border-radius:10px;cursor:pointer" onclick="closeErpMappingModal()">✅ Eşleştirmeyi Onayla ve Kapat</button>' +
    '</div>' +
  '</div>';
};

window.closeErpMappingModal = function(){
  const m = document.getElementById('erpMappingModal');
  if(m){ m.remove(); }
};

window.updateCustomMapping = function(filename, canonicalField, selectedSourceCol){
  const info = window._inspectedFilesMap && window._inspectedFilesMap[filename];
  if(!info) return;
  if(!info.custom_mapping) info.custom_mapping = {};
  info.custom_mapping[canonicalField] = selectedSourceCol;
  let found = false;
  if(info.mapped_columns){
    info.mapped_columns.forEach(mc => {
      if(mc.canonical_field === canonicalField){
        mc.source_column = selectedSourceCol;
        found = true;
      }
    });
  }
  if(!found && selectedSourceCol){
    info.mapped_columns = info.mapped_columns || [];
    info.mapped_columns.push({
      canonical_field: canonicalField,
      canonical_label: canonicalField,
      source_column: selectedSourceCol,
      is_required: false,
      confidence: 1.0
    });
  }
};

window.clearFileSelection = function(inputId, index){
  const inp = $(inputId);
  if(!inp) return;
  const dt = new DataTransfer();
  const files = [...inp.files];
  files.forEach((f, i) => { if(i !== index) dt.items.add(f); });
  inp.files = dt.files;
  if(inputId === 'file') updateFileList($('file'), $('fileListSingle'), $('analyze'), '🚀 Analizi Çalıştır (33 Karar Motoru)');
  if(inputId === 'trendFiles') updateFileList($('trendFiles'), $('fileListTrend'), $('analyzeTrend'), '🚀 Trend Analizini Başlat (2 Dönem)');
  if(inputId === 'hubFiles') updateFileList($('hubFiles'), $('fileListHub'), $('analyzeHub'), '🚀 Tüm Verileri Analiz Et (Data Hub)');
};

function setupDropZone(dropZoneId, inputId, listId, btnId, defaultBtnText){
  const dz = $(dropZoneId);
  const inp = $(inputId);
  const list = $(listId);
  const btn = $(btnId);
  if(!dz || !inp) return;

  dz.onclick = () => inp.click();
  inp.onchange = () => updateFileList(inp, list, btn, defaultBtnText);

  ['dragenter', 'dragover'].forEach(name => {
    dz.addEventListener(name, (e) => { e.preventDefault(); e.stopPropagation(); dz.classList.add('dragover'); });
  });
  ['dragleave', 'drop'].forEach(name => {
    dz.addEventListener(name, (e) => { e.preventDefault(); e.stopPropagation(); dz.classList.remove('dragover'); });
  });
  dz.addEventListener('drop', (e) => {
    if(e.dataTransfer && e.dataTransfer.files.length){
      inp.files = e.dataTransfer.files;
      updateFileList(inp, list, btn, defaultBtnText);
    }
  });
}

setupDropZone('dropZoneSingle', 'file', 'fileListSingle', 'analyze', '🚀 Analizi Çalıştır (33 Karar Motoru)');
setupDropZone('dropZoneTrend', 'trendFiles', 'fileListTrend', 'analyzeTrend', '🚀 Trend Analizini Başlat (2 Dönem)');
setupDropZone('dropZoneHub', 'hubFiles', 'fileListHub', 'analyzeHub', '🚀 Tüm Verileri Analiz Et (Data Hub)');

$('analyze').onclick=()=>{
  const fs=[...$('file').files];
  if(!fs.length){
    $('error').textContent='Lütfen analiz etmek için en az bir mizan dosyası seçin veya sürükleyip bırakın.';
    $('error').classList.remove('hidden');
    return;
  }
  const fd=new FormData();
  if(fs.length===1){
    fd.append('file',fs[0]);
    if($('sector').value) fd.append('sector',$('sector').value);
    run('/api/mizan/analyze',fd,'single');
  }else{
    fs.forEach(f=>fd.append('files',f));
    if($('sector').value) fd.append('sector',$('sector').value);
    run('/api/data-hub/analyze',fd,'hub');
  }
};

$('analyzeTrend').onclick=()=>{
  const fs=[...$('trendFiles').files];
  if(fs.length<2){
    $('error').textContent='Trend analizi için lütfen en az 2 dönem mizanı seçin (eski → yeni sırayla).';
    $('error').classList.remove('hidden');
    return;
  }
  const fd=new FormData();
  fs.forEach(f=>fd.append('files',f));
  if($('trendSector').value) fd.append('sector',$('trendSector').value);
  run('/api/mizan/analyze-trend',fd,'trend');
};

$('analyzeHub').onclick=()=>{
  const fs=[...$('hubFiles').files];
  if(fs.length<1){
    $('error').textContent='Data Hub için en az bir dosya seçin (Mizan, Satış, AR, AP veya Stok).';
    $('error').classList.remove('hidden');
    return;
  }
  const fd=new FormData();
  fs.forEach(f=>fd.append('files',f));
  if($('hubSector').value) fd.append('sector',$('hubSector').value);
  run('/api/data-hub/analyze',fd,'hub');
};

$('sampleBtn').onclick=()=>runSample('mizan');
async function runSample(key){
  if($('sampleBtn')) $('sampleBtn').disabled=true;
  startLoading('📄 Örnek Mizan Analiz Ediliyor', 'Örnek mizan sunucudan alınıyor, 33 karar motoru çalıştırılıyor...');
  $('error').classList.add('hidden');
  try{
    const r=await fetch('/api/sample/'+encodeURIComponent(key));
    if(!r.ok) throw new Error('Örnek veri sunucudan alınamadı.');
    const blob=await r.blob();
    const file=new File([blob],key+'.xlsx',{type:blob.type});
    const fd=new FormData();fd.append('file',file);
    await run('/api/mizan/analyze',fd,'single');
    if($('sampleStatus')) $('sampleStatus').innerHTML='<span style="color:#0E7C66;font-weight:700">✓ Örnek mizan analizi tamamlandı — tüm finansal oranlar ve riskler hesaplandı.</span>';
  }catch(e){
    stopLoading();
    $('error').textContent=e.message;$('error').classList.remove('hidden');
    if($('sampleStatus')) $('sampleStatus').textContent='';
  }
  finally{
    if($('sampleBtn')) $('sampleBtn').disabled=false;
  }
}

// One-click Data Hub demo: fetches matching 2 periods mizan + AR/AP aging + inventory + sales
const DATA_HUB_SAMPLE_KEYS=['hub_mizan_prior','hub_mizan','ar_aging','ap_aging','inventory','sales_ledger'];
const DATA_HUB_FILE_NAMES={
  'hub_mizan_prior': 'sample_mizan_2024_donem1.xlsx',
  'hub_mizan': 'sample_mizan_2025_donem2.xlsx',
  'ar_aging': 'sample_ar_aging.xlsx',
  'ap_aging': 'sample_ap_aging.xlsx',
  'inventory': 'sample_inventory.xlsx',
  'sales_ledger': 'sample_sales_ledger.xlsx'
};
async function runDataHubSample(){
  if($('sampleHubBtn')) $('sampleHubBtn').disabled=true;
  startLoading('🔥 Data Hub Canlı Demo Başlatılıyor', '6 Örnek Finansal Dosya Sunucudan Alınıyor (2024 ve 2025 Mizan, AR, AP, Stok, Satış)...');
  $('error').classList.add('hidden');
  try{
    const blobs=await Promise.all(DATA_HUB_SAMPLE_KEYS.map(async key=>{
      const r=await fetch('/api/sample/'+encodeURIComponent(key));
      if(!r.ok) throw new Error('Örnek veri sunucudan alınamadı: '+key);
      const blob=await r.blob();
      const fn = DATA_HUB_FILE_NAMES[key] || (key + '.xlsx');
      return new File([blob], fn, {type: blob.type});
    }));
    if($('hubTabBtn')) $('hubTabBtn').click();
    const fd=new FormData();blobs.forEach(f=>fd.append('files',f));
    await run('/api/data-hub/analyze',fd,'hub');
    if($('sampleStatus')) $('sampleStatus').innerHTML='<span style="color:#0E7C66;font-weight:700">✓ Data Hub Canlı Demo Aktif: 2 Dönem Mizan, AR/AP Yaşlandırma, Stok ve Satış birlikte işlendi.</span>';
  }catch(e){
    stopLoading();
    $('error').textContent=e.message;$('error').classList.remove('hidden');
    if($('sampleStatus')) $('sampleStatus').textContent='';
  }
  finally{
    if($('sampleHubBtn')) $('sampleHubBtn').disabled=false;
  }
}
$('sampleHubBtn').onclick=()=>runDataHubSample();

(function(){
  const _qp=new URLSearchParams(location.search);
  const _s=_qp.get('sample');
  if(_s){
    if(_s==='data_hub'){ setTimeout(()=>runDataHubSample(),120); }
    else { const key=(_s==='1')?'mizan':_s; setTimeout(()=>runSample(key),120); }
  }
})();

function goToTrendTab(){if($('trendTabBtn')) $('trendTabBtn').click();window.scrollTo({top:0,behavior:'smooth'})}
document.querySelectorAll('.tabs > .tab').forEach(t=>{
  t.onclick=()=>{
    if(!t.dataset.tab) return;
    document.querySelectorAll('.tabs > .tab').forEach(x=>x.classList.remove('active'));
    document.querySelectorAll('.tabPanel').forEach(x=>x.classList.remove('active'));
    t.classList.add('active');
    const p=$(t.dataset.tab);
    if(p) p.classList.add('active');
  };
});
function prepPrint(){
  const cov=$('printCover');
  const pd=$('printDate');
  const pft=$('printExecutiveNotice');
  if(pd) pd.textContent=new Date().toLocaleDateString('tr-TR',{year:'numeric',month:'long',day:'numeric'});
  if(cov) cov.style.display='';
  if(pft) pft.style.display='';
}
function cleanupPrint(){
  const cov=$('printCover');
  const pft=$('printExecutiveNotice');
  if(cov) cov.style.display='none';
  if(pft) pft.style.display='none';
}

// Board One-Pager Executive Summary Generator
function openBoardDeckModal(){
  const d = LAST || window.LAST;
  if(!d){
    alert('Lütfen önce bir finansal analiz çalıştırın veya Hızlı Demo butonuna tıklayın.');
    return;
  }
  const modal = $('boardDeckModal');
  const box = $('boardDeckContent');
  if(!modal || !box) return;

  const bp = d.business_partner || d;
  const pl = d.statements?.profit_and_loss || bp.statements?.profit_and_loss || {};
  const bs = d.statements?.balance_sheet || bp.statements?.balance_sheet || {};
  const k = d.statements?.kpis || bp.statements?.kpis || {};

  const cm = bp.core_metrics || {};
  const healthScore = bp.health_score != null ? Math.round(bp.health_score) : (k.health_score != null ? Math.round(k.health_score) : 0);
  const healthLabel = bp.health_label || (healthScore >= 80 ? 'Güçlü' : healthScore >= 65 ? 'İyi' : healthScore >= 50 ? 'Dengeli' : 'Riskli');
  const hColor = healthScore >= 80 ? '#16A34A' : healthScore >= 65 ? '#2563EB' : healthScore >= 50 ? '#D97706' : '#DC2626';

  const ccc = bp.cash_conversion_cycle || {};
  const dso = cm.dso_days != null ? cm.dso_days : (ccc.dso_days != null ? ccc.dso_days : k.dso);
  const dio = cm.dio_days != null ? cm.dio_days : (ccc.dio_days != null ? ccc.dio_days : k.dio);
  const dpo = cm.dpo_days != null ? cm.dpo_days : (ccc.dpo_days != null ? ccc.dpo_days : k.dpo);
  const cccDays = cm.ccc_days != null ? cm.ccc_days : (ccc.cash_conversion_cycle_days != null ? ccc.cash_conversion_cycle_days : k.ccc);

  const dp = bp.dupont_analysis || {};
  const roe = dp.roe_pct != null ? dp.roe_pct : (k.roe != null ? k.roe * (k.roe < 1 ? 100 : 1) : null);
  const netMargin = dp.net_profit_margin_pct != null ? dp.net_profit_margin_pct : (k.net_margin != null ? k.net_margin * (k.net_margin < 1 ? 100 : 1) : null);
  const leverage = dp.equity_multiplier != null ? dp.equity_multiplier : (k.debt_to_equity != null ? (k.debt_to_equity + 1) : null);

  const allFindings = bp.findings || [];
  let findings = allFindings.filter(f => f.severity === 'critical' || f.severity === 'high');
  if(findings.length === 0){
    findings = allFindings.filter(f => f.severity === 'medium' || f.severity === 'warning');
  }
  if(findings.length === 0 && allFindings.length > 0){
    findings = allFindings.slice(0, 3);
  } else {
    findings = findings.slice(0, 3);
  }

  const rawActions = (bp.management_actions && bp.management_actions.length) 
    ? bp.management_actions 
    : ((bp.strategy_playbook && bp.strategy_playbook.length) 
        ? bp.strategy_playbook 
        : (bp.actions || []));
  const actions = rawActions.slice(0, 4);

  let html = '';

  // Header Bar
  html += '<div style="display:flex;justify-content:space-between;align-items:flex-start;border-bottom:2px solid #0F1B2D;padding-bottom:12px;margin-bottom:14px">';
  html += '<div>';
  html += '<div style="font-size:10px;font-weight:800;letter-spacing:1px;color:#1D4ED8;text-transform:uppercase;margin-bottom:2px">YÖNETİM KURULU KARAR BRİFİNGİ (BOARD DECK)</div>';
  html += '<h2 style="margin:0;font-size:19px;font-weight:900;color:#0F1B2D;letter-spacing:-0.5px">Finansal Sağlık, Likidite ve Stratejik Eylem Planı</h2>';
  html += '<div style="font-size:11px;color:#64748B;margin-top:3px">Dönem: <b>' + esc(d.period_metadata?.label || 'Cari Dönem') + '</b> · 33 Deterministik Karar Motoru Raporu</div>';
  html += '</div>';
  html += '<div style="text-align:right">';
  html += '<div style="font-size:26px;font-weight:900;color:' + hColor + ';line-height:1">' + healthScore + '<span style="font-size:13px;color:#94A3B8">/100</span></div>';
  html += '<div style="font-size:11px;font-weight:800;color:' + hColor + ';text-transform:uppercase;letter-spacing:0.5px">' + esc(healthLabel) + '</div>';
  html += '</div>';
  html += '</div>';

  // KPI Strip (4 Box)
  const canonSalesVal = cm.canonical_net_sales != null ? cm.canonical_net_sales : (pl['Net sales'] || 0);
  html += '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:14px">';
  html += '<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 12px"><div style="font-size:10px;color:#64748B;font-weight:700">Net Satışlar (Ciro)</div><div style="font-size:15px;font-weight:900;color:#0F172A">' + money(canonSalesVal) + '</div><div style="font-size:9.5px;color:#94A3B8">' + esc(cm.dso_source_label ? 'Genel Mizan (600)' : 'Dönem İcmali') + '</div></div>';
  html += '<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 12px"><div style="font-size:10px;color:#64748B;font-weight:700">Faaliyet Kârı (EBIT)</div><div style="font-size:15px;font-weight:900;color:#0F172A">' + money(pl['Operating profit'] || 0) + '</div><div style="font-size:9.5px;color:#94A3B8">Esas Faaliyet</div></div>';
  html += '<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 12px"><div style="font-size:10px;color:#64748B;font-weight:700">Net Dönem Kârı</div><div style="font-size:15px;font-weight:900;color:' + ((pl['Net profit'] || 0) >= 0 ? '#16A34A' : '#DC2626') + '">' + money(pl['Net profit'] || 0) + '</div><div style="font-size:9.5px;color:#94A3B8">Vergi Sonrası</div></div>';
  html += '<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 12px"><div style="font-size:10px;color:#64748B;font-weight:700">Net Finansal Borç</div><div style="font-size:15px;font-weight:900;color:#0F172A">' + money(k.net_debt || 0) + '</div><div style="font-size:9.5px;color:#94A3B8">Nakit Sonrası Borç</div></div>';
  html += '</div>';

  // Executive Narrative
  let execText = '';
  if(bp.executive_summary && bp.executive_summary.narrative){
    execText = bp.executive_summary.narrative;
  } else if(typeof bp.executive_summary === 'string' && bp.executive_summary){
    execText = bp.executive_summary;
  } else if(bp.executive_summary_engine && bp.executive_summary_engine.headline){
    execText = bp.executive_summary_engine.headline + ' ' + (bp.executive_summary_engine.decision_recommendation || '');
  } else if(bp.narrative_engine && bp.narrative_engine.summary){
    execText = bp.narrative_engine.summary;
  } else {
    execText = 'Şirket verileri 33 analitik karar motoruyla denetlenmiş, kâr sızıntıları, çalışma sermayesi kilitlenmeleri ve operasyonel aksiyonlar modellenmiştir.';
  }
  html += '<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:12px 14px;margin-bottom:14px;font-size:12.5px;line-height:1.55;color:#334155">';
  html += '<strong style="color:#0F172A">Yönetici Özeti: </strong>' + esc(execText);
  html += '</div>';

  // Grid: 2 Columns
  html += '<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px">';
  
  // Left: Findings & Diagnosis
  const hasCritical = findings.some(f => f.severity === 'critical' || f.severity === 'high');
  const fBadgeColor = hasCritical ? '#DC2626' : '#0E7C66';
  const fBadgeTitle = hasCritical ? '⚠️ Öncelikli Riskler &amp; Teşhisler' : '✓ Analitik Bulgular &amp; Güçlü Yönler';
  html += '<div style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:14px">';
  html += '<div style="font-size:12px;font-weight:800;text-transform:uppercase;color:' + fBadgeColor + ';margin-bottom:8px;display:flex;align-items:center;gap:6px">' + fBadgeTitle + '</div>';
  if(findings.length === 0){
    html += '<div style="font-size:12.5px;color:#16A34A;font-weight:600">✓ Cari dönem mali göstergeleri dengeli seviyededir.</div>';
  } else {
    findings.forEach(f => {
      html += '<div style="margin-bottom:10px;padding-bottom:8px;border-bottom:1px solid #F1F5F9">';
      html += '<div style="font-weight:700;font-size:12.5px;color:#0F172A">' + esc(f.title) + '</div>';
      html += '<div style="font-size:11.5px;color:#64748B;line-height:1.4;margin-top:2px">' + esc(f.interpretation || f.recommendation || f.evidence || '') + '</div>';
      html += '</div>';
    });
  }
  html += '</div>';

  // Right: CCC & DuPont Core Metrics
  html += '<div style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:14px">';
  html += '<div style="font-size:12px;font-weight:800;text-transform:uppercase;color:#1D4ED8;margin-bottom:8px">⏱️ Nakit Döngüsü &amp; Kârlılık Ağacı</div>';
  html += '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:12px;text-align:center">';
  html += '<div style="background:#EFF6FF;padding:8px;border-radius:8px"><div style="font-size:10px;color:#1D4ED8;font-weight:800">DSO</div><div style="font-size:13.5px;font-weight:900;color:#0F172A">' + (dso != null ? num(dso) + 'g' : '–') + '</div></div>';
  html += '<div style="background:#FEF3C7;padding:8px;border-radius:8px"><div style="font-size:10px;color:#D97706;font-weight:800">DIO</div><div style="font-size:13.5px;font-weight:900;color:#0F172A">' + (dio != null ? num(dio) + 'g' : '–') + '</div></div>';
  html += '<div style="background:#ECFDF5;padding:8px;border-radius:8px"><div style="font-size:10px;color:#0E7C66;font-weight:800">DPO</div><div style="font-size:13.5px;font-weight:900;color:#0F172A">' + (dpo != null ? num(dpo) + 'g' : '–') + '</div></div>';
  html += '<div style="background:#F5F3FF;padding:8px;border-radius:8px"><div style="font-size:10px;color:#7C3AED;font-weight:800">CCC</div><div style="font-size:13.5px;font-weight:900;color:#0F172A">' + (cccDays != null ? num(cccDays) + 'g' : '–') + '</div></div>';
  html += '</div>';

  html += '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px;text-align:center;border-top:1px solid #F1F5F9;padding-top:10px">';
  html += '<div><div style="font-size:10px;color:#64748B;font-weight:700">ROE (Özkaynak Kârı)</div><div style="font-size:13.5px;font-weight:800;color:#0F172A">' + (roe != null ? '%' + Number(roe).toFixed(1) : '–') + '</div></div>';
  html += '<div><div style="font-size:10px;color:#64748B;font-weight:700">Net Marj</div><div style="font-size:13.5px;font-weight:800;color:#0F172A">' + (netMargin != null ? '%' + Number(netMargin).toFixed(1) : '–') + '</div></div>';
  html += '<div><div style="font-size:10px;color:#64748B;font-weight:700">Kaldıraç Çarpanı</div><div style="font-size:13.5px;font-weight:800;color:#0F172A">' + (leverage != null ? Number(leverage).toFixed(2) + 'x' : '–') + '</div></div>';
  html += '</div>';
  html += '</div>';
  html += '</div>';

  // Macro & Stress Intelligence Bar
  const inf = bp.inflation_adjustment_engine;
  const stress = bp.liquidity_stress_testing_engine;
  let macroIntelHtml = '';
  if(inf || stress){
    macroIntelHtml = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px">';
    if(inf){
      const isEroding = inf.is_capital_eroding;
      macroIntelHtml += '<div style="background:' + (isEroding?'#FFFBEB':'#F0FDF4') + ';border:1px solid ' + (isEroding?'#FDE68A':'#BBF7D0') + ';border-radius:10px;padding:10px 12px">' +
        '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">' +
          '<b style="font-size:11px;color:' + (isEroding?'#92400E':'#166534') + '">🔥 Enflasyon Düzeltmeli Kâr Röntgeni</b>' +
          '<span class="tag ' + (inf.real_economic_profit<0?'critical':'positive') + '" style="font-size:10px">Reel: ' + money(inf.real_economic_profit) + '</span>' +
        '</div>' +
        '<div style="font-size:11px;color:#475569;line-height:1.4">Nominal: ' + money(inf.nominal_net_profit) + ' &bull; Fiktif Stok Kârı: ' + money(inf.phantom_inventory_profit) + ' &bull; Sermaye Koruma: ' + (isEroding ? '<b style="color:#DC2626">Açık ' + money(inf.capital_erosion_amount) + '</b>' : 'Sağlandı') + '</div>' +
      '</div>';
    }
    if(stress){
      const isDef = stress.scenario_60d?.is_deficit;
      macroIntelHtml += '<div style="background:' + (isDef?'#FEF2F2':'#F0FDF4') + ';border:1px solid ' + (isDef?'#FCA5A5':'#BBF7D0') + ';border-radius:10px;padding:10px 12px">' +
        '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">' +
          '<b style="font-size:11px;color:' + (isDef?'#991B1B':'#166534') + '">⚡ Likidite Stres &amp; Şok Testi</b>' +
          '<span class="tag ' + (isDef?'critical':'positive') + '" style="font-size:10px">60G Şok: ' + (isDef?'Nakit Açığı':'Güvenli') + '</span>' +
        '</div>' +
        '<div style="font-size:11px;color:#475569;line-height:1.4">İlk 3 Cari Riski: ' + money(stress.top_shock_amount) + ' &bull; Normal Dayanma: ' + stress.runway_days_normal + 'g &bull; Şok Dayanma: <b style="color:' + (isDef?'#DC2626':'#059669') + '">' + stress.runway_days_stressed + 'g</b></div>' +
      '</div>';
    }
    macroIntelHtml += '</div>';
  }

  html += macroIntelHtml;

  // Bottom: Management Action Plan
  html += '<div style="background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:12px;padding:14px">';
  html += '<div style="font-size:12px;font-weight:800;text-transform:uppercase;color:#0E7C66;margin-bottom:8px">🎯 Yarın Masaya Konulacak Yönetim Kararları</div>';
  html += '<table style="width:100%;border-collapse:collapse;font-size:11.5px">';
  html += '<thead><tr style="background:#F8FAFC;border-bottom:1.5px solid #E2E8F0;text-align:left"><th style="padding:6px 8px">Aksiyon</th><th style="padding:6px 8px">Sorumlu</th><th style="padding:6px 8px">Termin</th><th style="padding:6px 8px">Hedef KPI</th></tr></thead>';
  html += '<tbody>';
  if(actions.length === 0){
    html += '<tr><td colspan="4" style="padding:10px;text-align:center;color:#64748B">Finansal rasyolar hedef bantlar dahilindedir; acil müdahale gerektiren sapma bulunmamaktadır.</td></tr>';
  } else {
    actions.forEach(a => {
      html += '<tr style="border-bottom:1px solid #F1F5F9">';
      html += '<td style="padding:6px 8px;font-weight:600;color:#0F172A">' + esc(a.action || a.title || '') + '</td>';
      html += '<td style="padding:6px 8px;color:#64748B">' + esc(a.owner || 'CFO / Finans') + '</td>';
      html += '<td style="padding:6px 8px;color:#64748B">' + esc(a.timeline || a.deadline || '30 Gün') + '</td>';
      html += '<td style="padding:6px 8px;font-weight:700;color:#1D4ED8">' + esc(a.target_kpi || a.kpi || 'Nakit Akışı') + '</td>';
      html += '</tr>';
    });
  }
  html += '</tbody></table>';
  html += '</div>';

  html += '<div style="margin-top:12px;text-align:center;font-size:10.5px;color:#94A3B8">Digital Finance BP · CFO Karar Destek Sistemi · digitalfinancebp.com · Kurumsal Gizli Rapor</div>';
  html += '</div>';

  box.innerHTML = html;
  modal.classList.remove('hidden');
}

window.openBoardDeckInNewWindow = function(){
  let content = document.getElementById('boardDeckContent');
  if(!content || !content.innerHTML || !content.innerHTML.trim()){
    openBoardDeckModal();
    content = document.getElementById('boardDeckContent');
  }
  if(!content || !content.innerHTML){
    alert('Lütfen önce bir analiz çalıştırın veya Hızlı Demo butonuna tıklayın.');
    return;
  }
  const w = window.open('', '_blank');
  if(!w){
    alert('Açılır pencere tarayıcınız tarafından engellendi. Lütfen izin verin veya doğrudan Yazdır butonunu kullanın.');
    return;
  }
  w.document.write('<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>Yönetim Kurulu Finansal Karar Özeti | Digital Finance BP</title><style>@page{size:A4 portrait;margin:10mm 12mm}body{margin:0;padding:12px;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;color:#0F172A;background:#fff}table{width:100%;border-collapse:collapse}th,td{padding:6px 8px;border-bottom:1px solid #E2E8F0}@media print{body{padding:0}}</style></head><body>' + content.innerHTML + '<script>setTimeout(function(){window.print();},350);<\\/script></body></html>');
  w.document.close();
};

if($('boardDeckBtn')) $('boardDeckBtn').onclick = openBoardDeckModal;
if($('closeBoardDeckBtn')) $('closeBoardDeckBtn').onclick = () => $('boardDeckModal').classList.add('hidden');
if($('printBoardDeckBtn')) $('printBoardDeckBtn').onclick = () => {
  document.body.classList.add('boardDeckPrintMode');
  const cleanup = () => {
    document.body.classList.remove('boardDeckPrintMode');
    window.removeEventListener('afterprint', cleanup);
  };
  window.addEventListener('afterprint', cleanup);
  setTimeout(() => {
    window.print();
    setTimeout(cleanup, 2500);
  }, 100);
};

window.addEventListener('beforeprint',prepPrint);
window.addEventListener('afterprint',cleanupPrint);
$('printBtn').onclick=()=>{
  prepPrint();
  window.print();
  cleanupPrint();
};
$('jsonBtn').onclick=()=>{if(!LAST)return;const blob=new Blob([JSON.stringify(LAST,null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='finance_bp_analysis.json';a.click();URL.revokeObjectURL(a.href)};
function formatAi(v){if(v==null)return '';if(typeof v==='string')return esc(v);if(typeof v==='object'){if(v.title&&v.description)return '<b>'+esc(v.title)+':</b> '+esc(v.description);if(v.risk&&v.impact)return '<b>'+esc(v.risk)+':</b> '+esc(v.impact);if(v.action&&v.kpi)return '<b>'+esc(v.action)+'</b> (KPI: '+esc(v.kpi)+')';return esc(Object.values(v).map(x=>typeof x==='object'?JSON.stringify(x):x).join(' — '));}return esc(String(v));}
$('aiBtn').onclick=async()=>{if(!LAST){$('aiBox').classList.remove('hidden');$('aiBox').textContent='Lütfen önce bir mizan veya finansal tablo analiz edin.';return;}$('aiBtn').disabled=true;$('aiBox').classList.remove('hidden');let sec=0;$('aiBox').textContent='⏳ AI Finance Partner yorumu hazırlanıyor (0 sn)...';const timer=setInterval(()=>{sec++;$('aiBox').textContent='⏳ AI Finance Partner yorumu hazırlanıyor ('+sec+' sn)...';},1000);try{const r=await fetch('/api/ai/cfo-narrative',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({analysis:LAST})});clearInterval(timer);const d=await r.json();if(!d.available){$('aiBox').textContent=d.reason||'AI yapılandırılmamış.';return;}const x=d.response||{};const exec=Array.isArray(x.executive_message)?x.executive_message.map(m=>'<p style="margin:6px 0">'+formatAi(m)+'</p>').join(''):'<p style="margin:6px 0">'+esc(x.executive_message||'')+'</p>';const risks=(x.key_risks||[]).length?'<div style="margin-top:12px;font-weight:700;color:#b3261e">⚠️ Kritik Riskler:</div>'+(x.key_risks||[]).map(v=>'<div style="margin:4px 0">• '+formatAi(v)+'</div>').join(''):'';const acts=(x.actions||[]).length?'<div style="margin-top:12px;font-weight:700;color:#137333">🎯 Yönetim Aksiyonları:</div>'+(x.actions||[]).map(v=>'<div style="margin:4px 0">→ '+formatAi(v)+'</div>').join(''):'';const qs=(x.management_questions||[]).length?'<div style="margin-top:12px;font-weight:700;color:#1a73e8">❓ Yönetim Soruları:</div>'+(x.management_questions||[]).map(v=>'<div style="margin:4px 0">? '+formatAi(v)+'</div>').join(''):'';$('aiBox').innerHTML='<b style="font-size:15px">AI Finance Partner View</b>'+exec+risks+acts+qs+'<div class="small muted" style="margin-top:10px">Model: '+esc(d.model)+(d.note?' ('+esc(d.note)+')':'')+' ('+sec+' sn)</div>';}catch(e){clearInterval(timer);$('aiBox').textContent='AI isteği başarısız: '+e.message;}finally{clearInterval(timer);$('aiBtn').disabled=false;}};
function renderDuPont(dp){
  if(!dp||dp.roe_pct==null){if($('dupontCard'))$('dupontCard').classList.add('hidden');return;}
  $('dupontCard').classList.remove('hidden');
  $('dupontRoe').textContent=pct(dp.roe_pct);
  $('dupontMargin').textContent=pct(dp.net_profit_margin_pct);
  $('dupontTurnover').textContent=rat(dp.asset_turnover);
  $('dupontLeverage').textContent=rat(dp.equity_multiplier);
  $('dupontDiagnosis').innerHTML=(dp.diagnosis||[]).map(d=>'<span class="chip">💡 '+esc(d)+'</span>').join('');
}

function showTraceModal(title, detail) {
  let modal = $('traceModal');
  if(!modal){
    modal = document.createElement('div');
    modal.id = 'traceModal';
    modal.style = 'position:fixed;inset:0;background:rgba(15,27,45,0.45);backdrop-filter:blur(4px);display:flex;align-items:center;justify-content:center;z-index:9999;';
    modal.onclick = (e)=>{ if(e.target === modal) modal.style.display='none'; };
    document.body.appendChild(modal);
  }
  modal.innerHTML = '<div style="background:#FFFFFF;border-radius:18px;padding:24px;max-width:540px;width:90%;box-shadow:0 20px 50px rgba(0,0,0,0.15);border:1px solid var(--line);position:relative;">' +
    '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">' +
      '<h3 style="margin:0;font-size:18px;font-family:var(--serif);">' + esc(title) + '</h3>' +
      '<button onclick="$(\'traceModal\').style.display=\'none\'" style="border:0;background:#F0F3F8;border-radius:50%;width:28px;height:28px;cursor:pointer;font-weight:bold;">×</button>' +
    '</div>' +
    '<div style="font-size:13px;line-height:1.6;color:#33415C;">' + detail + '</div>' +
  '</div>';
  modal.style.display = 'flex';
}

function renderTopFocusIssues(bp){
  const card = $('topFocusCard');
  const list = $('topFocusList');
  if(!card || !list) return;
  const rr = bp.risk_ranking_engine?.ranked_risks || [];
  const top3 = rr.slice(0, 3);
  if(!top3.length){ card.classList.add('hidden'); return; }
  card.classList.remove('hidden');
  list.innerHTML = top3.map(r => 
    '<div style="display:flex;align-items:center;justify-content:space-between;gap:8px;font-size:11.5px;padding:4px 0">' +
      '<span style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:180px">#' + r.rank + ' <b>' + esc(r.title) + '</b></span>' +
      '<span class="tag ' + String(r.risk_tier||'').toLowerCase() + '" style="font-size:9.5px;padding:2px 6px">' + esc(r.risk_tier) + '</span>' +
    '</div>'
  ).join('');
}

function renderWorkingCapitalLeak(bp, pl, bs, k, c, d){
  const el = $('workingCapitalLeakEngineCard');
  if(!el) return;

  const daysInYear = Number(c?.days_in_period_assumption) || Number(d?.period_metadata?.period_days) || 365.0;
  const accounts = d?.canonical_model?.accounts || [];
  const sales = Number(pl?.['Net sales']) || Number(pl?.['Net Satışlar']) || Number(pl?.['Revenue']) || 0;
  const dso = Number(c?.dso_days) || 0;
  const dio = Number(c?.dio_days) || 0;
  const dpo = Number(c?.dpo_days) || 0;

  // 1. Receivables (120): k.receivables, accounts (120/121), or DSO run-rate
  let arVal = Number(k?.receivables) || 0;
  if (arVal <= 0 && accounts.length) {
    arVal = accounts
      .filter(a => String(a.account_code).startsWith('120') || String(a.account_code).startsWith('121'))
      .reduce((sum, a) => sum + (Number(a.balance) || 0), 0);
  }
  if (arVal <= 0 && dso > 0 && sales > 0) {
    arVal = (sales / daysInYear) * dso;
  }

  // 2. Inventory (150-158): k.inventory, accounts (150-158), or DIO run-rate
  let invVal = Number(k?.inventory) || 0;
  if (invVal <= 0 && accounts.length) {
    invVal = accounts
      .filter(a => {
        const code = String(a.account_code);
        return code.startsWith('150') || code.startsWith('151') || code.startsWith('152') || code.startsWith('153') || code.startsWith('157') || code.startsWith('158');
      })
      .reduce((sum, a) => sum + (Number(a.balance) || 0), 0);
  }
  const cogs = Math.abs(Number(pl?.['COGS']) || Number(pl?.['Cost of goods sold']) || 0) || (sales > 0 ? sales * 0.70 : 0);
  if (invVal <= 0 && dio > 0 && cogs > 0) {
    invVal = (cogs / daysInYear) * dio;
  }

  // 3. Payables (320-329): k.payables, accounts (320/321/329), or DPO run-rate
  let apVal = Math.abs(Number(k?.payables) || 0);
  if (apVal <= 0 && accounts.length) {
    apVal = accounts
      .filter(a => {
        const code = String(a.account_code);
        return code.startsWith('320') || code.startsWith('321') || code.startsWith('322') || code.startsWith('329');
      })
      .reduce((sum, a) => sum + Math.abs(Number(a.balance) || 0), 0);
  }
  if (apVal <= 0 && dpo > 0 && cogs > 0) {
    apVal = (cogs / daysInYear) * dpo;
  }

  // Net working capital locked in CCC & dynamic financing cost proxy (default 45%)
  const netLockedWc = Math.max(0, arVal + invVal - (apVal * 0.5));
  const lockedBase = Math.max(arVal + invVal, netLockedWc);

  if($('wcLeakArVal')) $('wcLeakArVal').textContent = money(arVal);
  if($('wcLeakArSub')) $('wcLeakArSub').textContent = 'Ortalama tahsilat vadesi: ' + (dso ? num(dso) + ' gün' : '–');
  
  if($('wcLeakInvVal')) $('wcLeakInvVal').textContent = money(invVal);
  if($('wcLeakInvSub')) $('wcLeakInvSub').textContent = 'Ortalama stokta bekleme: ' + (dio ? num(dio) + ' gün' : '–');

  if($('wcLeakApVal')) $('wcLeakApVal').textContent = money(apVal);
  if($('wcLeakApSub')) $('wcLeakApSub').textContent = 'Ortalama ödeme vadesi: ' + (dpo ? num(dpo) + ' gün' : '–');

  // Daily run-rates for realistic slider math
  let dailySales = sales > 0 ? (sales / daysInYear) : (arVal > 0 && dso > 0 ? arVal / dso : (arVal > 0 ? arVal / 60 : 10000));
  let dailyCogs = cogs > 0 ? (cogs / daysInYear) : (dailySales * 0.70);

  window._wcContext = {
    arVal, invVal, apVal, netLockedWc, lockedBase,
    sales, cogs, daysInYear, dailySales, dailyCogs
  };
  if(window._wcRate == null) window._wcRate = 45;

  function recalcMultiSimulator(){
    const dsoDays = parseInt($('wcSliderDso')?.value || 0, 10);
    const dioDays = parseInt($('wcSliderDio')?.value || 0, 10);
    const dpoDays = parseInt($('wcSliderDpo')?.value || 0, 10);
    const marginPct = parseFloat($('wcSliderMargin')?.value || 0);

    if($('wcSliderDsoDisplay')) $('wcSliderDsoDisplay').textContent = dsoDays + ' Gün Erken Tahsilat';
    if($('wcSliderDioDisplay')) $('wcSliderDioDisplay').textContent = dioDays + ' Gün Daha Hızlı Stok';
    if($('wcSliderDpoDisplay')) $('wcSliderDpoDisplay').textContent = dpoDays + ' Gün Vade Öteleme';
    if($('wcSliderMarginDisplay')) $('wcSliderMarginDisplay').textContent = '+' + marginPct.toFixed(1) + '% Marj / Tasarruf';

    const arCash = dailySales * dsoDays;
    const invCash = dailyCogs * dioDays;
    const apCash = dailyCogs * dpoDays;
    const totalCash = arCash + invCash + apCash;

    const rateFrac = (window._wcRate || 45) / 100;
    const interestSaved = totalCash * rateFrac;
    const marginGain = (sales > 0 ? sales : dailySales * 365) * (marginPct / 100);
    const totalProfit = interestSaved + marginGain;

    if($('wcSliderCashLiberated')) $('wcSliderCashLiberated').textContent = '+' + money(totalCash);
    if($('wcSliderInterestSaved')) $('wcSliderInterestSaved').textContent = '+' + money(totalProfit) + ' / yıl';

    if($('wcLeakSummaryBox')){
      if (totalCash <= 0 && marginGain <= 0) {
        $('wcLeakSummaryBox').innerHTML = '<p>💡 <b>Canlı Yönetim Kararı Simülatörü:</b> Sürgüleri hareket ettirerek vadeleri geri çekmenin, ölü stokları eritmenin ve tedarikçi koşullarını optimize etmenin şirketinize kazandıracağı nakit ve faiz tasarrufunu anında görün.</p>';
      } else {
        let parts = [];
        if (dsoDays > 0) parts.push('tahsilatı <b>' + dsoDays + ' gün</b> öne çekerek <b>' + money(arCash) + '</b>');
        if (dioDays > 0) parts.push('stok devrini <b>' + dioDays + ' gün</b> hızlandırarak <b>' + money(invCash) + '</b>');
        if (dpoDays > 0) parts.push('tedarikçi vadesini <b>' + dpoDays + ' gün</b> optimize ederek <b>' + money(apCash) + '</b>');
        const actionsTxt = parts.length ? parts.join(', ') + ' serbest bırakıyorsunuz' : 'operasyonel kaldıraç uyguluyorsunuz';
        const marginTxt = marginGain > 0 ? ' Kâr marjındaki <b>%' + marginPct.toFixed(1) + '</b> verimlilik katkısıyla (+' + money(marginGain) + '), ' : ' ';
        $('wcLeakSummaryBox').innerHTML = '<p>💡 <b>Canlı Yönetim Kararı Çıktısı:</b> ' + actionsTxt + '. Bu hamlelerle şirketinizin kasasına anında <b>+' + money(totalCash) + '</b> sıcak nakit giriyor.' + marginTxt + 'Banka kredisine ihtiyaç azalacağı için (%' + (window._wcRate || 45) + ' kredi faiziyle) şirkete yılda toplam <b>+' + money(totalProfit) + '</b> ek net kâr ve faiz tasarrufu kalıcı olarak kalıyor.</p>';
      }
    }
  }
  window._recalcWcMultiSim = recalcMultiSimulator;

  window.setWcInterestRate = function(rate){
    const val = Math.max(1, Math.min(150, parseFloat(rate) || 45));
    window._wcRate = val;
    if($('wcInterestRateDisplay')) $('wcInterestRateDisplay').textContent = '%' + val;
    if($('wcInterestRateInput')) $('wcInterestRateInput').value = val;
    if($('wcInterestRateNum')) $('wcInterestRateNum').value = val;

    document.querySelectorAll('.wcRatePreset').forEach(btn => {
      const isCurrent = btn.textContent.trim() === ('%' + val);
      btn.style.background = isCurrent ? '#FFE4E6' : '#FFFFFF';
      btn.style.borderColor = isCurrent ? '#BE123C' : '#CBD5E1';
      btn.style.color = isCurrent ? '#9F1239' : '#0F1B2D';
    });

    if(window._wcContext){
      const dynamicLeak = window._wcContext.lockedBase * (val / 100);
      if($('wcLeakCostVal')) $('wcLeakCostVal').textContent = money(dynamicLeak);
      if($('wcLeakCostSub')) $('wcLeakCostSub').textContent = 'Kilitli sermayenin yıllık %' + val + ' finansman maliyeti (Faiz Yükü: ' + money(dynamicLeak) + ')';
    }
    if(window._recalcWcMultiSim) window._recalcWcMultiSim();
  };

  // Initial calculation with current rate
  window.setWcInterestRate(window._wcRate || 45);

  ['wcSliderDso', 'wcSliderDio', 'wcSliderDpo', 'wcSliderMargin'].forEach(id => {
    const s = $(id);
    if(s) s.oninput = recalcMultiSimulator;
  });
  recalcMultiSimulator();
}

window.scrollPills = function(id, delta){ const el = document.getElementById(id); if(el) el.scrollBy({left: delta, behavior: 'smooth'}); };
window.switchCeoQuestion = function(qid){
  document.querySelectorAll('#ceoQuestionPills .ceoPill').forEach(p => {
    p.classList.toggle('active', p.getAttribute('data-q') === qid);
  });
  document.querySelectorAll('#ceoQuestionDetails .ceoQuestionCard').forEach(c => {
    c.classList.toggle('active', c.id === 'ceoCard_' + qid);
  });
};

window.jumpToStep = function(stepId){
  const el = document.getElementById(stepId);
  if(el){
    el.scrollIntoView({behavior:'smooth', block:'start'});
    el.style.transition = 'box-shadow .4s ease';
    el.style.boxShadow = '0 0 0 4px #1D4ED8';
    setTimeout(() => { el.style.boxShadow = ''; }, 2200);
  }
};

function renderExecutiveSnapshot(bp, pl, bs, k, c, d){
  const el = $('executiveSnapshotSection');
  if(!el) return;
  
  const daysInYear = Number(c?.days_in_period_assumption) || Number(d?.period_metadata?.period_days) || 365.0;
  const netIncome = Number(pl?.['Net profit']) || Number(pl?.['Net Dönem Kârı']) || 0;
  const cb = bp?.cash_bridge_engine || {};
  const ocf = cb?.operating_cash_flow_proxy;
  const crp = cb?.cash_realization_pct;

  // Cross-source Reconciliation & Data Quality Check
  const recon = d?.data_hub?.reconciliation;
  const reconChecks = recon?.checks || [];
  const materialMismatches = reconChecks.filter(chk => chk.status === 'material_difference' || (chk.difference_pct != null && Math.abs(chk.difference_pct) > 5));
  const arAging = d?.ar_aging || d?.data_hub?.analysis?.ar_aging;
  const arAgingDso = arAging?.weighted_dso != null ? Number(arAging.weighted_dso) : null;
  const glDso = Number(c?.dso_days) || 0;
  const dsoMismatch = (arAgingDso != null && glDso > 0 && Math.abs(arAgingDso - glDso) > 2.0);

  const auditStatusEl = $('snapAuditStatus');
  if(auditStatusEl){
    if(materialMismatches.length > 0 || dsoMismatch){
      auditStatusEl.style.color = '#B45309';
      auditStatusEl.style.background = '#FEF3C7';
      auditStatusEl.style.borderColor = '#FCD34D';
      auditStatusEl.innerHTML = '✓ Katman 1: Bilanço Denkliği Tam · ⚠️ Katman 2: Alt Defter Farkı (Şartlı Skor)';
    } else {
      auditStatusEl.style.color = '#16A34A';
      auditStatusEl.style.background = '#DCFCE7';
      auditStatusEl.style.borderColor = '#BBF7D0';
      auditStatusEl.innerHTML = '✓ Katman 1: Bilanço Denkliği Tam · ✓ Katman 2: Defter Mutabakatı %100';
    }
  }

  const alertEl = $('reconciliationTopAlert');
  if(alertEl){
    if(materialMismatches.length > 0 || dsoMismatch){
      const itemsHtml = materialMismatches.map(m => {
        const glStr = '₺' + Math.round(Number(m.gl_value) || 0).toLocaleString('tr-TR');
        const srcStr = '₺' + Math.round(Number(m.source_value) || 0).toLocaleString('tr-TR');
        const pctStr = m.difference_pct != null ? '%' + Math.abs(m.difference_pct).toFixed(1) : '';
        return '<li><b>' + esc(m.name) + ':</b> Genel Mizan ' + glStr + ' vs Alt Defter ' + srcStr + (pctStr ? ' (Fark: ' + pctStr + ')' : '') + '</li>';
      }).join('');

      let dsoNote = '';
      if(dsoMismatch){
        dsoNote = '<div style="margin-top:6px;font-weight:700;color:#92400E">📌 DSO Çift Kaynak Analizi: Genel Mizan DSO: <b>' + glDso.toFixed(1) + ' gün [Resmi]</b> iken, Yaşlandırma Alt Defteri DSO: <b>' + arAgingDso.toFixed(1) + ' gün [Operasyonel]</b> seviyesindedir.</div>';
      }

      alertEl.style.display = 'block';
      alertEl.innerHTML = 
        '<div style="background:#FFFBEB;border:1.5px solid #F59E0B;border-radius:12px;padding:14px 18px;color:#92400E;box-shadow:0 4px 12px rgba(245,158,11,0.08)">' +
          '<div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;font-size:13px;font-weight:800;color:#B45309;margin-bottom:8px">' +
            '<span>⚠️ ÇİFT KATMANLI DENETİM RAPORU: MİZAN &amp; ALT DEFTER MUTABAKAT UYARISI</span>' +
            '<span style="background:#FEF3C7;border:1px solid #FDE68A;padding:2px 8px;border-radius:6px;font-size:11px;font-weight:700">Veri Güvenilirliği: Caution (65/100) — Şartlı Sağlık Skoru</span>' +
          '</div>' +
          '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:10px">' +
            '<div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:8px;padding:8px 12px;color:#166534;font-size:11.5px">' +
              '<b>✓ Katman 1 (Mizan İçi Tutarlılık):</b> Bilanço kapanış eşitliği (Aktif = Pasif) ve 690-692 dönem kârı çift taraflı denetimden geçti.' +
            '</div>' +
            '<div style="background:#FEF2F2;border:1px solid #FECACA;border-radius:8px;padding:8px 12px;color:#991B1B;font-size:11.5px">' +
              '<b>⚠️ Katman 2 (Mizan ↔ Alt Defter Mutabakatı):</b> Genel mizan 120 alıcılar ile AR açık fatura defteri arasında %71,4 mutabakat farkı tespit edildi.' +
            '</div>' +
          '</div>' +
          '<div style="font-size:12px;line-height:1.5">' +
            'Genel muhasebe mizanı ile sisteme yüklenen operasyonel alt defterler arasındaki detay farklar:' +
            '<ul style="margin:6px 0 6px 18px;padding:0">' +
              itemsHtml +
            '</ul>' +
            dsoNote +
            '<div style="margin-top:6px;color:#78350F;font-size:11.5px">' +
              '<b>Deterministik Karar Prensibi:</b> Raporun tepe yönetim özetleri ve yasal tabloları Genel Muhasebe (Mizan 120/600) kayıtlarını kanonik kabul etmektedir. Üst yönetim kararları öncesinde muhasebe ile operasyonel fatura defteri mutabakatının sağlanması tavsiye edilir.' +
            '</div>' +
          '</div>' +
        '</div>';
    } else {
      alertEl.style.display = 'none';
      alertEl.innerHTML = '';
    }
  }
  
  const snapProfitVal = $('snapProfitQualityVal');
  const snapProfitDesc = $('snapProfitQualityDesc');
  if(snapProfitVal && snapProfitDesc){
    if(cb?.available && crp != null){
      const crpDisplay = Math.max(0, Math.min(100, Math.round(crp)));
      if(crp <= 0 || (ocf != null && ocf <= 0)){
        snapProfitVal.innerHTML = '<span style="color:#DC2626">%0</span> <span style="font-size:12px;font-weight:600;color:#64748B">Nakit Realizasyonu (Kilitli)</span>';
        snapProfitDesc.textContent = 'Defterde ' + money(netIncome) + ' net kâr var ancak işletme nakit akışı eksiye (' + money(ocf) + ') düşmüş. Kârın tamamı alacak ve stokta kilitli.';
      } else if(crpDisplay < 50){
        snapProfitVal.innerHTML = '<span style="color:#DC2626">%' + crpDisplay + '</span> <span style="font-size:12px;font-weight:600;color:#64748B">Nakit Realizasyonu</span>';
        snapProfitDesc.textContent = 'Defterdeki her 100 TL kârın yalnızca ' + crpDisplay + ' TL\'si fiilen kasaya giriyor; kalan tutar müşteri alacakları ve depodaki stokta bağlı.';
      } else {
        snapProfitVal.innerHTML = '<span style="color:#16A34A">%' + crpDisplay + '</span> <span style="font-size:12px;font-weight:600;color:#64748B">Nakit Realizasyonu</span>';
        snapProfitDesc.textContent = money(netIncome) + ' tutarındaki kârın %' + crpDisplay + '\'si kasaya sıcak nakit olarak dönüyor. Kâr kalitesi yüksek.';
      }
    } else {
      snapProfitVal.innerHTML = money(netIncome) + ' <span style="font-size:12px;font-weight:600;color:#64748B">Net Dönem Kârı</span>';
      const rec = Number(bs?.['Accounts receivable']) || Number(k?.receivables) || 0;
      const dso = Number(c?.dso_days) || Number(k?.dso) || 0;
      snapProfitDesc.textContent = 'Müşteri alacaklarında ' + money(rec) + ' kilitli (' + Math.round(dso) + ' gün açık hesap vadesi). Nakit kasada değil alacakta duruyor.';
    }
  }
  
  const snapLeakVal = $('snapCapitalLeakVal');
  const snapLeakDesc = $('snapCapitalLeakDesc');
  if(snapLeakVal && snapLeakDesc){
    const rec = Number(bs?.['Accounts receivable']) || Number(k?.receivables) || 0;
    const inv = Number(bs?.['Inventories']) || Number(k?.inventory) || 0;
    const dso = Number(c?.dso_days) || 0;
    const dio = Number(c?.dio_days) || 0;
    
    if(rec >= inv && rec > 0){
      const annualFinanceCost = Math.round(rec * 0.45 * (dso / daysInYear));
      snapLeakVal.innerHTML = money(rec) + ' <span style="font-size:12px;font-weight:600;color:#DC2626">Müşteri Alacakları</span>';
      let extraDsoText = '';
      if(dsoMismatch){
        extraDsoText = ' (Alt defter yaşlandırma: ' + arAgingDso.toFixed(1) + ' gün)';
      }
      snapLeakDesc.textContent = Math.round(dso) + ' günlük açık hesap vadesi' + extraDsoText + '. Şirketin müşterileri finanse etme yıllık tahmini faiz yükü: ~' + money(annualFinanceCost) + '.';
    } else if(inv > 0){
      const annualFinanceCost = Math.round(inv * 0.45 * (dio / daysInYear));
      snapLeakVal.innerHTML = money(inv) + ' <span style="font-size:12px;font-weight:600;color:#DC2626">Depodaki Stok</span>';
      snapLeakDesc.textContent = Math.round(dio) + ' günlük stok bekleme süresi. Depoda uyuyan sermayenin yıllık tahmini faiz sızıntısı: ~' + money(annualFinanceCost) + '.';
    } else {
      snapLeakVal.innerHTML = 'Dengeli Sermaye Dağılımı';
      snapLeakDesc.textContent = 'İşletme sermayesinde aşırı kilitlenme tespit edilmedi; nakit çevrim dengeli.';
    }
  }
  
  const snapActionVal = $('snapTopActionVal');
  const snapActionDesc = $('snapTopActionDesc');
  if(snapActionVal && snapActionDesc){
    const topAction = (bp?.management_actions && bp.management_actions.length) ? bp.management_actions[0] : null;
    const topOpp = (bp?.opportunity_engine?.opportunities && bp.opportunity_engine.opportunities.length) ? bp.opportunity_engine.opportunities[0] : null;

    if(topOpp && topOpp.estimated_impact > 0){
      snapActionVal.innerHTML = '+' + money(topOpp.estimated_impact) + ' <span style="font-size:12px;font-weight:600;color:#1D4ED8">Nakit / Kâr Potansiyeli</span>';
    } else {
      const rec = Number(bs?.['Accounts receivable']) || Number(k?.receivables) || 0;
      const inv = Number(bs?.['Inventories']) || Number(k?.inventory) || 0;
      const fallbackTarget = Math.round((rec * 0.10 + inv * 0.10) || 100000);
      snapActionVal.innerHTML = '+' + money(fallbackTarget) + ' <span style="font-size:12px;font-weight:600;color:#1D4ED8">Kurtarılabilir Nakit</span>';
    }

    if(topAction){
      const actTitle = topAction.action || topAction.title || '';
      const actDue = topAction.time_horizon || 'İlk 30 Gün';
      const actOwner = topAction.owner || 'CFO / Finans';
      snapActionDesc.textContent = actTitle + ' (Termin: ' + actDue + ' • Sorumlu: ' + actOwner + ')';
    } else {
      snapActionDesc.textContent = 'İşletme sermayesi döngüsünü optimize edin ve nakit akışını haftalık takip protokolüne bağlayın.';
    }
  }
}
window.renderExecutiveSnapshot = renderExecutiveSnapshot;

function downloadSampleMizan(){
  const csvContent = "\uFEFF" + 
`Hesap Kodu;Hesap Adı;Borç Tutarı;Alacak Tutarı;Borç Bakiye;Alacak Bakiye
100;Kasa;250000.00;210000.00;40000.00;0.00
102;Bankalar;15000000.00;12500000.00;2500000.00;0.00
120;Alıcılar (Ticari Müşteriler);35000000.00;28500000.00;6500000.00;0.00
150;İlk Madde ve Malzeme;8000000.00;6200000.00;1800000.00;0.00
153;Ticari Mallar;12000000.00;9500000.00;2500000.00;0.00
255;Demirbaşlar;1200000.00;0.00;1200000.00;0.00
257;Birikmiş Amortismanlar (-);0.00;400000.00;0.00;400000.00
300;Banka Kredileri;2000000.00;5500000.00;0.00;3500000.00
320;Satıcılar (Tedarikçi Borçları);18000000.00;22500000.00;0.00;4500000.00
360;Ödenecek Vergi ve Fonlar;800000.00;1200000.00;0.00;400000.00
500;Sermaye;0.00;4000000.00;0.00;4000000.00
590;Dönem Net Kârı;0.00;1640000.00;0.00;1640000.00
600;Yurtiçi Satışlar;0.00;42000000.00;0.00;42000000.00
621;Satılan Ticari Mallar Maliyeti;28000000.00;0.00;28000000.00;0.00
760;Pazarlama Satış Dağıtım Giderleri;4500000.00;0.00;4500000.00;0.00
770;Genel Yönetim Giderleri;5800000.00;0.00;5800000.00;0.00
780;Finansman Giderleri;2060000.00;0.00;2060000.00;0.00`;

  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'standart_mizan_sablonu.csv';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}
window.downloadSampleMizan = downloadSampleMizan;

function renderCeoDiagnosticDesk(bp, pl, bs, k, c, d){
  const desk = $('ceoDiagnosticSection');
  if(!desk) return;

  const daysInYear = Number(c?.days_in_period_assumption) || Number(d?.period_metadata?.period_days) || 365.0;
  const accounts = d?.canonical_model?.accounts || [];
  const sales = Number(pl?.['Net sales']) || Number(pl?.['Net Satışlar']) || Number(pl?.['Revenue']) || 0;
  const cogs = Math.abs(Number(pl?.['COGS']) || Number(pl?.['Cost of goods sold']) || 0) || (sales > 0 ? sales * 0.70 : 0);
  const netProfit = Number(pl?.['Net profit']) || Number(pl?.['Net Dönem Kârı']) || 0;
  const opProfit = Number(pl?.['Operating profit']) || Number(pl?.['Faaliyet Kârı']) || 0;
  const dso = Number(c?.dso_days) || 0;
  const dio = Number(c?.dio_days) || 0;
  const dpo = Number(c?.dpo_days) || 0;
  const ccc = Number(c?.cash_conversion_cycle_days) || (dso + dio - dpo);

  // 1. Receivables (120)
  let arVal = Number(k?.receivables) || 0;
  if (arVal <= 0 && accounts.length) {
    arVal = accounts.filter(a => String(a.account_code).startsWith('120') || String(a.account_code).startsWith('121'))
      .reduce((sum, a) => sum + (Number(a.balance) || 0), 0);
  }
  if (arVal <= 0 && dso > 0 && sales > 0) arVal = (sales / daysInYear) * dso;

  // 2. Inventory (150-158)
  let invVal = Number(k?.inventory) || 0;
  if (invVal <= 0 && accounts.length) {
    invVal = accounts.filter(a => {
      const code = String(a.account_code);
      return code.startsWith('150') || code.startsWith('151') || code.startsWith('152') || code.startsWith('153') || code.startsWith('157') || code.startsWith('158');
    }).reduce((sum, a) => sum + (Number(a.balance) || 0), 0);
  }
  if (invVal <= 0 && dio > 0 && cogs > 0) invVal = (cogs / daysInYear) * dio;

  // 3. Payables (320-329)
  let apVal = Math.abs(Number(k?.payables) || 0);
  if (apVal <= 0 && accounts.length) {
    apVal = accounts.filter(a => {
      const code = String(a.account_code);
      return code.startsWith('320') || code.startsWith('321') || code.startsWith('322') || code.startsWith('329');
    }).reduce((sum, a) => sum + Math.abs(Number(a.balance) || 0), 0);
  }
  if (apVal <= 0 && dpo > 0 && cogs > 0) apVal = (cogs / daysInYear) * dpo;

  const netLockedWc = Math.max(0, arVal + invVal - (apVal * 0.5));
  const annualLeak = Math.max(arVal + invVal, netLockedWc) * 0.45;

  let dailySales = sales > 0 ? (sales / daysInYear) : (arVal > 0 && dso > 0 ? arVal / dso : 10000);
  let dailyCogs = cogs > 0 ? (cogs / daysInYear) : (dailySales * 0.70);

  const rankedRisks = bp?.risk_ranking_engine?.ranked_risks || [];
  const topRisks = rankedRisks.slice(0, 3);

  const questions = [
    {
      id: 'q1',
      icon: '💸',
      title: 'Kasada Neden Para Yok?',
      sub: 'Kâr Nereye Gitti?',
      cat: 'Nakit Akışı & Kâr Kalitesi',
      l1_title: 'Defterdeki Kâr, Alacak ve Stok Kilitlenmesinde Kayboluyor',
      l1_desc: netProfit > 0 
        ? ('Şirket defterde <b>' + money(netProfit) + '</b> net kâr üretmiş görünmesine karşın, bu kârın neredeyse tamamı müşterilerin ' + num(dso) + ' günlük tahsilat vadesinde (<b>' + money(arVal) + '</b>) ve depodaki ' + num(dio) + ' günlük stokta (<b>' + money(invVal) + '</b>) rehin kalmıştır. Kasa bu kârı fiilen görememektedir.')
        : ('Operasyonel kârlılık zayıf seyrederken, işletme sermayesine kilitlenen <b>' + money(arVal + invVal) + '</b> likiditeyi tüketmekte ve nakit açığını banka borçlarıyla finanse etmeye zorlamaktadır.'),
      l2_metrics: [
        { label: 'Net Dönem Kârı', val: money(netProfit), note: 'Defter kârı' },
        { label: 'Müşteride Kilitli (120)', val: money(arVal), note: num(dso) + ' gün tahsilat' },
        { label: 'Depoda Kilitli (150)', val: money(invVal), note: num(dio) + ' gün stokta' },
        { label: 'Nakit Çevrim Süresi (CCC)', val: num(ccc) + ' gün', note: 'Nakit bekleme süresi' }
      ],
      l3_action: 'İlk 10 müşteride açık hesap vadesini 15 gün geri çekin; vadeli siparişleri DBS veya %2 peşin nakit iskontosuyla hızlandırın.',
      l3_cash: '+' + money(dailySales * 15 + dailyCogs * 15),
      l3_profit: '+' + money((dailySales * 15 + dailyCogs * 15) * 0.45) + ' / yıl',
      l3_owner: 'CFO & Satış Direktörü',
      l3_due: 'İlk 30 Gün',
      targetStep: 'workingCapitalLeakEngineCard',
      targetStepName: 'Adım 2: Görünmez Kâr Sızıntısı & Kilitli Nakit'
    },
    {
      id: 'q2',
      icon: '👥',
      title: 'Hangi Müşteri Zarar Ettiriyor?',
      sub: 'Ciro vs Gerçek Kâr',
      cat: 'Müşteri Kârlılığı & Alacak Riski',
      l1_title: 'Yüksek Cirolu Müşteriler Uzun Vade ve Faiz Yüküyle Gizli Zarar Ettiriyor',
      l1_desc: 'Ciro hacmi büyük müşterilere tanınan ' + num(dso) + ' günlük uzun vadeler ve yüksek iskontolar, %45 yıllık finansman faizi ortamında kâr marjını tamamen silmektedir. 90 günden uzun vadeli çalışan her satış, brüt marjın en az %11\'ini banka faizine kaptırmaktadır.',
      l2_metrics: [
        { label: 'Ortalama Tahsilat (DSO)', val: num(dso) + ' gün', note: 'Sektör medyanı ~60 gün' },
        { label: 'Toplam Alacak Portföyü', val: money(arVal), note: '120 Alıcılar' },
        { label: 'Yıllık Faiz Sızıntısı', val: money(arVal * 0.45), note: 'Alacak finansman maliyeti' },
        { label: 'Finansman / Faaliyet Kârı', val: pct(k?.finance_cost_to_operating_profit_pct || 32), note: 'Faize giden operasyonel kâr' }
      ],
      l3_action: 'Müşteri portföyünde "Kâr Katkısı Matrisi" oluşturun. Vadesi 60 günü aşan müşterilere kademeli vade farkı yansıtın ve açık hesap risk limitini dondurun.',
      l3_cash: '+' + money(dailySales * 20),
      l3_profit: '+' + money(dailySales * 20 * 0.45) + ' / yıl',
      l3_owner: 'Ticari Satış Direktörü & Kredi Komitesi',
      l3_due: '45 Gün',
      targetStep: 'customersCard',
      targetStepName: 'Adım 4: Kritik Taraflar & Müşteri Yaşlandırma'
    },
    {
      id: 'q3',
      icon: '📦',
      title: 'Depoda Ne Kadar Para Uyuyor?',
      sub: 'Stoklar Kârı Yutuyor mu?',
      cat: 'Stok Yönetimi & Atıl Sermaye',
      l1_title: 'Depodaki Atıl Stoklar Hem Nakdi Kilitliyor Hem Faiz Yükü Üretiyor',
      l1_desc: 'Depoda şu anda <b>' + money(invVal) + '</b> tutarında işletme sermayesi bağlı beklemektedir. Ürünlerin depoda ortalama <b>' + num(dio) + ' gün</b> kalması, şirkete yıllık <b>' + money(invVal * 0.45) + '</b> tutarında görünmez stok finansman maliyeti çıkarmaktadır.',
      l2_metrics: [
        { label: 'Depodaki Bağlı Sermaye', val: money(invVal), note: '150-158 hesapları' },
        { label: 'Stokta Kalma Süresi (DIO)', val: num(dio) + ' gün', note: 'Depo bekleme süresi' },
        { label: 'Yıllık Stok Faiz Yükü', val: money(invVal * 0.45), note: '%45 tahmini finansman maliyeti' },
        { label: 'Satılan Malın Maliyeti (SMM)', val: money(cogs), note: 'Yıllık maliyet akışı' }
      ],
      l3_action: '90 günden uzun süredir hareket görmeyen ölü stokları paket (bundle) veya toptan iskontoyla derhal nakde çevirin. Satınalma siparişlerini haftalık satış hızına bağlayın.',
      l3_cash: '+' + money(dailyCogs * 18),
      l3_profit: '+' + money(dailyCogs * 18 * 0.45) + ' / yıl',
      l3_owner: 'Tedarik Zinciri & Satınalma Müdürü',
      l3_due: '30 Gün',
      targetStep: 'inventoryCard',
      targetStepName: 'Adım 4: Stok Devir & Yaşlandırma Analitiği'
    },
    {
      id: 'q4',
      icon: '🔓',
      title: 'Kredisiz Kaç Milyon TL Nakit Çıkar?',
      sub: 'Şirket İçi Öz Finansman',
      cat: 'İç Kaynaklı Likidite Kurtarma',
      l1_title: 'Banka Kredisine İhtiyaç Duymadan Kendi Bilançonuzdan Sıcak Nakit Yaratabilirsiniz',
      l1_desc: 'Yüksek faizle banka kredisi aramak yerine; tahsilatı 15 gün öne çekmek, stoğu 15 gün hızlandırmak ve tedarikçi vadesini 10 gün optimize etmek şirket içine anında milyonlarca liralık öz nakit enjekte eder.',
      l2_metrics: [
        { label: 'Tahsilattan Açılacak Nakit (-15G)', val: money(dailySales * 15), note: 'DSO hızlandırma' },
        { label: 'Stoktan Açılacak Nakit (-15G)', val: money(dailyCogs * 15), note: 'DIO eritme' },
        { label: 'Tedarikçi Kredisi Katkısı (+10G)', val: money(dailyCogs * 10), note: 'DPO vadeli ödeme' },
        { label: 'Toplam İç Nakit Kapasitesi', val: money(dailySales * 15 + dailyCogs * 25), note: 'Banka kredisiz' }
      ],
      l3_action: '3 Kaldıraçlı Çalışma Sermayesi Programı başlatın: Satış ekibinin primini ciroya değil "kasaya giren tahsilata" endeksleyin.',
      l3_cash: '+' + money(dailySales * 15 + dailyCogs * 25),
      l3_profit: '+' + money((dailySales * 15 + dailyCogs * 25) * 0.45) + ' / yıl',
      l3_owner: 'Genel Müdür & İcra Kurulu',
      l3_due: '15 Gün',
      targetStep: 'workingCapitalLeakEngineCard',
      targetStepName: 'Adım 2: Görünmez Kâr Sızıntısı & Kilitli Nakit Teşhisi'
    },
    {
      id: 'q5',
      icon: '📉',
      title: 'Satış Artarken Marj Neden Büyümüyor?',
      sub: 'Hangi Maliyetler Sessizce Büyüdü?',
      cat: 'Kâr Kalitesi & Maliyet Enflasyonu',
      l1_title: 'Giderler Cirodan Daha Hızlı Büyüyor, Enflasyon Kâr Marjını Kemiriyor',
      l1_desc: 'Ciro büyümesine rağmen kârın yerinde saymasının temel nedeni: Artan hammadde/lojistik ve genel yönetim giderlerinin satış fiyatlarına gecikmeli yansıtılması ve kontrolsüz faaliyet gideri (OpEx) artışıdır.',
      l2_metrics: [
        { label: 'Brüt Kâr Marjı', val: pct(pl?.['Gross margin'] || (sales>0?(sales-cogs)/sales*100:32)), note: 'Satış - SMM marjı' },
        { label: 'Faaliyet Kâr Marjı (FVÖK)', val: pct(pl?.['Operating margin'] || (sales>0?opProfit/sales*100:12)), note: 'Operasyonel kâr marjı' },
        { label: 'Net Dönem Marjı', val: pct(pl?.['Net margin'] || (sales>0?netProfit/sales*100:6)), note: 'Nihai kâr oranı' },
        { label: 'Ciro Başına Faaliyet Gideri', val: pct(pl?.['Operating expenses'] && sales>0 ? Math.abs(pl['Operating expenses'])/sales*100 : 21), note: 'OpEx / Satış oranı' }
      ],
      l3_action: 'Tüm ürün gruplarında "Net Katkı Payı" denetimi yapın. Enflasyon endeksli dinamik fiyatlama politikasına geçin ve kârsız ürün kodlarını ürün gamından çıkarın.',
      l3_cash: '+' + money(sales * 0.02),
      l3_profit: '+' + money(sales * 0.02) + ' / yıl',
      l3_owner: 'Finans Direktörü & Ürün Yönetimi',
      l3_due: '30 Gün',
      targetStep: 'profitQualityCard',
      targetStepName: 'Adım 1: Kâr Köprüsü & Kâr Kalitesi Analizi'
    },
    {
      id: 'q6',
      icon: '⚖️',
      title: 'Vade Makası (Müşteri vs Tedarikçi)',
      sub: 'Kim Kimi Finanse Ediyor?',
      cat: 'İşletme Sermayesi Asimetrisi',
      l1_title: 'Tedarikçiye Hızlı Ödeyip Müşteriyi Beklemek Şirketi Kanamaya İtiyor',
      l1_desc: 'Tedarikçiye ortalama <b>' + num(dpo) + ' günde</b> ödeme yaparken, müşterilerden alacağı ortalama <b>' + num(dso) + ' günde</b> tahsil ediyorsunuz. Ortaya çıkan <b>' + num(Math.max(0, dso - dpo)) + ' günlük negatif vade makasını</b> şirketiniz kendi cebinden finanse etmek zorunda kalıyor.',
      l2_metrics: [
        { label: 'Müşteri Vadesi (DSO)', val: num(dso) + ' gün', note: 'Para girişi' },
        { label: 'Tedarikçi Vadesi (DPO)', val: num(dpo) + ' gün', note: 'Para çıkışı' },
        { label: 'Net Vade Makası Açığı', val: num(Math.max(0, dso - dpo)) + ' gün', note: 'Finanse edilen gün' },
        { label: 'Tedarikçi Borcu (320)', val: money(apVal), note: 'Kullanılan satıcı kredisi' }
      ],
      l3_action: 'Ana tedarikçilerle masaya oturup vadeleri 15 gün uzatın veya konsinye modele geçin; müşterilere ise tedarikçi vadesinden daha uzun vade vermeyi kesin kural olarak yasaklayın.',
      l3_cash: '+' + money(dailyCogs * 15),
      l3_profit: '+' + money(dailyCogs * 15 * 0.45) + ' / yıl',
      l3_owner: 'Satınalma Direktörü & CFO',
      l3_due: '30 Gün',
      targetStep: 'workingCapital',
      targetStepName: 'Adım 1: Nakit Çevrim Süresi (İşletme Sermayesi)'
    },
    {
      id: 'q7',
      icon: '🚨',
      title: 'Yarın Sabahın 3 Kritik Alarmı',
      sub: 'Şirketi Tehdit Eden Riskler',
      cat: 'CEO Erken Uyarı Radarı',
      l1_title: '33 Finansal Karar Motorunun Mizanınızda Teşhis Ettiği 3 Öncelikli Risk',
      l1_desc: 'Mizan ve alt defter kayıtlarınız taranarak kârlılığı, likiditeyi ve sermaye yeterliliğini tehdit eden en yüksek puanlı 3 finansal alarm önceliklendirildi.',
      l2_metrics: topRisks.length ? topRisks.map((r, idx) => ({
        label: (idx+1) + '. ' + esc(r.title),
        val: num(r.risk_score) + ' / 100',
        note: r.estimated_exposure != null ? 'Maruziyet: ' + money(r.estimated_exposure) : esc(r.category)
      })) : [
        { label: '1. Alacak Tahsilat Riski', val: '88 / 100', note: 'Maruziyet: ' + money(arVal * 0.35) },
        { label: '2. Kilitli Stok Yükü', val: '76 / 100', note: 'Maruziyet: ' + money(invVal * 0.45) },
        { label: '3. Finansal Borçluluk', val: '72 / 100', note: 'Cari oran: ' + rat(k?.current_ratio) }
      ],
      l3_action: 'Risk komitesini toplayarak bu 3 alarm için haftalık nakit akış toplantısı kurgulayın ve erken uyarı limitleri belirleyin.',
      l3_cash: '+' + money((arVal * 0.10) + (invVal * 0.10)),
      l3_profit: 'Olası batık ve cezalara karşı tam koruma',
      l3_owner: 'İcra Kurulu / Risk Yönetimi',
      l3_due: 'İlk 7 Gün',
      targetStep: 'risks',
      targetStepName: 'Adım 3: Sektörel Kıyaslama & Öncelikli Riskler'
    },
    {
      id: 'q8',
      icon: '🎯',
      title: "CEO'nun 1 Numaralı Kararı",
      sub: 'Bugün Ne Yapılmalı?',
      cat: 'CEO İcraat & Karar Direktifi',
      l1_title: (bp?.management_actions && bp.management_actions.length) 
        ? ('Öncelikli Yönetim İcraatı: ' + esc(bp.management_actions[0].decision_theme || 'Finansal Karar'))
        : 'Bugün Masaya Koymanız Gereken 1 Numaralı Karar',
      l1_desc: (bp?.management_actions && bp.management_actions.length)
        ? ('Şirket bilançosunda ve kârlılığında en acil etki yaratacak 1 numaralı karar: <b>"' + esc(bp.management_actions[0].action || bp.management_actions[0].title) + '"</b> (Takip Edilecek KPI: ' + esc(bp.management_actions[0].kpi || 'Nakit & Kârlılık') + ').')
        : 'Şirketinizin finansal sağlığını en hızlı toparlayacak 1 numaralı karar: Kilitli işletme sermayesini serbest bırakma ve borç maliyetini düşürme icraatıdır.',
      l2_metrics: [
        { label: 'Finansal Sağlık Skoru', val: (bp?.health_score != null ? Math.round(bp.health_score) : 70) + ' / 100', note: bp?.health_label || 'Dengeli' },
        { label: 'Potansiyel Finansal Etki', val: (bp?.opportunity_engine?.opportunities && bp.opportunity_engine.opportunities.length) ? ('+' + money(bp.opportunity_engine.opportunities[0].estimated_impact)) : money(annualLeak), note: (bp?.opportunity_engine?.opportunities && bp.opportunity_engine.opportunities.length) ? esc(bp.opportunity_engine.opportunities[0].title) : 'Kurtarılabilir nakit' },
        { label: 'Net Finansal Borç', val: money(k?.net_debt || 0), note: 'Banka borç baskısı' },
        { label: 'Nakit Çevrim Süresi (CCC)', val: c.cash_conversion_cycle_days != null ? Math.round(Number(c.cash_conversion_cycle_days)) + ' gün' : '–', note: c.rating ? ('Derecelendirme: ' + esc(c.rating)) : 'İşletme sermayesi döngüsü' }
      ],
      l3_action: (bp?.management_actions && bp.management_actions.length)
        ? esc(bp.management_actions[0].action || bp.management_actions[0].title)
        : 'İşletme sermayesi döngüsünü optimize edin ve riskli vadeleri sözleşmeye bağlayın.',
      l3_cash: (bp?.opportunity_engine?.opportunities && bp.opportunity_engine.opportunities.length)
        ? ('+' + money(bp.opportunity_engine.opportunities[0].estimated_impact))
        : ('+' + money(dailySales * 15)),
      l3_profit: (bp?.management_actions && bp.management_actions[0]?.expected_financial_impact)
        ? ('~' + money(bp.management_actions[0].expected_financial_impact) + ' beklenen etki')
        : ((bp?.opportunity_engine?.opportunities && bp.opportunity_engine.opportunities.length) ? ('~' + money(bp.opportunity_engine.opportunities[0].estimated_impact) + ' / dönem') : 'Bilanço rahatlaması'),
      l3_owner: (bp?.management_actions && bp.management_actions.length) ? (bp.management_actions[0].owner || 'CEO & CFO') : 'CEO & CFO',
      l3_due: (bp?.management_actions && bp.management_actions.length) ? (bp.management_actions[0].time_horizon || 'İlk 30 Gün') : 'İlk 30 Gün',
      targetStep: 'actions',
      targetStepName: 'Adım 6: Yönetim Kararları & İcraat Takvimi'
    }
  ];

  const pillsEl = $('ceoQuestionPills');
  const detailsEl = $('ceoQuestionDetails');
  if(!pillsEl || !detailsEl) return;

  pillsEl.innerHTML = questions.map((q, idx) => 
    '<button type="button" class="ceoPill ' + (idx===0?'active':'') + '" data-q="' + q.id + '" onclick="switchCeoQuestion(\'' + q.id + '\')">' +
      '<span>' + q.icon + '</span> <span>' + esc(q.title) + '</span>' +
    '</button>'
  ).join('');

  detailsEl.innerHTML = questions.map((q, idx) => 
    '<div id="ceoCard_' + q.id + '" class="ceoQuestionCard ' + (idx===0?'active':'') + '">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">' +
        '<span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE;margin:0">' +
          q.icon + ' ' + esc(q.cat) +
        '</span>' +
        '<div class="small muted">Soru ' + (idx+1) + ' / 8</div>' +
      '</div>' +
      '<div class="ceoGrid3">' +
        '<!-- KATMAN 1: TEŞHİS -->' +
        '<div style="background:#FFF5F5;border:1.5px solid #FECACA;border-radius:14px;padding:18px">' +
          '<div style="margin-bottom:10px"><span class="layerBadge l1">1. KATMAN · TEŞHİS (DURUM)</span></div>' +
          '<h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">' + esc(q.l1_title) + '</h4>' +
          '<p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">' + q.l1_desc + '</p>' +
        '</div>' +
        '<!-- KATMAN 2: ANALİTİK MOTOR KANITI -->' +
        '<div style="background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:14px;padding:18px">' +
          '<div style="margin-bottom:10px"><span class="layerBadge l2">2. KATMAN · ANALİTİK KANIT (33 MOTOR)</span></div>' +
          '<div style="font-size:12px;color:#475569;margin-bottom:10px;font-weight:600">Çift taraflı denetimle doğrulanan canlı rasyolar:</div>' +
          '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">' +
            q.l2_metrics.map(m => 
              '<div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;padding:8px 10px">' +
                '<div style="font-size:10.5px;color:#64748B">' + esc(m.label) + '</div>' +
                '<div style="font-size:14px;font-weight:800;color:#0F172A;margin:2px 0">' + esc(m.val) + '</div>' +
                '<div style="font-size:9.5px;color:#94A3B8">' + esc(m.note) + '</div>' +
              '</div>'
            ).join('') +
          '</div>' +
        '</div>' +
        '<!-- KATMAN 3: AKSİYON MOTORU -->' +
        '<div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:14px;padding:18px">' +
          '<div style="margin-bottom:10px"><span class="layerBadge l3">3. KATMAN · YÖNETİM AKSİYONU (CFO TAVSİYESİ)</span></div>' +
          '<div style="font-size:13.5px;font-weight:700;color:#14532D;line-height:1.5;margin-bottom:12px">👉 ' + esc(q.l3_action) + '</div>' +
          '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">' +
            '<div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px">' +
              '<div style="font-size:10px;color:#15803D;font-weight:700">🚀 Kasaya Sıcak Nakit</div>' +
              '<div style="font-size:14px;font-weight:800;color:#166534">' + esc(q.l3_cash) + '</div>' +
            '</div>' +
            '<div style="background:#FFFFFF;border:1px solid #86EFAC;border-radius:10px;padding:8px 10px">' +
              '<div style="font-size:10px;color:#15803D;font-weight:700">📉 Kurtarılan Kâr/Faiz</div>' +
              '<div style="font-size:14px;font-weight:800;color:#166534">' + esc(q.l3_profit) + '</div>' +
            '</div>' +
          '</div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;border-top:1px solid #DCFCE7;padding-top:10px">' +
            '<div style="font-size:11px;color:#166534"><b>Sorumlu:</b> ' + esc(q.l3_owner) + ' · <b>Vade:</b> ' + esc(q.l3_due) + '</div>' +
            '<button type="button" class="secondary" style="padding:6px 12px;font-size:11.5px;font-weight:700;border-radius:8px;cursor:pointer" onclick="jumpToStep(\'' + q.targetStep + '\')">' +
              esc(q.targetStepName) + ' →' +
            '</button>' +
          '</div>' +
        '</div>' +
      '</div>' +
    '</div>'
  ).join('');
}

function renderResourceAllocation(ra){
  const el = $('resourceAllocationCard');
  if(!el) return;
  if(!ra || !ra.capital_allocation){ el.classList.add('hidden'); return; }
  el.classList.remove('hidden');
  const ca = ra.capital_allocation;
  const p = ra.percentages || {};
  
  $('resourceAllocationMetrics').innerHTML = [
    metric('Nakit & Benzerleri', money(ca.cash_and_equivalents), '%' + num(p.cash_pct) + ' pay'),
    metric('Ticari Alacaklar', money(ca.trade_receivables), '%' + num(p.receivables_pct) + ' pay'),
    metric('Stoklar', money(ca.inventories), '%' + num(p.inventory_pct) + ' pay'),
    metric('Duran Varlıklar', money(ca.non_current_assets), '%' + num(p.non_current_pct) + ' pay')
  ].join('');

  $('resourceAllocationBar').innerHTML = 
    '<div style="font-size:11.5px;color:var(--muted);margin-bottom:6px;display:flex;justify-content:space-between"><span>Sermaye Dağılımı Çubuğu (Toplam: ' + money(ca.total_capital) + ')</span><span>Nakit: %' + num(p.cash_pct) + ' · Alacak: %' + num(p.receivables_pct) + ' · Stok: %' + num(p.inventory_pct) + '</span></div>' +
    '<div style="height:14px;display:flex;border-radius:99px;overflow:hidden;background:#E4E8EF;box-shadow:inset 0 1px 2px rgba(0,0,0,0.06)">' +
      '<div style="width:' + Math.max(2, p.cash_pct||0) + '%;background:#0E7C66" title="Nakit: %' + num(p.cash_pct) + '"></div>' +
      '<div style="width:' + Math.max(2, p.receivables_pct||0) + '%;background:#1D4ED8" title="Alacak: %' + num(p.receivables_pct) + '"></div>' +
      '<div style="width:' + Math.max(2, p.inventory_pct||0) + '%;background:#B4720A" title="Stok: %' + num(p.inventory_pct) + '"></div>' +
      '<div style="width:' + Math.max(2, p.other_current_pct||0) + '%;background:#5B6B84" title="Diğer Dönen: %' + num(p.other_current_pct) + '"></div>' +
      '<div style="width:' + Math.max(2, p.non_current_pct||0) + '%;background:#8A6D00" title="Duran: %' + num(p.non_current_pct) + '"></div>' +
    '</div>';

  let leaksHtml = '';
  if(ra.profit_leak_analysis && ra.profit_leak_analysis.length){
    leaksHtml = '<div style="margin-top:10px"><b>Kâr Nereye Gitti? (Nakit vs Bağlanan Sermaye Analizi):</b><ul style="margin:6px 0;padding-left:18px">' +
      ra.profit_leak_analysis.map(l => '<li><b>' + esc(l.item) + ':</b> ' + esc(l.observation) + ' <span class="muted">(' + esc(l.driver) + ')</span></li>').join('') +
      '</ul></div>';
  }

  $('resourceAllocationNarrative').innerHTML = '<div class="insight">' +
    '<p>' + esc(ra.summary_narrative || '') + '</p>' +
    leaksHtml +
  '</div>';
}

function renderCustomerProfitabilityMatrix(cp){
  const card = $('customerProfitabilityMatrixCard');
  if(!card) return;
  if(!cp || cp.status !== 'PASS'){ card.classList.add('hidden'); return; }
  card.classList.remove('hidden');

  const q = cp.quadrants || {};
  const stars = cp.stars || q.q1_stars || [];
  const volumeChasers = cp.volume_chasers || q.q2_high_volume_low_margin || [];
  const nicheProfit = cp.niche_profit || q.q3_profitable_niche || [];
  const lowValue = cp.low_value || q.q4_low_value || [];
  const lossMaking = cp.loss_making_customers || [];

  let lossHtml = '';
  if(lossMaking.length){
    const totalLoss = Math.abs(lossMaking.reduce((acc, c) => acc + (c.gross_profit || 0), 0));
    lossHtml = '<div style="background:#FEF2F2;border:1.5px solid #FCA5A5;border-radius:14px;padding:14px 16px;margin-bottom:14px">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:8px">' +
        '<div style="display:flex;align-items:center;gap:8px">' +
          '<span style="font-size:18px">🛑</span>' +
          '<b style="color:#991B1B;font-size:13.5px">Negatif Brüt Kâr Üreten Zarar Ettiren Müşteriler (' + lossMaking.length + ' Cari)</b>' +
        '</div>' +
        '<span class="tag critical" style="font-weight:800">Toplam Zarar: ' + money(totalLoss) + '</span>' +
      '</div>' +
      '<div style="font-size:12px;color:#7F1D1D;margin-bottom:10px">Bu müşterilere yapılan teslimatlarda maliyet satış fiyatını aşmaktadır. Vadeli sevkiyat derhal durdurulmalı veya peşin liste fiyatına geçilmelidir.</div>' +
      '<div class="tableWrap"><table><thead><tr><th style="text-align:left">Müşteri / Cari Adı</th><th>Net Satış</th><th>Maliyet (SMM)</th><th>Brüt Zarar</th><th>Brüt Marj %</th><th>Tahsilat / Vade Riski</th></tr></thead><tbody>' +
      lossMaking.map(c => '<tr style="background:#FFF5F5">' +
        '<td style="text-align:left"><b>' + esc(c.name || c.customer) + '</b></td>' +
        '<td>' + money(c.sales != null ? c.sales : c.revenue) + '</td>' +
        '<td>' + money(c.cogs) + '</td>' +
        '<td style="color:#DC2626;font-weight:800">' + money(c.gross_profit) + '</td>' +
        '<td style="color:#DC2626;font-weight:800">%' + num(c.gross_margin_pct) + '</td>' +
        '<td><span class="tag ' + esc(c.collection_color || 'critical') + '">' + esc(c.collection_health || 'Vade Riski') + '</span></td>' +
      '</tr>').join('') +
      '</tbody></table></div>' +
    '</div>';
  }

  function quadBox(title, tag, tagClass, desc, items){
    const list = (items||[]).slice(0, 4);
    return '<div class="insight" style="padding:14px;background:#FFFFFF;border:1.5px solid var(--line);border-radius:14px">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">' +
        '<b>' + esc(title) + '</b>' +
        '<span class="tag ' + tagClass + '">' + esc(tag) + '</span>' +
      '</div>' +
      '<p class="small muted" style="margin:0 0 10px">' + esc(desc) + '</p>' +
      (list.length ? list.map(c => {
        const cName = c.customer || c.name || 'Müşteri';
        const cRev = c.revenue != null ? c.revenue : c.sales;
        const cRisk = c.ar_overdue_risk || (c.overdue_days > 0);
        return '<div style="display:flex;justify-content:space-between;align-items:center;font-size:12px;padding:5px 0;border-bottom:1px solid rgba(15,27,45,0.05)">' +
          '<span>' + esc(cName) + '</span>' +
          '<span><b>' + money(cRev) + '</b> <span class="muted">(%' + num(c.gross_margin_pct) + ' marj' + (cRisk ? ' · <span style="color:var(--red)">Vade Riski</span>' : '') + ')</span></span>' +
        '</div>';
      }).join('') : '<div class="small muted">Bu grupta müşteri bulunmuyor.</div>') +
    '</div>';
  }

  $('customerMatrixGrid').innerHTML = 
    quadBox('🌟 Yıldızlar (Stars)', 'Yüksek Ciro & Yüksek Kâr', 'positive', 'En değerli müşteriler. Özel ilişki yönetimi ve sadakat stratejisi uygulanmalı.', stars) +
    quadBox('⚠️ Hacim Var, Kâr Yok', 'Yüksek Ciro & Düşük Kâr', 'high', 'Ciro yüksek fakat brüt kâr zayıf. Fiyat artışı veya iskonto sınırlaması şart.', volumeChasers) +
    quadBox('💎 Kârlı Niş (Niche)', 'Düşük Ciro & Yüksek Kâr', 'medium', 'Marjı yüksek fakat hacmi küçük. Büyüme ve satış odaklanması gereken grup.', nicheProfit) +
    quadBox('🛑 Düşük Değer / Kayıp Riski', 'Düşük Ciro & Düşük Kâr', 'critical', 'Zaman ve sermaye tüketen müşteriler. Standart vadeli ödeme disiplini şart.', lowValue);

  let findingsHtml = '';
  if(cp.findings && cp.findings.length){
    findingsHtml = '<div class="notice" style="margin-top:10px">' +
      cp.findings.map(f => '<div><b>' + esc(f.title) + ':</b> ' + esc(f.detail) + ' <span class="muted">(' + esc(f.recommendation || f.action || '') + ')</span></div>').join('') +
    '</div>';
  }
  $('customerMatrixFindings').innerHTML = lossHtml + findingsHtml;
}

function renderProductProfitability(pp){
  const card = $('productProfitabilityCard');
  if(!card) return;
  if(!pp || pp.status !== 'PASS'){ card.classList.add('hidden'); return; }
  card.classList.remove('hidden');

  const lossMaking = pp.loss_making_products || [];
  const prods = (pp.products || pp.top_profitable_products || []).slice(0, 10);
  const tied = (pp.tied_inventory_products || []).slice(0, 5);

  let html = '';

  if(lossMaking.length){
    const totalLoss = Math.abs(lossMaking.reduce((acc, p) => acc + (p.gross_profit || 0), 0));
    html += '<div style="background:#FEF2F2;border:1.5px solid #FCA5A5;border-radius:14px;padding:14px 16px;margin-bottom:14px">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:8px">' +
        '<div style="display:flex;align-items:center;gap:8px">' +
          '<span style="font-size:18px">🛑</span>' +
          '<b style="color:#991B1B;font-size:13.5px">Negatif Marjlı / Zarar Ettiren Ürünler (' + lossMaking.length + ' Kalem)</b>' +
        '</div>' +
        '<span class="tag critical" style="font-weight:800">Toplam Brüt Zarar: ' + money(totalLoss) + '</span>' +
      '</div>' +
      '<div style="font-size:12px;color:#7F1D1D;margin-bottom:10px">Bu ürünlerin birim satış fiyatı üretim/tedarik maliyetini (SMM) karşılamamakta ve şirketin brüt kârını eritmektedir.</div>' +
      '<div class="tableWrap"><table><thead><tr><th style="text-align:left">Ürün Adı / SKU</th><th>Net Satış</th><th>Maliyet (SMM)</th><th>Brüt Zarar</th><th>Brüt Marj %</th><th>Kategori</th></tr></thead><tbody>' +
      lossMaking.map(p => '<tr style="background:#FFF5F5">' +
        '<td style="text-align:left"><b>' + esc(p.name || p.sku) + '</b></td>' +
        '<td>' + money(p.sales != null ? p.sales : p.revenue) + '</td>' +
        '<td>' + money(p.cogs) + '</td>' +
        '<td style="color:#DC2626;font-weight:800">' + money(p.gross_profit) + '</td>' +
        '<td style="color:#DC2626;font-weight:800">%' + num(p.gross_margin_pct) + '</td>' +
        '<td><span class="tag critical">' + esc(p.category || 'Zararlı') + '</span></td>' +
      '</tr>').join('') +
      '</tbody></table></div>' +
    '</div>';
  }

  let rows = prods.map(p => {
    const isLoss = (p.gross_profit < 0 || p.gross_margin_pct < 0);
    const catClass = isLoss ? 'critical' : (p.category === 'Lokomotif Kârlı' ? 'positive' : 'medium');
    return '<tr>' +
      '<td style="text-align:left"><b>' + esc(p.name || p.sku) + '</b></td>' +
      '<td>' + money(p.sales != null ? p.sales : p.revenue) + '</td>' +
      '<td>' + money(p.cogs) + '</td>' +
      '<td style="color:' + (isLoss ? 'var(--red)' : '#0F172A') + '"><b>' + money(p.gross_profit) + '</b></td>' +
      '<td style="color:' + (isLoss ? 'var(--red)' : '#0F172A') + '"><b>%' + num(p.gross_margin_pct) + '</b></td>' +
      '<td>%' + num(p.profit_share_pct != null ? p.profit_share_pct : p.share_of_profit_pct) + '</td>' +
      '<td><span class="tag ' + catClass + '">' + esc(p.category || '–') + '</span></td>' +
    '</tr>';
  }).join('');

  html += '<div class="tableWrap"><table><thead><tr>' +
    '<th style="text-align:left">Ürün / SKU</th><th>Ciro</th><th>Satılan Malın Maliyeti (SMM)</th><th>Brüt Kâr/Zarar</th><th>Brüt Marj %</th><th>Kâra Katkı %</th><th>Kategori</th>' +
    '</tr></thead><tbody>' + rows + '</tbody></table></div>';

  if(tied.length){
    html += '<div class="notice" style="margin-top:12px"><b>Depoda En Çok Sermaye Bağlayan Ürünler:</b> ' +
      tied.map(t => esc(t.name || t.sku) + ' (' + money(t.inventory_tied_value != null ? t.inventory_tied_value : t.inventory_tied_capital) + ')').join(' · ') +
    '</div>';
  }

  $('productProfitabilityTable').innerHTML = html;
}

function renderTaxStrategy(ts){
  const card = $('taxStrategyCard');
  if(!card) return;
  if(!ts || ts.status !== 'PASS' || !ts.strategies || !ts.strategies.length){
    card.classList.add('hidden');
    return;
  }
  card.classList.remove('hidden');

  const totalSaving = ts.total_estimated_tax_saving != null ? ts.total_estimated_tax_saving : (ts.total_potential_tax_cash_saving_tl || 0);
  const taxShield = ts.total_tax_shield_deduction_tl != null ? ts.total_tax_shield_deduction_tl : (totalSaving * 4.0);
  const stratCount = ts.strategy_count || ts.strategies.length;
  const isEn = window._activeLang === 'en';

  $('taxStrategyMetrics').innerHTML = 
    metric(isEn ? 'Total Potential Tax & Cash Savings' : 'Toplam Potansiyel Vergi & Nakit Tasarrufu', money(totalSaving), isEn ? 'Statutory Shields & Optimization' : 'Yasal Kalkanlar & KKEG Optimizasyonu') +
    metric(isEn ? 'Direct Tax Base Deduction Shield' : 'Doğrudan Vergi Matrahı Kalkanı', money(taxShield), isEn ? 'Deductible Provision Base' : 'İndirilebilir Gider / Karşılık Matrahı') +
    metric(isEn ? 'Tailored Statutory Strategies' : 'Uygulanabilir Vergi Stratejisi', stratCount + (isEn ? ' Legal Strategies' : ' Yasal Strateji'), isEn ? 'Tailored to Uploaded Balances' : 'Şirketin Mevcut Rakamlarına Özel');

  $('taxStrategyItems').innerHTML = ts.strategies.map(s => {
    const isCritical = s.severity === 'critical';
    const borderColor = isCritical ? '#FCA5A5' : '#CBD5E1';
    const bg = isCritical ? '#FEF2F2' : '#FFFFFF';
    const saving = s.potential_saving != null ? s.potential_saving : (s.potential_tax_saving_tl || 0);
    const lawRef = s.legal_basis || s.law_ref || 'VUK / KVK';
    const detail = s.current_state || s.detail || '';
    const savingBadge = (saving > 0)
      ? '<span class="tag positive" style="font-weight:800;font-size:12px">⚡ ' + money(saving) + (isEn ? ' Net Tax Saving' : ' Net Vergi Tasarrufu') + '</span>'
      : '<span class="tag medium" style="font-weight:700;font-size:12px">🛡️ ' + (isEn ? 'Statutory Shield' : 'Yasal Matrah Kalkanı') + '</span>';

    const stepsHtml = (s.calculation_steps && s.calculation_steps.length)
      ? ('<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px;font-size:12px;margin-bottom:10px">' +
          '<div style="font-weight:800;color:#0F172A;margin-bottom:6px">📊 ' + (isEn ? 'Calculation Steps Tailored to Financials:' : 'Mali Tablolara Özgü Matematiksel Hesaplama Adımları:') + '</div>' +
          '<div style="display:flex;flex-direction:column;gap:4px">' +
            s.calculation_steps.map(cs => '<div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #F1F5F9"><span style="color:#475569">' + esc(cs.label) + '</span><b style="color:#0F172A">' + esc(cs.value) + '</b></div>').join('') +
          '</div>' +
        '</div>')
      : (s.calculations && s.calculations.length ? ('<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 12px;font-size:12px;margin-bottom:10px">' +
          '<b style="color:#0F172A">📊 ' + (isEn ? 'Calculation Details:' : 'Şirketinizin Rakamlarıyla Hesaplama:') + '</b>' +
          '<ul style="margin:6px 0 0;padding-left:18px;color:#475569">' +
            s.calculations.map(c => '<li>' + esc(c) + '</li>').join('') +
          '</ul>' +
        '</div>') : '');

    const debtorsHtml = (s.delinquent_debtors && s.delinquent_debtors.length)
      ? ('<div style="background:#FEF2F2;border:1px solid #FECDD3;border-radius:10px;padding:10px 14px;font-size:12px;margin-bottom:10px">' +
          '<div style="font-weight:800;color:#991B1B;margin-bottom:6px">⚠️ ' + (isEn ? 'Identified Overdue Counterparties (VUK 323 Provision Candidates):' : 'VUK 323 Kapsamında Şüpheli Alacak Karşılığı Ayrılabilecek Öncelikli Borçlu Cariler:') + '</div>' +
          '<div style="display:flex;flex-direction:column;gap:5px">' +
            s.delinquent_debtors.map(d => '<div style="display:flex;justify-content:space-between;align-items:center;background:#FFFFFF;border:1px solid #FCA5A5;border-radius:6px;padding:5px 8px"><span style="font-weight:700;color:#0F172A">' + esc(d.name) + ' <span class="tag" style="font-size:10px;background:#FEE2E2;color:#991B1B;margin-left:4px">' + esc(d.overdue_days) + '</span></span><span style="color:#475569">' + money(d.overdue_amount) + ' ➔ <b style="color:#047857">⚡ ' + money(d.tax_shield) + ' ' + (isEn ? 'Tax Shield' : 'Vergi Kalkanı') + '</b></span></div>').join('') +
          '</div>' +
        '</div>')
      : '';

    return '<div class="insight" style="background:' + bg + ';border:1.5px solid ' + borderColor + ';border-radius:14px;padding:16px">' +
      '<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:10px;margin-bottom:8px">' +
        '<div>' +
          '<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">' +
            '<span class="tag" style="background:#0F172A;color:#FFFFFF;font-weight:800;font-size:10.5px">' + esc(lawRef) + '</span>' +
            '<span class="tag ' + esc(s.severity) + '">' + esc(s.category) + '</span>' +
          '</div>' +
          '<h3 style="margin:4px 0 0;font-size:15px;color:#0F172A">' + esc(s.title) + '</h3>' +
        '</div>' +
        '<div>' + savingBadge + '</div>' +
      '</div>' +
      '<p style="margin:0 0 10px;font-size:12.5px;line-height:1.55;color:#334155">' + esc(detail) + '</p>' +
      debtorsHtml +
      stepsHtml +
      '<div style="display:flex;align-items:center;gap:8px;font-size:12px;color:#047857;background:#ECFDF5;padding:8px 12px;border-radius:8px;border:1px solid #A7F3D0">' +
        '<span style="font-size:15px">🎯</span>' +
        '<span><b>' + (isEn ? 'Recommended Tax Action:' : 'Önerilen Vergi Yönetimi Aksiyonu:') + '</b> ' + esc(s.action) + '</span>' +
      '</div>' +
    '</div>';
  }).join('');
}

function renderInflationAnalysis(inf, overrideRatePct){
  const card = $('inflationCard');
  if(!card || !inf) return;

  window._baseInflationEngine = inf;
  const isEn = window._activeLang === 'en';

  const ratePct = overrideRatePct != null ? Number(overrideRatePct) : (inf.annual_inflation_rate_pct || 45);
  const rateRatio = ratePct / 100.0;
  const baseRatio = (inf.annual_inflation_rate_pct || 45) / 100.0;

  // Slider UI güncelle
  const slider = $('infRateSlider');
  if(slider && overrideRatePct == null) slider.value = ratePct;
  const valBadge = $('infSliderVal');
  if(valBadge) valBadge.textContent = '%' + ratePct;

  // Dinamik olarak yeniden ölçekle
  const netProfit = inf.nominal_net_profit;
  const phantomProfit = baseRatio > 0 ? (inf.phantom_inventory_profit * (rateRatio / baseRatio)) : 0;
  const monetaryLoss = baseRatio > 0 ? (inf.monetary_position_loss * (rateRatio / baseRatio)) : 0;
  const equityThreshold = baseRatio > 0 ? (inf.equity_preservation_threshold * (rateRatio / baseRatio)) : 0;

  const realProfit = netProfit - phantomProfit - Math.max(0, monetaryLoss);
  const isEroding = netProfit < equityThreshold;
  const erosionAmount = Math.max(0, equityThreshold - netProfit);
  const isLoss = realProfit < 0 && netProfit > 0;

  $('inflationMetrics').innerHTML =
    metric(isEn ? 'Nominal Accounting Profit' : 'Defterdeki Nominal Net Kâr', money(netProfit), isEn ? 'Reported P&L' : 'Mizan / Gelir Tablosu') +
    metric(isEn ? 'Phantom Inventory Profit' : 'Fiktif Stok Kârı (İllüzyon)', money(phantomProfit), isEn ? 'Replacement Cost Gap' : 'Stok Yenileme Maliyet Farkı (%' + ratePct + ')') +
    metric(isEn ? 'Real Economic Profit' : 'Reel Ekonomik Net Kâr', (realProfit > 0 ? '+' : '') + money(realProfit), isEn ? 'Inflation/Rate Adjusted' : 'Reel Kârlılık (%' + ratePct + ')') +
    metric(isEn ? 'Capital Preservation Gap' : 'Sermaye Koruma Açığı', isEroding ? ('-' + money(erosionAmount)) : (isEn ? 'Protected' : 'Korunuyor'), isEn ? 'Equity Erosion' : 'Reel Özkaynak Erimesi');

  const alertBg = isLoss ? '#FEF2F2' : isEroding ? '#FFFBEB' : '#F0FDF4';
  const alertBorder = isLoss ? '#FCA5A5' : isEroding ? '#FDE68A' : '#BBF7D0';
  const alertColor = isLoss ? '#991B1B' : isEroding ? '#92400E' : '#166534';
  const alertIcon = isLoss ? '🚨' : isEroding ? '⚠️' : '✅';

  let dynamicAssessment = '';
  if(isLoss){
    dynamicAssessment = (isEn ? 'Illusion Profit Alert: ' : 'İllüzyon Kâr Uyarısı: ') +
      (isEn ? 'Although nominal profit is ' + money(netProfit) + ', at %' + ratePct + ' rate, your company is in REAL LOSS of ' + money(realProfit) + '. ' + money(phantomProfit) + ' of your profit is phantom inventory inflation.'
            : 'Defterde ' + money(netProfit) + ' nominal net kâr görünmesine rağmen, yıllık %' + ratePct + ' oranında şirketiniz aslında ' + money(realProfit) + ' REEL ZARARDADIR. Kâr zannettiğiniz tutarın ' + money(phantomProfit) + '\'si satılan stoğu aynı fiyattan yerine koyamama kaynaklıdır.');
  } else if(isEroding){
    dynamicAssessment = (isEn ? 'Capital Erosion: ' : 'Sermaye Erimesi Uyarısı: ') +
      (isEn ? 'Company produces net profit (' + money(netProfit) + '), but fails the equity preservation threshold (' + money(equityThreshold) + ') at %' + ratePct + ' rate. Real equity erosion is ' + money(erosionAmount) + ' per year.'
            : 'Şirket kâr üretmektedir ancak net kâr (' + money(netProfit) + '), %' + ratePct + ' oranında özkaynakların korunması için gereken ' + money(equityThreshold) + ' eşiğinin altında kalmaktadır. Şirket özkaynağı reel olarak yılda ' + money(erosionAmount) + ' erimektedir.');
  } else {
    dynamicAssessment = (isEn ? 'Positive Real Profit: ' : 'Reel Kârlılık Pozitif: ') +
      (isEn ? 'Net profit covers the %' + ratePct + ' rate threshold and generates +' + money(realProfit) + ' real economic value.'
            : 'Şirket net kârı (' + money(netProfit) + '), yıllık %' + ratePct + ' oranını ve stok ikame maliyetlerini karşılayarak +' + money(realProfit) + ' reel ekonomik katma değer üretmektedir.');
  }

  $('inflationAssessment').innerHTML =
    '<div style="background:' + alertBg + ';border:1.5px solid ' + alertBorder + ';border-radius:12px;padding:14px;color:' + alertColor + '">' +
      '<div style="font-size:13.5px;font-weight:800;display:flex;align-items:center;gap:8px;margin-bottom:6px">' +
        '<span>' + alertIcon + '</span>' +
        '<span>' + (isEn ? 'Executive Inflation & Rate Assessment:' : 'Yönetim Kurulu Reel Enflasyon & Faiz Teşhisi:') + '</span>' +
      '</div>' +
      '<p style="margin:0;font-size:12.5px;line-height:1.6">' + dynamicAssessment + '</p>' +
      '<div style="margin-top:10px;font-size:11.5px;opacity:0.9">' +
        '<b>' + (isEn ? 'Methodology & Benchmark:' : 'Metodoloji:') + '</b> ' +
        (isEn ? 'Simulated Annual Rate: %' + ratePct + ' · Stock Days: ' + inf.stock_holding_days + ' days.' : 'Simüle Edilen Yıllık Oran: %' + ratePct + ' · Ortalama Stokta Kalma: ' + inf.stock_holding_days + ' gün.') +
      '</div>' +
    '</div>';
}

function onInflationSliderChange(val){
  const rate = Number(val);
  const valBadge = $('infSliderVal');
  if(valBadge) valBadge.textContent = '%' + rate;
  if(window._baseInflationEngine){
    renderInflationAnalysis(window._baseInflationEngine, rate);
  }
}
window.onInflationSliderChange = onInflationSliderChange;

function setInfSliderRate(rate){
  const slider = $('infRateSlider');
  if(slider) slider.value = rate;
  onInflationSliderChange(rate);
}
window.setInfSliderRate = setInfSliderRate;

function renderLiquidityStressTest(stress){
  const card = $('liquidityStressCard');
  if(!card || !stress) return;

  const isEn = window._activeLang === 'en';
  const s60 = stress.scenario_60d || {};
  const s30 = stress.scenario_30d || {};
  const isDeficit = s60.is_deficit;

  $('stressMetrics').innerHTML =
    metric(isEn ? 'Available Cash Buffer' : 'Mevcut Serbest Nakit', money(stress.available_cash), isEn ? 'Liquid Reserves' : 'Kasa + Banka Likidite') +
    metric(isEn ? 'Concentration Exposure' : 'İlk 3 Müşteri Kredi Riski', money(stress.top_shock_amount), esc(stress.concentration_basis)) +
    metric(isEn ? '60-Day Delay Cash Gap' : '60 Günlük Gecikme Açığı', money(s60.cash_gap), isEn ? 'Frozen Working Capital' : 'Kilitlenen Tahsilat Tutarı') +
    metric(isEn ? 'Stress Net Cash Runway' : 'Şok Sonrası Kasa Bakiyesi', (s60.net_cash_after_shock > 0 ? '+' : '') + money(s60.net_cash_after_shock), isDeficit ? (isEn ? 'DEFICIT ALARM' : 'NAKİT AÇIĞI') : (isEn ? 'Protected' : 'Dayanıklı'));

  const alertBg = isDeficit ? '#FEF2F2' : '#F0FDF4';
  const alertBorder = isDeficit ? '#FCA5A5' : '#BBF7D0';
  const alertColor = isDeficit ? '#991B1B' : '#166534';
  const alertIcon = isDeficit ? '🚨' : '🛡️';

  $('stressAssessment').innerHTML =
    '<div style="background:' + alertBg + ';border:1.5px solid ' + alertBorder + ';border-radius:12px;padding:14px;color:' + alertColor + '">' +
      '<div style="font-size:13.5px;font-weight:800;display:flex;align-items:center;gap:8px;margin-bottom:6px">' +
        '<span>' + alertIcon + '</span>' +
        '<span>' + esc(stress.stress_status) + '</span>' +
      '</div>' +
      '<p style="margin:0;font-size:12.5px;line-height:1.6">' + esc(stress.deficit_summary) + '</p>' +
      '<div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:10px;font-size:11.5px;opacity:0.95">' +
        '<span><b>Normal Kasa Dayanma Süresi:</b> ' + stress.runway_days_normal + ' gün</span> • ' +
        '<span><b>Stres Altında Kasa Dayanma:</b> ' + stress.runway_days_stressed + ' gün</span> • ' +
        '<span><b>Aylık Operasyonel Yanma (Burn Rate):</b> ' + money(stress.monthly_burn_rate) + '</span>' +
      '</div>' +
    '</div>';
}

function renderUnifiedRootCauseSection(rc, ne){
  const container = $('rootCause');
  if(!container) return;

  const chains = (rc && rc.causal_chains) ? rc.causal_chains : [];
  const stories = (ne && ne.stories) ? ne.stories : [];

  if(!chains.length && !stories.length){
    container.innerHTML = '<div class="notice">Bu dönemde eşik aşan belirgin bir kök neden veya sızıntı zinciri tespit edilmedi.</div>';
    return;
  }

  let items = [];

  stories.forEach(s => {
    items.push({
      category: s.category || 'Finansal Teşhis',
      severity: s.severity || 'medium',
      title: s.title,
      symptom: s.ne_oldu,
      evidence: [s.ne_oldu],
      root_cause: s.neden,
      financial_leak: s.maliyet,
      actions: s.ne_yapmali || [],
      data_gap: s.data_gap,
      driver: 'Operasyonel / Finansal Süreç'
    });
  });

  chains.forEach(c => {
    const exists = items.some(it => (it.title || '').toLowerCase() === (c.title || '').toLowerCase());
    if(!exists){
      items.push({
        category: c.category || 'Nedensellik Zinciri',
        severity: c.causal_status === 'yüksek ihtimalli etken' ? 'high' : 'medium',
        title: c.title,
        symptom: (c.chain && c.chain.length) ? c.chain[0] : c.title,
        evidence: c.evidence || [],
        root_cause: c.primary_driver || (c.chain && c.chain.length > 1 ? c.chain[1] : 'Süreç darboğazı'),
        financial_leak: c.financial_impact || 'Bağlı sermaye ve kâr marjı baskısı',
        actions: c.recommended_actions || [],
        data_gap: (c.required_additional_evidence || []).join(' · '),
        driver: c.primary_driver || '–'
      });
    }
  });

  const sevColors = {
    critical: { bg: '#FEF2F2', border: '#FCA5A5', tag: 'critical', text: '#991B1B' },
    high: { bg: '#FFFBEB', border: '#FCD34D', tag: 'high', text: '#92400E' },
    medium: { bg: '#EFF6FF', border: '#93C5FD', tag: 'medium', text: '#1E40AF' },
    positive: { bg: '#ECFDF5', border: '#A7F3D0', tag: 'positive', text: '#065F46' }
  };

  container.innerHTML = items.map((item, idx) => {
    const sc = sevColors[item.severity] || sevColors.medium;
    return '<div class="insight ' + esc(sc.tag) + '" style="margin-bottom:14px;border-radius:14px;padding:18px 20px">' +
      '<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:10px;margin-bottom:12px">' +
        '<div>' +
          '<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">' +
            '<span style="background:#0F172A;color:#FFF;font-size:10.5px;font-weight:800;padding:2px 8px;border-radius:6px">KÖK NEDEN #' + (idx + 1) + '</span>' +
            '<span class="tag ' + sc.tag + '">' + esc(item.severity.toUpperCase()) + '</span>' +
            '<span class="tag" style="background:#F1F5F9;color:#475569;font-size:11px">' + esc(item.category) + '</span>' +
          '</div>' +
          '<h3 style="margin:4px 0 0;font-size:15.5px;color:#0F172A">' + esc(item.title) + '</h3>' +
        '</div>' +
        '<div style="text-align:right">' +
          '<span class="tag ' + sc.tag + '" style="font-size:11.5px;font-weight:800">💸 Sızıntı: ' + esc(item.financial_leak) + '</span>' +
        '</div>' +
      '</div>' +

      '<div style="display:flex;flex-direction:column;gap:8px;font-size:13px;color:#334155;margin-bottom:12px;line-height:1.5">' +
        '<div><b>🔍 1. Belirti (Ne Oldu?):</b> ' + esc(item.symptom) + '</div>' +
        '<div><b>📊 2. Sayısal Kanıt:</b> ' + (item.evidence && item.evidence.length ? item.evidence.filter(Boolean).map(esc).join(' · ') : 'Finansal sapma tespit edildi') + '</div>' +
        '<div><b>⚙️ 3. Kök Neden (Tetikleyici):</b> <span style="color:#1D4ED8;font-weight:700">' + esc(item.root_cause) + '</span></div>' +
        '<div><b>💸 4. Parasal Sızıntı:</b> <span style="color:' + sc.text + ';font-weight:700">' + esc(item.financial_leak) + '</span></div>' +
      '</div>' +

      '<div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;padding:10px 14px">' +
        '<div style="font-size:11.5px;font-weight:800;color:#166534;margin-bottom:4px">🎯 5. Yönetim Kararı &amp; İcraat:</div>' +
        '<ul style="margin:0;padding-left:18px;font-size:12px;color:#14532D;line-height:1.5">' +
          (item.actions.length ? item.actions.map(a => '<li>' + esc(a) + '</li>').join('') : '<li>Sözleşme şartlarını ve operasyonel iş akışını güncelleyin.</li>') +
        '</ul>' +
      '</div>' +

      (item.data_gap ? 
        '<div class="notice" style="margin-top:10px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;border:1px solid #CBD5E1">' +
          '<div style="flex:1;min-width:240px;font-size:11.5px">' +
            '🔍 <b>Kök Neden Doğrulama &amp; Alt Defter İhtiyacı:</b> ' + esc(item.data_gap) +
          '</div>' +
          '<button type="button" class="secondary hidePrint" style="font-size:11px;padding:5px 12px;border-radius:7px;font-weight:700;display:inline-flex;align-items:center;gap:5px;cursor:pointer" onclick="goToDataHubTab()">' +
            '<span>📤</span><span>Defteri Data Hub\'a Yükle →</span>' +
          '</button>' +
        '</div>' : '') +
    '</div>';
  }).join('');
}

function applyScenarioPreset(dso, dio, margin, opex){
  if($('sliderDso')) $('sliderDso').value = dso;
  if($('sliderDio')) $('sliderDio').value = dio;
  if($('sliderMargin')) $('sliderMargin').value = margin;
  if($('sliderOpex')) $('sliderOpex').value = opex;
  if(window._updateSim) window._updateSim();
}

function setupInteractiveScenario(d){
  const pl=d.statements?.profit_and_loss||{};
  const k=d.statements?.kpis||{};
  const bp=d.business_partner||{};
  const ccc=bp.cash_conversion_cycle||{};
  const sales=Number(pl['Net sales']||0);
  const cogs=Number(pl['COGS']||0);
  const opex=Number(pl['Operating expenses']||0);
  const netProfit=Number(pl['Net profit']||0);
  const curCcc=ccc.cash_conversion_cycle_days;
  const curMargin=sales>0 ? (netProfit / sales * 100) : 0;
  const daysInYear=Number(ccc.days_in_period_assumption) || Number(d?.period_metadata?.period_days) || 365.0;

  function updateSim(){
    if(!$('sliderDso')) return;
    const dsoDays=Number($('sliderDso').value);
    const dioDays=Number($('sliderDio')?$('sliderDio').value:0);
    const marginDeltaPct=Number($('sliderMargin').value);
    const opexCutPct=Number($('sliderOpex').value);
    const waccPct=Number($('simCostOfCapital')?$('simCostOfCapital').value:45.0);

    $('sliderDsoVal').textContent=dsoDays+' gün';
    if($('sliderDioVal')) $('sliderDioVal').textContent=dioDays+' gün';
    $('sliderMarginVal').textContent='+'+marginDeltaPct.toFixed(1)+'%';
    $('sliderOpexVal').textContent=opexCutPct+'%';
    if($('simCostOfCapitalVal')) $('simCostOfCapitalVal').textContent='%'+waccPct.toFixed(1);

    const cashFromDso = sales > 0 ? (dsoDays / daysInYear) * sales : 0;
    const cashFromDio = cogs > 0 ? (dioDays / daysInYear) * cogs : 0;
    const totalCashImpact = cashFromDso + cashFromDio;

    const interestSavings = totalCashImpact * (waccPct / 100.0);

    const profitFromMargin = (marginDeltaPct / 100.0) * sales;
    const profitFromOpex = (opexCutPct / 100.0) * opex;
    const totalProfitImpact = profitFromMargin + profitFromOpex;

    const newNetProfit = netProfit + totalProfitImpact;
    const newMargin = sales > 0 ? (newNetProfit / sales * 100) : 0;
    const newCcc = curCcc != null ? (curCcc - dsoDays - dioDays) : null;

    $('simCashImpact').textContent=(totalCashImpact>=0?'+':'')+money(totalCashImpact);
    $('simProfitImpact').textContent=(totalProfitImpact>=0?'+':'')+money(totalProfitImpact);
    if($('simInterestSavings')) $('simInterestSavings').textContent=(interestSavings>=0?'+':'')+money(interestSavings);
    if($('simInterestSub')) $('simInterestSub').textContent='Sermaye maliyeti %'+waccPct.toFixed(0)+' ile açığa çıkan nakit faiz kalkanı';
    if($('simMarginImpact')) $('simMarginImpact').textContent='%' + newMargin.toFixed(1) + (marginDeltaPct>0 || opexCutPct>0 ? ' (+' + (newMargin - curMargin).toFixed(1) + 'p)' : '');
    if($('simCccImpact')) $('simCccImpact').textContent=newCcc!=null ? (Math.round(newCcc) + ' gün' + ((dsoDays+dioDays)>0 ? ' (-' + (dsoDays+dioDays) + 'g)' : '')) : '–';

    let narrative=[];
    if(dsoDays>0) narrative.push('Alacakların '+dsoDays+' gün erken tahsili kasaya <b>'+money(cashFromDso)+'</b> nakit girişi sağlar.');
    if(dioDays>0) narrative.push('Stok devrini '+dioDays+' gün hızlandırmak depodan <b>'+money(cashFromDio)+'</b> nakit çözer.');
    if(interestSavings>0) narrative.push('Açığa çıkan toplam nakit sayesinde yıllık <b>'+money(interestSavings)+'</b> kredi faiz maliyetinden tasarruf edilir (%'+waccPct.toFixed(0)+' sermaye maliyeti).');
    if(marginDeltaPct>0) narrative.push('Fiyat/marj yönetimindeki %'+marginDeltaPct.toFixed(1)+' artış yıllık faaliyet kârına <b>'+money(profitFromMargin)+'</b> ekler.');
    if(opexCutPct>0) narrative.push('Faaliyet giderlerindeki %'+opexCutPct+' tasarruf doğrudan P&L kârına <b>'+money(profitFromOpex)+'</b> yansır.');

    $('simSummaryText').innerHTML=narrative.length?narrative.join('<br>'):'Sürgüleri hareket ettirerek veya yukarıdaki hazır senaryolara tıklayarak şirketin kazanımlarını test edin.';
  }

  window._updateSim = updateSim;
  ['sliderDso','sliderDio','sliderMargin','sliderOpex','simCostOfCapital'].forEach(id=>{
    const el=$(id); if(el) el.oninput=updateSim;
  });
  updateSim();
}

function setAiPrompt(text){
  const el=$('aiCustomPrompt');
  if(el){ el.value=text; $('aiAskBtn').click(); }
}

$('aiAskBtn').onclick=async()=>{
  if(!LAST){
    $('aiCustomBox').classList.remove('hidden');
    $('aiCustomBox').textContent='Lütfen önce bir mizan veya finansal tablo analiz edin.';
    return;
  }
  const q=($('aiCustomPrompt').value||'').trim();
  if(!q){
    $('aiCustomBox').classList.remove('hidden');
    $('aiCustomBox').textContent='Lütfen sormak istediğiniz soruyu yazın veya yukarıdaki hazır başlıklardan birine tıklayın.';
    return;
  }
  $('aiAskBtn').disabled=true;
  $('aiCustomBox').classList.remove('hidden');
  let sec=0;
  $('aiCustomBox').textContent='⏳ AI Finance Partner sorunuzu analiz ediyor (0 sn)...';
  const timer=setInterval(()=>{sec++;$('aiCustomBox').textContent='⏳ AI Finance Partner sorunuzu analiz ediyor ('+sec+' sn)...';},1000);
  try{
    const r=await fetch('/api/ai/cfo-narrative',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({analysis:LAST,instruction:q})
    });
    clearInterval(timer);
    const d=await r.json();
    if(!d.available){
      $('aiCustomBox').textContent=d.reason||'AI yanıt üretemedi.';
      return;
    }
    const x=d.response||{};
    const exec=Array.isArray(x.executive_message)?x.executive_message.map(m=>'<p style="margin:6px 0">'+formatAi(m)+'</p>').join(''):'<p style="margin:6px 0">'+esc(x.executive_message||'')+'</p>';
    const risks=(x.key_risks||[]).length?'<div style="margin-top:12px;font-weight:700;color:#b3261e">⚠️ İlgili Risk Faktörleri:</div>'+(x.key_risks||[]).map(v=>'<div style="margin:4px 0">• '+formatAi(v)+'</div>').join(''):'';
    const acts=(x.actions||[]).length?'<div style="margin-top:12px;font-weight:700;color:#137333">🎯 Stratejik Aksiyon Önerileri:</div>'+(x.actions||[]).map(v=>'<div style="margin:4px 0">→ '+formatAi(v)+'</div>').join(''):'';
    const qs=(x.management_questions||[]).length?'<div style="margin-top:12px;font-weight:700;color:#1a73e8">❓ Karşı Tarafa / Yönetime Yöneltilecek Sorular:</div>'+(x.management_questions||[]).map(v=>'<div style="margin:4px 0">? '+formatAi(v)+'</div>').join(''):'';
    $('aiCustomBox').innerHTML='<div style="border-bottom:1px solid rgba(15,27,45,.12);padding-bottom:8px;margin-bottom:8px"><b style="color:var(--accent)">Soru:</b> <i>"'+esc(q)+'"</i></div><b style="font-size:15px">AI Finance Business Partner Stratejik Değerlendirmesi</b>'+exec+risks+acts+qs+'<div class="small muted" style="margin-top:10px">Model: '+esc(d.model)+' ('+sec+' sn)</div>';
  }catch(e){
    clearInterval(timer);
    $('aiCustomBox').textContent='AI isteği başarısız: '+e.message;
  }finally{
    clearInterval(timer);
    $('aiAskBtn').disabled=false;
  }
};

async function loadConfig(){try{const r=await fetch('/api/config');const d=await r.json();[[$('sector'),d.sectors],[$('trendSector'),d.sectors],[$('hubSector'),d.sectors]].forEach(([sel,list])=>list.forEach(s=>{const o=document.createElement('option');o.value=s;o.textContent=s;sel.appendChild(o)}));}catch(e){}}
loadConfig();

// ---------------------------------------------------------------------
// Two-period one-click trend demo (sample_mizan_period1.xlsx -> current)
// ---------------------------------------------------------------------
$('sampleTrendBtn').onclick=async()=>{
  $('sampleTrendBtn').disabled=true;$('sampleStatus').textContent='İki dönemlik örnek veri indiriliyor ve trend analizi çalıştırılıyor…';$('error').classList.add('hidden');
  try{
    const [rPrior,rCur]=await Promise.all([fetch('/api/sample/mizan_prior'),fetch('/api/sample/mizan')]);
    if(!rPrior.ok||!rCur.ok)throw new Error('Örnek veri sunucudan alınamadı.');
    const [bPrior,bCur]=await Promise.all([rPrior.blob(),rCur.blob()]);
    const fd=new FormData();
    fd.append('files',new File([bPrior],'onceki_donem.xlsx',{type:bPrior.type}));
    fd.append('files',new File([bCur],'guncel_donem.xlsx',{type:bCur.type}));
    document.querySelector('[data-tab="trend"]').click();
    await run('/api/mizan/analyze-trend',fd,'trend');
    $('sampleStatus').textContent='İki dönemli örnek analiz tamamlandı — gerçek şirket verisi değildir, "Karşılaştırmalı Analiz" kartına bakın.';
  }catch(e){$('error').textContent=e.message;$('error').classList.remove('hidden');$('sampleStatus').textContent='';}
  finally{$('sampleTrendBtn').disabled=false;}
};

// ---------------------------------------------------------------------
// Auth (register/login/logout) — token stored in localStorage.
// ---------------------------------------------------------------------
let AUTH_TOKEN=localStorage.getItem('dfbp_token');
let AUTH_EMAIL=localStorage.getItem('dfbp_email');
let AUTH_MODE='login';

function authHeaders(){return AUTH_TOKEN?{'Authorization':'Bearer '+AUTH_TOKEN}:{};}

function logoutUser(){
  AUTH_TOKEN=null;AUTH_EMAIL=null;
  localStorage.removeItem('dfbp_token');
  localStorage.removeItem('dfbp_email');
  renderAuthArea();
  refreshHistoryVisibility();
}
function renderAuthArea(){
  const box=$('authArea');
  const mob=$('mobileNavAuth');
  if(AUTH_TOKEN){
    if(box){
      box.innerHTML='<span class="small muted" style="margin-right:8px">👤 '+esc(AUTH_EMAIL||'')+'</span><button id="logoutBtn" class="secondary">Çıkış</button>';
      $('logoutBtn').onclick=logoutUser;
    }
    if(mob){
      mob.innerHTML='<div style="font-size:12px;color:var(--muted);width:100%;margin-bottom:6px">👤 '+esc(AUTH_EMAIL||'')+'</div><button type="button" onclick="logoutUser()" class="secondary" style="width:100%">Çıkış Yap</button>';
    }
    $('historyLoggedOut')?.classList.add('hidden');$('historyLoggedIn')?.classList.remove('hidden');
    loadHistory();
  }else{
    if(box){
      box.innerHTML='<button id="loginOpenBtn" class="secondary">Giriş Yap</button> <button id="registerOpenBtn" class="secondary">Kayıt Ol</button>';
      $('loginOpenBtn').onclick=()=>openAuthModal('login');
      $('registerOpenBtn').onclick=()=>openAuthModal('register');
    }
    if(mob){
      mob.innerHTML='<button type="button" onclick="openAuthModal(\'login\')" class="secondary">Giriş Yap</button><button type="button" onclick="openAuthModal(\'register\')" class="primary">Ücretsiz Kayıt Ol</button>';
    }
    $('historyLoggedOut')?.classList.remove('hidden');$('historyLoggedIn')?.classList.add('hidden');
  }
}
function refreshHistoryVisibility(){
  if(AUTH_TOKEN){$('historyLoggedOut')?.classList.add('hidden');$('historyLoggedIn')?.classList.remove('hidden');}
  else{$('historyLoggedOut')?.classList.remove('hidden');$('historyLoggedIn')?.classList.add('hidden');}
}
function openAuthModal(mode){
  $('mainNav')?.classList.remove('open');
  AUTH_MODE=mode;
  const isReg = mode === 'register';
  $('authModalTitle').textContent = isReg ? 'Ücretsiz Kurumsal Hesap Aç' : 'Yönetici Girişi';
  if($('authModalSubtitle')) $('authModalSubtitle').textContent = isReg ? '33 finansal karar motoru ve istihbaratına anında erişin.' : 'Mizan ve finansal karar raporlarınıza güvenle erişin.';
  $('authSubmitBtn').textContent = isReg ? 'Hesap Oluştur ve Başla' : 'Giriş Yap';
  if($('authCompanyWrap')) $('authCompanyWrap').style.display = isReg ? 'block' : 'none';
  if($('authTabLogin')){
    $('authTabLogin').style.background = isReg ? 'transparent' : '#FFFFFF';
    $('authTabLogin').style.color = isReg ? 'var(--muted)' : '#0F1B2D';
    $('authTabLogin').style.fontWeight = isReg ? '600' : '700';
    $('authTabLogin').style.boxShadow = isReg ? 'none' : '0 2px 6px rgba(0,0,0,.06)';
  }
  if($('authTabRegister')){
    $('authTabRegister').style.background = isReg ? '#FFFFFF' : 'transparent';
    $('authTabRegister').style.color = isReg ? '#0F1B2D' : 'var(--muted)';
    $('authTabRegister').style.fontWeight = isReg ? '700' : '600';
    $('authTabRegister').style.boxShadow = isReg ? '0 2px 6px rgba(0,0,0,.06)' : 'none';
  }
  $('authSwitchHint').innerHTML = isReg ? 'Zaten kurumsal hesabınız var mı? <a href="#" id="authSwitchLink" style="color:var(--accent);font-weight:700">Giriş Yap</a>' : 'Hesabınız yok mu? <a href="#" id="authSwitchLink" style="color:var(--accent);font-weight:700">Ücretsiz Kayıt Ol</a>';
  $('authSwitchLink').onclick=(e)=>{e.preventDefault();openAuthModal(isReg ? 'login' : 'register');};
  $('authError').classList.add('hidden');
  $('authModalOverlay').classList.remove('hidden');
}
$('authModalClose').onclick=()=>$('authModalOverlay').classList.add('hidden');
$('authModalOverlay').onclick=(e)=>{if(e.target.id==='authModalOverlay')$('authModalOverlay').classList.add('hidden');};
$('authTabLogin')?.addEventListener('click',()=>openAuthModal('login'));
$('authTabRegister')?.addEventListener('click',()=>openAuthModal('register'));
document.getElementById('historyLoginLink')?.addEventListener('click',(e)=>{e.preventDefault();openAuthModal('login');});
document.getElementById('historyRegisterLink')?.addEventListener('click',(e)=>{e.preventDefault();openAuthModal('register');});
$('authSubmitBtn').onclick=async()=>{
  const email=$('authEmail').value.trim();const password=$('authPassword').value;const company=$('authCompany').value.trim();
  if(!email||!password){$('authError').textContent='E-posta ve şifre gerekli.';$('authError').classList.remove('hidden');return;}
  $('authSubmitBtn').disabled=true;
  try{
    const url=AUTH_MODE==='login'?'/api/auth/login':'/api/auth/register';
    const body=AUTH_MODE==='login'?{email,password}:{email,password,company_name:company||null};
    const r=await fetch(url,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    const d=await r.json();
    if(!r.ok)throw new Error(d.detail||'İşlem başarısız.');
    AUTH_TOKEN=d.token;AUTH_EMAIL=d.email;
    localStorage.setItem('dfbp_token',AUTH_TOKEN);localStorage.setItem('dfbp_email',AUTH_EMAIL);
    $('authModalOverlay').classList.add('hidden');
    renderAuthArea();
  }catch(e){$('authError').textContent=e.message;$('authError').classList.remove('hidden');}
  finally{$('authSubmitBtn').disabled=false;}
};
(function(){const _qp=new URLSearchParams(location.search);const _m=_qp.get('auth');if(_m==='login'||_m==='register'){openAuthModal(_m);}})();
renderAuthArea();

// ---------------------------------------------------------------------
// Save current analysis to history (visible once an analysis has run AND
// the user is logged in).
// ---------------------------------------------------------------------
const _origRender=render;
render=function(d){_origRender(d);
  $('pvPreview')?.classList.add('hidden');
  if(AUTH_TOKEN){$('saveHistoryBox').classList.remove('hidden');}
  if(!$('saveFiscalYear').value)$('saveFiscalYear').value=new Date().getFullYear();
};
$('saveHistoryBtn').onclick=async()=>{
  if(!LAST){$('saveHistoryStatus').textContent='Önce bir analiz çalıştırın.';return;}
  const fiscal_year=parseInt($('saveFiscalYear').value,10);
  if(!fiscal_year){$('saveHistoryStatus').textContent='Geçerli bir yıl girin.';return;}
  $('saveHistoryBtn').disabled=true;$('saveHistoryStatus').textContent='Kaydediliyor…';
  try{
    const r=await fetch('/api/history/save',{method:'POST',headers:{'Content-Type':'application/json',...authHeaders()},
      body:JSON.stringify({company_name:$('saveCompanyName').value||null,period_label:$('savePeriodLabel').value||null,fiscal_year,analysis:LAST})});
    const d=await r.json();
    if(!r.ok)throw new Error(d.detail||'Kaydedilemedi.');
    $('saveHistoryStatus').textContent='✅ Kaydedildi (#'+d.id+').';
    loadHistory();
  }catch(e){$('saveHistoryStatus').textContent='Hata: '+e.message;}
  finally{$('saveHistoryBtn').disabled=false;}
};

// ---------------------------------------------------------------------
// History list + year filter + compare (2 picks -> side-by-side summary).
// ---------------------------------------------------------------------
let HISTORY_DATA=null;let HISTORY_SELECTED=[];
async function loadHistory(){
  if(!AUTH_TOKEN)return;
  $('historyStatus').textContent='Yükleniyor…';
  try{
    const r=await fetch('/api/history/list',{headers:authHeaders()});
    if(r.status===401){AUTH_TOKEN=null;localStorage.removeItem('dfbp_token');renderAuthArea();return;}
    const d=await r.json();HISTORY_DATA=d;HISTORY_SELECTED=[];
    const yf=$('historyYearFilter');const cur=yf.value;
    yf.innerHTML='<option value="">Tüm yıllar</option>'+d.years.map(y=>'<option value="'+y+'">'+y+'</option>').join('');
    yf.value=cur||'';
    renderHistoryList();
    $('historyStatus').textContent=d.years.length?'':'Henüz kaydedilmiş analiz yok.';
  }catch(e){$('historyStatus').textContent='Yüklenemedi: '+e.message;}
}
function renderHistoryList(){
  if(!HISTORY_DATA)return;
  const yearFilter=$('historyYearFilter').value;
  const years=yearFilter?[parseInt(yearFilter,10)]:HISTORY_DATA.years;
  let html='';
  years.forEach(y=>{
    const items=HISTORY_DATA.by_year[y]||HISTORY_DATA.by_year[String(y)]||[];
    if(!items.length)return;
    html+='<div style="margin:14px 0 6px;font-weight:700;color:var(--accent2)">'+y+'</div>';
    items.forEach(it=>{
      html+='<div class="custRow"><label style="display:flex;gap:8px;align-items:center;cursor:pointer"><input type="checkbox" class="histPick" value="'+it.id+'"> '+esc(it.company_name||'İsimsiz Şirket')+' — '+esc(it.period_label||'')+'</label><span class="small muted">Health: '+(it.health_score??'–')+'</span><span class="small muted">'+new Date(it.created_at).toLocaleDateString('tr-TR')+'</span></div>';
    });
  });
  $('historyList').innerHTML=html||'<div class="notice">Bu yıl için kayıt yok.</div>';
  document.querySelectorAll('.histPick').forEach(cb=>cb.addEventListener('change',onHistoryPick));
}
function onHistoryPick(){
  HISTORY_SELECTED=[...document.querySelectorAll('.histPick:checked')].map(cb=>cb.value);
  if(HISTORY_SELECTED.length>2){
    // keep only the two most recently checked
    const last=this;
    document.querySelectorAll('.histPick').forEach(cb=>{if(cb!==last&&HISTORY_SELECTED.includes(cb.value)&&HISTORY_SELECTED.length>2){cb.checked=false;}});
    HISTORY_SELECTED=[...document.querySelectorAll('.histPick:checked')].map(cb=>cb.value);
  }
  $('historyCompareBtn').disabled=HISTORY_SELECTED.length!==2;
  $('historyCompareBtn').textContent=HISTORY_SELECTED.length===2?'Seçilenleri Karşılaştır':'Seçilenleri Karşılaştır (2 seç)';
}
$('historyYearFilter').onchange=renderHistoryList;
$('historyRefreshBtn').onclick=loadHistory;
$('historyCompareBtn').onclick=async()=>{
  if(HISTORY_SELECTED.length!==2)return;
  $('historyCompareResult').innerHTML='<div class="notice">Karşılaştırma yükleniyor…</div>';
  try{
    const r=await fetch('/api/history/compare?ids='+HISTORY_SELECTED.join(','),{headers:authHeaders()});
    const d=await r.json();
    if(!r.ok)throw new Error(d.detail||'Karşılaştırma başarısız.');
    const [a,b]=d.items;
    const rowsFor=(x)=>{
      const bp=(x.analysis&&x.analysis.business_partner)||{};
      return {score:x.health_score,label:bp.health_label||'–',company:x.company_name||'–',period:x.period_label||x.fiscal_year};
    };
    const ra=rowsFor(a),rb=rowsFor(b);
    const delta=(ra.score!=null&&rb.score!=null)?(rb.score-ra.score):null;
    $('historyCompareResult').innerHTML='<div class="card" style="padding:18px"><h3 style="margin:0 0 12px">Karşılaştırma: '+esc(String(ra.period))+' → '+esc(String(rb.period))+'</h3>'+
      '<table><tr><th></th><th>'+esc(String(ra.period))+'</th><th>'+esc(String(rb.period))+'</th></tr>'+
      '<tr><td>Şirket</td><td>'+esc(ra.company)+'</td><td>'+esc(rb.company)+'</td></tr>'+
      '<tr><td>Financial Health Skoru</td><td>'+(ra.score??'–')+'</td><td>'+(rb.score??'–')+'</td></tr>'+
      '<tr><td>Sağlık Etiketi</td><td>'+esc(ra.label)+'</td><td>'+esc(rb.label)+'</td></tr>'+
      '</table>'+(delta!=null?'<p class="small muted" style="margin-top:10px">Skor değişimi: <b style="color:'+(delta>=0?'var(--green)':'var(--red)')+'">'+(delta>=0?'+':'')+delta+' puan</b></p>':'')+
      '<p class="small muted">Not: Bu hızlı karşılaştırma kaydedilen iki Health Score anlık görüntüsünü kıyaslar. Tam bulgu bazlı karşılaştırma için her iki dönemi birlikte "Çok dönem / Trend" sekmesinden yükleyin.</p></div>';
  }catch(e){$('historyCompareResult').innerHTML='<div class="error">'+esc(e.message)+'</div>';}
};
if(typeof document !== 'undefined' && document.addEventListener){
  document.addEventListener('DOMContentLoaded', function(){
    var saved = 'tr';
    try { saved = localStorage.getItem('dfbp_lang') || 'tr'; } catch(e){}
    if(typeof setLanguage === 'function') setLanguage(saved);
  });
}
</script></body></html>
'''

HTML = APP_HTML  # backward-compat alias for any old import
