import subprocess, os
W,H=1500,600
C=dict(paper="#F7F0E6",cream="#EFE3D3",terra="#C4674B",clay="#E3AE92",sage="#8DA38A",sagel="#C8D5C0",brown="#5E4637",mustard="#D9A54C",blush="#F0CDBB")
def svg(body,bg=C["paper"],w=W,h=H):
    grain=f'''<filter id="g"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0.37  0 0 0 0 0.27  0 0 0 0 0.21  0 0 0 0.07 0"/></filter>'''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs>{grain}</defs><rect width="100%" height="100%" fill="{bg}"/>{body}<rect width="100%" height="100%" filter="url(#g)"/></svg>'
covers={}
# Foyer: house arch, sun, hill
covers["foyer"]=svg(f'''
<circle cx="1180" cy="210" r="120" fill="{C['mustard']}"/>
<path d="M0 600 C 300 430 600 470 820 520 S 1300 470 1500 420 L1500 600Z" fill="{C['sagel']}"/>
<path d="M0 600 C 250 520 520 540 760 580 L760 600Z" fill="{C['sage']}"/>
<g transform="translate(560 170)">
 <path d="M0 330 L0 150 Q190 -40 380 150 L380 330Z" fill="{C['terra']}"/>
 <path d="M140 330 L140 220 Q190 170 240 220 L240 330Z" fill="{C['paper']}"/>
 <rect x="45" y="180" width="60" height="60" rx="30" fill="{C['blush']}"/>
 <rect x="275" y="180" width="60" height="60" rx="30" fill="{C['blush']}"/>
</g>
<circle cx="250" cy="170" r="46" fill="{C['clay']}" opacity=".7"/>
<circle cx="330" cy="240" r="22" fill="{C['clay']}" opacity=".5"/>''')
# Tâches: clothesline with linen
def linen(x,y,w,h,col,rx=10): return f'<path d="M{x} {y} h{w} v{h-20} q{-w/4} 26 {-w/2} 0 q{-w/4} -26 {-w/2} 0 Z" fill="{col}"/>'
covers["taches"]=svg(f'''
<circle cx="1320" cy="120" r="70" fill="{C['blush']}"/>
<path d="M-20 170 Q750 300 1520 170" stroke="{C['brown']}" stroke-width="5" fill="none"/>
{linen(230,205,170,220,C['terra'])}{linen(470,232,120,170,C['mustard'])}{linen(650,240,200,240,C['sage'])}{linen(910,232,130,160,C['clay'])}{linen(1100,212,170,210,C['sagel'])}
<g fill="{C['brown']}"><rect x="300" y="196" width="10" height="26" rx="4"/><rect x="520" y="222" width="10" height="26" rx="4"/><rect x="740" y="232" width="10" height="26" rx="4"/><rect x="965" y="222" width="10" height="26" rx="4"/><rect x="1180" y="203" width="10" height="26" rx="4"/></g>''')
# Stock: shelf of jars
def jar(x,w,h,col,lid):
    y=430-h
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w*0.22}" fill="{col}"/><rect x="{x+w*0.12}" y="{y-22}" width="{w*0.76}" height="28" rx="8" fill="{lid}"/><rect x="{x+w*0.2}" y="{y+h*0.35}" width="{w*0.6}" height="{h*0.28}" rx="6" fill="{C['paper']}" opacity=".85"/>'
covers["stock"]=svg(f'''
<rect x="0" y="430" width="1500" height="24" fill="{C['brown']}"/>
<rect x="0" y="454" width="1500" height="146" fill="{C['cream']}"/>
{jar(170,150,210,C['clay'],C['brown'])}{jar(360,120,160,C['sage'],C['brown'])}{jar(520,170,260,C['mustard'],C['brown'])}{jar(735,130,180,C['terra'],C['brown'])}{jar(910,150,230,C['sagel'],C['brown'])}{jar(1105,110,150,C['blush'],C['brown'])}{jar(1255,140,200,C['sage'],C['brown'])}
<circle cx="90" cy="120" r="40" fill="{C['mustard']}" opacity=".6"/>''')
# Repas: pot with steam, bowl, lemon
covers["repas"]=svg(f'''
<rect x="0" y="470" width="1500" height="130" fill="{C['cream']}"/>
<path d="M600 300 h300 v120 q0 70 -70 70 h-160 q-70 0 -70 -70Z" fill="{C['terra']}"/>
<rect x="580" y="285" width="340" height="30" rx="15" fill="{C['brown']}"/>
<rect x="540" y="330" width="60" height="18" rx="9" fill="{C['brown']}"/><rect x="900" y="330" width="60" height="18" rx="9" fill="{C['brown']}"/>
<g stroke="{C['clay']}" stroke-width="10" fill="none" stroke-linecap="round"><path d="M680 250 q-25 -40 0 -80 q25 -40 0 -80"/><path d="M750 250 q-25 -40 0 -80 q25 -40 0 -80"/><path d="M820 250 q-25 -40 0 -80 q25 -40 0 -80"/></g>
<path d="M1040 400 h220 q0 90 -110 90 q-110 0 -110 -90Z" fill="{C['sage']}"/>
<circle cx="1110" cy="392" r="26" fill="{C['mustard']}"/><circle cx="1170" cy="388" r="20" fill="{C['terra']}"/>
<ellipse cx="330" cy="455" rx="70" ry="48" fill="{C['mustard']}"/><path d="M330 408 q30 -40 70 -30 q-30 20 -70 30" fill="{C['sage']}"/>
<ellipse cx="200" cy="470" rx="45" ry="32" fill="{C['clay']}"/>''')
# Semaine: 7 day dots/cards + sun
days=''.join(f'<rect x="{170+i*170}" y="{200 if i%2 else 230}" width="130" height="{200 if i%2 else 170}" rx="65" fill="{c}"/>' for i,c in enumerate([C['terra'],C['clay'],C['mustard'],C['sage'],C['sagel'],C['blush'],C['terra']]))
covers["semaine"]=svg(days+f'<circle cx="1390" cy="110" r="55" fill="{C["mustard"]}" opacity=".7"/>')
# Démarrer: winding path + plant
covers["demarrer"]=svg(f'''
<path d="M-40 520 C 300 520 300 330 640 330 S 980 160 1300 160" stroke="{C['clay']}" stroke-width="44" fill="none" stroke-linecap="round" stroke-dasharray="2 70"/>
<circle cx="1300" cy="160" r="60" fill="{C['terra']}"/><circle cx="1300" cy="160" r="22" fill="{C['paper']}"/>
<g transform="translate(220 250)"><path d="M60 250 h120 l-18 110 h-84Z" fill="{C['terra']}" transform="translate(0 -110)"/>
<path d="M120 140 q-90 -40 -90 -130 q90 30 90 130" fill="{C['sage']}"/><path d="M120 140 q90 -60 70 -150 q-80 50 -70 150" fill="{C['sagel']}"/></g>''')
# Coulisses: neutral grid
grid=''.join(f'<rect x="{80+i*140}" y="{140+j*110}" width="110" height="80" rx="18" fill="{C["cream"] if (i+j)%3 else C["sagel"]}"/>' for i in range(10) for j in range(3))
covers["coulisses"]=svg(grid)
for k,v in covers.items():
    open(f'/tmp/art/{k}.svg','w').write(v)
    subprocess.run(['rsvg-convert','-w','1500','-h','600',f'/tmp/art/{k}.svg','-o',f'/home/claude/foyer-notion/assets/covers/{k}.png'],check=True)
# Icons 280x280
def icon(bg,glyph): return svg(f'<circle cx="140" cy="140" r="132" fill="{bg}"/>{glyph}',bg="none",w=280,h=280).replace('<rect width="100%" height="100%" fill="none"/>','')
P=C['paper']
icons={
"foyer":icon(C['terra'],f'<path d="M80 200 v-60 q60 -70 120 0 v60Z" fill="{P}"/><path d="M125 200 v-35 q15 -16 30 0 v35Z" fill="{C["terra"]}"/>'),
"taches":icon(C['sage'],f'<path d="M85 145 l35 35 l75 -85" stroke="{P}" stroke-width="22" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'),
"stock":icon(C['mustard'],f'<rect x="95" y="105" width="90" height="105" rx="22" fill="{P}"/><rect x="105" y="80" width="70" height="26" rx="8" fill="{P}"/>'),
"repas":icon(C['terra'],f'<path d="M75 140 h130 q0 70 -65 70 q-65 0 -65 -70Z" fill="{P}"/><path d="M115 115 q-12 -20 0 -40 M160 115 q-12 -20 0 -40" stroke="{P}" stroke-width="10" fill="none" stroke-linecap="round"/>'),
"semaine":icon(C['clay'],f'<rect x="80" y="90" width="120" height="110" rx="18" fill="{P}"/><rect x="80" y="90" width="120" height="30" rx="12" fill="{C["brown"]}"/><circle cx="115" cy="155" r="10" fill="{C["terra"]}"/>'),
"demarrer":icon(C['sage'],f'<path d="M140 70 l55 70 h-30 v70 h-50 v-70 h-30Z" fill="{P}"/>'),
"coulisses":icon(C['brown'],f'<g fill="{P}"><rect x="85" y="85" width="45" height="45" rx="10"/><rect x="150" y="85" width="45" height="45" rx="10"/><rect x="85" y="150" width="45" height="45" rx="10"/><rect x="150" y="150" width="45" height="45" rx="10"/></g>'),
}
for k,v in icons.items():
    open(f'/tmp/art/i_{k}.svg','w').write(v)
    subprocess.run(['rsvg-convert','-w','280','-h','280',f'/tmp/art/i_{k}.svg','-o',f'/home/claude/foyer-notion/assets/icons/{k}.png'],check=True)
print('ok')
