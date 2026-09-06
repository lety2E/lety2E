"""Circunferencia en el plano (Math 3): centro, radio y los cuatro puntos extremos.
Relleno magenta al 15% + contorno sólido, la misma convención que los triángulos.
"""
U = 15
PAD = 14
MAG = "#FF00AA"

def circulo(h, k, r, xr, yr, punto=None):
    x0, x1 = xr; y0, y1 = yr
    W = (x1 - x0) * U + 2 * PAD
    H = (y1 - y0) * U + 2 * PAD
    X = lambda x: PAD + (x - x0) * U
    Y = lambda y: PAD + (y1 - y) * U
    s = [f'<svg class="graf-svg" viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W:.0f}" height="{H:.0f}" role="img" aria-label="Circunferencia con su centro y su radio">']
    for i in range(x0, x1 + 1):
        s.append(f'<line x1="{X(i)}" y1="{PAD}" x2="{X(i)}" y2="{H-PAD:.0f}" stroke="#E0C4BC" stroke-width="0.5"/>')
    for j in range(y0, y1 + 1):
        s.append(f'<line x1="{PAD}" y1="{Y(j)}" x2="{W-PAD:.0f}" y2="{Y(j)}" stroke="#E0C4BC" stroke-width="0.5"/>')
    if y0 <= 0 <= y1:
        s.append(f'<line x1="{PAD}" y1="{Y(0)}" x2="{W-PAD:.0f}" y2="{Y(0)}" stroke="#7B5A50" stroke-width="1.2"/>')
    if x0 <= 0 <= x1:
        s.append(f'<line x1="{X(0)}" y1="{PAD}" x2="{X(0)}" y2="{H-PAD:.0f}" stroke="#7B5A50" stroke-width="1.2"/>')
    s.append(f'<circle cx="{X(h)}" cy="{Y(k)}" r="{r*U}" fill="{MAG}" fill-opacity="0.15" '
             f'stroke="{MAG}" stroke-width="2.2"/>')
    # radios
    s.append(f'<line x1="{X(h-r)}" y1="{Y(k)}" x2="{X(h+r)}" y2="{Y(k)}" stroke="{MAG}" stroke-width="1"/>')
    s.append(f'<line x1="{X(h)}" y1="{Y(k-r)}" x2="{X(h)}" y2="{Y(k+r)}" stroke="{MAG}" stroke-width="1"/>')
    for px, py in ((h-r, k), (h+r, k), (h, k-r), (h, k+r)):
        s.append(f'<circle cx="{X(px)}" cy="{Y(py)}" r="2.6" fill="#1A0828"/>')
    s.append(f'<circle cx="{X(h)}" cy="{Y(k)}" r="3.4" fill="#4A0080"/>')
    if punto:
        s.append(f'<circle cx="{X(punto[0])}" cy="{Y(punto[1])}" r="5.5" fill="none" '
                 f'stroke="#4A0080" stroke-width="1.6"/>')
    s.append('</svg>')
    return "".join(s)
