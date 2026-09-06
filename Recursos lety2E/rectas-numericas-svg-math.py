"""Recta numérica con intervalo sombreado (desigualdades, Math 3).

Punto abierto = círculo con relleno del fondo; cerrado = relleno sólido.
Colores del sitio: trazo del intervalo magenta, eje y marcas #7B5A50.
"""
U = 26
PAD_X, ALTO = 22, 56
EJE_Y = 30
MAG = "#FF00AA"

def recta(x0, x1, marcas, ini=None, fin=None, cerrado_ini=False, cerrado_fin=False):
    """ini/fin: extremos del intervalo (None = infinito, con flecha)."""
    W = (x1 - x0) * U + 2 * PAD_X
    X = lambda v: PAD_X + (v - x0) * U
    s = [f'<svg class="recta-svg" viewBox="0 0 {W} {ALTO}" xmlns="http://www.w3.org/2000/svg" '
         f'width="{W}" height="{ALTO}" role="img" aria-label="Recta numérica con el intervalo solución">']
    # trazo del intervalo
    a = X(ini) if ini is not None else 4
    b = X(fin) if fin is not None else W - 4
    s.append(f'<line x1="{a}" y1="{EJE_Y}" x2="{b}" y2="{EJE_Y}" stroke="{MAG}" stroke-width="3.2" stroke-linecap="round"/>')
    if ini is None:
        s.append(f'<path d="M{a},{EJE_Y} l7,-4.5 v9 z" fill="{MAG}"/>')
    if fin is None:
        s.append(f'<path d="M{b},{EJE_Y} l-7,-4.5 v9 z" fill="{MAG}"/>')
    # eje y marcas
    s.append(f'<line x1="{PAD_X-8}" y1="{EJE_Y}" x2="{W-PAD_X+8}" y2="{EJE_Y}" stroke="#7B5A50" stroke-width="1.2"/>')
    for m in marcas:
        h = 9 if m == 0 else 5
        gr = 1.6 if m == 0 else 1
        s.append(f'<line x1="{X(m)}" y1="{EJE_Y-h}" x2="{X(m)}" y2="{EJE_Y+h}" stroke="#7B5A50" stroke-width="{gr}"/>')
        if m != 0:
            s.append(f'<text x="{X(m)}" y="{EJE_Y+21}" font-size="9.5" fill="#6E4F4F" '
                     f'text-anchor="middle" font-family="system-ui, sans-serif">{m}</text>')
    # extremos
    for v, cerr in ((ini, cerrado_ini), (fin, cerrado_fin)):
        if v is None:
            continue
        if cerr:
            s.append(f'<circle cx="{X(v)}" cy="{EJE_Y}" r="4.6" fill="{MAG}"/>')
        else:
            s.append(f'<circle cx="{X(v)}" cy="{EJE_Y}" r="4.6" fill="#FBF2EF" stroke="{MAG}" stroke-width="2.2"/>')
    s.append('</svg>')
    return "".join(s)
