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

def cosechar(ruta_html):
    """{clave normalizada del ejercicio: respuesta publicada}."""
    html = open(ruta_html, encoding='utf-8').read()
    por_tarjeta = cosechar_tarjetas(html)
    if por_tarjeta:
        return por_tarjeta
    pagina = parse_file(ruta_html)                  # listas paralelas: por posición
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
    return (t.get('manuales', {}).get(tex)
            or t.get('cosechadas', {}).get(norm(tex))
            or t.get('cosechadas', {}).get(tex))

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
