#!/usr/bin/env python3
"""Construye el banco de reactivos de un curso a partir del sitio (SOLO LECTURA).

Por cada tema guarda dos listas: los ejercicios que en la pagina traen respuesta
(seccion "Ejercicios") y los que no (seccion "Ejercicios extra"), conservando
los bloques tal como estan en el sitio.
"""
import os, json
from extraer import P, walk, text, clean, items_of
from propios import PROPIOS

# curso -> (carpeta del sitio, temas)
# Cada tema: (archivo, titulo del examen, receta).
#
# La RECETA dice cuanto toma cada version de ese tema. Dos formas:
#   ('bloques', R, E)     R bloques de los de ejercicios + E de los extra.
#                         El bloque entra completo: el bloque ES el tema.
#   ('bloques', R, E, T)  igual, pero rearmando bloques de T ejercicios a
#                         partir de la lista del sitio, en su mismo orden.
#                         Sirve cuando el sitio ya los trae alternados.
#   ('bloques', R, E, T, 'mitades')
#                         igual, pero emparejando la primera mitad de cada
#                         bloque del sitio con la segunda. Sirve cuando el
#                         bloque trae todos los de un tipo y luego los del
#                         otro (A,A,B,B en vez de A,B,A,B).
#   ('por bloque', R, E)  R ejercicios de CADA bloque con respuesta + E de
#                         CADA bloque extra. El bloque no entra entero: se
#                         toma un renglón de cada uno.
#   ('por bloque', R, E, bR, bE)
#                         igual, pero usando solo los primeros bR bloques de
#                         ejercicios y bE de extras. Los demás quedan en la
#                         página como práctica y no entran al examen.
#   ('ejercicios', R, E)  R ejercicios sueltos con respuesta + E extras.
#                         Para temas cuyos "bloques" son listas largas o
#                         repeticiones del mismo tipo.
# Varia tema por tema a proposito. Se ajusta aqui.
CURSOS = {
 'Matemáticas 1': ('../../math/matematicas-1', [
    ('operaciones-basicas.html',   'Operaciones básicas',       ('bloques', 1, 1)),
    # un bloque por tipo: una expresión con potencias y unos corchetes anidados
    ('jerarquia.html',             'Jerarquía de operaciones',  ('por bloque', 1, 1)),
    # un ejercicio del bloque de resueltos y uno de cada bloque de extra 1
    ('ecuaciones.html',            'Ecuaciones',                ('por bloque', 1, 1)),
    ('monomios.html',              'Monomios',                  ('ejercicios', 1, 2)),
    # cada bloque mezcla los dos tipos: uno del primer bloque resuelto y uno
    # de cada bloque de extras. El Bloque 2 de resueltos queda de práctica.
    ('expresiones-algebraicas.html','Expresiones algebraicas',  ('por bloque', 1, 1, 1, 2)),
    ('grafica-tabulacion.html',    'Gráfica con tabulación',    ('ejercicios', 1, 2)),
    ('pendiente-ordenada.html',    'Pendiente y ordenada',      ('ejercicios', 1, 2)),
    ('area-perimetro.html',        'Área y perímetro',          ('ejercicios', 1, 2)),
    ('ecuaciones-angulos.html',    'Ecuaciones con ángulos',    ('ejercicios', 1, 1)),
    ('reglas-exponentes.html',     'Reglas de exponentes',      ('ejercicios', 1, 2)),
    ('mcm-mcd.html',               'mcm y MCD',                 ('ejercicios', 1, 2)),
    ('lenguaje-algebraico.html',   'Lenguaje algebraico',       ('ejercicios', 1, 2)),
    ('problemas-ecuaciones.html',  'Problemas de ecuaciones',   ('ejercicios', 1, 2)),
 ]),
}

def raw(n):
    """Serializa un nodo de vuelta a HTML, para conservar los SVG tal cual."""
    if isinstance(n, str): return n
    a = ''.join(' %s="%s"' % (k, v.replace('"','&quot;')) for k, v in n.attrs.items())
    return '<%s%s>%s</%s>' % (n.tag, a, ''.join(raw(k) for k in n.kids), n.tag)

# El sitio puede partir los extras en "Ejercicios extra 1" y "Ejercicios extra 2".
# Cuando lo hace, el examen sale SOLO del 1: asi el alumno sabe que estudiar
# mirando la pagina, sin que se le diga. El 2 es practica y nunca entra.
FUENTE_EXTRA = ('Ejercicios extra 1', 'Ejercicios extra')

def secciones(path):
    p = P(); p.feed(open(path, encoding='utf-8').read())
    out = {}
    for sec in walk(p.root):
        if isinstance(sec, str) or 'section-block' not in sec.cls(): continue
        h2 = next((clean(text(x)) for x in walk(sec)
                   if not isinstance(x,str) and x.tag=='h2'), None)
        if h2 and (h2 == 'Ejercicios' or h2.startswith('Ejercicios extra')):
            out[h2] = sec
    return out

def seccion_extra(secs):
    """La seccion de la que salen los extras del examen."""
    for nombre in FUENTE_EXTRA:
        if nombre in secs: return secs[nombre], nombre
    return None, None

def reactivos(sec):
    """[(bloque, [reactivo,...]),...]  reactivo = {'tex':..} o {'svg':..}"""
    bloques = []
    cards = [c for c in walk(sec) if not isinstance(c,str) and 'mini-card' in c.cls()]
    if cards:
        for c in cards:
            head = next((clean(text(x)) for x in walk(c)
                         if not isinstance(x,str) and 'mini-card-head' in x.cls()), '')
            body = next((x for x in walk(c)
                         if not isinstance(x,str) and 'mini-card-body' in x.cls()), None)
            it = [{'tex': i} for i in items_of(body)] if body is not None else []
            if it: bloques.append((head, it))
        return bloques
    figs = [x for x in walk(sec) if not isinstance(x,str) and 'ejer-card-body' in x.cls()]
    if figs:
        it = []
        for f in figs:
            svg = next((raw(x) for x in walk(f) if not isinstance(x,str) and x.tag=='svg'), None)
            if svg: it.append({'svg': svg})
        if it: return [('', it)]
    rows = [clean(text(x)) for x in walk(sec) if not isinstance(x,str) and 'ej-row' in x.cls()]
    rows = [r for r in rows if r]
    if rows: return [('', [{'tex': r} for r in rows])]
    return []

def agregar_propios(tema, curso):
    """Suma al final los ejercicios que no estan en el sitio (ver propios.py)."""
    extra = PROPIOS.get(curso, {}).get(tema['titulo'])
    if not extra: return 0
    n = 0
    for seccion in ('con_respuesta', 'extras'):
        nuevos = [{'tex': t, 'propio': True} for t in extra.get(seccion, [])]
        if nuevos:
            tema[seccion] = tema[seccion] + [('Propios', nuevos)]
            n += len(nuevos)
    return n

def construir(curso):
    carpeta, temas = CURSOS[curso]
    carpeta = os.path.expanduser(carpeta)
    banco = []
    for arch, titulo, receta in temas:
        secs = secciones(os.path.join(carpeta, arch))
        sec_extra, de_donde = seccion_extra(secs)
        tema = {
            'archivo': arch, 'titulo': titulo, 'receta': list(receta),
            'con_respuesta': reactivos(secs['Ejercicios']) if 'Ejercicios' in secs else [],
            'extras':        reactivos(sec_extra) if sec_extra is not None else [],
            'fuente_extra':  de_donde,
        }
        tema['propios'] = agregar_propios(tema, curso)
        banco.append(tema)
    return banco

if __name__ == '__main__':
    import sys
    curso = sys.argv[1] if len(sys.argv) > 1 else 'Matemáticas 1'
    banco = construir(curso)
    json.dump(banco, open('banco.json','w'), ensure_ascii=False, indent=1)
    for t in banco:
        lc = [len(b[1]) for b in t['con_respuesta']]
        le = [len(b[1]) for b in t['extras']]
        modo, r, e = t['receta'][:3]
        if len(t['receta']) > 3: modo += ' de %d' % t['receta'][3]
        marca = '  (+%d propios)' % t['propios'] if t['propios'] else ''
        if t.get('fuente_extra') == 'Ejercicios extra 1': marca += '  [extra 1]'
        print('%-26s %-13s %d+%d  con respuesta=%2d %-18s extras=%2d %s%s'
              % (t['titulo'], modo, r, e, sum(lc), lc, sum(le), le, marca))
