"""SVG inline de puntos sueltos con su recta guía (Math 4, representación de funciones).

La recta va **punteada** a propósito: el dominio son sólo los puntos de la tabla,
la recta no es la gráfica de la función, es la guía que los alinea.

Reglas de CLAUDE.md: 1 cuadro = 1 unidad, grid #E0C4BC 0.5, ejes #7B5A50 1.2,
recta #FF00AA 2.2, puntos #1A0828 r=3.
"""
U = 20          # px por unidad
PAD = 9
RECTA = "#FF00AA"

def rango(vals, minimo=4):
    """Ventana entera que cubre los valores, con margen 1 y el 0 siempre dentro."""
    lo, hi = min(list(vals) + [0]) - 1, max(list(vals) + [0]) + 1
    while hi - lo < minimo:
        lo -= 1; hi += 1
    return lo, hi

def _clip(m, b, x0, x1, y0, y1):
    pts = []
    for x in (x0, x1):
        y = b + m * x
        if y0 - 1e-9 <= y <= y1 + 1e-9: pts.append((x, y))
    if m != 0:
        for y in (y0, y1):
            x = (y - b) / m
            if x0 - 1e-9 <= x <= x1 + 1e-9: pts.append((x, y))
    pts = sorted(set((round(p, 6), round(q, 6)) for p, q in pts))
    return (pts[0], pts[-1]) if len(pts) >= 2 else None

def grafica(puntos, m, b, etiqueta="Puntos de la tabla y la recta que los alinea"):
    """puntos: [(x, y), ...]. m, b: la recta y = m x + b que pasa por ellos."""
    x0, x1 = rango([p[0] for p in puntos])
    y0, y1 = rango([p[1] for p in puntos])
    W = (x1 - x0) * U + 2 * PAD
    H = (y1 - y0) * U + 2 * PAD
    X = lambda x: PAD + (x - x0) * U
    Y = lambda y: PAD + (y1 - y) * U

    s = [f'<svg class="graf-svg" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W}" height="{H}" role="img" aria-label="{etiqueta}">']
    for i in range(x0, x1 + 1):
        s.append(f'<line x1="{X(i)}" y1="{PAD}" x2="{X(i)}" y2="{H-PAD}" stroke="#E0C4BC" stroke-width="0.5"/>')
    for j in range(y0, y1 + 1):
        s.append(f'<line x1="{PAD}" y1="{Y(j)}" x2="{W-PAD}" y2="{Y(j)}" stroke="#E0C4BC" stroke-width="0.5"/>')
    s.append(f'<line x1="{PAD}" y1="{Y(0)}" x2="{W-PAD}" y2="{Y(0)}" stroke="#7B5A50" stroke-width="1.2"/>')
    s.append(f'<line x1="{X(0)}" y1="{PAD}" x2="{X(0)}" y2="{H-PAD}" stroke="#7B5A50" stroke-width="1.2"/>')

    seg = _clip(float(m), float(b), x0, x1, y0, y1)
    if seg:
        (ax, ay), (bx, by) = seg
        s.append(f'<line x1="{X(ax):.1f}" y1="{Y(ay):.1f}" x2="{X(bx):.1f}" y2="{Y(by):.1f}" '
                 f'stroke="{RECTA}" stroke-width="2.2" stroke-linecap="round" stroke-dasharray="5 4" opacity="0.75"/>')
    for px, py in puntos:
        s.append(f'<circle cx="{X(px)}" cy="{Y(py)}" r="3" fill="#1A0828"/>')
    s.append('</svg>')
    return "".join(s)

def sagital(pares, dom_t="Dom", ran_t="Ran"):
    """Diagrama sagital: dos óvalos con flechas de dominio a rango."""
    n = len(pares)
    H = 34 + n * 26
    W = 190
    cx1, cx2 = 46, 144
    ry = 14 + n * 12
    cy = H / 2
    s = [f'<svg class="graf-svg sagital" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W}" height="{H}" role="img" aria-label="Diagrama sagital de la función">']
    s.append(f'<text x="{cx1}" y="13" text-anchor="middle" font-size="11" fill="#7B2CBF">{dom_t}</text>')
    s.append(f'<text x="{cx2}" y="13" text-anchor="middle" font-size="11" fill="#FF00AA">{ran_t}</text>')
    s.append(f'<ellipse cx="{cx1}" cy="{cy+6}" rx="26" ry="{ry}" fill="none" stroke="#7B2CBF" stroke-width="1.2"/>')
    s.append(f'<ellipse cx="{cx2}" cy="{cy+6}" rx="26" ry="{ry}" fill="none" stroke="#FF00AA" stroke-width="1.2"/>')
    y0 = cy + 6 - (n - 1) * 13
    for i, (a, b) in enumerate(pares):
        y = y0 + i * 26
        s.append(f'<text x="{cx1}" y="{y+4}" text-anchor="middle" font-size="12" fill="#1A0828">{a}</text>')
        s.append(f'<text x="{cx2}" y="{y+4}" text-anchor="middle" font-size="12" fill="#1A0828">{b}</text>')
        s.append(f'<line x1="{cx1+16}" y1="{y}" x2="{cx2-18}" y2="{y}" stroke="#7B5A50" stroke-width="1" '
                 f'marker-end="url(#fl)"/>')
    s.insert(1, '<defs><marker id="fl" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" '
                'orient="auto"><path d="M0 1 L7 4 L0 7 z" fill="#7B5A50"/></marker></defs>')
    s.append('</svg>')
    return "".join(s)
