import re

with open("backend/finance_engine/multi_source_intelligence.py", "r") as f:
    content = f.read()

replacement = """        if role=='sales':
            analysis=analyze_sales(combined,mappings); analysis['source_files']=file_names; result['analysis_sales']=analysis
            result['findings'].extend([{**f,'source':'sales'} for f in analysis.get('findings',[])])
            try:
                from .pvm_engine import build_pvm_analysis
                if 'date' in mappings and 'product' in mappings and 'quantity' in mappings and 'net_sales' in mappings:
                    combined['_pvm_period'] = pd.to_datetime(combined[mappings['date']], errors='coerce').dt.to_period('Y').astype(str)
                    pvm = build_pvm_analysis(combined, '_pvm_period', mappings['product'], mappings['quantity'], mappings['net_sales'])
                    if pvm.get('available'):
                        analysis['pvm_analysis'] = pvm
            except Exception as e:
                pass"""

content = re.sub(r"        if role=='sales':\n            analysis=analyze_sales\(combined,mappings\); analysis\['source_files'\]=file_names; result\['analysis_sales'\]=analysis\n            result\['findings'\].extend\(\[\{\*\*f,'source':'sales'\} for f in analysis.get\('findings',\[\]\)\]\)", replacement, content)

with open("backend/finance_engine/multi_source_intelligence.py", "w") as f:
    f.write(content)

