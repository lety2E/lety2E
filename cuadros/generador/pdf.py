#!/usr/bin/env python3
"""Junta las versiones de un examen en UN PDF, una versión por hoja carta,
listo para imprimir. Lo deja en ~/Downloads.

Parte de los exámenes autocontenidos que escribe generar.py en la carpeta de
IEMS; los imprime con Google Chrome sin ventana (--headless) y los pega con
pypdf. Lety lo pidió el 17-sep-2026 para llevar el examen a la copiadora.

Uso (desde esta carpeta, después de generar.py):
    python3 pdf.py                       -> Examen 1 del curso ACTUAL (ver cursos.py)
    python3 pdf.py 2                     -> Examen 2 del curso ACTUAL
    python3 pdf.py "Matemáticas 1" 2     -> Examen 2 de Matemáticas 1
"""
import os, sys, subprocess, tempfile
from acomodo import examenes
from cursos import elegir
import generar   # generar.destino(curso): donde deja los .html

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
DESTINO = os.path.expanduser('~/Downloads')

def pdf_de(curso, numero):
    import pypdf
    nombre, letras, _ = examenes(curso)[numero - 1]
    carpeta = generar.destino(curso)
    salida = os.path.join(DESTINO, '%s %s (versiones %s-%s).pdf'
                          % (nombre, curso, letras[0], letras[-1]))
    w = pypdf.PdfWriter()
    with tempfile.TemporaryDirectory() as tmp:
        for L in letras:
            html = os.path.join(carpeta, '%s %s%s.html' % (nombre, curso, L))
            uno = os.path.join(tmp, L + '.pdf')
            subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                            '--print-to-pdf=' + uno, 'file://' + html],
                           check=True, capture_output=True)
            paginas = len(pypdf.PdfReader(uno).pages)
            if paginas != 1:
                print('  ojo: %s%s salió en %d páginas' % (curso, L, paginas))
            w.append(uno)
    w.write(salida)
    print('PDF: %s  (%d hojas)' % (salida, len(letras)))

if __name__ == '__main__':
    curso, resto = elegir()
    pdf_de(curso, int(resto[0]) if resto else 1)
