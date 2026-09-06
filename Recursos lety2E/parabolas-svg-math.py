"""SVG inline de parábolas para Math 3 (gráfica de una ecuación cuadrática).

Sigue las reglas de CLAUDE.md: grid #E0C4BC 0.5, ejes #7B5A50 1.2, curva 2.2 magenta,
puntos #1A0828 r=3. Cuando el rango en y es grande, el grid se marca cada `paso_y`
unidades — igual que en el cuaderno de Lety, que rotula de 5 en 5 en esos casos.
"""
ANCHO_MAX, ALTO_MAX = 250.0, 360.0
PAD = 12
CURVA = "#FF00AA"

def parabola(h, k, puntos, xr, yr, paso_x=1, paso_y=1, a=1):
    """y = a(x-h)^2 + k ; puntos: [(x, y)] de la tabla."""
    x0, x1 = xr; y0, y1 = yr
    ux = min(ANCHO_MAX / (x1 - x0), 26)
    uy = min(ALTO_MAX / (y1 - y0), ux)
    W = (x1 - x0) * ux + 2 * PAD
    H = (y1 - y0) * uy + 2 * PAD
    X = lambda x: PAD + (x - x0) * ux
    Y = lambda y: PAD + (y1 - y) * uy

    s = [f'<svg class="graf-svg" viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W:.0f}" height="{H:.0f}" role="img" aria-label="Parábola con su vértice y los puntos de la tabla">']
    i = x0 - (x0 % paso_x)
    while i <= x1:
        s.append(f'<line x1="{X(i):.1f}" y1="{PAD}" x2="{X(i):.1f}" y2="{H-PAD:.1f}" stroke="#E0C4BC" stroke-width="0.5"/>')
        i += paso_x
    j = y0 - (y0 % paso_y)
    while j <= y1:
        s.append(f'<line x1="{PAD}" y1="{Y(j):.1f}" x2="{W-PAD:.1f}" y2="{Y(j):.1f}" stroke="#E0C4BC" stroke-width="0.5"/>')
        j += paso_y
    if y0 <= 0 <= y1:
        s.append(f'<line x1="{PAD}" y1="{Y(0):.1f}" x2="{W-PAD:.1f}" y2="{Y(0):.1f}" stroke="#7B5A50" stroke-width="1.2"/>')
    if x0 <= 0 <= x1:
        s.append(f'<line x1="{X(0):.1f}" y1="{PAD}" x2="{X(0):.1f}" y2="{H-PAD:.1f}" stroke="#7B5A50" stroke-width="1.2"/>')

    # curva (muestreo fino, recortada a la ventana)
    d, dentro = [], False
    n = 240
    for t in range(n + 1):
        x = x0 + (x1 - x0) * t / n
        y = a * (x - h) ** 2 + k
        if y0 <= y <= y1:
            d.append(("L" if dentro else "M") + f"{X(x):.1f},{Y(y):.1f}")
            dentro = True
        else:
            dentro = False
    s.append(f'<path d="{" ".join(d)}" fill="none" stroke="{CURVA}" stroke-width="2.2" stroke-linecap="round"/>')

    for px, py in puntos:
        s.append(f'<circle cx="{X(px):.1f}" cy="{Y(py):.1f}" r="3" fill="#1A0828"/>')
    # vértice resaltado
    s.append(f'<circle cx="{X(h):.1f}" cy="{Y(k):.1f}" r="5.5" fill="none" stroke="#1A0828" stroke-width="1.2"/>')
    s.append('</svg>')
    return "".join(s)


def parabola_foco(h, k, p, arriba, xr, yr, puntos=(), paso_x=1, paso_y=1):
    """(x-h)^2 = ±4p(y-k): dibuja la curva con su vértice, foco y directriz."""
    a = (1 if arriba else -1) / (4.0 * p)
    x0, x1 = xr; y0, y1 = yr
    ux = min(ANCHO_MAX / (x1 - x0), 26)
    uy = min(ALTO_MAX / (y1 - y0), ux)
    W = (x1 - x0) * ux + 2 * PAD
    H = (y1 - y0) * uy + 2 * PAD
    X = lambda x: PAD + (x - x0) * ux
    Y = lambda y: PAD + (y1 - y) * uy
    dir_y = k - p if arriba else k + p
    foco = (h, k + p) if arriba else (h, k - p)

    s = [f'<svg class="graf-svg" viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W:.0f}" height="{H:.0f}" role="img" aria-label="Parábola con su vértice, foco y directriz">']
    i = x0 - (x0 % paso_x)
    while i <= x1:
        s.append(f'<line x1="{X(i):.1f}" y1="{PAD}" x2="{X(i):.1f}" y2="{H-PAD:.1f}" stroke="#E0C4BC" stroke-width="0.5"/>')
        i += paso_x
    j = y0 - (y0 % paso_y)
    while j <= y1:
        s.append(f'<line x1="{PAD}" y1="{Y(j):.1f}" x2="{W-PAD:.1f}" y2="{Y(j):.1f}" stroke="#E0C4BC" stroke-width="0.5"/>')
        j += paso_y
    if y0 <= 0 <= y1:
        s.append(f'<line x1="{PAD}" y1="{Y(0):.1f}" x2="{W-PAD:.1f}" y2="{Y(0):.1f}" stroke="#7B5A50" stroke-width="1.2"/>')
    if x0 <= 0 <= x1:
        s.append(f'<line x1="{X(0):.1f}" y1="{PAD}" x2="{X(0):.1f}" y2="{H-PAD:.1f}" stroke="#7B5A50" stroke-width="1.2"/>')
    # directriz
    if y0 <= dir_y <= y1:
        s.append(f'<line x1="{PAD}" y1="{Y(dir_y):.1f}" x2="{W-PAD:.1f}" y2="{Y(dir_y):.1f}" '
                 f'stroke="#4A0080" stroke-width="1.6" stroke-dasharray="5 4"/>')
    # curva
    d, dentro = [], False
    n = 240
    for t in range(n + 1):
        x = x0 + (x1 - x0) * t / n
        y = a * (x - h) ** 2 + k
        if y0 <= y <= y1:
            d.append(("L" if dentro else "M") + f"{X(x):.1f},{Y(y):.1f}")
            dentro = True
        else:
            dentro = False
    s.append(f'<path d="{" ".join(d)}" fill="none" stroke="{CURVA}" stroke-width="2.2" stroke-linecap="round"/>')
    for px, py in puntos:
        s.append(f'<circle cx="{X(px):.1f}" cy="{Y(py):.1f}" r="3" fill="#1A0828"/>')
    s.append(f'<circle cx="{X(foco[0]):.1f}" cy="{Y(foco[1]):.1f}" r="3.6" fill="#4A0080"/>')
    s.append(f'<circle cx="{X(h):.1f}" cy="{Y(k):.1f}" r="5.5" fill="none" stroke="#1A0828" stroke-width="1.4"/>')
    s.append('</svg>')
    return "".join(s)
