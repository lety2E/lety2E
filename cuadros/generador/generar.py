#!/usr/bin/env python3
"""Genera las versiones del examen en HTML, con el mismo aspecto que las
tarjetas de ejercicios del sitio lety2E. Minimalista: sin encabezado,
sin instrucciones, sin numeracion y sin puntaje."""
import json, os, html, re, base64, subprocess
from acomodo import examenes

SITIO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITIO_KATEX = os.path.join(SITIO, 'assets', 'katex')
DESTINO = os.path.expanduser('~/Desktop/IEMS/4 Materiales y evaluación/Exámenes/Matemáticas 1')
CURSO = 'Matemáticas 1'
_cache = {}

# ─────────────────────────── KaTeX ───────────────────────────

def render_tex(formulas):
    """Renderiza LaTeX a HTML con el KaTeX del sitio (una sola llamada a node)."""
    faltan = [f for f in formulas if f not in _cache]
    if faltan:
        p = subprocess.run(['node', 'render_katex.js'],
                           input=json.dumps({'formulas': faltan}),
                           capture_output=True, text=True, check=True)
        for tex, out in zip(faltan, json.loads(p.stdout)['html']):
            if isinstance(out, dict):
                raise SystemExit('KaTeX no pudo con: %s (%s)' % (out['tex'], out['error']))
            _cache[tex] = out
    return [_cache[f] for f in formulas]

def css_katex():
    """katex.min.css con las fuentes woff2 incrustadas: archivo autocontenido."""
    css = open(os.path.join(SITIO_KATEX, 'katex.min.css'), encoding='utf-8').read()
    def sustituir(m):
        ruta = os.path.join(SITIO_KATEX, m.group(1))
        if not m.group(1).endswith('.woff2') or not os.path.exists(ruta):
            return 'url()'
        return 'url(data:font/woff2;base64,%s)' % base64.b64encode(open(ruta,'rb').read()).decode()
    css = re.sub(r'url\((fonts/[^)]+)\)', sustituir, css)
    css = re.sub(r'url\(\)\s*format\("[a-z]+"\)\s*,?\s*', '', css)
    return re.sub(r'src:\s*;', '', css)

# ─────────────────────────── Estilo ───────────────────────────
# Tomado de las tarjetas de tema del sitio (.mini-card / .mini-card-head /
# .mini-card-body) y de sus variables de :root.

CSS = r'''
:root{
  --bg-card:#FFFFFF;
  --text:#3D2525;
  --border:#E0C4BC;
  --r-md:12px;
  --font-body:'DM Sans',system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif;
  --font-display:'Playfair Display',Georgia,serif;
  /* Aire entre renglones (el sitio usa 2.4). Es la palanca para que
     el examen quepa en UNA hoja carta; la otra es el acomodo (ver acomodo.py).
     Con 49 ejercicios el examen ocupa ~97%% de la hoja: 2.4 lo dejaba justo en el
     borde y cualquier impresora lo pasaba a dos hojas. */
  --renglon:2.3;
}
*{box-sizing:border-box}
body{margin:0;background:#fff;color:var(--text);font-family:var(--font-body);font-size:10pt}
.hoja{max-width:20.4cm;margin:0 auto;padding:.8cm}

.titulo{font-family:var(--font-display);font-size:.95rem;font-weight:700;
        margin:0 0 .5rem;letter-spacing:.01em;text-align:right}

/* La hoja se arma por filas, como los minipages: en cada fila los temas se
   reparten el ancho segun su peso (ver acomodo.py). */
.rejilla{display:flex;flex-direction:column;gap:.6rem}
.fila{display:grid;gap:.6rem;align-items:start;
      break-inside:avoid;-webkit-column-break-inside:avoid;page-break-inside:avoid}
@media (max-width:640px){.fila{grid-template-columns:1fr !important}}

.mini-card{
  background:var(--bg-card);border:1.5px solid var(--border);
  border-radius:var(--r-md);overflow:hidden;
  break-inside:avoid;-webkit-column-break-inside:avoid;page-break-inside:avoid;
  width:100%;min-width:0;
}
/* tarjeta ancha con muchos ejercicios cortos: se parten en columnas adentro */
.mini-card-body.en-columnas{column-gap:1.2rem}
.mini-card-body.en-columnas .ej-line{break-inside:avoid}
/* Titulo del tema: discreto y en negritas. Sin pestana de color: una barra
   solida en cada tarjeta gasta tinta de mas al fotocopiar. */
.mini-card-head{
  padding:.35rem .6rem 0;
  font-family:var(--font-display);font-size:.82rem;font-weight:700;
  line-height:1.25;
}
.mini-card-body{padding:.35rem .6rem .5rem;font-size:.9rem;line-height:var(--renglon)}
/* En el sitio los renglones son nowrap con scroll; en papel no hay scroll, asi
   que aqui las formulas largas se parten solas en sus operadores. La sangria
   francesa hace evidente que el renglon viene continuado. */
.ej-line{white-space:normal;padding-left:1.1em;text-indent:-1.1em}
.ej-line.libre{line-height:1.5;margin:.4rem 0;padding-left:0;text-indent:0}
.mini-card-body .katex,.mini-card-body .katex-html{white-space:normal}
.mini-card-body .katex{font-size:.95em}
.figura svg{max-width:100%;height:auto;max-height:80px;display:block;margin:.2rem auto}

@page{size:letter;margin:.9cm}
@media print{
  .hoja{padding:0;max-width:none}
}
'''

# ─────────────────────────── Armado ───────────────────────────

PARTE = re.compile(r'\$([^$]+)\$')
# listas de vertices: se parten en formulas sueltas para que el renglon pueda cortarse
TUPLAS = re.compile(r'^\s*\([^()]*\)(?:\s*,\s*\([^()]*\))+\s*$')

def separar_tuplas(texto):
    def sust(m):
        f = m.group(1)
        if not TUPLAS.match(f): return m.group(0)
        return ', '.join('$%s$' % p for p in re.findall(r'\([^()]*\)', f))
    return PARTE.sub(sust, texto)

def enunciado(tex):
    trozos = PARTE.split(separar_tuplas(tex))   # [texto, formula, texto, ...]
    rendidas = render_tex(trozos[1::2]) if len(trozos) > 1 else []
    return ''.join(rendidas[i//2] if i % 2 else html.escape(t)
                   for i, t in enumerate(trozos)).strip()

def linea(item):
    if 'svg' in item:
        return '<div class="ej-line libre figura">%s</div>' % item['svg']
    cuerpo = enunciado(item['tex'])
    # las frases en lenguaje comun se acomodan en varios renglones
    clase = 'ej-line' if 'katex' in cuerpo[:40] else 'ej-line libre'
    return '<div class="%s">%s</div>' % (clase, cuerpo)

def tarjeta(tema, items, columnas):
    clase = 'mini-card-body en-columnas' if columnas > 1 else 'mini-card-body'
    estilo = ' style="column-count:%d"' % columnas if columnas > 1 else ''
    return ('<div class="mini-card">'
            '<div class="mini-card-head">%s</div>'
            '<div class="%s"%s>%s</div>'
            '</div>' % (html.escape(tema), clase, estilo,
                        ''.join(linea(i) for i in items)))

def hoja(sel, v, letra, plan):
    titulo = '%s%s' % (CURSO, letra)
    porTitulo = {t['titulo']: t['versiones'][v] for t in sel}
    tarjetas = []
    for fila in plan:
        fila = [(t, p, c) for t, p, c in fila if porTitulo.get(t)]
        if not fila: continue
        anchos = ' '.join('%dfr' % p for _, p, _ in fila)
        celdas = ''.join(tarjeta(t, porTitulo[t], c) for t, _, c in fila)
        tarjetas.append('<div class="fila" style="grid-template-columns:%s">%s</div>'
                        % (anchos, celdas))
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Examen {titulo}</title>
<style>{css_katex()}</style>
<style>{CSS}</style>
</head>
<body>
<div class="hoja">
  <p class="titulo">{titulo}</p>
  <div class="rejilla">
{chr(10).join(tarjetas)}
  </div>
</div>
</body>
</html>
'''

if __name__ == '__main__':
    sel = json.load(open('seleccion.json'))
    os.makedirs(DESTINO, exist_ok=True)
    for nombre, letras, plan in examenes(CURSO):
        temas = {t for fila in plan for t, _, _ in fila}
        recorte = [t for t in sel if t['titulo'] in temas]
        if not recorte:
            print('%s: ningun tema, se salta' % nombre); continue
        for v in range(len(recorte[0]['versiones'])):
            ruta = os.path.join(DESTINO, '%s %s%s.html' % (nombre, CURSO, letras[v]))
            open(ruta, 'w', encoding='utf-8').write(hoja(recorte, v, letras[v], plan))
            print('escrito:', os.path.basename(ruta))
