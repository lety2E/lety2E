"""Math 4 · Tema 12 · Ecuaciones exponenciales y logarítmicas.

Fuente (capturas): leyes de exponentes y definición de logaritmo (apuntes); 3 exponenciales
resueltas (resueltos1) y 5 logarítmicas resueltas (ejemplo, ejemplos1, 2, 4) → Ejemplos;
ejercicios1 (9 exponenciales, SIN hoja de resueltos: se resolvieron aquí con los pasos de los
ejemplos), ejercicios2 (9 logarítmicas, con resueltos2) y ejercicios3 (4 con potencia, sin
resolver → van a extras).
"""
import pathlib
from fractions import Fraction
exec(pathlib.Path(__file__).with_name("tema9.py").read_text().split("def division")[0])   # term, tex, reduce, neg, mult
exec("def junta(p):\n    o, d = [], {}\n    for c, e in p:\n        if e not in d:\n            o.append(e); d[e] = 0\n        d[e] += c\n    return [(d[e], e) for e in o if d[e]]")

def L(*t):                      # L(3, -2) = 3x − 2 ; L((3,0), (-4,1)) = 3 − 4x
    if isinstance(t[0], tuple):
        return list(t)
    a, b = t
    return [(a, 1)] + ([(b, 0)] if b else [])

def por(k, E):
    return [(k * c, e) for c, e in E]

def fr(q):
    return str(q.numerator) if q.denominator == 1 else ("-" if q < 0 else "") + f"\\dfrac{{{abs(q.numerator)}}}{{{q.denominator}}}"

def despeje(izq, der):
    """izq = der (términos) → renglones hasta x = …  Devuelve (renglones, x)."""
    xs = [t for t in izq if t[1]] + neg([t for t in der if t[1]])
    cs = [t for t in der if not t[1]] + neg([t for t in izq if not t[1]])
    l = []
    if len(xs) > 1 or len(cs) > 1 or any(t[1] for t in der) or any(not t[1] for t in izq):
        l.append(f"{tex(xs)} &= {tex(cs)}")
    A = sum(c for c, _ in xs); B = sum(c for c, _ in cs)
    if len(xs) > 1 or len(cs) > 1:
        l.append(f"{tex([(A, 1)])} &= {B}")
    x = Fraction(B, A)
    if A == 1:
        pass
    else:
        cruda = f"\\dfrac{{{B}}}{{{A}}}"
        l.append(f"x &= {cruda}" + (f" = {fr(x)}" if fr(x) != cruda else ""))
    l[-1] = l[-1].rsplit("= ", 1)[0] + "= \\boldsymbol{" + l[-1].rsplit("= ", 1)[1] + "}"
    return l, x

def exp_bases(a, E1, b, E2, p, m, n):
    assert p ** m == a and p ** n == b
    enun = f"{a}^{{{tex(E1)}}} = {b}^{{{tex(E2)}}}"
    l = [enun.replace(" = ", " &= "),
         f"({p}^{{{m}}})^{{{tex(E1)}}} &= ({p}^{{{n}}})^{{{tex(E2)}}}",
         f"{p}^{{{tex(por(m, E1))}}} &= {p}^{{{tex(por(n, E2))}}}",
         f"{tex(por(m, E1))} &= {tex(por(n, E2))}"]
    d, x = despeje(por(m, E1), por(n, E2))
    return enun, l + d, x

def exp_prod(p, E1, E2, N, k, cociente=False):
    assert p ** k == N
    if cociente:
        enun = f"\\dfrac{{{p}^{{{tex(E1)}}}}}{{{p}^{{{tex(E2)}}}}} = {N}"
        junto = E1 + neg(E2)
        l = [enun.replace(" = ", " &= "), f"{p}^{{{tex(E1)} - ({tex(E2)})}} &= {N}"]
        if len(E2) > 1:
            l.append(f"{p}^{{{tex(junto)}}} &= {N}")
    else:
        enun = f"{p}^{{{tex(E1)}}}({p}^{{{tex(E2)}}}) = {N}"
        junto = E1 + E2
        l = [enun.replace(" = ", " &= "), f"{p}^{{{tex(junto)}}} &= {N}"]
    S = junta(junto)
    l += [f"{p}^{{{tex(S)}}} &= {N}", f"\\log_{{{p}}}({p}^{{{tex(S)}}}) &= \\log_{{{p}}} {N}", f"{tex(S)} &= {k}"]
    d, x = despeje(S, [(k, 0)])
    return enun, l + d, x

def ev(E, x):
    return sum(c * (x if e else 1) for c, e in E)

# ── comprobación de cada exponencial con su x ──
def comprueba(tipo, args, x):
    import math
    if tipo == "bases":
        a, E1, b, E2, p, m, n = args
        assert m * ev(E1, x) == n * ev(E2, x)
    else:
        p, E1, E2, N, k = args[:5]
        s = ev(E1, x) - ev(E2, x) if (len(args) > 5 and args[5]) else ev(E1, x) + ev(E2, x)
        assert s == k

def EXP(tipo, *args):
    enun, l, x = (exp_bases if tipo == "bases" else exp_prod)(*args)
    comprueba(tipo, args, x)
    return enun, l, x

EJ_EXP = [EXP("bases", 4, L(3, -2), 8, L(1, -4), 2, 2, 3),
          EXP("prod", 2, L(1, 0), L(3, -2), 16, 4),
          EXP("prod", 4, L(2, 3), L(5, -1), 64, 3, True)]
assert [fr(e[2]) for e in EJ_EXP] == ["-\\dfrac{8}{3}", "\\dfrac{3}{2}", "\\dfrac{1}{3}"]      # resueltos1

EXPS = [EXP("bases", 9, L(5, -1), 27, L(1, -2), 3, 2, 3),
        EXP("bases", 16, L(4, -1), 8, L(1, 6), 2, 4, 3),
        EXP("bases", 25, L((3, 0), (-4, 1)), 125, L(6, -3), 5, 2, 3),
        EXP("prod", 3, L(1, 0), L(2, -5), 81, 4),
        EXP("prod", 5, L(2, 0), L((6, 0), (-1, 1)), 125, 3),
        EXP("prod", 4, L(1, 3), L((2, 0), (-3, 1)), 16, 2),
        EXP("prod", 5, L(1, -6), L(2, -4), 125, 3, True),
        EXP("prod", 5, L(3, -1), L(4, 0), 25, 2, True),
        EXP("prod", 3, L(1, -2), L((6, 0), (-4, 1)), 81, 4, True)]
print("exponenciales:", [fr(e[2]) for e in EXPS])

X_EXP = [EXP("bases", 4, L(2, 1), 8, L(1, -3), 2, 2, 3), EXP("bases", 27, L(1, -1), 9, L(2, 3), 3, 3, 2),
         EXP("bases", 8, L(3, -2), 16, L(1, 1), 2, 3, 4),
         EXP("prod", 2, L(3, 0), L(1, -5), 8, 3), EXP("prod", 3, L(1, 4), L(2, -1), 27, 3),
         EXP("prod", 6, L(2, -3), L((4, 0), (-1, 1)), 36, 2),
         EXP("prod", 2, L(5, -3), L(2, 1), 32, 5, True), EXP("prod", 7, L(4, 0), L(1, -5), 49, 2, True),
         EXP("prod", 3, L(2, 7), L(5, -2), 27, 3, True)]

# ── logarítmicas: transcritas de las hojas (enunciado, renglones) ──
def lg(b, arg):
    return f"\\log_{{{b}}}({arg})" if b else f"\\log({arg})"
B_ = lambda s: f"\\boldsymbol{{{s}}}"
EJ_LOG = [
    (f"{lg(5, '10x - 3')} = 3",
     ["5^3 &= 10x - 3", "125 &= 10x - 3", "125 + 3 &= 10x", "128 &= 10x", "x &= \\dfrac{128}{10}", f"x &= \\boldsymbol{{12.8}}"]),
    (f"{lg(2, '6x - 4')} = {lg(2, '3x - 1')}",
     ["6x - 4 &= 3x - 1", "6x - 3x &= -1 + 4", "3x &= 3", f"x &= \\boldsymbol{{1}}"]),
    (f"{lg(3, '2x - 1')} - \\log_3 5 = {lg(3, '4x - 3')}",
     [f"\\log_3\\left(\\dfrac{{2x - 1}}{{5}}\\right) &= {lg(3, '4x - 3')}", "\\dfrac{2x - 1}{5} &= 4x - 3", "2x - 1 &= 5(4x - 3)",
      "2x - 1 &= 20x - 15", "2x - 20x &= -15 + 1", "-18x &= -14", f"x &= \\dfrac{{-14}}{{-18}} = \\boldsymbol{{\\dfrac{{7}}{{9}}}}"]),
    (f"{lg(5, '3x - 4')} + \\log_5 6 = {lg(5, '8x - 1')}",
     [f"\\log_5[6(3x - 4)] &= {lg(5, '8x - 1')}", f"{lg(5, '18x - 24')} &= {lg(5, '8x - 1')}", "18x - 24 &= 8x - 1",
      "18x - 8x &= -1 + 24", "10x &= 23", "x &= \\dfrac{23}{10}", f"x &= \\boldsymbol{{2.3}}"]),
    ("\\log(3x - 5)^2 = 6",
     ["2\\log(3x - 5) &= 6", "\\log(3x - 5) &= \\dfrac{6}{2}", "\\log(3x - 5) &= 3", "10^3 &= 3x - 5", "1000 + 5 &= 3x",
      "1005 &= 3x", "\\dfrac{1005}{3} &= x", f"x &= \\boldsymbol{{335}}"]),
]
LOGS = [
    (f"{lg(3, '5x + 2')} = 4", ["3^4 &= 5x + 2", "81 &= 5x + 2", "81 - 2 &= 5x", "79 &= 5x", f"x &= \\boldsymbol{{\\dfrac{{79}}{{5}}}}"]),
    (f"{lg(4, '6x - 7')} = 3", ["4^3 &= 6x - 7", "64 &= 6x - 7", "64 + 7 &= 6x", "71 &= 6x", f"x &= \\boldsymbol{{\\dfrac{{71}}{{6}}}}"]),
    (f"{lg(2, '8x + 1')} = 5", ["2^5 &= 8x + 1", "32 &= 8x + 1", "32 - 1 &= 8x", "31 &= 8x", f"x &= \\boldsymbol{{\\dfrac{{31}}{{8}}}}"]),
    (f"{lg(3, '3x + 5')} = {lg(3, 'x - 4')}", ["3x + 5 &= x - 4", "3x - x &= -4 - 5", "2x &= -9", f"x &= \\boldsymbol{{-\\dfrac{{9}}{{2}}}}"]),
    (f"{lg(6, 'x - 8')} = {lg(6, '5x + 2')}", ["x - 8 &= 5x + 2", "x - 5x &= 2 + 8", "-4x &= 10",
                                                f"x &= \\dfrac{{10}}{{-4}} = \\boldsymbol{{-\\dfrac{{5}}{{2}}}}"]),
    (f"{lg(2, '4x + 5')} = {lg(2, '6x - 1')}", ["4x + 5 &= 6x - 1", "4x - 6x &= -1 - 5", "-2x &= -6", "x &= \\dfrac{-6}{-2}", f"x &= \\boldsymbol{{3}}"]),
    (f"{lg(2, '2x - 3')} - {lg(2, '4')} = {lg(2, '4x - 1')}",
     [f"\\log_2\\left(\\dfrac{{2x - 3}}{{4}}\\right) &= {lg(2, '4x - 1')}", "\\dfrac{2x - 3}{4} &= 4x - 1", "2x - 3 &= 4(4x - 1)",
      "2x - 3 &= 16x - 4", "2x - 16x &= -4 + 3", "-14x &= -1", f"x &= \\dfrac{{-1}}{{-14}} = \\boldsymbol{{\\dfrac{{1}}{{14}}}}"]),
    (f"{lg(4, '8x + 4')} - {lg(4, '5')} = {lg(4, '2x + 1')}",
     [f"\\log_4\\left(\\dfrac{{8x + 4}}{{5}}\\right) &= {lg(4, '2x + 1')}", "\\dfrac{8x + 4}{5} &= 2x + 1", "8x + 4 &= 5(2x + 1)",
      "8x + 4 &= 10x + 5", "8x - 10x &= 5 - 4", "-2x &= 1", f"x &= \\boldsymbol{{-\\dfrac{{1}}{{2}}}}"]),
    (f"{lg(7, '5x - 2')} + {lg(7, '1')} = {lg(7, '6x - 3')}",
     [f"\\log_7[(5x - 2)(1)] &= {lg(7, '6x - 3')}", f"{lg(7, '5x - 2')} &= {lg(7, '6x - 3')}", "5x - 2 &= 6x - 3",
      "5x - 6x &= -3 + 2", "-x &= -1", f"x &= \\boldsymbol{{1}}"]),
]
X_LOG = [f"{lg(2, '3x + 1')} = 4", f"{lg(5, '4x - 3')} = 2", f"{lg(3, '7x - 1')} = 3",
         f"{lg(4, '5x - 2')} = {lg(4, '2x + 7')}", f"{lg(2, '7x - 3')} = {lg(2, '4x + 9')}", f"{lg(5, '9x - 4')} = {lg(5, '3x + 8')}",
         f"{lg(3, '10x + 2')} - {lg(3, '4')} = {lg(3, 'x + 5')}", f"{lg(2, '3x - 1')} + {lg(2, '5')} = {lg(2, '7x + 11')}",
         f"{lg(6, '9x + 3')} - {lg(6, '2')} = {lg(6, 'x + 12')}"]
X_POT = ["\\log(5x - 3)^2 = 8", "\\log(3x + 5)^3 = 28", "\\log(4x - 1)^2 = 16", "\\log(6x + 4)^3 = 100"]     # ejercicios3

def res(enun, lineas, con_enunciado=True):
    cab = f'<div class="ej-line">${enun}$</div>\n' if con_enunciado else ""
    return (f'<div class="ec-item">\n{cab}<div class="sol">$$\\begin{{aligned}} ' + " \\\\ ".join(lineas)
            + ' \\end{aligned}$$</div>\n</div>')

def card(titulo, enuns):
    filas = "\n".join(f'          <div class="ej-line">${e}$</div>' for e in enuns)
    return (f'        <div class="mini-card">\n          <div class="mini-card-head">{titulo}</div>\n'
            f'          <div class="mini-card-body">\n{filas}\n          </div>\n        </div>')

ap = apuntes([
    "<strong>Leyes de los exponentes</strong>",
    "$a^m a^n = a^{m+n} \\qquad \\dfrac{a^m}{a^n} = a^{m-n} \\qquad (a^m)^n = a^{mn}$",
    "<strong>Logaritmo</strong>",
    "$\\log_a N = x \\iff a^x = N$",
    "Por ejemplo, $\\log_3 81 = x$ es lo mismo que $3^x = 81$, así que $x = 4$.",
])
ej1 = G.seccion_ejemplo('        <div class="ec-grid">\n' + "\n".join(res(e, l[1:] if False else l, False) for e, l, _ in EJ_EXP)
                        + '\n        </div>', titulo="Ejemplos · Ecuaciones exponenciales")
ej2 = G.seccion_ejemplo('        <div class="ec-grid">\n' + "\n".join(res(e, l) for e, l in EJ_LOG)
                        + '\n        </div>', titulo="Ejemplos · Ecuaciones logarítmicas")
ejercicios = G.seccion("Ejercicios", "ejercicios",
    '      <p class="enunciado">Resuelve las siguientes ecuaciones.</p>\n'
    + G.grid([card("Bloque 1 · Exponenciales", [e[0] for e in EXPS]), card("Bloque 2 · Logarítmicas", [e[0] for e in LOGS])], 2))
# Bloque 1 (exponenciales) no trae hoja de resueltos: se publica sin respuesta. Las resoluciones
# calculadas quedan en EXPS por si Lety las quiere; basta volver a agregar ese bloque aquí.
respuestas = G.seccion("Respuestas", "respuestas", G.resol_grid([
    '          <div class="resol-item">\n            <div class="resol-num">Bloque 2 · Logarítmicas</div>\n            <div class="ec-grid">\n'
    + "\n".join(res(e, l) for e, l in LOGS) + '\n            </div>\n          </div>']), colapsable=True)
extras = G.seccion("Ejercicios extra", "extra",
    '      <p class="enunciado">Resuelve las siguientes ecuaciones.</p>\n'
    + G.grid([card("Bloque 1 · Exponenciales", [e[0] for e in X_EXP]), card("Bloque 2 · Logarítmicas", X_LOG + X_POT)], 2),
    colapsable=True)

CSS = CSS_COMUN + """
    .ec-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: .9rem; }
    @media (max-width: 900px) { .ec-grid { grid-template-columns: 1fr 1fr; } }
    @media (max-width: 560px) { .ec-grid { grid-template-columns: 1fr; } }
    .ec-item { border: 1px solid var(--border-s); border-radius: var(--r-md); padding: .7rem .5rem; text-align: center; }
    .ec-item .ej-line { text-align: center; }
    .mini-card-body { text-align: center; }
    @media (max-width: 480px) { .sol .katex-display { font-size: .82em; } .ec-item .ej-line .katex { font-size: .8em; } }
"""
G.pagina("ecuaciones-exponenciales-logaritmicas", 12, "Ecuaciones exponenciales y logarítmicas",
         "Ecuaciones exponenciales y logarítmicas: leyes de exponentes, definición de logaritmo, ejemplos y ejercicios resueltos.",
         [ap, ej1, ej2, ejercicios, respuestas, extras],
         prev=("dominio-maximo.html", "Dominio máximo"),
         sig=("sucesiones-series.html", "Sucesiones y series"), css_extra=CSS)
print("ok tema 12")
