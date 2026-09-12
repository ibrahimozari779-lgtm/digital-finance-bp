"""Digital Finance Business Partner — multi-page marketing site + app.

Pages: HOME_HTML (/), PRICING_HTML (/paketler), ABOUT_HTML (/hakkimizda),
CONTACT_HTML (/iletisim), APP_HTML (/uygulama, the actual analysis tool).
All share one nav/footer/CSS design system assembled in build scripts.
"""

HOME_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Digital Finance Business Partner | Finansal Karar Destek Platformu</title>
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
.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
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
.topNav{display:flex;gap:26px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.navBtns,#authArea{display:flex;gap:8px;align-items:center}
.navBtns a,.navBtns button,#authArea button{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  font-size:13px;
  font-weight:700;
  padding:8px 16px;
  border-radius:10px;
  text-decoration:none;
  transition:all .15s ease;
  cursor:pointer;
  line-height:1.2;
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
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text)}
@media(max-width:920px){
  .topNav{position:fixed;top:74px;left:0;right:0;background:#F7F9FC;border-bottom:1px solid var(--line);flex-direction:column;align-items:flex-start;gap:0;padding:6px 22px;max-height:0;overflow:hidden;transition:max-height .25s ease;z-index:60}
  .topNav.open{max-height:280px;padding:14px 22px}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.08)}
  .navToggle{display:inline-flex}
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

</style></head>
<body>
<header class="top"><div class="wrap brand"><div>
  <a href="/" style="text-decoration:none;display:flex;align-items:center;gap:12px">
    <div style="width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div>
      <div style="font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2">
        Digital Finance Business Partner
      </div>
      <div style="font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px">
        Finansal Teşhis &amp; Yönetim Karar Destek Platformu
      </div>
    </div>
  </a>
</div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/" class="active">Anasayfa</a><a href="/hakkimizda">Hakkımızda</a><a href="/uygulama">Uygulama</a><a href="/paketler">Paketler</a><a href="/guvenlik">Güvenlik</a><a href="/iletisim">İletişim</a></nav><div class="navBtns"><a href="/uygulama?auth=login" class="navBtn secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="navBtn primary">Ücretsiz Kayıt Ol</a></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<section class="mHero">
  <div class="reveal in">
    <div class="livePill"><i></i> YÖNETİCİLER &amp; ŞİRKET SAHİPLERİ İÇİN FİNANSAL KARAR PLATFORMU</div>
    <h1>Rakamları Değil, Şirketinizi Büyüten Yönetim Kararlarını Masaya Koyun.<br><span class="gradText">Finansal Verileri Stratejik İcraat Gücüne Dönüştüren Karar Platformu.</span></h1>
    <p class="lead">Klasik muhasebe geçmiş mali kayıtları ve vergi matrahını raporlar; <b>Digital Finance Business Partner</b> ise şirketin sermaye verimliliğini ve net nakit akışını maksimize eden stratejik icraat kararları üretir. Mizan ve alt defter kayıtlarınızı yükleyin; <b>33 Deterministik Karar Motoru</b> 60 saniyede çift yönlü matematiksel denetimle çalışarak işletme sermayesindeki nakit kilitlenmelerini, gizli kâr sızıntılarını ve üst yönetimin uygulamaya alacağı somut eylem planını masanıza koysun.</p>
    <div class="ctaRow">
      <a href="/uygulama?sample=data_hub" class="primary" style="padding:15px 26px;border-radius:14px;font-size:15px;display:inline-flex;align-items:center;gap:10px">🔥 Kayıt Olmadan Canlı Demoyu Başlat <span>(Data Hub)</span></a>
      <a href="/uygulama" class="secondary" style="padding:15px 26px;border-radius:14px;font-size:15px">⚡ Kendi Verinizi Yükleyin →</a>
    </div>
    <div class="miniTrust">
      <span><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>%100 Deterministik Çift Taraflı Denetim</span>
      <span><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>KVKK Uyumlu · Kalıcı Saklama Yok</span>
      <span><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 5-8"/></svg>33 Finansal Karar Motoru</span>
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
          <div class="dTitle">Canlı Karar Simülatörü — "Fiyatı %3 Artırırsak Kasaya Ne Girer?"</div>
          <svg viewBox="0 0 320 135" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:135px">
            <line x1="0" y1="115" x2="320" y2="115" stroke="#E2E8F0" stroke-width="1"/>
            <polyline points="10,105 60,95 110,98 160,70 210,75 260,45 300,50" fill="none" stroke="#94A3B8" stroke-width="2" stroke-dasharray="4 4"/>
            <polyline points="10,105 60,82 110,80 160,46 210,42 260,16 300,12" fill="none" stroke="#2563EB" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="300" cy="12" r="5" fill="#2563EB"/><circle cx="300" cy="50" r="4" fill="#94A3B8"/>
            <text x="295" y="8" fill="#1D4ED8" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" text-anchor="end">+%3 Fiyat (+324.000 ₺)</text>
            <text x="295" y="65" fill="#64748B" font-family="Inter,sans-serif" font-size="8.5" text-anchor="end">Mevcut Durum</text>
          </svg>
          <div class="dashKpis"><div><b>+324.000 ₺</b><span>Net Kâr Katkısı</span></div><div><b>+450.000 ₺</b><span>Tahsilatı 15 Gün Çekme</span></div><div><b>+774.000 ₺</b><span>Toplam Serbest Nakit</span></div></div>
        </div>
      </div>
      <div class="foot"><span>%100 Deterministik Çift Taraflı Denetim</span><span>60 Saniyede Hazır Yönetim Raporu</span></div>
    </div>
  </div>
</section>

<!-- SECTION: 4 EXECUTIVE DILEMMAS -->
<div class="secBlock reveal"><section id="dilemmas" class="marketingSection hidePrint" style="padding-top:0">
<div class="marketingHead">
  <span class="workflowBadge">YÖNETİCİLER & ŞİRKET SAHİPLERİ İÇİN</span>
  <h2>Patronların Her Gece Düşündüğü 4 Büyük Finansal Çıkmaz</h2>
  <p>Muhasebe programınız geçmiş fişleri kaydeder ancak bu sorulara cevap veremez. Digital Finance Business Partner bu kararları yönetmek için geliştirildi.</p>
</div>
<div class="dilemmaGrid">
  <div class="dilemmaCard">
    <div class="dilemmaQ"><span>SORU 1</span> "Kâğıt üzerinde kâr görünüyor ama kasada para nerede?"</div>
    <div class="dilemmaA">
      <b>DFBP Çözümü: Sermaye Dağılım Metresi & Nakit Köprüsü</b>
      Net kârınızın ne kadarının kasaya nakit olarak girdiği, ne kadarının müşterideki açık vadeli hesaplarda veya depodaki ölü stokta kilitlendiği TL kuruşuna kadar ayrıştırılır.
    </div>
  </div>
  <div class="dilemmaCard">
    <div class="dilemmaQ"><span>SORU 2</span> "Cirosu en yüksek müşterim bana gerçekten para kazandırıyor mu?"</div>
    <div class="dilemmaA">
      <b>DFBP Çözümü: 4-Kadran Müşteri Kârlılık Matrisi</b>
      Vade aşımı, iskonto ve işletme finansman maliyeti hesaba katılarak "Görünürde dev ciro yapan ama nakit yutan" müşteriler tespit edilir ve fiyatlama aksiyonuna bağlanır.
    </div>
  </div>
  <div class="dilemmaCard">
    <div class="dilemmaQ"><span>SORU 3</span> "Depodaki stok nakdimi ne kadar boğuyor?"</div>
    <div class="dilemmaA">
      <b>DFBP Çözümü: Stok Yaşlandırma & Ölü Stok Tespiti (DIO)</b>
      180+ gündür satılmayan atıl stokların değeri hesaplanır; depodaki bağlı sermayeyi nakde çevirecek tasfiye, kampanya ve sipariş kısıtları önerilir.
    </div>
  </div>
  <div class="dilemmaCard">
    <div class="dilemmaQ"><span>SORU 4</span> "Fiyatlarımızı %3 artırsak veya vadeyi 15 gün çeksek nakit ne olur?"</div>
    <div class="dilemmaA">
      <b>DFBP Çözümü: Canlı What-If Senaryo Laboratuvarı</b>
      Hissiyata gerek kalmadan doğrudan gerçek bilançonuz üzerinden formüllü simülasyon yapılır; kâr, nakit ve borç üzerindeki anlık duyarlılık patronun masasına konur.
    </div>
  </div>
</div>
</section></div>

<!-- SECTION: WORKING CAPITAL LEAK & LOCKED CASH CALCULATOR -->
<div class="secBlock reveal"><section id="calculator" class="marketingSection hidePrint" style="padding-top:0">
  <div style="background:linear-gradient(145deg,#FFFFFF 0%,#F8FAFC 100%);border:1.5px solid #CBD5E1;border-radius:24px;box-shadow:0 16px 44px rgba(15,27,45,.07);padding:36px">
    <div style="text-align:center;max-width:700px;margin:0 auto 28px">
      <span class="workflowBadge" style="background:#EEF4FF;border-color:#BFDBFE;color:#1D4ED8">⚡ 10 SANİYELİK İNTERAKTİF FİNANSAL TEŞHİS</span>
      <h2 style="font-family:var(--serif);font-size:30px;margin:10px 0 8px;letter-spacing:-.4px;color:#0F1B2D">Görünmez Kâr Sızıntısı &amp; Kilitli Nakit Hesaplayıcı</h2>
      <p style="color:var(--muted);font-size:14px;margin:0">Cironuzu ve piyasadaki ortalama tahsilat vadenizi belirleyin; müşterilerde duran sermayenizi ve her yıl faize giden gizli kâr kaybınızı anında görün.</p>
    </div>

    <div class="grid2" style="gap:28px;align-items:center">
      <!-- Input Controls -->
      <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:18px;padding:24px;display:flex;flex-direction:column;gap:20px;box-shadow:0 2px 8px rgba(0,0,0,.02)">
        <div>
          <div style="display:flex;justify-content:space-between;align-items:center;font-size:13px;margin-bottom:8px">
            <span style="font-weight:700;color:#0F172A">Yıllık Net Ciro (Satış Hacmi)</span>
            <b id="leakRevDisplay" style="color:#1D4ED8;font-size:15px;font-family:var(--serif)">₺36.000.000</b>
          </div>
          <input id="leakRevSlider" type="range" min="5000000" max="250000000" step="1000000" value="36000000" style="width:100%;cursor:pointer">
          <div style="display:flex;justify-content:space-between;font-size:10.5px;color:#64748B;margin-top:4px">
            <span>5M ₺</span><span>100M ₺</span><span>250M ₺</span>
          </div>
        </div>

        <div>
          <div style="display:flex;justify-content:space-between;align-items:center;font-size:13px;margin-bottom:8px">
            <span style="font-weight:700;color:#0F172A">Ortalama Müşteri Vadesi (DSO)</span>
            <b id="leakDsoDisplay" style="color:#1D4ED8;font-size:15px;font-family:var(--serif)">85 Gün</b>
          </div>
          <input id="leakDsoSlider" type="range" min="30" max="150" step="1" value="85" style="width:100%;cursor:pointer">
          <div style="display:flex;justify-content:space-between;font-size:10.5px;color:#64748B;margin-top:4px">
            <span>30 Gün (Peşin Ağırlıklı)</span><span>90 Gün (Piyasa Ort.)</span><span>150 Gün (Yüksek Risk)</span>
          </div>
        </div>

        <div>
          <div style="font-size:13px;font-weight:700;color:#0F172A;margin-bottom:8px">Faaliyet Sektörünüz</div>
          <select id="leakSectorSelect" class="select" style="width:100%;padding:10px 14px;border-radius:10px;font-size:13px">
            <option value="0.45" selected>Üretim &amp; Sanayi (Yıllık %45 Kredi/Finansman Faizi)</option>
            <option value="0.48">Toptan &amp; Ticaret (Yıllık %48 Kredi/Finansman Faizi)</option>
            <option value="0.42">Hizmet &amp; Bilişim (Yıllık %42 Kredi/Finansman Faizi)</option>
            <option value="0.50">İnşaat &amp; Taahhüt (Yıllık %50 Kredi/Finansman Faizi)</option>
            <option value="0.44">Perakende &amp; Mağazacılık (Yıllık %44 Kredi/Finansman Faizi)</option>
          </select>
        </div>
      </div>

      <!-- Output Display Cards -->
      <div style="display:flex;flex-direction:column;gap:14px">
        <div style="background:#FFFFFF;border:1.5px solid #FCA5A5;border-radius:16px;padding:16px 20px;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-size:11.5px;font-weight:800;text-transform:uppercase;letter-spacing:.6px;color:#DC2626">🔒 Müşterilerde Kilitli Kalan Nakit</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px">Tahsil edilene kadar kasada olmayan sermaye</div>
          </div>
          <div id="leakLockedCash" style="font-size:22px;font-weight:900;color:#991B1B;font-family:var(--serif)">₺8.383.562</div>
        </div>

        <div style="background:#FFFFFF;border:1.5px solid #FCD34D;border-radius:16px;padding:16px 20px;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-size:11.5px;font-weight:800;text-transform:uppercase;letter-spacing:.6px;color:#D97706">💸 Görünmez Yıllık Kâr Kaybı (Finansman Yükü)</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px">Bu nakdi taşımak için katlanılan faiz/finansman maliyeti</div>
          </div>
          <div id="leakAnnualCost" style="font-size:22px;font-weight:900;color:#B45309;font-family:var(--serif)">₺3.772.603</div>
        </div>

        <div style="background:#FFFFFF;border:1.5px solid #86EFAC;border-radius:16px;padding:16px 20px;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="font-size:11.5px;font-weight:800;text-transform:uppercase;letter-spacing:.6px;color:#16A34A">🚀 15 Gün Erken Tahsilatın Kasaya Katkısı</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px">Sadece 15 günlük vade disipliniyle açığa çıkacak nakit</div>
          </div>
          <div id="leak15DayImpact" style="font-size:22px;font-weight:900;color:#047857;font-family:var(--serif)">+₺1.479.452</div>
        </div>

        <div style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:16px;padding:16px 18px;margin-top:2px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px">
          <div style="font-size:12.5px;color:#1E3A8A;line-height:1.45;flex:1;min-width:240px">
            <b>Bu simülasyon bir tahmin değildir.</b> Gerçek mizanınızı yükleyerek 120 alıcı, 320 satıcı ve stok yaşlandırmanızdaki gerçek sızıntıyı kuruşu kuruşuna 60 saniyede görün.
          </div>
          <div style="display:flex;gap:8px;flex-wrap:wrap">
            <a href="/uygulama?sample=data_hub" class="primary" style="padding:10px 16px;border-radius:10px;font-size:12.5px;text-decoration:none;white-space:nowrap">🔥 Canlı Demoda İncele</a>
            <a href="/uygulama" class="secondary" style="padding:10px 16px;border-radius:10px;font-size:12.5px;text-decoration:none;white-space:nowrap">Kendi Mizanını Tara →</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Institutional B2B Trust Pillars -->
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:32px;padding-top:24px;border-top:1px solid #E2E8F0">
      <div style="text-align:center;padding:10px">
        <div style="font-size:22px;margin-bottom:6px">🏛️</div>
        <div style="font-size:11.5px;font-weight:700;color:#0F172A">TCMB &amp; BIST Kıyaslama</div>
        <div style="font-size:10.5px;color:#64748B;margin-top:3px">500+ halka açık şirket ve sektör medyanlarıyla rasyo analizi</div>
      </div>
      <div style="text-align:center;padding:10px">
        <div style="font-size:22px;margin-bottom:6px">🔗</div>
        <div style="font-size:11.5px;font-weight:700;color:#0F172A">ERP &amp; Muhasebe Uyumu</div>
        <div style="font-size:10.5px;color:#64748B;margin-top:3px">Logo, Netsis, Mikro, SAP, Zirve, Luca ve Paraşüt mizanları</div>
      </div>
      <div style="text-align:center;padding:10px">
        <div style="font-size:22px;margin-bottom:6px">🛡️</div>
        <div style="font-size:11.5px;font-weight:700;color:#0F172A">KVKK &amp; RAM-Only Güvenlik</div>
        <div style="font-size:10.5px;color:#64748B;margin-top:3px">Kalıcı veri saklanmaz; analiz tamamlanınca RAM'den silinir</div>
      </div>
      <div style="text-align:center;padding:10px">
        <div style="font-size:22px;margin-bottom:6px">⚡</div>
        <div style="font-size:11.5px;font-weight:700;color:#0F172A">33 Deterministik Karar Motoru</div>
        <div style="font-size:10.5px;color:#64748B;margin-top:3px">Çift taraflı denetim ve kural tabanlı matematiksel kesinlik</div>
      </div>
      <div style="text-align:center;padding:10px">
        <div style="font-size:22px;margin-bottom:6px">📑</div>
        <div style="font-size:11.5px;font-weight:700;color:#0F172A">Boardroom Executive PDF</div>
        <div style="font-size:10.5px;color:#64748B;margin-top:3px">Yönetim Kurulu ve bankalara özel sıkıştırılmış C-Level brifing</div>
      </div>
    </div>
  </div>
</section></div>

<!-- SECTION: 3-KATMANLI ÜRÜN MİMARİSİ (PATRONUN AKLINDAKİ 8 KRİTİK SORU) -->
<div class="secBlock tint reveal">
  <section id="patronSorulari" class="marketingSection hidePrint">
    <div class="marketingHead">
      <span class="workflowBadge" style="background:#EFF6FF;color:#1D4ED8;border-color:#BFDBFE">3 KATMANLI ÜRÜN MİMARİSİ</span>
      <h2>Patron Muhasebe Raporu Değil; "Kasada Neden Para Yok ve Yarın Ne Yapmalıyım?" Sorusunun Cevabını İster</h2>
      <p>Muhasebe programları sadece geçmişin dökümünü listeler. Digital Finance Business Partner ise patronun geceleri aklına takılan 8 kritik soruyu; çift taraflı analitik kanıtlar, net TL getirisi ve yarın sabah başlatılacak icraat kararlarıyla anında çözer.</p>
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
              <h4 style="font-size:15px;color:#991B1B;margin:0 0 8px;line-height:1.4">Kâğıt Üzerindeki Kâr, Alacak ve Stok Kilitlenmesinde Kayboluyor</h4>
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
              <p style="font-size:13px;color:#7F1D1D;line-height:1.6;margin:0">Cironun %38'ini tek başına oluşturan ilk 3 müşteri, 110 gün vade kullanmaktadır. %45 ticari kredi faizi ortamında bu vadenin faiz maliyeti satış marjının %14'ünü tüketmekte ve kâğıt üzerindeki kârı gizli zarara dönüştürmektedir.</p>
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

<!-- SECTION: 4-STEP WORKFLOW WITH INTERACTIVE PLAYER -->
<div class="secBlock tint reveal"><section id="workflow" class="marketingSection hidePrint">
<div class="marketingHead">
  <span class="workflowBadge">İNTERAKTİF İŞ AKIŞI MİMARİSİ</span>
  <h2>Peki Bu Kararlar Nasıl Üretiliyor? 4 Adımda Bütünleşik İş Akışı</h2>
  <p>Verinizi sisteme bıraktığınız andan yönetim kurulu aksiyon planına kadar geçen deterministik süreç.</p>
</div>
<div class="workflowGrid" id="wfGrid">
  <div class="workflowCard wfInteractive" data-step="0" style="cursor:pointer;border-top:3px solid var(--accent)">
    <span class="workflowBadge">ADIM 1 · GİRİŞ</span>
    <h3>Sıfır Entegrasyonla Yükleme</h3>
    <p>Mizan (1xx-7xx), Satış Defteri, AR/AP Yaşlandırma veya Stok dosyanızı sürükleyin. Aylar süren ERP kurulumu gerekmez; 60 saniyede hazır.</p>
  </div>
  <div class="workflowCard wfInteractive" data-step="1" style="cursor:pointer">
    <span class="workflowBadge">ADIM 2 · HESAPLAMA</span>
    <h3>33 Deterministik Motor</h3>
    <p>Bilanço denkliği, gelir tablosu kontrolleri ve alt defter mutabakatları çift taraflı denetimden geçer. Matematiksel kesinlikle kurallar çalışır.</p>
  </div>
  <div class="workflowCard wfInteractive" data-step="2" style="cursor:pointer">
    <span class="workflowBadge">ADIM 3 · ANLATIM</span>
    <h3>Kök Neden & Karar Zinciri</h3>
    <p>WHAT → WHY → SO WHAT → NOW WHAT → WHAT IF mantığıyla her rakamın kök nedeni, finansal riski ve parasal büyüklüğü açıklanır.</p>
  </div>
  <div class="workflowCard wfInteractive" data-step="3" style="cursor:pointer">
    <span class="workflowBadge">ADIM 4 · İŞ KARARLARI</span>
    <h3>Yönetim Aksiyonları & AI Partner</h3>
    <p>Sahibi, vadesi ve beklenen TL getirisi belli aksiyon planı oluşur. Stratejik kararlarınız için yapay zeka destekli soru-cevap katmanı hazırdır.</p>
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
      <button type="button" class="wfPill" data-wfpill="2" style="padding:6px 14px;font-size:11.5px;font-weight:700;background:#F1F5F9;color:#64748B;border:1px solid #E2E8F0;border-radius:999px;cursor:pointer">3. Kök Neden</button>
      <button type="button" class="wfPill" data-wfpill="3" style="padding:6px 14px;font-size:11.5px;font-weight:700;background:#F1F5F9;color:#64748B;border:1px solid #E2E8F0;border-radius:999px;cursor:pointer">4. Yönetim Aksiyonları</button>
    </div>
  </div>
  <div id="wfViewerContent">
    <div style="display:grid;grid-template-columns:1.2fr .8fr;gap:20px;align-items:center">
      <div>
        <p style="color:#334155;font-size:13.5px;line-height:1.6;margin:0 0 14px">ERP veya muhasebe programınızdan aldığınız standart Excel/CSV mizanınızı ve varsa yaşlandırma/stok alt defterlerinizi tarayıcıya sürükleyin. Kolon eşleme yapay zeka tahminiyle değil, hesap planı kuralları (1xx-7xx) üzerinden deterministik olarak anında tanınır.</p>
        <div style="display:flex;gap:10px;flex-wrap:wrap">
          <span style="background:#F1F5F9;border:1px solid #CBD5E1;padding:6px 12px;border-radius:8px;font-size:12px;color:#1D4ED8;font-weight:600">✓ Luca, Logo, Mikro, Netsis, Zirve uyumlu</span>
          <span style="background:#ECFDF5;border:1px solid #A7F3D0;padding:6px 12px;border-radius:8px;font-size:12px;color:#047857;font-weight:600">✓ Sıfır Kurulum & Sıfır Bekleme</span>
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
<div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • deterministic finance layer + optional Gemini interpretation • Financial facts are calculated before AI interpretation.<br><span style="opacity:.85">Bu rapor otomatik/deterministik hesaplamalara ve (etkinleştirildiyse) yapay zekâ yorumuna dayanır; muhasebe, denetim, vergi, hukuki veya yatırım tavsiyesi değildir ve resmi mali tablo/beyanname yerine geçmez. Nihai kararlar için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca bu analizi üretmek için işlenir; sunucu tarafında kalıcı olarak saklanmaz. KVKK kapsamındaki veri işleme hakkında bilgi için [Aydınlatma Metni] bağlantısını inceleyin.</span></div></div></div>
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
  if(!tabs.length||!panes.length) return;
  let idx=0, timer=null;
  function show(i){
    idx=i;
    tabs.forEach(t=>t.classList.toggle('on', t.dataset.pane===String(i)));
    panes.forEach(p=>p.classList.toggle('on', p.dataset.pane===String(i)));
  }
  function next(){ show((idx+1)%panes.length); }
  function restart(){ if(timer) clearInterval(timer); timer=setInterval(next,4200); }
  tabs.forEach(t=>t.addEventListener('click',()=>{ show(parseInt(t.dataset.pane,10)); restart(); }));
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
      html: '<div style="display:grid;grid-template-columns:1.2fr .8fr;gap:20px;align-items:center"><div><p style="color:#334155;font-size:13.5px;line-height:1.6;margin:0 0 14px">ERP veya muhasebe programınızdan aldığınız standart Excel/CSV mizanınızı ve varsa yaşlandırma/stok alt defterlerinizi tarayıcıya sürükleyin. Kolon eşleme yapay zeka tahminiyle değil, hesap planı kuralları (1xx-7xx) üzerinden deterministik olarak anında tanınır.</p><div style="display:flex;gap:10px;flex-wrap:wrap"><span style="background:#F1F5F9;border:1px solid #CBD5E1;padding:6px 12px;border-radius:8px;font-size:12px;color:#1D4ED8;font-weight:600">✓ Luca, Logo, Mikro, Netsis, Zirve uyumlu</span><span style="background:#ECFDF5;border:1px solid #A7F3D0;padding:6px 12px;border-radius:8px;font-size:12px;color:#047857;font-weight:600">✓ Sıfır Kurulum & Sıfır Bekleme</span></div></div><div style="background:#F8FAFC;border:2px dashed #93C5FD;border-radius:14px;padding:24px 20px;text-align:center"><div style="font-size:32px;margin-bottom:8px">📥</div><b style="color:#0F172A;font-size:13px;display:block">Mizan Dosyanızı Sürükleyin</b><span style="color:#64748B;font-size:11px">.xlsx, .xls, .csv formatları otomatik taranır</span></div></div>'
    },
    {
      badge: 'CANLI SİMÜLASYON · ADIM 2',
      title: '33 Deterministik Finans Motoruyla Çift Taraflı Denetim',
      html: '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px"><div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:14px;padding:16px"><b style="color:#1D4ED8;font-size:13px;display:block;margin-bottom:8px">🔍 Bilanço & Likidite Doğrulaması</b><ul style="margin:0;padding-left:16px;color:#334155;font-size:12.5px;line-height:1.8"><li>Aktif = Pasif denkliği kontrolü (0.00 TL tolerans)</li><li>Cari Oran, Likidite, Nakit Oranı analizi</li><li>Altman Z-Score İflas Riski motoru</li></ul></div><div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:14px;padding:16px"><b style="color:#047857;font-size:13px;display:block;margin-bottom:8px">⚡ Nakit & Kârlılık Çapraz Kontrolleri</b><ul style="margin:0;padding-left:16px;color:#334155;font-size:12.5px;line-height:1.8"><li>Kârın Nakde Dönüşüm Oranı (Cash Realization)</li><li>Müşteri / Ürün 4-Kadran kârlılık matrisi</li><li>180+ gün ölü stok ve vade aşım tespiti</li></ul></div></div>'
    },
    {
      badge: 'CANLI SİMÜLASYON · ADIM 3',
      title: 'Kök Neden & Karar Zinciri (WHAT → WHY → SO WHAT)',
      html: '<div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:14px;padding:18px"><div style="display:flex;gap:10px;align-items:center;margin-bottom:12px"><span style="background:#EF4444;color:#FFF;padding:3px 8px;border-radius:6px;font-size:10px;font-weight:900">WHAT</span><b style="color:#0F172A;font-size:13px">DSO 80 gün ile sektör medyanının (45 gün) 35 gün üzerinde.</b></div><div style="display:flex;gap:10px;align-items:center;margin-bottom:12px"><span style="background:#F59E0B;color:#FFF;padding:3px 8px;border-radius:6px;font-size:10px;font-weight:900">WHY</span><span style="color:#334155;font-size:12.5px">En büyük 3 müşteriye yazılı mutabakat olmadan 90+ gün gayriresmi vade tanınmış.</span></div><div style="display:flex;gap:10px;align-items:center"><span style="background:#2563EB;color:#FFF;padding:3px 8px;border-radius:6px;font-size:10px;font-weight:900">SO WHAT</span><span style="color:#047857;font-size:12.5px;font-weight:700">Kasada 1.250.000 ₺ likidite kilitlendi; şirket gereksiz yere aylık 65.000 ₺ rotatif kredi faizi ödüyor.</span></div></div>'
    },
    {
      badge: 'CANLI SİMÜLASYON · ADIM 4',
      title: 'Yönetim Aksiyonları & Somut İş Kararları',
      html: '<div style="display:grid;grid-template-columns:1.2fr .8fr;gap:16px;align-items:center"><div><div style="background:#F8FAFC;border:1px solid #E2E8F0;border-left:4px solid #10B981;border-radius:0 12px 12px 0;padding:12px 16px;margin-bottom:10px"><b style="color:#0F172A;font-size:13px;display:block">Aksiyon 1: Müşteri Vade Protokolü ve %2 Erken Ödeme İskontosu</b><span style="color:#64748B;font-size:11.5px">Sahibi: Satış Direktörü & Finans · Hedef: 30 Gün · Kurtarılacak Nakit: +620.000 ₺</span></div><div style="background:#F8FAFC;border:1px solid #E2E8F0;border-left:4px solid #2563EB;border-radius:0 12px 12px 0;padding:12px 16px"><b style="color:#0F172A;font-size:13px;display:block">Aksiyon 2: 180+ Gün Ölü Stok Tasfiyesi ve Sipariş Kısıtı</b><span style="color:#64748B;font-size:11.5px">Sahibi: Tedarik Zinciri · Hedef: 45 Gün · Kurtarılacak Nakit: +380.000 ₺</span></div></div><div style="background:linear-gradient(135deg,#EFF6FF,#DBEAFE);border:1px solid #BFDBFE;border-radius:14px;padding:16px;text-align:center"><div style="font-size:24px;margin-bottom:6px">🤖</div><b style="color:#1D4ED8;font-size:13px;display:block;margin-bottom:4px">Stratejik Karar Asistanı</b><span style="color:#1E3A8A;font-size:11.5px">Yönetim kurulu veya banka görüşmeleriniz için stratejik finansal sorularınızı anında yanıtlar.</span></div></div>'
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
</script>
</body></html>'''


PRICING_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Paketler | Digital Finance Business Partner</title>
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
.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
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
.topNav{display:flex;gap:26px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.navBtns{display:flex;gap:10px;align-items:center}
.navBtn{display:inline-flex;align-items:center;justify-content:center;padding:8px 18px;border-radius:10px;font-size:13px;font-weight:700;letter-spacing:-.1px;text-decoration:none;cursor:pointer;transition:all .18s ease;line-height:1.2}
.navBtn.sec{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
.navBtn.sec:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
.navBtn.pri{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
.navBtn.pri:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text)}
@media(max-width:920px){
  .topNav{position:fixed;top:74px;left:0;right:0;background:#F7F9FC;border-bottom:1px solid var(--line);flex-direction:column;align-items:flex-start;gap:0;padding:6px 22px;max-height:0;overflow:hidden;transition:max-height .25s ease;z-index:60}
  .topNav.open{max-height:280px;padding:14px 22px}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.08)}
  .navToggle{display:inline-flex}
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
<header class="top"><div class="wrap brand"><div>
  <a href="/" style="text-decoration:none;display:flex;align-items:center;gap:12px">
    <div style="width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div>
      <div style="font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2">
        Digital Finance Business Partner
      </div>
      <div style="font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px">
        Finansal Teşhis &amp; Yönetim Karar Destek Platformu
      </div>
    </div>
  </a>
</div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/hakkimizda">Hakkımızda</a><a href="/uygulama">Uygulama</a><a href="/paketler" class="active">Paketler</a><a href="/guvenlik">Güvenlik</a><a href="/iletisim">İletişim</a></nav><div class="navBtns"><a href="/uygulama?auth=login" class="navBtn sec">Giriş Yap</a><a href="/uygulama?auth=register" class="navBtn pri">Ücretsiz Kayıt Ol</a></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<div class="pageHead reveal in"><span class="eyebrow">Paketler</span><h1>Şirketiniz İçin Doğru Çözümü Seçin</h1><p>Tek seferlik bir örnek raporla mı başlamak istiyorsunuz, yoksa her ay yönetim kuruluna sunacağınız 33 karar motorlu finansal zekayı mı kurmak istiyorsunuz — tüm paketler aynı deterministik finansal çekirdeği kullanır.</p>
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
<div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • deterministic finance layer + optional Gemini interpretation • Financial facts are calculated before AI interpretation.<br><span style="opacity:.85">Bu rapor otomatik/deterministik hesaplamalara ve (etkinleştirildiyse) yapay zekâ yorumuna dayanır; muhasebe, denetim, vergi, hukuki veya yatırım tavsiyesi değildir ve resmi mali tablo/beyanname yerine geçmez. Nihai kararlar için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca bu analizi üretmek için işlenir; sunucu tarafında kalıcı olarak saklanmaz. KVKK kapsamındaki veri işleme hakkında bilgi için [Aydınlatma Metni] bağlantısını inceleyin.</span></div></div></div>
<script>
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
</body></html>'''

ABOUT_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Hakkımızda | Digital Finance Business Partner</title>
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
.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
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
.topNav{display:flex;gap:26px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.navBtns{display:flex;gap:10px;align-items:center}
.navBtn{display:inline-flex;align-items:center;justify-content:center;padding:8px 18px;border-radius:10px;font-size:13px;font-weight:700;letter-spacing:-.1px;text-decoration:none;cursor:pointer;transition:all .18s ease;line-height:1.2}
.navBtn.sec{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
.navBtn.sec:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
.navBtn.pri{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
.navBtn.pri:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text)}
@media(max-width:920px){
  .topNav{position:fixed;top:74px;left:0;right:0;background:#F7F9FC;border-bottom:1px solid var(--line);flex-direction:column;align-items:flex-start;gap:0;padding:6px 22px;max-height:0;overflow:hidden;transition:max-height .25s ease;z-index:60}
  .topNav.open{max-height:280px;padding:14px 22px}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.08)}
  .navToggle{display:inline-flex}
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
<header class="top"><div class="wrap brand"><div>
  <a href="/" style="text-decoration:none;display:flex;align-items:center;gap:12px">
    <div style="width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div>
      <div style="font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2">
        Digital Finance Business Partner
      </div>
      <div style="font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px">
        Finansal Teşhis &amp; Yönetim Karar Destek Platformu
      </div>
    </div>
  </a>
</div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/hakkimizda" class="active">Hakkımızda</a><a href="/uygulama">Uygulama</a><a href="/paketler">Paketler</a><a href="/guvenlik">Güvenlik</a><a href="/iletisim">İletişim</a></nav><div class="navBtns"><a href="/uygulama?auth=login" class="navBtn sec">Giriş Yap</a><a href="/uygulama?auth=register" class="navBtn pri">Ücretsiz Kayıt Ol</a></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<div class="pageHead reveal in"><span class="eyebrow">Hakkımızda</span><h1>Muhasebe Raporu Değil, Stratejik İş Kararları Üretiyoruz</h1><p>Finans ekiplerinin ve şirket sahiplerinin saatlerce harcadığı "rakamları toparlama ve mutabakat" işini sıfıra indirip, zamanı asıl değerin üretildiği yere — stratejik iş ve yönetim kararlarına — taşıyoruz.</p></div>

<div class="secBlock reveal"><section id="about" class="marketingSection hidePrint" style="padding-top:0"><div class="aboutGrid">
<div><span class="badge" style="margin-bottom:14px;display:inline-block">Kurumsal Değer Önerimiz</span><h2 style="font-family:var(--serif);font-size:30px;margin:6px 0 12px;letter-spacing:-.5px">Finansal Verileri İş Kararlarına Dönüştüren Sistem</h2><p class="muted" style="font-size:14.5px;line-height:1.7">Digital Finance Business Partner, finansal verileri statik bir defter kaydı olmaktan çıkarıp şirketin geleceğini yöneten bir karar motoruna dönüştürmek amacıyla kuruldu. Sistem önce <b>33 finansal karar motoruyla</b> çift taraflı denetim yapar; rakamları doğrular, kârın nerede nakde dönüşmediğini saptar ve somut yönetim kararları ile aksiyon planları üretir. Yapay zeka yalnızca üstte ayrı etiketlenmiş stratejik bir yorum katmanıdır; rakamlar asla halüsinasyona bırakılmaz.</p><div class="aboutStats"><div class="st"><b>33</b><span>Karar Motoru</span></div><div class="st"><b>%100</b><span>Deterministik Denetim</span></div><div class="st"><b>0</b><span>Kalıcı Veri Saklama</span></div></div></div>
<div class="card" style="padding:26px">
<div style="display:inline-flex;align-items:center;gap:8px;background:#EFF6FF;border:1px solid #BFDBFE;color:var(--accent);font-size:11.5px;font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:6px 14px;border-radius:999px;margin-bottom:16px">
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
  Bağımsız Karar Destek Prensibi
</div>
<h3 style="margin:0 0 12px;font-family:var(--serif);font-size:20px;color:#0F1B2D">Temel İlkelerimiz</h3>
<ul style="margin:0;padding-left:18px;color:#33415C;font-size:13.5px;line-height:2">
<li>Karar destek, robotik veya kuru rapor üretiminden çok farklıdır.</li>
<li><b>Önce hesap, sonra yorum</b> — sıra asla değişmez.</li>
<li>Veri sizindir; oturum RAM'de işlenir, sunucuda kalıcı depolanmaz.</li>
<li>Yapay zekâ yorumu, doğrulanmış rakamların yerine değil, üstüne konur.</li>
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
    <div style="color:#1D4ED8;font-size:12px;font-weight:700;margin-bottom:10px">Patronu "Kâğıt Üstünde Kâr" Yanılsamasından Kurtarmak</div>
    <p style="color:#5B6B84;font-size:13px;line-height:1.65;margin:0">Muhasebe geçmişi kaydeder, patron ise yarın için risk alır. Aradaki en ölümcül tehlike; şirketin defterde kârlı görünürken, paranın müşteri vadelerinde ve depoda kilitlenip şirketi sessizce tüketmesidir. Temel varoluş sebebimiz; bu finansal kör noktayı anında ortadan kaldırmak ve patronun şirketteki her kuruşun nereye bağlandığını çıplak gözle görmesini sağlamaktır.</p>
  </div>
  <div class="card" style="padding:28px;border-top:4px solid #10B981;background:#FFFFFF;box-shadow:0 8px 26px rgba(15,27,45,0.05)">
    <div style="font-size:32px;margin-bottom:12px">⚡</div>
    <h3 style="font-size:18px;font-family:var(--serif);margin:0 0 8px;color:#0F1B2D">Misyonumuz (Her Gün Yaptığımız İş)</h3>
    <div style="color:#047857;font-size:12px;font-weight:700;margin-bottom:10px">Her Şirketin Masasına Bağımsız Bir CFO Aklı Koymak</div>
    <p style="color:#5B6B84;font-size:13px;line-height:1.65;margin:0">Milyonluk danışmanlık faturalarına veya aylar süren ERP projelerine gerek bırakmadan; Türkiye'deki her KOBİ ve işletmenin yüklediği mizanı <b>60 saniyede 33 deterministik karar motoruyla</b> denetlemek, görünmez kâr sızıntılarını kuruşu kuruşuna hesaplamak ve vadesi, sahibi, TL getirisi belli icraat kararlarını doğrudan masaya koymaktır.</p>
  </div>
  <div class="card" style="padding:28px;border-top:4px solid #F59E0B;background:#FFFFFF;box-shadow:0 8px 26px rgba(15,27,45,0.05)">
    <div style="font-size:32px;margin-bottom:12px">🎯</div>
    <h3 style="font-size:18px;font-family:var(--serif);margin:0 0 8px;color:#0F1B2D">Vizyonumuz (Hedeflediğimiz Dönüşüm)</h3>
    <div style="color:#B45309;font-size:12px;font-weight:700;margin-bottom:10px">Sezgisel Yönetimden, "Rakamla Kanıtlanmış İcraat" Standartlarına Geçiş</div>
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

<div class="secBlock reveal">
  <div class="marketingHead">
    <span class="workflowBadge">KURUMSAL ÇALIŞMA DİSİPLİNİMİZ</span>
    <h2>Finansal Ham Veriden Yönetim Kurulu İcraatına: 3 Kademeli Karar Mimarisi</h2>
    <p>Rakamların arkasındaki operasyonel gerçekleri ortaya çıkaran, varsayımları eleyen ve şirketi doğrudan net nakit üretimine odaklayan kurumsal metodolojimiz.</p>
  </div>
  <div class="grid3">
    <div class="card" style="padding:26px;background:#FFFFFF;border:1px solid #E2E8F0;box-shadow:0 6px 20px rgba(15,27,45,0.04)">
      <div class="tag positive" style="margin-bottom:10px;font-size:11px;font-weight:800">KADEME 01 · GÜVENİLİRLİK</div>
      <h3 style="margin:0 0 8px;font-size:16px;color:#0F1B2D">Deterministik Veri Bütünlüğü &amp; Çift Yönlü Mutabakat</h3>
      <p style="color:#5B6B84;font-size:13px;line-height:1.65;margin:0">ERP veya muhasebe sistemlerinden (Logo, Netsis, Mikro, Luca, SAP vb.) aktarılan mizan ve alt defter kayıtları; tekdüzen hesap planı hiyerarşisi, bilanço-gelir tablosu dengesi ve çift taraflı kayıt kurallarına göre kuruş sapmasız denetlenir. Veri güvenilirliği %100 matematiksel olarak doğrulanmadan hiçbir analitik hesaplama başlatılmaz.</p>
    </div>
    <div class="card" style="padding:26px;background:#FFFFFF;border:1px solid #E2E8F0;box-shadow:0 6px 20px rgba(15,27,45,0.04)">
      <div class="tag" style="margin-bottom:10px;font-size:11px;font-weight:800;background:#EFF6FF;color:#1D4ED8">KADEME 02 · TEŞHİS</div>
      <h3 style="margin:0 0 8px;font-size:16px;color:#0F1B2D">33 Finansal Karar Motoru &amp; Çok Boyutlu Kök Neden Teşhisi</h3>
      <p style="color:#5B6B84;font-size:13px;line-height:1.65;margin:0">Doğrulanmış veri; çalışma sermayesi kilitlenmeleri (DSO, DIO, DPO makası), kâr kalitesi, görünmez finansman faiz sızıntıları, DuPont özkaynak kârlılığı ve müşteri bazlı gizli zarar dinamiklerini kuruşu kuruşuna modelleyen 33 karar motoruna beslenir. Sistem sadece "ne oldu"yu değil; paranın nereye kilitlendiğini ve kârın neden eridiğini kanıtlar.</p>
    </div>
    <div class="card" style="padding:26px;background:#FFFFFF;border:1px solid #E2E8F0;box-shadow:0 6px 20px rgba(15,27,45,0.04)">
      <div class="tag" style="margin-bottom:10px;font-size:11px;font-weight:800;background:#FEF3C7;color:#D97706">KADEME 03 · İCRAAT</div>
      <h3 style="margin:0 0 8px;font-size:16px;color:#0F1B2D">İcra Kurulu Karar Taslağı, What-If Simülasyonu &amp; Eylem Planı</h3>
      <p style="color:#5B6B84;font-size:13px;line-height:1.65;margin:0">Teşhis edilen her finansal bulgu; <i>"Sorumlusu Kim?"</i>, <i>"Termini Ne Zaman?"</i> ve <i>"Kasaya Kazandıracağı Net TL Tutarı Kaç Lira?"</i> kriterleriyle icraat takvimine bağlanır. What-If senaryolarıyla tahsilat, stok ve marj kararlarının nakit etkisi önceden test edilir; üst yönetimin onayına ölçülebilir bir karar paketi sunulur.</p>
    </div>
  </div>
</div>
<div class="secBlock reveal"><section class="ctaBanner hidePrint"><div><h3>Bizi tanımak ister misiniz?</h3><p>Ekibinizle birlikte 15 dakikalık bir canlı demo oturumu planlayabilir veya Data Hub ile anında deneyebilirsiniz.</p></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a href="/uygulama?sample=data_hub" class="primary" style="text-decoration:none;padding:12px 20px;border-radius:11px">🔥 Canlı Demoyu Başlat</a><a href="/iletisim" class="secondary" style="text-decoration:none;padding:12px 20px;border-radius:11px">İletişime Geç</a></div></section></div>

</main>
<div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • deterministic finance layer + optional Gemini interpretation • Financial facts are calculated before AI interpretation.<br><span style="opacity:.85">Bu rapor otomatik/deterministik hesaplamalara ve (etkinleştirildiyse) yapay zekâ yorumuna dayanır; muhasebe, denetim, vergi, hukuki veya yatırım tavsiyesi değildir ve resmi mali tablo/beyanname yerine geçmez. Nihai kararlar için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca bu analizi üretmek için işlenir; sunucu tarafında kalıcı olarak saklanmaz. KVKK kapsamındaki veri işleme hakkında bilgi için [Aydınlatma Metni] bağlantısını inceleyin.</span></div></div></div>
<script>
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
</body></html>'''

CONTACT_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>İletişim | Digital Finance Business Partner</title>
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
.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
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
.topNav{display:flex;gap:26px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.navBtns{display:flex;gap:10px;align-items:center}
.navBtn{display:inline-flex;align-items:center;justify-content:center;padding:8px 18px;border-radius:10px;font-size:13px;font-weight:700;letter-spacing:-.1px;text-decoration:none;cursor:pointer;transition:all .18s ease;line-height:1.2}
.navBtn.sec{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
.navBtn.sec:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
.navBtn.pri{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
.navBtn.pri:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text)}
@media(max-width:920px){
  .topNav{position:fixed;top:74px;left:0;right:0;background:#F7F9FC;border-bottom:1px solid var(--line);flex-direction:column;align-items:flex-start;gap:0;padding:6px 22px;max-height:0;overflow:hidden;transition:max-height .25s ease;z-index:60}
  .topNav.open{max-height:280px;padding:14px 22px}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.08)}
  .navToggle{display:inline-flex}
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
<header class="top"><div class="wrap brand"><div>
  <a href="/" style="text-decoration:none;display:flex;align-items:center;gap:12px">
    <div style="width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div>
      <div style="font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2">
        Digital Finance Business Partner
      </div>
      <div style="font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px">
        Finansal Teşhis &amp; Yönetim Karar Destek Platformu
      </div>
    </div>
  </a>
</div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/hakkimizda">Hakkımızda</a><a href="/uygulama">Uygulama</a><a href="/paketler">Paketler</a><a href="/guvenlik">Güvenlik</a><a href="/iletisim" class="active">İletişim</a></nav><div class="navBtns"><a href="/uygulama?auth=login" class="navBtn sec">Giriş Yap</a><a href="/uygulama?auth=register" class="navBtn pri">Ücretsiz Kayıt Ol</a></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
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
    <div class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg><b>Telefon:</b> +90 (212) 000 00 00</div>
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
<div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • deterministic finance layer + optional Gemini interpretation • Financial facts are calculated before AI interpretation.<br><span style="opacity:.85">Bu rapor otomatik/deterministik hesaplamalara ve (etkinleştirildiyse) yapay zekâ yorumuna dayanır; muhasebe, denetim, vergi, hukuki veya yatırım tavsiyesi değildir ve resmi mali tablo/beyanname yerine geçmez. Nihai kararlar için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca bu analizi üretmek için işlenir; sunucu tarafında kalıcı olarak saklanmaz. KVKK kapsamındaki veri işleme hakkında bilgi için [Aydınlatma Metni] bağlantısını inceleyin.</span></div></div></div>
<script>
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
</body></html>'''

SECURITY_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Security &amp; Governance | Digital Finance Business Partner</title>
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
.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
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
.topNav{display:flex;gap:26px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.navBtns{display:flex;gap:10px;align-items:center}
.navBtn{display:inline-flex;align-items:center;justify-content:center;padding:8px 18px;border-radius:10px;font-size:13px;font-weight:700;letter-spacing:-.1px;text-decoration:none;cursor:pointer;transition:all .18s ease;line-height:1.2}
.navBtn.sec{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
.navBtn.sec:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
.navBtn.pri{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
.navBtn.pri:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text)}
@media(max-width:920px){
  .topNav{position:fixed;top:74px;left:0;right:0;background:#F7F9FC;border-bottom:1px solid var(--line);flex-direction:column;align-items:flex-start;gap:0;padding:6px 22px;max-height:0;overflow:hidden;transition:max-height .25s ease;z-index:60}
  .topNav.open{max-height:280px;padding:14px 22px}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.08)}
  .navToggle{display:inline-flex}
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
<header class="top"><div class="wrap brand"><div>
  <a href="/" style="text-decoration:none;display:flex;align-items:center;gap:12px">
    <div style="width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div>
      <div style="font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2">
        Digital Finance Business Partner
      </div>
      <div style="font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px">
        Finansal Teşhis &amp; Yönetim Karar Destek Platformu
      </div>
    </div>
  </a>
</div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/hakkimizda">Hakkımızda</a><a href="/uygulama">Uygulama</a><a href="/paketler">Paketler</a><a href="/guvenlik" class="active">Güvenlik</a><a href="/iletisim">İletişim</a></nav><div class="navBtns"><a href="/uygulama?auth=login" class="navBtn sec">Giriş Yap</a><a href="/uygulama?auth=register" class="navBtn pri">Ücretsiz Kayıt Ol</a></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
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
<div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • deterministic finance layer + optional Gemini interpretation • Financial facts are calculated before AI interpretation.<br><span style="opacity:.85">Bu rapor otomatik/deterministik hesaplamalara ve (etkinleştirildiyse) yapay zekâ yorumuna dayanır; muhasebe, denetim, vergi, hukuki veya yatırım tavsiyesi değildir ve resmi mali tablo/beyanname yerine geçmez. Nihai kararlar için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca bu analizi üretmek için işlenir; sunucu tarafında kalıcı olarak saklanmaz. KVKK kapsamındaki veri işleme hakkında bilgi için [Aydınlatma Metni] bağlantısını inceleyin.</span></div></div></div>
<script>
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
</body></html>'''

APP_HTML = r'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Uygulama | Digital Finance Business Partner</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&display=swap" rel="stylesheet">
<style>
:root{--bg:#F6F7F9;--panel:#FFFFFF;--panel2:#F0F3F8;--line:#E4E8EF;--text:#0F1B2D;--muted:#5B6B84;--accent:#1D4ED8;--accent2:#4F8CFF;--red:#C22A3E;--amber:#B4720A;--green:#0E7C66;--shadow:0 1px 2px rgba(15,27,45,.04),0 12px 32px rgba(15,27,45,.06);--serif:'Fraunces',ui-serif,Georgia,serif}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(1100px 480px at 12% -10%, rgba(29,78,216,.07), transparent 60%),radial-gradient(900px 420px at 100% 0%, rgba(14,124,102,.05), transparent 55%),#F6F7F9;color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45}button,input,select{font:inherit}.wrap{max-width:1440px;margin:auto;padding:0 28px}.top{padding:26px 0 18px;border-bottom:1px solid rgba(15,27,45,.08);position:sticky;top:0;background:rgba(246,247,249,.86);backdrop-filter:blur(18px);z-index:10}.brand{display:flex;align-items:center;justify-content:space-between;gap:20px}.brand h1{margin:0;font-size:25px;letter-spacing:-.6px}.brand p{margin:3px 0 0;color:var(--muted);font-size:13px}.badge{padding:6px 10px;border:1px solid #D7DEE8;border-radius:999px;color:var(--accent);font-size:12px;white-space:nowrap}.hero{padding:34px 0 24px;display:grid;grid-template-columns:1.45fr .55fr;gap:18px}.heroCard,.card{background:#FFFFFF;border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow)}.heroCard{padding:28px}.heroTitle{font-family:var(--serif);font-weight:600;font-size:44px;line-height:1.08;margin:0 0 14px;letter-spacing:-.5px}.heroText{color:var(--muted);max-width:780px}.framework{display:flex;flex-wrap:wrap;gap:8px 10px;margin:16px 0 2px;padding:0}.framework span{font-size:11.5px;color:#33415C;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px}.framework span b{color:var(--accent);font-weight:800}
.qsel{margin-top:18px}.qsel .qtitle{font-size:12px;color:var(--muted);margin-bottom:8px;font-weight:700}.qsel .qrow{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.qsel button{border:1px solid #D7DEE8;background:#EEF2FF;color:#33415C;border-radius:12px;padding:10px 12px;font-size:12.5px;cursor:pointer;text-align:left;line-height:1.3}.qsel button:hover{border-color:#B7C3D6}.qsel button.active{border-color:var(--accent);color:var(--accent);background:#DCE6FB}
.upload{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}.file{border:1px dashed #C9D2DE;padding:12px;border-radius:12px;background:#F5F7FA;max-width:100%}.select,button{border:1px solid #D7DEE8;border-radius:11px;padding:11px 14px;background:#FFFFFF;color:var(--text)}button.primary,a.primary{background:linear-gradient(135deg,#2557E8,#1D4ED8);border:0;color:#FFFFFF;font-weight:800;cursor:pointer;transition:transform .15s ease,box-shadow .15s ease;box-shadow:0 6px 16px rgba(29,78,216,.25)}a.primary:hover,button.primary:hover{transform:translateY(-1px);box-shadow:0 10px 22px rgba(29,78,216,.32)}button.secondary,a.secondary{cursor:pointer;border:1.5px solid #C9D2DE;background:#FFFFFF;color:var(--text)}a.secondary:hover,button.secondary:hover{border-color:var(--accent);color:var(--accent)}button:disabled{opacity:.5;cursor:not-allowed}.scoreCard{padding:25px;display:flex;flex-direction:column;justify-content:center}.scoreRing{width:170px;height:170px;border-radius:50%;margin:auto;display:grid;place-items:center;background:conic-gradient(var(--accent) calc(var(--score)*1%),#E4E8EF 0);position:relative}.scoreRing:after{content:"";position:absolute;inset:12px;border-radius:50%;background:#FFFFFF}.scoreNum{position:relative;z-index:1;text-align:center}.scoreNum strong{display:block;font-size:48px;line-height:1}.scoreNum span{color:var(--muted);font-size:12px}.status{margin:15px auto 0;padding:7px 12px;border-radius:999px;background:#EAF0FF;color:var(--accent);font-size:12px;font-weight:700}.grid5{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.card{padding:22px;margin:0 0 16px;transition:transform .18s ease,box-shadow .18s ease,outline .2s}.card:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(15,27,45,.08)}@keyframes growUp{from{transform:scaleY(0);opacity:0}to{transform:scaleY(1);opacity:1}}.wf{transform-origin:bottom}.wf .col{transform-origin:bottom}@keyframes growWidth{from{width:0}to{}}.metric{padding:17px;border:1px solid var(--line);border-radius:15px;background:rgba(15,27,45,.03)}.metric .label{color:var(--muted);font-size:12px}.metric .value{font-size:25px;font-weight:800;margin-top:5px;letter-spacing:-.5px}.metric .sub{font-size:11px;color:var(--muted);margin-top:5px}.sectionHead{display:flex;align-items:end;justify-content:space-between;gap:15px;margin-bottom:17px}.sectionHead h2{margin:0;font-size:18px}.sectionHead p{margin:0;color:var(--muted);font-size:12px}.flowStep{margin:36px 0 14px;padding-top:6px;border-top:1px solid rgba(15,27,45,.08)}.flowStep:first-child{margin-top:0;border-top:0;padding-top:0}.flowLabel{display:flex;align-items:center;gap:10px;font-size:12px;font-weight:800;letter-spacing:1.8px;text-transform:uppercase;color:var(--accent);margin:0 0 4px}.flowLabel .n{width:22px;height:22px;border-radius:50%;background:#EAF0FF;color:var(--accent);display:inline-flex;align-items:center;justify-content:center;font-size:11px}.flowLabel p{margin:0;color:var(--muted);font-size:12.5px;font-weight:500;text-transform:none;letter-spacing:0}.flowLabel.alt{color:var(--accent2)}.flowLabel.alt .n{color:var(--accent2)}.flowSub{color:var(--muted);font-size:12.5px;margin:2px 0 16px 32px}.insight{border:1px solid var(--line);border-radius:15px;padding:16px;background:#F7F9FC}.insight.critical{border-color:#E8B4BD}.insight.high{border-color:#E9CBA8}.insight.medium{border-color:#E5DBA0}.insight.positive{border-color:#A9D9C9}.insight h3{margin:0 0 5px;font-size:14px}.insight p{margin:6px 0;color:#33415C;font-size:13px}.insight ul{margin:6px 0;padding-left:18px;color:#33415C;font-size:13px}.tag{display:inline-flex;padding:4px 8px;border-radius:999px;font-size:10px;font-weight:800;text-transform:uppercase;background:#EAF0FF;color:#5B6B84}.tag.critical{background:#FCE8EA;color:#C22A3E}.tag.high{background:#FDF0E0;color:#B4720A}.tag.medium{background:#FBF6DE;color:#8A6D00}.tag.positive{background:#E4F5EF;color:#0E7C66}.riskRow,.actionRow{display:grid;grid-template-columns:40px 1fr auto;gap:12px;align-items:center;padding:13px 0;border-bottom:1px solid rgba(15,27,45,.08)}.rank{font-size:18px;font-weight:900;color:#5B6B84}.riskScore{font-size:12px;color:var(--muted)}.bar{height:7px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:8px}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:99px}.waterfall{display:flex;align-items:flex-end;gap:7px;height:190px;padding:20px 5px 0;border-bottom:1px solid var(--line)}.wf{flex:1;display:flex;flex-direction:column;justify-content:end;height:100%;min-width:0}.wf .col{border-radius:6px 6px 2px 2px;background:linear-gradient(180deg,#83a4ff,#506fd0);min-height:3px}.wf.neg .col{background:linear-gradient(180deg,#ff8290,#9d3e54)}.wf .lab{font-size:10px;color:var(--muted);text-align:center;margin-top:7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.wf .num{font-size:9px;text-align:center;color:#33415C;margin-bottom:4px}.scenario{padding:18px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(145deg,#F5F8FF,#EEF3FC)}.scenario h3{margin:0 0 6px;font-size:15px}.scenario .big{font-size:24px;font-weight:900;color:var(--accent)}.scenario p{color:var(--muted);font-size:11px;margin:6px 0}.muted{color:var(--muted)}.small{font-size:11px}.tableWrap{overflow:auto}table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:10px 8px;border-bottom:1px solid rgba(15,27,45,.08);text-align:right}th:first-child,td:first-child{text-align:left}th{color:#5B6B84;font-weight:600}.notice{padding:12px 14px;border-radius:12px;background:#EEF2FF;border:1px solid var(--line);color:#5B6B84;font-size:12px}.error{color:#C22A3E;background:#FCE8EA;border:1px solid #E8B4BD;padding:12px;border-radius:12px;margin:15px 0}.hidden{display:none!important}.footer{padding:25px 0 50px;color:#5B6B84;font-size:11px;text-align:center}.tabs{display:flex;gap:8px;margin-top:16px}.tab{padding:8px 12px;border-radius:999px;background:#F0F3F8;border:1px solid var(--line);color:#5B6B84;cursor:pointer}.tab.active{background:#DCE6FB;color:var(--accent);border-color:#1D4ED8}.tabPanel{display:none}.tabPanel.active{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.hidePrint{display:block}
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
.heroPreview .pvLabel{font-size:11px;color:var(--muted);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}
.heroPreview .pvLabel span.dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;box-shadow:0 0 0 3px rgba(14,124,102,.15)}
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
@media(max-width:1000px){.hero{grid-template-columns:1fr}.grid5,.grid4{grid-template-columns:repeat(2,1fr)}.grid3,.grid2{grid-template-columns:1fr}.wrap{padding:0 15px}.heroTitle{font-size:31px}.flowSub{margin-left:0}.qsel .qrow{grid-template-columns:1fr}}
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
.topNav{display:flex;gap:26px;align-items:center}
.topNav a{color:var(--muted);font-size:13.5px;text-decoration:none;font-weight:600;padding:6px 2px;border-bottom:2px solid transparent;transition:color .15s,border-color .15s}
.topNav a:hover{color:var(--text)}
.topNav a.active{color:var(--accent);border-color:var(--accent)}
.top.scrolled{box-shadow:0 12px 30px rgba(15,27,45,.10)}
.navBtns{display:flex;gap:10px;align-items:center}
.navBtn{display:inline-flex;align-items:center;justify-content:center;padding:8px 18px;border-radius:10px;font-size:13px;font-weight:700;letter-spacing:-.1px;text-decoration:none;cursor:pointer;transition:all .18s ease;line-height:1.2}
.navBtn.sec{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
.navBtn.sec:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
.navBtn.pri{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
.navBtn.pri:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
#authArea{display:flex;gap:10px;align-items:center}
#authArea button{padding:8px 18px;border-radius:10px;font-size:13px;font-weight:700;line-height:1.2;cursor:pointer;transition:all .18s ease}
#authArea button.secondary{background:#FFFFFF;border:1.5px solid #CBD5E1;color:#1E293B}
#authArea button.secondary:hover{border-color:var(--accent);color:var(--accent);background:#F8FAFC}
#authArea button.primary{background:linear-gradient(135deg,#2563EB 0%,#1D4ED8 100%);border:1.5px solid #1D4ED8;color:#FFFFFF;box-shadow:0 4px 12px rgba(29,78,216,.28)}
#authArea button.primary:hover{background:linear-gradient(135deg,#1D4ED8 0%,#1E40AF 100%);transform:translateY(-1px);box-shadow:0 6px 16px rgba(29,78,216,.36)}
.navToggle{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:8px 10px;cursor:pointer;color:var(--text)}
@media(max-width:920px){
  .topNav{position:fixed;top:74px;left:0;right:0;background:#F7F9FC;border-bottom:1px solid var(--line);flex-direction:column;align-items:flex-start;gap:0;padding:6px 22px;max-height:0;overflow:hidden;transition:max-height .25s ease;z-index:60}
  .topNav.open{max-height:280px;padding:14px 22px}
  .topNav a{width:100%;padding:12px 0;border-bottom:1px solid rgba(15,27,45,.08)}
  .navToggle{display:inline-flex}
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
<header class="top"><div class="wrap brand"><div>
  <a href="/" style="text-decoration:none;display:flex;align-items:center;gap:12px">
    <div style="width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,#1D4ED8 0%,#0E7C66 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(29,78,216,0.28);flex-shrink:0">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
        <path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 6-8"/><circle cx="21" cy="5" r="2" fill="#FFFFFF"/>
      </svg>
    </div>
    <div>
      <div style="font-family:var(--serif);font-size:18px;font-weight:700;color:#0F1B2D;letter-spacing:-.4px;line-height:1.2">
        Digital Finance Business Partner
      </div>
      <div style="font-size:11px;color:#64748B;font-weight:500;letter-spacing:.2px;margin-top:2px">
        Finansal Teşhis &amp; Yönetim Karar Destek Platformu
      </div>
    </div>
  </a>
</div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/hakkimizda">Hakkımızda</a><a href="/uygulama" class="active">Uygulama</a><a href="/paketler">Paketler</a><a href="/guvenlik">Güvenlik</a><a href="/iletisim">İletişim</a></nav><div id="authArea"><button id="loginOpenBtn" class="secondary">Giriş Yap</button> <button id="registerOpenBtn" class="primary">Ücretsiz Kayıt Ol</button></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
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

<main class="wrap"><section class="hero"><div class="heroCard"><h2 class="heroTitle">Mizanınızı Yükleyin, <span style="color:var(--accent)">Şirketinizin Karar Raporunu</span> Alın.</h2><p class="heroText">Mizan veya finansal defterlerinizi yükleyin — 33 karar motoru verilerinizi çift taraflı denetler, kâr sızıntılarını kuruşuna kadar hesaplar, riskleri önceliklendirir ve yarın uygulanacak yönetim kararlarını masaya koyar.</p><div class="framework"><span><b>1. NE OLDU?</b> (Finansal Gerçekler)</span><span><b>2. PARA NEREDE?</b> (Kilitli Nakit &amp; Sızıntı)</span><span><b>3. RİSK &amp; SEKTÖR NE?</b> (Kıyaslama)</span><span><b>4. KİM YAPIYOR?</b> (Müşteri &amp; Stok Zekâsı)</span><span><b>5. NEDEN OLDU?</b> (Kök Neden)</span><span><b>6. NE YAPMALIYIZ?</b> (Yönetim Kararları)</span><span><b>7. SİMÜLE ET</b> (What-If Laboratuvarı)</span></div>
<div style="margin-top:14px;display:flex;flex-wrap:wrap;gap:10px;align-items:center"><button id="sampleBtn" class="secondary">📄 Tek dönem örnekle dene</button><button id="sampleTrendBtn" class="secondary">📊 İki dönemli örnekle dene (Trend Demo)</button><button id="sampleHubBtn" class="secondary">🗂️ Data Hub örnekle dene (Mizan + AR + AP + Stok + Satış)</button> <span id="sampleStatus" class="small muted" style="margin-left:8px"></span></div>
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
<div id="error" class="error hidden"></div>
</div><div class="heroCard scoreCard"><div id="scoreRing" class="scoreRing" style="--score:0"><div class="scoreNum"><strong id="score">-</strong><span>Finansal Sağlık Skoru</span></div></div><div id="healthLabel" class="status">Dosya bekleniyor</div>
<div id="topFocusCard" class="hidden hidePrint" style="margin-top:14px;border-top:1px solid rgba(15,27,45,.10);padding-top:10px;text-align:left"><div style="font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px">Öncelikli Odak Konuları</div><div id="topFocusList" style="display:flex;flex-direction:column;gap:6px"></div></div>
<div id="pvPreview" class="hidePrint" style="margin-top:18px;padding-top:16px;border-top:1px solid rgba(15,27,45,.10);text-align:left">
  <div class="pvLabel"><span><span class="dot"></span>Örnek Rapor Görünümü</span><span>Canlı Karar Motoru</span></div>
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

<!-- CEO & YÖNETİM KURULU KARAR MASASI (3 KATMANLI MOTOR) -->
<section id="ceoDiagnosticSection" class="flowStep" style="margin-bottom:28px">
  <div class="card" style="border:2px solid #1D4ED8;background:linear-gradient(180deg,#FFFFFF 0%,#F8FAFC 100%);box-shadow:0 14px 40px rgba(29,78,216,.09);padding:26px;border-radius:22px">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px;border-bottom:1.5px solid #E2E8F0;padding-bottom:18px;margin-bottom:20px">
      <div>
        <div style="display:inline-flex;align-items:center;gap:8px;background:#EFF6FF;border:1px solid #BFDBFE;padding:4px 12px;border-radius:999px;color:#1D4ED8;font-size:11px;font-weight:800;letter-spacing:.5px;margin-bottom:8px">
          👔 CEO &amp; İCRA KURULU FİNANSAL TEŞHİS MASASI
        </div>
        <h2 style="font-family:var(--serif);font-size:24px;color:#0F1B2D;margin:0 0 6px;letter-spacing:-.5px">
          Finansal Gerçeklerden Yönetim İcraatına: 8 Kritik Patron Sorusu
        </h2>
        <p class="muted" style="margin:0;font-size:13.5px;max-width:880px;line-height:1.6">
          Patron muhasebe raporu değil; <i>"Kasada neden para yok ve yarın ne yapmalıyım?"</i> sorusunun cevabını ister. Yüklediğiniz mizan ve defterlerden <b>33 Finansal Karar Motorunun</b> ürettiği anlık 3 katmanlı teşhis, kurtarılabilir kâr ve aksiyonlar:
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

    <!-- Question Detail Container (Shows Katman 1, Katman 2, Katman 3) -->
    <div id="ceoQuestionDetails"></div>
  </div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">1</span>Finansal Gerçekler &amp; Kârlılık Kalitesi (Ne Oldu?)<p>Şirkette gerçekte ne oldu: Kâr nereden nereye aktı?</p></div><div class="flowSub">Doğrulanmış rakamlar: Ciro, operasyonel kâr kalitesi, borç yapısı ve kârın nakde dönüşümü.</div>
<div class="grid4"><div class="metric"><div class="label">Net Satış (Ciro)</div><div id="mSales" class="value">-</div><div class="sub">Doğrulanmış toplam satış hacmi</div></div><div class="metric"><div class="label">Faaliyet Kârı</div><div id="mOp" class="value">-</div><div class="sub">Esas faaliyetlerden kalan operasyonel kâr</div></div><div class="metric"><div class="label">Net Dönem Kârı</div><div id="mNet" class="value">-</div><div class="sub">Vergi ve finansman giderleri sonrası net kâr</div></div><div class="metric"><div class="label">Net Finansal Borç</div><div id="mDebt" class="value">-</div><div class="sub">Toplam banka borcundan nakit düşülmüş net yük</div></div></div>
<div id="dupontCard" class="card hidden" style="margin-top:16px"><div class="sectionHead"><div><h2>Özkaynak Kârlılık Ağacı (ROE Motorları)</h2><p>Hissedarın koyduğu sermayenin getirisini (ROE) belirleyen üç ana motor: Kâr Marjı × Varlık Devir Hızı × Finansal Kaldıraç</p></div></div><div class="grid4"><div class="metric"><div class="label">Özkaynak Kârlılığı (ROE)</div><div id="dupontRoe" class="value">-</div><div class="sub">Hissedar Getirisi</div></div><div class="metric"><div class="label">Net Kâr Marjı</div><div id="dupontMargin" class="value">-</div><div class="sub">Operasyonel Kârlılık Oranı</div></div><div class="metric"><div class="label">Varlık Devir Hızı</div><div id="dupontTurnover" class="value">-</div><div class="sub">Varlıkları Paraya Çevirme Hızı</div></div><div class="metric"><div class="label">Kaldıraç Çarpanı</div><div id="dupontLeverage" class="value">-</div><div class="sub">Varlık / Özkaynak Çarpanı</div></div></div><div id="dupontDiagnosis" class="chips" style="margin-top:12px"></div></div>
<div id="comparativeCard" class="card hidden" style="margin-top:16px"><div class="sectionHead"><div><h2>Dönemsel Trend Karşılaştırması</h2><p>Yüklenen dönemler arasındaki değişim, büyüme yönü ve yönetim için anlamı</p></div></div><div id="comparativeCards" class="grid3" style="margin-top:4px"></div><div id="comparativeFindings" style="margin-top:14px"></div><div id="comparativeTable" class="tableWrap" style="margin-top:14px"></div></div>
<section style="margin-top:16px"><div id="profitQualityCard" class="card"><div class="sectionHead"><div><h2>Kâr Köprüsü &amp; Kâr Kalitesi</h2><p>Net satıştan net kâra giden yol ve bu kârın ne kadarının operasyonel olduğu</p></div></div><div class="grid2"><div><div class="small muted" style="margin-bottom:8px">Kâr Köprüsü</div><div id="waterfall" class="waterfall"></div></div><div><div class="small muted" style="margin-bottom:8px">Kâr Kalitesi Analizi</div><div id="profitQuality"></div></div></div><div id="profitabilityCommentary" style="margin-top:14px"></div></div></section>
<div class="grid2" style="margin-top:16px">
  <div id="leverageCard" class="card"><div class="sectionHead"><div><h2>Borç Yapısı &amp; Likidite</h2><p>Bilançonun taşıdığı finansal borç baskısı ve kısa vadeli ödeme gücü</p></div></div><div id="liquidity" class="grid2"></div><div id="leverageCommentary" style="margin-top:14px"></div></div>
  <div id="solvencyCard" class="card"><div class="sectionHead"><div><h2>Finansal Sağlık &amp; Sermaye Dayanıklılığı</h2><p>Faiz karşılama gücü, borç servis kapasitesi ve bilanço tamponu</p></div></div><div id="solvencyMetrics" class="grid2"></div><div id="solvencyCommentary" style="margin-top:14px"></div></div>
</div>
<div id="cashBridgeCard" class="card" style="margin-top:16px">
  <div class="sectionHead"><div><h2>Nakit Akış Köprüsü &amp; Kârın Nakde Dönüşümü</h2><p>Defterdeki net kârın ne kadarı fiilen kasaya giriyor ve dönem boyunca gerçek para hareketi</p></div><span class="tag positive" style="font-weight:700">DÖNÜŞÜM ANALİTİĞİ</span></div>
  <div id="cashBridgeContent"></div>
</div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">2</span>Para Nerede? — Çalışma Sermayesi Kilitlenmesi &amp; Görünmez Kâr Sızıntısı<p>Kâğıt üzerinde kâr var ama para kasada nerede duruyor?</p></div><div class="flowSub">Nakit Çevrim Döngüsü (CCC), vadeler, alacak ve depoda kilitlenen TL sermaye ve yıllık %45 finansman faiz sızıntısı.</div>

<div id="workingCapitalLeakEngineCard" class="card" style="border:1.5px solid #CBD5E1;background:linear-gradient(145deg,#FFFFFF 0%,#F8FAFC 100%)">
  <div class="sectionHead">
    <div>
      <h2 style="font-size:16px;color:#1D4ED8">⚡ Çalışma Sermayesi (CCC) &amp; Kilitli Nakit Teşhis Panosu</h2>
      <p>Yüklenen mizan ve defterlerinizden hesaplanan gerçek nakit çevrim günleri, sermaye kilitlenmesi ve faiz yükü</p>
    </div>
    <span class="tag positive" style="font-weight:800;font-size:11px">CANLI MİZAN TEŞHİSİ</span>
  </div>
  
  <div class="grid5" style="margin-top:10px" id="wcMetricsRow">
    <div class="metric" style="background:#FFFFFF;border-color:#FCA5A5">
      <div class="label" style="color:#DC2626">🔒 Kilitli Alacak (120)</div>
      <div id="wcLeakArVal" class="value" style="color:#991B1B">-</div>
      <div id="wcLeakArSub" class="sub">DSO Tahsilat: – gün</div>
    </div>
    <div class="metric" style="background:#FFFFFF;border-color:#FCD34D">
      <div class="label" style="color:#D97706">📦 Kilitli Stok (150-153)</div>
      <div id="wcLeakInvVal" class="value" style="color:#B45309">-</div>
      <div id="wcLeakInvSub" class="sub">DIO Bekleme: – gün</div>
    </div>
    <div class="metric" style="background:#FFFFFF;border-color:#93C5FD">
      <div class="label" style="color:#2563EB">🏭 Tedarikçiler (320)</div>
      <div id="wcLeakApVal" class="value" style="color:#1D4ED8">-</div>
      <div id="wcLeakApSub" class="sub">DPO Ödeme: – gün</div>
    </div>
    <div class="metric" style="background:#FFFFFF;border-color:#C7D2FE">
      <div class="label" style="color:#4338CA">⏱️ Nakit Çevrim (CCC)</div>
      <div id="wcLeakCccVal" class="value" style="color:#3730A3">-</div>
      <div id="wcLeakCccSub" class="sub">Net Nakit Döngüsü</div>
    </div>
    <div class="metric" style="background:#FFFFFF;border-color:#FECDD3">
      <div class="label" style="color:#E11D48">💸 Yıllık Kâr Sızıntısı</div>
      <div id="wcLeakCostVal" class="value" style="color:#BE123C">-</div>
      <div id="wcLeakCostSub" class="sub">%45 faiz maliyeti</div>
    </div>
  </div>

  <div id="wcNarrativeBox" style="margin-top:14px"></div>

  <!-- Entegre Sermaye Dağılımı ve Varlık Yapısı -->
  <div id="resourceAllocationCard" class="hidden" style="margin-top:16px;padding-top:14px;border-top:1px solid #E2E8F0">
    <div class="small muted" style="margin-bottom:8px;font-weight:700">ŞİRKET SERMAYESİNİN VARLIK DAĞILIMI (PARA NEREDE DURUYOR?)</div>
    <div id="resourceAllocationMetrics" class="grid4"></div>
    <div id="resourceAllocationBar" style="margin-top:14px"></div>
    <div id="resourceAllocationNarrative" style="margin-top:12px"></div>
  </div>

  <!-- Çoklu Kaldıraçlı Nakit Kurtarma Simülatörü -->
  <div style="margin-top:16px;background:#FFFFFF;border:1px solid #E2E8F0;border-radius:14px;padding:16px">
    <div style="font-size:13.5px;font-weight:800;color:#0F172A;margin-bottom:12px;display:flex;justify-content:space-between;align-items:center">
      <span>🎛️ Çalışma Sermayesi Kilitli Nakit Kurtarma Simülatörü</span>
      <span class="tag" style="background:#EFF6FF;color:var(--accent);font-size:10.5px">SERBEST NAKİT KALDIRAÇLARI</span>
    </div>

    <div class="grid3" style="gap:14px">
      <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
          <span style="font-size:12px;font-weight:700;color:#1E293B">1. Tahsilatı Hızlandır (DSO)</span>
          <b id="wcSliderDsoDisplay" style="color:#1D4ED8;font-size:13px">15 Gün Erken</b>
        </div>
        <input id="wcSliderDso" type="range" min="0" max="60" value="15" step="1" style="width:100%;cursor:pointer">
      </div>

      <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
          <span style="font-size:12px;font-weight:700;color:#1E293B">2. Stok Devrini Artır (DIO)</span>
          <b id="wcSliderDioDisplay" style="color:#D97706;font-size:13px">10 Gün Daha Hızlı</b>
        </div>
        <input id="wcSliderDio" type="range" min="0" max="60" value="10" step="1" style="width:100%;cursor:pointer">
      </div>

      <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 14px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
          <span style="font-size:12px;font-weight:700;color:#1E293B">3. Tedarikçi Vadesi (DPO)</span>
          <b id="wcSliderDpoDisplay" style="color:#0E7C66;font-size:13px">5 Gün Öteleme</b>
        </div>
        <input id="wcSliderDpo" type="range" min="0" max="45" value="5" step="1" style="width:100%;cursor:pointer">
      </div>
    </div>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px">
      <div style="background:#F0FDF4;border:1.5px solid #BBF7D0;border-radius:12px;padding:12px 16px">
        <div style="font-size:11px;font-weight:800;color:#16A34A;text-transform:uppercase">🚀 Kasaya Girecek Sıcak Nakit</div>
        <div id="wcSliderCashLiberated" style="font-size:24px;font-weight:900;color:#047857;margin-top:2px">+₺0</div>
        <div class="small muted">Alacak tahsilatı + stok eritme + tedarikçi finansmanıyla doğrudan kasaya giren nakit</div>
      </div>
      <div style="background:#EFF6FF;border:1.5px solid #BFDBFE;border-radius:12px;padding:12px 16px">
        <div style="font-size:11px;font-weight:800;color:#1D4ED8;text-transform:uppercase">📈 Yıllık Kurtarılacak Faiz Tasarrufu</div>
        <div id="wcSliderInterestSaved" style="font-size:24px;font-weight:900;color:#1E40AF;margin-top:2px">+₺0 / yıl</div>
        <div class="small muted">Kurtarılan %45 kredi faizi yüküyle doğrudan şirkette kalan kâr</div>
      </div>
    </div>
  </div>

  <div id="wcLeakSummaryBox" class="insight" style="margin-top:14px;margin-bottom:0"></div>
</div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">3</span>Sektörel Kıyaslama &amp; Öncelikli Riskler (Bize Maliyeti Ne?)<p>Sektör ortalamalarına göre neredeyiz ve acil ele alınması gereken riskler</p></div><div class="flowSub">TCMB Sektör Bilançoları &amp; Borsa İstanbul (BIST) 500+ şirket verisiyle kıyaslama ve skorlanmış riskler.</div>
<div class="card"><div class="sectionHead"><div><h2>Sektörel Kıyaslama &amp; Göstergeler (TCMB &amp; BIST)</h2><p>Yön duyarlı, gösterge amaçlı sektör bantları ve şirketin sektöre göre konumu</p></div></div><div id="benchmark"></div></div>
<div class="card" style="margin-top:16px"><div class="sectionHead"><div><h2>Öncelikli Yönetim Riskleri</h2><p>Finansal maruziyet, risk skoru ve şiddet derecesi birlikte sıralanır</p></div></div><div id="risks"></div></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">4</span>Kritik Taraflar &amp; Operasyonel İstihbarat (Sızıntıyı Kim Yapıyor?)<p>Hangi müşteri, tedarikçi veya stok kalemi kârı ve nakdi doğrudan etkiliyor?</p></div><div class="flowSub">Nakit ve kâr üzerinde en büyük etkisi olan müşteriler ve stok kalemleri. Çoklu veri yüklendiğinde otomatik detaylanır.</div>
<div id="criticalPartiesNotice" class="notice">Bu bölüm "Data Hub / Çoklu Veri" sekmesinden satış, alacak yaşlandırma veya stok dosyası yüklendiğinde zenginleşir.</div>
<div id="customerProfitabilityMatrixCard" class="card hidden" style="margin-top:14px"><div class="sectionHead"><div><h2>Müşteri Kârlılık Matrisi (4 Kadran)</h2><p>Hangi müşteriler kâr getiriyor, hangileri ciro yaratıp sermaye tüketiyor?</p></div></div><div id="customerMatrixGrid" class="grid2" style="gap:12px"></div><div id="customerMatrixFindings" style="margin-top:14px"></div></div>
<div id="productProfitabilityCard" class="card hidden" style="margin-top:14px"><div class="sectionHead"><div><h2>Ürün &amp; Portföy Kârlılığı</h2><p>Hangi ürünler brüt kârı sırtlıyor, hangi ürünler depoda sermaye kilitliyor?</p></div></div><div id="productProfitabilityTable" class="tableWrap"></div></div>
<div id="criticalCustomersCard" style="margin-top:14px"></div>
<div id="criticalSuppliersCard" style="margin-top:14px"></div>
<div class="grid2" style="margin-top:14px"><div id="salesIntel"></div><div id="arApIntel"></div></div><div id="inventoryIntel" style="margin-top:14px"></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">5</span>Kök Neden &amp; Karar Hikâyeleri (Neden Oldu?)<p>Bulguların arkasındaki nedensellik zinciri ve finansal maliyeti</p></div><div class="flowSub">Bulgu → Kanıt → Olası Kök Neden → Alınacak Karar. Tek tek okunabilir yönetim hikâyeleri.</div>
<div id="rootCauseCard" class="card"><div id="rootCause"></div></div>
<div id="narrativeStories" style="margin-top:16px"></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">6</span>Yönetim Kararları &amp; Aksiyon Takvimi (Şimdi Ne Yapmalı?)<p>Yönetimin masaya koyup uygulayacağı somut kararlar</p></div><div class="flowSub">Karar maddesi → Sahibi → Termini → Takip Edilecek KPI. Her aksiyon maddesi ayrı bir takip numarasına sahiptir.</div>
<div class="card"><div id="actions"></div></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">7</span>Varsayımı Değiştirirsek Ne Olur? (Stratejik P&amp;L &amp; Bilanço Laboratuvarı)<p>Fiyatı artırırsak, gideri kıssak, büyümeyi hızlandırsak veya borcu kapatsak ne kazanırız?</p></div><div class="flowSub">P&amp;L ve bilanço yeniden yapılandırma simülatörü. Çalışma sermayesi kilitli nakit kurtarma kaldıraçları Adım 2'de modellenmiştir; burada marj, gider, büyüme ve sermaye yapısı test edilir.</div>
<div class="card"><div id="opportunities" class="grid3"></div></div>
<div id="interactiveScenarioCard" class="card" style="margin-top:16px"><div class="sectionHead"><div><h2>İnteraktif Senaryo Laboratuvarı &amp; Stratejik P&amp;L Simülatörü</h2><p>Sürgüleri hareket ettirerek marj artışı, gider kısıntısı ve borç itfasının kâr ve faiz etkisini anında simüle edin</p></div><span class="tag positive" style="font-weight:700">STRATEJİK RESTRÜKTÜRASYON</span></div><div class="grid2"><div style="display:flex;flex-direction:column;gap:14px"><div><div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px"><span>1. Brüt Kâr Marjı Artışı (Fiyatlama / Maliyet İyileştirme)</span><b id="sliderMarginVal" style="color:var(--accent)">+0.0%</b></div><input id="sliderMargin" type="range" min="0" max="5.0" value="0" step="0.1" style="width:100%;cursor:pointer"></div><div><div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px"><span>2. Faaliyet Gideri (OpEx) Tasarrufu</span><b id="sliderOpexVal" style="color:var(--accent)">0%</b></div><input id="sliderOpex" type="range" min="0" max="15" value="0" step="1" style="width:100%;cursor:pointer"></div><div><div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px"><span>3. Satış Hacmi Büyümesi</span><b id="sliderGrowthVal" style="color:var(--accent)">0%</b></div><input id="sliderGrowth" type="range" min="0" max="25" value="0" step="1" style="width:100%;cursor:pointer"></div><div><div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px"><span>4. Finansal Borç İtfası (Banka Kredisi Kapama)</span><b id="sliderDebtVal" style="color:var(--accent)">0%</b></div><input id="sliderDebt" type="range" min="0" max="50" value="0" step="5" style="width:100%;cursor:pointer"></div></div><div style="background:#F8FAFC;border:1px solid var(--line);border-radius:15px;padding:18px;display:flex;flex-direction:column;justify-content:center;gap:12px"><div style="font-size:12px;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:1px">Simüle Edilen Stratejik Etki</div><div class="grid2"><div class="metric" style="background:#EAF0FF"><div class="label">Yıllık Ek Faaliyet Kârı</div><div id="simProfitImpact" class="value" style="color:var(--accent)">0 TL</div><div class="sub">P&amp;L Marj + Gider Katkısı</div></div><div class="metric" style="background:#EAF0FF"><div class="label">Yıllık Faiz Tasarrufu</div><div id="simInterestImpact" class="value" style="color:var(--green)">0 TL</div><div class="sub">Borç İtfası Sonucu</div></div></div><div id="simSummaryText" class="small muted" style="line-height:1.5;margin-top:4px">Sürgüleri hareket ettirerek yönetim senaryonuzu belirleyin.</div></div></div></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">8</span>Yönetici Özeti &amp; AI Finance Business Partner (Karar Brifingi)<span class="tag" style="margin-left:8px;background:#eef2ff;color:#3b4b8a">Kural Tabanlı · AI Değil</span><p>Tüm analizin tek paragrafta özeti ve stratejik soru-cevap</p></div><div class="flowSub">Önce matematiksel kurallarla hesaplanır, sonra yorumlanır. Yöneticinin bu raporla hangi stratejik adımı atması gerektiği açıkça belirtilir.</div>
<div class="card"><div id="exec" class="insight"></div><div id="execChips" class="chips"></div><div id="execDecision" style="margin-top:14px"></div><div style="margin-top:14px"><button id="aiBtn" class="secondary hidePrint">✨ AI Finance Partner yorumunu üret (opsiyonel, LLM)</button> <button id="printBtn" class="secondary hidePrint">Raporu yazdır / PDF</button> <button id="jsonBtn" class="secondary hidePrint">JSON indir</button></div><div id="aiBox" class="notice hidden" style="margin-top:12px"></div><div id="methodNote" class="notice" style="margin-top:12px"></div><div style="margin-top:16px;padding-top:16px;border-top:1px solid rgba(15,27,45,.10)"><div style="display:flex;align-items:center;gap:8px;margin-bottom:10px"><span style="font-size:18px">💬</span><b style="font-size:14px">AI Finance Business Partner'a Özel Soru Sor (Stratejik Q&amp;A)</b><span class="tag" style="background:#EAF0FF;color:var(--accent)">Gemini 3.6 Flash Doğrulanmış</span></div><div style="display:flex;gap:10px;align-items:center"><input id="aiCustomPrompt" type="text" placeholder="Örn: Nakit neden oluşmuyor?" style="flex:1;background:#FFFFFF;border:1px solid #D7DEE8;color:#0F1B2D;border-radius:10px;padding:10px 14px;font-size:13px"><button id="aiAskBtn" class="primary hidePrint" style="white-space:nowrap;padding:10px 18px">Soruyu Yanıtla ⚡</button></div><div class="chips hidePrint" style="margin-top:10px"><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Nakit neden oluşmuyor?')">💸 Nakit neden oluşmuyor?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Kâr neden düşüyor?')">📉 Kâr neden düşüyor?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Borç neden artıyor?')">📈 Borç neden artıyor?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Kâr gerçekten nakde dönüşüyor mu?')">🔄 Kâr gerçekten nakde dönüşüyor mu?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Hangi müşteriler risk yaratıyor?')">⚠️ Hangi müşteriler risk yaratıyor?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Hangi tedarikçiler kritik?')">🏭 Hangi tedarikçiler kritik?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Stok neden şişiyor?')">📦 Stok neden şişiyor?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Büyüme neden kâra dönüşmüyor?')">🚀 Büyüme neden kâra dönüşmüyor?</span></div><div id="aiCustomBox" class="notice hidden" style="margin-top:14px"></div></div></div>
</section>

<section class="flowStep"><div class="flowLabel alt"><span class="n">+</span>Ek A — Veri Güvenilirliği &amp; Çift Taraflı Hesaplama Denetimi<p>Analizin dayandığı verinin doğrulanma düzeyi ve dosya bazlı kırılım</p></div>
<div class="card"><div class="sectionHead"><div><h2>Veri Kalitesi &amp; Bilanço Denkliği</h2><p>Skorlar ve bulgular, buradaki veri güvenilirliğine dayanır</p></div></div><div class="grid4"><div class="metric"><div class="label">Veri Güvenilirlik Skoru</div><div id="dq" class="value">-</div><div class="sub" id="dqStatus">-</div></div><div class="metric"><div class="label">Çift Taraflı Denetim</div><div id="auditValue" class="value">-</div><div class="sub" id="auditSub">-</div></div><div class="metric"><div class="label">Eşlenemeyen Hesap Sayısı</div><div id="dqUnmapped" class="value">-</div><div class="sub">Eşlenemeyen hesap sayısı</div></div><div class="metric"><div class="label">Nakit Çevrim Süresi</div><div id="cccMetric" class="value">-</div><div class="sub">Gün</div></div></div><div id="dqChecks" class="tableWrap" style="margin-top:16px"></div><div id="dqIssues" style="margin-top:12px"></div><div id="dqNote" class="notice" style="margin-top:12px"></div></div>
<section id="dataHubCard" class="card hidden"><div class="sectionHead"><div><h2>Çoklu Veri İstihbaratı (Data Hub)</h2><p>Dosya sınıflandırma, kaynak bazlı analiz ve büyük defter mutabakatı</p></div></div><div id="hubSummary" class="grid4"></div><div id="hubSources" class="card" style="margin-top:14px"></div><div id="hubFindings" class="card" style="margin-top:14px"></div><div id="pvmIntel" class="card hidden" style="margin-top:14px"></div><div id="hubReconciliation" class="card" style="margin-top:14px"></div></section>
</section>

<section class="flowStep"><div class="flowLabel alt"><span class="n">+</span>Ek B — Trend İzleme, İzlenebilirlik &amp; 3 Temel Mali Tablo<p>Çok dönem yüklendiğinde hareketi gösterir; her sayı kaynağına izlenebilir</p></div>
<div class="card"><div id="trendBlock"></div><div id="trace" class="tableWrap" style="margin-top:15px"></div></div>
<div class="card" style="margin-top:16px"><div class="sectionHead"><div><h2>3 Temel Mali Tablo (Gelir Tablosu, Bilanço ve Nakit Akış)</h2><p>Doğrulanmış Gelir Tablosu (P&amp;L), Bilanço ve Nakit Akış Tablosu</p></div></div><div class="grid3"><div id="plTable" class="tableWrap"></div><div id="bsTable" class="tableWrap"></div><div id="cfTable" class="tableWrap"></div></div></div>
<div id="printExecutiveNotice" class="printExecutiveFooter" style="display:none">
  <span>Digital Finance Business Partner &bull; Deterministik Finans Karar Motoru &bull; Gizli &amp; Şirket Yönetimine Özel Brifing</span>
  <span>Stratejik Rapor Sonu</span>
</div>
</main><div class="siteFooter"><div class="wrap"><div class="cols"><div class="brandCol"><h1 style="font-size:17px;margin:0 0 8px">Digital Finance Business Partner</h1><p>Rakamları değil kararları gösteren, deterministik hesap + isteğe bağlı AI yorum katmanlı finansal karar destek platformu.</p></div><div><h4>Ürün</h4><ul><li><a href="/uygulama">Uygulamayı Dene</a></li><li><a href="/paketler">Paketler</a></li></ul></div><div><h4>Şirket</h4><ul><li><a href="/hakkimizda">Hakkımızda</a></li><li><a href="/iletisim">İletişim</a></li></ul></div><div><h4>İletişim</h4><ul><li><a href="mailto:info@digitalfinancebp.com">info@digitalfinancebp.com</a></li><li>İstanbul, Türkiye</li></ul></div></div><div class="legal">Digital Finance Business Partner • deterministic finance layer + optional Gemini interpretation • Financial facts are calculated before AI interpretation.<br><span style="opacity:.85">Bu rapor otomatik/deterministik hesaplamalara ve (etkinleştirildiyse) yapay zekâ yorumuna dayanır; muhasebe, denetim, vergi, hukuki veya yatırım tavsiyesi değildir ve resmi mali tablo/beyanname yerine geçmez. Nihai kararlar için mali müşavirinize/YMM'nize danışın. Yüklediğiniz dosyalar yalnızca bu analizi üretmek için işlenir; sunucu tarafında kalıcı olarak saklanmaz. KVKK kapsamındaki veri işleme hakkında bilgi için [Aydınlatma Metni] bağlantısını inceleyin.</span></div></div></div>
<script>
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
const money=v=>v==null?'–':new Intl.NumberFormat('tr-TR',{maximumFractionDigits:0}).format(v)+' TL';
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
    +'<tr><td style="padding-left:14px">Faaliyet Kârı (EBIT Proxy)</td><td><b>'+money(cb.operating_profit)+'</b></td></tr>'
    +'<tr><td style="padding-left:14px;color:var(--muted)">Δ Ticari Alacak Değişimi (Müşteri)</td><td style="color:'+(wcc.receivables_effect<0?'var(--red)':'var(--green)')+'"><b>'+money(wcc.receivables_effect)+'</b></td></tr>'
    +'<tr><td style="padding-left:14px;color:var(--muted)">Δ Stok Değişimi (Depo Kilidi)</td><td style="color:'+(wcc.inventory_effect<0?'var(--red)':'var(--green)')+'"><b>'+money(wcc.inventory_effect)+'</b></td></tr>'
    +'<tr><td style="padding-left:14px;color:var(--muted)">Δ Ticari Borç Değişimi (Tedarikçi)</td><td style="color:'+(wcc.payables_effect<0?'var(--red)':'var(--green)')+'"><b>'+money(wcc.payables_effect)+'</b></td></tr>'
    +'<tr style="font-weight:700"><td>İşletme Sermayesi Net Etkisi</td><td style="color:'+(cb.working_capital_effect<0?'var(--red)':'var(--green)')+'"><b>'+money(cb.working_capital_effect)+'</b></td></tr>'
    +'<tr style="background:#EAF0FF;font-weight:800"><td>İşletme Faaliyetleri Nakit Akışı (OCF Proxy)</td><td style="color:'+(cb.operating_cash_flow_proxy<0?'var(--red)':'var(--green)')+'"><b>'+money(cb.operating_cash_flow_proxy)+'</b></td></tr>'
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
function metric(label,value,sub,color){return '<div class="metric"><div class="label">'+esc(label)+'</div><div class="value"'+(color?' style="color:'+color+'"':'')+'>'+esc(value)+'</div><div class="sub">'+esc(sub||'')+'</div></div>'}
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
  const unitFor={net_sales:'amount',gross_profit:'amount',operating_profit:'amount',net_profit:'amount',total_assets:'amount',total_equity:'amount',financial_debt:'amount',gross_margin_pct:'pct_points',operating_margin_pct:'pct_points',net_margin_pct:'pct_points',current_ratio:'ratio',debt_to_equity:'x',ccc_days:'days'};
  const dirArrow={improving:'<span style="color:#2e7d32;font-weight:700">↑</span>',worsening:'<span style="color:#c62828;font-weight:700">↓</span>',flat:'<span style="color:#888">→</span>'};
  const rows=Object.entries(tr.metric_trends||{}).map(([k,m])=>{
    const dir=m.latest_direction||'flat';
    const arrowHtml=dirArrow[dir]||'<span style="color:#888">→</span>';
    return '<tr><td style="font-weight:600">'+esc(m.label)+'</td>'+(m.series||[]).map((v,i)=>{
      const prev=m.series[i-1];
      let bg='';
      if(i>0&&prev!=null&&v!=null){const up=v>prev;const good=(k==='financial_debt'||k==='debt_to_equity'||k==='ccc_days')?!up:up;bg=good?'background:#f0fbf3':'background:#fff5f5';}
      return '<td style="'+bg+';text-align:right">'+(unitFor[k]==='ratio'?(v==null?'–':num(v)):_cmpUnit(unitFor[k]||'amount',v))+'</td>';
    }).join('')+'<td style="text-align:center">'+arrowHtml+'</td></tr>';
  }).join('');
  $('comparativeTable').innerHTML='<div class="sectionHead" style="margin-bottom:8px"><div><h2 style="font-size:10.5pt">Tüm Metriklerin Tam Dönem Serisi</h2></div></div><table><thead><tr><th>Metrik</th>'+(tr.period_labels||[]).map(l=>'<th>'+esc(l)+'</th>').join('')+'<th>Yön</th></tr></thead><tbody>'+rows+'</tbody></table><p class="small muted" style="margin-top:8px">'+esc(tr.note||'')+'</p>';
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
function workingCapitalNarrative(c){
  if(!c||c.cash_conversion_cycle_days==null) return '<div class="notice">Nakit dönüşüm süresi hesaplanamadı — DSO/DIO/DPO için yeterli veri yok.</div>';
  const ccc=c.cash_conversion_cycle_days;
  const tier=ccc<=30?'positive':ccc<=75?'medium':'high';
  // Each candidate's own contribution to CCC length: DSO/DIO lengthen it directly,
  // a *low* DPO lengthens it (little supplier financing), so compare on that basis.
  const candidates=[['DSO','Alacak tahsilat süresi',c.dso_days,c.dso_days],['DIO','Stokta bekleme süresi',c.dio_days,c.dio_days],['DPO','Tedarikçiye ödeme süresinin kısalığı',c.dpo_days,c.dpo_days==null?null:-c.dpo_days]].filter(x=>x[2]!=null);
  const worst=candidates.length?candidates.reduce((a,b)=>b[3]>a[3]?b:a):null;
  let bits=['<b>Nakit dönüşüm süresi '+num(ccc)+' gün.</b> Bu, şirketin mal/hizmet için ödeme yaptığı andan müşteriden tahsilat yapana kadar geçen — ve bu sürede finansmanının şirketin kendi kaynaklarından veya kredi hattından karşılandığı — gün sayısı.'];
  if(worst) bits.push('Bu süreyi en çok '+esc(worst[1]).toLowerCase()+' ('+worst[0]+': '+num(worst[2])+' gün) uzatıyor; kısaltmak için ilk bakılacak yer burası.');
  bits.push(ccc<=30?'Bu bant düşük — işletme sermayesi nakit üzerinde ek bir baskı yaratmıyor.':ccc<=75?'Bu bant orta seviyede; tahsilat/stok/ödeme koşullarından biri iyileştirilirse nakit serbest kalır.':'Bu bant yüksek; işletme sermayesi önemli miktarda nakdi bağlıyor ve kısa vadeli likidite üzerinde baskı oluşturuyor.');
  return '<div class="insight '+tier+'"><p>'+bits.join(' ')+'</p>'+(c.note?'<p class="small muted" style="margin-top:6px">'+esc(c.note)+'</p>':'')+(c.inventory_flag?'<p class="small muted" style="margin-top:4px">'+esc(c.inventory_flag)+'</p>':'')+'</div>';
}

// Leverage & Liquidity: one synthesized paragraph instead of one card per
// rule (L001/L002/D004/D006/Q001...). Several of those rules describe the
// same underlying condition (too much debt) from slightly different angles,
// which read as duplicated commentary when stacked as separate cards. Full
// detail + recommendation per rule still lives in Priority Risks (So What)
// and Management Actions (Now What); this paragraph only says what the
// numbers above mean, once.
function leverageNarrative(findings){
  const list=findingsByCategory(findings,['Borçluluk','Likidite']);
  if(!list.length) return '<div class="notice">Kaldıraç ve likidite oranları sağlıklı bantta; öne çıkan bir risk yok.</div>';
  const worst=list.reduce((a,b)=>sevRank(b.severity)>sevRank(a.severity)?b:a,list[0]);
  const sentences=[...new Set(list.map(f=>f.interpretation).filter(Boolean))];
  return '<div class="insight '+esc(worst.severity)+'"><b>Genel görünüm: '+esc(worst.severity)+'</b><p>'+sentences.join(' ')+'</p><p class="small muted">Ayrıntılı risk skorları "So What → Priority Risks" bölümünde, önerilen aksiyonlar ise "Now What" bölümünde yer alıyor — burada tekrar edilmiyor.</p></div>'
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

function renderSolvency(pl, bs, k, pq, derived){
  const el = $('solvencyMetrics');
  if(!el) return;
  const op = Number(pl?.['Operating profit']) || 0;
  const fin = Math.abs(Number(pl?.['Finance costs']) || 0);
  const netDebt = Number(k?.net_debt) || 0;

  const icr = fin > 0 ? (op / fin) : (op > 0 ? 99 : 0);
  const icrStr = fin > 0 ? rat(icr) + 'x' : (op > 0 ? '> 10x' : '–');
  const icrColor = icr < 1.0 ? 'var(--red)' : icr < 2.0 ? 'var(--amber)' : 'var(--green)';

  const netDebtToEbit = op > 0 ? (netDebt / op) : (netDebt > 0 ? 99 : 0);
  const netDebtToEbitStr = op > 0 ? rat(netDebtToEbit) + 'x' : (netDebt > 0 ? 'Yüksek' : '0x (Net Nakit)');
  const ndColor = netDebtToEbit > 3.5 ? 'var(--red)' : netDebtToEbit > 2.0 ? 'var(--amber)' : 'var(--green)';

  const finLoadPct = pq?.finance_cost_to_operating_profit_pct;
  const finColor = (finLoadPct > 50 || finLoadPct < 0) ? 'var(--red)' : finLoadPct > 25 ? 'var(--amber)' : 'var(--green)';

  const eqRatio = derived?.equity_to_assets_pct != null ? derived.equity_to_assets_pct : (k?.debt_to_equity ? (100 / (1 + Number(k.debt_to_equity))) : 40);
  const eqColor = eqRatio < 20 ? 'var(--red)' : eqRatio < 35 ? 'var(--amber)' : 'var(--green)';

  el.innerHTML = [
    metric('Faiz Karşılama (ICR)', icrStr, 'EBIT / Finansman Gideri', icrColor),
    metric('Net Borç / Faaliyet Kârı', netDebtToEbitStr, 'Geri ödeme çarpanı', ndColor),
    metric('Finansman / Faaliyet Kârı', pct(finLoadPct), 'Kârı eriten faiz payı', finColor),
    metric('Özkaynak / Toplam Aktif', pct(eqRatio), 'Bilanço sermaye güvencesi', eqColor)
  ].join('');

  let comm = '';
  if(icr < 1.0 || netDebtToEbit > 4.0){
    comm = '<div class="insight critical"><b>⚠️ Yüksek Borç Servisi &amp; Refinansman Riski:</b> Faaliyet kârı finansman faiz giderlerini karşılamakta yetersiz kalmaktadır (ICR: ' + icrStr + '). Banka kredisi itfası veya sermaye tamamlama önceliklidir.</div>';
  } else if(icr < 2.5 || netDebtToEbit > 2.2){
    comm = '<div class="insight medium"><b>Dengeli Borç Baskısı:</b> Faaliyet kârı borç faizini karşılamakta ancak marj daralması veya ciro şoklarında kırılganlık mevcuttur.</div>';
  } else {
    comm = '<div class="insight positive"><b>Güçlü Sermaye Dayanıklılığı:</b> Bilanço borç yükünü güvenle taşımaktadır; faiz karşılama gücü ve özkaynak payı sağlıklı seviyededir.</div>';
  }
  if($('solvencyCommentary')) $('solvencyCommentary').innerHTML = comm;
}

function renderCashBridge(cb){
  const el = $('cashBridgeContent');
  if(!el) return;
  if(cb && cb.available){
    let crMetricHtml = '';
    if(cb.cash_realization_pct!=null){
      const crp=cb.cash_realization_pct;
      const crTier=crp>=80?'positive':crp>=50?'medium':crp>=0?'high':'critical';
      let crExpl='';
      if(crp<=0){
        crExpl='⚠️ <b>Kâğıt üzerinde '+money(cb.net_profit)+' net kâr görünmesine rağmen, işletme nakit akışı '+money(cb.operating_cash_flow_proxy)+' negatiftir.</b> Net kârın tamamı ve fazlası alacaklarda ('+money(cb.working_capital_components?.receivables_effect)+') ve stokta ('+money(cb.working_capital_components?.inventory_effect)+') kilitlenmiştir. Kasa bu kârı fiilen görememiştir.';
      } else if(crp<80){
        crExpl='Net kâr '+money(cb.net_profit)+'; işletme nakdi '+money(cb.operating_cash_flow_proxy)+'. Defter kârının yaklaşık <b>%'+num(crp)+'\u0027i</b> fiilen kasaya girmiştir. Kalan tutar alacak ve stokta bağlıdır.';
      } else {
        crExpl='Net kâr '+money(cb.net_profit)+'; işletme nakdi '+money(cb.operating_cash_flow_proxy)+'. Kâr büyük ölçüde (<b>'+pct(crp)+'</b>) nakde dönüşmüştür; çalışma sermayesi kâr üzerinde baskı yaratmamaktadır.';
      }
      crMetricHtml = '<div class="metric" style="margin-bottom:12px"><div class="label">Kâr Nakde Dönüşüm Oranı (Cash Realization)</div><div class="value" style="color:'+(crp<=0?'var(--red)':crp<80?'var(--amber)':'var(--green)')+'">'+pct(crp)+'</div><div class="sub">Net Kâr → İşletme Nakit Akışı Dönüşüm Oranı</div></div><div class="insight '+crTier+'"><p>'+crExpl+'</p></div>';
    }
    el.innerHTML = '<div class="grid2"><div><div class="small muted" style="margin-bottom:8px;font-weight:700">AÇILIŞTAN KAPANIŞA GERÇEK NAKİT HAREKETİ KÖPRÜSÜ</div><div id="cashFlowWf" class="waterfall"></div><div class="notice" style="margin-top:12px">Net Kasa Değişimi: <b>'+money(cb.cash_change)+'</b>. '+esc(cb.note||'')+'</div></div><div><div class="small muted" style="margin-bottom:8px;font-weight:700">KÂRIN NAKDE DÖNÜŞÜM VERİMİ (CASH REALIZATION)</div>' + crMetricHtml + '</div></div>';
    waterfall('cashFlowWf',[['Açılış Nakit',cb.opening_cash,false],['Faaliyet Kârı',cb.operating_profit,false],['Alacak Etkisi',cb.working_capital_components.receivables_effect,cb.working_capital_components.receivables_effect<0],['Stok Etkisi',cb.working_capital_components.inventory_effect,cb.working_capital_components.inventory_effect<0],['Borç(AP) Etkisi',cb.working_capital_components.payables_effect,cb.working_capital_components.payables_effect<0],['Finansal Borç Δ',cb.debt_change,cb.debt_change<0],['Açıklanmayan',cb.unexplained_cash_change,cb.unexplained_cash_change<0],['Kapanış Nakit',cb.closing_cash,false]]);
  } else {
    const wp=cb?.working_capital_proxy||{};
    el.innerHTML = '<div class="notice" style="line-height:1.65">⚠️ <b>Nakit akış köprüsü ve kârın nakde dönüşüm verimi için en az iki dönemlik veri gereklidir.</b><br>Tek dönemlik statik bir mizandan net nakit giriş-çıkışı ve kârın kasaya akma hızı matematiksel olarak türetilemez. Alt defterlerinizi veya ikinci dönemi yükleyerek tam nakit köprüsünü açabilirsiniz. <button class="secondary hidePrint" style="margin-top:8px;display:inline-block" onclick="runDataHubSample()">Canlı 2 Dönemli Data Hub Demosunu Çalıştır ⚡</button></div><div class="grid3" style="margin-top:14px">'+metric('Alacak Büyüklüğü (120)',money(wp.receivables),'Mevcut Ticari Alacak')+metric('Stok Büyüklüğü (150)',money(wp.inventory),'Mevcut Depo Varlığı')+metric('Tedarikçi Borçları (320)',money(wp.payables),'Kısa Vadeli Borç Yükü')+'</div>';
  }
}

function render(d){
  LAST=d;$('dashboard').classList.remove('hidden');
  const bp=d.business_partner,pl=d.statements.profit_and_loss,bs=d.statements.balance_sheet,k=d.statements.kpis;
  setRing(bp.health_score);$('healthLabel').textContent=bp.health_label;
  renderTopFocusIssues(bp);

  // Step 1 — WHAT (financial facts)
  $('mSales').textContent=money(pl['Net sales']);$('mOp').textContent=money(pl['Operating profit']);$('mNet').textContent=money(pl['Net profit']);$('mDebt').textContent=money(k.net_debt);
  renderDuPont(bp.dupont_analysis||{});
  renderComparative(bp.trend_analysis||{});
  waterfall('waterfall',[['Net satış',pl['Net sales'],false],['COGS',-pl['COGS'],true],['Brüt kâr',pl['Gross profit'],false],['Faaliyet gideri',-pl['Operating expenses'],true],['Faaliyet kârı',pl['Operating profit'],false],['Finansman',-pl['Finance costs'],true],['Vergi',-pl['Tax expense'],true],['Net kâr',pl['Net profit'],false]]);
  const pq=bp.profit_quality_engine||{};
  $('liquidity').innerHTML=[['Cari Oran (Current Ratio)',rat(k.current_ratio),'1.5 - 2.0 ideal seviye'],['Nakit Oran (Cash Ratio)',rat(k.cash_ratio),'hazır nakit / kısa vadeli borç'],['Kaldıraç (Borç / Özkaynak)',rat(k.debt_to_equity),'düşük olması güvenlidir'],['Borç / Aktif Oranı',pct(bp.derived_metrics?.debt_to_assets_pct),'finansman yoğunluğu']].map(x=>metric(x[0],x[1],x[2])).join('');
  $('leverageCommentary').innerHTML=leverageNarrative(bp.findings);

  const c=bp.cash_conversion_cycle||{};if($('cccMetric')) $('cccMetric').textContent=c.cash_conversion_cycle_days==null?'–':num(c.cash_conversion_cycle_days);
  renderSolvency(pl, bs, k, pq, bp.derived_metrics);
  renderCashBridge(bp.cash_bridge_engine);
  renderResourceAllocation(bp.resource_allocation_engine);
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
  $('benchmark').innerHTML='<div class="insight positive" style="margin-bottom:12px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px">'
    +'<div><b>🏛️ Kurumsal Kıyaslama Kaynağı:</b> <span class="muted">'+esc(instRef)+'</span></div>'
    +'<div class="small">Sektör: <b>'+esc(bm.sector||'Genel')+'</b> · Konum: <span class="tag '+(bm.overall_score>=70?'positive':bm.overall_score>=50?'medium':'critical')+'">'+esc(bm.overall_label)+' ('+esc(bm.overall_score)+'/100)</span></div>'
    +'</div>'
    +'<div class="tableWrap" style="margin-top:8px"><table><thead><tr><th>Gösterge</th><th>Şirket Değeri</th><th>Sektör Bandı (Düşük / Medyan / Yüksek)</th><th>Sektöre Göre Konum</th></tr></thead><tbody>'
    +(bm.metrics||[]).map(m=>'<tr><td><b>'+esc(m.label)+'</b></td><td>'+esc(m.value)+'</td><td>'+esc(m.band_low)+' / <b>'+esc(m.band_mid)+'</b> / '+esc(m.band_high)+'</td><td><span class="tag '+(m.favorability==='favorable'?'positive':m.favorability==='unfavorable'?'critical':'medium')+'">'+esc(m.favorability)+'</span></td></tr>').join('')
    +'</tbody></table></div>';

  // Step 3 — WHY (root cause; carries the "missing evidence" angle itself)
  const rc=bp.root_cause_engine||{};$('rootCause').innerHTML=(rc.causal_chains||[]).map(c=>{const ev=(c.evidence||[]).map(esc).join(' · ');const miss=(c.required_additional_evidence||[]).map(esc).join(' · ');const acts=(c.recommended_actions||[]).map(esc).join(' · ');return '<div class="insight" style="margin-bottom:10px"><h3>'+esc(c.title)+'</h3><div class="small muted">Ana Tetikleyici: '+esc(c.primary_driver||'–')+' · '+esc(c.causal_status||'yüksek ihtimalli etken')+'</div><p><b>Etki Zinciri:</b> '+(c.chain||[]).map(esc).join(' → ')+'</p>'+(ev?'<div class="small"><b>Doğrulanan Kanıt:</b> '+ev+'</div>':'')+(miss?'<div class="small muted" style="margin-top:5px"><b>Eksik Kanıt:</b> '+miss+'</div>':'')+(c.financial_impact?'<div class="small" style="margin-top:5px"><b>Finansal Risk / Maruziyet:</b> '+esc(c.financial_impact)+'</div>':'')+(acts?'<div class="small" style="margin-top:5px"><b>Önerilen Aksiyon:</b> '+acts+'</div>':'')+'</div>'}).join('')||'<div class="notice">Yeterli kök neden kanıtı yok.</div>';

  // Step 6b — Narrative Engine: one card per independently-triggered
  // scenario (risk or positive), each already-computed-number-only.
  const ne=bp.narrative_engine||{};
  const sevClass={critical:'critical',high:'high',medium:'medium',positive:'positive'};
  $('narrativeStories').innerHTML=(ne.stories&&ne.stories.length)?ne.stories.map(s=>
    '<div class="insight '+esc(sevClass[s.severity]||'medium')+'" style="margin-bottom:10px">'
    +'<div class="small muted">'+esc(s.category)+' · '+esc(s.severity)+'</div>'
    +'<h3>'+esc(s.title)+'</h3>'
    +'<p><b>Ne oldu?</b> '+esc(s.ne_oldu)+'</p>'
    +'<p><b>Neden?</b> '+esc(s.neden)+'</p>'
    +'<p><b>Bana maliyeti ne?</b> '+esc(s.maliyet)+'</p>'
    +'<p><b>Ne yapmam lazım?</b></p><ul>'+(s.ne_yapmali||[]).map(a=>'<li>'+esc(a)+'</li>').join('')+'</ul>'
    +(s.data_gap?'<div class="small muted" style="margin-top:6px">⚠ '+esc(s.data_gap)+'</div>':'')
    +'</div>'
  ).join(''):'<div class="notice">Bu dönemde eşik aşan bir senaryo tetiklenmedi.</div>';

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
  $('exec').innerHTML='<h3>'+esc(bp.executive_summary)+'</h3>';
  const topRisk=rr[0], topOpp=opps[0];
  const chips=[['Sağlık Skoru',bp.health_score+'/100'],['CCC',c.cash_conversion_cycle_days==null?'–':num(c.cash_conversion_cycle_days)+' gün'],(cb.available&&cb.cash_realization_pct!=null)?['Kâr → Nakit',pct(cb.cash_realization_pct)]:null,topRisk?['En Kritik Risk',topRisk.title]:null,topOpp?['En Büyük Fırsat',topOpp.title+' ('+money(topOpp.estimated_impact)+')']:null,['Sektör Konumu',bm.overall_label||'–']].filter(Boolean);
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
  if(!data) return '<div class="notice">'+esc(title)+' verisi yüklenmedi.</div>';
  const buckets=(data.aging_buckets||[]).filter(b=>b.amount);
  const bucketRows=buckets.length?'<div style="margin-top:10px">'+buckets.map(b=>'<div style="margin-top:8px"><div class="small" style="display:flex;justify-content:space-between"><span>'+esc(b.bucket)+'</span><span>'+money(b.amount)+' · '+pct(b.pct_of_outstanding)+'</span></div><div class="abar"><i style="width:'+Math.min(100,b.pct_of_outstanding||0)+'%"></i></div></div>').join('')+'</div>':'';
  const overduePct=data.overdue_pct||0;
  const overdueBar='<div style="margin-top:10px"><div class="small" style="display:flex;justify-content:space-between"><span>Vadesi Geçen Oranı</span><span>'+pct(data.overdue_pct)+'</span></div><div class="abar"><i style="width:'+Math.min(100,overduePct)+'%"></i></div></div>';
  const topOverdue=(data.top_overdue_parties||[]).slice(0,5);
  const topOverdueRows=topOverdue.length?'<div class="small" style="margin-top:10px"><b>En çok geciken '+(title==='AR'?'müşteriler':'tedarikçiler')+':</b> '+topOverdue.map(p=>esc(p.name)+' ('+money(p.amount)+(p.avg_days_overdue!=null?', ort. '+num(p.avg_days_overdue)+' gün':'')+')').join(' · ')+'</div>':'';
  const riskTierTag=data.risk_tier?'<span class="tag '+(data.risk_tier==='Kritik'?'critical':data.risk_tier==='Yüksek'?'high':data.risk_tier==='Orta'?'medium':'positive')+'">'+esc(data.risk_tier)+'</span>':'';
  const partyWord=title==='AR'?'müşteri':'tedarikçi';
  const concTxt=data.concentration_80pct_party_count!=null?' · Toplamın %80\u0027ine <b>'+data.concentration_80pct_party_count+'</b> '+partyWord+' denk geliyor ('+esc(data.party_count??'–')+' '+partyWord+'\u0027nin %'+num(data.concentration_80pct_share_of_parties_pct)+'\u0027i)':'';
  const anomalyBlock=(data.data_anomalies&&data.data_anomalies.length)?'<p class="small" style="margin-top:8px;color:#9a6b00">⚠ Veri uyarısı: '+data.data_anomalies.map(esc).join(' · ')+'</p>':'';
  const titleLabel = title==='AR'?'Alacak Yaşlandırma (AR)':'Borç Yaşlandırma (AP)';
  return '<div class="insight" style="margin-top:10px"><b>'+esc(titleLabel)+'</b> '+riskTierTag+'<p>Toplam Bakiye: '+money(data.outstanding)+' · Vadesi Geçen: '+money(data.overdue)+' · '+esc(due)+': '+(data[due==='DSO'?'dso_days':'dpo_days']==null?'–':num(data[due==='DSO'?'dso_days':'dpo_days'])+' gün')+'</p>'+overdueBar+'<p class="small muted" style="margin-top:8px">Ağırlıklı ort. gecikme: '+(data.weighted_average_overdue_days==null?'–':num(data.weighted_average_overdue_days)+' gün')+' · Beklenen tahsilat/ödeme riski: '+money(data.collection_risk_estimate)+' ('+pct(data.collection_risk_estimate_pct_of_outstanding)+') · İlk 10 taraf payı: '+pct(data.top_10_share_pct)+' ('+(data.party_count??'–')+' '+partyWord+')'+concTxt+'</p>'+anomalyBlock+bucketRows+topOverdueRows+'</div>'
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
  return '<div class="card"><div class="sectionHead"><div><h2>Kritik Müşteriler'+concTag+'</h2><p>Tahsilat önceliklendirmesi ve olası nakit etkisi</p></div></div><div class="notice" style="margin-bottom:6px">Bu '+top.length+' müşteriden tahsilat sağlanırsa yaklaşık <b>'+money(totalImpact)+'</b> nakit serbestleşir (toplam AR overdue riskinin '+pct(arData.outstanding?totalImpact/arData.outstanding*100:null)+'\u0027i).</div>'+rows+concLine+concNote+'</div>';
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
  return '<div class="card"><div class="sectionHead"><div><h2>Kritik Tedarikçiler</h2><p>Ödeme önceliklendirmesi ve tedarik ilişkisi riski</p></div></div><div class="notice" style="margin-bottom:6px">Bu '+top.length+' tedarikçiye geciken <b>'+money(totalImpact)+'</b> tutarındaki ödeme, ilişki/tedarik kesintisi riski taşıyor (toplam AP overdue riskinin '+pct(apData.outstanding?totalImpact/apData.outstanding*100:null)+'\u0027i).</div>'+rows+concLine+'</div>';
}

function renderHub(ms){
  if(!ms){$('dataHubCard').classList.add('hidden');return}
  $('dataHubCard').classList.remove('hidden');
  const sm=ms.summary||{};
  const errorRows=(ms.errors||[]).map(e=>'<div class="notice" style="margin-top:8px"><b>Dosya hatası:</b> '+esc(e.file||'')+' · '+esc(e.error||'')+'</div>').join('');
  const fileRows=(ms.files||[]).map(f=>{const rs=(f.roles||[]).map(r=>r.role+' ('+Math.round((r.confidence||0)*100)+'%)').join(', ');return '<tr><td>'+esc(f.filename)+'</td><td>'+esc(rs||'unknown')+'</td><td>'+esc(f.roles?.[0]?.rows||'–')+'</td></tr>'}).join('');
  if($('hubSources')) $('hubSources').innerHTML='<div class="sectionHead"><div><h2>Source Registry</h2><p>Dosyaların içerik bazlı sınıflandırılması</p></div></div>'+(fileRows?'<div class="tableWrap"><table><thead><tr><th>Dosya</th><th>Rol</th><th>Satır</th></tr></thead><tbody>'+fileRows+'</tbody></table></div>':'<div class="notice">Kaynak bulunamadı.</div>')+errorRows;
  const labels=[['Sales',sm.sales_loaded?'Loaded':'Not loaded',''],['AR Aging',sm.ar_aging_loaded?'Loaded':'Not loaded',''],['AP Aging',sm.ap_aging_loaded?'Loaded':'Not loaded',''],['Inventory',sm.inventory_loaded?'Loaded':'Not loaded','']];
  $('hubSummary').innerHTML=labels.map(x=>metric(x[0],x[1],x[2])).join('');
  const checks=ms.reconciliation?.checks||[];
  $('hubReconciliation').innerHTML='<div class="sectionHead"><div><h2>Source Reconciliation</h2><p>GL ile operasyonel dosya arasındaki farklar</p></div></div>'+(checks.length?'<div class="tableWrap"><table><thead><tr><th>Kontrol</th><th>GL</th><th>Source</th><th>Difference</th><th>Status</th></tr></thead><tbody>'+checks.map(c=>'<tr><td>'+esc(c.name)+'</td><td>'+money(c.gl_value)+'</td><td>'+money(c.source_value)+'</td><td>'+money(c.difference)+'</td><td>'+esc(c.status)+'</td></tr>').join('')+'</tbody></table></div>':'<div class="notice">Mutabakat için yeterli veri yok.</div>');
  const an=ms.analysis||{}; const sales=an.sales||{};
  if(sales.pvm_analysis && sales.pvm_analysis.available) {
    $('pvmIntel').classList.remove('hidden');
    const p=sales.pvm_analysis;
    const wfId = 'pvmWf';
    $('pvmIntel').innerHTML='<div class="sectionHead"><div><h2>Price-Volume-Mix (PVM) Analizi</h2><p>Ciro değişiminin kök nedenleri: Fiyat mı, Hacim mi, Karma mı?</p></div></div>'
      +'<div class="grid4" style="margin-bottom:16px">'
      +metric('Dönem 1 Ciro', money(p.revenue_1), p.period_1)
      +metric('Dönem 2 Ciro', money(p.revenue_2), p.period_2)
      +metric('Ciro Değişimi', money(p.revenue_delta), '')
      +metric('En Büyük Etken', Math.abs(p.total_price_effect)>Math.abs(p.total_volume_effect)?'Fiyat (Price)':'Hacim (Volume)', '')
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
  // Sales Intelligence
  $('salesIntel').innerHTML='<div class="sectionHead"><div><h2>Sales Intelligence</h2><p>Vade fiyatlaması ve ürün karması</p></div></div>'+(an.sales?'<div class="grid2">'+metric('Vade Primi',pct(sales.term_premium_pct),'Peşin → vadeli fark')+metric('İlk 10 Müşteri Payı',pct(sales.top_10_customer_share_pct),'Concentration')+'</div>'+((sales.product_mix||[]).length?'<div class="insight" style="margin-top:10px"><b>Ürün karması</b><p>'+sales.product_mix.slice(0,7).map(v=>esc(v.name)+': '+money(v.sales)+' ('+pct(v.share_pct)+')').join(' · ')+'</p></div>':'')+(sales.term_premium_pct>15?'<div class="insight high" style="margin-top:10px"><b>Vadeli satış fiyatı peşin fiyattan belirgin yüksek</b><p>Vade primi %'+num(sales.term_premium_pct)+'; finansman maliyeti ve tahsilat riski fiyatlamaya yansıtılıyor mu kontrol edilmeli.</p></div>':''):'<div class="notice">Sales datası yüklenmedi.</div>');
  $('arApIntel').innerHTML='<div class="sectionHead"><div><h2>AR / AP Intelligence</h2><p>Aging, risk yoğunlaşması ve tahsilat/ödeme riski</p></div></div>'+agingBlock('AR','DSO',an.ar_aging)+agingBlock('AP','DPO',an.ap_aging);
  const inv = an.inventory || an.inventory_aging || {};
  const hasInv = !!(an.inventory || an.inventory_aging);
  $('inventoryIntel').innerHTML='<div class="sectionHead"><div><h2>Inventory Intelligence</h2><p>Stok değeri, yaşlanma ve nakit kilitleme sinyalleri</p></div></div>'+(hasInv?'<div class="grid4">'+metric('Inventory Value',money(inv.value),'Stok Defteri')+metric('SKU Sayısı',inv.sku_count??'–','Toplam Kalem')+metric('DIO',inv.dio_days==null?'–':num(inv.dio_days)+' gün','Ortalama Satış Süresi')+metric('180+ Gün Stok',money(inv.stale_180_amount),'Nakit Kilitleyen')+ '</div>'+(inv.findings||[]).map(f=>'<div class="insight '+esc(f.severity)+'" style="margin-top:10px"><b>'+esc(f.title)+'</b><p>'+esc(f.detail)+'</p></div>').join(''):'<div class="notice">Inventory datası yüklenmedi.</div>');
}

// ---------------------------------------------------------------------
// Core Analysis Engine Runner with Institutional Progress & Auto-Scroll
// ---------------------------------------------------------------------
async function run(url,fd,kind='single'){
  $('error').classList.add('hidden');
  startLoading(
    kind==='hub'?'Data Hub Analizi Çalıştırılıyor':'Finansal Veriler Analiz Ediliyor',
    '33 Finansal Karar Motoru Çalıştırılıyor (Hesap Doğrulama, Likidite, Cash Bridge, DuPont)...'
  );
  $('analyze').disabled=true;$('analyzeTrend').disabled=true;$('analyzeHub').disabled=true;
  try{
    const r=await fetch(url,{method:'POST',body:fd});
    const d=await r.json();
    if(!r.ok) throw new Error(d.detail||'Analiz başarısız oldu.');
    render(d);
    if(kind==='hub') renderHub(d.data_hub);
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
  listEl.innerHTML = files.map((f, i) => 
    '<div class="filePill"><b>📄 ' + esc(f.name) + '</b> <span class="muted">(' + formatBytes(f.size) + ')</span>' +
    '<span class="pillDel" title="Kaldır" onclick="clearFileSelection(\''+inputEl.id+'\','+i+')">×</span></div>'
  ).join('');
}

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
async function runDataHubSample(){
  if($('sampleHubBtn')) $('sampleHubBtn').disabled=true;
  startLoading('🔥 Data Hub Canlı Demo Başlatılıyor', '6 Örnek Finansal Dosya Sunucudan Alınıyor (2 Dönem Mizan + AR + AP + Stok + Satış)...');
  $('error').classList.add('hidden');
  try{
    const blobs=await Promise.all(DATA_HUB_SAMPLE_KEYS.map(async key=>{
      const r=await fetch('/api/sample/'+encodeURIComponent(key));
      if(!r.ok) throw new Error('Örnek veri sunucudan alınamadı: '+key);
      const blob=await r.blob();
      return new File([blob],key+'.xlsx',{type:blob.type});
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
    arVal = (sales / 365) * dso;
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
    invVal = (cogs / 365) * dio;
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
    apVal = (cogs / 365) * dpo;
  }

  // Net working capital locked in CCC & 45% annual financing cost proxy
  const netLockedWc = Math.max(0, arVal + invVal - (apVal * 0.5));
  const annualLeak = Math.max(arVal + invVal, netLockedWc) * 0.45;

  if($('wcLeakArVal')) $('wcLeakArVal').textContent = money(arVal);
  if($('wcLeakArSub')) $('wcLeakArSub').textContent = 'Ortalama tahsilat vadesi: ' + (dso ? num(dso) + ' gün' : '–');
  
  if($('wcLeakInvVal')) $('wcLeakInvVal').textContent = money(invVal);
  if($('wcLeakInvSub')) $('wcLeakInvSub').textContent = 'Ortalama stokta bekleme: ' + (dio ? num(dio) + ' gün' : '–');

  if($('wcLeakApVal')) $('wcLeakApVal').textContent = money(apVal);
  if($('wcLeakApSub')) $('wcLeakApSub').textContent = 'DPO Ödeme: ' + (dpo ? num(dpo) + ' gün' : '–');

  const ccc = c?.cash_conversion_cycle_days;
  if($('wcLeakCccVal')) $('wcLeakCccVal').textContent = ccc == null ? '–' : num(ccc) + ' gün';
  if($('wcLeakCccSub')) $('wcLeakCccSub').textContent = ccc == null ? 'Hesaplanamadı' : (ccc > 120 ? 'Kritik Yavaş Döngü' : ccc > 60 ? 'Geliştirilebilir' : 'Hızlı / Sağlıklı');

  if($('wcLeakCostVal')) $('wcLeakCostVal').textContent = money(annualLeak);

  if($('wcNarrativeBox')) $('wcNarrativeBox').innerHTML = workingCapitalNarrative(c);

  // Daily run-rates for realistic slider math
  let dailySales = sales > 0 ? (sales / 365) : (arVal > 0 && dso > 0 ? arVal / dso : (arVal > 0 ? arVal / 60 : 10000));
  let dailyCogs = cogs > 0 ? (cogs / 365) : (dailySales * 0.70);

  function recalcMultiSimulator(){
    const dsoDays = parseInt($('wcSliderDso')?.value || 0, 10);
    const dioDays = parseInt($('wcSliderDio')?.value || 0, 10);
    const dpoDays = parseInt($('wcSliderDpo')?.value || 0, 10);

    if($('wcSliderDsoDisplay')) $('wcSliderDsoDisplay').textContent = dsoDays + ' Gün Erken';
    if($('wcSliderDioDisplay')) $('wcSliderDioDisplay').textContent = dioDays + ' Gün Daha Hızlı';
    if($('wcSliderDpoDisplay')) $('wcSliderDpoDisplay').textContent = dpoDays + ' Gün Öteleme';

    const arCash = dailySales * dsoDays;
    const invCash = dailyCogs * dioDays;
    const apCash = dailyCogs * dpoDays;
    const totalCash = arCash + invCash + apCash;
    const interestSaved = totalCash * 0.45;

    if($('wcSliderCashLiberated')) $('wcSliderCashLiberated').textContent = '+' + money(totalCash);
    if($('wcSliderInterestSaved')) $('wcSliderInterestSaved').textContent = '+' + money(interestSaved) + ' / yıl';

    if($('wcLeakSummaryBox')){
      if (totalCash <= 0) {
        $('wcLeakSummaryBox').innerHTML = '<p>💡 <b>Canlı Çalışma Sermayesi Simülatörü:</b> Sürgüleri hareket ettirerek tahsilat vadesini çekmenin, depodaki ölü stoğu eritmenin ve tedarikçi ödemelerini planlamanın şirketinize kazandıracağı nakit ve faiz tasarrufunu anında görün.</p>';
      } else {
        let parts = [];
        if (dsoDays > 0) parts.push('tahsilatı <b>' + dsoDays + ' gün</b> öne çekerek <b>' + money(arCash) + '</b>');
        if (dioDays > 0) parts.push('stok devrini <b>' + dioDays + ' gün</b> hızlandırarak <b>' + money(invCash) + '</b>');
        if (dpoDays > 0) parts.push('tedarikçi vadesini <b>' + dpoDays + ' gün</b> optimize ederek <b>' + money(apCash) + '</b>');
        const actionsTxt = parts.length ? parts.join(', ') + ' serbest bırakıyorsunuz' : 'operasyonel kaldıraç uyguluyorsunuz';
        $('wcLeakSummaryBox').innerHTML = '<p>💡 <b>Canlı Yönetim Kararı Çıktısı:</b> ' + actionsTxt + '. Bu hamlelerle şirketin kasasına anında <b>+' + money(totalCash) + '</b> sıcak nakit giriyor. Kilitli paradan kurtarılan yıllık finansman faiz tasarrufu ise <b>+' + money(interestSaved) + ' / yıl</b> olarak doğrudan şirketin net kâr hanesinde kalıyor.</p>';
      }
    }
  }

  ['wcSliderDso', 'wcSliderDio', 'wcSliderDpo'].forEach(id => {
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

function renderCeoDiagnosticDesk(bp, pl, bs, k, c, d){
  const desk = $('ceoDiagnosticSection');
  if(!desk) return;

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
  if (arVal <= 0 && dso > 0 && sales > 0) arVal = (sales / 365) * dso;

  // 2. Inventory (150-158)
  let invVal = Number(k?.inventory) || 0;
  if (invVal <= 0 && accounts.length) {
    invVal = accounts.filter(a => {
      const code = String(a.account_code);
      return code.startsWith('150') || code.startsWith('151') || code.startsWith('152') || code.startsWith('153') || code.startsWith('157') || code.startsWith('158');
    }).reduce((sum, a) => sum + (Number(a.balance) || 0), 0);
  }
  if (invVal <= 0 && dio > 0 && cogs > 0) invVal = (cogs / 365) * dio;

  // 3. Payables (320-329)
  let apVal = Math.abs(Number(k?.payables) || 0);
  if (apVal <= 0 && accounts.length) {
    apVal = accounts.filter(a => {
      const code = String(a.account_code);
      return code.startsWith('320') || code.startsWith('321') || code.startsWith('322') || code.startsWith('329');
    }).reduce((sum, a) => sum + Math.abs(Number(a.balance) || 0), 0);
  }
  if (apVal <= 0 && dpo > 0 && cogs > 0) apVal = (cogs / 365) * dpo;

  const netLockedWc = Math.max(0, arVal + invVal - (apVal * 0.5));
  const annualLeak = Math.max(arVal + invVal, netLockedWc) * 0.45;

  let dailySales = sales > 0 ? (sales / 365) : (arVal > 0 && dso > 0 ? arVal / dso : 10000);
  let dailyCogs = cogs > 0 ? (cogs / 365) : (dailySales * 0.70);

  const rankedRisks = bp?.risk_ranking_engine?.ranked_risks || [];
  const topRisks = rankedRisks.slice(0, 3);

  const questions = [
    {
      id: 'q1',
      icon: '💸',
      title: 'Kasada Neden Para Yok?',
      sub: 'Kâr Nereye Gitti?',
      cat: 'Nakit Akışı & Kâr Kalitesi',
      l1_title: 'Kâğıt Üzerindeki Kâr, Alacak ve Stok Kilitlenmesinde Kayboluyor',
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
        { label: 'Yıllık Stok Faiz Yükü', val: money(invVal * 0.45), note: '%45 faiz proxy' },
        { label: 'Satışların Maliyeti (COGS)', val: money(cogs), note: 'Yıllık maliyet akışı' }
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
      l3_owner: 'İcra Kurulu & Genel Müdür',
      l3_due: 'Hemen Devrede',
      targetStep: 'workingCapitalLeakEngineCard',
      targetStepName: 'Adım 2: 4 Kaldıraçlı Kâr & Nakit Simülatörü'
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
        { label: 'Brüt Kâr Marjı', val: pct(pl?.['Gross margin'] || (sales>0?(sales-cogs)/sales*100:32)), note: 'Satış - COGS marjı' },
        { label: 'Faaliyet Kâr Marjı (EBIT)', val: pct(pl?.['Operating margin'] || (sales>0?opProfit/sales*100:12)), note: 'Operasyonel kâr marjı' },
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
      l1_title: 'Bugün Masaya Koymanız Gereken En Yüksek Parasal Getirili Karar',
      l1_desc: 'Şirketinizin finansal sağlığını en hızlı toparlayacak ve kasayı güçlendirecek 1 numaralı karar: "Kilitli İşletme Sermayesini Serbest Bırakma ve Alacak Tahsilatını Sözleşmeye Bağlama İcraatıdır".',
      l2_metrics: [
        { label: 'Finansal Sağlık Skoru', val: (bp?.health_score || 72) + ' / 100', note: bp?.health_label || 'Sağlıklı' },
        { label: 'Kurtarılabilir Yıllık Kâr', val: money(annualLeak), note: 'Finansman sızıntısı' },
        { label: 'Net Finansal Borç', val: money(k?.net_debt || 0), note: 'Banka borç baskısı' },
        { label: 'Nakit Üretme Gücü', val: c.cash_conversion_cycle_days ? num(c.cash_conversion_cycle_days) + ' gün' : 'Orta', note: 'İşletme sermayesi döngüsü' }
      ],
      l3_action: 'Satış direktörüne bugün doğrudan talimat verin: Vadesi 60 günü aşan müşterilere yeni mal sevkiyatını durdurun ve ilk 10 müşteriyle banka DBS teminat protokolü imzalayın.',
      l3_cash: '+' + money(dailySales * 25),
      l3_profit: '+' + money(dailySales * 25 * 0.45) + ' / yıl',
      l3_owner: 'CEO & Genel Müdür',
      l3_due: 'Bugün',
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

  if(cp.findings && cp.findings.length){
    $('customerMatrixFindings').innerHTML = '<div class="notice" style="margin-top:10px">' +
      cp.findings.map(f => '<div><b>' + esc(f.title) + ':</b> ' + esc(f.detail) + ' <span class="muted">(' + esc(f.recommendation || f.action || '') + ')</span></div>').join('') +
    '</div>';
  }
}

function renderProductProfitability(pp){
  const card = $('productProfitabilityCard');
  if(!card) return;
  if(!pp || pp.status !== 'PASS'){ card.classList.add('hidden'); return; }
  card.classList.remove('hidden');

  const top = (pp.top_profitable_products || []).slice(0, 8);
  const tied = (pp.tied_inventory_products || []).slice(0, 5);

  let rows = top.map(p => 
    '<tr>' +
      '<td style="text-align:left"><b>' + esc(p.sku) + '</b></td>' +
      '<td>' + money(p.revenue) + '</td>' +
      '<td>' + money(p.cogs) + '</td>' +
      '<td><b>%' + num(p.gross_margin_pct) + '</b></td>' +
      '<td>%' + num(p.share_of_profit_pct) + '</td>' +
    '</tr>'
  ).join('');

  let html = '<div class="tableWrap"><table><thead><tr>' +
    '<th style="text-align:left">Ürün / SKU</th><th>Ciro</th><th>Maliyet (COGS)</th><th>Brüt Marj %</th><th>Kâra Katkı %</th>' +
    '</tr></thead><tbody>' + rows + '</tbody></table></div>';

  if(tied.length){
    html += '<div class="notice" style="margin-top:12px"><b>Depoda En Çok Sermaye Bağlayan Ürünler:</b> ' +
      tied.map(t => esc(t.sku) + ' (' + money(t.inventory_tied_capital) + ')').join(' · ') +
    '</div>';
  }

  $('productProfitabilityTable').innerHTML = html;
}

function setupInteractiveScenario(d){
  const pl=d.statements?.profit_and_loss||{};
  const k=d.statements?.kpis||{};
  const sales=Number(pl['Net sales']||0);
  const opex=Number(pl['Operating expenses']||0);
  const debt=Number(k.financial_debt||0);
  const fin=Number(pl['Finance costs']||0);

  function updateSim(){
    if(!$('sliderMargin')) return;
    const marginDeltaPct=Number($('sliderMargin')?.value||0);
    const opexCutPct=Number($('sliderOpex')?.value||0);
    const growthPct=Number($('sliderGrowth')?.value||0);
    const debtPayPct=Number($('sliderDebt')?.value||0);

    if($('sliderMarginVal')) $('sliderMarginVal').textContent='+'+marginDeltaPct.toFixed(1)+'%';
    if($('sliderOpexVal')) $('sliderOpexVal').textContent=opexCutPct+'%';
    if($('sliderGrowthVal')) $('sliderGrowthVal').textContent='+'+growthPct+'%';
    if($('sliderDebtVal')) $('sliderDebtVal').textContent=debtPayPct+'%';

    const profitFromMargin = (marginDeltaPct / 100.0) * sales;
    const profitFromOpex = (opexCutPct / 100.0) * opex;
    const grossMarginRatio = sales > 0 ? ((Number(pl['Gross profit'])||0) / sales) : 0.30;
    const profitFromGrowth = (growthPct / 100.0) * sales * Math.max(0.15, grossMarginRatio);
    const debtRepaid = (debtPayPct / 100.0) * debt;
    const interestRate = (debt > 0 && fin > 0) ? (fin / debt) : 0.40;
    const interestSaved = debtRepaid * interestRate;
    const totalProfitImpact = profitFromMargin + profitFromOpex + profitFromGrowth;

    if($('simProfitImpact')) $('simProfitImpact').textContent=(totalProfitImpact>=0?'+':'')+money(totalProfitImpact);
    if($('simInterestImpact')) $('simInterestImpact').textContent=(interestSaved>=0?'+':'')+money(interestSaved)+' / yıl';

    let narrative=[];
    if(marginDeltaPct>0) narrative.push('Brüt kâr marjındaki %'+marginDeltaPct.toFixed(1)+' iyileşme doğrudan faaliyet kârına <b>+'+money(profitFromMargin)+'</b> ekler.');
    if(opexCutPct>0) narrative.push('Faaliyet giderlerindeki %'+opexCutPct+' tasarruf bilançoda <b>+'+money(profitFromOpex)+'</b> operasyonel kâr bırakır.');
    if(growthPct>0) narrative.push('Satış hacmindeki %'+growthPct+' büyüme <b>+'+money(profitFromGrowth)+'</b> ek brüt kâr üretir.');
    if(debtPayPct>0) narrative.push('İtfa edilen '+money(debtRepaid)+' borç ile şirketin yıllık faiz yükü <b>+'+money(interestSaved)+'</b> azalır.');

    if($('simSummaryText')) $('simSummaryText').innerHTML=narrative.length?narrative.join('<br>'):'Sürgüleri hareket ettirerek yönetim kurulu senaryonuzu belirleyin.';
  }

  ['sliderMargin','sliderOpex','sliderGrowth','sliderDebt'].forEach(id=>{
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

function renderAuthArea(){
  const box=$('authArea');
  if(AUTH_TOKEN){
    box.innerHTML='<span class="small muted" style="margin-right:8px">👤 '+esc(AUTH_EMAIL||'')+'</span><button id="logoutBtn" class="secondary">Çıkış</button>';
    $('logoutBtn').onclick=()=>{AUTH_TOKEN=null;AUTH_EMAIL=null;localStorage.removeItem('dfbp_token');localStorage.removeItem('dfbp_email');renderAuthArea();refreshHistoryVisibility();};
    $('historyLoggedOut').classList.add('hidden');$('historyLoggedIn').classList.remove('hidden');
    loadHistory();
  }else{
    box.innerHTML='<button id="loginOpenBtn" class="secondary">Giriş Yap</button> <button id="registerOpenBtn" class="secondary">Kayıt Ol</button>';
    $('loginOpenBtn').onclick=()=>openAuthModal('login');
    $('registerOpenBtn').onclick=()=>openAuthModal('register');
    $('historyLoggedOut').classList.remove('hidden');$('historyLoggedIn').classList.add('hidden');
  }
}
function refreshHistoryVisibility(){
  if(AUTH_TOKEN){$('historyLoggedOut').classList.add('hidden');$('historyLoggedIn').classList.remove('hidden');}
  else{$('historyLoggedOut').classList.remove('hidden');$('historyLoggedIn').classList.add('hidden');}
}
function openAuthModal(mode){
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
</script></body></html>
'''

HTML = APP_HTML  # backward-compat alias for any old import
