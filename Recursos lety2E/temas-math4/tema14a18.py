"""Math 4 · Temas 14 a 18 (sucesiones y series, notación sigma, límites, derivadas, sumas de Riemann).

Fuente: capturas. Sólo el tema 17 trae hoja de resueltos; en los demás van los ejemplos de las
hojas, los ejercicios SIN respuesta (regla: lo que no se puede verificar contra la fuente no se
resuelve por cuenta propia) y extras nuevos.
"""
from fractions import Fraction
from comun import g as G, CSS_COMUN, apuntes

B = lambda s: "\\boldsymbol{" + str(s) + "}"

def al(lineas, clase="sol"):
    return f'<div class="{clase}">$$\\begin{{aligned}} ' + " \\\\ ".join(lineas) + ' \\end{aligned}$$</div>'

def caja(titulo, cuerpo, nota=""):
    t = f'<div class="paso-titulo">{titulo}</div>\n' if titulo else ""
    n = f'<p class="enunciado nota">{nota}</p>\n' if nota else ""
    return f'<div class="ec-item">\n{t}{cuerpo}\n{n}</div>'

def card(titulo, enuns, clase="ej-line alta"):
    filas = "\n".join(f'          <div class="{clase}">${e}$</div>' for e in enuns)
    return (f'        <div class="mini-card">\n          <div class="mini-card-head">{titulo}</div>\n'
            f'          <div class="mini-card-body">\n{filas}\n          </div>\n        </div>')

def rejilla(cajas, cols=2):
    return f'        <div class="ec-grid c{cols}">\n' + "\n".join(cajas) + '\n        </div>'

CSS = CSS_COMUN + """
    .ec-grid { display: grid; grid-template-columns: 1fr 1fr; gap: .9rem; }
    .ec-grid.c3 { grid-template-columns: repeat(3, 1fr); }
    .ec-grid.c1 { grid-template-columns: 1fr; }
    @media (max-width: 900px) { .ec-grid.c3 { grid-template-columns: 1fr 1fr; } }
    @media (max-width: 620px) { .ec-grid, .ec-grid.c3 { grid-template-columns: 1fr; } }
    .ec-item { min-width: 0; border: 1px solid var(--border-s); border-radius: var(--r-md); padding: .8rem .6rem; text-align: center; }
    .ec-item .ej-line { text-align: center; }
    .ec-item .paso-titulo { margin: 0 0 .3rem; }
    .enunciado.nota { margin: .4rem 0 0; color: var(--text-3); font-size: .88rem; }
    .mini-card-body { text-align: center; }
    .mini-card-body .ej-line.alta, .ej-line.alta { line-height: 3.6; }
    .regla-unica .formula { margin: .5rem 0; line-height: 3; }
    .indet { color: var(--M); font-weight: 600; font-size: .85rem; margin: .1rem 0; }
    @media (max-width: 480px) { .sol .katex-display { font-size: .8em; } }
    @media (max-width: 380px) { .sol .katex-display { font-size: .7em; } }
"""

def fr(q):
    q = Fraction(q)
    return str(q.numerator) if q.denominator == 1 else ("-" if q < 0 else "") + f"\\dfrac{{{abs(q.numerator)}}}{{{q.denominator}}}"

# ══════════════════════════ TEMA 14 · Sucesiones y series ══════════════════════════
def suc(terminos):
    return ",\\ ".join(fr(t) for t in terminos) + ",\\ \\ldots"

EJ14 = [((2, 6, 10, 14), 5, 4), ((3, 9, 27, 81), 4, 5),
        ((Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 16)), 7, 6),
        ((5, 7, 9, 11), 6, 7), ((4, 9, 14, 19), 8, 5), ((3, 12, 48, 192), 10, 4)]
X14 = [((3, 7, 11, 15), 7, 5), ((2, 6, 18, 54), 5, 4), ((1, 6, 11, 16), 9, 4), ((5, 10, 20, 40), 7, 5),
       ((10, 7, 4, 1), 6, 5), ((1, 4, 16, 64), 6, 4), ((6, 8, 10, 12), 10, 6), ((2, 10, 50, 250), 5, 3),
       ((-5, -1, 3, 7), 8, 4),
       ((Fraction(1, 3), Fraction(1, 9), Fraction(1, 27), Fraction(1, 81)), 5, 4)]
for t, _, _ in EJ14 + X14:          # cada sucesión es aritmética o geométrica de verdad
    d = [b - a for a, b in zip(t, t[1:])]; r = [Fraction(b) / a for a, b in zip(t, t[1:])]
    assert len(set(d)) == 1 or len(set(r)) == 1, t
assert len({t for t, _, _ in EJ14 + X14} | {(2, 5, 8, 11), (4, 12, 36, 108)}) == len(EJ14 + X14) + 2

def fila14(t, k, s):
    return f'{suc(t)} \\qquad a_n,\\ a_{{{k}}},\\ S_{{{s}}}'

ap14 = apuntes([
    "<strong>Sucesión aritmética</strong>: cada término se obtiene sumando la misma <strong>diferencia</strong> $d$.",
    "$a_n = a_1 + d(n - 1) \\qquad S_n = \\dfrac{n(a_1 + a_n)}{2}$",
    "<strong>Sucesión geométrica</strong>: cada término se obtiene multiplicando por la misma <strong>razón</strong> $r$.",
    "$a_n = a_1 r^{\\,n-1} \\qquad S_n = a_1\\left(\\dfrac{r^n - 1}{r - 1}\\right)$",
]).replace("<p>$", '<p class="formula">$')
ej14 = G.seccion_ejemplo(rejilla([
    caja("Sucesión aritmética",
         '<div class="ej-line">$2,\\ 5,\\ 8,\\ 11,\\ \\ldots$</div>\n<p class="enunciado nota">Diferencia igual a 3</p>\n'
         '<div class="paso-titulo">Término general</div>\n' + al(["a_n &= 2 + 3(n - 1)", "a_n &= 2 + 3n - 3", f"a_n &= {B('3n - 1')}"])
         + '\n<div class="paso-titulo">Encuentra el término a₆</div>\n' + al(["a_6 &= 3(6) - 1", "a_6 &= 18 - 1", f"a_6 &= {B(17)}"])
         + '\n<div class="paso-titulo">Suma de n términos</div>\n'
         + al(["S_4 &= \\dfrac{4(2 + 11)}{2}", "&= \\dfrac{4(13)}{2} = \\dfrac{52}{2}", f"&= {B(26)}"])),
    caja("Sucesión geométrica",
         '<div class="ej-line">$4,\\ 12,\\ 36,\\ 108,\\ \\ldots$</div>\n<p class="enunciado nota">Razón igual a 3</p>\n'
         '<div class="paso-titulo">Término general</div>\n' + al([f"a_n &= {B('4(3)^{n-1}')}"])
         + '\n<div class="paso-titulo">Encuentra el término a₆</div>\n'
         + al(["a_6 &= 4(3)^{6-1}", "a_6 &= 4(3)^5", "a_6 &= 4(243)", f"a_6 &= {B(972)}"])
         + '\n<div class="paso-titulo">Suma de n términos</div>\n'
         + al(["S_4 &= 4\\left(\\dfrac{3^4 - 1}{3 - 1}\\right)", "&= 4\\left(\\dfrac{80}{2}\\right)", f"&= {B(160)}"])),
]), titulo="Ejemplos")
assert 3 * 6 - 1 == 17 and 4 * 3 ** 5 == 972 and 4 * (2 + 11) // 2 == 26 and 4 * (3 ** 4 - 1) // 2 == 160
PIDE14 = "De cada sucesión encuentra el término general $a_n$, el término y la suma que se indican."
G.pagina("sucesiones-series", 14, "Sucesiones y series",
         "Sucesiones aritméticas y geométricas: término general, término n-ésimo y suma de n términos.",
         [ap14, ej14,
          G.seccion("Ejercicios", "ejercicios", f'      <p class="enunciado">{PIDE14}</p>\n'
                    + G.grid([card("Bloque 1", [fila14(*e) for e in EJ14[:3]]), card("Bloque 2", [fila14(*e) for e in EJ14[3:]])], 2)),
          G.seccion("Ejercicios extra", "extra", f'      <p class="enunciado">{PIDE14}</p>\n'
                    + G.grid([card("Bloque 1", [fila14(*e) for e in X14[:5]]), card("Bloque 2", [fila14(*e) for e in X14[5:]])], 2),
                    colapsable=True)],
         prev=("transformacion-funciones.html", "Transformación de funciones"),
         sig=("notacion-sigma.html", "Notación sigma"), css_extra=CSS)
print("ok tema 14")

# ══════════════════════════ TEMA 15 · Notación sigma ══════════════════════════
S = lambda cuerpo, a, b, v="i": f"\\displaystyle\\sum_{{{v}={a}}}^{{{b}}} {cuerpo}"
INF = "\\infty"
P = lambda a, b: f"\\left(\\dfrac{{{a}}}{{{b}}}\\right)^n"
assert sum(3 * i for i in range(1, 6)) == 45 and sum(i * i for i in range(2, 7)) == 90
assert sum(Fraction(5 - i, 2) for i in range(3, 7)) == 1            # la hoja dice 1/2
assert sum(4 * i for i in range(1, 13)) == 312 and sum(5 * i * i for i in range(1, 11)) == 1925
assert sum(4 * i * i - 3 * i + 2 for i in range(1, 11)) == 1395      # la hoja dice 1390

ap15 = apuntes([
    "$\\displaystyle\\sum_{i=1}^{n} a_i = a_1 + a_2 + \\ldots + a_n$",
    "<strong>Con fórmulas</strong>",
    "$\\displaystyle\\sum_{i=1}^{n} c\\,a_i = c\\sum_{i=1}^{n} a_i \\qquad \\sum_{i=1}^{n} (a_i + b_i) = \\sum_{i=1}^{n} a_i + \\sum_{i=1}^{n} b_i$",
    "$\\displaystyle\\sum_{i=1}^{n} 1 = n \\qquad \\sum_{i=1}^{n} i = \\dfrac{n(n+1)}{2} \\qquad \\sum_{i=1}^{n} i^2 = \\dfrac{n(n+1)(2n+1)}{6}$",
    "<strong>Series</strong>: en $\\displaystyle\\sum_{n=1}^{\\infty} r^n$, si $r \\ge 1$ la serie es <strong>divergente</strong>; "
    "si $r < 1$ es <strong>convergente</strong> y existe la suma infinita $S_\\infty$.",
    "$S_\\infty = \\displaystyle\\sum_{n=1}^{\\infty} r^n = \\dfrac{a_1}{1 - r}$",
]).replace("<p>$", '<p class="formula">$').replace("<p><strong>Series", '<p class="formula"><strong>Series')
ej15a = G.seccion_ejemplo(rejilla([
    caja("", al([f"{S('3i', 1, 5)} &= 3(1) + 3(2) + 3(3) + 3(4) + 3(5)", "&= 3 + 6 + 9 + 12 + 15", f"&= {B(45)}"])),
    caja("", al([f"{S('i^2', 2, 6)} &= (2)^2 + (3)^2 + (4)^2 + (5)^2 + (6)^2", "&= 4 + 9 + 16 + 25 + 36", f"&= {B(90)}"])),
    caja("", al([S('\\dfrac{5 - i}{2}', 3, 6) + " &= \\dfrac{5 - 3}{2} + \\dfrac{5 - 4}{2} + \\dfrac{5 - 5}{2} + \\dfrac{5 - 6}{2}",
                 "&= \\dfrac{2}{2} + \\dfrac{1}{2} - \\dfrac{1}{2}", f"&= {B(1)}"])),
], 1), titulo="Ejemplos · Desarrollando la suma")
ej15b = G.seccion_ejemplo(rejilla([
    caja("", al([S('4i', 1, 12) + " &= 4" + S('i', 1, 12), "&= 4\\left(\\dfrac{12(13)}{2}\\right)", "&= 2(12)(13)", f"&= {B(312)}"])),
    caja("", al([S('5i^2', 1, 10) + " &= 5" + S('i^2', 1, 10), "&= 5\\left(\\dfrac{10(11)(21)}{6}\\right)", "&= 5^2(7)(11)", f"&= {B(1925)}"])),
    caja("", al([S('(4i^2 - 3i + 2)', 1, 10) + " &= 4" + S('i^2', 1, 10) + " - 3" + S('i', 1, 10) + " + 2" + S('1', 1, 10),
                 "&= 4\\left[\\dfrac{10(11)(21)}{6}\\right] - 3\\left[\\dfrac{10(11)}{2}\\right] + 2(10)",
                 "&= 2[10(11)(7)] - 3(5)(11) + 20", "&= 1540 - 165 + 20", f"&= {B(1395)}"])),
], 1), titulo="Ejemplos · Con fórmulas")
ej15c = G.seccion_ejemplo(
    '        <p class="enunciado">Si la serie converge, encuentra la suma infinita $S_\\infty$.</p>\n' + rejilla([
    caja("", ('<div class="ej-line alta">$' + S(P(1, 2), 1, INF, "n") + '$</div>')
         + '\n<p class="enunciado nota">Vemos que $r = \\frac{1}{2} < 1$: es convergente.</p>\n'
         + al(["S_\\infty &= \\dfrac{\\frac{1}{2}}{1 - \\frac{1}{2}}", "&= \\dfrac{\\frac{1}{2}}{\\frac{2}{2} - \\frac{1}{2}}", f"&= {B(1)}"])),
    caja("", ('<div class="ej-line alta">$' + S(P(4, 2), 1, INF, "n") + '$</div>')
         + '\n<p class="enunciado nota">Vemos que $r = 2 > 1$: es <strong>divergente</strong>.</p>'),
    caja("", al([S('\\left(\\dfrac{3}{2^n}\\right)', 1, INF, 'n') + " &= 3" + S('\\left(\\dfrac{1}{2^n}\\right)', 1, INF, 'n'),
                 "&= 3\\left[" + S('\\left(\\dfrac{1}{2}\\right)^n', 1, INF, 'n') + "\\right]", "&= 3(1)", f"&= {B(3)}"])
         + '\n<p class="enunciado nota">Convergente.</p>'),
], 3), titulo="Ejemplos · Series")
EJ15_S = [S('\\dfrac{4 - i}{3}', 2, 5), S('\\dfrac{8 - i}{5}', 1, 6), S('3i', 1, 10), S('7i', 1, 8), S('8i^2', 1, 10), S('5i^2', 1, 12),
          S('(5i^2 - 7i + 4)', 1, 8), S('(2i^2 - 3i + 5)', 1, 8)]
EJ15_R = [S(P(1, 4), 1, INF, 'n'), S(P(1, 5), 1, INF, 'n'), S('\\left(\\dfrac{1}{3^n}\\right)', 1, INF, 'n'),
          S(P(3, 2), 1, INF, 'n'), S(P(5, 3), 1, INF, 'n'), S(P(2, 3), 1, INF, 'n')]
X15_S = [S('\\dfrac{6 - i}{4}', 1, 5), S('\\dfrac{i + 2}{3}', 2, 6), S('5i', 1, 9), S('9i', 1, 12), S('2i^2', 1, 6), S('3i^2', 1, 9),
         S('(3i^2 - 2i + 6)', 1, 6), S('(i^2 + 4i - 3)', 1, 10)]
X15_R = [S(P(1, 6), 1, INF, 'n'), S(P(3, 4), 1, INF, 'n'), S('\\left(\\dfrac{5}{2^n}\\right)', 1, INF, 'n'),
         S(P(7, 4), 1, INF, 'n'), S(P(2, 5), 1, INF, 'n'), S(P(9, 8), 1, INF, 'n')]
assert not (set(EJ15_S + EJ15_R) & set(X15_S + X15_R))
def sec15(titulo, icono, s, r, colapsable=False):
    return G.seccion(titulo, icono, G.grid([card("Bloque 1 · Calcula la suma", s),
                                             card("Bloque 2 · Si la serie converge, encuentra S∞", r)], 2), colapsable=colapsable)
G.pagina("notacion-sigma", 15, "Notación sigma",
         "Notación sigma: sumas desarrolladas, sumas con fórmulas y series geométricas convergentes y divergentes.",
         [ap15, ej15a, ej15b, ej15c, sec15("Ejercicios", "ejercicios", EJ15_S, EJ15_R),
          sec15("Ejercicios extra", "extra", X15_S, X15_R, True)],
         prev=("sucesiones-series.html", "Sucesiones y series"), sig=("limites.html", "Límites"), css_extra=CSS)
print("ok tema 15")

# ══════════════════════════ TEMA 16 · Límites ══════════════════════════
lim = lambda a, cuerpo: f"\\displaystyle\\lim_{{x \\to {a}}} {cuerpo}"
F = lambda a, b: f"\\dfrac{{{a}}}{{{b}}}"
IND = '<p class="indet">Indeterminación</p>\n'
ej16 = G.seccion_ejemplo(rejilla([
    caja("Sustitución directa", al([lim(4, F("x - 1", "x^2 - 1")) + " &= " + F("4 - 1", "16 - 1"), f"&= {F(3, 15)} = {B(F(1, 5))}"])),
    caja("Sustitución directa", al([lim(1, F("x^2 - 2x - 15", "x^2 - 3x - 10")) + " &= " + F("(1)^2 - 2(1) - 15", "(1)^2 - 3(1) - 10"),
                                     "&= " + F("1 - 2 - 15", "1 - 3 - 10") + " = " + F("1 - 17", "1 - 13"),
                                     "&= " + F(-16, -12) + " = " + B(F(4, 3))])),
    caja("Factorizando", al([lim(1, F("x - 1", "x^2 - 1")) + " &= " + F("1 - 1", "(1)^2 - 1") + " = " + F(0, 0)]) + "\n" + IND
         + al([lim(1, F("x - 1", "x^2 - 1")) + " &= " + lim(1, F("x - 1", "(x + 1)(x - 1)")), "&= " + lim(1, F(1, "x + 1")), "&= " + B(F(1, 2))]),
         "Para poder calcularlo, se factoriza."),
    caja("Factorizando", al([lim(5, F("x^2 - 2x - 15", "x^2 - 3x - 10")) + " &= " + F("(5)^2 - 2(5) - 15", "(5)^2 - 3(5) - 10"),
                              "&= " + F("25 - 10 - 15", "25 - 15 - 10") + " = " + F(0, 0)]) + "\n" + IND
         + al([lim(5, F("x^2 - 2x - 15", "x^2 - 3x - 10")) + " &= " + lim(5, F("(x - 5)(x + 3)", "(x - 5)(x + 2)")),
               "&= " + lim(5, F("x + 3", "x + 2")), "&= " + F("5 + 3", "5 + 2") + " = " + B(F(8, 7))]),
         "Para poder calcularlo, se factoriza."),
    caja("Racionalizando", al([lim(0, F("x", "1 - \\sqrt{1 - x}")) + " &= " + F(0, 0)]) + "\n" + IND
         + al([lim(0, F("x", "1 - \\sqrt{1 - x}")) + "\\left(" + F("1 + \\sqrt{1 - x}", "1 + \\sqrt{1 - x}") + "\\right) &= "
               + lim(0, F("x(1 + \\sqrt{1 - x})", "(1)^2 - (\\sqrt{1 - x})^2")),
               "&= " + lim(0, F("x(1 + \\sqrt{1 - x})", "1 - (1 - x)")), "&= " + lim(0, F("x(1 + \\sqrt{1 - x})", "x")),
               "&= " + lim(0, "1 + \\sqrt{1 - x}"), "&= 1 + \\sqrt{1 - 0} = " + B(2)]),
         "Para poder calcularlo, se racionalizan los radicales: se multiplica por 1, escrito con el conjugado."),
    caja("Al infinito", al([lim(INF, F("-3x^4 - 5x + 2", "2x^4 + 1")) + " &= " + F("-\\infty", "\\infty")]) + "\n" + IND
         + al([lim(INF, "\\left(" + F("\\frac{1}{x^4}", "\\frac{1}{x^4}") + "\\right)\\left(" + F("-3x^4 - 5x + 2", "2x^4 + 1") + "\\right)") + " &= "
                   + lim(INF, F("-\\frac{3x^4}{x^4} - \\frac{5x}{x^4} + \\frac{2}{x^4}", "\\frac{2x^4}{x^4} + \\frac{1}{x^4}")),
               "&= " + B("-\\dfrac{3}{2}")]),
         "Para poder calcularlo, se multiplica por 1, escrito con la $x$ de mayor exponente. Los términos que quedan con $x$ en el denominador se van a 0."),
], 1), titulo="Ejemplos")
EJ16 = [lim(-5, F("x + 5", "x^2 - 25")), lim(3, F("x + 5", "x^2 - 25")), lim(-3, F("x + 3", "x^2 - 9")), lim(2, F("x - 2", "x^2 - 4")),
        lim(-2, F("x^2 + x - 12", "x^2 + 5x + 4")), lim(-4, F("x^2 + x - 12", "x^2 + 5x + 4")),
        lim(2, F("x^2 + x - 6", "x^2 + 4x - 12")), lim(1, F("x^2 + x - 6", "x^2 + 4x - 12")),
        lim(4, F("x - 4", "\\sqrt{x - 4}")), lim(0, F("x", "\\sqrt{3 - x} - \\sqrt{3}")),
        lim(3, F("x - 3", "\\sqrt{x - 3}")), lim(0, F("2x", "\\sqrt{5} + \\sqrt{x + 5}")),
        lim(INF, F("-4x^3 - 4x + 2", "2x^3 + x - 7")), lim(0, F("x", "\\sqrt{25 + x} - 5")),
        lim(INF, F("2x^5 - 6x + 4", "3x^5 - 3x^2 - 1")), lim(INF, F("x^4 - 8x^3 - 6", "5x^4 - 4x^2 - x"))]
X16 = [lim(-4, F("x + 4", "x^2 - 16")), lim(2, F("x + 4", "x^2 - 16")), lim(6, F("x - 6", "x^2 - 36")), lim(3, F("x^2 - x - 6", "x^2 - 2x - 3")),
       lim(1, F("x^2 - x - 6", "x^2 - 2x - 3")), lim(-1, F("x^2 - 4x - 5", "x^2 + 3x + 2")),
       lim(7, F("x - 7", "\\sqrt{x - 7}")), lim(0, F("x", "\\sqrt{4 + x} - 2")), lim(0, F("x", "3 - \\sqrt{9 - x}")),
       lim(INF, F("6x^2 - x + 3", "2x^2 + 5")), lim(INF, F("-x^3 + 4x^2 - 1", "4x^3 - 2x")), lim(INF, F("5x^6 - 2x^3 + x", "10x^6 + 7"))]
assert not (set(EJ16) & set(X16))
G.pagina("limites", 16, "Límites",
         "Límites: sustitución directa, indeterminaciones que se resuelven factorizando o racionalizando, y límites al infinito.",
         [ej16,
          G.seccion("Ejercicios", "ejercicios", '      <p class="enunciado">Calcula los siguientes límites.</p>\n'
                    + G.grid([card("Bloque 1", EJ16[0::2]), card("Bloque 2", EJ16[1::2])], 2)),
          G.seccion("Ejercicios extra", "extra", '      <p class="enunciado">Calcula los siguientes límites.</p>\n'
                    + G.grid([card("Bloque 1", X16[:6]), card("Bloque 2", X16[6:])], 2), colapsable=True)],
         prev=("notacion-sigma.html", "Notación sigma"), sig=("derivadas.html", "Derivadas"), css_extra=CSS)
print("ok tema 16")

# ══════════════════════════ TEMA 17 · Derivadas ══════════════════════════
limh = lambda cuerpo: f"\\displaystyle\\lim_{{h \\to 0}} {cuerpo}"
def sg(v, primero=False, cuerpo=""):
    """±|v|cuerpo, omitiendo el 1 delante de letras."""
    a = abs(v); c = "" if (a == 1 and cuerpo) else str(a)
    if primero:
        return ("-" if v < 0 else "") + c + cuerpo
    return (" - " if v < 0 else " + ") + c + cuerpo

def poli(a, b, c):
    s, primero = "", True
    for v, cu in ((a, "x^2"), (b, "x"), (c, "")):
        if v:
            s += sg(v, primero, cu); primero = False
    return s

def derivada(a, b, c):
    """f(x) = ax² + bx + c por la definición. → (enunciado f, f(x+h), renglones, f')"""
    f = poli(a, b, c)
    fh, primero = "", True
    if a:
        fh += sg(a, True, "(x + h)^2"); primero = False
    if b:
        fh += sg(b, primero, "(x + h)"); primero = False
    if c:
        fh += sg(c, primero)
    menos_f = f"({f})" if (f.startswith("-") or sum(1 for v in (a, b, c) if v) > 1) else f
    l = [f"f'(x) &= " + limh(F(f"{fh} - {menos_f}", "h"))]
    if a == 0:                                    # lineal
        exp = sg(b, True, "x") + sg(b, False, "h") + (sg(c) if c else "") + sg(-b, False, "x") + (sg(-c) if c else "")
        l += ["&= " + limh(F(exp, "h")), "&= " + limh(F(sg(b, True, "h"), "h")), f"&= {B(b)}"]
        return f, fh, l, str(b)
    if b == 0 and c == 0:                         # ax²
        l += ["&= " + limh(F(sg(a, True, "(x^2 + 2xh + h^2)") + f" - {menos_f}", "h")),
              "&= " + limh(F(sg(a, True, "x^2") + sg(2 * a, False, "xh") + sg(a, False, "h^2") + sg(-a, False, "x^2"), "h")),
              "&= " + limh(F("h(" + sg(2 * a, True, "x") + sg(a, False, "h") + ")", "h")),
              "&= " + sg(2 * a, True, "x") + sg(a, False, "(0)"), f"&= {B(sg(2 * a, True, 'x'))}"]
        return f, fh, l, sg(2 * a, True, "x")
    assert a == 1                                 # x² + bx + c
    exp = "x^2 + 2xh + h^2" + (sg(b, False, "x") + sg(b, False, "h") if b else "") + (sg(c) if c else "") \
          + " - x^2" + (sg(-b, False, "x") if b else "") + (sg(-c) if c else "")
    der = "2x" + (sg(b) if b else "")
    l += ["&= " + limh(F(exp, "h")), "&= " + limh(F("2xh + h^2" + (sg(b, False, "h") if b else ""), "h")),
          "&= " + limh(F("h(2x + h" + (sg(b) if b else "") + ")", "h")),
          "&= 2x + 0" + (sg(b) if b else ""), f"&= {B(der)}"]
    return f, fh, l, der

def res17(abc):
    f, fh, l, _ = derivada(*abc)
    return caja("", f'<div class="ej-line">$f(x) = {f} \\qquad f(x + h) = {fh}$</div>\n' + al(l))

EJ17 = [(0, 4, 2), (0, 6, -5), (3, 0, 0), (-5, 0, 0), (1, -3, -2), (1, -1, 5)]
assert [derivada(*e)[3] for e in EJ17] == ["4", "6", "6x", "-10x", "2x - 3", "2x - 1"]        # hoja de resueltos
EJEMPLOS17 = [(0, 2, 3), (4, 0, 0), (1, 5, -4)]                                                # nuevos, mismos pasos
X17 = [(0, 3, -7), (0, -2, 9), (0, 5, 1), (0, -1, 4), (2, 0, 0), (-4, 0, 0), (7, 0, 0), (6, 0, 0),
       (1, 4, -1), (1, -6, 3), (1, 1, -8), (1, -2, 0)]
assert len(set(EJ17 + EJEMPLOS17 + X17)) == len(EJ17 + EJEMPLOS17 + X17)
ap17 = apuntes([
    "La <strong>derivada</strong> de una función se obtiene con el límite:",
    "$f'(x) = \\displaystyle\\lim_{h \\to 0} \\dfrac{f(x + h) - f(x)}{h}$",
    "Primero se escribe $f(x + h)$, se sustituye en el límite, se desarrolla y se simplifica hasta poder cancelar la $h$ del denominador.",
]).replace("<p>$", '<p class="formula">$')
PIDE17 = "Encuentra la derivada de cada función con la definición."
G.pagina("derivadas", 17, "Derivadas",
         "Derivadas por definición: el límite del cociente de diferencias, con ejercicios resueltos paso a paso.",
         [ap17, G.seccion_ejemplo(f'        <p class="enunciado">{PIDE17}</p>\n' + rejilla([res17(e) for e in EJEMPLOS17], 1), titulo="Ejemplos"),
          G.seccion("Ejercicios", "ejercicios", f'      <p class="enunciado">{PIDE17}</p>\n'
                    + G.grid([card("Bloque 1", [f"f(x) = {poli(*e)}" for e in EJ17[:3]], "ej-line"),
                              card("Bloque 2", [f"f(x) = {poli(*e)}" for e in EJ17[3:]], "ej-line")], 2)),
          G.seccion("Respuestas", "respuestas", G.resol_grid([
              f'          <div class="resol-item">\n            <div class="resol-num">Bloque {i + 1}</div>\n'
              + rejilla([res17(e) for e in blo], 1) + '\n          </div>' for i, blo in enumerate((EJ17[:3], EJ17[3:]))]), colapsable=True),
          G.seccion("Ejercicios extra", "extra", f'      <p class="enunciado">{PIDE17}</p>\n'
                    + G.grid([card("Bloque 1", [f"f(x) = {poli(*e)}" for e in X17[:6]], "ej-line"),
                              card("Bloque 2", [f"f(x) = {poli(*e)}" for e in X17[6:]], "ej-line")], 2), colapsable=True)],
         prev=("limites.html", "Límites"), sig=("sumas-riemann.html", "Sumas de Riemann"), css_extra=CSS)
print("ok tema 17")

# ══════════════════════════ TEMA 18 · Sumas de Riemann ══════════════════════════
I = lambda a, b, f: f"\\displaystyle\\int_{{{a}}}^{{{b}}} ({f})\\,dx"
Sn = lambda cuerpo: f"\\displaystyle\\sum_{{i=1}}^{{n}} {cuerpo}"
assert Fraction(125, 3) - 50 + 40 == Fraction(95, 3) and Fraction(125, 2) - Fraction(100, 2) == Fraction(25, 2)
assert (Fraction(27, 3) + 12) - (Fraction(-8, 3) - 8) == Fraction(95, 3)
ap18 = apuntes([
    "$\\displaystyle\\int_a^b f(x)\\,dx = \\lim_{n \\to \\infty} \\sum_{i=1}^{n} f(x_i)\\,\\Delta x$",
    "$\\Delta x = \\dfrac{b - a}{n} \\qquad x_i = a + \\Delta x\\, i$",
    "$\\displaystyle\\sum_{i=1}^{n} i^2 = \\dfrac{n^3}{3} + \\dfrac{n^2}{2} + \\dfrac{n}{6} \\qquad \\sum_{i=1}^{n} i = \\dfrac{n^2}{2} + \\dfrac{n}{2} \\qquad \\sum_{i=1}^{n} 1 = n$",
]).replace("<p>$", '<p class="formula">$')
ej18 = G.seccion_ejemplo(
    f'        <div class="ej-line alta">${I(-2, 3, "x^2 + 4")}$</div>\n' + rejilla([
    caja("1 · Δx y xᵢ", al(["\\Delta x &= \\dfrac{3 - (-2)}{n} = \\dfrac{5}{n}", "x_i &= -2 + \\dfrac{5}{n}\\,i"])),
    caja("2 · f(xᵢ)", al(["f(x_i) &= \\left(-2 + \\dfrac{5}{n}\\,i\\right)^2 + 4", "&= 4 - \\dfrac{20}{n}\\,i + \\dfrac{25}{n^2}\\,i^2 + 4",
                          "&= \\dfrac{25}{n^2}\\,i^2 - \\dfrac{20}{n}\\,i + 8"])),
    caja("3 · f(xᵢ)Δx", al(["f(x_i)\\,\\Delta x &= \\left(\\dfrac{25}{n^2}\\,i^2 - \\dfrac{20}{n}\\,i + 8\\right)\\dfrac{5}{n}",
                            "&= \\dfrac{125}{n^3}\\,i^2 - \\dfrac{100}{n^2}\\,i + \\dfrac{40}{n}"])),
    caja("4 · La suma", al([Sn("f(x_i)\\,\\Delta x") + " &= " + Sn("\\left(\\dfrac{125}{n^3}\\,i^2 - \\dfrac{100}{n^2}\\,i + \\dfrac{40}{n}\\right)"),
                            "&= \\dfrac{125}{n^3}" + Sn("i^2") + " - \\dfrac{100}{n^2}" + Sn("i") + " + \\dfrac{40}{n}" + Sn("1"),
                            "&= \\dfrac{125}{n^3}\\left(\\dfrac{n^3}{3} + \\dfrac{n^2}{2} + \\dfrac{n}{6}\\right) - \\dfrac{100}{n^2}\\left(\\dfrac{n^2}{2} + \\dfrac{n}{2}\\right) + \\dfrac{40}{n}(n)",
                            "&= \\dfrac{125}{3} + \\dfrac{125}{2n} + \\dfrac{125}{6n^2} - \\dfrac{100}{2} - \\dfrac{100}{2n} + 40",
                            "&= \\dfrac{125}{3} - 10 + \\dfrac{125}{6n^2} + \\dfrac{25}{2n}"])),
    caja("5 · El límite", al(["\\displaystyle\\lim_{n \\to \\infty} " + Sn("f(x_i)\\,\\Delta x") + " &= \\displaystyle\\lim_{n \\to \\infty}\\left(\\dfrac{95}{3} + \\dfrac{125}{6n^2} + \\dfrac{25}{2n}\\right)",
                              "&= " + B("\\dfrac{95}{3}")]),
         "Los términos con $n$ en el denominador se van a 0."),
], 1), titulo="Ejemplo")
EJ18 = [I(-1, 4, "x^2 + 5"), I(2, 6, "3 - x^2"), I(5, 8, "4 + 3x^2"), I(-2, 5, "x^2 - 6")]
X18 = [I(0, 3, "x^2 + 2"), I(1, 4, "x^2 + 1"), I(-1, 2, "x^2 + 3"), I(0, 2, "5 - x^2"), I(2, 5, "2x^2 + 1"),
       I(-3, 1, "x^2 - 2"), I(1, 3, "6 + x^2"), I(0, 4, "x^2 - 5"), I(-2, 2, "2 + 3x^2"), I(3, 6, "x^2 - 4")]
assert not (set(EJ18) & set(X18))
PIDE18 = "Calcula cada integral con sumas de Riemann."
G.pagina("sumas-riemann", 18, "Sumas de Riemann",
         "Sumas de Riemann: la integral definida como límite de una suma, con un ejemplo resuelto paso a paso.",
         [ap18, ej18,
          G.seccion("Ejercicios", "ejercicios", f'      <p class="enunciado">{PIDE18}</p>\n'
                    + G.grid([card("Bloque 1", EJ18[:2]), card("Bloque 2", EJ18[2:])], 2)),
          G.seccion("Ejercicios extra", "extra", f'      <p class="enunciado">{PIDE18}</p>\n'
                    + G.grid([card("Bloque 1", X18[:5]), card("Bloque 2", X18[5:])], 2), colapsable=True)],
         prev=("derivadas.html", "Derivadas"), sig=None, css_extra=CSS)
print("ok tema 18")
