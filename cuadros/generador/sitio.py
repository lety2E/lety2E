#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escribe el sitio de exámenes a partir de seleccion.json.

Cada versión es su propia página (no una sola página con doce pestañas): así
carga rápido y se imprime tal cual. La barra de arriba hace de pestañas.

Las páginas usan el KaTeX, las tipografías y el `style.css` del propio sitio
(`assets/`), como manda su manual: cero CDNs y nada duplicado. En cambio los
exámenes que `generar.py` deja en IEMS sí llevan todo incrustado, porque ésos se
abren con doble clic y sin internet.

Se corre desde esta carpeta:  python3 sitio.py  (o con el curso: python3 sitio.py "Matemáticas 1")
Escribe la carpeta de ese curso y rehace el índice general contando lo que
haya en las carpetas de todos los cursos.
"""
import json, os, html, re
from acomodo import examenes, revisar as acomodo_revisar
from resoluciones import construir as construir_resoluciones, resolucion_de, grafica_de, figura_de
from cursos import elegir, archivo, carpeta as carpeta_de, MATERIAS
import generar

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # cuadros/
SITIO = os.path.dirname(RAIZ)                                        # la raíz de lety2E

# ─────────────────────────── Estilo del sitio ───────────────────────────

SITIO_CSS = r'''
:root{
  --bg:#FBF2EF; --bg-card:#FFFFFF; --text:#3D2525; --text-2:#6E4F4F;
  --text-3:#A08080; --border:#E0C4BC; --border-s:#EDD8D0; --accent:#4A0080;
  --accent-light:#F0E0F5; --r-sm:6px; --r-md:12px; --r-lg:18px;
  --font-body:'DM Sans',system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif;
  --font-display:'Playfair Display',Georgia,serif;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--font-body)}
a{color:var(--accent)}
.envoltura{max-width:1000px;margin:0 auto;padding:1.6rem 1rem 3rem}
h1{font-family:var(--font-display);font-size:1.6rem;margin:0 0 .2rem}
.sub{color:var(--text-2);margin:0 0 1.6rem;font-size:.95rem}
.migaja{font-size:.85rem;color:var(--text-3);margin:0 0 .8rem}
.migaja a{color:var(--text-2);text-decoration:none}
.migaja a:hover{text-decoration:underline}

.tarjetas{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1rem}
.materia{display:block;background:var(--bg-card);border:1.5px solid var(--border);
  border-radius:var(--r-lg);padding:1rem 1.1rem;text-decoration:none;color:inherit}
.materia:hover{border-color:var(--accent);box-shadow:0 2px 10px rgba(74,0,128,.07)}
.materia h2{font-family:var(--font-display);font-size:1.15rem;margin:0 0 .15rem}
.materia p{margin:0;color:var(--text-3);font-size:.85rem}
.materia .cuenta{margin-top:.6rem;font-size:.8rem;color:var(--accent);font-weight:600}
.materia.vacia{opacity:.55;pointer-events:none}
.materia.vacia .cuenta{color:var(--text-3);font-weight:400}

.examen{background:var(--bg-card);border:1.5px solid var(--border);
  border-radius:var(--r-lg);padding:1rem 1.1rem;margin-bottom:1rem}
.examen h2{font-family:var(--font-display);font-size:1.1rem;margin:0 0 .1rem}
.examen .temas{margin:.1rem 0 .8rem;color:var(--text-3);font-size:.82rem}
.examen .etiqueta{margin:.9rem 0 .4rem;font-size:.78rem;color:var(--text-2);text-transform:uppercase;letter-spacing:.04em}
.versiones{display:flex;flex-wrap:wrap;gap:.5rem}
.v{display:inline-block;min-width:3.4rem;text-align:center;padding:.45rem .7rem;
  border:1.5px solid var(--border);border-radius:var(--r-sm);background:#fff;
  text-decoration:none;color:var(--text);font-weight:600;font-size:.9rem}
.v:hover{border-color:var(--accent);color:var(--accent)}
.v.actual{background:var(--accent);border-color:var(--accent);color:#fff}

/* La barra de pestañas de una versión */
.barra{background:var(--bg-card);border-bottom:1.5px solid var(--border);
  padding:.7rem 1rem;position:sticky;top:0;z-index:5}
.barra .interior{max-width:1000px;margin:0 auto;display:flex;flex-wrap:wrap;
  align-items:center;gap:.4rem}
.barra .grupo{font-size:.8rem;color:var(--text-3);margin-right:.2rem}
.barra .sep{width:1px;height:1.2rem;background:var(--border-s);margin:0 .5rem}
.barra .v{min-width:2.2rem;padding:.3rem .5rem;font-size:.85rem}
.barra .imprimir{margin-left:auto;border:1.5px solid var(--accent);color:var(--accent);
  border-radius:var(--r-sm);padding:.35rem .8rem;background:#fff;cursor:pointer;
  font-family:inherit;font-size:.85rem;font-weight:600}
.papel{max-width:20.4cm;margin:1.2rem auto;background:#fff;border:1.5px solid var(--border-s);
  border-radius:var(--r-md);box-shadow:0 2px 12px rgba(61,37,37,.06)}
.aviso{max-width:1000px;margin:0 auto;padding:.9rem 1rem 0;color:var(--text-3);font-size:.85rem}

/* La hoja resuelta: cada ejercicio con su resolución debajo */
.sol{display:block;margin:-.35rem 0 .5rem 1.1em;font-size:.82rem;color:var(--accent);
  line-height:1.5}
/* Un aligned largo (las resoluciones de Mate 5) en línea se centra en el renglón y se
   monta sobre el enunciado: va como bloque, con su aire. */
.sol .katex{display:inline-block;vertical-align:top;margin:.15rem 0}
.papel.resuelta .mini-card-body .ej-line:not(.libre){line-height:2.2}
.papel.resuelta .sol{margin-top:.15rem}
.sol.falta{color:var(--text-3);font-style:italic}
.papel.resuelta .mini-card-body{line-height:1.6}
.marca{display:inline-block;margin-left:.5rem;padding:.1rem .45rem;border-radius:var(--r-sm);
  background:var(--accent-light);color:var(--accent);font-size:.72rem;font-weight:600;
  vertical-align:middle}
/* Hoja resuelta (23-sep-2026): sin tarjetas, cada pregunta y su resolución con aire y una
   línea antes de la siguiente. Es para calificar en pantalla: no se ahorra espacio. */
.papel.resuelta .rejilla{display:block}
.papel.resuelta .fila{display:block}
.tema-resuelto{margin:0 0 2rem}
.tema-resuelto h3{font-family:var(--font-display);font-size:1.05rem;margin:0 0 .3rem;
  padding-bottom:.35rem;border-bottom:2px solid var(--text)}
.par-resuelto{padding:1rem 0 1.1rem;border-bottom:1px solid var(--border)}
.par-resuelto:last-child{border-bottom:none}
.par-resuelto .pregunta .ej-line{line-height:2.2}
.par-resuelto .pregunta{margin-bottom:.55rem}
.par-resuelto .sol{margin:0 0 0 .2rem;font-size:1rem;line-height:1.7;color:var(--text)}
.par-resuelto .sol .mathbf{color:#FF00AA}
.sol-grafica{margin:.8rem 0 0 .2rem}
.sol-grafica svg{width:100%;max-width:240px;max-height:300px;height:auto;display:block}
.v.par{min-width:auto;padding:.45rem .6rem;font-weight:400;font-size:.82rem}

/* Al imprimir, todo en negro sobre blanco: la hoja ya lo está (el CSS de
   generar.py), aquí faltaban las resoluciones y su etiqueta, que en pantalla
   van en morado. */
@media print{
  .barra,.aviso{display:none}
  body{background:#fff}
  .papel{margin:0;border:0;border-radius:0;box-shadow:none;max-width:none}
  .sol,.sol.falta{color:#000}
  .marca{background:none;color:#000;padding:0}
}
'''

# ─────────────────────────── Piezas ───────────────────────────

def cabeza(titulo, prof=0):
    aqui = '../' * prof            # hasta cuadros/
    sitio = '../' * (prof + 1)     # hasta la raíz de lety2E
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{html.escape(titulo)}</title>
<link rel="stylesheet" href="{sitio}assets/katex/katex.min.css">
<link rel="stylesheet" href="{sitio}style.css">
<link rel="stylesheet" href="{aqui}cuadros.css">
<style>{generar.CSS}</style>
</head>
<body>'''

def cuerpo_hoja(curso, sel, v, letra, plan, banco=None, numeros=None):
    """El mismo .hoja de generar.py, sin el documento alrededor.
    Con `banco`, cada ejercicio lleva su resolución debajo."""
    porTitulo = {t['titulo']: t['versiones'][v] for t in sel}
    filas = []
    numeros = numeros or {}                # numero del tema en el curso (ver generar.numeros_de)
    for fila in plan:
        fila = [(t, p, c) for t, p, c in fila if porTitulo.get(t)]
        if not fila: continue
        anchos = ' '.join('%dfr' % p for _, p, _ in fila)
        celdas = ''
        for t, _, c in fila:
            n = numeros.get(t, 0)
            if banco is None:
                celdas += generar.tarjeta(t, porTitulo[t], c, n)
            else:
                celdas += tarjeta_resuelta(banco, t, porTitulo[t], c, n)
        filas.append('<div class="fila" style="grid-template-columns:%s">%s</div>'
                     % (anchos, celdas))
    marca = '<span class="marca">resuelta</span>' if banco is not None else ''
    return ('<div class="hoja"><p class="titulo">%s%s%s</p><div class="rejilla">%s</div></div>'
            % (html.escape(curso), letra, marca, ''.join(filas)))

def _plano(tex):
    """Para comparar enunciado y resolución sin espacios ni adornos."""
    t = re.sub(r'\\(displaystyle|left|right|begin\{aligned\}|end\{aligned\}|[,;!])', '', tex or '')
    t = t.replace('\\dfrac', '\\frac').replace('\\operatorname{sen}', 'sen')
    t = re.sub(r'[\s$&{}]', '', t)
    return t[:-1] if t.endswith('=') else t

def _trae_la_pregunta(tex, res):
    """¿La resolución empieza con el enunciado? Entonces no se repite (Lety, 23-sep-2026)."""
    q, r = _plano(tex), _plano(res)
    return bool(q) and q in r[:len(q) + 12]

def _resalta(res):
    """El resultado en magenta, como en la página. Si ya trae \\mathbf lo pinta el CSS. Si no
    (Operaciones básicas y parecidos): o el resultado viene aparte ('$… =$ $-1$', el <strong> de
    la página) y se pinta esa fórmula, o se pinta lo que va tras el último = de la cadena."""
    if '\\mathbf' in res or '\\begin' in res:
        return res
    partes = re.findall(r'\$[^$]*\$', res)
    if not partes or re.sub(r'\$[^$]*\$|\s', '', res):
        return res                                   # hay texto suelto: se deja como está
    ultima = partes[-1][1:-1]
    if len(partes) > 1 and partes[-2].rstrip('$ ').endswith('='):
        return res[:res.rfind(partes[-1])] + '${\\color{#FF00AA}%s}$' % ultima.strip()
    i = ultima.rfind('=')
    if i < 0: return res
    return res[:res.rfind(partes[-1])] + '$%s= {\\color{#FF00AA}%s}$' % (ultima[:i], ultima[i + 1:].strip())

def tarjeta_resuelta(banco, tema, items, columnas, numero=0):
    """El tema en la hoja RESUELTA, para calificar en pantalla (Lety, 23-sep-2026): sin tarjeta,
    cada ejercicio con aire y una línea antes del siguiente; "más parecido a la resolución del
    ejemplo": la pregunta no se repite si la resolución ya empieza con ella, el resultado va en
    magenta, y va la gráfica de la respuesta publicada cuando la hay."""
    trozos = []
    for item in items:
        partes = []
        if 'tex' not in item:                          # la pregunta es una figura
            fig = figura_de(banco, tema, item)
            if fig:
                partes += ['<div class="sol-grafica">%s</div>' % fig[1],
                           '<div class="sol">%s</div>' % generar.enunciado(fig[0])]
            else:
                partes += ['<div class="pregunta">%s</div>' % generar.linea(item),
                           '<div class="sol falta">pendiente</div>']
        else:
            r = resolucion_de(banco, tema, item['tex'])
            if not r or not _trae_la_pregunta(item['tex'], r):
                partes.append('<div class="pregunta">%s</div>' % generar.linea(item))
            if r:
                partes.append('<div class="sol">%s</div>' % generar.enunciado(_resalta(r)))
                g = grafica_de(banco, tema, item)
                if g: partes.append('<div class="sol-grafica">%s</div>' % g)
            else:
                partes.append('<div class="sol falta">pendiente</div>')
        trozos.append('<div class="par-resuelto">%s</div>' % ''.join(partes))
    return ('<section class="tema-resuelto"><h3>%s</h3>%s</section>'
            % (generar.titulo_cuadro(tema, numero), ''.join(trozos)))

def barra(curso, planes, letra_actual, resuelta=False):
    """Las pestañas: los dos exámenes con sus seis versiones."""
    trozos = []
    for i, (nombre, letras, _) in enumerate(planes):
        if i: trozos.append('<span class="sep"></span>')
        trozos.append('<span class="grupo">%s</span>' % html.escape(nombre))
        for L in letras:
            clase = 'v actual' if L == letra_actual else 'v'
            destino = '%s-resuelta.html' % L if resuelta else '%s.html' % L
            trozos.append('<a class="%s" href="%s">%s</a>' % (clase, destino, L))
    par = ('<a class="v par" href="%s.html">ver en blanco</a>' % letra_actual if resuelta
           else '<a class="v par" href="%s-resuelta.html">ver resuelta</a>' % letra_actual)
    return ('<div class="barra"><div class="interior">'
            '<a class="grupo" href="index.html" style="text-decoration:none">← %s</a>'
            '<span class="sep"></span>%s<span class="sep"></span>%s'
            '<button class="imprimir" onclick="window.print()">Imprimir</button>'
            '</div></div>' % (html.escape(curso), ''.join(trozos), par))

# ─────────────────────────── Páginas ───────────────────────────

def pagina_version(curso, sel, planes, nombre, letras, plan, v, destino, banco):
    letra = letras[v]
    temas = {t for fila in plan for t, _, _ in fila}
    recorte = [t for t in sel if t['titulo'] in temas]
    numeros = generar.numeros_de(sel)

    doc = (cabeza('%s%s' % (curso, letra), prof=1)
           + barra(curso, planes, letra)
           + '<div class="papel">' + cuerpo_hoja(curso, recorte, v, letra, plan, numeros=numeros) + '</div>'
           + '</body></html>\n')
    open(os.path.join(destino, '%s.html' % letra), 'w', encoding='utf-8').write(doc)

    # La hoja resuelta es para calificar en pantalla, no para imprimir: cada tema
    # va a lo ancho, en el orden del curso, para que las resoluciones largas (los
    # aligned de Mate 5) no se corten en una tarjeta angosta.
    plan_resuelto = [[(t['titulo'], 1, 1)] for t in recorte]
    doc = (cabeza('%s%s resuelta' % (curso, letra), prof=1)
           + barra(curso, planes, letra, resuelta=True)
           + '<div class="papel resuelta">'
           + cuerpo_hoja(curso, recorte, v, letra, plan_resuelto, banco, numeros) + '</div>'
           + '</body></html>\n')
    open(os.path.join(destino, '%s-resuelta.html' % letra), 'w', encoding='utf-8').write(doc)

def pagina_materia(curso, sel, planes, destino):
    orden = [t['titulo'] for t in sel]   # el orden del sitio, no el del acomodo
    bloques = []
    for nombre, letras, plan in planes:
        del_examen = {t for fila in plan for t, _, _ in fila}
        temas = [t for t in orden if t in del_examen]
        vs = ''.join('<a class="v" href="%s.html">%s</a>' % (L, L) for L in letras)
        rs = ''.join('<a class="v" href="%s-resuelta.html">%s</a>' % (L, L) for L in letras)
        bloques.append('<div class="examen"><h2>%s</h2>'
                       '<p class="temas">%s</p>'
                       '<p class="etiqueta">Para imprimir</p>'
                       '<div class="versiones">%s</div>'
                       '<p class="etiqueta">Resueltas, para calificar</p>'
                       '<div class="versiones">%s</div></div>'
                       % (html.escape(nombre), html.escape(' · '.join(temas)), vs, rs))
    doc = (cabeza(curso, prof=1)
           + '<div class="envoltura">'
           + '<p class="migaja"><a href="../">Exámenes</a> / %s</p>' % html.escape(curso)
           + '<h1>%s</h1>' % html.escape(curso)
           + '<p class="sub">Seis versiones por examen. Los ejercicios salen de las '
             'páginas de temas del curso.</p>'
           + ''.join(bloques) + '</div></body></html>\n')
    open(os.path.join(destino, 'index.html'), 'w', encoding='utf-8').write(doc)

def versiones_hechas(carpeta):
    """Cuántas versiones hay ya escritas en cuadros/<carpeta>/ (a.html, b.html…)."""
    ruta = os.path.join(RAIZ, carpeta)
    if not os.path.isdir(ruta): return 0
    return sum(1 for f in os.listdir(ruta) if re.fullmatch(r'[a-z]\.html', f))

def pagina_indice():
    """El índice general: cuenta lo que hay en la carpeta de cada curso, así
    el de hoy no borra a los demás."""
    tarjetas = []
    for titulo, carpeta, semestre in MATERIAS:
        n = versiones_hechas(carpeta)
        if n:
            cuenta = '%d versiones' % n
            tarjetas.append('<a class="materia" href="%s/"><h2>%s</h2><p>%s</p>'
                            '<p class="cuenta">%s</p></a>'
                            % (carpeta, html.escape(titulo), semestre, cuenta))
        else:
            tarjetas.append('<span class="materia vacia"><h2>%s</h2><p>%s</p>'
                            '<p class="cuenta">por armar</p></span>'
                            % (html.escape(titulo), semestre))
    doc = (cabeza('Exámenes', prof=0)
           + '<div class="envoltura"><h1>Exámenes</h1>'
           + '<p class="sub">Las versiones de cada examen, por materia.</p>'
           + '<div class="tarjetas">%s</div></div></body></html>\n' % ''.join(tarjetas))
    open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf-8').write(doc)

if __name__ == '__main__':
    curso, _ = elegir()
    sel = json.load(open(archivo('seleccion', curso)))
    for aviso in acomodo_revisar(curso, [t['titulo'] for t in sel]): print(aviso)
    banco = construir_resoluciones(curso)
    planes = examenes(curso)
    destino = os.path.join(RAIZ, carpeta_de(curso))
    os.makedirs(destino, exist_ok=True)
    open(os.path.join(RAIZ, 'cuadros.css'), 'w', encoding='utf-8').write(SITIO_CSS)

    total = 0
    for nombre, letras, plan in planes:
        for v in range(len(letras)):
            pagina_version(curso, sel, planes, nombre, letras, plan, v, destino, banco)
            total += 1
    pagina_materia(curso, sel, planes, destino)
    pagina_indice()
    print('sitio escrito: %d versiones en %s/' % (total, carpeta_de(curso)))
