"""Math 4 · Tema 5 · Función inversa (regla de correspondencia).

Fuente: el ejemplo de letymath.com/matemáticas-4/función-inversa (Lety lo pasó el 9-nov-2026) y la
hoja de ejercicios de las capturas. El ejemplo de la página es el segundo conjunto de la hoja, así
que aquí va sólo como ejemplo. No hay hoja de resueltos: los ejercicios van sin respuesta.
"""
from fractions import Fraction
from comun import g as G, cargar, CSS_COMUN, apuntes
graf = cargar("funciones-svg-math").grafica
MOR = "#7B2CBF"

def conj(pares):
    return "\\{" + ",\\,".join(f"({x},\\,{y})" for x, y in pares) + "\\}"

def lista(v):
    return "\\{" + ",\\,".join(map(str, v)) + "\\}"

def recta(pares):
    (x1, y1), (x2, y2) = pares[0], pares[1]
    m = Fraction(y2 - y1, x2 - x1); b = y1 - m * x1
    assert m.denominator == 1 and b.denominator == 1 and m != 0
    assert all(y == m * x + b for x, y in pares), pares
    return int(m), int(b)

def sg(v, cuerpo=""):
    a = abs(v); c = "" if (a == 1 and cuerpo) else str(a)
    return (" - " if v < 0 else " + ") + c + cuerpo

def al(l):
    return '<div class="sol">$$\\begin{aligned} ' + " \\\\ ".join(l) + ' \\end{aligned}$$</div>'

def dato(et, tex):
    return f'<div class="dato"><span class="et">{et}</span>${tex}$</div>'

EJEMPLO = [(0, -2), (1, 3), (-1, -7), (2, 8)]
EJERCICIOS = [[(0, 4), (1, 2), (-1, 6), (3, -2)], [(0, -3), (1, 2), (-1, -8), (2, 7)],
              [(0, -5), (1, -1), (-1, -9), (2, 3)], [(0, 2), (1, -1), (2, -4), (-1, 5)]]
EXTRAS = [[(0, 1), (1, 3), (-1, -1), (2, 5)], [(0, -4), (1, -1), (-1, -7), (2, 2)], [(0, 3), (1, -1), (-1, 7), (2, -5)],
          [(0, 6), (1, 4), (-1, 8), (3, 0)], [(0, -1), (1, 4), (-1, -6), (2, 9)], [(0, 5), (1, 2), (2, -1), (-1, 8)],
          [(0, -6), (1, -2), (-1, -10), (2, 2)], [(0, 2), (1, 4), (-2, -2), (3, 8)], [(0, -3), (1, -5), (-1, -1), (2, -7)],
          [(0, 4), (1, 7), (-1, 1), (-2, -2)]]
todos = [EJEMPLO] + EJERCICIOS + EXTRAS
for t in todos:
    recta(t)
assert len({tuple(t) for t in todos}) == len(todos) and len({recta(t) for t in todos}) == len(todos)

# ── el ejemplo, con los pasos de la página de Lety ──
m, b = recta(EJEMPLO)
assert (m, b) == (5, -2)
inv = [(y, x) for x, y in EJEMPLO]
regla = f"{b}{sg(m, 'x')}"                                   # -2 + 5x
finv = lambda x: Fraction(b - x, -m)                          # (-2 - x)/(-5)
assert all(finv(y) == x for x, y in EJEMPLO)
xs = [p[0] for p in EJEMPLO]; ys = [p[1] for p in EJEMPLO]

def comprueba(v):
    num = b - v
    l = [f"f^{{-1}}({v}) &= \\dfrac{{{b} - ({v})}}{{{-m}}}"]
    if v < 0:
        l.append(f"&= \\dfrac{{{b}{sg(-v)}}}{{{-m}}}")
    l.append(f"&= \\dfrac{{{num}}}{{{-m}}}")
    l.append(f"f^{{-1}}({v}) &= \\boldsymbol{{{finv(v)}}}")
    return f'<div><p class="ej-sub">para x = {v}</p>{al(l)}</div>'

g1 = graf([(lambda x: m * x + b, min(xs), max(xs))], puntos=EJEMPLO, etiqueta="Gráfica de f(x)")
lo, hi = min(xs + ys) - 1, max(xs + ys) + 1
g2 = graf([(lambda x: m * x + b, min(xs), max(xs)), (lambda x: (b - x) / -m, min(ys), max(ys))],
          puntos=EJEMPLO + inv, ventana=(lo, hi, lo, hi), punteadas=[("d", 0)], segundo_color=MOR,
          etiqueta="Gráfica de f(x), su inversa y la recta y = x")

DESPEJE = al([f"y &= {regla}", f"x &= {b}{sg(m, 'y')}", f"{-m}y &= {b} - x", "y &= \\dfrac{%d - x}{%d}" % (b, -m)])
REGLA_INV = dato("regla de la inversa", "f^{-1}(x) = \\boldsymbol{\\dfrac{%d - x}{%d}}" % (b, -m))
ejemplo = G.seccion_ejemplo(
    f'        <div class="ej-line">$f(x) = {conj(EJEMPLO)}$</div>\n'
    '        <div class="dos-col">\n'
    '          <div>\n            <div class="paso-titulo">Función directa</div>\n'
    f'            {dato("regla de correspondencia", f"f(x) = {regla}")}\n'
    f'            {dato("dominio", lista(xs))}\n            {dato("rango", lista(ys))}\n'
    f'            <div class="graf-wrap">{g1}</div>\n          </div>\n'
    '          <div>\n            <div class="paso-titulo">Cálculo de la inversa</div>\n'
    '            <p class="enunciado nota">Se intercambian $x$ y $y$, y se despeja $y$.</p>\n'
    f'            {DESPEJE}\n'
    f'            {REGLA_INV}\n'
    f'            {dato("dominio de la inversa", lista(ys))}\n            {dato("rango de la inversa", lista(xs))}\n'
    '          </div>\n        </div>\n'
    f'        <div class="ej-line">$f^{{-1}}(x) = {conj(inv)}$</div>\n'
    '        <div class="paso-titulo">Comprobar dos puntos</div>\n'
    f'        <div class="dos-col">{comprueba(ys[0])}{comprueba(ys[1])}</div>\n'
    '        <div class="paso-titulo">Graficar f(x), f⁻¹(x) y y = x</div>\n'
    f'        <div class="graf-wrap grande">{g2}</div>\n'
    '        <p class="leyenda"><span class="c-f">f(x)</span> · <span class="c-inv">f⁻¹(x)</span> · punteada: y = x</p>\n'
    '        <p class="enunciado nota">Observa la simetría de los puntos y las rectas respecto a la línea punteada $y = x$.</p>')

PIDE = ("De cada función encuentra la regla de correspondencia, el dominio y el rango; calcula su inversa con su "
        "dominio y su rango, comprueba dos puntos y grafica $f(x)$, $f^{-1}(x)$ y $y = x$.")
def card(titulo, conjuntos):
    filas = "\n".join(f'          <div class="ej-line">$f(x) = {conj(c)}$</div>' for c in conjuntos)
    return (f'        <div class="mini-card">\n          <div class="mini-card-head">{titulo}</div>\n'
            f'          <div class="mini-card-body">\n{filas}\n          </div>\n        </div>')

ap = apuntes([
    "La <strong>función inversa</strong> $f^{-1}(x)$ deshace lo que hace $f(x)$: cada pareja $(x,\\,y)$ se convierte en $(y,\\,x)$.",
    "Por eso el dominio de la inversa es el rango de la función, y su rango es el dominio de la función.",
])
CSS = CSS_COMUN + """
    .ej-sub { font-size: .72rem; font-weight: 700; text-transform: uppercase; letter-spacing: .06em;
              color: var(--text-3); margin: 0 0 .2rem; text-align: center; }
    .ejemplo-block > .ej-line { text-align: center; }
    .dos-col { display: grid; grid-template-columns: 1fr 1fr; gap: .6rem 1.5rem; align-items: start; }
    @media (max-width: 620px) { .dos-col { grid-template-columns: 1fr; } }
    .paso-titulo { margin: 1.3rem 0 .3rem; text-align: center; }
    .enunciado.nota { margin: .3rem 0; color: var(--text-3); font-size: .88rem; }
    .graf-wrap { margin: .6rem 0; }
    .graf-wrap.grande .graf-svg { max-width: 100%; width: 340px; max-height: none; }
    .leyenda { text-align: center; font-size: .85rem; color: var(--text-3); margin: 0; }
    .leyenda .c-f { color: var(--M); font-weight: 700; }
    .leyenda .c-inv { color: #7B2CBF; font-weight: 700; }
    .dato { font-size: .95rem; color: var(--text); }
    @media (max-width: 480px) { .ej-line .katex { font-size: .88em; } }
"""
G.pagina("funcion-inversa", 5, "Función inversa",
         "Función inversa: regla de correspondencia, dominio y rango de la inversa, comprobación y gráfica con la recta y = x.",
         [ap, ejemplo,
          G.seccion("Ejercicios", "ejercicios", f'      <p class="enunciado">{PIDE}</p>\n'
                    + G.grid([card("Bloque 1", EJERCICIOS[:2]), card("Bloque 2", EJERCICIOS[2:])], 2)),
          G.seccion("Ejercicios extra", "extra", f'      <p class="enunciado">{PIDE}</p>\n'
                    + G.grid([card("Bloque 1", EXTRAS[:5]), card("Bloque 2", EXTRAS[5:])], 2), colapsable=True)],
         prev=("funcion-cuadratica.html", "Función cuadrática"),
         sig=("area-funcion-longitud.html", "Área como función de la longitud"), css_extra=CSS)
print("ok tema 5")
