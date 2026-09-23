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
import json, os, re
from extraer import parse_html
from banco import CURSOS  # {curso: (ruta, [(archivo, titulo, receta), ...])}
from cursos import elegir, archivo

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


def norm(tex):
    """Clave para emparejar ejercicio con resolución: sin $, sin espacios y
    sin el '=' final que traen los enunciados ('$2x+3=$')."""
    t = re.sub(r'[\s$]', '', tex or '')
    return t[:-1] if t.endswith('=') else t

# Páginas que traen CADA resolución en su propia tarjeta (no en una lista
# paralela a los ejercicios). El parser las lee como un solo bloque y el
# emparejamiento por posición pega todo bajo el primer ejercicio. Aquí se
# leen tarjeta por tarjeta, sacando el LaTeX de cada <annotation>.
CONTENEDORES = ('ejemplo-item', 'po-block', 'tabulacion-block', 'tri-block', 'factor-block')
RE_TEX = re.compile(r'annotation encoding="application/x-tex">(.*?)</annotation>', re.S)
RE_H2 = re.compile(r'<h2>([^<]*)</h2>')

def _seccion_respuestas(html):
    """El HTML entre el <h2> de respuestas y el siguiente <h2>."""
    for m in RE_H2.finditer(html):
        if m.group(1).strip().lower() in NOMBRES_RESPUESTAS:
            n = RE_H2.search(html, m.end())
            return html[m.end(): n.start() if n else len(html)]
    return ''

def _aligned(lineas):
    return '$\\begin{aligned} ' + ' \\\\ '.join(lineas) + ' \\end{aligned}$'

def _con_amp(t):
    """'y = 5 - 3x' -> 'y &= 5 - 3x'; '\\mathbf{y = 5-3x}' -> '\\mathbf{y} &= \\mathbf{5-3x}'."""
    t = t.strip()
    m = re.match(r'^\\mathbf\{(.*)\}$', t)
    if m and '=' in m.group(1):
        l, r = m.group(1).split('=', 1)
        return '\\mathbf{%s} &= \\mathbf{%s}' % (l.strip(), r.strip())
    return t.replace('=', '&=', 1) if '=' in t else t

def _de_tarjeta(clase, cuerpo):
    """(clave, resolución) de una tarjeta, según su tipo. None si no aplica."""
    texs = [t.strip() for t in RE_TEX.findall(cuerpo)]
    if not texs: return None
    if clase == 'ejemplo-item':                       # Expresiones: un aligned por ejercicio
        t = texs[0]
        primera = t.split('\\\\')[0].replace('\\begin{aligned}', '')
        primera = primera.replace('&amp;', '').replace('&', '').strip().rstrip('=').strip()
        return primera, '$' + t.replace('&amp;', '&') + '$'
    if clase == 'po-block' and len(texs) >= 2:        # Pendiente: ecuación + despeje
        return texs[0], '$' + texs[1].replace('&amp;', '&') + '$'
    if clase == 'tabulacion-block':                   # Gráfica: ecuación, 'y', 3 pasos
        pasos = [t for t in texs[1:] if t != 'y'][:3]
        if len(pasos) < 3: return None
        return texs[0], _aligned([_con_amp(t) for t in pasos])
    if clase == 'tri-block':                          # Área: a, m, n, P con sus resultados
        lineas = []
        for ini in ('a =', 'm =', 'n =', 'P ='):
            i = next((k for k, t in enumerate(texs) if t.startswith(ini)), None)
            if i is None: continue
            trozos = [texs[i]]
            j = i + 1
            while j < len(texs) and (texs[j].startswith('=') or trozos[-1].endswith('=')):
                trozos.append(texs[j]); j += 1
                if not texs[j-1].startswith('='): break
            trozos = [t.replace('\\;', '\\,') for t in trozos]
            if ini in ('a =', 'P =') and len(trozos) >= 2:     # el resultado, resaltado (23-sep-2026)
                trozos[-1] = '\\mathbf{%s}' % trozos[-1]
            # en dos renglones para que quepa en la tarjeta angosta de la hoja
            if len(trozos) >= 3:
                lineas.append(_con_amp(' '.join(trozos[:-1])))
                lineas.append('&' + trozos[-1])
            elif len(trozos) == 2 and ini == 'P =':
                lineas.append(_con_amp(trozos[0].rstrip('= ')))
                lineas.append('&= ' + trozos[1])
            else:
                lineas.append(_con_amp(' '.join(trozos)))
        if not lineas: return None
        return texs[0], _aligned(lineas)
    if clase == 'factor-block' and len(texs) >= 3:    # mcm / MCD
        m = re.search(r'<span class="ej-label">\s*([A-Za-z]+)', cuerpo)
        etiqueta = m.group(1) if m else ''
        return etiqueta + ' ' + texs[0], '$' + texs[1] + ' ' + texs[2] + '$'
    return None

def cosechar_tarjetas(html):
    sec = _seccion_respuestas(html)
    out = {}
    for clase in CONTENEDORES:
        marca = '<div class="%s">' % clase
        partes = sec.split(marca)[1:]
        for cuerpo in partes:
            r = _de_tarjeta(clase, cuerpo)
            if r: out[norm(r[0])] = r[1]
    return out

RE_DIV = re.compile(r'<div\b|</div>')

def _quitar_divs(html, clase):
    """Quita los <div class="clase"...>...</div> completos (con lo que traigan dentro)."""
    pat = re.compile(r'<div class="%s[" ]' % re.escape(clase))
    while True:
        m = pat.search(html)
        if not m: return html
        prof = 0
        for t in RE_DIV.finditer(html, m.start()):
            prof += -1 if t.group() == '</div>' else 1
            if prof == 0:
                html = html[:m.start()] + html[t.end():]
                break
        else:
            return html

# Lo que sobra en la hoja resuelta: el rótulo "Ejercicio N — ..." repite el
# enunciado, y las tablas de valores y gráficas de Recta tangente no se pueden
# leer como texto corrido.
SIN_COSECHAR = ('sol-rotulo', 'graficas-row')

def cosechar(ruta_html):
    """{clave normalizada del ejercicio: respuesta publicada}."""
    html = open(ruta_html, encoding='utf-8').read()
    por_tarjeta = cosechar_tarjetas(html)
    if por_tarjeta:
        return por_tarjeta
    for clase in SIN_COSECHAR:
        html = _quitar_divs(html, clase)
    pagina = parse_html(html)                       # listas paralelas: por posición
    ejercicios = secciones(pagina, NOMBRES_EJERCICIOS)
    respuestas = secciones(pagina, NOMBRES_RESPUESTAS)
    if not ejercicios or not respuestas:
        return {}
    out = {}
    for sec_e, sec_r in zip(ejercicios, respuestas):
        for card_e, card_r in zip(sec_e['cards'], sec_r['cards']):
            for tex, resp in zip(card_e['items'], card_r['items']):
                resp = limpio(resp)
                if resp: out[norm(tex)] = resp
    return out

# ── Gráficas de las respuestas publicadas (23-sep-2026) ──────────────────────
# Lety quiere la hoja resuelta "más parecida a la resolución del ejemplo, incluyendo gráfica
# cuando es necesario". Se toma la gráfica que ya publica la página junto a cada respuesta.
RE_SVG = re.compile(r'<svg\b[^>]*\brole="img"[^>]*>.*?</svg>', re.S)

def graficas(ruta_html):
    """({clave del ejercicio: svg}, {número de figura: [resolución, svg]}).
    Tarjetas (tri-block, tabulacion-block…): la clave es la misma de la cosecha.
    Triángulos de ángulos: el ejercicio es una figura, se empareja por 'Triángulo N'.
    Listas paralelas (Recta tangente): la n-ésima respuesta es del n-ésimo ejercicio."""
    html = open(ruta_html, encoding='utf-8').read()
    sec = _seccion_respuestas(html)
    if not RE_SVG.search(sec):
        return {}, {}
    por_clave, por_figura = {}, {}
    for clase in CONTENEDORES:
        for cuerpo in sec.split('<div class="%s">' % clase)[1:]:
            svg = RE_SVG.search(cuerpo)
            if not svg: continue
            fig = re.search(r'aria-label="Tri[aá]ngulo (\d+) — respuesta"', svg.group(0))
            if fig:
                texs = [t.strip().replace('&amp;', '&') for t in RE_TEX.findall(cuerpo)]
                res = ' '.join('$%s$' % t for t in texs[:1] + texs[2:])
                por_figura[fig.group(1)] = [res, svg.group(0)]
                continue
            r = _de_tarjeta(clase, cuerpo)
            if r: por_clave[norm(r[0])] = svg.group(0)
    if not por_clave and not por_figura:
        pagina = parse_html(html)
        ejercicios = [x for s_ in secciones(pagina, NOMBRES_EJERCICIOS) for c in s_['cards'] for x in c['items']]
        trozos = sec.split('<div class="sol">')[1:]
        for tex, trozo in zip(ejercicios, trozos):
            svg = RE_SVG.search(trozo)
            if svg: por_clave[norm(tex)] = svg.group(0)
    return por_clave, por_figura

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
        g, f = graficas(ruta)
        banco[titulo] = {'cosechadas': cosechar(ruta), 'manuales': {}, 'graficas': g, 'figuras': f}
    # gráficas y figuras de los extras, dibujadas aparte (23-sep-2026)
    ruta_g = 'graficas-manuales.json'
    if os.path.exists(ruta_g):
        for titulo, d in json.load(open(ruta_g)).get(curso, {}).items():
            t = banco.setdefault(titulo, {'cosechadas': {}, 'manuales': {}, 'graficas': {}, 'figuras': {}})
            t.setdefault('graficas', {}).update({norm(k): v for k, v in d.get('graficas', {}).items()})
            t.setdefault('figuras', {}).update(d.get('figuras', {}))
    for titulo, res in manuales().get(curso, {}).items():
        banco.setdefault(titulo, {'cosechadas': {}, 'manuales': {}})['manuales'] = res
    return banco

def grafica_de(banco, tema, item):
    """La gráfica de la respuesta publicada, si la hay."""
    t = banco.get(tema, {})
    if 'tex' in item:
        return t.get('graficas', {}).get(norm(item['tex']))
    return None

def figura_de(banco, tema, item):
    """[resolución, svg] de un ejercicio que es una figura (triángulos de ángulos)."""
    m = re.search(r'aria-label="(Tri[aá]ngulo \d+|Extra \d+)[:\s]', item.get('svg', ''))
    if not m: return None
    figs = banco.get(tema, {}).get('figuras', {})
    return figs.get(m.group(1)) or figs.get(m.group(1).split()[-1])

def resolucion_de(banco, tema, tex):
    """La resolución escrita a mano gana: es la que Lety revisó."""
    t = banco.get(tema, {})
    return (t.get('manuales', {}).get(tex)
            or t.get('cosechadas', {}).get(norm(tex))
            or t.get('cosechadas', {}).get(tex))

if __name__ == '__main__':
    curso, _ = elegir()
    banco = construir(curso)
    # resoluciones.json guarda todos los cursos; aquí se reescribe solo el de hoy
    todas = json.load(open(SALIDA)) if os.path.exists(SALIDA) else {}
    todas[curso] = banco
    json.dump(todas, open(SALIDA, 'w'), ensure_ascii=False, indent=1)

    sel = json.load(open(archivo('seleccion', curso)))
    print(curso)
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
