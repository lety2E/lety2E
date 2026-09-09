#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Qué examen lleva qué temas, y cómo se acomodan en la hoja.

El curso se parte en varios EXÁMENES, cada uno con sus temas y sus versiones.
Las letras no se repiten entre exámenes (el primero va de la a a la f, el
segundo de la g a la l), así que cada hoja que se reparte en el salón tiene un
identificador único: "Matemáticas 1a", "Matemáticas 1g".

Dentro de cada examen, la hoja se arma por FILAS, como los minipages de LaTeX:
en cada fila los temas se reparten el ancho según su peso.

  'Tema'          el tema con peso 1
  ('Tema', 2)     el tema con el doble de ancho
  ('Tema', 1, 3)  además, sus ejercicios en 3 columnas dentro de la tarjeta
                  (útil cuando son muchos y cortos)

Los temas se emparejan por altura para que no queden huecos. Al cambiar los
contenidos cambian las alturas: hay que volver a mirar la hoja. Si ya no cabe,
la decisión de Lety es irse a dos hojas antes que apretar más.

CUANDO SON DOS HOJAS, EL CORTE RESPETA EL ORDEN DE LOS TEMAS. El emparejado por
altura puede reacomodar dentro de una hoja, pero no a través del corte: la
primera hoja se lleva los primeros temas del curso y la segunda los que siguen.
Regla de Lety (8-sep-2026): "no me pongas un último tema en la primera hoja".

Ojo con las filas del Examen 1 de Matemáticas 1: hoy caben en una hoja, pero la
primera fila empareja Operaciones básicas (tema 1) con Ecuaciones con ángulos
(tema 9). El día que pase a dos hojas hay que rehacerlas.
"""

EXAMENES = {
 'Matemáticas 1': [
   {
     'nombre': 'Examen 1',
     'letras': 'abcdef',
     'filas': [
       [('Operaciones básicas', 2, 3), ('Ecuaciones con ángulos', 1)],
       ['Jerarquía de operaciones', 'Expresiones algebraicas'],
       ['Ecuaciones', 'Monomios'],
       ['Gráfica con tabulación', 'Pendiente y ordenada', 'Área y perímetro'],
     ],
   },
   {
     'nombre': 'Examen 2',
     'letras': 'ghijkl',
     'filas': [
       ['Reglas de exponentes', 'mcm y MCD'],
       ['Problemas de ecuaciones', 'Lenguaje algebraico'],
     ],
   },
 ],
}

def normalizar(entrada):
    """'Tema' | ('Tema', peso) | ('Tema', peso, columnas) -> (tema, peso, columnas)"""
    if isinstance(entrada, str): return (entrada, 1, 1)
    if len(entrada) == 2: return (entrada[0], entrada[1], 1)
    return tuple(entrada)

def examenes(curso):
    """[(nombre, letras, [[(tema, peso, columnas), ...], ...]), ...]"""
    return [(e['nombre'], e['letras'],
             [[normalizar(x) for x in fila] for fila in e['filas']])
            for e in EXAMENES.get(curso, [])]

def temas_de(curso, nombre):
    for n, _, filas in examenes(curso):
        if n == nombre:
            return [t for fila in filas for t, _, _ in fila]
    return []
