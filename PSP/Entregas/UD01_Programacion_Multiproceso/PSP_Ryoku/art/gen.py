import sys, numpy as np
from PIL import Image
sys.path.insert(0,'/home/adrian/Documentos/Claude/50-Recursos/ryoku-arte')
from halftone_ryoku import halftone, to_rgba
rng=np.random.default_rng(7)

def sphere(W=1200,H=1200,light=(-.5,-.6)):
    y,x=np.mgrid[0:H,0:W].astype(np.float32)
    cx,cy,r=W/2,H/2,W*.44
    nx,ny=(x-cx)/r,(y-cy)/r; d=nx**2+ny**2; ins=d<1
    nz=np.sqrt(np.clip(1-d,0,1))
    l=nx*light[0]+ny*light[1]+nz*.7
    lum=np.clip(0.18+l/1.5,0,1)
    # curved bands (seigaiha-ish rings) for texture
    lum=np.clip(lum*(0.85+0.15*np.cos(np.hypot(nx+.3,ny+.3)*40)),0,1)
    return lum,ins

# 1 planeta/CPU: esfera media tinta
lum,ins=sphere()
m=halftone(lum,cell=9,gamma=1.1,contrast=1.5)
to_rgba(m,ins).save('art/esfera.png')

# 2 columna jonica
W,H=700,1400
y,x=np.mgrid[0:H,0:W].astype(np.float32)
lum=np.zeros((H,W),np.float32); alpha=np.zeros((H,W),bool)
cx=W/2
sh=(x>W*.2)&(x<W*.8)&(y>170)&(y<H-150)
u=(x-W*.2)/(W*.6)
flut=0.5+0.5*np.cos(u*2*np.pi*6)
base=np.clip(np.sin(u*np.pi),0,1)**.6
lum[sh]=(base*(0.55+0.45*flut))[sh]; alpha|=sh
cap=(y>90)&(y<170)&(x>W*.1)&(x<W*.9); lum[cap]=.8-.3*((y[cap]-90)/80); alpha|=cap
for cxv in (W*.14,W*.86):
    vol=np.hypot(x-cxv,y-150)<46; lum[vol]=np.clip(.9-np.hypot(x-cxv+8,y-150+8)/70,0,1)[vol]; alpha|=vol
ab=(y>60)&(y<95)&(x>W*.06)&(x<W*.94); lum[ab]=.85; alpha|=ab
bs=(y>H-150)&(y<H-90)&(x>W*.1)&(x<W*.9); lum[bs]=.75; alpha|=bs
bs2=(y>H-90)&(y<H-40)&(x>W*.04)&(x<W*.96); lum[bs2]=.6; alpha|=bs2
m=halftone(lum,cell=7,gamma=1.0,contrast=1.4); to_rgba(m,alpha).save('art/columna.png')

# 3 dither lluvia (fondo de datos) 
W,H=1600,900
y,x=np.mgrid[0:H,0:W].astype(np.float32)
lum=np.clip((x/W)**1.4*0.9+rng.random((H,W))*.0,0,1)
cols=rng.random(W//6+1)
streak=cols[(x//6).astype(int)]
lum=np.clip(lum*streak*1.3*(1-(y/H)**.6*.7),0,1)
mask=lum>rng.random((H,W))*.9
out=np.zeros((H,W,4),np.uint8); big=np.kron(mask,np.ones((1,1),bool))
out[mask]=(205,196,186,255)
Image.fromarray(out,'RGBA').resize((800,450),Image.NEAREST).save('art/lluvia.png')

# 4 torii
W,H=1200,1000
y,x=np.mgrid[0:H,0:W].astype(np.float32)
lum=np.zeros((H,W),np.float32); a=np.zeros((H,W),bool)
def rect(x0,x1,y0,y1,v):
    global lum,a
    s=(x>=x0)&(x<=x1)&(y>=y0)&(y<=y1); lum[s]=v; a|=s
for px in (230,970):
    s=(abs(x-px)<42)&(y>260); lum[s]=np.clip(.35+.65*(1-abs(x-px)/42)**.8,0,1)[s]; a|=s
rect(120,1080,170,235,.95); rect(170,1030,255,310,.8)
# kasagi curvature tips
for dx in (-1,1):
    t=(abs(x-600)>440)&(abs(x-600)<500)&(y>140)&(y<175)&(y<175-((abs(x-600)-440)*.5)+40); 
m=halftone(lum,cell=7,gamma=1.0,contrast=1.4); to_rgba(m,a).save('art/torii.png')
print('ok')
