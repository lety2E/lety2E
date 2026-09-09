#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El banco de resoluciones, para las hojas resueltas con las que Lety califica.

Dos fuentes, y nunca se pisan:

  · COSECHADAS del sitio — la sección "Ejercicios" de cada tema tiene su sección
    "Respuestas"; se emparejan por posición (bloque N, renglón M). Se vuelven a
    cosechar cada vez, así que si Lety corrige una respuesta allá, aquí se actualiza.

  · ESCRITAS A MANO — `resoluciones-manuales.json`. Los *Ejercicios extra* del sitio
    no traen respuesta a propósito (son los que se evalúan), así que sus resoluciones
    se escriben aquí. Este archivo NO se toca al cosechar: es trabajo de Lety.

La llave de cada resolución es el propio enunciado (`tex`), que es lo que guarda
`seleccion.json`. Se corre desde esta carpeta:  python3 resoluciones.py
"""
import json, os
from extraer import parse_file
from banco import CURSOS  # {curso: (ruta, [(archivo, titulo, receta), ...])}

MANUALES = 'resoluciones-manuales.json'
SALIDA = 'resoluciones.json'

# El sitio no llama igual a la sección en todos los temas.
NOMBRES_EJERCICIOS = ('ejercicios',)
NOMBRES_RESPUESTAS = ('respuestas', 'ejercicios resueltos', 'resoluciones', 'soluciones')

def secciones(pagina, nombres):
    return [s for s in pagina if s['seccion'].strip().lower() in nombres]

def limpio(texto):
    """Descarta lo que no es una respuesta: encabezados de sección que el
    parser recoge cuando la sección es plegable (traen el chevron ▼)."""
    t = texto.strip()
    if '▼' in t or t.lower().rstrip('▼ ') in NOMBRES_RESPUESTAS + NOMBRES_EJERCICIOS:
        return None
    return t or None


def cosechar(ruta_html):
    """{tex del ejercicio: respuesta publicada}, emparejando por posición."""
    pagina = parse_file(ruta_html)
    ejercicios = secciones(pagina, NOMBRES_EJERCICIOS)
    respuestas = secciones(pagina, NOMBRES_RESPUESTAS)
    if not ejercicios or not respuestas:
        return {}
    out = {}
    for sec_e, sec_r in zip(ejercicios, respuestas):
        for card_e, card_r in zip(sec_e['cards'], sec_r['cards']):
            for tex, resp in zip(card_e['items'], card_r['items']):
                resp = limpio(resp)
                if resp: out[tex] = resp
    return out

def manuales():
    if not os.path.exists(MANUALES):
        json.dump({}, open(MANUALES, 'w'), ensure_ascii=False, indent=1)
        return {}
    return json.load(open(MANUALES))

def construir(curso):
    base, archivos = CURSOS[curso]
    base = os.path.expanduser(base)
    banco = {}
    for archivo, titulo, _receta in archivos:
        ruta = os.path.join(base, archivo)
        if not os.path.exists(ruta): continue
        banco[titulo] = {'cosechadas': cosechar(ruta), 'manuales': {}}
    for titulo, res in manuales().get(curso, {}).items():
        banco.setdefault(titulo, {'cosechadas': {}, 'manuales': {}})['manuales'] = res
    return banco

def resolucion_de(banco, tema, tex):
    """La resolución escrita a mano gana: es la que Lety revisó."""
    t = banco.get(tema, {})
    return t.get('manuales', {}).get(tex) or t.get('cosechadas', {}).get(tex)

if __name__ == '__main__':
    curso = 'Matemáticas 1'
    banco = construir(curso)
    json.dump({curso: banco}, open(SALIDA, 'w'), ensure_ascii=False, indent=1)

    sel = json.load(open('seleccion.json'))
    total = con = 0
    faltan = {}
    for tema in sel:
        for version in tema['versiones']:
            for item in version:
                if 'tex' not in item: continue
                total += 1
                if resolucion_de(banco, tema['titulo'], item['tex']): con += 1
                else: faltan[tema['titulo']] = faltan.get(tema['titulo'], 0) + 1
    print('resoluciones: %d de %d ejercicios del examen (%d%%)'
          % (con, total, round(100*con/total)))
    if faltan:
        print('faltan, por tema:')
        for t, n in sorted(faltan.items(), key=lambda x: -x[1]):
            print('  %-28s %d' % (t, n))
