"""Genera SVG inline de dos rectas en el mismo plano (metodo grafico, Math 3).
Reglas de CLAUDE.md: 1 cuadro = 1 unidad, grid #E0C4BC 0.5, ejes #7B5A50 1.2,
rectas 2.2, puntos #1A0828 r=3."""
from fractions import Fraction as F

U = 22          # px por unidad
PAD = 10
C1, C2 = "#7B2CBF", "#FF00AA"   # recta 1 morado (columna izq), recta 2 magenta (der)

def _clip(m, b, x0, x1, y0, y1):
    """Segmento de y = b + m x recortado a la ventana."""
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

def grafica(rectas, punto, xr, yr):
    """rectas: [(m, b), (m, b)] con y = b + m x. punto: (x, y) interseccion."""
    x0, x1 = xr; y0, y1 = yr
    W = (x1 - x0) * U + 2 * PAD
    H = (y1 - y0) * U + 2 * PAD
    X = lambda x: PAD + (x - x0) * U
    Y = lambda y: PAD + (y1 - y) * U

    s = [f'<svg class="graf-svg" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W}" height="{H}" role="img" aria-label="Rectas del sistema y su punto de corte">']
    # grid
    for i in range(x0, x1 + 1):
        s.append(f'<line x1="{X(i)}" y1="{PAD}" x2="{X(i)}" y2="{H-PAD}" stroke="#E0C4BC" stroke-width="0.5"/>')
    for j in range(y0, y1 + 1):
        s.append(f'<line x1="{PAD}" y1="{Y(j)}" x2="{W-PAD}" y2="{Y(j)}" stroke="#E0C4BC" stroke-width="0.5"/>')
    # ejes
    if y0 <= 0 <= y1:
        s.append(f'<line x1="{PAD}" y1="{Y(0)}" x2="{W-PAD}" y2="{Y(0)}" stroke="#7B5A50" stroke-width="1.2"/>')
    if x0 <= 0 <= x1:
        s.append(f'<line x1="{X(0)}" y1="{PAD}" x2="{X(0)}" y2="{H-PAD}" stroke="#7B5A50" stroke-width="1.2"/>')
    # rectas
    for (m, b), col in zip(rectas, (C1, C2)):
        seg = _clip(float(m), float(b), x0, x1, y0, y1)
        if seg:
            (ax, ay), (bx, by) = seg
            s.append(f'<line x1="{X(ax):.1f}" y1="{Y(ay):.1f}" x2="{X(bx):.1f}" y2="{Y(by):.1f}" '
                     f'stroke="{col}" stroke-width="2.2" stroke-linecap="round"/>')
    # punto de corte
    px, py = punto
    s.append(f'<circle cx="{X(px)}" cy="{Y(py)}" r="5.5" fill="none" stroke="#1A0828" stroke-width="1.2"/>')
    s.append(f'<circle cx="{X(px)}" cy="{Y(py)}" r="3" fill="#1A0828"/>')
    s.append('</svg>')
    return "".join(s)
