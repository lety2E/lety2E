"""Elipse en el plano (Math 3): centro, vértices, focos y los dos ejes.

Misma convención que la circunferencia: relleno magenta al 15% + contorno sólido,
grid #E0C4BC, ejes #7B5A50. Los vértices van en negro y los focos en morado, para
que se distingan de un vistazo.
"""
U = 15
PAD = 14
MAG = "#FF00AA"
FOCO = "#4A0080"

def elipse(h, k, a, b, horiz, xr, yr, punto=None, triangulo=False):
    """a = semieje mayor, b = semieje menor, horiz = eje mayor sobre x."""
    rx, ry = (a, b) if horiz else (b, a)
    x0, x1 = xr; y0, y1 = yr
    W = (x1 - x0) * U + 2 * PAD
    H = (y1 - y0) * U + 2 * PAD
    X = lambda v: PAD + (v - x0) * U
    Y = lambda v: PAD + (y1 - v) * U
    c = (a * a - b * b) ** 0.5

    s = [f'<svg class="graf-svg" viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W:.0f}" height="{H:.0f}" role="img" '
         f'aria-label="Elipse con su centro, sus vértices y sus focos">']
    for i in range(x0, x1 + 1):
        s.append(f'<line x1="{X(i)}" y1="{PAD}" x2="{X(i)}" y2="{H-PAD:.0f}" stroke="#E0C4BC" stroke-width="0.5"/>')
    for j in range(y0, y1 + 1):
        s.append(f'<line x1="{PAD}" y1="{Y(j)}" x2="{W-PAD:.0f}" y2="{Y(j)}" stroke="#E0C4BC" stroke-width="0.5"/>')
    if y0 <= 0 <= y1:
        s.append(f'<line x1="{PAD}" y1="{Y(0)}" x2="{W-PAD:.0f}" y2="{Y(0)}" stroke="#7B5A50" stroke-width="1.2"/>')
    if x0 <= 0 <= x1:
        s.append(f'<line x1="{X(0)}" y1="{PAD}" x2="{X(0)}" y2="{H-PAD:.0f}" stroke="#7B5A50" stroke-width="1.2"/>')

    s.append(f'<ellipse cx="{X(h)}" cy="{Y(k)}" rx="{rx*U}" ry="{ry*U}" '
             f'fill="{MAG}" fill-opacity="0.15" stroke="{MAG}" stroke-width="2.2"/>')
    # ejes mayor y menor
    s.append(f'<line x1="{X(h-rx)}" y1="{Y(k)}" x2="{X(h+rx)}" y2="{Y(k)}" stroke="{MAG}" stroke-width="1"/>')
    s.append(f'<line x1="{X(h)}" y1="{Y(k-ry)}" x2="{X(h)}" y2="{Y(k+ry)}" stroke="{MAG}" stroke-width="1"/>')
    # vértices (extremos del eje mayor) y extremos del menor
    v = [(h - a, k), (h + a, k)] if horiz else [(h, k - a), (h, k + a)]
    w = [(h, k - b), (h, k + b)] if horiz else [(h - b, k), (h + b, k)]
    for px, py in w:
        s.append(f'<circle cx="{X(px)}" cy="{Y(py)}" r="2.4" fill="#1A0828" fill-opacity="0.55"/>')
    for px, py in v:
        s.append(f'<circle cx="{X(px)}" cy="{Y(py)}" r="3.2" fill="#1A0828"/>')
    # focos
    f = [(h - c, k), (h + c, k)] if horiz else [(h, k - c), (h, k + c)]
    for px, py in f:
        s.append(f'<circle cx="{X(px)}" cy="{Y(py)}" r="3.4" fill="{FOCO}"/>')
    s.append(f'<circle cx="{X(h)}" cy="{Y(k)}" r="2.8" fill="none" stroke="{FOCO}" stroke-width="1.4"/>')
    if triangulo:
        """El mismo triángulo del apunte, con los números de este ejercicio:
           catetos b y c, hipotenusa a."""
        if horiz: v1, v2 = (h, k + b), (h + c, k)
        else:     v1, v2 = (h + b, k), (h, k + c)
        s.append(f'<polygon points="{X(h)},{Y(k)} {X(v1[0])},{Y(v1[1])} {X(v2[0])},{Y(v2[1])}" '
                 f'fill="{FOCO}" fill-opacity="0.12" stroke="{FOCO}" stroke-width="1.6"/>')
        d = 0.34 * U
        dx, dy = (0, -d) if horiz else (d, 0)
        s.append(f'<path d="M{X(h)+(d if horiz else 0)},{Y(k)+(0 if horiz else -d)} '
                 f'l{0 if horiz else d},{-d if horiz else 0} l{-d if horiz else 0},{0 if horiz else d}" '
                 f'fill="none" stroke="{FOCO}" stroke-width="1.1"/>')
        T = lambda xx, yy, t, col: (f'<text x="{xx:.1f}" y="{yy:.1f}" font-size="12" fill="{col}" '
                                    f'text-anchor="middle" font-weight="700" font-style="italic" '
                                    f'font-family="system-ui, sans-serif">{t}</text>')
        if horiz:
            s.append(T(X(h) - 11, Y(k + b / 2) + 4, "b", FOCO))
            s.append(T(X(h + c / 2), Y(k) - 7, "c", FOCO))
            s.append(T(X(h + c / 2) + 16, Y(k + b / 2) - 4, "a", MAG))
        else:
            s.append(T(X(h + b / 2), Y(k) - 7, "b", FOCO))
            s.append(T(X(h) - 11, Y(k + c / 2) + 4, "c", FOCO))
            s.append(T(X(h + b / 2) + 14, Y(k + c / 2) - 2, "a", MAG))
    if punto:
        s.append(f'<circle cx="{X(punto[0])}" cy="{Y(punto[1])}" r="6" fill="none" '
                 f'stroke="{FOCO}" stroke-width="1.6"/>')
    s.append('</svg>')
    return "".join(s)


def apunte_elipse(a=5, b=4, c=3, U2=26):
    """Elipse genérica con a, b y c rotulados y el triángulo rectángulo que forman.

    El triángulo va del centro al extremo del eje menor (cateto b), del centro al
    foco (cateto c), y la hipotenusa que los cierra mide exactamente a — que es lo
    que hace visible a² = b² + c².
    """
    x0, x1, y0, y1 = -(a + 1), a + 1, -(b + 1), b + 1
    P = 16
    W = (x1 - x0) * U2 + 2 * P
    H = (y1 - y0) * U2 + 2 * P
    X = lambda v: P + (v - x0) * U2
    Y = lambda v: P + (y1 - v) * U2
    T = lambda x, y, t, col, anchor="middle", sz=13, w=700: (
        f'<text x="{x:.1f}" y="{y:.1f}" font-size="{sz}" fill="{col}" text-anchor="{anchor}" '
        f'font-weight="{w}" font-family="system-ui, sans-serif" font-style="italic">{t}</text>')

    s = [f'<svg class="apunte-svg" viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W:.0f}" height="{H:.0f}" role="img" '
         f'aria-label="Elipse con los segmentos a, b y c formando un triángulo rectángulo">']
    for i in range(x0, x1 + 1):
        s.append(f'<line x1="{X(i)}" y1="{P}" x2="{X(i)}" y2="{H-P:.0f}" stroke="#E0C4BC" stroke-width="0.5"/>')
    for j in range(y0, y1 + 1):
        s.append(f'<line x1="{P}" y1="{Y(j)}" x2="{W-P:.0f}" y2="{Y(j)}" stroke="#E0C4BC" stroke-width="0.5"/>')
    s.append(f'<line x1="{P}" y1="{Y(0)}" x2="{W-P:.0f}" y2="{Y(0)}" stroke="#7B5A50" stroke-width="1.2"/>')
    s.append(f'<line x1="{X(0)}" y1="{P}" x2="{X(0)}" y2="{H-P:.0f}" stroke="#7B5A50" stroke-width="1.2"/>')
    s.append(f'<ellipse cx="{X(0)}" cy="{Y(0)}" rx="{a*U2}" ry="{b*U2}" fill="none" '
             f'stroke="{MAG}" stroke-width="2.2"/>')

    # triángulo rectángulo: centro → (0, b) → (c, 0)
    s.append(f'<polygon points="{X(0)},{Y(0)} {X(0)},{Y(b)} {X(c)},{Y(0)}" '
             f'fill="{MAG}" fill-opacity="0.15" stroke="{FOCO}" stroke-width="1.8"/>')
    # marca de ángulo recto
    d = 0.32 * U2
    s.append(f'<path d="M{X(0)+d},{Y(0)} L{X(0)+d},{Y(0)-d} L{X(0)},{Y(0)-d}" fill="none" '
             f'stroke="{FOCO}" stroke-width="1.2"/>')

    # semieje mayor a (del centro al vértice), por debajo del eje
    s.append(f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(a)}" y2="{Y(0)}" stroke="{MAG}" stroke-width="2.6"/>')
    s.append(T(X(a * 0.82), Y(0) + 17, "a", MAG))
    # cateto b
    s.append(T(X(0) - 12, Y(b/2) + 5, "b", FOCO, anchor="end"))
    # cateto c
    s.append(T(X(c/2), Y(0) - 9, "c", FOCO))
    # hipotenusa = a
    s.append(T((X(0) + X(c)) / 2 + 20, (Y(b) + Y(0)) / 2 - 6, "a", MAG))

    # puntos
    s.append(f'<circle cx="{X(a)}" cy="{Y(0)}" r="3.4" fill="#1A0828"/>')
    s.append(f'<circle cx="{X(-a)}" cy="{Y(0)}" r="3.4" fill="#1A0828"/>')
    s.append(f'<circle cx="{X(0)}" cy="{Y(b)}" r="3" fill="#1A0828" fill-opacity="0.55"/>')
    s.append(f'<circle cx="{X(0)}" cy="{Y(-b)}" r="3" fill="#1A0828" fill-opacity="0.55"/>')
    s.append(f'<circle cx="{X(c)}" cy="{Y(0)}" r="3.8" fill="{FOCO}"/>')
    s.append(f'<circle cx="{X(-c)}" cy="{Y(0)}" r="3.8" fill="{FOCO}"/>')
    s.append(f'<circle cx="{X(0)}" cy="{Y(0)}" r="2.8" fill="none" stroke="{FOCO}" stroke-width="1.4"/>')
    # rótulos de vértice y foco
    s.append(T(X(a), Y(0) + 34, "vértice", "#6E4F4F", sz=9.5, w=500))
    s.append(T(X(c), Y(0) + 34, "foco", FOCO, sz=9.5, w=600))
    s.append('</svg>')
    return "".join(s)


def puntos_elipse(h, k, a, c, horiz, xr, yr):
    """Sólo los datos en el plano: centro, vértices y focos, con a y c medidos.

    Va antes de calcular b: la curva todavía no se puede trazar, pero a y c ya se
    cuentan en los cuadros.
    """
    x0, x1 = xr; y0, y1 = yr
    W = (x1 - x0) * U + 2 * PAD
    H = (y1 - y0) * U + 2 * PAD
    X = lambda v: PAD + (v - x0) * U
    Y = lambda v: PAD + (y1 - v) * U
    T = lambda xx, yy, t, col, sz=12, w=700: (
        f'<text x="{xx:.1f}" y="{yy:.1f}" font-size="{sz}" fill="{col}" text-anchor="middle" '
        f'font-weight="{w}" font-style="italic" font-family="system-ui, sans-serif">{t}</text>')

    s = [f'<svg class="graf-svg" viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W:.0f}" height="{H:.0f}" role="img" '
         f'aria-label="Centro, vértices y focos ubicados en el plano, con a y c medidos">']
    for i in range(x0, x1 + 1):
        s.append(f'<line x1="{X(i)}" y1="{PAD}" x2="{X(i)}" y2="{H-PAD:.0f}" stroke="#E0C4BC" stroke-width="0.5"/>')
    for j in range(y0, y1 + 1):
        s.append(f'<line x1="{PAD}" y1="{Y(j)}" x2="{W-PAD:.0f}" y2="{Y(j)}" stroke="#E0C4BC" stroke-width="0.5"/>')
    if y0 <= 0 <= y1:
        s.append(f'<line x1="{PAD}" y1="{Y(0)}" x2="{W-PAD:.0f}" y2="{Y(0)}" stroke="#7B5A50" stroke-width="1.2"/>')
    if x0 <= 0 <= x1:
        s.append(f'<line x1="{X(0)}" y1="{PAD}" x2="{X(0)}" y2="{H-PAD:.0f}" stroke="#7B5A50" stroke-width="1.2"/>')

    v = [(h - a, k), (h + a, k)] if horiz else [(h, k - a), (h, k + a)]
    f = [(h - c, k), (h + c, k)] if horiz else [(h, k - c), (h, k + c)]

    def cota(p1, p2, off, col, etiq):
        """Acotación separada del eje, con ganchos en los extremos — como la traza
        Lety a mano, para que la medida no se encime con los puntos ni con el eje."""
        g = 0.42
        if horiz:
            yy = k + off
            s.append(f'<line x1="{X(p1)}" y1="{Y(yy)}" x2="{X(p2)}" y2="{Y(yy)}" '
                     f'stroke="{col}" stroke-width="1.6"/>')
            for xx in (p1, p2):
                s.append(f'<line x1="{X(xx)}" y1="{Y(yy)}" x2="{X(xx)}" y2="{Y(yy - g if off > 0 else yy + g)}" '
                         f'stroke="{col}" stroke-width="1.6"/>')
            s.append(T((X(p1) + X(p2)) / 2, Y(yy) + (-6 if off > 0 else 15), etiq, col))
        else:
            xx = h + off
            s.append(f'<line x1="{X(xx)}" y1="{Y(p1)}" x2="{X(xx)}" y2="{Y(p2)}" '
                     f'stroke="{col}" stroke-width="1.6"/>')
            for yy in (p1, p2):
                s.append(f'<line x1="{X(xx)}" y1="{Y(yy)}" x2="{X(xx - g if off > 0 else xx + g)}" y2="{Y(yy)}" '
                         f'stroke="{col}" stroke-width="1.6"/>')
            s.append(T(X(xx) + (13 if off > 0 else -13), (Y(p1) + Y(p2)) / 2 + 4, etiq, col))

    if horiz:
        cota(h, h + a, -1.35, MAG, "a")     # a, por debajo del eje
        cota(h, h + c, 1.35, FOCO, "c")     # c, por encima
    else:
        cota(k, k + a, 1.35, MAG, "a")      # a, a la derecha del eje
        cota(k, k + c, -1.35, FOCO, "c")    # c, a la izquierda

    for px, py in f:
        s.append(f'<circle cx="{X(px)}" cy="{Y(py)}" r="3.8" fill="{FOCO}"/>')
    for px, py in v:
        s.append(f'<circle cx="{X(px)}" cy="{Y(py)}" r="3.4" fill="#1A0828"/>')
    s.append(f'<circle cx="{X(h)}" cy="{Y(k)}" r="2.8" fill="none" stroke="{FOCO}" stroke-width="1.4"/>')
    s.append('</svg>')
    return "".join(s)
