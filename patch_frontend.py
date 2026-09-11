import re

with open("backend/frontend_template.py", "r") as f:
    content = f.read()

html_replacement = r'<section id="dataHubCard" class="card hidden"><div class="sectionHead"><div><h2>Data Hub Intelligence</h2><p>Dosya sınıflandırma, kaynak bazlı analiz ve GL mutabakatı</p></div></div><div id="hubSummary" class="grid4"></div><div id="hubSources" class="card" style="margin-top:14px"></div><div id="hubFindings" class="card" style="margin-top:14px"></div><div id="pvmIntel" class="card hidden" style="margin-top:14px"></div><div id="hubReconciliation" class="card" style="margin-top:14px"></div></section>'

content = re.sub(r'<section id="dataHubCard" class="card hidden"><div class="sectionHead"><div><h2>Data Hub Intelligence</h2><p>Dosya sınıflandırma, kaynak bazlı analiz ve GL mutabakatı</p></div></div><div id="hubSummary" class="grid4"></div><div id="hubSources" class="card" style="margin-top:14px"></div><div id="hubFindings" class="card" style="margin-top:14px"></div><div id="hubReconciliation" class="card" style="margin-top:14px"></div></section>', html_replacement, content)


js_replacement = """  const an=ms.analysis||{}; const sales=an.sales||{};
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
"""

content = content.replace("  const an=ms.analysis||{}; const sales=an.sales||{};", js_replacement)

with open("backend/frontend_template.py", "w") as f:
    f.write(content)
