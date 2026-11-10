"""Math 4 · Tema 3 · Función escalonada. Fuente: capturas (ejemplos, ejercicios, resueltos)."""
import sys
from comun import g, cargar, CSS_COMUN, apuntes, card, dato, resol
esc = cargar("escalonadas-svg-math").escalonada

# tramo = (valor, a, b, cerrado)
def n(x):
    return str(x)

def regla(tramos):
    LE = "\\le"
    filas = " \\\\ ".join(
        f"{n(v)} & {n(a)} {LE if c else '<'} x {LE if c else '<'} {n(b)}" for v, a, b, c in tramos)
    return f"f(x) = \\begin{{cases}} {filas} \\end{{cases}}"

def dominio(tramos):
    return " \\cup ".join((f"[{a},\\,{b}]" if c else f"({a},\\,{b})") for v, a, b, c in tramos)

def rango(tramos):
    return "\\{" + ",\\,".join(n(t[0]) for t in tramos) + "\\}"

def f_card(t):   # regla de correspondencia en display
    return f'<div class="ej-line">$${regla(t)}$$</div>'

def g_card(t):   # la gráfica
    return f'<div class="graf-wrap">{esc(t)}</div>'

# ── datos ────────────────────────────────────────────────────────────────
EJ1 = [(-3, -2, 0, False), (2, 1, 3, True), (5, 4, 6, False)]
EJ2 = [(-1, -3, -1, False), (2, 0, 3, True), (-2, 4, 5, False)]

GRAFICA = [  # ejercicios1.jpg — de la regla a la gráfica
    [(-3, -4, -2, True), (2, -1, 1, False), (-1, 2, 4, False)],
    [(4, -5, -3, False), (-2, -2, 0, True), (1, 1, 3, True)],
    [(-2, -3, -1, False), (3, 0, 3, True), (-4, 4, 6, False)],
    [(5, -6, -3, True), (-1, -2, 1, False), (2, 2, 3, True)],
]
REGLA = [    # ejercicios2.jpg — de la gráfica a la regla
    [(-2, -5, -2, False), (3, -1, 2, True), (1, 3, 5, False)],
    [(2, -5, -1, True), (-1, 0, 2, False), (-3, 3, 6, True)],
    [(4, -7, -3, False), (3, -2, 1, True), (-1, 2, 6, True)],
    [(2, -6, -3, False), (-3, -2, 1, False), (1, 2, 6, True)],
]
# extras nuevos (sin respuesta)
X_GRAFICA = [
    [(2, -5, -3, False), (-1, -2, 1, True), (4, 2, 5, False)],
    [(-4, -6, -4, True), (1, -3, 0, False), (3, 1, 4, True)],
    [(3, -4, -1, True), (-2, 0, 2, True), (5, 3, 6, False)],
    [(-1, -5, -2, False), (4, -1, 1, False), (-3, 2, 5, True)],
    [(1, -6, -3, False), (-3, -2, 2, True), (2, 3, 5, False)],
    [(-2, -3, 0, True), (3, 1, 3, False), (-4, 4, 7, True)],
]
X_REGLA = [
    [(3, -6, -3, True), (-2, -2, 1, False), (1, 2, 5, True)],
    [(-3, -5, -2, False), (2, -1, 2, True), (4, 3, 6, False)],
    [(1, -4, -1, False), (-1, 0, 3, False), (3, 4, 6, True)],
    [(-2, -7, -4, True), (4, -3, 0, True), (-4, 1, 4, False)],
    [(5, -5, -3, False), (2, -2, 2, True), (-1, 3, 6, True)],
    [(-1, -6, -2, True), (-3, -1, 1, False), (2, 2, 4, False)],
]

# comprobación mínima: los tramos no se enciman y van de izquierda a derecha
for lista in (GRAFICA, REGLA, X_GRAFICA, X_REGLA, [EJ1, EJ2]):
    for t in lista:
        for (v, a, b, c), (v2, a2, b2, c2) in zip(t, t[1:]):
            assert a < b < a2 < b2, t
        assert len({x[0] for x in t}) == len(t), t
todos = [tuple(t) for l in (GRAFICA, REGLA, X_GRAFICA, X_REGLA, [EJ1, EJ2]) for t in l]
assert len(set(todos)) == len(todos), "hay un ejercicio repetido"

# ── secciones ────────────────────────────────────────────────────────────
ap = apuntes([
    "Una <strong>función escalonada</strong> toma un valor fijo en cada parte de su dominio: "
    "su gráfica son tramos horizontales, como escalones.",
    "<strong>Intervalo abierto</strong> $a < x < b$ se escribe $(a,\\,b)$: la desigualdad es estricta, "
    "<strong>no incluye</strong> a $a$ ni a $b$, y sus extremos se dibujan <strong>huecos</strong>.",
    "<strong>Intervalo cerrado</strong> $a \\le x \\le b$ se escribe $[a,\\,b]$: la desigualdad no es estricta, "
    "<strong>incluye</strong> a $a$ y a $b$, y sus extremos se dibujan <strong>rellenos</strong>.",
    "El <strong>rango</strong> son los valores que toma la función en $y$.",
])

ej1 = g.seccion_ejemplo(
    '        <p class="enunciado">Grafica la función escalonada a partir de su regla de correspondencia; '
    'escribe su dominio y su rango.</p>\n'
    f'        <div class="ej-line">$${regla(EJ1)}$$</div>\n'
    f'        <div class="resol-2col">\n          <div>\n'
    f'            {dato("dominio", dominio(EJ1))}\n            {dato("rango", rango(EJ1))}\n          </div>\n'
    f'          {g_card(EJ1)}\n        </div>', titulo="Ejemplo 1 · Gráfica")

ej2 = g.seccion_ejemplo(
    '        <p class="enunciado">Encuentra la regla de correspondencia de la gráfica de la función '
    'escalonada y expresa el dominio con desigualdades.</p>\n'
    f'        <div class="resol-2col">\n          {g_card(EJ2)}\n'
    f'          <div class="ej-line">$${regla(EJ2)}$$</div>\n        </div>', titulo="Ejemplo 2 · Regla de correspondencia")

ejercicios = g.seccion("Ejercicios", "ejercicios",
    '      <p class="parte-titulo">Gráfica</p>\n'
    '      <p class="enunciado">Grafica cada función; escribe su dominio y su rango.</p>\n'
    + g.grid([card(i + 1, f_card(t)) for i, t in enumerate(GRAFICA)], 2) + "\n"
    '      <p class="parte-titulo">Regla de correspondencia</p>\n'
    '      <p class="enunciado">Encuentra la regla de correspondencia de cada gráfica.</p>\n'
    + g.grid([card(i + 5, g_card(t)) for i, t in enumerate(REGLA)], 2))

r1 = [resol(f"Ejercicio {i + 1}",
            f'<div class="resol-2col"><div>{dato("dominio", dominio(t))}{dato("rango", rango(t))}</div>{g_card(t)}</div>')
      for i, t in enumerate(GRAFICA)]
r2 = [resol(f"Ejercicio {i + 5}", f'<div class="sol">$${regla(t)}$$</div>') for i, t in enumerate(REGLA)]
respuestas = g.seccion("Respuestas", "respuestas", g.resol_grid(r1 + r2), colapsable=True)

extras = g.seccion("Ejercicios extra", "extra",
    '      <p class="parte-titulo">Gráfica</p>\n'
    '      <p class="enunciado">Grafica cada función; escribe su dominio y su rango.</p>\n'
    + g.grid([card(i + 9, f_card(t)) for i, t in enumerate(X_GRAFICA)], 3) + "\n"
    '      <p class="parte-titulo">Regla de correspondencia</p>\n'
    '      <p class="enunciado">Encuentra la regla de correspondencia de cada gráfica.</p>\n'
    + g.grid([card(i + 15, g_card(t)) for i, t in enumerate(X_REGLA)], 3), colapsable=True)

video = g.seccion_video(["6NKZhTKLVrQ", "yewJZul6ReM"], "Función escalonada")

g.pagina("funcion-escalonada", 3, "Función escalonada",
         "Función escalonada: gráfica, dominio, rango y regla de correspondencia. Ejemplos y ejercicios resueltos.",
         [video, ap, ej1, ej2, ejercicios, respuestas, extras],
         prev=("representacion-funciones.html", "Representación de funciones"), sig=("funcion-cuadratica.html", "Función cuadrática"),
         css_extra=CSS_COMUN + "    .graf-svg { max-width: 100%; width: 300px; }\n")
print("ok tema 3")
