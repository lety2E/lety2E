#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cuánto de la hoja carta ocupa un examen.

Regla de Lety (8-sep-2026): cada versión tiene que caber en UNA hoja tamaño
carta. Puede sobrar espacio, pero no se puede exceder — si se excede, la
impresora suelta una segunda hoja con dos tarjetas huérfanas.

Aquí no hay navegador, así que la altura se calcula con las medidas reales del
CSS de `generar.py`, tomadas del navegador el 8-sep-2026 y verificadas contra
las doce versiones de Matemáticas 1 (Examen 1: 723 px medidos, 723 estimados).
Si se cambian `--renglon`, los paddings o las tipografías, hay que volver a
tomar las medidas.

Es una estimación: lo único que no se puede saber sin navegador es en qué punto
un renglón largo se parte en dos. Se calcula por ancho de columna y número de
caracteres, y se redondea hacia arriba. Por eso la alarma salta al 92%.
"""
import math, re

CM = 96 / 2.54                     # px por cm, a 96 dpi

# La hoja: carta con el margen de @page de generar.py (.9cm)
HOJA_ALTO  = (27.94 - 1.8) * CM    # 987.8 px
HOJA_ANCHO = (21.59 - 1.8) * CM    # 747.9 px

TITULO   = 25.8 + 8                # el identificador de arriba, con su margen
HUECO    = 9.6                     # gap entre filas y entre tarjetas (.6rem)
CHROME   = 37.7                    # borde + paddings + encabezado de la tarjeta
INTERIOR = 22.2                    # lo que la tarjeta le quita a su contenido
COLUMNA  = 19.2                    # column-gap (1.2rem)

ALTO_FORMULA = 33.1                # .9rem x --renglon 2.3
ALTO_LIBRE   = 21.6                # .9rem x 1.5
ALTO_FIGURA  = 80.0                # svg max-height
MARGEN_LIBRE = 6.4                 # .4rem arriba y abajo, que se colapsan

# Caracteres que caben en un renglón, por píxel de ancho. Calibrado con los
# enunciados de Lenguaje algebraico y Problemas de ecuaciones.
CHARS_LIBRE   = 0.135
CHARS_FORMULA = 0.111              # la fórmula ya renderizada es más ancha


def _visuales(tipo, texto, ancho):
    if tipo == 'figura':
        return 1
    densidad = CHARS_LIBRE if tipo == 'libre' else CHARS_FORMULA
    return max(1, math.ceil(len(texto) / max(1, ancho * densidad)))


def alto_tarjeta(lineas, ancho, columnas=1):
    """lineas: [(tipo, texto)] con tipo 'formula' | 'libre' | 'figura'."""
    ancho_col = (ancho - INTERIOR - COLUMNA * (columnas - 1)) / columnas
    altos = []
    for tipo, texto in lineas:
        v = _visuales(tipo, texto, ancho_col)
        if tipo == 'figura':
            altos.append(ALTO_FIGURA)
        elif tipo == 'libre':
            altos.append(ALTO_LIBRE * v)
        else:
            altos.append(ALTO_FORMULA * v)
    # los renglones sueltos (texto y figuras) llevan margen; los contiguos lo colapsan
    sueltos = [i for i, (t, _) in enumerate(lineas) if t != 'formula']
    margen = 0.0
    for i in sueltos:
        margen += MARGEN_LIBRE
        if i - 1 not in sueltos:
            margen += MARGEN_LIBRE
    # con varias columnas, el navegador reparte los renglones entre ellas
    if columnas > 1:
        por_columna = math.ceil(len(altos) / columnas)
        alto = max(sum(altos[i:i + por_columna])
                   for i in range(0, len(altos), por_columna))
        margen /= columnas
    else:
        alto = sum(altos)
    return CHROME + alto + margen


def anchos_de_fila(pesos):
    """El ancho en px de cada tarjeta de una fila, según su peso."""
    libre = HOJA_ANCHO - HUECO * (len(pesos) - 1)
    total = sum(pesos)
    return [libre * p / total for p in pesos]


def alto_hoja(filas):
    """filas: [[(peso, columnas, [(tipo, texto), ...]), ...], ...] -> px."""
    filas = [f for f in filas if f]
    if not filas:
        return 0.0
    alto = TITULO + HUECO * (len(filas) - 1)
    for fila in filas:
        anchos = anchos_de_fila([p for p, _, _ in fila])
        alto += max(alto_tarjeta(l, a, c)
                    for (p, c, l), a in zip(fila, anchos))
    return alto


def informe(nombre, filas):
    """Una línea de texto con qué tanto llena la hoja, y si se pasa."""
    alto = alto_hoja(filas)
    pct = alto / HOJA_ALTO * 100
    cabe = '  ¡NO CABE! →' if pct > 100 else ('  ojo, va al tope →' if pct > 92 else '')
    return '%s: %.1f de %.1f cm de hoja (%.0f%%)%s' % (
        nombre, alto / CM, HOJA_ALTO / CM, pct, cabe)
