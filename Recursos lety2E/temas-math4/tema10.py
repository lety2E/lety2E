"""Math 4 · Tema 10 · Composición de funciones. Fuente: capturas (3 hojas de ejemplo, 3 bloques, resueltos).

Cada bloque trae f (cuadrática), g (lineal), m = kx², h = jx³ y L = N/D racional (una parte lineal
y la otra cuadrática sin término en x, en el orden en que están escritas). Los pasos de cada
composición son los de las hojas de Lety.
"""
import pathlib
exec(pathlib.Path(__file__).with_name("tema9.py").read_text().split("def division")[0])   # term, tex, reduce, neg, mult

def junta(p):
    """Suma términos semejantes SIN reordenar: cada uno queda donde apareció por primera vez."""
    orden, d = [], {}
    for c, e in p:
        if e not in d:
            orden.append(e); d[e] = 0
        d[e] += c
    return [(d[e], e) for e in orden if d[e]]

def trozos(l):
    """l = [(signo, cuerpo)] → texto con los signos entre trozos."""
    s = ""
    for i, (sg, cuerpo) in enumerate(l):
        s += (("-" if sg < 0 else "") if i == 0 else (" - " if sg < 0 else " + ")) + cuerpo
    return s

def de_poly(p):
    return [(1 if c > 0 else -1, term(abs(c), e, True)) for c, e in p]

def cf(c):                      # coeficiente delante de un paréntesis
    return "" if abs(c) == 1 else str(abs(c))

def par(v):                     # número suelto dentro de un producto
    return f"({v})"

def al(nombre, lineas):
    return ('<div class="sol">$$\\begin{aligned} ' + f"{nombre} &= " + " \\\\ &= ".join(lineas)
            + ' \\end{aligned}$$</div>')

def negr(s):
    return f"\\boldsymbol{{{s}}}"

def cuadrado_lineal(gp):
    (p, _), (q, _) = gp
    binomio = f"({p}x)^2 + 2({p}x){par(q)} + {par(q)}^2"
    exp = [(p * p, 2), (2 * p * q, 1), (q * q, 0)]
    return binomio, exp

# ── sustituir una función dentro de un polinomio "en su orden" ──────────────
def en_mono(P, k, n):
    """P(k x^n): tres renglones (sustituido, a medias, resuelto)."""
    l1, l2, l3 = [], [], []
    inner = tex([(k, n)])
    for c, e in P:
        sg = 1 if c > 0 else -1
        if e == 0:
            for l in (l1, l2, l3):
                l.append((sg, str(abs(c))))
        elif e == 1:
            l1.append((sg, f"{cf(c)}({inner})"))
            for l in (l2, l3):
                l.extend(de_poly([(c * k, n)]))
        else:
            l1.append((sg, f"{cf(c)}({inner})^2"))
            l2.append((sg, f"{cf(c)}({tex([(k * k, 2 * n)])})"))
            l3.extend(de_poly([(c * k * k, 2 * n)]))
    return trozos(l1), trozos(l2), trozos(l3), [(c * k ** e, n * e) for c, e in P]

def en_lineal(P, gp):
    """P(px + q): cuatro renglones, como en las hojas."""
    (p, _), (q, _) = gp
    _, exp = cuadrado_lineal(gp)
    es_cuad = any(e == 2 for _, e in P)
    l1, l2, l3, total = [], [], [], []
    for c, e in P:
        sg = 1 if c > 0 else -1
        if e == 0:
            for l in (l1, l2, l3):
                l.append((sg, str(abs(c))))
            total.append((c, 0))
        elif e == 1:
            l1.append((sg, f"{cf(c)}({tex(gp)})"))
            d = [(c * p, 1), (c * q, 0)]
            l2.extend(de_poly(d)); l3.extend(de_poly(d)); total.extend(d)
        else:
            l1.append((sg, f"{cf(c)}({tex(gp)})^2"))
            l2.append((sg, f"{cf(c)}({tex(exp)})"))
            d = [(c * a, b) for a, b in exp]
            l3.extend(de_poly(d)); total.extend(d)
    final = tex(reduce(total))
    if not es_cuad:                       # la parte lineal ya queda resuelta en el tercer renglón
        return trozos(l1), trozos(l2), final, final, reduce(total)
    return trozos(l1), trozos(l2), trozos(l3), final, reduce(total)

def frac(a, b):
    return f"\\dfrac{{{a}}}{{{b}}}"

def composiciones(F):
    f, gp, m, h, N, D = F["f"], F["g"], F["m"], F["h"], F["N"], F["D"]
    (a, _), (b, _), (c, _) = f
    (p, _), (q, _) = gp
    (k, _), = m
    (j, _), = h
    out = []
    # 1 · f∘h
    l1, l2, l3, r = en_mono(f, j, 3)
    out.append(("f", "h", [l1, l2, negr(l3)], tex(r)))
    # 2 · f∘g
    binomio, exp = cuadrado_lineal(gp)
    bg = [(b * p, 1), (b * q, 0)]
    sa = 1 if a > 0 else -1
    L1 = trozos([(sa, f"{cf(a)}({tex(gp)})^2"), (1 if b > 0 else -1, f"{cf(b)}({tex(gp)})"), (1 if c > 0 else -1, str(abs(c)))])
    L2 = trozos([(sa, f"{abs(a)}({binomio})")] + de_poly(bg) + de_poly([(c, 0)]))
    resto = junta(bg + [(c, 0)])
    L3 = trozos([(sa, f"{abs(a)}({tex(exp)})")] + de_poly(resto))
    dist = [(a * u, e) for u, e in exp]
    L4 = tex(dist + resto)
    r = reduce(dist + resto)
    out.append(("f", "g", [L1, L2, L3, L4, negr(tex(r))], tex(r)))
    # 3 · m∘h
    l1, l2, l3, r = en_mono(m, j, 3)
    out.append(("m", "h", [l1, l2, negr(l3)], tex(r)))
    # 4 · m∘g
    sk = 1 if k > 0 else -1
    r = [(k * u, e) for u, e in exp]
    out.append(("m", "g", [trozos([(sk, f"{cf(k)}({tex(gp)})^2")]), trozos([(sk, f"{abs(k)}({binomio})")]),
                           trozos([(sk, f"{abs(k)}({tex(exp)})")]), negr(tex(r))], tex(r)))
    # 5 · L∘m
    n1, n2, n3, rn = en_mono(N, k, 2)
    d1, d2, d3, rd = en_mono(D, k, 2)
    out.append(("L", "m", [frac(n1, d1), frac(n2, d2), negr(frac(n3, d3))], frac(n3, d3)))
    # 6 · L∘g
    n = en_lineal(N, gp); d = en_lineal(D, gp)
    out.append(("L", "g", [frac(n[0], d[0]), frac(n[1], d[1]), frac(n[2], d[2]), negr(frac(n[3], d[3]))], frac(n[3], d[3])))
    # 7 · g∘L
    pN = [(p * u, e) for u, e in N]
    qD = [(q * u, e) for u, e in D]
    sq = 1 if q > 0 else -1
    L1 = f"\\dfrac{{{p}}}{{1}}\\left({frac(tex(N), tex(D))}\\right) {'+' if q > 0 else '-'} {abs(q)}"
    L2 = frac(trozos(de_poly(pN) + [(sq, f"{abs(q)}({tex(D)})")]), tex(D))
    L3 = frac(tex(pN + qD), tex(D))
    r = frac(tex(junta(pN + qD)), tex(D))
    out.append(("g", "L", [L1, L2, L3, negr(r)], r))
    return out

def resoluciones(F):
    return "\n".join(al(f"({x} \\circ {y})(x)", lineas) for x, y, lineas, _ in composiciones(F))

def finales(F):
    return [r for *_, r in composiciones(F)]

def bloque(f, g, m, h, N, D):
    return dict(f=f, g=g, m=m, h=h, N=N, D=D)

EJEMPLO = bloque([(4, 2), (3, 1), (-5, 0)], [(3, 1), (1, 0)], [(4, 2)], [(-5, 3)], [(5, 1), (-2, 0)], [(2, 2), (1, 0)])
BLOQUES = [
    bloque([(5, 2), (-3, 1), (1, 0)], [(4, 1), (2, 0)], [(3, 2)], [(-4, 3)], [(3, 1), (-5, 0)], [(4, 2), (6, 0)]),
    bloque([(-2, 2), (5, 1), (-3, 0)], [(6, 1), (-4, 0)], [(-3, 2)], [(2, 3)], [(5, 2), (-1, 0)], [(3, 0), (-4, 1)]),
    bloque([(-3, 2), (6, 1), (-4, 0)], [(7, 1), (-2, 0)], [(5, 2)], [(-3, 3)], [(4, 1), (-1, 0)], [(5, 0), (-1, 2)]),
]
EXTRAS = [
    bloque([(2, 2), (-4, 1), (3, 0)], [(5, 1), (1, 0)], [(2, 2)], [(3, 3)], [(2, 1), (3, 0)], [(1, 2), (-4, 0)]),
    bloque([(-4, 2), (1, 1), (-2, 0)], [(3, 1), (-5, 0)], [(-2, 2)], [(-2, 3)], [(3, 2), (2, 0)], [(1, 0), (-6, 1)]),
]

# ── lo que dicen las hojas ──
F = "\\dfrac{%s}{%s}"
assert finales(EJEMPLO) == ["100x^{6} - 15x^{3} - 5", "36x^{2} + 33x + 2", "100x^{6}", "36x^{2} + 24x + 4",
                            F % ("20x^{2} - 2", "32x^{4} + 1"), F % ("15x + 3", "18x^{2} + 12x + 3"),
                            F % ("15x - 5 + 2x^{2}", "2x^{2} + 1")], finales(EJEMPLO)
assert finales(BLOQUES[0]) == ["80x^{6} + 12x^{3} + 1", "80x^{2} + 68x + 15", "48x^{6}", "48x^{2} + 48x + 12",
                               F % ("9x^{2} - 5", "36x^{4} + 6"), F % ("12x + 1", "64x^{2} + 64x + 22"),
                               F % ("12x - 8 + 8x^{2}", "4x^{2} + 6")], finales(BLOQUES[0])
assert finales(BLOQUES[1]) == ["-8x^{6} + 10x^{3} - 3", "-72x^{2} + 126x - 55", "-12x^{6}", "-108x^{2} + 144x - 48",
                               F % ("45x^{4} - 1", "3 + 12x^{2}"), F % ("180x^{2} - 240x + 79", "-24x + 19"),
                               F % ("30x^{2} - 18 + 16x", "3 - 4x")], finales(BLOQUES[1])
assert finales(BLOQUES[2]) == ["-27x^{6} - 18x^{3} - 4", "-147x^{2} + 126x - 28", "45x^{6}", "245x^{2} - 140x + 20",
                               F % ("20x^{2} - 1", "5 - 25x^{4}"), F % ("28x - 9", "-49x^{2} + 28x + 1"),
                               F % ("28x - 17 + 2x^{2}", "5 - x^{2}")], finales(BLOQUES[2])
for B in EXTRAS:
    print(finales(B))
print("respuestas = hojas")

def funciones_tex(B):
    return [f"f(x) = {tex(B['f'])}", f"g(x) = {tex(B['g'])}", f"m(x) = {tex(B['m'])}", f"h(x) = {tex(B['h'])}",
            f"L(x) = {frac(tex(B['N']), tex(B['D']))}"]
PIDE = [f"({x} \\circ {y})(x)" for x, y in ("fh", "fg", "mh", "mg", "Lm", "Lg", "gL")]

def card_bloque(titulo, B):
    return (G.card_funciones(titulo, funciones_tex(B), PIDE)
            .replace("encuentra", "realiza las siguientes composiciones"))

dadas = "".join(f'<div class="ej-line">${t}$</div>' for t in funciones_tex(EJEMPLO))
ap = apuntes([
    "El símbolo $\\circ$ indica una <strong>composición</strong>: en $(f \\circ h)(x)$ la función $f$ está compuesta con $h$, "
    "así que en lugar de las $x$ de $f$ se coloca $h(x)$, y ya sólo se resuelve.",
    "Recordemos que $(a + b)^2 = a^2 + 2ab + b^2$.",
])
ejemplo = G.seccion_ejemplo(
    f'        <p class="ej-sub">dadas las funciones</p>\n        <div class="dadas">{dadas}</div>\n'
    f'        <p class="ej-sub ej-sub-2">realiza las siguientes composiciones</p>\n'
    f'        {resoluciones(EJEMPLO)}', titulo="Ejemplos")
video = G.seccion_video("7dn4MzHxI04", "Composición de funciones")
ejercicios = G.seccion("Ejercicios", "ejercicios",
    G.grid([card_bloque(f"Bloque {i + 1}", B) for i, B in enumerate(BLOQUES)], 3))
respuestas = G.seccion("Respuestas", "respuestas",
    G.resol_grid([f'          <div class="resol-item">\n            <div class="resol-num">Bloque {i + 1}</div>\n'
                  f'{resoluciones(B)}\n          </div>' for i, B in enumerate(BLOQUES)]), colapsable=True)
extras = G.seccion("Ejercicios extra", "extra",
    G.grid([card_bloque(f"Bloque {i + 1}", B) for i, B in enumerate(EXTRAS)], 2), colapsable=True)

CSS = CSS_COMUN + """
    .ej-sub {
      font-size: .72rem; font-weight: 700; text-transform: uppercase;
      letter-spacing: .06em; color: var(--text-3);
      margin: 0 0 .35rem; text-align: center;
    }
    .ej-sub-2 { margin-top: .9rem; }
    .mini-card-body .ej-sub + .ej-line { padding-top: .1rem; }
    .pide-lista { display: flex; flex-wrap: wrap; gap: .4rem; justify-content: center; align-items: center; }
    /* OJO: sólo el hijo directo — un `span` suelto alcanzaría a los de KaTeX */
    .pide-lista > span {
      display: inline-block; background: var(--accent-light); color: var(--accent);
      border-radius: 99px; padding: .22rem .65rem; font-weight: 600;
    }
    .dadas { text-align: center; margin-bottom: .4rem; }
    .ejemplo-block .sol + .sol, .resol-item .sol + .sol { border-top: 1px solid var(--border-s); }
    @media (max-width: 480px) { .sol .katex-display { font-size: .66em; } }
    @media (max-width: 380px) { .sol .katex-display { font-size: .6em; } }
"""
G.pagina("composicion-funciones", 10, "Composición de funciones",
         "Composición de funciones: cómo sustituir una función dentro de otra, con ejemplos y ejercicios resueltos paso a paso.",
         [video, ap, ejemplo, ejercicios, respuestas, extras],
         prev=("operaciones-funciones.html", "Operaciones con funciones"),
         sig=("dominio-maximo.html", "Dominio máximo"), css_extra=CSS)
print("ok tema 10")
