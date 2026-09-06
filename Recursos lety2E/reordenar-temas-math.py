"""Reordena el índice de un curso de Math: cards, colores, número de Tema y botones prev/next.
Uso: python3 reordenar.py <carpeta>   (el orden va en la lista ORDEN de abajo)"""
import re, sys, os, glob

ORDEN = ['reglas-basicas','velocidad-media','senos-cosenos','raices',
         'regla-producto-p1','regla-producto-p2','regla-cociente-p1','regla-cociente-p2',
         'regla-cadena-p1','regla-cadena-p2','recta-tangente','puntos-criticos',
         'optimizacion-areas','integrales-indefinidas','integrales-definidas',
         'area-bajo-curva-p1','area-bajo-curva-p2','derivada-definicion','suma-riemann',
         'historia-calculo']
COLORES = ['#FF00AA', '#00DEC8', '#4A0080']

os.chdir(sys.argv[1] if len(sys.argv) > 1 else '.')
idx = open('index.html', encoding='utf-8').read()
slugs = re.findall(r'<a href="([a-z0-9\-]+)\.html" class="content-card"', idx)
bloques = re.findall(r'<a href="[a-z0-9\-]+\.html" class="content-card".*?</a>', idx, re.S)
cards = dict(zip(slugs, bloques))
assert set(cards) == set(ORDEN), f'faltan/sobran: {set(cards) ^ set(ORDEN)}'
titulos = {s: re.search(r'<h1>(.*?)</h1>', open(f'{s}.html', encoding='utf-8').read()).group(1)
           for s in ORDEN}

nuevos = ['      ' + re.sub(r'--card-accent: #[0-9A-Fa-f]{6};',
                            f'--card-accent: {COLORES[i % 3]};', cards[s]).strip()
          for i, s in enumerate(ORDEN)]
ini = idx.index('<div class="content-grid">') + len('<div class="content-grid">')
fin = idx.index('    </div>\n\n    <p class="proximamente-nota">')
open('index.html', 'w', encoding='utf-8').write(idx[:ini] + '\n\n' + '\n\n'.join(nuevos) + '\n\n' + idx[fin:])

for i, s in enumerate(ORDEN):
    t = open(f'{s}.html', encoding='utf-8').read()
    t = re.sub(r'(Matemáticas 5 · Tema )\d+', rf'\g<1>{i+1}', t)
    btns = []
    if i > 0:
        a = ORDEN[i-1]; btns.append(f'      <a href="{a}.html" class="btn-anterior">← {titulos[a]}</a>')
    if i < len(ORDEN)-1:
        b = ORDEN[i+1]; btns.append(f'      <a href="{b}.html" class="btn-siguiente">{titulos[b]} →</a>')
    clase = 'topic-nav-btns solo-siguiente' if i == 0 else 'topic-nav-btns'
    nav = f'<div class="{clase}">\n' + '\n'.join(btns) + '\n    </div>'
    t, n = re.subn(r'<div class="topic-nav-btns[^"]*">.*?</div>', nav, t, count=1, flags=re.S)
    assert n == 1, f'{s}: no encontré el bloque de navegación'
    open(f'{s}.html', 'w', encoding='utf-8').write(t)

# verificación
idx = open('index.html', encoding='utf-8').read()
orden = re.findall(r'<a href="([^"]+)\.html" class="content-card"', idx)
probs = []
for i, s in enumerate(orden):
    t = open(f'{s}.html', encoding='utf-8').read()
    if int(re.search(r'Tema (\d+)</div>', t).group(1)) != i+1: probs.append(f'{s}: Tema')
    nav = re.search(r'<div class="topic-nav-btns[^"]*">.*?</div>', t, re.S).group(0)
    p = re.search(r'href="([^"]+)\.html" class="btn-anterior"', nav)
    n = re.search(r'href="([^"]+)\.html" class="btn-siguiente"', nav)
    if (p.group(1) if p else None) != (orden[i-1] if i else None): probs.append(f'{s}: anterior')
    if (n.group(1) if n else None) != (orden[i+1] if i < len(orden)-1 else None): probs.append(f'{s}: siguiente')
rotos = [f'{f}->{h}' for f in glob.glob('*.html')
         for h in re.findall(r'href="([a-z0-9\-]+\.html)"', open(f, encoding='utf-8').read())
         if not os.path.exists(h)]
for i, s in enumerate(orden):
    print(f'  {i+1:2}. {titulos[s]}')
print('\nEnlaces rotos:', rotos or 'ninguno')
print('Problemas:', probs or 'ninguno')
