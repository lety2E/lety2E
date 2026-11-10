"""Gráfica SVG de una función escalonada (lety2e.com · Math 4, tema 3).

Cada tramo es (valor, a, b, cerrado): un segmento horizontal en y = valor
de x = a a x = b; `cerrado` True pinta los extremos rellenos (a <= x <= b),
False los deja huecos (a < x < b).

Reglas del proyecto: 1 cuadro = 1 unidad, grid #E0C4BC, ejes #7B5A50,
trazo #FF00AA 2.2, puntos #1A0828. Aquí los ejes SÍ llevan números, porque
el alumno tiene que leer los extremos de cada tramo.
"""
U = 20          # px por unidad
PAD = 14
GRID, EJE, MAG, PUNTO = "#E0C4BC", "#7B5A50", "#FF00AA", "#1A0828"


def escalonada(tramos, etiqueta="Gráfica de la función escalonada"):
    xs = [t[1] for t in tramos] + [t[2] for t in tramos] + [0]
    ys = [t[0] for t in tramos] + [0]
    x0, x1 = min(xs) - 1, max(xs) + 1
    y0, y1 = min(ys) - 1, max(ys) + 1
    W = (x1 - x0) * U + 2 * PAD
    H = (y1 - y0) * U + 2 * PAD
    X = lambda x: PAD + (x - x0) * U
    Y = lambda y: PAD + (y1 - y) * U
    o = [f'<svg class="graf-svg" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W}" height="{H}" role="img" aria-label="{etiqueta}">']
    for x in range(x0, x1 + 1):
        o.append(f'<line x1="{X(x)}" y1="{Y(y1)}" x2="{X(x)}" y2="{Y(y0)}" stroke="{GRID}" stroke-width="0.5"/>')
    for y in range(y0, y1 + 1):
        o.append(f'<line x1="{X(x0)}" y1="{Y(y)}" x2="{X(x1)}" y2="{Y(y)}" stroke="{GRID}" stroke-width="0.5"/>')
    o.append(f'<line x1="{X(x0)}" y1="{Y(0)}" x2="{X(x1)}" y2="{Y(0)}" stroke="{EJE}" stroke-width="1.2"/>')
    o.append(f'<line x1="{X(0)}" y1="{Y(y1)}" x2="{X(0)}" y2="{Y(y0)}" stroke="{EJE}" stroke-width="1.2"/>')
    # números de los ejes
    for x in range(x0 + 1, x1):
        if x:
            o.append(f'<line x1="{X(x)}" y1="{Y(0) - 2.5}" x2="{X(x)}" y2="{Y(0) + 2.5}" stroke="{EJE}" stroke-width="1"/>')
            o.append(f'<text x="{X(x)}" y="{Y(0) + 11}" text-anchor="middle" font-size="8" fill="{EJE}">{x}</text>')
    for y in range(y0 + 1, y1):
        if y:
            o.append(f'<line x1="{X(0) - 2.5}" y1="{Y(y)}" x2="{X(0) + 2.5}" y2="{Y(y)}" stroke="{EJE}" stroke-width="1"/>')
            o.append(f'<text x="{X(0) - 5}" y="{Y(y) + 3}" text-anchor="end" font-size="8" fill="{EJE}">{y}</text>')
    # tramos
    for v, a, b, cerrado in tramos:
        o.append(f'<line x1="{X(a)}" y1="{Y(v)}" x2="{X(b)}" y2="{Y(v)}" stroke="{MAG}" stroke-width="2.2"/>')
    for v, a, b, cerrado in tramos:
        for x in (a, b):
            if cerrado:
                o.append(f'<circle cx="{X(x)}" cy="{Y(v)}" r="3.4" fill="{PUNTO}"/>')
            else:
                o.append(f'<circle cx="{X(x)}" cy="{Y(v)}" r="3.2" fill="#FFFFFF" stroke="{PUNTO}" stroke-width="1.4"/>')
    o.append('</svg>')
    return "".join(o)
