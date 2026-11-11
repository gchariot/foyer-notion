import subprocess, math, random
C=dict(paper="#F7F0E6",cream="#EFE3D3",terra="#C4674B",clay="#E3AE92",sage="#8DA38A",sagel="#C8D5C0",brown="#5E4637",mustard="#D9A54C",blush="#F0CDBB",white="#FBF7F1")
W,H=800,500
R={ # bg, bowl color, food colors, kind
"curry":(C['sagel'],C['terra'],[C['mustard'],C['clay'],C['sage']],"bowl"),
"dahl":(C['blush'],C['sage'],[C['mustard'],C['terra']],"bowl"),
"pates":(C['cream'],C['white'],[C['terra'],C['mustard']],"plate"),
"gratin":(C['sagel'],C['terra'],[C['mustard'],"#E9C77E"],"dish"),
"soupe":(C['cream'],C['sage'],[C['terra'],C['clay']],"bowl"),
"omelette":(C['blush'],C['white'],[C['mustard'],C['sage']],"plate"),
"couscous":(C['cream'],C['clay'],[C['mustard'],C['sage'],C['terra']],"plate"),
"porridge":(C['sagel'],C['white'],["#E8D6B8",C['mustard']],"bowl"),
"poulet":(C['blush'],C['sage'],[C['mustard'],C['white'],C['terra']],"bowl"),
"crumble":(C['sagel'],C['terra'],["#E9C77E",C['clay']],"dish"),
}
for k,(bg,vessel,foods,kind) in R.items():
    random.seed(k); dots=''
    cx,cy=400,260
    if kind=="dish":
        base=f'<rect x="210" y="150" width="380" height="230" rx="40" fill="{vessel}"/><rect x="235" y="170" width="330" height="190" rx="30" fill="{foods[0]}"/>'
        for i in range(14): dots+=f'<circle cx="{random.randint(260,540)}" cy="{random.randint(195,335)}" r="{random.randint(10,20)}" fill="{foods[1]}"/>'
    else:
        r=170 if kind=="plate" else 150
        base=f'<circle cx="{cx}" cy="{cy}" r="{r+20}" fill="{vessel}"/><circle cx="{cx}" cy="{cy}" r="{r-25 if kind=="plate" else r-10}" fill="{foods[0]}"/>'
        for i in range(16):
            a=random.random()*6.28; d=random.random()*(r-60)
            dots+=f'<circle cx="{cx+d*math.cos(a):.0f}" cy="{cy+d*math.sin(a):.0f}" r="{random.randint(9,22)}" fill="{random.choice(foods[1:])}"/>'
    leaf=f'<path d="M650 400 q-60 -20 -70 -90 q60 10 70 90" fill="{C["sage"]}"/><path d="M110 120 q50 -10 70 -70 q-55 0 -70 70" fill="{C["sage"]}" opacity=".7"/>'
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"><rect width="100%" height="100%" fill="{bg}"/>{leaf}{base}{dots}</svg>'
    open(f'/tmp/art/r_{k}.svg','w').write(svg)
    subprocess.run(['rsvg-convert','-w',str(W),'-h',str(H),f'/tmp/art/r_{k}.svg','-o',f'/home/claude/foyer-notion/assets/recettes/{k}.png'],check=True)
from PIL import Image
ims=[Image.open(f'/home/claude/foyer-notion/assets/recettes/{k}.png').resize((320,200)) for k in R]
s=Image.new('RGB',(320*5,400),'white')
for i,im in enumerate(ims): s.paste(im,((i%5)*320,(i//5)*200))
s.save('/tmp/art/rec_sheet.png')
