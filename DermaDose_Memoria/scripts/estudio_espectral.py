"""Estudio reproducible de la memoria. Ejecutar con --repo RUTA_DERMADOSE --out CARPETA.
No modifica las tablas ni utiliza datos de pacientes. SpekPy 2.5.4.
"""
import argparse,csv,json,sys,hashlib,platform,importlib.metadata
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
sys.path.insert(0,str(a.repo.resolve()))
from skindose_verifier.spectral import generate_spectrum,integrate_spectrum,benchmark_reference
from skindose_verifier.surface_factors import WaterSurfaceDataset
out=a.out;out.mkdir(parents=True,exist_ok=True)
def savecsv(name,rows):
 with (out/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
report=benchmark_reference();(out/'comparacion_referencia.json').write_text(json.dumps(report,indent=2))
rows=[]
for cu in [0.,.1,.4]:
 e,phi,mu,audit=generate_spectrum(80.,4.1,cu)
 w=e*phi*mu*.5; w/=w.sum()
 for energy,f,k in zip(e,phi,w):rows.append({'energy_kev':energy,'cu_mm':cu,'fluence_rel_per_kev':f/(phi.sum()*.5),'kerma_rel_per_kev':k/.5})
savecsv('espectros_80kv.csv',rows)
for cu in [0.,.1,.4]:savecsv('espectro_cu_'+str(cu).replace('.','p')+'.csv',[r for r in rows if r['cu_mm']==cu])
rows=[]
for kvp,al,cu,side in [(50,2.5,0.,5.),(80,3.1,.1,20.),(100,4.1,.1,10.),(120,3.1,.3,25.)]:
 values=[]
 for dk in [1.,.5,.25,.125]:
  e,phi,mu,audit=generate_spectrum(kvp,al,cu,dk_kev=dk)
  r=integrate_spectrum(e,phi,mu,side,bin_width_kev=dk)
  values.append({'kvp':kvp,'al_mm':al,'cu_mm':cu,'side_cm':side,'dk_kev':dk,'C':r['combined_factor']})
 for r in values:r['difference_to_0125_percent']=100*(r['C']/values[-1]['C']-1)
 rows.extend(values)
savecsv('convergencia_espectral.csv',rows)
dataset=WaterSurfaceDataset(a.repo/'skindose_verifier/data/derived_azurion_spekpy')
rows=[]
for kvp in [55.,85.,115.]:
 for cu,side in [(.05,7.5),(.2,15.),(.3,30.)]:
  e,phi,mu,audit=generate_spectrum(kvp,4.1,cu)
  direct=integrate_spectrum(e,phi,mu,side,bin_width_kev=.5)
  pair=dataset.evaluate('clinical',inherent_al_mm=4.1,kvp=kvp,added_cu_mm=cu,field_side_cm=side)
  C=float(pair.k_bs*pair.k_f)
  rows.append({'kvp':kvp,'al_mm':4.1,'cu_mm':cu,'side_cm':side,'C_direct':direct['combined_factor'],'C_interpolated':C,'difference_percent':100*(C/direct['combined_factor']-1)})
savecsv('interpolacion_derivada.csv',rows)
rows=[]
for angle in [9.,12.,15.]:
 for al in [2.8,3.1,3.4]:
  e,phi,mu,audit=generate_spectrum(80.,al,.1,anode_angle_deg=angle)
  r=integrate_spectrum(e,phi,mu,20.,bin_width_kev=.5)
  rows.append({'angle_deg':angle,'fixed_al_mm':al,'C':r['combined_factor'],'hvl1_mm_al':audit['hvl1_mm_al']})
base=next(r['C'] for r in rows if r['angle_deg']==12. and r['fixed_al_mm']==3.1)
for r in rows:r['difference_percent']=100*(r['C']/base-1)
savecsv('sensibilidad_hipotesis.csv',rows)
versions={m:importlib.metadata.version(m) for m in ['spekpy','numpy','scipy','pydicom','trimesh','rtree','plotly','pytest']}
(out/'entorno.json').write_text(json.dumps({'python':platform.python_version(),'packages':versions},indent=2))
print(json.dumps({'benchmark_cases':len(report['cases']),'interpolation_max_abs_percent':max(abs(float(r['difference_percent'])) for r in list(csv.DictReader((out/'interpolacion_derivada.csv').open())))}))
