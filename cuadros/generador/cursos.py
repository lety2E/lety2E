#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Con qué curso trabaja el generador.

Hasta el 17-sep-2026 todo estaba fijo en Matemáticas 1. Desde entonces cada
script recibe el curso como primer argumento, y si no se le pasa usa ACTUAL
(el curso del semestre en curso):

    python3 banco.py                    -> ACTUAL
    python3 banco.py "Matemáticas 1"    -> ese curso

Los archivos que se generan llevan el curso en el nombre (`banco-matematicas-5.json`,
`seleccion-matematicas-5.json`), así los cursos no se pisan entre sí.
"""
import sys

# (título, carpeta, semestre) — las seis materias, en el orden del sitio.
# La carpeta es la misma en `math/` y en `cuadros/`.
MATERIAS = [
    ('Matemáticas 1', 'matematicas-1', 'Primer semestre'),
    ('Matemáticas 2', 'matematicas-2', 'Segundo semestre'),
    ('Matemáticas 3', 'matematicas-3', 'Tercer semestre'),
    ('Matemáticas 4', 'matematicas-4', 'Cuarto semestre'),
    ('Matemáticas 5', 'matematicas-5', 'Quinto semestre'),
    ('Optativa',      'optativa',      'Sexto semestre'),
]
TITULOS = [t for t, _, _ in MATERIAS]

# El curso con el que se trabaja cuando no se dice otro.
ACTUAL = 'Matemáticas 5'

def carpeta(curso):
    for t, c, _ in MATERIAS:
        if t == curso: return c
    raise SystemExit('curso desconocido: %r (los que hay: %s)' % (curso, ', '.join(TITULOS)))

def archivo(nombre, curso):
    """`banco` + Matemáticas 5 -> banco-matematicas-5.json"""
    return '%s-%s.json' % (nombre, carpeta(curso))

def elegir(argv=None):
    """El curso pedido en la línea de comandos, o ACTUAL. Devuelve también los
    argumentos que sobran, para que cada script lea los suyos."""
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] in TITULOS:
        return argv[0], argv[1:]
    if argv and argv[0].startswith('Matem'):
        raise SystemExit('curso desconocido: %r (los que hay: %s)' % (argv[0], ', '.join(TITULOS)))
    return ACTUAL, argv
