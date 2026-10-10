#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hoja de práctica para prestar: Ejemplo resuelto + Ejercicios sin resolver de
los temas que entran al Examen 1 de cada materia (según cuadros/generador/acomodo.py),
para que los alumnos sin datos los copien a mano o le tomen foto.

Negro sobre blanco, compacto — no el "formato de página" del sitio (esa
maquetación es para pantalla, con mucho aire). Cada tema inicia en hoja nueva
(para prestar/repartir por tema suelto). Un PDF por curso. Deja el resultado
en ~/Downloads.

Reusa el Ejemplo y los Ejercicios reales de cada página de math/ tal cual —
nunca inventa contenido — pero les quita el color (cada tema aísla su <style>
inline con @scope, para que un tema no le cambie el layout a otro) y aprieta
los espacios para imprimir.

Uso (desde esta carpeta):
    python3 hoja-practica-generador.py
"""
import os, subprocess, tempfile
from bs4 import BeautifulSoup
import pypdf

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
DESTINO = os.path.expanduser('~/Downloads')

# Examen 1 de cada materia (cuadros/generador/acomodo.py, 22-sep-2026), en el
# orden del índice del curso — no el orden de acomodo, que está pensado para
# repartir la hoja del examen, no para estudiar en secuencia.
CURSOS = [
    ('Matemáticas 1', 'matematicas-1', [
        'operaciones-basicas', 'jerarquia', 'ecuaciones', 'monomios',
        'expresiones-algebraicas', 'grafica-tabulacion', 'pendiente-ordenada',
        'area-perimetro', 'ecuaciones-angulos',
    ]),
    ('Matemáticas 5', 'matematicas-5', [
        'reglas-basicas', 'velocidad-media', 'senos-cosenos', 'raices',
        'regla-producto-p1', 'regla-producto-p2', 'regla-cociente-p1',
        'regla-cociente-p2', 'regla-cadena-p1', 'regla-cadena-p2',
    ]),
]

ESTILO_GLOBAL = """
  @page { size: letter; margin: 1cm 1.2cm; }
  html, body { background: #fff !important; }
  body[data-section="math"] { filter: grayscale(1) contrast(1.05); }
  main.topic-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }

  .tema { margin: 0 !important; padding-top: 0; break-before: page; page-break-before: always; }
  .tema:first-child { break-before: auto; page-break-before: avoid; }

  h1, h2, h3 { color: #000 !important; }
  .topic-header { text-align: left !important; margin-bottom: .5rem !important; }
  .topic-header h1 { font-size: 1.2rem !important; margin: 0 0 .15rem !important; }
  .topic-tag { background: transparent !important; color: #000 !important; border: 1px solid #000 !important;
               font-size: .68rem !important; padding: .1rem .5rem !important; margin-bottom: 0 !important; }
  .topic-tag::before { background: #000 !important; }

  .section-block { margin-bottom: .7rem !important; }
  .ejemplo-section { margin: .5rem 0 .8rem !important; }
  .ejemplo-head, .sec-head { margin-bottom: .35rem !important; gap: .4rem !important; }
  .ejemplo-head h3, .sec-head h2 { font-size: .92rem !important; }
  .sec-icon { width: 20px !important; height: 20px !important; background: transparent !important; border: 1px solid #000 !important; }
  .sec-icon svg { stroke: #000 !important; width: 11px !important; height: 11px !important; }

  .ejemplo-block { padding: .6rem .8rem !important; line-height: 1.6 !important; font-size: .92rem !important; }
  .ejemplo-block strong { color: #000 !important; }
  /* A dos columnas un \\begin{aligned} ancho se sale de su mitad (no hay dónde
     reflowearlo). A una columna cabe siempre en el ancho de la hoja. */
  .ejemplo-grid { grid-template-columns: 1fr !important; }
  body[data-section="math"] .katex,
  body[data-section="math"] .ej-line,
  body[data-section="math"] .sol { white-space: normal !important; }
  .katex-display > .katex { font-size: .95em !important; }
  .formula-pill, .formula-pill.salmon, .resultado-pill {
    background: transparent !important; border: 1px solid #000 !important; color: #000 !important;
  }

  .mini-card { border: 1px solid #000 !important; }
  .mini-card-head { background: transparent !important; color: #000 !important; border-bottom: 1px solid #000 !important;
                     padding: .22rem .55rem !important; font-size: .76rem !important; }
  .mini-card-body { padding: .35rem .55rem !important; font-size: .84rem !important; line-height: 1.65 !important; }

  .mini-card, .ejemplo-block { break-inside: avoid !important; page-break-inside: avoid !important; }
  .bloques-1, .bloques-2, .bloques-3, .ejemplo-grid { gap: .55rem !important; }
"""

PLANTILLA = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{curso} — Examen 1 — hoja de práctica</title>
<link rel="stylesheet" href="file://{raiz}/style.css">
<link rel="stylesheet" href="file://{raiz}/assets/katex/katex.min.css">
<style>{estilo_global}</style>
</head>
<body data-section="math">
  <main class="topic-content">
{temas}
  </main>
</body>
</html>
"""

TEMA_PLANTILLA = """    <section class="tema tema-{i}">
      <style>@scope (.tema-{i}) {{
{estilo}
      }}</style>
      <header class="topic-header">
        {topic_tag}
        <h1>{titulo}</h1>
      </header>
      {ejemplo}
      {ejercicios}
    </section>
"""


def extraer(curso_dir, slug):
    ruta = os.path.join(RAIZ, 'math', curso_dir, slug + '.html')
    with open(ruta, encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    def por_encabezado(texto):
        for tag in soup.find_all(['h2', 'h3']):
            if tag.get_text(strip=True) == texto:
                return tag.find_parent('section')
        return None

    h1 = soup.find('h1')
    titulo = h1.get_text(strip=True) if h1 else slug
    topic_tag = soup.find('div', class_='topic-tag')
    estilo = soup.head.find('style')

    # La mayoría usa <section class="ejemplo-section">, pero algunas (ej.
    # ecuaciones-angulos, con triángulo) sólo llevan <h2>Ejemplo</h2> en un
    # section-block corriente.
    ejemplo = (soup.find('section', class_='ejemplo-section')
               or por_encabezado('Ejemplo') or por_encabezado('Ejemplos'))
    ejercicios = por_encabezado('Ejercicios')
    if ejercicios is None:
        raise RuntimeError('No encontré la sección "Ejercicios" en %s' % ruta)
    if ejemplo is None:
        print('  ojo: %s no tiene bloque de Ejemplo, se deja sin él' % slug)

    return dict(
        titulo=titulo,
        topic_tag=str(topic_tag) if topic_tag else '',
        estilo=estilo.decode_contents() if estilo else '',
        ejemplo=str(ejemplo) if ejemplo else '',
        ejercicios=str(ejercicios),
    )


def armar_curso(curso, curso_dir, slugs):
    piezas = []
    for i, slug in enumerate(slugs, start=1):
        print('  %s...' % slug)
        datos = extraer(curso_dir, slug)
        piezas.append(TEMA_PLANTILLA.format(i=i, **datos))
    return PLANTILLA.format(raiz=RAIZ, curso=curso, estilo_global=ESTILO_GLOBAL,
                             temas='\n'.join(piezas))


def main():
    with tempfile.TemporaryDirectory() as tmp:
        for curso, curso_dir, slugs in CURSOS:
            print('Armando %s...' % curso)
            html = armar_curso(curso, curso_dir, slugs)
            html_path = os.path.join(tmp, curso_dir + '.html')
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html)

            pdf_path = os.path.join(
                DESTINO, 'Hoja de práctica - Examen 1 %s.pdf' % curso)
            subprocess.run([
                CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                '--print-to-pdf=' + pdf_path, 'file://' + html_path,
            ], check=True, capture_output=True)
            paginas = len(pypdf.PdfReader(pdf_path).pages)
            print('  PDF: %s  (%d páginas)\n' % (pdf_path, paginas))


if __name__ == '__main__':
    main()
