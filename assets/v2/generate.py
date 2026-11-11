"""Système visuel « L'étiqueteuse » pour le modèle Notion Foyer.
Génère couvertures, icônes, titres de section et couvertures de recettes
en SVG puis PNG (rsvg-convert). Police : Barlow Condensed (OFL), installée localement."""
import subprocess, random, os
OUT=os.path.dirname(os.path.abspath(__file__))
TAPE=dict(noir="#1D1D1B",rouge="#D7262B",bleu="#1F4E9B",vert="#1E7A46",jaune="#F2C230",gris="#5B5B5B")
KRAFT="#C3A47C"
FONT="Barlow Condensed"

def defs():
    return f'''<defs>
<filter id="kraft" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="3" seed="7"/>
<feColorMatrix values="0 0 0 0 0.42  0 0 0 0 0.31  0 0 0 0 0.19  0 0 0 0.22 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="fibre" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.35" numOctaves="2" seed="3"/>
<feColorMatrix values="0 0 0 0 0.55  0 0 0 0 0.42  0 0 0 0 0.27  0 0 0 0.18 0"/></filter>
<filter id="drop" x="-10%" y="-30%" width="120%" height="170%"><feDropShadow dx="0" dy="5" stdDeviation="5" flood-color="#3A2A18" flood-opacity=".38"/></filter>
<filter id="plastic" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9 0.04" numOctaves="2" seed="11"/>
<feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.06 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<linearGradient id="sheen" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset=".18" stop-color="#fff" stop-opacity=".05"/><stop offset=".85" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".25"/></linearGradient>
</defs>'''

def kraft_bg(w,h):
    return f'<rect width="{w}" height="{h}" fill="{KRAFT}"/><rect width="{w}" height="{h}" fill="{KRAFT}" filter="url(#kraft)"/><rect width="{w}" height="{h}" filter="url(#fibre)"/>'

def tape(x,y,text,col,fs=64,rot=0,seed=1,ink=None):
    """Ruban gaufré : retourne (svg, largeur)."""
    r=random.Random(seed+len(text))
    adv=fs*0.50; track=fs*0.16; pad=fs*0.55
    w=pad*2+len(text)*adv+(len(text)-1)*track; h=fs*1.45
    ink = ink or ("#1D1D1B" if col==TAPE['jaune'] else "#F3F1EA")
    letters=''
    cx=x+pad
    for ch in text:
        esc={'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;'}.get(ch,ch)
        if ch==' ':
            cx+=adv+track; continue
        dy=r.uniform(-fs*0.03,fs*0.03); base=y+h*0.5+fs*0.36+dy
        lx=cx+adv/2
        letters+=(f'<text x="{lx+1.6:.1f}" y="{base+1.8:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="800" font-size="{fs}" fill="#000" opacity=".35">{esc}</text>'
                  f'<text x="{lx-1:.1f}" y="{base-1:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="800" font-size="{fs}" fill="#fff" opacity=".35">{esc}</text>'
                  f'<text x="{lx:.1f}" y="{base:.1f}" text-anchor="middle" font-family="{FONT}" font-weight="800" font-size="{fs}" fill="{ink}">{esc}</text>')
        cx+=adv+track
    cut=fs*0.08
    shape=f'M{x+cut} {y} H{x+w-cut} L{x+w} {y+h*0.5} L{x+w-cut} {y+h} H{x+cut} L{x} {y+h*0.5} Z' if False else f'M{x} {y+2} Q{x} {y} {x+3} {y} H{x+w-3} Q{x+w} {y} {x+w} {y+2} V{y+h-2} Q{x+w} {y+h} {x+w-3} {y+h} H{x+3} Q{x} {y+h} {x} {y+h-2} Z'
    g=(f'<g transform="rotate({rot} {x+w/2:.0f} {y+h/2:.0f})"><g filter="url(#drop)"><path d="{shape}" fill="{col}"/></g>'
       f'<path d="{shape}" fill="url(#sheen)"/><path d="{shape}" fill="{col}" filter="url(#plastic)"/>{letters}</g>')
    return g,w

def svg(w,h,body,bg=True):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{defs()}{kraft_bg(w,h) if bg else ""}{body}</svg>'

def render(name,content,w,h):
    p=f'/tmp/{os.path.basename(name)}.svg'; open(p,'w').write(content)
    subprocess.run(['rsvg-convert','-w',str(w),'-h',str(h),p,'-o',os.path.join(OUT,name+'.png')],check=True)

# ---------- couvertures 2400x400 : Notion n'affiche qu'une bande, tout tient dans le centre ----------
COVERS={
 "foyer":(("FOYER","noir",120),[("TÂCHES","rouge"),("STOCK","bleu"),("REPAS","vert"),("À RACHETER","jaune")]),
 "taches":(("TÂCHES DU FOYER","rouge",84),[("QUI FAIT QUOI","noir"),("EN RETARD","rouge"),("AUJOURD'HUI","jaune")]),
 "stock":(("STOCK & COURSES","bleu",84),[("RÉSERVE","noir"),("QUOTIDIEN","gris"),("À RACHETER","jaune")]),
 "repas":(("REPAS","vert",120),[("MENU DE LA SEMAINE","noir"),("CUISINÉ","vert"),("100 % DISPO","jaune")]),
 "semaine":(("POINT DU DIMANCHE","noir",84),[("10 MIN","jaune"),("À DEUX","rouge")]),
 "demarrer":(("DÉMARRER","noir",120),[("15 MIN","jaune"),("PREMIÈRE FOIS","bleu")]),
 "coulisses":(("COULISSES","gris",110),[("NE PAS TOUCHER","noir")]),
}
ROTS=[1.2,-1.4,1.8,-0.8]
CW,CH=2400,400
# Notion recadre la couverture des deux côtés selon la largeur de fenêtre :
# la composition est centrée et tient dans la zone sûre (70 % central).
SAFE=CW*0.70
def cover_layout(t,c,fs,smalls,x0):
    bh=fs*1.45; sh=38*1.45
    g,w=tape(x0,CH/2-bh/2-6,t,TAPE[c],fs,-1.2,seed=len(t)); body=g
    x=x0+w+60
    for i,(st,sc) in enumerate(smalls):
        g,sw=tape(x,CH/2-28-sh/2+(14 if i%2 else -10),st,TAPE[sc],38,ROTS[i%4],seed=i+3)
        body+=g; x+=sw+30
    return body,x-30-x0
# Sur mobile, Notion ne garde que le centre (~35 % de la largeur) : le titre est
# centré et tient dans MOBILE ; les petites étiquettes se répartissent de chaque côté.
MOBILE=CW*0.36
def small_row(items,x0,seed0):
    body,x='',x0; sh=38*1.45
    for i,(st,sc) in enumerate(items):
        g,sw=tape(x,CH/2-28-sh/2+(14 if i%2 else -10),st,TAPE[sc],38,ROTS[(i+seed0)%4],seed=i+seed0)
        body+=g; x+=sw+30
    return body,x-30-x0
for k,(big,smalls) in COVERS.items():
    t,c,fs=big
    _,w=tape(0,0,t,TAPE[c],fs,-1.2,seed=len(t))
    while w>MOBILE: fs-=4; _,w=tape(0,0,t,TAPE[c],fs,-1.2,seed=len(t))
    bx=(CW-w)/2; bh=fs*1.45
    body,_=tape(bx,CH/2-28-bh/2-6,t,TAPE[c],fs,-1.2,seed=len(t))
    def split(items):
        L,R=[],[]
        for it in items:  # équilibre : chaque étiquette va du côté le plus court
            (L if small_row(L,0,7)[1]<small_row(R,0,3)[1] else R).append(it)
        return L,R
    room=bx-50-CW*0.08
    left,right=split(smalls)
    while max(small_row(left,0,7)[1],small_row(right,0,3)[1])>room:
        smalls=smalls[:-1]; left,right=split(smalls)
    _,lw=small_row(left,0,7)
    lb,_=small_row(left,bx-50-lw,7); rb,rw=small_row(right,bx+w+50,3)
    print(k,fs,round(w))
    render(f'covers/{k}',svg(CW,CH,body+lb+rb),CW,CH)

# ---------- icônes 280x280 : pastille de ruban + monogramme ----------
ICONS={"foyer":("F","noir"),"taches":("T","rouge"),"stock":("S","bleu"),"repas":("R","vert"),"semaine":("7","jaune"),"demarrer":("1","gris"),"coulisses":("C","gris")}
for k,(ch,c) in ICONS.items():
    g,w=tape(0,0,ch,TAPE[c],fs=150,seed=3)
    # centre la pastille dans 280x280
    body=f'<g transform="translate({(280-w)/2:.0f} {(280-150*1.45)/2:.0f})">{g}</g>'
    render(f'icons/{k}',svg(280,280,body,bg=False),280,280)

# ---------- titres de section : bande transparente 1600x170, ruban à gauche ----------
TITRES={"aujourdhui":("AUJOURD'HUI","noir"),"mes-taches":("MES TÂCHES","rouge"),"au-menu":("AU MENU","vert"),"a-racheter":("À RACHETER","jaune"),
        "a-faire":("À FAIRE","rouge"),"liste-courses":("LISTE DE COURSES","jaune"),"le-stock":("LE STOCK","bleu"),"cette-semaine":("CETTE SEMAINE","vert"),
        "livre-recettes":("LIVRE DE RECETTES","noir"),"etapes":("EN 5 ÉTAPES","noir"),"bon-a-savoir":("BON À SAVOIR","gris"),"pret-ce-soir":("PRÊT CE SOIR","vert")}
FULL_WIDTH={'pret-ce-soir'}
for k,(t,c) in TITRES.items():
    g,w=tape(12,24,t,TAPE[c],fs=78,seed=5)
    # titres posés en pleine largeur (hors colonnes) : canevas doublé pour garder la même taille affichée
    W=3200 if k in FULL_WIDTH else 1600
    render(f'titres/{k}',svg(W,170,g,bg=False),W,170)

# ---------- recettes 800x500 : kraft + étiquette du plat ----------
REC={"curry":("CURRY COCO","vert"),"dahl":("DAHL","jaune"),"pates":("PÂTES TOMATE","rouge"),"gratin":("GRATIN","noir"),"soupe":("SOUPE CAROTTE","rouge"),
     "omelette":("OMELETTE","jaune"),"couscous":("COUSCOUS","bleu"),"porridge":("PORRIDGE","gris"),"poulet":("POULET CURRY","vert"),"crumble":("CRUMBLE","noir")}
for k,(t,c) in REC.items():
    fs=96 if len(t)<9 else 74
    g,w=tape(0,0,t,TAPE[c],fs=fs,rot=-2,seed=9)
    body=f'<g transform="translate({(800-w)/2:.0f} {(500-fs*1.45)/2:.0f})">{g}</g>'
    render(f'recettes/{k}',svg(800,500,body),800,500)
# ---------- types de recette 800x500 : une couleur par type (alignée sur les options Notion) ----------
TYPES={"plat":("PLAT","rouge",-2),"batch":("BATCH COOKING","vert",1.5),"dessert":("DESSERT","jaune",-1),
       "petit-dej":("PETIT-DÉJ","gris",2),"soupe":("SOUPE","bleu",-1.5)}
for k,(t,c,rot) in TYPES.items():
    fs=96 if len(t)<9 else 78
    g,w=tape(0,0,t,TAPE[c],fs=fs,rot=rot,seed=len(t))
    body=f'<g transform="translate({(800-w)/2:.0f} {(500-fs*1.45)/2:.0f})">{g}</g>'
    render(f'types/{k}',svg(800,500,body),800,500)
print("ok")
