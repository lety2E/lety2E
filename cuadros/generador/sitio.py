#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escribe el sitio de exámenes a partir de seleccion.json.

Cada versión es su propia página (no una sola página con doce pestañas): así
carga rápido y se imprime tal cual. La barra de arriba hace de pestañas.

Las páginas usan el KaTeX, las tipografías y el `style.css` del propio sitio
(`assets/`), como manda su manual: cero CDNs y nada duplicado. En cambio los
exámenes que `generar.py` deja en IEMS sí llevan todo incrustado, porque ésos se
abren con doble clic y sin internet.

Se corre desde esta carpeta:  python3 sitio.py
"""
import json, os, html
from acomodo import examenes, revisar as acomodo_revisar
from resoluciones import construir as construir_resoluciones, resolucion_de
import generar

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # cuadros/
SITIO = os.path.dirname(RAIZ)                                        # la raíz de lety2E
CURSO = 'Matemáticas 1'
CARPETA = 'matematicas-1'

MATERIAS = [
    ('Matemáticas 1', 'matematicas-1', 'Primer semestre'),
    ('Matemáticas 2', 'matematicas-2', 'Segundo semestre'),
    ('Matemáticas 3', 'matematicas-3', 'Tercer semestre'),
    ('Matemáticas 4', 'matematicas-4', 'Cuarto semestre'),
    ('Matemáticas 5', 'matematicas-5', 'Quinto semestre'),
    ('Optativa',      'optativa',      'Sexto semestre'),
]

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
.sol.falta{color:var(--text-3);font-style:italic}
.papel.resuelta .mini-card-body{line-height:1.6}
.marca{display:inline-block;margin-left:.5rem;padding:.1rem .45rem;border-radius:var(--r-sm);
  background:var(--accent-light);color:var(--accent);font-size:.72rem;font-weight:600;
  vertical-align:middle}
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

def cuerpo_hoja(sel, v, letra, plan, banco=None):
    """El mismo .hoja de generar.py, sin el documento alrededor.
    Con `banco`, cada ejercicio lleva su resolución debajo."""
    porTitulo = {t['titulo']: t['versiones'][v] for t in sel}
    filas = []
    for fila in plan:
        fila = [(t, p, c) for t, p, c in fila if porTitulo.get(t)]
        if not fila: continue
        anchos = ' '.join('%dfr' % p for _, p, _ in fila)
        if banco is None:
            celdas = ''.join(generar.tarjeta(t, porTitulo[t], c) for t, _, c in fila)
        else:
            celdas = ''.join(tarjeta_resuelta(banco, t, porTitulo[t], c) for t, _, c in fila)
        filas.append('<div class="fila" style="grid-template-columns:%s">%s</div>'
                     % (anchos, celdas))
    marca = '<span class="marca">resuelta</span>' if banco is not None else ''
    return ('<div class="hoja"><p class="titulo">%s%s%s</p><div class="rejilla">%s</div></div>'
            % (html.escape(CURSO), letra, marca, ''.join(filas)))

def tarjeta_resuelta(banco, tema, items, columnas):
    """La misma tarjeta, pero cada ejercicio con su resolución debajo."""
    trozos = []
    for item in items:
        trozos.append(generar.linea(item))
        if 'tex' not in item:
            continue
        r = resolucion_de(banco, tema, item['tex'])
        if r:
            trozos.append('<div class="sol">%s</div>' % generar.enunciado(r))
        else:
            trozos.append('<div class="sol falta">pendiente</div>')
    clase = 'mini-card-body en-columnas' if columnas > 1 else 'mini-card-body'
    estilo = ' style="column-count:%d"' % columnas if columnas > 1 else ''
    return ('<div class="mini-card"><div class="mini-card-head">%s</div>'
            '<div class="%s"%s>%s</div></div>'
            % (html.escape(tema), clase, estilo, ''.join(trozos)))


def barra(planes, letra_actual, resuelta=False):
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
            '</div></div>' % (html.escape(CURSO), ''.join(trozos), par))

# ─────────────────────────── Páginas ───────────────────────────

def pagina_version(sel, planes, nombre, letras, plan, v, destino, banco):
    letra = letras[v]
    temas = {t for fila in plan for t, _, _ in fila}
    recorte = [t for t in sel if t['titulo'] in temas]

    doc = (cabeza('%s%s' % (CURSO, letra), prof=1)
           + barra(planes, letra)
           + '<div class="papel">' + cuerpo_hoja(recorte, v, letra, plan) + '</div>'
           + '</body></html>\n')
    open(os.path.join(destino, '%s.html' % letra), 'w', encoding='utf-8').write(doc)

    doc = (cabeza('%s%s resuelta' % (CURSO, letra), prof=1)
           + barra(planes, letra, resuelta=True)
           + '<div class="papel resuelta">'
           + cuerpo_hoja(recorte, v, letra, plan, banco) + '</div>'
           + '</body></html>\n')
    open(os.path.join(destino, '%s-resuelta.html' % letra), 'w', encoding='utf-8').write(doc)

def pagina_materia(sel, planes, destino):
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
    doc = (cabeza(CURSO, prof=1)
           + '<div class="envoltura">'
           + '<p class="migaja"><a href="../">Exámenes</a> / %s</p>' % html.escape(CURSO)
           + '<h1>%s</h1>' % html.escape(CURSO)
           + '<p class="sub">Seis versiones por examen. Los ejercicios salen de las '
             'páginas de temas del curso.</p>'
           + ''.join(bloques) + '</div></body></html>\n')
    open(os.path.join(destino, 'index.html'), 'w', encoding='utf-8').write(doc)

def pagina_indice(hechas):
    tarjetas = []
    for titulo, carpeta, semestre in MATERIAS:
        n = hechas.get(carpeta, 0)
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
    sel = json.load(open('seleccion.json'))
    for aviso in acomodo_revisar(CURSO, [t['titulo'] for t in sel]): print(aviso)
    banco = construir_resoluciones(CURSO)
    planes = examenes(CURSO)
    destino = os.path.join(RAIZ, CARPETA)
    os.makedirs(destino, exist_ok=True)
    open(os.path.join(RAIZ, 'cuadros.css'), 'w', encoding='utf-8').write(SITIO_CSS)

    total = 0
    for nombre, letras, plan in planes:
        for v in range(len(letras)):
            pagina_version(sel, planes, nombre, letras, plan, v, destino, banco)
            total += 1
    pagina_materia(sel, planes, destino)
    pagina_indice({CARPETA: total})
    print('sitio escrito: %d versiones en %s/' % (total, CARPETA))
