from pathlib import Path
import csv,json
out=Path(__file__).resolve().parents[1];data=out/'datos'
def num(x,n=4):return r'\num{'+f'{float(x):.{n}f}'+'}'
r=json.load(open(data/'comparacion_referencia.json'))['cases']
s='\\begin{tabular}{rrrrrrr}\\toprule\nkVp & Al & Cu & Lado & $C_{\\rm ref}$ & $C_{\\rm calc}$ & $\\delta_C$ (\\%)\\\\\\midrule\n'
for a in r:s+=' & '.join([str(a['kvp']),num(a['total_al_mm'],1),num(a['cu_mm'],1),str(int(a['field_side_cm'])),num(a['reference_combined'],6),num(a['derived']['combined_factor'],6),num(a['combined_difference_percent'],4)])+r'\\'+'\n'
s+=r'\bottomrule\end{tabular}'
(out/'datos/tabla_referencia.tex').write_text(s)
s='\\begin{tabular}{rrrrrr}\\toprule\nkVp & Al & Cu & HVL1 ref. & HVL1 calc. & $\\delta_{H_1}$ (\\%)\\\\\\midrule\n'
for a in r:s+=' & '.join([str(a['kvp']),num(a['total_al_mm'],1),num(a['cu_mm'],1),num(a['reference_hvl1_mm_al'],3),num(a['hvl1_mm_al'],3),num(a['hvl1_difference_percent'],3)])+r'\\'+'\n'
s+=r'\bottomrule\end{tabular}'
(out/'datos/tabla_hvl.tex').write_text(s)
rows=list(csv.DictReader((data/'convergencia_espectral.csv').open()))
s='\\begin{tabular}{rrrrr}\\toprule\nCaso & $\\Delta E=1$ & $\\Delta E=0{,}5$ & $\\Delta E=0{,}25$ & $\\Delta E=0{,}125$\\\\\\midrule\n'
for i in range(4):s+=str(i+1)+' & '+' & '.join(num(x['difference_to_0125_percent'],6) for x in rows[4*i:4*i+4])+r'\\'+'\n'
s+=r'\bottomrule\end{tabular}'
(out/'datos/tabla_convergencia.tex').write_text(s)
rows=list(csv.DictReader((data/'interpolacion_derivada.csv').open()))
s='\\begin{tabular}{rrrrrr}\\toprule\nkVp & Cu & Lado & $C_{\\rm directo}$ & $C_{\\rm interpolado}$ & $\\delta$ (\\%)\\\\\\midrule\n'
for r in rows:s+=' & '.join([num(r['kvp'],0),num(r['cu_mm'],2),num(r['side_cm'],1),num(r['C_direct'],6),num(r['C_interpolated'],6),num(r['difference_percent'],4)])+r'\\'+'\n'
s+=r'\bottomrule\end{tabular}'
(out/'datos/tabla_interpolacion.tex').write_text(s)
rows=list(csv.DictReader((data/'sensibilidad_hipotesis.csv').open()))
s='\\begin{tabular}{rrrrr}\\toprule\nÁngulo ($^\\circ$) & Al fijo (mm) & $C$ & HVL1 (mm Al) & $\\delta_C$ (\\%)\\\\\\midrule\n'
for r in rows:s+=' & '.join([num(r['angle_deg'],0),num(r['fixed_al_mm'],1),num(r['C'],6),num(r['hvl1_mm_al'],3),num(r['difference_percent'],4)])+r'\\'+'\n'
s+=r'\bottomrule\end{tabular}'
(out/'datos/tabla_sensibilidad.tex').write_text(s)
# Annex: one physically useful factor/HVL row per spectrum at 10 cm, all 78 qualities.
meta=json.load(open(out/'datos_fuente/derived_azurion_spekpy/metadata.json'))
cr=list(csv.DictReader(open(out/'datos_fuente/derived_azurion_spekpy/derived_clinical.csv')))
s='\\begin{longtable}{rrrrrrr}\n\\caption{Extracto verificable de las 78 calidades calculadas, para lado 10 cm. Espesores en mm y HVL1 en mm Al. No son medidas del equipo.}\\label{tab:78}\\\\\n\\toprule kVp & Al total & Cu & HVL1 & $B$ & $f_{\\rm eff}$ & $C$\\\\\\midrule\\endfirsthead\n\\toprule kVp & Al total & Cu & HVL1 & $B$ & $f_{\\rm eff}$ & $C$\\\\\\midrule\\endhead\n\\bottomrule\\endfoot\n'
for a in meta['spectra']:
 r=next(r for r in cr if float(r['field_side_cm'])==10 and float(r['kvp'])==a['kvp'] and float(r['inherent_al_mm'])==a['total_al_mm'] and float(r['added_cu_mm'])==a['cu_mm'])
 s+=' & '.join([num(a['kvp'],0),num(a['total_al_mm'],1),num(a['cu_mm'],1),num(a['hvl1_mm_al'],3),num(r['k_bs'],5),num(r['k_f'],5),num(float(r['k_bs'])*float(r['k_f']),5)])+r'\\'+'\n'
s+=r'\end{longtable}'
(out/'datos/tabla_78.tex').write_text(s)
