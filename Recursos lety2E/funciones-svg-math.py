"""Gráfica SVG de una función en el plano, con ejes numerados (lety2e.com · Math 4).

    grafica(curvas, puntos=[...], ventana=(x0, x1, y0, y1))

- curvas: lista de (f, a, b) — se traza y = f(x) de x = a a x = b. Si f truena o se
  sale de la ventana en algún x, el trazo se corta ahí (sirve para 1/x, raíces…).
- puntos: lista de (x, y) o (x, y, "hueco").
- ventana: opcional; si falta se calcula de los puntos y las curvas.
- paso_y / paso_x: cada cuántas unidades va una línea del grid (1 por omisión). Cuando
  el rango es muy grande se sube a 2, 4 o 5 y la escala se encoge en ese eje.
- punteadas: lista de ("v", x) o ("h", y) — asíntotas o rectas guía.

Reglas del proyecto: 1 cuadro = 1 unidad, grid #E0C4BC, ejes #7B5A50,
curva #FF00AA 2.2, puntos #1A0828 r=3.
"""
import math

U = 20
PAD = 14
GRID, EJE, MAG, PUNTO = "#E0C4BC", "#7B5A50", "#FF00AA", "#1A0828"


def _n(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def grafica(curvas=(), puntos=(), ventana=None, paso_x=1, paso_y=1, punteadas=(),
            etiqueta="Gráfica de la función", segundo_color=None, muestras=60):
    xs, ys = [0], [0]
    for p in puntos:
        xs.append(p[0]); ys.append(p[1])
    if ventana:
        x0, x1, y0, y1 = ventana
    else:
        for f, a, b in curvas:
            for i in range(muestras + 1):
                x = a + (b - a) * i / muestras
                try:
                    y = f(x)
                except (ValueError, ZeroDivisionError):
                    continue
                xs.append(x); ys.append(y)
        x0, x1 = math.floor(min(xs)) - 1, math.ceil(max(xs)) + 1
        y0, y1 = math.floor(min(ys)) - 1, math.ceil(max(ys)) + 1
    ux, uy = U / paso_x, U / paso_y
    W = (x1 - x0) * ux + 2 * PAD
    H = (y1 - y0) * uy + 2 * PAD
    X = lambda x: PAD + (x - x0) * ux
    Y = lambda y: PAD + (y1 - y) * uy
    o = [f'<svg class="graf-svg" viewBox="0 0 {_n(W)} {_n(H)}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{_n(W)}" height="{_n(H)}" role="img" aria-label="{etiqueta}">']
    gx = [x for x in range(x0, x1 + 1) if x % paso_x == 0]
    gy = [y for y in range(y0, y1 + 1) if y % paso_y == 0]
    for x in gx:
        o.append(f'<line x1="{_n(X(x))}" y1="{_n(Y(y1))}" x2="{_n(X(x))}" y2="{_n(Y(y0))}" stroke="{GRID}" stroke-width="0.5"/>')
    for y in gy:
        o.append(f'<line x1="{_n(X(x0))}" y1="{_n(Y(y))}" x2="{_n(X(x1))}" y2="{_n(Y(y))}" stroke="{GRID}" stroke-width="0.5"/>')
    ex = min(max(0, x0), x1)     # si el 0 queda fuera, el eje va en el borde
    ey = min(max(0, y0), y1)
    o.append(f'<line x1="{_n(X(x0))}" y1="{_n(Y(ey))}" x2="{_n(X(x1))}" y2="{_n(Y(ey))}" stroke="{EJE}" stroke-width="1.2"/>')
    o.append(f'<line x1="{_n(X(ex))}" y1="{_n(Y(y1))}" x2="{_n(X(ex))}" y2="{_n(Y(y0))}" stroke="{EJE}" stroke-width="1.2"/>')
    for x in gx:
        if x != ex and x0 < x < x1:
            o.append(f'<line x1="{_n(X(x))}" y1="{_n(Y(ey) - 2.5)}" x2="{_n(X(x))}" y2="{_n(Y(ey) + 2.5)}" stroke="{EJE}" stroke-width="1"/>')
            o.append(f'<text x="{_n(X(x))}" y="{_n(Y(ey) + 11)}" text-anchor="middle" font-size="8" fill="{EJE}">{x}</text>')
    for y in gy:
        if y != ey and y0 < y < y1:
            o.append(f'<line x1="{_n(X(ex) - 2.5)}" y1="{_n(Y(y))}" x2="{_n(X(ex) + 2.5)}" y2="{_n(Y(y))}" stroke="{EJE}" stroke-width="1"/>')
            o.append(f'<text x="{_n(X(ex) - 5)}" y="{_n(Y(y) + 3)}" text-anchor="end" font-size="8" fill="{EJE}">{y}</text>')
    for tipo, v in punteadas:
        if tipo == "v":
            o.append(f'<line x1="{_n(X(v))}" y1="{_n(Y(y1))}" x2="{_n(X(v))}" y2="{_n(Y(y0))}" stroke="{EJE}" stroke-width="1" stroke-dasharray="4 3"/>')
        else:
            o.append(f'<line x1="{_n(X(x0))}" y1="{_n(Y(v))}" x2="{_n(X(x1))}" y2="{_n(Y(v))}" stroke="{EJE}" stroke-width="1" stroke-dasharray="4 3"/>')
    for k, (f, a, b) in enumerate(curvas):
        color = segundo_color if (segundo_color and k) else MAG
        tramo, tramos = [], []
        for i in range(muestras + 1):
            x = a + (b - a) * i / muestras
            try:
                y = f(x)
                ok = y0 - 1e-9 <= y <= y1 + 1e-9
            except (ValueError, ZeroDivisionError):
                ok = False
            if ok:
                tramo.append(f"{_n(X(x))},{_n(Y(y))}")
            elif tramo:
                tramos.append(tramo); tramo = []
        if tramo:
            tramos.append(tramo)
        for t in tramos:
            if len(t) > 1:
                o.append(f'<polyline points="{" ".join(t)}" fill="none" stroke="{color}" stroke-width="2.2" '
                         f'stroke-linecap="round" stroke-linejoin="round"/>')
    for p in puntos:
        if len(p) > 2 and p[2] == "hueco":
            o.append(f'<circle cx="{_n(X(p[0]))}" cy="{_n(Y(p[1]))}" r="3" fill="#FFFFFF" stroke="{PUNTO}" stroke-width="1.4"/>')
        else:
            o.append(f'<circle cx="{_n(X(p[0]))}" cy="{_n(Y(p[1]))}" r="3" fill="{PUNTO}"/>')
    o.append('</svg>')
    return "".join(o)
