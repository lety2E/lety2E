#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Qué examen lleva qué temas, y cómo se acomodan en la hoja.

El curso se parte en DOS EXÁMENES por semestre: el primero se lleva los primeros
temas del sitio y el segundo los que siguen. Las letras no se repiten entre
exámenes (el primero va de la a a la f, el segundo de la g a la l), así que cada
hoja que se reparte en el salón tiene un identificador único: "Matemáticas 1a",
"Matemáticas 1g".

CADA VERSIÓN CABE EN UNA HOJA CARTA. Regla de Lety (8-sep-2026): puede sobrar
espacio, pero no se puede exceder. `medida.py` calcula qué tanto llena la hoja y
lo dice al generar; si un examen se pasa, la salida grita "¡NO CABE!". Las dos
palancas para bajarlo son el acomodo de aquí y `--renglon` en `generar.py`; la
tercera, si de plano ya no da, es mover un tema al otro examen.

DENTRO DE UN EXAMEN LOS TEMAS VAN EN EL ORDEN QUE CONVENGA. Lo único que importa
es que estén los que le tocan: los primeros temas en el primero, los siguientes
en el segundo. Palabras de Lety (8-sep-2026): "ya cómo se acomoden esos temas no
importa que no estén ordenados, con que estén los correspondientes". Por eso las
filas se emparejan por altura, para que no queden huecos.

(La regla anterior — "no me pongas un último tema en la primera hoja" — era para
cuando un examen se iba a dos hojas. Ahora cada examen es una hoja, así que el
corte que importa es el de los exámenes, no el de las hojas.)

Dentro de cada examen, la hoja se arma por FILAS, como los minipages de LaTeX:
en cada fila los temas se reparten el ancho según su peso.

  'Tema'          el tema con peso 1
  ('Tema', 2)     el tema con el doble de ancho
  ('Tema', 1, 3)  además, sus ejercicios en 3 columnas dentro de la tarjeta
                  (útil cuando son muchos y cortos)

Al cambiar los contenidos cambian las alturas: hay que volver a mirar la hoja.
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

def revisar(curso, titulos):
    """Que cada tema del banco esté en uno de los dos exámenes, y en uno solo.

    Es lo único que el acomodo tiene que garantizar: el orden adentro da igual,
    pero un tema que no aparece en ninguna fila desaparece del examen sin ruido.
    Devuelve una lista de avisos; vacía si todo está en su lugar.
    """
    dondes = {}
    for nombre, _, filas in examenes(curso):
        for fila in filas:
            for t, _, _ in fila:
                dondes.setdefault(t, []).append(nombre)
    avisos = []
    for t in titulos:
        if t not in dondes:
            avisos.append('OJO: "%s" no está en ningún examen' % t)
        elif len(dondes[t]) > 1:
            avisos.append('OJO: "%s" está en %s' % (t, ' y '.join(dondes[t])))
    for t in dondes:
        if t not in titulos:
            avisos.append('OJO: "%s" está en el acomodo pero no en el banco' % t)
    return avisos
