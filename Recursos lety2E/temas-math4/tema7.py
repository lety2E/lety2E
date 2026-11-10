"""Math 4 · Tema 7 · Análisis de una función. Fuente: capturas (ejemplo, 4 gráficas, resueltos).

Cada gráfica se describe con sus nodos (x, y): extremos del dominio, máximos, mínimos y raíces.
La curva pasa suave por ellos (tangente horizontal en máximos y mínimos) y las respuestas se
calculan de los mismos nodos.
"""
from comun import g, cargar, CSS_COMUN, apuntes, card, dato, resol
graf = cargar("funciones-svg-math").grafica

def curva(nodos):
    xs = [p[0] for p in nodos]; ys = [p[1] for p in nodos]
    n = len(nodos)
    d = [(ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i]) for i in range(n - 1)]
    m = [0.0] * n
    for i in range(1, n - 1):
        if d[i - 1] * d[i] > 0:                       # nodo de paso (raíz): media armónica
            w1 = 2 * (xs[i + 1] - xs[i]) + (xs[i] - xs[i - 1])
            w2 = (xs[i + 1] - xs[i]) + 2 * (xs[i] - xs[i - 1])
            m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])
    m[0], m[-1] = 1.5 * d[0], 1.5 * d[-1]
    def f(x):
        i = max(0, min(n - 2, max(k for k in range(n - 1) if xs[k] <= x + 1e-12)))
        h = xs[i + 1] - xs[i]; t = (x - xs[i]) / h
        return ((2 * t**3 - 3 * t**2 + 1) * ys[i] + (t**3 - 2 * t**2 + t) * h * m[i]
                + (-2 * t**3 + 3 * t**2) * ys[i + 1] + (t**3 - t**2) * h * m[i + 1])
    return f

def iv(a, b):
    return f"({a},\\,{b})"

def union(l):
    return " \\cup ".join(l)

def analiza(nodos):
    giros = [p for p in nodos if p[1] != 0 or p in (nodos[0], nodos[-1])]
    giros = [p for i, p in enumerate(nodos) if i in (0, len(nodos) - 1) or p[1] != 0]
    raices = [p[0] for p in nodos if p[1] == 0]
    sube = [b[1] > a[1] for a, b in zip(giros, giros[1:])]
    assert all(s != t for s, t in zip(sube, sube[1:])), ("no alterna", nodos)
    for a, b in zip(nodos, nodos[1:]):
        assert a[0] < b[0]
    for a, b in zip(giros, giros[1:]):                # entre giros de signo contrario hay una raíz
        if a[1] * b[1] < 0:
            assert any(a[0] < r < b[0] for r in raices), ("falta raíz", a, b)
    maxs, mins = [], []
    for i, p in enumerate(giros):
        es_max = sube[i - 1] if i else not sube[0]
        (maxs if es_max else mins).append(p)
    crec = [iv(a[0], b[0]) for (a, b), s in zip(zip(giros, giros[1:]), sube) if s]
    decr = [iv(a[0], b[0]) for (a, b), s in zip(zip(giros, giros[1:]), sube) if not s]
    f = curva(nodos)
    cortes = [nodos[0][0]] + raices + [nodos[-1][0]]
    cortes = sorted(set(cortes))
    pos = [iv(a, b) for a, b in zip(cortes, cortes[1:]) if f((a + b) / 2) > 0]
    neg = [iv(a, b) for a, b in zip(cortes, cortes[1:]) if f((a + b) / 2) < 0]
    ys = [p[1] for p in nodos]
    pts = lambda l: "\\{" + ",\\,".join(f"({x},\\,{y})" for x, y in l) + "\\}"
    return dict(f=f, giros=giros,
                dominio=iv(nodos[0][0], nodos[-1][0]), rango=iv(min(ys), max(ys)),
                maximos=pts(maxs), minimos=pts(mins),
                raices="\\{" + ",\\,".join(map(str, raices)) + "\\}",
                crece=union(crec), decrece=union(decr), positiva=union(pos), negativa=union(neg))

def grafica(nodos):
    d = analiza(nodos)
    ys = [p[1] for p in nodos]
    return ('<div class="graf-wrap">' + graf([(d["f"], nodos[0][0], nodos[-1][0])], puntos=d["giros"],
            ventana=(nodos[0][0] - 1, nodos[-1][0] + 1, min(ys) - 1, max(ys) + 1), muestras=160,
            etiqueta="Gráfica de la función a analizar") + '</div>')

def datos_html(nodos):
    d = analiza(nodos)
    return ('<div class="datos-grid">'
            + dato("dominio", d["dominio"]) + dato("rango", d["rango"])
            + dato("puntos máximos", d["maximos"]) + dato("puntos mínimos", d["minimos"])
            + dato("raíces", d["raices"]) + dato("crecimiento", d["crece"])
            + dato("decrecimiento", d["decrece"]) + dato("positiva", d["positiva"])
            + dato("negativa", d["negativa"]) + '</div>')

EJEMPLO = [(-6, 5), (-4, 0), (-2, -3), (1, 0), (3, 3), (5, 0), (6, -2)]
EJERCICIOS = [
    [(-7, 3), (-6, 0), (-5, -2), (-2, 0), (1, 2), (2, 0), (4, -3)],
    [(-6, 2), (-2, 4), (2, 0), (4, -2), (5, 0), (6, 1)],
    [(-7, -2), (-5, 0), (-2, 3), (1, 0), (4, -3), (6, -1)],
    [(-6, -2), (-3, -5), (2, 0), (5, 3), (7, 0), (8, -2)],
]
EXTRAS = [
    [(-6, -3), (-4, 0), (-2, 4), (1, 0), (3, -2), (5, 0), (7, 3)],
    [(-7, 4), (-5, 0), (-3, -3), (0, 0), (2, 2), (4, 0), (6, -4)],
    [(-5, 2), (-3, 5), (0, 0), (2, -3), (5, 0), (6, 2)],
    [(-8, -1), (-6, -4), (-3, 0), (-1, 3), (2, 0), (4, -2)],
    [(-6, 5), (-3, 0), (-1, -2), (1, 0), (4, 4), (6, 0), (7, -1)],
    [(-7, -2), (-6, 0), (-4, 3), (-1, 0), (2, -5), (5, 0), (6, 1)],
    [(-4, 3), (-2, 0), (0, -4), (3, 0), (5, 2), (7, 0), (8, -3)],
    [(-6, 1), (-4, 4), (-1, 0), (1, -3), (4, 0), (6, 5)],
    [(-5, -4), (-2, 0), (0, 2), (2, 0), (5, -3), (7, 0), (8, 2)],
    [(-8, 2), (-6, 0), (-5, -1), (-2, 0), (1, 5), (3, 0), (6, -2)],
]
todos = [EJEMPLO] + EJERCICIOS + EXTRAS
assert len({tuple(t) for t in todos}) == len(todos)

# lo que dicen las capturas (rango, máximos, mínimos, raíces, crece, decrece, positiva, negativa)
def tupla(n):
    d = analiza(n)
    return tuple(d[k].replace("\\,", "").replace("\\{", "{").replace("\\}", "}").replace(" \\cup ", "U")
                 for k in ("dominio", "rango", "maximos", "minimos", "raices", "crece", "decrece", "positiva", "negativa"))
CAPTURA = [
    ("(-6,6)", "(-3,5)", "{(-6,5),(3,3)}", "{(-2,-3),(6,-2)}", "{-4,1,5}", "(-2,3)", "(-6,-2)U(3,6)", "(-6,-4)U(1,5)", "(-4,1)U(5,6)"),
    ("(-7,4)", "(-3,3)", "{(-7,3),(1,2)}", "{(-5,-2),(4,-3)}", "{-6,-2,2}", "(-5,1)", "(-7,-5)U(1,4)", "(-7,-6)U(-2,2)", "(-6,-2)U(2,4)"),
    ("(-6,6)", "(-2,4)", "{(-2,4),(6,1)}", "{(-6,2),(4,-2)}", "{2,5}", "(-6,-2)U(4,6)", "(-2,4)", "(-6,2)U(5,6)", "(2,5)"),
    ("(-7,6)", "(-3,3)", "{(-2,3),(6,-1)}", "{(-7,-2),(4,-3)}", "{-5,1}", "(-7,-2)U(4,6)", "(-2,4)", "(-5,1)", "(-7,-5)U(1,6)"),
    ("(-6,8)", "(-5,3)", "{(-6,-2),(5,3)}", "{(-3,-5),(8,-2)}", "{2,7}", "(-3,5)", "(-6,-3)U(5,8)", "(2,7)", "(-6,2)U(7,8)"),
]
for n, esperado in zip([EJEMPLO] + EJERCICIOS, CAPTURA):
    assert tupla(n) == esperado, (tupla(n), esperado)
for n in EXTRAS:
    analiza(n)
print("respuestas = captura")

ENUN = ("Encuentra el dominio, el rango, los puntos máximos y mínimos, las raíces, los intervalos de "
        "crecimiento y decrecimiento, y los intervalos donde la función es positiva y donde es negativa.")

video = g.seccion_video("nS-2rjZhCi4", "Análisis de una función")
ap = apuntes([
    "<strong>Dominio y rango</strong>: se marca un rectángulo que abarca la función; el dominio se lee en el eje $x$ y el rango en el eje $y$.",
    "<strong>Puntos máximos y mínimos</strong>: los puntos más altos y los más bajos.",
    "<strong>Raíces</strong>: donde la función cruza el eje $x$, es decir, $f(x) = 0$.",
    "<strong>Crecimiento y decrecimiento</strong>: las zonas del dominio donde la función va para arriba, y donde va para abajo.",
    "<strong>Positiva y negativa</strong>: las zonas del dominio donde la función está arriba del eje $x$, y donde está abajo.",
])
ejemplo = g.seccion_ejemplo(
    f'        <p class="enunciado">{ENUN}</p>\n        {grafica(EJEMPLO)}\n        {datos_html(EJEMPLO)}')
ejercicios = g.seccion("Ejercicios", "ejercicios",
    f'      <p class="enunciado">{ENUN}</p>\n'
    + g.grid([card(i + 1, grafica(n)) for i, n in enumerate(EJERCICIOS)], 2))
respuestas = g.seccion("Respuestas", "respuestas",
    g.resol_grid([resol(f"Ejercicio {i + 1}", grafica(n) + datos_html(n)) for i, n in enumerate(EJERCICIOS)]),
    colapsable=True)
extras = g.seccion("Ejercicios extra", "extra",
    f'      <p class="enunciado">{ENUN}</p>\n'
    + g.grid([card(i + 5, grafica(n)) for i, n in enumerate(EXTRAS)], 2), colapsable=True)

CSS = CSS_COMUN + """
    .graf-svg { max-width: 100%; width: 320px; }
    .graf-wrap { margin: .4rem 0 .8rem; }
    .datos-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0 1rem; }
    @media (max-width: 700px) { .datos-grid { grid-template-columns: 1fr 1fr; } }
    @media (max-width: 420px) { .datos-grid { grid-template-columns: 1fr; } }
    .dato { font-size: .95rem; color: var(--text); }
"""
g.pagina("analisis-funcion", 7, "Análisis de una función",
         "Análisis de una función a partir de su gráfica: dominio, rango, máximos, mínimos, raíces, crecimiento y signo.",
         [video, ap, ejemplo, ejercicios, respuestas, extras],
         prev=("area-funcion-longitud.html", "Área como función de la longitud"),
         sig=("esbozo-grafico.html", "Esbozo gráfico de una función"), css_extra=CSS)
print("ok tema 7")
