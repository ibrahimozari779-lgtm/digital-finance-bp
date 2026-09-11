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
.marketingSection{padding:60px 0}
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
.navBtns a.secondary,.navBtns a.primary{text-decoration:none;display:inline-flex;align-items:center;font-weight:700}
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
.secBlock{padding:58px 0}
.secBlock.tint{background:linear-gradient(180deg,rgba(16,31,51,.55),rgba(10,23,39,.15));border-radius:32px;margin:0 -10px}
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
.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

</style></head>
<body>
<header class="top"><div class="wrap brand"><div><a href="/" style="text-decoration:none;color:inherit"><h1>Digital Finance Business Partner</h1><p>Verified financial facts → decision intelligence → management action</p></a></div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/" class="active">Anasayfa</a><a href="/paketler">Paketler</a><a href="/hakkimizda">Hakkımızda</a><a href="/iletisim">İletişim</a><a href="/guvenlik">Güvenlik</a><a href="/uygulama">Uygulama</a></nav><span class="badge v">Finance Core v__APP_VERSION__</span><div class="navBtns"><a href="/uygulama?auth=login" class="secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="primary">Ücretsiz Kayıt Ol</a></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<section class="mHero">
  <div class="reveal in">
    <span class="eyebrow">The Executive Intelligence Layer for Finance</span>
    <h1>Yönetim Kurulu İçin <span>Finansal Karar Motoru</span></h1>
    <p class="lead">Mizanınızı yükleyin. Sistem finansal verileri doğrulasın, kök nedenleri analiz etsin, riskleri ortaya çıkarsın ve yönetim aksiyonlarını oluştursun. <b style="color:var(--text)">2 dakikada.</b></p>
    <div class="ctaRow"><a href="/uygulama?sample=1" class="primary" style="padding:13px 22px;border-radius:12px">Executive Demo</a><a href="#journey" class="secondary" style="padding:13px 22px;border-radius:12px">Platform Tour</a></div>
    <div class="miniTrust">
      <span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>Önce hesap, sonra yorum</span>
      <span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>KVKK uyumlu, kalıcı saklama yok</span>
      <span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 5-8"/></svg>33 analiz motoru</span>
    </div>
  </div>
  <div class="heroArt reveal in">
    <div class="heroDash">
      <div class="dHead">
        <div class="dots"><span style="background:#C22A3E"></span><span style="background:#B4720A"></span><span style="background:#0E7C66"></span></div>
        <span class="live"><i></i>CANLI GÖRÜNÜM</span>
      </div>
      <div class="dashTabs" id="heroDashTabs">
        <span data-pane="0" class="on">EBITDA Waterfall</span>
        <span data-pane="1">DuPont Tree</span>
        <span data-pane="2">Cash Conversion Cycle</span>
        <span data-pane="3">Risk Radar</span>
        <span data-pane="4">Scenario Lab</span>
      </div>
      <div id="heroDashPanes">
        <div class="dashPane on" data-pane="0">
          <div class="dTitle">EBITDA Köprüsü — Bu Dönem</div>
          <svg viewBox="0 0 300 140" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:140px">
            <rect x="4" y="30" width="30" height="100" fill="#4CC9F0" rx="3"/>
            <rect x="42" y="55" width="30" height="75" fill="#15E3B3" rx="3"/>
            <rect x="80" y="20" width="30" height="45" fill="#FF6B7A" rx="3" opacity=".85"/>
            <rect x="118" y="40" width="30" height="90" fill="#15E3B3" rx="3"/>
            <rect x="156" y="10" width="30" height="120" fill="#FFB020" rx="3" opacity=".9"/>
            <rect x="194" y="18" width="30" height="112" fill="#4CC9F0" rx="3"/>
            <text x="19" y="145" fill="#7C8FAD" font-size="8" text-anchor="middle" font-family="Inter,sans-serif">Geçen</text>
            <text x="57" y="145" fill="#7C8FAD" font-size="8" text-anchor="middle" font-family="Inter,sans-serif">Hacim</text>
            <text x="95" y="145" fill="#7C8FAD" font-size="8" text-anchor="middle" font-family="Inter,sans-serif">Maliyet</text>
            <text x="133" y="145" fill="#7C8FAD" font-size="8" text-anchor="middle" font-family="Inter,sans-serif">Fiyat</text>
            <text x="171" y="145" fill="#7C8FAD" font-size="8" text-anchor="middle" font-family="Inter,sans-serif">Opex</text>
            <text x="209" y="145" fill="#7C8FAD" font-size="8" text-anchor="middle" font-family="Inter,sans-serif">Bu Dönem</text>
          </svg>
          <div class="dashKpis"><div><b>%18,9</b><span>EBITDA Marjı</span></div><div><b>+3,2pp</b><span>YoY Değişim</span></div><div><b>84</b><span>Health Score</span></div></div>
        </div>
        <div class="dashPane" data-pane="1">
          <div class="dTitle">DuPont Ayrıştırması — ROE</div>
          <svg viewBox="0 0 300 130" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:130px">
            <rect x="110" y="4" width="80" height="26" rx="6" fill="#132238" stroke="#20334b"/><text x="150" y="21" text-anchor="middle" fill="#4CC9F0" font-family="Inter,sans-serif" font-size="10" font-weight="700">ROE %22</text>
            <line x1="130" y1="30" x2="70" y2="52" stroke="#20334b"/><line x1="170" y1="30" x2="230" y2="52" stroke="#20334b"/>
            <rect x="30" y="54" width="80" height="24" rx="6" fill="#132238" stroke="#20334b"/><text x="70" y="70" text-anchor="middle" fill="#C7D2E8" font-family="Inter,sans-serif" font-size="9">Net Marj %9,4</text>
            <rect x="190" y="54" width="80" height="24" rx="6" fill="#132238" stroke="#20334b"/><text x="230" y="70" text-anchor="middle" fill="#C7D2E8" font-family="Inter,sans-serif" font-size="9">Kaldıraç 2,1x</text>
            <line x1="55" y1="78" x2="35" y2="100" stroke="#20334b"/><line x1="85" y1="78" x2="105" y2="100" stroke="#20334b"/>
            <rect x="6" y="102" width="58" height="22" rx="6" fill="#101F33" stroke="#20334b"/><text x="35" y="117" text-anchor="middle" fill="#7C8FAD" font-family="Inter,sans-serif" font-size="8">Brüt Marj</text>
            <rect x="76" y="102" width="58" height="22" rx="6" fill="#101F33" stroke="#20334b"/><text x="105" y="117" text-anchor="middle" fill="#7C8FAD" font-family="Inter,sans-serif" font-size="8">Aktif Devir</text>
          </svg>
          <div class="dashKpis"><div><b>%9,4</b><span>Net Marj</span></div><div><b>1,18x</b><span>Aktif Devir</span></div><div><b>2,1x</b><span>Kaldıraç</span></div></div>
        </div>
        <div class="dashPane" data-pane="2">
          <div class="dTitle">Nakit Dönüşüm Döngüsü — Gün</div>
          <svg viewBox="0 0 300 130" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:130px">
            <text x="4" y="20" fill="#7C8FAD" font-family="Inter,sans-serif" font-size="9">DSO</text><rect x="4" y="26" width="292" height="16" rx="8" fill="#101F33"/><rect x="4" y="26" width="150" height="16" rx="8" fill="#4CC9F0"/><text x="160" y="38" fill="#C7D2E8" font-family="Inter,sans-serif" font-size="9">42 gün</text>
            <text x="4" y="60" fill="#7C8FAD" font-family="Inter,sans-serif" font-size="9">DIO</text><rect x="4" y="66" width="292" height="16" rx="8" fill="#101F33"/><rect x="4" y="66" width="120" height="16" rx="8" fill="#15E3B3"/><text x="130" y="78" fill="#C7D2E8" font-family="Inter,sans-serif" font-size="9">31 gün</text>
            <text x="4" y="100" fill="#7C8FAD" font-family="Inter,sans-serif" font-size="9">DPO</text><rect x="4" y="106" width="292" height="16" rx="8" fill="#101F33"/><rect x="4" y="106" width="90" height="16" rx="8" fill="#FFB020"/><text x="100" y="118" fill="#C7D2E8" font-family="Inter,sans-serif" font-size="9">-35 gün</text>
          </svg>
          <div class="dashKpis"><div><b>38 gün</b><span>Net CCC</span></div><div><b>+6</b><span>Geçen Döneme Göre</span></div><div><b>₺2,1M</b><span>Bağlı İşletme Sermayesi</span></div></div>
        </div>
        <div class="dashPane" data-pane="3">
          <div class="dTitle">Risk Radarı — Öncelik Sırası</div>
          <svg viewBox="0 0 300 130" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:130px" font-family="Inter,sans-serif">
            <circle cx="14" cy="18" r="5" fill="#FF6B7A"/><text x="28" y="22" fill="#C7D2E8" font-size="10">Tahsilat vadesi 12 gün uzadı</text>
            <rect x="150" y="12" width="60" height="14" rx="7" fill="#2A1420"/><rect x="150" y="12" width="48" height="14" rx="7" fill="#FF6B7A"/>
            <circle cx="14" cy="48" r="5" fill="#FFB020"/><text x="28" y="52" fill="#C7D2E8" font-size="10">Stok devri 3. ay kötüleşiyor</text>
            <rect x="150" y="42" width="60" height="14" rx="7" fill="#2A2010"/><rect x="150" y="42" width="36" height="14" rx="7" fill="#FFB020"/>
            <circle cx="14" cy="78" r="5" fill="#FFB020"/><text x="28" y="82" fill="#C7D2E8" font-size="10">Tedarikçi yoğunlaşması yüksek</text>
            <rect x="150" y="72" width="60" height="14" rx="7" fill="#2A2010"/><rect x="150" y="72" width="28" height="14" rx="7" fill="#FFB020"/>
            <circle cx="14" cy="108" r="5" fill="#15E3B3"/><text x="28" y="112" fill="#C7D2E8" font-size="10">Brüt marj hedefin üzerinde</text>
            <rect x="150" y="102" width="60" height="14" rx="7" fill="#0E2A22"/><rect x="150" y="102" width="52" height="14" rx="7" fill="#15E3B3"/>
          </svg>
          <div class="dashKpis"><div><b>3</b><span>Kritik Risk</span></div><div><b>5</b><span>Yüksek Öncelik</span></div><div><b>12</b><span>Toplam Bulgu</span></div></div>
        </div>
        <div class="dashPane" data-pane="4">
          <div class="dTitle">Senaryo Laboratuvarı — What If</div>
          <svg viewBox="0 0 300 130" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:130px">
            <polyline points="4,100 50,88 96,92 142,66 188,72 234,40 280,46" fill="none" stroke="#7C8FAD" stroke-width="2" stroke-dasharray="3 3"/>
            <polyline points="4,100 50,80 96,78 142,44 188,40 234,10 280,8" fill="none" stroke="#4CC9F0" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="280" cy="8" r="4" fill="#4CC9F0"/><circle cx="280" cy="46" r="4" fill="#7C8FAD"/>
            <text x="284" y="12" fill="#4CC9F0" font-family="Inter,sans-serif" font-size="9">İyimser</text>
            <text x="284" y="50" fill="#7C8FAD" font-family="Inter,sans-serif" font-size="9">Baz</text>
          </svg>
          <div class="dashKpis"><div><b>+%14</b><span>İyimser EBITDA</span></div><div><b>-%6</b><span>Kötümser EBITDA</span></div><div><b>3</b><span>Aktif Senaryo</span></div></div>
        </div>
      </div>
      <div class="foot"><span>Fiyat, hacim, maliyet ve opex ayrıştırması</span><span>Gerçek zamanlı yeniden hesap</span></div>
    </div>
  </div>
</section>

<div class="secBlock reveal"><section id="whyTrust" class="marketingSection hidePrint" style="padding-top:0">
<div class="marketingHead"><h2>Why CFOs Trust Digital Finance BP</h2><p>Bir "kara kutu" skor değil — her rakamın kaynağına kadar izlenebildiği bir karar motoru.</p></div>
<div class="trustGrid">
<div class="card trustCard"><div class="icoWrap2"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg></div><h3>Verified Calculations</h3><p>%100 deterministic financial engine — her rakam kaynağına kadar izlenebilir bir hesaplamadan gelir.</p></div>
<div class="card trustCard"><div class="icoWrap2"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h7l-1 8 10-12h-7l1-8z"/></svg></div><h3>Explainable AI</h3><p>AI yorumları her zaman ayrı, açık şekilde etiketlenir — doğrulanmış rakamların yerine değil, üstüne konur.</p></div>
<div class="card trustCard"><div class="icoWrap2"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg></div><h3>Audit Ready</h3><p>Her hesaplama adımı, kaynak veriye kadar tam izlenebilirlikle kayıt altında — denetime hazır.</p></div>
<div class="card trustCard"><div class="icoWrap2"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg></div><h3>Enterprise Security</h3><p>Yüklediğiniz veriler yalnızca analiz için işlenir; hesap açmadan sunucuda kalıcı saklanmaz. <a href="/guvenlik" style="color:var(--accent);text-decoration:none;font-weight:700">Detaylar →</a></p></div>
</div>
</section></div>

<div class="secBlock tint reveal"><section id="journey" class="marketingSection hidePrint">
<div class="marketingHead"><h2>Executive Journey</h2><p>Yüklemeden aksiyona, 6 adımda. Uzun paragraf yok — ürünün nasıl çalıştığını 10 saniyede görün.</p></div>
<div class="journey">
<div class="jStep"><div class="jDot">1</div><h4>UPLOAD</h4><p>Mizanınızı veya Excel dosyanızı yükleyin</p></div>
<div class="jStep"><div class="jDot">2</div><h4>VALIDATE</h4><p>Sistem verileri doğrular, tutarsızlıkları işaretler</p></div>
<div class="jStep"><div class="jDot">3</div><h4>ANALYZE</h4><p>33 motor finansal tabloları ve oranları kurar</p></div>
<div class="jStep"><div class="jDot">4</div><h4>INTERPRET</h4><p>Kök nedenler açıklanır, riskler önceliklendirilir</p></div>
<div class="jStep"><div class="jDot">5</div><h4>ACT</h4><p>Sahibi ve KPI'sı belli yönetim aksiyonları oluşur</p></div>
<div class="jStep"><div class="jDot">6</div><h4>IMPROVE</h4><p>Dönemler arası karşılaştırıp ilerlemeyi izleyin</p></div>
</div>
</section></div>

<div class="secBlock reveal"><section id="modules" class="marketingSection hidePrint">
<div class="marketingHead"><h2>Sonuç satın alırsınız, özellik değil</h2><p>Tek tek modül değil, dört karar sonucu: finansal sağlık, performans, nakit ve karar zekâsı.</p></div>
<div class="intelGrid">
<div class="card intelCard"><div class="igIco"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div><h3>Financial Health Intelligence</h3><ul><li>DuPont Ayrıştırması</li><li>Likidite</li><li>Kârlılık</li><li>Solvency (Borç Ödeme Gücü)</li></ul></div>
<div class="card intelCard"><div class="igIco"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 5-8"/></svg></div><h3>Performance Intelligence</h3><ul><li>Sapma (Variance) Analizi</li><li>Kâr Köprüsü</li><li>Kök Neden Analitiği</li></ul></div>
<div class="card intelCard"><div class="igIco"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></div><h3>Cash Intelligence</h3><ul><li>Nakit Dönüşüm Döngüsü</li><li>İşletme Sermayesi</li><li>Nakit Öngörüsü</li></ul></div>
<div class="card intelCard"><div class="igIco"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h7l-1 8 10-12h-7l1-8z"/></svg></div><h3>Decision Intelligence</h3><ul><li>Senaryo Laboratuvarı</li><li>AI Advisor</li><li>Risk Radarı</li></ul></div>
</div>
</section></div>

<div class="secBlock reveal"><section id="video" class="marketingSection hidePrint" style="padding-top:10px">
<div class="card" style="display:grid;grid-template-columns:1fr 1fr;gap:0;overflow:hidden;padding:0">
  <div style="padding:38px 36px;display:flex;flex-direction:column;justify-content:center">
    <span class="badge" style="align-self:flex-start;margin-bottom:14px">İZLE · 90 SANİYE</span>
    <h2 style="font-family:var(--serif);font-size:24px;margin:0 0 10px;letter-spacing:-.4px">Bu ne yapıyor, gerçekten?</h2>
    <p class="muted" style="font-size:13.5px;max-width:40ch;margin:0">Bir finans yöneticisinin Excel dosyasını yüklemesinden yönetim kuruluna sunacağı rapora kadar geçen süreci ekran kaydıyla gösteriyoruz.</p>
  </div>
  <div style="position:relative;background:#0F1B2D;min-height:260px">
    <video controls preload="metadata" poster="/static/video/demo-poster.jpg" style="width:100%;height:100%;object-fit:cover;display:block">
      <source src="/static/video/dfbp-90sec-demo.mp4" type="video/mp4">
    </video>
  </div>
</div>
</section></div>

<div class="secBlock tint reveal"><section id="ornekDene" class="marketingSection hidePrint">
<div class="marketingHead"><h2>Çıktı nasıl görünüyor, kendiniz görün</h2><p>Kayıt olmadan, kendi dosyanızı hazırlamadan — hazır örnek verilerden biriyle tam raporu inceleyin.</p></div>
<div class="grid4">
<div class="card" style="padding:24px"><div class="tag" style="margin-bottom:12px">Tek Dönem</div><h3 style="margin:0 0 6px;font-size:16px">Genel Mizan</h3><p class="muted small">Standart bir mizan dosyasından P&amp;L, Bilanço, Nakit Akışı ve Yönetici Özeti nasıl çıkarılır, görün.</p><a href="/uygulama?sample=mizan" class="secondary" style="display:block;text-align:center;margin-top:16px;text-decoration:none;padding:10px;border-radius:10px">Raporu Aç</a></div>
<div class="card" style="padding:24px"><div class="tag" style="margin-bottom:12px">Dönem Karşılaştırma</div><h3 style="margin:0 0 6px;font-size:16px">Önceki Dönem ile Trend</h3><p class="muted small">İki dönemlik mizan karşılaştırmasıyla değişim, sapma ve kök neden analizinin nasıl işlediğini görün.</p><a href="/uygulama?sample=mizan_prior" class="secondary" style="display:block;text-align:center;margin-top:16px;text-decoration:none;padding:10px;border-radius:10px">Raporu Aç</a></div>
<div class="card" style="padding:24px"><div class="tag" style="margin-bottom:12px">3 Tablo</div><h3 style="margin:0 0 6px;font-size:16px">Bilanço + Gelir Tablosu</h3><p class="muted small">Mizan yerine hazır bilanço ve gelir tablosu ile çalışan şirketler için örnek analiz akışı.</p><a href="/uygulama?sample=three_sheet" class="secondary" style="display:block;text-align:center;margin-top:16px;text-decoration:none;padding:10px;border-radius:10px">Raporu Aç</a></div>
<div class="card" style="padding:24px;border-color:var(--accent)"><div class="tag" style="margin-bottom:12px;background:#DCE6FB;color:var(--accent)">Data Hub</div><h3 style="margin:0 0 6px;font-size:16px">Mizan + AR/AP + Stok + Satış</h3><p class="muted small">Mizanla birlikte AR/AP yaşlandırma, stok ve satış defterini tek seferde yükleyip tüm karar motorlarının (Risk, PVM, Nakit) birlikte çalıştığını görün.</p><a href="/uygulama?sample=data_hub" class="secondary" style="display:block;text-align:center;margin-top:16px;text-decoration:none;padding:10px;border-radius:10px">Raporu Aç</a></div>
</div>
<div style="text-align:center;margin-top:26px"><a href="/uygulama?sample=1" class="primary" style="text-decoration:none;padding:13px 22px;border-radius:12px;display:inline-block">Örnek Veriyle Analizi Şimdi Başlat</a><p class="muted small" style="margin-top:10px">Sıfır kurulum · Şablon hazırlamanıza gerek yok · saniyeler içinde P&amp;L, Nakit Akışı, İşletme Sermayesi ve Yönetici Özeti</p></div>
</section></div>

<div class="secBlock reveal"><section class="statsStrip hidePrint">
<div class="stat"><b>33</b><span>Deterministik analiz motoru — kâr köprüsü, DuPont, senaryo, kök-neden</span></div>
<div class="stat"><b>5</b><span>Adımlı karar akışı: What → Why → So What → Now What → What If</span></div>
<div class="stat"><b>&lt;2 dk</b><span>Dosya yüklemeden yönetim raporuna geçen süre</span></div>
<div class="stat"><b>0₺</b><span>Örnek veriyle deneme — kayıt olmadan, kredi kartı istemeden</span></div>
</section>
<section id="whyUs" class="flowStep hidePrint" style="margin-top:8px"><div class="flowLabel"><span class="n">★</span>Neden Digital Finance Business Partner?<p>Bir Excel şablonu değil, karar destek katmanı</p></div>
<div class="grid4">
<div class="card whyCard"><div class="icoWrap"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg></div><h3 style="margin:0 0 6px;font-size:15px">Kural tabanlı, kanıtlanabilir</h3><p class="muted small">Her rakam, kaynağına kadar izlenebilir bir hesaplamadan gelir. AI yorumu isteğe bağlı ve her zaman ayrı etiketlenir — "kara kutu" bir skor değil.</p></div>
<div class="card whyCard"><div class="icoWrap"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h7l-1 8 10-12h-7l1-8z"/></svg></div><h3 style="margin:0 0 6px;font-size:15px">Dakikalar içinde sonuç</h3><p class="muted small">Mizanınızı yükleyin, 33 analiz motoru bilanço, gelir tablosu, kök-neden ve senaryo analizini otomatik kurar — muhasebeci beklemeden.</p></div>
<div class="card whyCard"><div class="icoWrap"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 5-8"/></svg></div><h3 style="margin:0 0 6px;font-size:15px">Yönetim kurulu diliyle</h3><p class="muted small">Sadece rakam değil; "ne oldu, neden oldu, maliyeti ne, ne yapılmalı" akışıyla direkt karar destek raporu — bankaya, ortağa, yönetim kuruluna gösterilebilir.</p></div>
<div class="card whyCard"><div class="icoWrap"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg></div><h3 style="margin:0 0 6px;font-size:15px">Verileriniz size ait</h3><p class="muted small">Yüklediğiniz dosyalar yalnızca analiz üretmek için işlenir; hesap açmadan sunucuda kalıcı saklanmaz. Kayıt olursanız geçmişiniz sadece sizin erişiminizde tutulur.</p></div>
</div></section>
<section id="howTo" class="flowStep hidePrint"><div class="flowLabel alt"><span class="n">?</span>Nasıl Kullanılır<p>3 adımda finansal sağlık raporu</p></div>
<div class="grid3">
<div class="card" style="padding:18px"><div class="tag" style="margin-bottom:8px">ADIM 1</div><h3 style="margin:0 0 6px;font-size:15px">Dosyanı yükle (ya da örnekle dene)</h3><p class="muted small">Mizan/Excel dosyanı "Tek dönem" sekmesine sürükle. Dosyan yoksa yukarıdaki "Örnekle dene" butonuyla anında gerçek bir raporu gör.</p></div>
<div class="card" style="padding:18px"><div class="tag" style="margin-bottom:8px">ADIM 2</div><h3 style="margin:0 0 6px;font-size:15px">Raporu incele</h3><p class="muted small">Health Score, kök-neden bulguları, senaryo anlatıları ve yönetim aksiyonları otomatik oluşur. İstersen AI CFO'dan ek yorum veya soru-cevap iste.</p></div>
<div class="card" style="padding:18px"><div class="tag" style="margin-bottom:8px">ADIM 3</div><h3 style="margin:0 0 6px;font-size:15px">Kaydet, karşılaştır, paylaş</h3><p class="muted small">Ücretsiz kayıt olup analizi yıl bazında kaydet; sonraki dönemlerle karşılaştır ya da PDF olarak yönetim kuruluna gönder.</p></div>
</div></section>
</div>

<div class="secBlock reveal"><section class="execBand hidePrint">
  <div class="execCopy">
    <span class="execEyebrow">YÖNETİM KURULU GÖRÜNÜMÜ</span>
    <h2>Toplantıya girmeden önce gördüğünüz ekran, bu.</h2>
    <p>Health Score, kâr köprüsü, nakit dönüşüm döngüsü ve risk radarı — tek ekranda, tek bakışta. Excel sekmeleri arasında kaybolmak yok.</p>
    <ul class="execList">
      <li><b>Health Score</b> — tek sayıda finansal sağlık özeti</li>
      <li><b>Kâr Köprüsü</b> — geçen döneme göre neyin kârı artırıp azalttığı</li>
      <li><b>Nakit Dönüşüm Döngüsü</b> — tahsilat, stok ve ödeme süresi tek grafikte</li>
      <li><b>Risk Radarı</b> — öncelik sırasına dizilmiş kritik bulgular</li>
    </ul>
    <a href="/uygulama?sample=1" class="execCta">Bu Ekranı Kendi Verinizle Görün →</a>
  </div>
  <div class="execArt">
    <svg viewBox="0 0 480 340" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">
      <defs>
        <linearGradient id="eg1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4CC9F0"/><stop offset="1" stop-color="#1D4ED8"/></linearGradient>
        <linearGradient id="eg2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#15E3B3"/><stop offset="1" stop-color="#0E7C66"/></linearGradient>
      </defs>
      <rect x="8" y="8" width="464" height="324" rx="16" fill="#0D1B2A" stroke="#1E3050"/>
      <circle cx="30" cy="28" r="4" fill="#4CC9F0"/><circle cx="44" cy="28" r="4" fill="#15E3B3"/><circle cx="58" cy="28" r="4" fill="#94A3B8"/>
      <text x="400" y="32" fill="#7C8FAD" font-family="Inter,sans-serif" font-size="10" text-anchor="end">MONTHLY BUSINESS REVIEW</text>
      <line x1="20" y1="46" x2="460" y2="46" stroke="#1E3050"/>
      <!-- KPI tiles -->
      <g font-family="Inter,sans-serif">
        <rect x="20" y="58" width="104" height="56" rx="8" fill="#132238" stroke="#20334b"/>
        <text x="30" y="76" fill="#7C8FAD" font-size="9">HEALTH SCORE</text>
        <text x="30" y="98" fill="#4CC9F0" font-size="20" font-weight="700">84</text>
        <rect x="132" y="58" width="104" height="56" rx="8" fill="#132238" stroke="#20334b"/>
        <text x="142" y="76" fill="#7C8FAD" font-size="9">EBITDA MARJI</text>
        <text x="142" y="98" fill="#15E3B3" font-size="20" font-weight="700">%18,9</text>
        <rect x="244" y="58" width="104" height="56" rx="8" fill="#132238" stroke="#20334b"/>
        <text x="254" y="76" fill="#7C8FAD" font-size="9">NAKİT DÖNGÜSÜ</text>
        <text x="254" y="98" fill="#FFB020" font-size="20" font-weight="700">38 gün</text>
        <rect x="356" y="58" width="104" height="56" rx="8" fill="#132238" stroke="#20334b"/>
        <text x="366" y="76" fill="#7C8FAD" font-size="9">KRİTİK RİSK</text>
        <text x="366" y="98" fill="#FF6B7A" font-size="20" font-weight="700">3</text>
      </g>
      <!-- profit bridge waterfall -->
      <g>
        <text x="20" y="135" fill="#7C8FAD" font-family="Inter,sans-serif" font-size="9">KÂR KÖPRÜSÜ</text>
        <rect x="20" y="145" width="34" height="90" fill="url(#eg1)" rx="3"/>
        <rect x="62" y="175" width="34" height="60" fill="url(#eg2)" rx="3"/>
        <rect x="104" y="150" width="34" height="45" fill="#FF6B7A" rx="3" opacity=".85"/>
        <rect x="146" y="160" width="34" height="75" fill="url(#eg2)" rx="3"/>
        <rect x="188" y="120" width="34" height="115" fill="url(#eg1)" rx="3"/>
      </g>
      <!-- trend line -->
      <g>
        <text x="244" y="135" fill="#7C8FAD" font-family="Inter,sans-serif" font-size="9">GELİR TRENDİ</text>
        <polyline points="244,220 270,200 296,210 322,175 348,185 374,150 400,160 426,130" fill="none" stroke="#4CC9F0" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="426" cy="130" r="4" fill="#4CC9F0"/>
      </g>
      <line x1="20" y1="250" x2="460" y2="250" stroke="#1E3050"/>
      <!-- risk radar rows -->
      <g font-family="Inter,sans-serif" font-size="10.5">
        <circle cx="28" cy="268" r="4" fill="#FF6B7A"/><text x="40" y="272" fill="#C7D2E8">Tahsilat vadesi 12 gün uzadı — nakit akışı riski</text>
        <circle cx="28" cy="290" r="4" fill="#FFB020"/><text x="40" y="294" fill="#C7D2E8">Stok devir hızı yavaşlıyor — 3. aydır kötüleşiyor</text>
        <circle cx="28" cy="312" r="4" fill="#15E3B3"/><text x="40" y="316" fill="#C7D2E8">Brüt marj hedefin üzerinde — sürdürülebilir</text>
      </g>
    </svg>
  </div>
</section></div>

<div class="secBlock tint reveal"><div class="marketingHead"><h2>Size uygun paketi seçin</h2><p>Üç paket de aynı motoru kullanır, fark kapsam ve süreklilikte.</p></div>
<div class="pricingGrid">
<div class="card priceCard"><div class="plan">Başlangıç</div><h3>Starter</h3><div class="amt">₺0<span> /örnek analiz</span></div><div class="desc">Sistemi görmek isteyen ekipler için.</div><a href="/uygulama" class="secondary" style="width:100%;text-align:center;text-decoration:none;display:block;margin-top:auto">Ücretsiz Dene</a></div>
<div class="card priceCard featured"><div class="badgeTop">En Çok Tercih Edilen</div><div class="plan">Büyüyen Ekipler</div><h3>Professional</h3><div class="amt">₺2.490<span> /ay</span></div><div class="desc">Düzenli yönetim raporu üreten finans ekipleri için.</div><a href="/uygulama?auth=register" class="primary" style="width:100%;text-align:center;text-decoration:none;display:block;margin-top:auto">Kayıt Ol</a></div>
<div class="card priceCard"><div class="plan">Kurumsal</div><h3>Enterprise</h3><div class="amt">Teklif ile<span> /özel</span></div><div class="desc">Çoklu şirket/bölüm yapısı olan kurumlar için.</div><a href="/iletisim" class="secondary" style="width:100%;text-align:center;text-decoration:none;display:block;margin-top:auto">Bize Ulaşın</a></div>
</div>
<div style="text-align:center;margin-top:22px"><a href="/paketler" class="secondary" style="text-decoration:none;padding:11px 20px;border-radius:11px;display:inline-block">Tüm paket detaylarını gör →</a></div>
</div>

<div class="secBlock reveal"><section class="ctaBanner hidePrint"><div><h3>Finansal sağlığınızı şimdi görün</h3><p>Dosya yüklemeden, kayıt olmadan — örnek veriyle tam bir yönetim raporunun nasıl göründüğünü 2 dakikada deneyin.</p></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a href="/uygulama" class="primary" style="text-decoration:none;padding:12px 20px;border-radius:11px">Örnekle Dene</a><a href="/uygulama?auth=register" class="secondary" style="text-decoration:none;padding:12px 20px;border-radius:11px">Ücretsiz Kayıt Ol</a></div></section></div>
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
.marketingSection{padding:60px 0}
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
.navBtns a.secondary,.navBtns a.primary{text-decoration:none;display:inline-flex;align-items:center;font-weight:700}
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
.secBlock{padding:58px 0}
.secBlock.tint{background:linear-gradient(180deg,rgba(16,31,51,.55),rgba(10,23,39,.15));border-radius:32px;margin:0 -10px}
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
.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

</style></head>
<body>
<header class="top"><div class="wrap brand"><div><a href="/" style="text-decoration:none;color:inherit"><h1>Digital Finance Business Partner</h1><p>Verified financial facts → decision intelligence → management action</p></a></div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/paketler" class="active">Paketler</a><a href="/hakkimizda">Hakkımızda</a><a href="/iletisim">İletişim</a><a href="/guvenlik">Güvenlik</a><a href="/uygulama">Uygulama</a></nav><span class="badge v">Finance Core v__APP_VERSION__</span><div class="navBtns"><a href="/uygulama?auth=login" class="secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="primary">Ücretsiz Kayıt Ol</a></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<div class="pageHead reveal in"><span class="eyebrow">Paketler</span><h1>Size uygun paketi seçin</h1><p>Tek seferlik bir örnek raporla mı başlamak istiyorsunuz, yoksa ekibinizin her ay düzenli kullandığı bir karar destek katmanı mı arıyorsunuz — üç paket de aynı motoru kullanır, fark kapsam ve süreklilikte.</p></div>
<div class="secBlock reveal"><section class="marketingSection hidePrint">
<div class="pricingGrid">
<div class="card priceCard"><div class="plan">Başlangıç</div><h3>Starter</h3><div class="amt">₺0<span> /örnek analiz</span></div><div class="desc">Sistemi görmek isteyen, henüz dosya yüklemeyen ekipler için.</div><ul>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Örnek veriyle tam rapor denemesi</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>What / So What / Why / Now What akışı</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Kayıt gerekmez, tarayıcıda kalır</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Tek dönem, kaydetme yok</li>
</ul><button class="secondary" style="width:100%" onclick="window.location.href='/uygulama'">Ücretsiz Dene</button></div>
<div class="card priceCard featured"><div class="badgeTop">En Çok Tercih Edilen</div><div class="plan">Büyüyen Ekipler</div><h3>Professional</h3><div class="amt">₺2.490<span> /ay</span></div><div class="desc">Kendi verinizi düzenli yükleyip yönetim raporu üretmek isteyen finans ekipleri için.</div><ul>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Sınırsız dosya yükleme ve analiz</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Çok dönemli trend ve karşılaştırma</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Geçmiş analizleri kaydetme ve karşılaştırma</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Data Hub: kaynak bazlı mutabakat</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Opsiyonel AI CFO yorumu (Gemini)</li>
</ul><button class="primary" style="width:100%" onclick="window.location.href='/uygulama?auth=register'">Kayıt Ol</button></div>
<div class="card priceCard"><div class="plan">Kurumsal</div><h3>Enterprise</h3><div class="amt">Teklif ile<span> /özel</span></div><div class="desc">Çoklu şirket/bölüm yapısı, özel entegrasyon veya danışmanlık desteği isteyen kurumlar için.</div><ul>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Professional'daki her şey</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Çoklu kullanıcı ve şirket/bölüm yönetimi</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Özel kural/eşik seti (sektörünüze göre)</li>
<li><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>Öncelikli destek ve kurulum danışmanlığı</li>
</ul><button class="secondary" style="width:100%" onclick="window.location.href='/iletisim'">Bize Ulaşın</button></div>
</div></section>

</div>

<div class="secBlock reveal"><div class="marketingHead"><h2>Sık Sorulan Sorular</h2></div>
<div style="max-width:720px;margin:auto">
<details class="faqItem" open><summary>Verilerim güvende mi?</summary><p>Yüklediğiniz dosyalar yalnızca analiz üretmek için işlenir; hesap açmadan sunucuda kalıcı saklanmaz. Kayıt olursanız geçmişiniz yalnızca sizin erişiminizde tutulur.</p></details>
<details class="faqItem"><summary>Paket değiştirebilir miyim?</summary><p>Evet, ihtiyacınız değiştikçe paketler arasında geçiş yapabilirsiniz; mevcut analiz geçmişiniz korunur.</p></details>
<details class="faqItem"><summary>AI yorumu zorunlu mu?</summary><p>Hayır. Tüm rakamlar önce deterministik olarak hesaplanır; AI CFO yorumu tamamen isteğe bağlı, ayrı etiketlenmiş bir ek katmandır.</p></details>
<details class="faqItem"><summary>Kurumsal pakette neler özelleşiyor?</summary><p>Çoklu kullanıcı/şirket yönetimi, sektörünüze özel kural ve eşik setleri, öncelikli destek ve kurulum danışmanlığı Enterprise pakette yer alır.</p></details>
</div></div>

<div class="secBlock tint reveal"><section class="ctaBanner hidePrint"><div><h3>Hangi paketin size uygun olduğundan emin değil misiniz?</h3><p>2 dakikalık bir örnek analizle sistemi görün, sonra karar verin.</p></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a href="/uygulama" class="primary" style="text-decoration:none;padding:12px 20px;border-radius:11px">Örnekle Dene</a><a href="/iletisim" class="secondary" style="text-decoration:none;padding:12px 20px;border-radius:11px">Kurumsal Teklif Al</a></div></section></div>
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
.marketingSection{padding:60px 0}
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
.navBtns a.secondary,.navBtns a.primary{text-decoration:none;display:inline-flex;align-items:center;font-weight:700}
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
.secBlock{padding:58px 0}
.secBlock.tint{background:linear-gradient(180deg,rgba(16,31,51,.55),rgba(10,23,39,.15));border-radius:32px;margin:0 -10px}
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
.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

</style></head>
<body>
<header class="top"><div class="wrap brand"><div><a href="/" style="text-decoration:none;color:inherit"><h1>Digital Finance Business Partner</h1><p>Verified financial facts → decision intelligence → management action</p></a></div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/paketler">Paketler</a><a href="/hakkimizda" class="active">Hakkımızda</a><a href="/iletisim">İletişim</a><a href="/guvenlik">Güvenlik</a><a href="/uygulama">Uygulama</a></nav><span class="badge v">Finance Core v__APP_VERSION__</span><div class="navBtns"><a href="/uygulama?auth=login" class="secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="primary">Ücretsiz Kayıt Ol</a></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<div class="pageHead reveal in"><span class="eyebrow">Hakkımızda</span><h1>Muhasebe raporu değil, yönetim kararı üretiyoruz</h1><p>Finans ekiplerinin saatlerce harcadığı "rakamları toparlama" işini otomatikleştirip, zamanı asıl değerin katıldığı yere — yorum ve karara — taşıyoruz.</p></div>
<div class="secBlock reveal"><section id="about" class="marketingSection hidePrint"><div class="aboutGrid">
<div><span class="badge" style="margin-bottom:14px;display:inline-block">Hakkımızda</span><h2 style="font-family:var(--serif);font-size:30px;margin:6px 0 12px;letter-spacing:-.5px">Muhasebe raporu değil, yönetim kararı üretiyoruz</h2><p class="muted" style="font-size:14px;line-height:1.7">Digital Finance Business Partner, finans ekiplerinin saatlerce harcadığı "rakamları toparlama" işini otomatikleştirip, gerçek zamanı yönetime asıl değeri kattığı yere — yorum ve karara — taşımak için kuruldu. Motor önce deterministik olarak hesaplar, sonra yorumlar; yapay zekâ yalnızca isteğe bağlı, ayrı etiketlenmiş bir ek katmandır, asla ham rakamların yerine geçmez.</p><div class="aboutStats"><div class="st"><b>8+</b><span>Analiz motoru</span></div><div class="st"><b>%100</b><span>Deterministik hesap</span></div><div class="st"><b>0</b><span>Kalıcı veri saklama</span></div></div></div>
<div class="card" style="padding:26px">
<svg viewBox="0 0 320 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;margin-bottom:16px">
  <rect x="120" y="6" width="80" height="30" rx="7" fill="#EAF0FF" stroke="#C9D8F5"/><text x="160" y="25" text-anchor="middle" fill="#1D4ED8" font-family="Inter,sans-serif" font-size="10.5" font-weight="700">ROE %22</text>
  <line x1="140" y1="36" x2="70" y2="60" stroke="#C9D2DE"/><line x1="180" y1="36" x2="250" y2="60" stroke="#C9D2DE"/>
  <rect x="30" y="62" width="80" height="28" rx="6" fill="#F0F3F8" stroke="#E4E8EF"/><text x="70" y="80" text-anchor="middle" fill="#33415C" font-family="Inter,sans-serif" font-size="9.5">Net Marj</text>
  <rect x="210" y="62" width="80" height="28" rx="6" fill="#F0F3F8" stroke="#E4E8EF"/><text x="250" y="80" text-anchor="middle" fill="#33415C" font-family="Inter,sans-serif" font-size="9.5">Kaldıraç</text>
  <line x1="55" y1="90" x2="35" y2="112" stroke="#E4E8EF"/><line x1="85" y1="90" x2="105" y2="112" stroke="#E4E8EF"/>
  <rect x="8" y="114" width="60" height="26" rx="6" fill="#FFFFFF" stroke="#E4E8EF"/><text x="38" y="131" text-anchor="middle" fill="#5B6B84" font-family="Inter,sans-serif" font-size="8.5">Brüt Marj</text>
  <rect x="80" y="114" width="60" height="26" rx="6" fill="#FFFFFF" stroke="#E4E8EF"/><text x="110" y="131" text-anchor="middle" fill="#5B6B84" font-family="Inter,sans-serif" font-size="8.5">Aktif Devir</text>
</svg>
<h3 style="margin:0 0 12px">Neye inanıyoruz</h3><ul style="margin:0;padding-left:18px;color:#33415C;font-size:13.5px;line-height:2">
<li>Karar destek, robotik rapor üretiminden farklıdır.</li>
<li>Önce hesap, sonra yorum — sıra hiç değişmez.</li>
<li>Veri sizindir; hesap açmadan sunucuda kalıcı tutulmaz.</li>
<li>Yapay zekâ yorumu, doğrulanmış rakamların yerine değil, üstüne konur.</li>
</ul></div>
</div></section>

</div>
<div class="secBlock tint reveal"><div class="marketingHead"><h2>Nasıl çalışıyoruz</h2></div>
<div class="grid3">
<div class="card" style="padding:22px"><div class="tag" style="margin-bottom:8px">01</div><h3 style="margin:0 0 6px;font-size:15px">Önce hesap</h3><p class="muted small">Her rakam, kaynağına kadar izlenebilir deterministik bir hesaplamadan gelir. Yorum, hesaptan sonra gelir — asla önce değil.</p></div>
<div class="card" style="padding:22px"><div class="tag" style="margin-bottom:8px">02</div><h3 style="margin:0 0 6px;font-size:15px">Sonra yorum</h3><p class="muted small">33 analiz motoru bulguları önceliklendirir, kök nedeni açıklar; isteğe bağlı AI katmanı bunun üstüne, ayrı etiketlenmiş bir yorum ekler.</p></div>
<div class="card" style="padding:22px"><div class="tag" style="margin-bottom:8px">03</div><h3 style="margin:0 0 6px;font-size:15px">Sonunda aksiyon</h3><p class="muted small">Çıktı, bir Excel tablosu değil; sahibi ve KPI'sı belli, yönetim kurulunda okunabilecek somut aksiyon listesidir.</p></div>
</div></div>
<div class="secBlock reveal"><section class="ctaBanner hidePrint"><div><h3>Bizi tanımak ister misiniz?</h3><p>Ekibinizle birlikte 15 dakikalık bir demo planlayabiliriz.</p></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a href="/iletisim" class="primary" style="text-decoration:none;padding:12px 20px;border-radius:11px">İletişime Geç</a></div></section></div>
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
.marketingSection{padding:60px 0}
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
.navBtns a.secondary,.navBtns a.primary{text-decoration:none;display:inline-flex;align-items:center;font-weight:700}
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
.secBlock{padding:58px 0}
.secBlock.tint{background:linear-gradient(180deg,rgba(16,31,51,.55),rgba(10,23,39,.15));border-radius:32px;margin:0 -10px}
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
.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

</style></head>
<body>
<header class="top"><div class="wrap brand"><div><a href="/" style="text-decoration:none;color:inherit"><h1>Digital Finance Business Partner</h1><p>Verified financial facts → decision intelligence → management action</p></a></div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/paketler">Paketler</a><a href="/hakkimizda">Hakkımızda</a><a href="/iletisim" class="active">İletişim</a><a href="/guvenlik">Güvenlik</a><a href="/uygulama">Uygulama</a></nav><span class="badge v">Finance Core v__APP_VERSION__</span><div class="navBtns"><a href="/uygulama?auth=login" class="secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="primary">Ücretsiz Kayıt Ol</a></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
<main class="wrap">
<div class="pageHead reveal in"><span class="eyebrow">İletişim</span><h1>Konuşalım</h1><p>Paketler, kurumsal teklif veya demo talebi için bize ulaşın; genelde 1 iş günü içinde dönüş yapıyoruz.</p></div>
<div class="secBlock reveal"><section id="contact" class="marketingSection hidePrint"><div class="marketingHead"><h2>İletişim</h2><p>Paketler, kurumsal teklif veya demo talebi için bize ulaşın.</p></div>
<div class="contactGrid">
<div class="card contactCard"><h3 style="margin:0 0 4px">Bize yazın</h3><p class="muted small" style="margin:0 0 4px">Genelde 1 iş günü içinde dönüş yapıyoruz.</p><div class="contactRow">
<div class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="M22 6l-10 7L2 6"/></svg>info@digitalfinancebp.com</div>
<div class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>+90 (212) 000 00 00</div>
<div class="item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>İstanbul, Türkiye</div>
</div></div>
<div class="card contactCard"><h3 style="margin:0 0 12px">Hızlı mesaj</h3><div style="display:flex;flex-direction:column;gap:10px">
<input class="select" style="width:100%" type="text" placeholder="Adınız">
<input class="select" style="width:100%" type="email" placeholder="E-posta">
<input class="select" style="width:100%" type="text" placeholder="Şirket adı (opsiyonel)">
<textarea class="select" style="width:100%;min-height:80px;font-family:inherit" placeholder="Mesajınız"></textarea>
<button class="primary" style="width:100%" onclick="alert('Talebiniz alındı, en kısa sürede dönüş yapacağız.')">Gönder</button>
</div></div>
</div></section>

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
.marketingSection{padding:60px 0}
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
.navBtns a.secondary,.navBtns a.primary{text-decoration:none;display:inline-flex;align-items:center;font-weight:700}
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
.secBlock{padding:58px 0}
.secBlock.tint{background:linear-gradient(180deg,rgba(16,31,51,.55),rgba(10,23,39,.15));border-radius:32px;margin:0 -10px}
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
.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

</style></head>
<body>
<header class="top"><div class="wrap brand"><div><a href="/" style="text-decoration:none;color:inherit"><h1>Digital Finance Business Partner</h1><p>Verified financial facts → decision intelligence → management action</p></a></div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/paketler">Paketler</a><a href="/hakkimizda">Hakkımızda</a><a href="/iletisim">İletişim</a><a href="/guvenlik" class="active">Güvenlik</a><a href="/uygulama">Uygulama</a></nav><span class="badge v">Finance Core v__APP_VERSION__</span><div class="navBtns"><a href="/uygulama?auth=login" class="secondary">Giriş Yap</a><a href="/uygulama?auth=register" class="primary">Ücretsiz Kayıt Ol</a></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header>
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
</div>
</section></div>

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
.upload{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}.file{border:1px dashed #C9D2DE;padding:12px;border-radius:12px;background:#F5F7FA;max-width:100%}.select,button{border:1px solid #D7DEE8;border-radius:11px;padding:11px 14px;background:#FFFFFF;color:var(--text)}button.primary,a.primary{background:linear-gradient(135deg,#2557E8,#1D4ED8);border:0;color:#FFFFFF;font-weight:800;cursor:pointer;transition:transform .15s ease,box-shadow .15s ease;box-shadow:0 6px 16px rgba(29,78,216,.25)}a.primary:hover,button.primary:hover{transform:translateY(-1px);box-shadow:0 10px 22px rgba(29,78,216,.32)}button.secondary,a.secondary{cursor:pointer;border:1.5px solid #C9D2DE;background:#FFFFFF;color:var(--text)}a.secondary:hover,button.secondary:hover{border-color:var(--accent);color:var(--accent)}button:disabled{opacity:.5;cursor:not-allowed}.scoreCard{padding:25px;display:flex;flex-direction:column;justify-content:center}.scoreRing{width:170px;height:170px;border-radius:50%;margin:auto;display:grid;place-items:center;background:conic-gradient(var(--accent) calc(var(--score)*1%),#E4E8EF 0);position:relative}.scoreRing:after{content:"";position:absolute;inset:12px;border-radius:50%;background:#FFFFFF}.scoreNum{position:relative;z-index:1;text-align:center}.scoreNum strong{display:block;font-size:48px;line-height:1}.scoreNum span{color:var(--muted);font-size:12px}.status{margin:15px auto 0;padding:7px 12px;border-radius:999px;background:#EAF0FF;color:var(--accent);font-size:12px;font-weight:700}.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.card{padding:22px;margin:0 0 16px;transition:transform .18s ease,box-shadow .18s ease,outline .2s}.card:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(15,27,45,.08)}@keyframes growUp{from{transform:scaleY(0);opacity:0}to{transform:scaleY(1);opacity:1}}.wf{transform-origin:bottom}.wf .col{transform-origin:bottom}@keyframes growWidth{from{width:0}to{}}.metric{padding:17px;border:1px solid var(--line);border-radius:15px;background:rgba(15,27,45,.03)}.metric .label{color:var(--muted);font-size:12px}.metric .value{font-size:25px;font-weight:800;margin-top:5px;letter-spacing:-.5px}.metric .sub{font-size:11px;color:var(--muted);margin-top:5px}.sectionHead{display:flex;align-items:end;justify-content:space-between;gap:15px;margin-bottom:17px}.sectionHead h2{margin:0;font-size:18px}.sectionHead p{margin:0;color:var(--muted);font-size:12px}.flowStep{margin:36px 0 14px;padding-top:6px;border-top:1px solid rgba(15,27,45,.08)}.flowStep:first-child{margin-top:0;border-top:0;padding-top:0}.flowLabel{display:flex;align-items:center;gap:10px;font-size:12px;font-weight:800;letter-spacing:1.8px;text-transform:uppercase;color:var(--accent);margin:0 0 4px}.flowLabel .n{width:22px;height:22px;border-radius:50%;background:#EAF0FF;color:var(--accent);display:inline-flex;align-items:center;justify-content:center;font-size:11px}.flowLabel p{margin:0;color:var(--muted);font-size:12.5px;font-weight:500;text-transform:none;letter-spacing:0}.flowLabel.alt{color:var(--accent2)}.flowLabel.alt .n{color:var(--accent2)}.flowSub{color:var(--muted);font-size:12.5px;margin:2px 0 16px 32px}.insight{border:1px solid var(--line);border-radius:15px;padding:16px;background:#F7F9FC}.insight.critical{border-color:#E8B4BD}.insight.high{border-color:#E9CBA8}.insight.medium{border-color:#E5DBA0}.insight.positive{border-color:#A9D9C9}.insight h3{margin:0 0 5px;font-size:14px}.insight p{margin:6px 0;color:#33415C;font-size:13px}.insight ul{margin:6px 0;padding-left:18px;color:#33415C;font-size:13px}.tag{display:inline-flex;padding:4px 8px;border-radius:999px;font-size:10px;font-weight:800;text-transform:uppercase;background:#EAF0FF;color:#5B6B84}.tag.critical{background:#FCE8EA;color:#C22A3E}.tag.high{background:#FDF0E0;color:#B4720A}.tag.medium{background:#FBF6DE;color:#8A6D00}.tag.positive{background:#E4F5EF;color:#0E7C66}.riskRow,.actionRow{display:grid;grid-template-columns:40px 1fr auto;gap:12px;align-items:center;padding:13px 0;border-bottom:1px solid rgba(15,27,45,.08)}.rank{font-size:18px;font-weight:900;color:#5B6B84}.riskScore{font-size:12px;color:var(--muted)}.bar{height:7px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:8px}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:99px}.waterfall{display:flex;align-items:flex-end;gap:7px;height:190px;padding:20px 5px 0;border-bottom:1px solid var(--line)}.wf{flex:1;display:flex;flex-direction:column;justify-content:end;height:100%;min-width:0}.wf .col{border-radius:6px 6px 2px 2px;background:linear-gradient(180deg,#83a4ff,#506fd0);min-height:3px}.wf.neg .col{background:linear-gradient(180deg,#ff8290,#9d3e54)}.wf .lab{font-size:10px;color:var(--muted);text-align:center;margin-top:7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.wf .num{font-size:9px;text-align:center;color:#33415C;margin-bottom:4px}.scenario{padding:18px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(145deg,#F5F8FF,#EEF3FC)}.scenario h3{margin:0 0 6px;font-size:15px}.scenario .big{font-size:24px;font-weight:900;color:var(--accent)}.scenario p{color:var(--muted);font-size:11px;margin:6px 0}.muted{color:var(--muted)}.small{font-size:11px}.tableWrap{overflow:auto}table{width:100%;border-collapse:collapse;font-size:12px}th,td{padding:10px 8px;border-bottom:1px solid rgba(15,27,45,.08);text-align:right}th:first-child,td:first-child{text-align:left}th{color:#5B6B84;font-weight:600}.notice{padding:12px 14px;border-radius:12px;background:#EEF2FF;border:1px solid var(--line);color:#5B6B84;font-size:12px}.error{color:#C22A3E;background:#FCE8EA;border:1px solid #E8B4BD;padding:12px;border-radius:12px;margin:15px 0}.hidden{display:none!important}.footer{padding:25px 0 50px;color:#5B6B84;font-size:11px;text-align:center}.tabs{display:flex;gap:8px;margin-top:16px}.tab{padding:8px 12px;border-radius:999px;background:#F0F3F8;border:1px solid var(--line);color:#5B6B84;cursor:pointer}.tab.active{background:#DCE6FB;color:var(--accent);border-color:#1D4ED8}.tabPanel{display:none}.tabPanel.active{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.hidePrint{display:block}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.chip{font-size:11.5px;background:#EEF2FF;border:1px solid var(--line);border-radius:999px;padding:6px 11px;color:#33415C}.chip b{color:var(--accent)}
.abar{height:9px;background:#E4E8EF;border-radius:99px;overflow:hidden;margin-top:6px}.abar i{display:block;height:100%;background:linear-gradient(90deg,#8aa7ff,#ff8290);border-radius:99px}
.custRow{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(15,27,45,.08);font-size:12.5px}
.highlight-target{outline:2px solid var(--accent);outline-offset:6px}
/* --- Marketing surface additions --- */
.topNav{display:flex;gap:18px}
.topNav a{color:var(--muted);font-size:13px;text-decoration:none;font-weight:600}
.topNav a:hover{color:var(--accent)}
.marketingSection{padding:60px 0}
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
.navBtns a.secondary,.navBtns a.primary{text-decoration:none;display:inline-flex;align-items:center;font-weight:700}
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
.secBlock{padding:58px 0}
.secBlock.tint{background:linear-gradient(180deg,rgba(16,31,51,.55),rgba(10,23,39,.15));border-radius:32px;margin:0 -10px}
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
.secGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.secCard{padding:22px}
.secCard .scIco{width:38px;height:38px;border-radius:10px;background:#EAF0FF;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px}
.secCard h3{margin:0 0 7px;font-size:15px}
.secCard p{margin:0;color:var(--muted);font-size:12.5px;line-height:1.6}
@media(max-width:860px){.secGrid{grid-template-columns:1fr}}

</style></head>
<body>
<header class="top"><div class="wrap brand"><div><a href="/" style="text-decoration:none;color:inherit"><h1>Digital Finance Business Partner</h1><p>Verified financial facts → decision intelligence → management action</p></a></div><div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><nav class="topNav hidePrint" id="mainNav"><a href="/">Anasayfa</a><a href="/paketler">Paketler</a><a href="/hakkimizda">Hakkımızda</a><a href="/iletisim">İletişim</a><a href="/uygulama" class="active">Uygulama</a></nav><span class="badge v">Finance Core v__APP_VERSION__</span><div id="authArea"><button id="loginOpenBtn" class="secondary">Giriş Yap</button> <button id="registerOpenBtn" class="secondary">Kayıt Ol</button></div><button id="navToggle" class="navToggle hidePrint" aria-label="Menü">☰</button></div></div></header><div id="authModalOverlay" class="hidden" style="position:fixed;inset:0;background:rgba(15,27,45,.55);display:flex;align-items:center;justify-content:center;z-index:100">
  <div class="card" style="padding:26px;max-width:380px;width:92%">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px"><h3 id="authModalTitle" style="margin:0">Giriş Yap</h3><button id="authModalClose" class="secondary" style="padding:4px 10px">✕</button></div>
    <div style="display:flex;flex-direction:column;gap:10px">
      <input id="authEmail" class="select" style="width:100%" type="email" placeholder="E-posta">
      <input id="authPassword" class="select" style="width:100%" type="password" placeholder="Şifre (en az 6 karakter)">
      <input id="authCompany" class="select" style="width:100%" type="text" placeholder="Şirket adı (opsiyonel)">
      <button id="authSubmitBtn" class="primary" style="width:100%">Giriş Yap</button>
      <div id="authError" class="error hidden" style="margin:0"></div>
      <span id="authSwitchHint" class="small muted">Hesabın yok mu? <a href="#" id="authSwitchLink" style="color:var(--accent)">Kayıt ol</a></span>
    </div>
  </div>
</div>
<main class="wrap"><section class="hero"><div class="heroCard"><h2 class="heroTitle">Dosyanı yükle, <span style="color:var(--accent)">yönetim raporunu</span> gör.</h2><p class="heroText">Mizan veya finansal tablonuzu yükleyin — sistem hesapları doğrular, riskleri önceliklendirir, kök nedenleri açıklar ve yönetilebilir fırsatları 2 dakikada gösterir.</p><div class="framework"><span><b>WHAT</b> is happening?</span><span><b>WHY</b> is it happening?</span><span><b>SO WHAT</b> is the impact?</span><span><b>NOW WHAT</b> should management do?</span><span><b>WHAT IF</b> we change a key assumption?</span></div>
<div style="margin-top:14px;display:flex;flex-wrap:wrap;gap:10px;align-items:center"><button id="sampleBtn" class="secondary">📄 Tek dönem örnekle dene</button><button id="sampleTrendBtn" class="secondary">📊 İki dönemli örnekle dene (Trend Demo)</button><button id="sampleHubBtn" class="secondary">🗂️ Data Hub örnekle dene (Mizan + AR + AP + Stok + Satış)</button> <span id="sampleStatus" class="small muted" style="margin-left:8px"></span></div>
<div class="trustBar hidePrint">
<div class="item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>Önce hesap, sonra yorum — deterministik motor</div>
<div class="item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>KVKK kapsamında, kalıcı depolama isteğe bağlı</div>
<div class="item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 15l4-6 4 3 5-8"/></svg>33 analiz motoru, tek WHAT→WHY→NOW WHAT akışı</div>
</div>

<div class="tabs"><button class="tab active" data-tab="single">Tek dönem</button><button class="tab" data-tab="trend" id="trendTabBtn">Çok dönem / Trend</button><button class="tab" data-tab="datahub" id="hubTabBtn">Data Hub / Çoklu Veri</button></div><div id="single" class="tabPanel active"><input id="file" class="file" type="file" accept=".csv,.xlsx,.xls,.xlsm" multiple><select id="sector" class="select"><option value="">Genel</option></select><button id="analyze" class="primary">Analizi çalıştır</button></div><div id="trend" class="tabPanel"><input id="trendFiles" class="file" type="file" accept=".csv,.xlsx,.xls,.xlsm" multiple><select id="trendSector" class="select"><option value="">Genel</option></select><button id="analyzeTrend" class="primary">Trend analizi</button><span class="small muted">Dosyaları eski → yeni sırayla seç.</span></div><div id="datahub" class="tabPanel"><input id="hubFiles" class="file" type="file" accept=".csv,.xlsx,.xls,.xlsm" multiple><select id="hubSector" class="select"><option value="">Genel</option></select><button id="analyzeHub" class="primary">Tüm verileri analiz et</button><span class="small muted">Mizanı ekleyin; satış, AR/AP, stok dosyalarını tek tek veya birlikte yükleyin.</span></div><div id="error" class="error hidden"></div></div><div class="heroCard scoreCard"><div id="scoreRing" class="scoreRing" style="--score:0"><div class="scoreNum"><strong id="score">-</strong><span>Financial Health</span></div></div><div id="healthLabel" class="status">Dosya bekleniyor</div>
<div id="pvPreview" class="hidePrint" style="margin-top:18px;padding-top:16px;border-top:1px solid rgba(15,27,45,.10);text-align:left">
  <div class="pvLabel"><span><span class="dot"></span>Örnek Rapor Görünümü</span><span>canlı motor</span></div>
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
<div id="printCover" style="display:none"><h1>Digital Finance Business Partner</h1><div class="sub">Yönetim Kurulu Brifingi — Finansal Analiz Raporu &nbsp;|&nbsp; <span id="printDate"></span></div></div>
<div id="dashboard" class="hidden">

<section class="flowStep"><div class="flowLabel"><span class="n">1</span>What — Finansal Gerçekler<p>Şirkette gerçekte ne oldu</p></div><div class="flowSub">Yorum yok, sadece doğrulanmış rakamlar: kâr köprüsü, kâr kalitesi, borç/likidite yapısı ve nakit köprüsü.</div>
<div class="grid4"><div class="metric"><div class="label">Net Satış</div><div id="mSales" class="value">-</div><div class="sub">Revenue quality başlangıç noktası</div></div><div class="metric"><div class="label">Faaliyet Kârı</div><div id="mOp" class="value">-</div><div class="sub">Operating margin</div></div><div class="metric"><div class="label">Net Kâr</div><div id="mNet" class="value">-</div><div class="sub">Net margin</div></div><div class="metric"><div class="label">Net Borç</div><div id="mDebt" class="value">-</div><div class="sub">Debt less cash</div></div></div>
<div id="dupontCard" class="card hidden" style="margin-top:16px"><div class="sectionHead"><div><h2>DuPont Değer Ağacı Analizi (ROE Kırılımı)</h2><p>Özkaynak Kârlılığını (ROE) belirleyen üç ana motor: Kâr Marjı × Varlık Devir Hızı × Finansal Kaldıraç</p></div></div><div class="grid4"><div class="metric"><div class="label">Özkaynak Kârlılığı (ROE)</div><div id="dupontRoe" class="value">-</div><div class="sub">Hissedar Getirisi</div></div><div class="metric"><div class="label">Net Kâr Marjı</div><div id="dupontMargin" class="value">-</div><div class="sub">Operasyonel Kârlılık</div></div><div class="metric"><div class="label">Varlık Devir Hızı</div><div id="dupontTurnover" class="value">-</div><div class="sub">Varlık Verimliliği</div></div><div class="metric"><div class="label">Kaldıraç Çarpanı</div><div id="dupontLeverage" class="value">-</div><div class="sub">Varlık / Özkaynak Çarpanı</div></div></div><div id="dupontDiagnosis" class="chips" style="margin-top:12px"></div></div>
<div id="comparativeCard" class="card hidden" style="margin-top:16px"><div class="sectionHead"><div><h2>Karşılaştırmalı Analiz — Dönemsel Trend</h2><p>Yüklenen dönemler arasındaki değişim, yönü ve yönetim için anlamı</p></div></div><div id="comparativeCards" class="grid3" style="margin-top:4px"></div><div id="comparativeFindings" style="margin-top:14px"></div><div id="comparativeTable" class="tableWrap" style="margin-top:14px"></div></div>
<section style="margin-top:16px"><div id="profitQualityCard" class="card"><div class="sectionHead"><div><h2>Kâr Köprüsü &amp; Kâr Kalitesi</h2><p>Net satıştan net kâra giden yol ve bu kârın ne kadarının kalıcı/operasyonel olduğu — tek küme</p></div></div><div class="grid2"><div><div class="small muted" style="margin-bottom:8px">Kâr Köprüsü</div><div id="waterfall" class="waterfall"></div></div><div><div class="small muted" style="margin-bottom:8px">Kâr Kalitesi</div><div id="profitQuality"></div></div></div><div id="profitabilityCommentary" style="margin-top:14px"></div></div></section>
<div class="grid2" style="margin-top:16px"><div id="leverageCard" class="card"><div class="sectionHead"><div><h2>Kaldıraç &amp; Likidite</h2><p>Bilançonun taşıdığı finansal baskı</p></div></div><div id="liquidity" class="grid2"></div><div id="leverageCommentary" style="margin-top:14px"></div></div><div class="card"><div class="sectionHead"><div><h2>İşletme Sermayesi</h2><p>Nakit dönüşüm süresi (CCC) ve bağlı nakit</p></div></div><div id="workingCapital"></div></div></div>
<div class="grid2" style="margin-top:16px"><div id="cashFlowCard" class="card"><div class="sectionHead"><div><h2>Nakit Akış Köprüsü</h2><p>Açılış nakitten kapanış nakde giden yol</p></div></div><div id="cashFlow"></div></div><div id="cashRealizationCard" class="card"><div class="sectionHead"><div><h2>Kâr Nakde Dönüşüyor mu?</h2><p>Net kârın ne kadarı gerçekten kasaya nakit olarak giriyor</p></div></div><div id="cashRealization"></div></div></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">2</span>So What — İş Etkisi<p>Bu rakamların işletme için anlamı ve maruziyeti</p></div><div class="flowSub">Hangi bulgu önce ele alınmalı, sektöre göre konum ne — önceliklendirme burada başlar.</div>
<div class="card"><div class="sectionHead"><div><h2>Priority Risks</h2><p>Skor, şiddet ve finansal maruziyet birlikte değerlendirilir.</p></div></div><div id="risks"></div></div>
<div class="card"><div class="sectionHead"><div><h2>Benchmark</h2><p>Yön duyarlı, gösterge amaçlı sektör bantları</p></div></div><div id="benchmark"></div></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">3</span>Kritik Taraflar & Operasyonel Zeka<p>Hangi müşteri/tedarikçi/stok kalemi kararı etkiliyor</p></div><div class="flowSub">Bu bölüm teknik bir ek değil — nakit ve kâr üzerinde en çok etkisi olan taraflar burada. Data Hub'a satış/AR/AP/stok dosyası yüklendiğinde otomatik dolar.</div>
<div id="criticalPartiesNotice" class="notice">Bu bölüm "Data Hub / Çoklu Veri" sekmesinden satış, AR/AP veya stok dosyası yüklendiğinde otomatik dolar.</div>
<div id="criticalCustomersCard" style="margin-top:14px"></div>
<div id="criticalSuppliersCard" style="margin-top:14px"></div>
<div class="grid2" style="margin-top:14px"><div id="salesIntel"></div><div id="arApIntel"></div></div><div id="inventoryIntel" style="margin-top:14px"></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">4</span>Why — Kök Neden<p>Bu neden oldu</p></div><div class="flowSub">Bulgu → kanıt → olası neden → gerekli ek kanıt. Buradaki nedensel zincir, eksik/zayıf alanları da kapsar; ayrı bir liste tekrarlanmaz.</div>
<div id="rootCauseCard" class="card"><div id="rootCause"></div></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">5</span>Senaryo Anlatıları — Ne Oldu / Neden / Maliyeti Ne / Ne Yapmalı<p>Kök nedenin, tek tek okunabilir hikâyelere dönüşmüş hali</p></div><div class="flowSub">Her kart, yukarıdaki What/So What/Why adımlarında zaten hesaplanmış rakamlardan üretilir; burada yeni bir sayı türetilmez. Aynı anda birden fazla bağımsız senaryo (risk veya iyileşme) tetiklenebilir; bu kartlar bir sonraki adımdaki (Now What) aksiyonların gerekçesidir.</div>
<div id="narrativeStories"></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">6</span>Now What — Yönetim Aksiyonları<p>Yönetim şimdi ne yapmalı</p></div><div class="flowSub">Bulgu → aksiyon → sahip → KPI. Aynı ticari konuya değen aksiyonlar tek kartta gruplanır; her aksiyon metni kendi madde numarasıyla ayrı ayrı listelenir.</div>
<div class="card"><div id="actions"></div></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">7</span>What If — Fırsatlar &amp; Senaryo Simülatörü<p>Kilit bir varsayımı değiştirirsek ne olur</p></div><div class="flowSub">Her fırsat, hesaplama formülü ve dayandığı varsayımla birlikte gösterilir.</div>
<div class="card"><div id="opportunities" class="grid3"></div></div>
<div id="interactiveScenarioCard" class="card" style="margin-top:16px"><div class="sectionHead"><div><h2>İnteraktif Senaryo Laboratuvarı &amp; Nakit Simülatörü</h2><p>Sürgüleri hareket ettirerek serbest kalacak nakdi ve kâr etkisini anında simüle edin</p></div></div><div class="grid2"><div style="display:flex;flex-direction:column;gap:14px"><div><div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px"><span>Alacak Tahsilatını Hızlandır (DSO Azaltma)</span><b id="sliderDsoVal" style="color:var(--accent)">0 gün</b></div><input id="sliderDso" type="range" min="0" max="60" value="0" step="1" style="width:100%;cursor:pointer"></div><div><div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px"><span>Brüt Kâr Marjı Artışı (Fiyatlama / Maliyet)</span><b id="sliderMarginVal" style="color:var(--accent)">+0.0%</b></div><input id="sliderMargin" type="range" min="0" max="5.0" value="0" step="0.1" style="width:100%;cursor:pointer"></div><div><div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px"><span>Faaliyet Gideri (OpEx) Tasarrufu</span><b id="sliderOpexVal" style="color:var(--accent)">0%</b></div><input id="sliderOpex" type="range" min="0" max="15" value="0" step="1" style="width:100%;cursor:pointer"></div><div><div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:4px"><span>Borç Ödeme / İtfa (Nakit ile)</span><b id="sliderDebtVal" style="color:var(--accent)">0%</b></div><input id="sliderDebt" type="range" min="0" max="40" value="0" step="5" style="width:100%;cursor:pointer"></div></div><div style="background:rgba(15,27,45,.6);border:1px solid var(--line);border-radius:15px;padding:18px;display:flex;flex-direction:column;justify-content:center;gap:12px"><div style="font-size:12px;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:1px">Simüle Edilen Bütünleşik Etki</div><div class="grid2"><div class="metric" style="background:#EAF0FF"><div class="label">Tahmini Serbest Kalan Nakit</div><div id="simCashImpact" class="value" style="color:var(--green)">0 TL</div><div class="sub">Likiditeye anlık katkı</div></div><div class="metric" style="background:#EAF0FF"><div class="label">Tahmini Ek Faaliyet Kârı</div><div id="simProfitImpact" class="value" style="color:var(--accent)">0 TL</div><div class="sub">Yıllık P&amp;L etkisi</div></div></div><div id="simSummaryText" class="small muted" style="line-height:1.5;margin-top:4px">Sürgüleri hareket ettirerek yönetim senaryonuzu belirleyin.</div></div></div></div>
</section>

<section class="flowStep"><div class="flowLabel"><span class="n">8</span>Yönetici Özeti — Deterministik CFO Anlatısı<span class="tag" style="margin-left:8px;background:#eef2ff;color:#3b4b8a">Kural Tabanlı · AI Değil</span><p>Yukarıdaki her şeyin tek paragrafta özeti</p></div><div class="flowSub">Önce hesaplanır, sonra yorumlanır: bu bölüm yeni bir rakam üretmez, yukarıdaki bulguları sabit kurallarla bir araya getirir ve yöneticinin bu raporla ne yapması gerektiğini söyler. Aşağıdaki "AI CFO yorumunu üret" butonu ise <b>isteğe bağlı</b> olarak bu doğrulanmış rakamları büyük dil modeline (Gemini) göndererek ek, serbest-metin bir yorum üretir — bu iki katman ayrı ayrı etiketlenmiştir, birbirine karıştırılmaz.</div>
<div class="card"><div id="exec" class="insight"></div><div id="execChips" class="chips"></div><div id="execDecision" style="margin-top:14px"></div><div style="margin-top:14px"><button id="aiBtn" class="secondary hidePrint">✨ AI CFO yorumunu üret (opsiyonel, LLM)</button> <button id="printBtn" class="secondary hidePrint">Raporu yazdır / PDF</button> <button id="jsonBtn" class="secondary hidePrint">JSON indir</button></div><div id="aiBox" class="notice hidden" style="margin-top:12px"></div><div id="methodNote" class="notice" style="margin-top:12px"></div><div style="margin-top:16px;padding-top:16px;border-top:1px solid rgba(15,27,45,.10)"><div style="display:flex;align-items:center;gap:8px;margin-bottom:10px"><span style="font-size:18px">💬</span><b style="font-size:14px">AI CFO'ya Özel Soru Sor (Stratejik Q&amp;A)</b><span class="tag" style="background:#EAF0FF;color:var(--accent)">Gemini 3.6 Flash Doğrulanmış</span></div><div style="display:flex;gap:10px;align-items:center"><input id="aiCustomPrompt" type="text" placeholder="Örn: Nakit neden oluşmuyor?" style="flex:1;background:#FFFFFF;border:1px solid #D7DEE8;color:#0F1B2D;border-radius:10px;padding:10px 14px;font-size:13px"><button id="aiAskBtn" class="primary hidePrint" style="white-space:nowrap;padding:10px 18px">Soruyu Yanıtla ⚡</button></div><div class="chips hidePrint" style="margin-top:10px"><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Nakit neden oluşmuyor?')">💸 Nakit neden oluşmuyor?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Kâr neden düşüyor?')">📉 Kâr neden düşüyor?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Borç neden artıyor?')">📈 Borç neden artıyor?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Kâr gerçekten nakde dönüşüyor mu?')">🔄 Kâr gerçekten nakde dönüşüyor mu?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Hangi müşteriler risk yaratıyor?')">⚠️ Hangi müşteriler risk yaratıyor?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Hangi tedarikçiler kritik?')">🏭 Hangi tedarikçiler kritik?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Stok neden şişiyor?')">📦 Stok neden şişiyor?</span><span class="chip" style="cursor:pointer" onclick="setAiPrompt('Büyüme neden kâra dönüşmüyor?')">🚀 Büyüme neden kâra dönüşmüyor?</span></div><div id="aiCustomBox" class="notice hidden" style="margin-top:14px"></div></div></div>
</section>

<section class="flowStep"><div class="flowLabel alt"><span class="n">+</span>Ek A — Kaynak Verisi & Veri Kalitesi<p>Analizin dayandığı verinin doğrulanma düzeyi ve dosya bazlı kırılım</p></div>
<div class="card"><div class="sectionHead"><div><h2>Data Quality</h2><p>Skorlar ve bulgular, buradaki veri güvenilirliğine dayanır</p></div></div><div class="grid4"><div class="metric"><div class="label">Data Quality Score</div><div id="dq" class="value">-</div><div class="sub" id="dqStatus">-</div></div><div class="metric"><div class="label">Calculation Audit</div><div id="auditValue" class="value">-</div><div class="sub" id="auditSub">-</div></div><div class="metric"><div class="label">Unmapped Accounts</div><div id="dqUnmapped" class="value">-</div><div class="sub">Eşlenemeyen hesap sayısı</div></div><div class="metric"><div class="label">CCC</div><div id="cccMetric" class="value">-</div><div class="sub">Gün</div></div></div><div id="dqChecks" class="tableWrap" style="margin-top:16px"></div><div id="dqIssues" style="margin-top:12px"></div><div id="dqNote" class="notice" style="margin-top:12px"></div></div>
<section id="dataHubCard" class="card hidden"><div class="sectionHead"><div><h2>Data Hub Intelligence</h2><p>Dosya sınıflandırma, kaynak bazlı analiz ve GL mutabakatı</p></div></div><div id="hubSummary" class="grid4"></div><div id="hubSources" class="card" style="margin-top:14px"></div><div id="hubFindings" class="card" style="margin-top:14px"></div><div id="pvmIntel" class="card hidden" style="margin-top:14px"></div><div id="hubReconciliation" class="card" style="margin-top:14px"></div></section>
</section>

<section class="flowStep"><div class="flowLabel alt"><span class="n">+</span>Ek B — Trend, İzlenebilirlik & Kaynak Tablolar<p>Çok dönem yüklendiğinde hareketi gösterir; her sayı kaynağına izlenebilir</p></div>
<div class="card"><div id="trendBlock"></div><div id="trace" class="tableWrap" style="margin-top:15px"></div></div>
<div class="card" style="margin-top:16px"><div class="sectionHead"><div><h2>Financial Statements</h2><p>Hesaplanan bilanço ve gelir tablosu (kaynak veri)</p></div></div><div class="grid2"><div id="plTable" class="tableWrap"></div><div id="bsTable" class="tableWrap"></div></div></div>
</section>

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
function metric(label,value,sub){return '<div class="metric"><div class="label">'+esc(label)+'</div><div class="value">'+esc(value)+'</div><div class="sub">'+esc(sub||'')+'</div></div>'}
function setRing(v){$('scoreRing').style.setProperty('--score',Math.max(0,Math.min(100,v||0)));$('score').textContent=v==null?'–':Math.round(v)}
function waterfall(elId,rows){const max=Math.max(...rows.map(x=>Math.abs(x[1]||0)),1);$(elId).innerHTML=rows.map(r=>'<div class="wf '+(r[2]?'neg':'')+'"><div class="num">'+money(r[1]).replace(' TL','')+'</div><div class="col" style="height:'+Math.max(4,Math.abs(r[1]||0)/max*135)+'px"></div><div class="lab">'+esc(r[0])+'</div></div>').join('')}


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

function render(d){
  LAST=d;$('dashboard').classList.remove('hidden');
  const bp=d.business_partner,pl=d.statements.profit_and_loss,bs=d.statements.balance_sheet,k=d.statements.kpis;
  setRing(bp.health_score);$('healthLabel').textContent=bp.health_label;

  // Step 1 — WHAT (financial facts)
  $('mSales').textContent=money(pl['Net sales']);$('mOp').textContent=money(pl['Operating profit']);$('mNet').textContent=money(pl['Net profit']);$('mDebt').textContent=money(k.net_debt);
  renderDuPont(bp.dupont_analysis||{});
  renderComparative(bp.trend_analysis||{});
  waterfall('waterfall',[['Net satış',pl['Net sales'],false],['COGS',-pl['COGS'],true],['Brüt kâr',pl['Gross profit'],false],['Faaliyet gideri',-pl['Operating expenses'],true],['Faaliyet kârı',pl['Operating profit'],false],['Finansman',-pl['Finance costs'],true],['Vergi',-pl['Tax expense'],true],['Net kâr',pl['Net profit'],false]]);
  const pq=bp.profit_quality_engine||{};
  $('liquidity').innerHTML=[['Current Ratio',rat(k.current_ratio),'higher is better'],['Cash Ratio',rat(k.cash_ratio),'liquid cash / current liabilities'],['Debt / Equity',rat(k.debt_to_equity),'lower is generally safer'],['Debt / Assets',pct(bp.derived_metrics.debt_to_assets_pct),'financing intensity']].map(x=>metric(x[0],x[1],x[2])).join('');
  $('leverageCommentary').innerHTML=leverageNarrative(bp.findings);
  const c=bp.cash_conversion_cycle||{};$('cccMetric').textContent=c.cash_conversion_cycle_days==null?'–':num(c.cash_conversion_cycle_days);$('workingCapital').innerHTML='<div class="grid4">'+[['DSO',c.dso_days],['DIO',c.dio_days],['DPO',c.dpo_days],['CCC',c.cash_conversion_cycle_days]].map(x=>metric(x[0],x[1]==null?'–':num(x[1])+' gün','')).join('')+'</div><div style="margin-top:12px">'+workingCapitalNarrative(c)+'</div>';

  const cb=bp.cash_bridge_engine||{};
  if(cb.available){
    $('cashFlow').innerHTML='<div id="cashFlowWf" class="waterfall"></div><div class="notice" style="margin-top:12px">Nakit değişimi: '+money(cb.cash_change)+'. '+esc(cb.note||'')+'</div>';
    waterfall('cashFlowWf',[['Açılış Nakit',cb.opening_cash,false],['Faaliyet Kârı',cb.operating_profit,false],['Alacak Etkisi',cb.working_capital_components.receivables_effect,cb.working_capital_components.receivables_effect<0],['Stok Etkisi',cb.working_capital_components.inventory_effect,cb.working_capital_components.inventory_effect<0],['Borç(AP) Etkisi',cb.working_capital_components.payables_effect,cb.working_capital_components.payables_effect<0],['Finansal Borç Δ',cb.debt_change,cb.debt_change<0],['Açıklanmayan',cb.unexplained_cash_change,cb.unexplained_cash_change<0],['Kapanış Nakit',cb.closing_cash,false]]);
  } else {
    const wp=cb.working_capital_proxy||{};
    $('cashFlow').innerHTML='<div class="notice">'+esc(cb.note||'Gerçek nakit akış köprüsü için en az iki dönem gerekir.')+'</div><div class="grid3" style="margin-top:12px">'+metric('Alacaklar',money(wp.receivables),'Working capital proxy')+metric('Stok',money(wp.inventory),'Working capital proxy')+metric('Borçlar (AP)',money(wp.payables),'Working capital proxy')+'</div><div class="notice" style="margin-top:10px">Trend sekmesinden en az 2 dönem yüklersen, açılıştan kapanışa gerçek nakit köprüsü burada görünür. <button class="secondary hidePrint" style="margin-left:8px" onclick="goToTrendTab()">İkinci dönemi şimdi yükle →</button></div>';
  }

  // "Kâr Nakde Dönüşüyor mu?" — net kârın ne kadarının işletme nakdine
  // dönüştüğünü gösteren köprü. cash_bridge_engine 2 dönem gerektirir; tek
  // dönemde neden hesaplanamadığını açıkça söyler, sessizce boş bırakmaz.
  if(cb.available && cb.cash_realization_pct!=null){
    const crp=cb.cash_realization_pct;
    const crTier=crp>=80?'positive':crp>=50?'medium':'high';
    $('cashRealization').innerHTML='<div class="metric" style="margin-bottom:12px"><div class="label">Net Kâr → İşletme Nakdi</div><div class="value">'+pct(crp)+'</div><div class="sub">Net kârın işletme nakdine dönüşen kısmı</div></div><div id="crWf" class="waterfall"></div><div class="insight '+crTier+'" style="margin-top:12px"><p>Net kâr '+money(cb.net_profit)+'; alacak/stok/borç (AP) hareketleri dahil edildiğinde işletme nakdi (proxy) '+money(cb.operating_cash_flow_proxy)+' oluyor — yani defter kârının yaklaşık <b>%'+num(crp)+'\u0027i</b> gerçekten kasaya giriyor. '+(crp<80?'Aradaki fark alacak tahsilatında, stokta veya tedarikçi ödemelerinde bağlı; "Working Capital" ve "AR/AP Intelligence" bölümleriyle birlikte okunmalı.':'Kâr büyük ölçüde nakde dönüşüyor; işletme sermayesi kâr üzerinde ek bir baskı yaratmıyor.')+'</p></div>';
    waterfall('crWf',[['Net Kâr',cb.net_profit,false],['Faaliyet Dışı/Vergi Farkı',cb.non_operating_addback,cb.non_operating_addback<0],['Alacak Etkisi',cb.working_capital_components.receivables_effect,cb.working_capital_components.receivables_effect<0],['Stok Etkisi',cb.working_capital_components.inventory_effect,cb.working_capital_components.inventory_effect<0],['Borç(AP) Etkisi',cb.working_capital_components.payables_effect,cb.working_capital_components.payables_effect<0],['İşletme Nakdi (proxy)',cb.operating_cash_flow_proxy,false]]);
  } else {
    $('cashRealization').innerHTML='<div class="notice">Bu köprü için en az iki dönem (Trend sekmesi) gerekir — tek dönemlik bir mizandan "kâr nakde döndü mü" sorusu güvenilir şekilde cevaplanamaz. Trend analizini çalıştırdığınızda net kârın ne kadarının işletme nakdine dönüştüğü burada hesaplanır.</div>';
  }

  // Step 2 — SO WHAT (business impact)
  const rr=bp.risk_ranking_engine?.ranked_risks||[];$('risks').innerHTML=rr.slice(0,8).map((r,i)=>'<div class="riskRow"><div class="rank">#'+r.rank+'</div><div><b>'+esc(r.title)+'</b><div class="riskScore">'+esc(r.category)+' · '+num(r.risk_score)+' / 100'+(r.estimated_exposure!=null?' · '+money(r.estimated_exposure):'')+'</div><div class="bar"><i style="width:'+Math.min(100,r.risk_score||0)+'%"></i></div></div><span class="tag '+String(r.risk_tier||'').toLowerCase()+'">'+esc(r.risk_tier)+'</span></div>').join('')||'<div class="notice">Öncelikli risk bulunmadı.</div>';
  $('profitQuality').innerHTML='<div class="grid2">'+metric('Gross Margin',pct(pq.gross_margin_pct),'')+metric('Operating Margin',pct(pq.operating_margin_pct),'')+metric('Net Margin',pct(pq.net_margin_pct),'')+metric('Finance Cost / Operating Profit',pct(pq.finance_cost_to_operating_profit_pct),'')+'</div>';
  $('profitabilityCommentary').innerHTML=profitabilityNarrative(pl,pq);
  const bm=bp.benchmarking||{};$('benchmark').innerHTML='<div class="notice">Sektör: <b>'+esc(bm.sector)+'</b> · '+esc(bm.overall_label)+' · '+esc(bm.overall_score)+'/100</div><div class="tableWrap" style="margin-top:8px"><table><thead><tr><th>Gösterge</th><th>Değer</th><th>Bant</th><th>Favorability</th></tr></thead><tbody>'+(bm.metrics||[]).map(m=>'<tr><td>'+esc(m.label)+'</td><td>'+esc(m.value)+'</td><td>'+esc(m.band_low)+' / '+esc(m.band_mid)+' / '+esc(m.band_high)+'</td><td>'+esc(m.favorability)+'</td></tr>').join('')+'</tbody></table></div>';

  // Step 3 — WHY (root cause; carries the "missing evidence" angle itself)
  const rc=bp.root_cause_engine||{};$('rootCause').innerHTML=(rc.causal_chains||[]).map(c=>{const ev=(c.evidence||[]).map(esc).join(' · ');const miss=(c.required_additional_evidence||[]).map(esc).join(' · ');const acts=(c.recommended_actions||[]).map(esc).join(' · ');return '<div class="insight" style="margin-bottom:10px"><h3>'+esc(c.title)+'</h3><div class="small muted">Primary driver: '+esc(c.primary_driver||'–')+' · '+esc(c.causal_status||'likely driver')+'</div><p><b>Chain:</b> '+(c.chain||[]).map(esc).join(' → ')+'</p>'+(ev?'<div class="small"><b>Evidence:</b> '+ev+'</div>':'')+(miss?'<div class="small muted" style="margin-top:5px"><b>Eksik kanıt:</b> '+miss+'</div>':'')+(c.financial_impact?'<div class="small" style="margin-top:5px"><b>Finansal etki:</b> '+esc(c.financial_impact)+'</div>':'')+(acts?'<div class="small" style="margin-top:5px"><b>Aksiyon:</b> '+acts+'</div>':'')+'</div>'}).join('')||'<div class="notice">Yeterli kök neden kanıtı yok.</div>';

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
  const accounts=d.canonical_model?.accounts||[];$('trace').innerHTML='<div class="notice">Traceability: '+accounts.length+' canonical account rows. Örnek kaynaklar aşağıda.</div><table style="margin-top:8px"><thead><tr><th>Hesap</th><th>Ad</th><th>Bakiye</th><th>Sheet</th><th>Row</th></tr></thead><tbody>'+accounts.slice(0,15).map(a=>'<tr><td>'+esc(a.account_code)+'</td><td>'+esc(a.account_name)+'</td><td>'+money(a.balance)+'</td><td>'+esc(a.source_sheet)+'</td><td>'+esc(a.source_row)+'</td></tr>').join('')+'</tbody></table>';
  setupInteractiveScenario(d);
}

// AR / AP Intelligence — full aging-engine output rendered with visual bars
// (bucket share, overdue share) instead of plain text-only rows.
function agingBlock(title,due,data){
  if(!data) return '<div class="notice">'+esc(title)+' verisi yüklenmedi.</div>';
  const buckets=(data.aging_buckets||[]).filter(b=>b.amount);
  const bucketRows=buckets.length?'<div style="margin-top:10px">'+buckets.map(b=>'<div style="margin-top:8px"><div class="small" style="display:flex;justify-content:space-between"><span>'+esc(b.bucket)+'</span><span>'+money(b.amount)+' · '+pct(b.pct_of_outstanding)+'</span></div><div class="abar"><i style="width:'+Math.min(100,b.pct_of_outstanding||0)+'%"></i></div></div>').join('')+'</div>':'';
  const overduePct=data.overdue_pct||0;
  const overdueBar='<div style="margin-top:10px"><div class="small" style="display:flex;justify-content:space-between"><span>Overdue oranı</span><span>'+pct(data.overdue_pct)+'</span></div><div class="abar"><i style="width:'+Math.min(100,overduePct)+'%"></i></div></div>';
  const topOverdue=(data.top_overdue_parties||[]).slice(0,5);
  const topOverdueRows=topOverdue.length?'<div class="small" style="margin-top:10px"><b>En çok geciken '+(title==='AR'?'müşteriler':'tedarikçiler')+':</b> '+topOverdue.map(p=>esc(p.name)+' ('+money(p.amount)+(p.avg_days_overdue!=null?', ort. '+num(p.avg_days_overdue)+' gün':'')+')').join(' · ')+'</div>':'';
  const riskTierTag=data.risk_tier?'<span class="tag '+(data.risk_tier==='Kritik'?'critical':data.risk_tier==='Yüksek'?'high':data.risk_tier==='Orta'?'medium':'positive')+'">'+esc(data.risk_tier)+'</span>':'';
  const partyWord=title==='AR'?'müşteri':'tedarikçi';
  const concTxt=data.concentration_80pct_party_count!=null?' · Toplamın %80\u0027ine <b>'+data.concentration_80pct_party_count+'</b> '+partyWord+' denk geliyor ('+esc(data.party_count??'–')+' '+partyWord+'\u0027nin %'+num(data.concentration_80pct_share_of_parties_pct)+'\u0027i)':'';
  const anomalyBlock=(data.data_anomalies&&data.data_anomalies.length)?'<p class="small" style="margin-top:8px;color:#9a6b00">⚠ Veri tuhaflığı: '+data.data_anomalies.map(esc).join(' · ')+'</p>':'';
  return '<div class="insight" style="margin-top:10px"><b>'+esc(title)+' Aging</b> '+riskTierTag+'<p>Outstanding: '+money(data.outstanding)+' · Overdue: '+money(data.overdue)+' · '+esc(due)+': '+(data[due==='DSO'?'dso_days':'dpo_days']==null?'–':num(data[due==='DSO'?'dso_days':'dpo_days'])+' gün')+'</p>'+overdueBar+'<p class="small muted" style="margin-top:8px">Ağırlıklı ort. gecikme: '+(data.weighted_average_overdue_days==null?'–':num(data.weighted_average_overdue_days)+' gün')+' · Beklenen tahsilat/ödeme riski: '+money(data.collection_risk_estimate)+' ('+pct(data.collection_risk_estimate_pct_of_outstanding)+') · İlk 10 taraf payı: '+pct(data.top_10_share_pct)+' ('+(data.party_count??'–')+' '+partyWord+')'+concTxt+'</p>'+anomalyBlock+bucketRows+topOverdueRows+'</div>'
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
  $('criticalCustomersCard').innerHTML=criticalCustomersPanel(an.ar_aging);
  $('criticalSuppliersCard').innerHTML=criticalSuppliersPanel(an.ap_aging);
  // Sales Intelligence trimmed to what actually informs a decision: pricing
  // policy (term premium) and product mix. Customer-level detail now lives
  // in the Kritik Müşteriler panel above, driven by the aging engine instead
  // of restating outstanding/paid totals that AR Aging already shows.
  $('salesIntel').innerHTML='<div class="sectionHead"><div><h2>Sales Intelligence</h2><p>Vade fiyatlaması ve ürün karması</p></div></div>'+(an.sales?'<div class="grid2">'+metric('Vade Primi',pct(sales.term_premium_pct),'Peşin → vadeli fark')+metric('İlk 10 Müşteri Payı',pct(sales.top_10_customer_share_pct),'Concentration')+'</div>'+((sales.product_mix||[]).length?'<div class="insight" style="margin-top:10px"><b>Ürün karması</b><p>'+sales.product_mix.slice(0,7).map(v=>esc(v.name)+': '+money(v.sales)+' ('+pct(v.share_pct)+')').join(' · ')+'</p></div>':'')+(sales.term_premium_pct>15?'<div class="insight high" style="margin-top:10px"><b>Vadeli satış fiyatı peşin fiyattan belirgin yüksek</b><p>Vade primi %'+num(sales.term_premium_pct)+'; finansman maliyeti ve tahsilat riski fiyatlamaya yansıtılıyor mu kontrol edilmeli.</p></div>':''):'<div class="notice">Sales datası yüklenmedi.</div>');
  $('arApIntel').innerHTML='<div class="sectionHead"><div><h2>AR / AP Intelligence</h2><p>Aging, risk yoğunlaşması ve tahsilat/ödeme riski</p></div></div>'+agingBlock('AR','DSO',an.ar_aging)+agingBlock('AP','DPO',an.ap_aging);
  const inv=an.inventory_aging||{}; $('inventoryIntel').innerHTML='<div class="sectionHead"><div><h2>Inventory Intelligence</h2><p>Stok değeri ve yaşlanma sinyalleri</p></div></div>'+(an.inventory_aging?'<div class="grid4">'+metric('Inventory Value',money(inv.value),'Inventory Data')+metric('SKU Count',inv.sku_count??'–','')+metric('DIO',inv.dio_days==null?'–':num(inv.dio_days)+' gün','')+metric('180+ Days',money(inv.stale_180_amount),'Stale stock')+'</div>'+(inv.findings||[]).map(f=>'<div class="insight '+esc(f.severity)+'" style="margin-top:10px"><b>'+esc(f.title)+'</b><p>'+esc(f.detail)+'</p></div>').join(''):'<div class="notice">Inventory datası yüklenmedi.</div>');
}
async function run(url,fd,kind='single'){$('error').classList.add('hidden');$('analyze').disabled=true;$('analyzeTrend').disabled=true;$('analyzeHub').disabled=true;try{const r=await fetch(url,{method:'POST',body:fd});const d=await r.json();if(!r.ok)throw new Error(d.detail||'Analiz başarısız');render(d);if(kind==='hub')renderHub(d.data_hub)}catch(e){$('error').textContent=e.message;$('error').classList.remove('hidden')}finally{$('analyze').disabled=false;$('analyzeTrend').disabled=false;$('analyzeHub').disabled=false}}
$('analyze').onclick=()=>{const fs=[...$('file').files];if(!fs.length){$('error').textContent='Önce en az bir dosya seç.';$('error').classList.remove('hidden');return}const fd=new FormData();if(fs.length===1){fd.append('file',fs[0]);if($('sector').value)fd.append('sector',$('sector').value);run('/api/mizan/analyze',fd)}else{fs.forEach(f=>fd.append('files',f));if($('sector').value)fd.append('sector',$('sector').value);run('/api/data-hub/analyze',fd,'hub')}};
$('sampleBtn').onclick=()=>runSample('mizan');
async function runSample(key){
  $('sampleBtn').disabled=true;$('sampleStatus').textContent='Örnek veri indiriliyor ve analiz ediliyor…';$('error').classList.add('hidden');
  try{
    const r=await fetch('/api/sample/'+encodeURIComponent(key));
    if(!r.ok)throw new Error('Örnek veri sunucudan alınamadı.');
    const blob=await r.blob();
    const file=new File([blob],key+'.xlsx',{type:blob.type});
    const fd=new FormData();fd.append('file',file);
    await run('/api/mizan/analyze',fd);
    $('sampleStatus').textContent='Örnek veri analizi tamamlandı — bu gerçek şirket verisi değildir, gösterim amaçlıdır.';
    window.scrollTo({top:0,behavior:'smooth'});
  }catch(e){$('error').textContent=e.message;$('error').classList.remove('hidden');$('sampleStatus').textContent='';}
  finally{$('sampleBtn').disabled=false;}
}
(function(){
  const _qp=new URLSearchParams(location.search);
  const _s=_qp.get('sample');
  if(_s){
    if(_s==='data_hub'){ setTimeout(()=>runDataHubSample(),150); }
    else { const key=(_s==='1')?'mizan':_s; setTimeout(()=>runSample(key),150); }
  }
})();
// One-click Data Hub demo: fetches a matching mizan + AR/AP aging + inventory + sales
// ledger sample set together and submits them as one multi-file Data Hub analysis,
// so AR/AP Intelligence, Inventory Intelligence and PVM actually have data to show.
const DATA_HUB_SAMPLE_KEYS=['hub_mizan','ar_aging','ap_aging','inventory','sales_ledger'];
async function runDataHubSample(){
  $('sampleHubBtn').disabled=true;$('sampleStatus').textContent='Data Hub örnek verileri indiriliyor (mizan + AR + AP + stok + satış)…';$('error').classList.add('hidden');
  try{
    const blobs=await Promise.all(DATA_HUB_SAMPLE_KEYS.map(async key=>{
      const r=await fetch('/api/sample/'+encodeURIComponent(key));
      if(!r.ok)throw new Error('Örnek veri sunucudan alınamadı: '+key);
      const blob=await r.blob();
      return new File([blob],key+'.xlsx',{type:blob.type});
    }));
    document.querySelector('[data-tab="datahub"]').click();
    const fd=new FormData();blobs.forEach(f=>fd.append('files',f));
    await run('/api/data-hub/analyze',fd,'hub');
    $('sampleStatus').textContent='Data Hub örnek analizi tamamlandı — mizan, AR/AP yaşlandırma, stok ve satış birlikte işlendi. Bu gerçek şirket verisi değildir.';
    window.scrollTo({top:0,behavior:'smooth'});
  }catch(e){$('error').textContent=e.message;$('error').classList.remove('hidden');$('sampleStatus').textContent='';}
  finally{$('sampleHubBtn').disabled=false;}
}
$('sampleHubBtn').onclick=()=>runDataHubSample();
$('analyzeTrend').onclick=()=>{const fs=[...$('trendFiles').files];if(fs.length<2){$('error').textContent='Trend analizi için en az 2 dönem seç.';$('error').classList.remove('hidden');return}const fd=new FormData();fs.forEach(f=>fd.append('files',f));if($('trendSector').value)fd.append('sector',$('trendSector').value);run('/api/mizan/analyze-trend',fd,'trend')};
$('analyzeHub').onclick=()=>{const fs=[...$('hubFiles').files];if(fs.length<1){$('error').textContent='Data Hub için en az bir dosya seçin. Mizan olmadan da satış / AR / AP / stok verisi analiz edilebilir.';$('error').classList.remove('hidden');return}const fd=new FormData();fs.forEach(f=>fd.append('files',f));if($('hubSector').value)fd.append('sector',$('hubSector').value);run('/api/data-hub/analyze',fd,'hub')};
function goToTrendTab(){$('trendTabBtn').click();window.scrollTo({top:0,behavior:'smooth'})}
document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>{document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));document.querySelectorAll('.tabPanel').forEach(x=>x.classList.remove('active'));t.classList.add('active');$(t.dataset.tab).classList.add('active')});
$('printBtn').onclick=()=>{
  const cov=$('printCover');
  const pd=$('printDate');
  if(cov&&pd){
    pd.textContent=new Date().toLocaleDateString('tr-TR',{year:'numeric',month:'long',day:'numeric'});
    cov.style.display='';
  }
  window.print();
  if(cov) cov.style.display='none';
};
$('jsonBtn').onclick=()=>{if(!LAST)return;const blob=new Blob([JSON.stringify(LAST,null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='finance_bp_analysis.json';a.click();URL.revokeObjectURL(a.href)};
function formatAi(v){if(v==null)return '';if(typeof v==='string')return esc(v);if(typeof v==='object'){if(v.title&&v.description)return '<b>'+esc(v.title)+':</b> '+esc(v.description);if(v.risk&&v.impact)return '<b>'+esc(v.risk)+':</b> '+esc(v.impact);if(v.action&&v.kpi)return '<b>'+esc(v.action)+'</b> (KPI: '+esc(v.kpi)+')';return esc(Object.values(v).map(x=>typeof x==='object'?JSON.stringify(x):x).join(' — '));}return esc(String(v));}
$('aiBtn').onclick=async()=>{if(!LAST){$('aiBox').classList.remove('hidden');$('aiBox').textContent='Lütfen önce bir mizan veya finansal tablo analiz edin.';return;}$('aiBtn').disabled=true;$('aiBox').classList.remove('hidden');let sec=0;$('aiBox').textContent='⏳ AI CFO yorumu hazırlanıyor (0 sn)...';const timer=setInterval(()=>{sec++;$('aiBox').textContent='⏳ AI CFO yorumu hazırlanıyor ('+sec+' sn)...';},1000);try{const r=await fetch('/api/ai/cfo-narrative',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({analysis:LAST})});clearInterval(timer);const d=await r.json();if(!d.available){$('aiBox').textContent=d.reason||'AI yapılandırılmamış.';return;}const x=d.response||{};const exec=Array.isArray(x.executive_message)?x.executive_message.map(m=>'<p style="margin:6px 0">'+formatAi(m)+'</p>').join(''):'<p style="margin:6px 0">'+esc(x.executive_message||'')+'</p>';const risks=(x.key_risks||[]).length?'<div style="margin-top:12px;font-weight:700;color:#b3261e">⚠️ Kritik Riskler:</div>'+(x.key_risks||[]).map(v=>'<div style="margin:4px 0">• '+formatAi(v)+'</div>').join(''):'';const acts=(x.actions||[]).length?'<div style="margin-top:12px;font-weight:700;color:#137333">🎯 Yönetim Aksiyonları:</div>'+(x.actions||[]).map(v=>'<div style="margin:4px 0">→ '+formatAi(v)+'</div>').join(''):'';const qs=(x.management_questions||[]).length?'<div style="margin-top:12px;font-weight:700;color:#1a73e8">❓ Yönetim Soruları:</div>'+(x.management_questions||[]).map(v=>'<div style="margin:4px 0">? '+formatAi(v)+'</div>').join(''):'';$('aiBox').innerHTML='<b style="font-size:15px">AI CFO View</b>'+exec+risks+acts+qs+'<div class="small muted" style="margin-top:10px">Model: '+esc(d.model)+(d.note?' ('+esc(d.note)+')':'')+' ('+sec+' sn)</div>';}catch(e){clearInterval(timer);$('aiBox').textContent='AI isteği başarısız: '+e.message;}finally{clearInterval(timer);$('aiBtn').disabled=false;}};
function renderDuPont(dp){
  if(!dp||dp.roe_pct==null){if($('dupontCard'))$('dupontCard').classList.add('hidden');return;}
  $('dupontCard').classList.remove('hidden');
  $('dupontRoe').textContent=pct(dp.roe_pct);
  $('dupontMargin').textContent=pct(dp.net_profit_margin_pct);
  $('dupontTurnover').textContent=rat(dp.asset_turnover);
  $('dupontLeverage').textContent=rat(dp.equity_multiplier);
  $('dupontDiagnosis').innerHTML=(dp.diagnosis||[]).map(d=>'<span class="chip">💡 '+esc(d)+'</span>').join('');
}

function setupInteractiveScenario(d){
  const pl=d.statements?.profit_and_loss||{};
  const k=d.statements?.kpis||{};
  const sales=Number(pl['Net sales']||0);
  const opex=Number(pl['Operating expenses']||0);
  const debt=Number(k.financial_debt||0);
  const fin=Number(pl['Finance costs']||0);

  function updateSim(){
    if(!$('sliderDso')) return;
    const dsoDays=Number($('sliderDso').value);
    const marginDeltaPct=Number($('sliderMargin').value);
    const opexCutPct=Number($('sliderOpex').value);
    const debtPayPct=Number($('sliderDebt').value);

    $('sliderDsoVal').textContent=dsoDays+' gün';
    $('sliderMarginVal').textContent='+'+marginDeltaPct.toFixed(1)+'%';
    $('sliderOpexVal').textContent=opexCutPct+'%';
    $('sliderDebtVal').textContent=debtPayPct+'%';

    const cashFromDso = sales > 0 ? (dsoDays / 365.0) * sales : 0;
    const profitFromMargin = (marginDeltaPct / 100.0) * sales;
    const profitFromOpex = (opexCutPct / 100.0) * opex;
    const debtRepaid = (debtPayPct / 100.0) * debt;
    const interestRate = (debt > 0 && fin > 0) ? (fin / debt) : 0.40;
    const interestSaved = debtRepaid * interestRate;
    const totalProfitImpact = profitFromMargin + profitFromOpex + interestSaved;

    $('simCashImpact').textContent=(cashFromDso>=0?'+':'')+money(cashFromDso);
    $('simProfitImpact').textContent=(totalProfitImpact>=0?'+':'')+money(totalProfitImpact);

    let narrative=[];
    if(dsoDays>0) narrative.push('Alacakların '+dsoDays+' gün erken tahsili kasaya <b>'+money(cashFromDso)+'</b> nakit girişi sağlar.');
    if(marginDeltaPct>0) narrative.push('Brüt marjdaki %'+marginDeltaPct.toFixed(1)+' iyileşme faaliyet kârına <b>'+money(profitFromMargin)+'</b> ekler.');
    if(opexCutPct>0) narrative.push('Faaliyet giderlerindeki %'+opexCutPct+' tasarruf doğrudan PBT\'ye <b>'+money(profitFromOpex)+'</b> yansır.');
    if(debtPayPct>0) narrative.push('Ödenen '+money(debtRepaid)+' borç sayesinde yıllık tahmini <b>'+money(interestSaved)+'</b> faiz tasarrufu sağlanır.');

    $('simSummaryText').innerHTML=narrative.length?narrative.join('<br>'):'Sürgüleri hareket ettirerek yönetim senaryonuzu belirleyin.';
  }

  ['sliderDso','sliderMargin','sliderOpex','sliderDebt'].forEach(id=>{
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
    $('aiCustomBox').textContent='Lütfen AI CFO\'ya sormak istediğiniz soruyu yazın veya yukarıdaki hazır başlıklardan birine tıklayın.';
    return;
  }
  $('aiAskBtn').disabled=true;
  $('aiCustomBox').classList.remove('hidden');
  let sec=0;
  $('aiCustomBox').textContent='⏳ AI CFO sorunuzu analiz ediyor (0 sn)...';
  const timer=setInterval(()=>{sec++;$('aiCustomBox').textContent='⏳ AI CFO sorunuzu analiz ediyor ('+sec+' sn)...';},1000);
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
    $('aiCustomBox').innerHTML='<div style="border-bottom:1px solid rgba(15,27,45,.12);padding-bottom:8px;margin-bottom:8px"><b style="color:var(--accent)">Soru:</b> <i>"'+esc(q)+'"</i></div><b style="font-size:15px">AI CFO Stratejik Değerlendirmesi</b>'+exec+risks+acts+qs+'<div class="small muted" style="margin-top:10px">Model: '+esc(d.model)+' ('+sec+' sn)</div>';
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
  $('authModalTitle').textContent=mode==='login'?'Giriş Yap':'Ücretsiz Kayıt Ol';
  $('authSubmitBtn').textContent=mode==='login'?'Giriş Yap':'Kayıt Ol';
  $('authCompany').style.display=mode==='register'?'block':'none';
  $('authSwitchHint').innerHTML=mode==='login'?'Hesabın yok mu? <a href="#" id="authSwitchLink" style="color:var(--accent)">Kayıt ol</a>':'Zaten hesabın var mı? <a href="#" id="authSwitchLink" style="color:var(--accent)">Giriş yap</a>';
  $('authSwitchLink').onclick=(e)=>{e.preventDefault();openAuthModal(mode==='login'?'register':'login');};
  $('authError').classList.add('hidden');
  $('authModalOverlay').classList.remove('hidden');
}
$('authModalClose').onclick=()=>$('authModalOverlay').classList.add('hidden');
$('authModalOverlay').onclick=(e)=>{if(e.target.id==='authModalOverlay')$('authModalOverlay').classList.add('hidden');};
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
(function(){const _qp=new URLSearchParams(location.search);const _m=_qp.get('auth');if(_m==='login'||_m==='register'){openAuthModal(_m);}})();
  }catch(e){$('authError').textContent=e.message;$('authError').classList.remove('hidden');}
  finally{$('authSubmitBtn').disabled=false;}
};
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
