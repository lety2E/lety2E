"""Math 4 · Tema 8 · Esbozo gráfico de una función. Fuente: capturas (ejemplo, 4 ejercicios, resueltos).

Es el tema 7 al revés: se dan los datos y se pide la gráfica. Usa la misma maquinaria de nodos
(curva, analiza, datos_html), que se toma de tema7.py.
"""
import pathlib
exec(pathlib.Path(__file__).with_name("tema7.py").read_text().split("EJEMPLO = ")[0])

def esbozo(nodos):
    d = analiza(nodos)
    ys = [p[1] for p in nodos]
    return ('<div class="graf-wrap">' + graf([(d["f"], nodos[0][0], nodos[-1][0])], puntos=nodos,
            ventana=(nodos[0][0] - 1, nodos[-1][0] + 1, min(ys) - 1, max(ys) + 1), muestras=160,
            etiqueta="Esbozo de la función") + '</div>')

EJEMPLO = [(-7, 3), (-3, 4), (2, 0), (4, -3), (6, 0), (7, 1)]
EJERCICIOS = [
    [(-7, -1), (-5, -3), (-2, 0), (3, 4), (4, 2)],
    [(-6, 5), (-4, 0), (-3, -1), (-1, 0), (2, 3), (4, 0), (5, -1)],
    [(-7, -1), (-6, 0), (-3, 4), (3, 0), (5, -2), (7, 0), (8, 1)],
    [(-6, -2), (-3, -5), (3, 0), (6, 3), (7, 1)],
]
EXTRAS = [
    [(-7, 2), (-5, 0), (-3, -4), (0, 0), (2, 3), (5, 1)],
    [(-6, -3), (-4, 0), (-1, 5), (3, 0), (4, -2), (6, 0), (7, 2)],
    [(-8, 4), (-6, 0), (-4, -2), (-2, 0), (1, 3), (4, 0), (6, -5)],
    [(-5, -1), (-3, -4), (1, 0), (3, 2), (5, 0), (7, -3)],
    [(-7, -4), (-5, 0), (-2, 3), (2, 1), (6, 5)],
    [(-6, 4), (-3, 1), (0, 5), (3, 0), (5, -3), (8, -1)],
    [(-4, -2), (-2, 0), (1, 4), (4, 0), (6, -3), (7, 0), (8, 2)],
    [(-8, 1), (-6, 3), (-3, 0), (-1, -4), (2, 0), (5, 2)],
    [(-5, 5), (-2, 0), (0, -2), (3, 0), (5, 4), (7, 2)],
    [(-7, -3), (-4, 0), (-2, 2), (0, 0), (3, -5), (6, 0), (8, 3)],
]
todos = [EJEMPLO] + EJERCICIOS + EXTRAS
assert len({tuple(t) for t in todos}) == len(todos)

def tupla(n):
    d = analiza(n)
    return tuple(d[k].replace("\\,", "").replace("\\{", "{").replace("\\}", "}").replace(" \\cup ", "U")
                 for k in ("dominio", "rango", "maximos", "minimos", "raices", "crece", "decrece", "positiva", "negativa"))
CAPTURA = [
    # el ejemplo de la captura dice crecimiento (-7,3)U(4,7): es (-7,-3), el máximo está en x = -3
    ("(-7,7)", "(-3,4)", "{(-3,4),(7,1)}", "{(-7,3),(4,-3)}", "{2,6}", "(-7,-3)U(4,7)", "(-3,4)", "(-7,2)U(6,7)", "(2,6)"),
    ("(-7,4)", "(-3,4)", "{(-7,-1),(3,4)}", "{(-5,-3),(4,2)}", "{-2}", "(-5,3)", "(-7,-5)U(3,4)", "(-2,4)", "(-7,-2)"),
    ("(-6,5)", "(-1,5)", "{(-6,5),(2,3)}", "{(-3,-1),(5,-1)}", "{-4,-1,4}", "(-3,2)", "(-6,-3)U(2,5)", "(-6,-4)U(-1,4)", "(-4,-1)U(4,5)"),
    ("(-7,8)", "(-2,4)", "{(-3,4),(8,1)}", "{(-7,-1),(5,-2)}", "{-6,3,7}", "(-7,-3)U(5,8)", "(-3,5)", "(-6,3)U(7,8)", "(-7,-6)U(3,7)"),
    ("(-6,7)", "(-5,3)", "{(-6,-2),(6,3)}", "{(-3,-5),(7,1)}", "{3}", "(-3,6)", "(-6,-3)U(6,7)", "(3,7)", "(-6,3)"),
]
for n, esperado in zip([EJEMPLO] + EJERCICIOS, CAPTURA):
    assert tupla(n) == esperado, (tupla(n), esperado)
for n in EXTRAS:
    analiza(n)
print("datos = captura")

ENUN = "Esboza la gráfica de la función a partir de sus datos."
ap = apuntes([
    "En <strong>Análisis de una función</strong> se identifican las partes de una función observando su gráfica; "
    "también se puede hacer al revés: <strong>graficar la función a partir de los datos</strong>.",
    "Se empieza graficando los <strong>puntos máximos y mínimos</strong>. Después se traza una línea que junte todos "
    "los puntos, cuidando que cumpla con los demás datos — sobre todo, que toque los puntos donde están las <strong>raíces</strong>.",
])
ejemplo = g.seccion_ejemplo(
    f'        <p class="enunciado">{ENUN}</p>\n        {datos_html(EJEMPLO)}\n        {esbozo(EJEMPLO)}')
ejercicios = g.seccion("Ejercicios", "ejercicios",
    f'      <p class="enunciado">{ENUN}</p>\n'
    + g.grid([card(i + 1, datos_html(n)) for i, n in enumerate(EJERCICIOS)], 2))
respuestas = g.seccion("Respuestas", "respuestas",
    g.resol_grid([resol(f"Ejercicio {i + 1}", esbozo(n)) for i, n in enumerate(EJERCICIOS)]), colapsable=True)
extras = g.seccion("Ejercicios extra", "extra",
    f'      <p class="enunciado">{ENUN}</p>\n'
    + g.grid([card(i + 5, datos_html(n)) for i, n in enumerate(EXTRAS)], 2), colapsable=True)

CSS = CSS_COMUN + """
    .graf-svg { max-width: 100%; width: 320px; }
    .graf-wrap { margin: .4rem 0 .8rem; }
    .datos-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0 1rem; margin-bottom: .6rem; }
    .mini-card-body .datos-grid { grid-template-columns: 1fr 1fr; }
    @media (max-width: 700px) { .datos-grid { grid-template-columns: 1fr 1fr; } }
    @media (max-width: 420px) { .datos-grid, .mini-card-body .datos-grid { grid-template-columns: 1fr; } }
    .dato { font-size: .95rem; color: var(--text); }
    .resol-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
    @media (max-width: 760px) { .resol-grid { grid-template-columns: 1fr; } }
"""
g.pagina("esbozo-grafico", 8, "Esbozo gráfico de una función",
         "Esbozo gráfico de una función a partir de su dominio, rango, máximos, mínimos, raíces, crecimiento y signo.",
         [ap, ejemplo, ejercicios, respuestas, extras],
         prev=("analisis-funcion.html", "Análisis de una función"),
         sig=("operaciones-funciones.html", "Operaciones con funciones"), css_extra=CSS)
print("ok tema 8")
