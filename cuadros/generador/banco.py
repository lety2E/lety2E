#!/usr/bin/env python3
"""Construye el banco de reactivos de un curso a partir del sitio (SOLO LECTURA).

Por cada tema guarda dos listas: los ejercicios que en la pagina traen respuesta
(seccion "Ejercicios") y los que no (seccion "Ejercicios extra"), conservando
los bloques tal como estan en el sitio.
"""
import os, json
from extraer import P, walk, text, clean, items_of
from propios import PROPIOS
from cursos import elegir, archivo

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
#   ('cruzado', R, E)     los bloques son tipos (dos): R del bloque k de
#                         resueltos + E del OTRO bloque de extras, alternando
#                         k en cada version. Un tipo resuelto y el otro extra.
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
    # como Operaciones básicas: 1 bloque resuelto entero + 1 bloque extra
    # entero (5 tipos cada uno). Decidido por Lety el 17-sep-2026; para
    # las seis versiones se escribieron los bloques 5-6 y 11-12.
    ('monomios.html',              'Monomios',                  ('bloques', 1, 1)),
    # un bloque por tipo (17-sep-2026): Bloque 1 y Bloque A sin binomio al
    # cuadrado, Bloque 2 y Bloque B con él. Cada versión: uno del Bloque 1
    # (resuelto, sin cuadrado) + uno de A (sin) + uno de B (con). El Bloque 2
    # de resueltos queda de práctica.
    ('expresiones-algebraicas.html','Expresiones algebraicas',  ('por bloque', 1, 1, 1, 2)),
    # bloques por tipo, en el mismo orden en los dos lados: Bloque 1 y Bloque A
    # pendiente negativa, Bloque 2 y Bloque B positiva. Cada versión: 1 resuelto + 1 extra, uno de cada
    # signo (Lety, 17-sep-2026). Los extras salen de "Ejercicios extra 1".
    ('grafica-tabulacion.html',    'Gráfica con tabulación',    ('cruzado', 1, 1)),
    # bloques por tipo: Bloque 1 y Bloque A ordenada positiva, Bloque 2 y
    # Bloque B negativa; el Bloque 3 de resueltos es práctica. Cada versión:
    # 1 resuelto + 1 extra, uno de cada signo (Lety, 17-sep-2026).
    ('pendiente-ordenada.html',    'Pendiente y ordenada',      ('cruzado', 1, 1)),
    # 1 resuelto + 1 de "Ejercicios extra 1" (Lety, 17-sep-2026). Se escribió
    # el sexto resuelto para que alcance a las seis versiones.
    ('area-perimetro.html',        'Área y perímetro',          ('por bloque', 1, 1)),
    # 1 resuelto + 1 de "Ejercicios extra 1" (Lety, 17-sep-2026). Se dibujaron
    # el sexto triángulo resuelto y el sexto extra.
    ('ecuaciones-angulos.html',    'Ecuaciones con ángulos',    ('por bloque', 1, 1)),
    ('reglas-exponentes.html',     'Reglas de exponentes',      ('ejercicios', 1, 2)),
    ('mcm-mcd.html',               'mcm y MCD',                 ('ejercicios', 1, 2)),
    ('lenguaje-algebraico.html',   'Lenguaje algebraico',       ('ejercicios', 1, 2)),
    ('problemas-ecuaciones.html',  'Problemas de ecuaciones',   ('ejercicios', 1, 2)),
 ]),
 # Matemáticas 5 (21-sep-2026). Lety pidió reproducir los patrones de Mate 1 en
 # los 19 temas de una vez: bloques por tipo en el mismo orden en los dos lados
 # (Bloque 1 <-> Bloque A), cada versión 1 resuelto + extras de "Ejercicios
 # extra 1" de tipo distinto (modo cruzado): 1+2 en los temas mecánicos (reglas
 # de derivación e integrales), 1+1 en los pesados (problemas, gráficas, Riemann).
 # "Ejercicios extra 2" es práctica. Donde
 # no alcanzaban los resueltos se escribieron (Velocidad 2, Senos 1, Recta
 # tangente 1, Puntos críticos 2, Optimización 2, Área bajo la curva 1 y 1,
 # Riemann 2), verificados con sympy. Qué bloque es qué tipo, en la página.
 'Matemáticas 5': ('../../math/matematicas-5', [
    # Lety (21-sep-2026): 4 por versión, 2 de cada tipo — uno de cada bloque
    # resuelto (B1 polinomios, B2 con x en el denominador) y uno de cada bloque
    # de extra 1 (A polinomios, B mixtos), seis por bloque. El B3 de resueltos
    # (sólo x en el denominador + 2 mixtos) es práctica, como el extra 2.
    ('reglas-basicas.html',        'Reglas básicas de derivación',    ('por bloque', 1, 1, 2, 2)),
    # B1 parábola hacia arriba (t^2 positivo), B2 hacia abajo
    ('velocidad-media.html',       'Velocidad media e instantánea',   ('cruzado', 1, 1)),
    # Lety (22-sep-2026): los 6 resueltos en un bloque y dos bloques de 6 extras
    # igual de largos. Cada versión: 1 resuelto + 1 de cada bloque de extra 1 = 3.
    ('senos-cosenos.html',         'Derivadas de senos y cosenos',    ('por bloque', 1, 1)),
    # Lety (22-sep-2026): tres tipos, un bloque de 6 por tipo en los dos lados
    # (1 exponente mayor que el índice, 2 menor, 3 fracción con la raíz abajo).
    # Cada versión: uno de cada bloque = 3 resueltos + 3 extras.
    ('raices.html',                'Derivadas de raíces',             ('por bloque', 1, 1)),
    # Lety (22-sep-2026): "es más proceso", sólo dos al examen. Un bloque de 6
    # resueltos y uno de 6 en extra 1: uno de cada uno. Lo demás es extra 2.
    ('regla-producto-p1.html',     'Regla del producto (P1)',         ('por bloque', 1, 1)),
    # Lety (22-sep-2026): tres tipos — monomio × trascendente, trascendente ×
    # trascendente, raíz × trascendente —, 2 resueltos y 4 extras por tipo (B1/A,
    # B2/B, B3/C; el Bloque 4 es práctica y no entra). Cada versión 1 resuelto + 2
    # extras, los tres de tipo distinto.
    ('regla-producto-p2.html',     'Regla del producto (P2)',         ('rotado', 1, 2)),
    # Lety (22-sep-2026): 1 resuelto + 1 extra, cruzados por tipo. Bloque 1 y A
    # con número suelto en el denominador, Bloque 2 y B sin él: la versión a
    # lleva 1 y B, la b lleva 2 y A, y así alternando.
    ('regla-cociente-p1.html',     'Regla del cociente (P1)',         ('cruzado', 1, 1)),
    # Lety (22-sep-2026), con la lógica de Producto P2: tres tipos —términos
    # simples, binomio arriba, binomio abajo—, 2 resueltos y 4 extras por tipo
    # (B1/A, B2/B, B3/C). Cada versión 1 resuelto + 2 extras, uno de cada tipo.
    ('regla-cociente-p2.html',     'Regla del cociente (P2)',         ('rotado', 1, 2)),
    # Lety (22-sep-2026): 6 por tipo = 4 resueltos + 2 extras (B1/A cubos, B2/B
    # cuadrados, B3/C raíces). Cada versión 2 resueltos + 1 extra, uno de cada tipo.
    ('regla-cadena-p1.html',       'Regla de la cadena (P1)',         ('rotado', 2, 1)),
    # Lety (22-sep-2026): cuatro tipos —raíz de una potencia trigonométrica,
    # trigonométrica de un polinomio, logaritmo, potencia de una trigonométrica—
    # (B1/A … B4/D), 3 resueltos + 3 extras por tipo. Cada versión 2 resueltos +
    # 2 extras, los cuatro tipos: las 6 parejas posibles de tipos, una por versión.
    ('regla-cadena-p2.html',       'Regla de la cadena (P2)',         ('rotado', 2, 2)),
    # B1 parábola hacia arriba, B2 hacia abajo
    ('recta-tangente.html',        'Recta tangente',                  ('cruzado', 1, 1)),
    # B1 cúbico positivo, B2 negativo
    ('puntos-criticos.html',       'Puntos críticos',                 ('cruzado', 1, 2)),
    ('optimizacion-areas.html',    'Optimización de áreas',           ('cruzado', 1, 1)),
    ('integrales-indefinidas.html','Integrales indefinidas',          ('cruzado', 1, 2)),
    ('integrales-definidas.html',  'Integrales definidas',            ('cruzado', 1, 2)),
    # B1 pendiente positiva, B2 negativa
    ('area-bajo-curva-p1.html',    'Área bajo la curva (P1)',         ('cruzado', 1, 1)),
    # B1 parábola hacia arriba, B2 hacia abajo
    ('area-bajo-curva-p2.html',    'Área bajo la curva (P2)',         ('cruzado', 1, 1)),
    # B1 lineales, B2 cuadráticas puras, B3 cuadráticas completas
    ('derivada-definicion.html',   'Derivada por definición',         ('cruzado', 1, 1)),
    # B1 x^2 positivo, B2 negativo
    ('suma-riemann.html',          'Suma de Riemann',                 ('cruzado', 1, 1)),
    # historia-calculo.html no tiene ejercicios: no entra al examen.
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

def figura_de(n):
    """El <svg> de figura dentro de un nodo, saltando los que KaTeX mete en las
    raíces (van dentro de un span.katex)."""
    if isinstance(n, str): return None
    if n.tag == 'svg': return raw(n)
    if 'katex' in n.cls(): return None
    for k in n.kids:
        r = figura_de(k)
        if r: return r
    return None

def figuras_de(body):
    """Por cada .ej-line del cuerpo, su <svg> de figura o None."""
    out = []
    for x in walk(body):
        if isinstance(x, str) or 'ej-line' not in x.cls(): continue
        if not clean(text(x)): continue
        out.append(figura_de(x))
    return out

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
            # un .ej-line con figura adentro (Optimización: el rectángulo y su
            # perímetro) lleva las dos cosas: el svg se imprime y el tex es la llave
            figs = figuras_de(body) if body is not None else []
            if figs and len(figs) == len(it):
                for r, svg in zip(it, figs):
                    if svg: r['svg'] = svg
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
    curso, _ = elegir()
    banco = construir(curso)
    json.dump(banco, open(archivo('banco', curso),'w'), ensure_ascii=False, indent=1)
    print('%s -> %s' % (curso, archivo('banco', curso)))
    for t in banco:
        lc = [len(b[1]) for b in t['con_respuesta']]
        le = [len(b[1]) for b in t['extras']]
        modo, r, e = t['receta'][:3]
        if len(t['receta']) > 3: modo += ' de %d' % t['receta'][3]
        marca = '  (+%d propios)' % t['propios'] if t['propios'] else ''
        if t.get('fuente_extra') == 'Ejercicios extra 1': marca += '  [extra 1]'
        print('%-26s %-13s %d+%d  con respuesta=%2d %-18s extras=%2d %s%s'
              % (t['titulo'], modo, r, e, sum(lc), lc, sum(le), le, marca))
