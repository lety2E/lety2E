#!/usr/bin/env python3
"""Genera las versiones del examen en HTML, con el mismo aspecto que las
tarjetas de ejercicios del sitio lety2E. Minimalista: sin encabezado,
sin instrucciones, sin numeracion y sin puntaje."""
import json, os, html, re, base64, subprocess
from acomodo import examenes, revisar as acomodo_revisar
from cursos import elegir, archivo
import medida

SITIO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITIO_KATEX = os.path.join(SITIO, 'assets', 'katex')
EXAMENES_IEMS = os.path.expanduser('~/Desktop/IEMS/4 Materiales y evaluación/Exámenes')
_cache = {}

def destino(curso):
    """Dónde quedan los exámenes autocontenidos de un curso (una carpeta por curso)."""
    return os.path.join(EXAMENES_IEMS, curso)

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
/* El examen se imprime y se fotocopia por decenas: va en NEGRO SOBRE BLANCO,
   sin un solo color. Regla de Lety (8-sep-2026): gasta menos tinta y el
   fotocopiado sale limpio. Los rosas del sitio (#3D2525, #E0C4BC) salían
   grises y lavados al fotocopiar. */
:root{
  --bg-card:#FFFFFF;
  --text:#000000;
  --border:#000000;
  --r-md:12px;
  --font-body:'DM Sans',system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif;
  --font-display:'Playfair Display',Georgia,serif;
  /* Aire entre renglones (el sitio usa 2.4). Es la palanca para que
     el examen quepa en UNA hoja carta; la otra es el acomodo (ver acomodo.py).
     Con 49 ejercicios el examen ocupa ~97%% de la hoja: 2.4 lo dejaba justo en el
     borde y cualquier impresora lo pasaba a dos hojas. */
  --renglon:2.5;
}
*{box-sizing:border-box}
/* 12pt desde el 17-sep-2026: Lety imprimió la hoja a 10pt y la vio chica; con el
   Examen 1 al 80%% habia aire para crecer. A 12pt las seis versiones siguen en una hoja. */
body{margin:0;background:#fff;color:var(--text);font-family:var(--font-body);font-size:12pt}
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
  background:var(--bg-card);border:1px solid var(--border);
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
/* Figuras a 110px (eran 80): impresas a 80 los angulos casi no se leian. Y las
   etiquetas de los triangulos crecen en sus propias unidades (font-size del svg). */
.figura svg{max-width:100%;height:auto;max-height:110px;display:block;margin:.2rem auto}
.con-figura{display:flex;align-items:center;gap:.8rem;break-inside:avoid;-webkit-column-break-inside:avoid;page-break-inside:avoid}
.con-figura .figura{flex:0 0 auto;padding-left:0;text-indent:0}
/* en flex el svg sin medidas colapsa a 0x0: se le fija la altura y el ancho sale del viewBox */
.con-figura .figura svg{margin:.2rem 0;height:110px;width:auto;max-width:none}
.pegado,.pegado .katex,.pegado .katex-html{white-space:nowrap}
.figura svg text{font-size:15px;font-weight:700}
/* Las figuras llegan del sitio con su tinta de color (magentas y morados). En
   el examen van en escala de grises: la cuadricula clarita, los ejes gris
   medio y todo lo demas en negro. El relleno conserva su fill-opacity, asi que
   los triangulos quedan con un gris apenas visible. */
.figura svg [stroke]{stroke:#000}
.figura svg [stroke="#E0C4BC"]{stroke:#CCC}
.figura svg [stroke="#7B5A50"]{stroke:#555}
.figura svg [fill]:not([fill="none"]){fill:#000}
.figura svg [fill="#FBF2EF"]{fill:#FFF}

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

# Problemas con incisos ("... a) ... b) ... c) ..."): cada inciso en su renglon.
INCISOS = re.compile(r'(?<=[?$.])\s*(?=[a-d]\)\s)')

def con_incisos(tex):
    """Marca con un salto de linea el arranque de cada inciso."""
    return INCISOS.sub('\n', tex)

def texto_plano(t):
    """Limpia el aire que deja el extractor alrededor de las formulas ('$t=1$ , $t=3$ ?')."""
    t = html.escape(t)
    t = re.sub(r'\s+([,;:?.!])', r'\1', t)
    return t.replace('\n', '<br>')

def enunciado(tex):
    trozos = PARTE.split(separar_tuplas(con_incisos(tex)))   # [texto, formula, texto, ...]
    rendidas = render_tex(trozos[1::2]) if len(trozos) > 1 else []
    partes = [rendidas[i//2] if i % 2 else texto_plano(t) for i, t in enumerate(trozos)]
    # el signo que sigue a una formula ("$(1, 3)$?") se queda pegado a ella: el
    # navegador puede partir el renglon entre la formula y el signo
    for i in range(2, len(partes), 2):
        m = re.match(r'([?!,;.:]+)', partes[i])
        if m:
            partes[i-1] = '<span class="pegado">%s\u2060%s</span>' % (partes[i-1], m.group(1))
            partes[i] = partes[i][m.end():]
    return ''.join(partes).strip()

SIN_TEX = re.compile(r'\\[a-zA-Z]+|[${}]')

def partes_linea(item):
    """(tipo, texto plano, html). El tipo lo usa medida.py para la altura.
    Un reactivo con figura Y texto (Optimizacion: el rectangulo y su perimetro)
    devuelve dos partes; por eso partes() es lo que se usa desde afuera."""
    if 'svg' in item and 'tex' not in item:
        return 'figura', '', '<div class="ej-line libre figura">%s</div>' % item['svg']
    cuerpo = enunciado(item['tex'])
    # las frases en lenguaje comun se acomodan en varios renglones
    tipo = 'formula' if 'katex' in cuerpo[:40] else 'libre'
    clase = 'ej-line' if tipo == 'formula' else 'ej-line libre'
    # medida.py mide las formulas por tokens (con su LaTeX) y el texto por caracteres
    medible = item['tex'].strip('$ ') if tipo == 'formula' else SIN_TEX.sub('', con_incisos(item['tex']))
    return tipo, medible, '<div class="%s">%s</div>' % (clase, cuerpo)

def partes(item):
    """[(tipo, texto, html), ...] de un reactivo: la figura primero, si trae."""
    out = []
    if 'svg' in item and 'tex' in item:
        out.append(('figura', '', '<div class="ej-line libre figura">%s</div>' % item['svg']))
    out.append(partes_linea(item))
    return out

def linea(item):
    html_ = ''.join(p[2] for p in partes(item))
    # figura y renglon juntos, para que las columnas no los separen
    return '<div class="con-figura">%s</div>' % html_ if 'svg' in item and 'tex' in item else html_

def titulo_cuadro(tema, numero):
    """'4. Monomios' — los CUADROS van numerados con el numero del tema en el
    curso (el orden del indice del sitio, no el de la hoja), para nombrarlos al
    calificar; los ejercicios nunca (Lety, 17-sep-2026)."""
    return html.escape('%d. %s' % (numero, tema) if numero else tema)

def numeros_de(sel):
    """{titulo: numero del tema en el curso}. `sel` viene de seleccion.json, que
    guarda los temas en el orden del sitio (el de CURSOS en banco.py)."""
    return {t['titulo']: i + 1 for i, t in enumerate(sel)}

def tarjeta(tema, items, columnas, numero=0):
    clase = 'mini-card-body en-columnas' if columnas > 1 else 'mini-card-body'
    estilo = ' style="column-count:%d"' % columnas if columnas > 1 else ''
    return ('<div class="mini-card">'
            '<div class="mini-card-head">%s</div>'
            '<div class="%s"%s>%s</div>'
            '</div>' % (titulo_cuadro(tema, numero), clase, estilo,
                        ''.join(linea(i) for i in items)))

def hoja(sel, v, letra, plan, curso, numeros=None):
    titulo = '%s%s' % (curso, letra)
    porTitulo = {t['titulo']: t['versiones'][v] for t in sel}
    numeros = numeros or {}
    tarjetas = []
    for fila in plan:
        fila = [(t, p, c) for t, p, c in fila if porTitulo.get(t)]
        if not fila: continue
        anchos = ' '.join('%dfr' % p for _, p, _ in fila)
        celdas = ''.join(tarjeta(t, porTitulo[t], c, numeros.get(t, 0)) for t, _, c in fila)
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

def plan_medible(sel, v, plan):
    """El mismo plan, con lo que medida.py necesita para calcular la altura."""
    porTitulo = {t['titulo']: t['versiones'][v] for t in sel}
    filas = []
    for fila in plan:
        celdas = [(p, c, [q[:2] for i in porTitulo[t] for q in partes(i)])
                  for t, p, c in fila if porTitulo.get(t)]
        if celdas: filas.append(celdas)
    return filas

if __name__ == '__main__':
    curso, _ = elegir()
    sel = json.load(open(archivo('seleccion', curso)))
    for aviso in acomodo_revisar(curso, [t['titulo'] for t in sel]): print(aviso)
    carpeta = destino(curso)
    os.makedirs(carpeta, exist_ok=True)
    print('%s -> %s' % (curso, carpeta))
    for nombre, letras, plan in examenes(curso):
        temas = {t for fila in plan for t, _, _ in fila}
        recorte = [t for t in sel if t['titulo'] in temas]
        if not recorte:
            print('%s: ningun tema, se salta' % nombre); continue
        for v in range(len(recorte[0]['versiones'])):
            ruta = os.path.join(carpeta, '%s %s%s.html' % (nombre, curso, letras[v]))
            open(ruta, 'w', encoding='utf-8').write(hoja(recorte, v, letras[v], plan, curso, numeros_de(sel)))
            print(medida.informe(os.path.basename(ruta)[:-5],
                                 plan_medible(recorte, v, plan)))
