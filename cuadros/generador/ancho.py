# -*- coding: utf-8 -*-
"""Ancho aproximado de una fórmula KaTeX, contando tokens: dígitos, letras,
operadores con su aire, fracciones (el más ancho de arriba y abajo), raíces,
exponentes chicos. Lo usa medida.py para saber si un renglón se parte.

Calibrado el 21-sep-2026 contra 45 fórmulas medidas en el navegador (Mate 1 y
Mate 5): el conteo sale un 25 % pasado de forma pareja, así que se corrige con
FACTOR y queda dentro de ±8 %. Antes se estimaba por número de caracteres, y
las fórmulas compactas de Mate 5 (exponentes, fracciones) daban falsas alarmas
de "¡NO CABE!" en hojas que cabían.
"""
import re

FUNC = {'sen': 1.5, 'sin': 1.3, 'cos': 1.4, 'tan': 1.4, 'ln': 0.9, 'sec': 1.4, 'log': 1.3}
CMD = {'pm': 1.22, 'cdot': 0.7, 'times': 1.22, 'div': 1.22, 'int': 1.3, 'sum': 1.5,
       'infty': 1.0, 'pi': 0.57, 'theta': 0.47, 'alpha': 0.64, 'beta': 0.57,
       'quad': 1.0, 'qquad': 2.0, ',': 0.17, ';': 0.28, ' ': 0.33, 'to': 1.3, 'Rightarrow': 1.4,
       'le': 1.33, 'ge': 1.33, 'ne': 1.33, 'approx': 1.33, 'lim': 1.5}

def _grupo(s, i):
    """s[i] == '{' -> (contenido, índice después de '}')."""
    prof, j = 0, i
    while j < len(s):
        if s[j] == '{': prof += 1
        elif s[j] == '}':
            prof -= 1
            if prof == 0: return s[i+1:j], j + 1
        j += 1
    return s[i+1:], len(s)

def _arg(s, i):
    """Argumento de un comando: {grupo} o un solo carácter/comando."""
    while i < len(s) and s[i] == ' ': i += 1
    if i >= len(s): return '', i
    if s[i] == '{': return _grupo(s, i)
    if s[i] == '\\':
        m = re.match(r'\\[a-zA-Z]+', s[i:])
        return (m.group(0), i + m.end()) if m else (s[i:i+2], i + 2)
    return s[i], i + 1

def em(s):
    w, i, prev = 0.0, 0, ''
    while i < len(s):
        c = s[i]
        if c == '\\':
            m = re.match(r'\\([a-zA-Z]+|.)', s[i:])
            name = m.group(1); i += m.end()
            if name in ('dfrac', 'frac', 'tfrac'):
                a, i = _arg(s, i); b, i = _arg(s, i)
                w += max(em(a), em(b)) + 0.25; prev = 'x'
            elif name == 'sqrt':
                if i < len(s) and s[i] == '[':
                    j = s.index(']', i); i = j + 1
                a, i = _arg(s, i)
                w += em(a) + 1.05; prev = 'x'
            elif name in ('operatorname', 'text', 'mathbf', 'mathrm', 'textbf'):
                a, i = _arg(s, i)
                w += (FUNC.get(a, len(a) * 0.5) + 0.17) if name == 'operatorname' else em(a) if name in ('mathbf', 'textbf') else len(a) * 0.5
                prev = 'x'
            elif name in ('left', 'right'):
                a, i = _arg(s, i); w += 0.45; prev = a
            elif name in FUNC:
                w += FUNC[name] + 0.17; prev = 'x'
            elif name in ('displaystyle', 'begin', 'end', 'limits'):
                if name in ('begin', 'end'): _a, i = _arg(s, i)
            elif name == '\\':
                pass
            else:
                w += CMD.get(name, 0.8); prev = 'x'
            continue
        if c in '^_':
            a, i = _arg(s, i + 1)
            w += 0.72 * em(a) + 0.05
            continue
        if c == '{':
            a, i = _grupo(s, i); w += em(a); prev = 'x'; continue
        if c == '}': i += 1; continue
        i += 1
        if c == ' ': continue
        if c.isdigit() or c == '.': w += 0.5
        elif c.isalpha(): w += 0.55 if c.islower() else 0.75
        elif c in '+-−':
            w += 0.78 + (0.44 if prev not in ('', '(', '[', '=', '+', '-', ',') else 0.05)
        elif c == '=': w += 0.78 + 0.56
        elif c in '()[]|': w += 0.39
        elif c == ',': w += 0.28 + 0.17
        elif c in '<>': w += 0.78 + 0.56
        elif c == '&': continue
        else: w += 0.5
        prev = c
    return w


FACTOR = 0.80          # el conteo por tokens sale un 25 % pasado, parejo

def ancho_em(tex):
    """Ancho de la fórmula en em de KaTeX, ya corregido."""
    return em(tex) * FACTOR
