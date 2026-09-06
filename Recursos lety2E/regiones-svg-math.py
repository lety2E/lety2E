"""Plano con una recta y la región solución sombreada (desigualdades de dos variables).

La recta va sólida, como en el cuaderno de Lety. El sombreado usa magenta al 15%,
la misma convención que los triángulos del proyecto.
"""
U = 20
PAD = 12
RECTA = "#FF00AA"

def _clip_semiplano(poly, m, b, arriba):
    """Sutherland-Hodgman contra y >= mx+b (o y <= mx+b)."""
    def dentro(p):
        v = p[1] - (m * p[0] + b)
        return v >= -1e-9 if arriba else v <= 1e-9
    def corte(p, q):
        # parametriza p->q y busca donde y = m x + b
        dx, dy = q[0] - p[0], q[1] - p[1]
        den = dy - m * dx
        t = (m * p[0] + b - p[1]) / den if abs(den) > 1e-12 else 0
        return (p[0] + t * dx, p[1] + t * dy)
    out = []
    for i in range(len(poly)):
        a, c = poly[i], poly[(i + 1) % len(poly)]
        if dentro(a):
            out.append(a)
            if not dentro(c): out.append(corte(a, c))
        elif dentro(c):
            out.append(corte(a, c))
    return out

def region(m, b, xr, yr, arriba, pruebas):
    m, b = float(m), float(b)
    """pruebas: [((x, y), cumple)] — se marcan como puntos."""
    x0, x1 = xr; y0, y1 = yr
    W = (x1 - x0) * U + 2 * PAD
    H = (y1 - y0) * U + 2 * PAD
    X = lambda x: PAD + (x - x0) * U
    Y = lambda y: PAD + (y1 - y) * U

    s = [f'<svg class="graf-svg" viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W:.0f}" height="{H:.0f}" role="img" aria-label="Región solución de la desigualdad">']
    poly = _clip_semiplano([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], m, b, arriba)
    if poly:
        pts = " ".join(f"{X(px):.1f},{Y(py):.1f}" for px, py in poly)
        s.append(f'<polygon points="{pts}" fill="{RECTA}" fill-opacity="0.15"/>')
    for i in range(x0, x1 + 1):
        s.append(f'<line x1="{X(i)}" y1="{PAD}" x2="{X(i)}" y2="{H-PAD:.0f}" stroke="#E0C4BC" stroke-width="0.5"/>')
    for j in range(y0, y1 + 1):
        s.append(f'<line x1="{PAD}" y1="{Y(j)}" x2="{W-PAD:.0f}" y2="{Y(j)}" stroke="#E0C4BC" stroke-width="0.5"/>')
    if y0 <= 0 <= y1:
        s.append(f'<line x1="{PAD}" y1="{Y(0)}" x2="{W-PAD:.0f}" y2="{Y(0)}" stroke="#7B5A50" stroke-width="1.2"/>')
    if x0 <= 0 <= x1:
        s.append(f'<line x1="{X(0)}" y1="{PAD}" x2="{X(0)}" y2="{H-PAD:.0f}" stroke="#7B5A50" stroke-width="1.2"/>')
    # recta, recortada al marco
    pts = []
    for x in (x0, x1):
        y = m * x + b
        if y0 <= y <= y1: pts.append((x, y))
    if m != 0:
        for y in (y0, y1):
            x = (y - b) / m
            if x0 <= x <= x1: pts.append((x, y))
    pts = sorted(set((round(p, 6), round(q, 6)) for p, q in pts))
    if len(pts) >= 2:
        (ax, ay), (bx, by) = pts[0], pts[-1]
        s.append(f'<line x1="{X(ax):.1f}" y1="{Y(ay):.1f}" x2="{X(bx):.1f}" y2="{Y(by):.1f}" '
                 f'stroke="{RECTA}" stroke-width="2.2" stroke-linecap="round"/>')
    for (px, py), cumple in pruebas:
        col = "#4A0080" if cumple else "#1A0828"
        s.append(f'<circle cx="{X(px)}" cy="{Y(py)}" r="3.4" fill="{col}"/>')
        if cumple:
            s.append(f'<circle cx="{X(px)}" cy="{Y(py)}" r="6" fill="none" stroke="{col}" stroke-width="1.2"/>')
    s.append('</svg>')
    return "".join(s)
