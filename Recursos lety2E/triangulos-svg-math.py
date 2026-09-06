# -*- coding: utf-8 -*-
"""Genera los triángulos SVG inline de las páginas de Math (lety2e.com).

Nacieron para Matemáticas 2 (Pitágoras, razones trigonométricas y semejanza,
5-sep-2026) y sirven para cualquier tema que necesite triángulos.

Uso:
    import sys; sys.path.insert(0, "Recursos lety2E")
    from importlib import import_module
    T = import_module("triangulos-svg-math")
    html = T.tri2("x", "y", "12", 6.88, 9.83, top="&#946;", br="35&#176;")

Convención de todos los triángulos rectángulos (la misma de las hojas de Lety):
    ángulo recto abajo-izquierda · cateto vertical a la izquierda ·
    base abajo · hipotenusa de arriba-izquierda a abajo-derecha.

Reglas que hay que respetar (ya vienen aplicadas aquí):
  · Todo <svg> lleva `width`/`height` además del viewBox. Sin ellos colapsa a
    0x0 dentro de un grid o un flex, y el triángulo se vuelve invisible.
  · Se dibuja a ESCALA REAL: se pasan los valores numéricos de los lados
    (calculados con la trigonometría del propio ejercicio), no medidas a ojo.
  · Colores del palette: contorno y relleno magenta (#FF00AA al 12 %),
    marca de ángulo recto café (#7B5A50), ángulos en morado (#7B2CBF).
  · Las etiquetas numéricas van en redonda; las literales ($x$, $a$, $hip$)
    en cursiva. Lo decide `es_num()`, no hay que pensarlo.

Funciones:
  tri()      triángulo rectángulo, ángulos opcionales como alfa/beta
  tri2()     igual, pero con el arquito del ángulo y su etiqueta libre
             (top = vértice superior, br = vértice inferior derecho)
  recto()    versión mínima, sin ángulos (pares edificio/poste de sombras)
  oblicuo()  triángulo cualquiera con los tres lados etiquetados
             (para "escribe seis proporciones")
  anidado()  triángulo rectángulo con una vertical interna; el pequeño de la
             derecha es semejante al grande. La base total va con línea de
             cota abajo para que no se confunda con el tramo derecho.
  par()      envuelve dos figuras lado a lado (necesita .par-figs en el CSS)

CSS que esperan las páginas:
    .tri-svg  { max-width: 100%; height: auto; display: block; }
    .par-figs { display: flex; align-items: flex-end; justify-content: center;
                gap: 14px; flex-wrap: wrap; }

Vista previa:  python3 "Recursos lety2E/triangulos-svg-math.py"
               (escribe /tmp/triangulos-preview.html)
"""
import math

FONT  = 'DM Sans, sans-serif'
MAG   = "#FF00AA"     # contorno y relleno del triángulo
FILL  = "0.12"        # opacidad del relleno
RECTA = "#7B5A50"     # marca del ángulo recto y líneas de cota
TXT   = "#1A0828"     # etiquetas de lado
ANG   = "#7B2CBF"     # etiquetas y arcos de ángulo

ALFA, BETA = "&#945;", "&#946;"


def grados(n):
    """35 -> '35°' listo para pasar como etiqueta de ángulo."""
    return f"{n}&#176;"


def _es_num(t):
    return str(t).replace('.', '').isdigit()


def _t(x, y, txt, anchor="middle", italic=None, color=TXT, size=12):
    if italic is None:
        italic = not _es_num(txt)
    st = ' font-style="italic"' if italic else ''
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
            f'fill="{color}"{st} text-anchor="{anchor}">{txt}</text>')


def _svg(w, h, cuerpo, aria):
    return (f'<svg viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" '
            f'xmlns="http://www.w3.org/2000/svg" class="tri-svg" role="img" '
            f'aria-label="{aria}">\n' + "\n".join(cuerpo) + '\n</svg>')


def _cuerpo_recto(A, B, C, marca=9):
    """Polígono del triángulo rectángulo + la escuadrita del ángulo recto."""
    return [
        f'<polygon points="{B[0]:.1f},{B[1]:.1f} {C[0]:.1f},{C[1]:.1f} {A[0]:.1f},{A[1]:.1f}" '
        f'fill="{MAG}" fill-opacity="{FILL}" stroke="{MAG}" stroke-width="2" stroke-linejoin="round"/>',
        f'<polyline points="{B[0]:.1f},{B[1]-marca:.1f} {B[0]+marca:.1f},{B[1]-marca:.1f} '
        f'{B[0]+marca:.1f},{B[1]:.1f}" fill="none" stroke="{RECTA}" stroke-width="1"/>',
    ]


def tri(v_lab, b_lab, h_lab, v_val, b_val, alpha=False, beta=False,
        box=(190, 140), aria=None):
    """Triángulo rectángulo a escala. `alpha` marca el vértice superior y
    `beta` el inferior derecho, con las letras griegas."""
    PL, PR, PT, PB = 30, 34, 12, 24
    s = min(box[0] / b_val, box[1] / v_val)
    W, H = b_val * s, v_val * s
    x0, y0 = PL, PT
    A, B, C = (x0, y0), (x0, y0 + H), (x0 + W, y0 + H)
    out = _cuerpo_recto(A, B, C)
    out.append(_t(x0 - 8, y0 + H / 2 + 4, v_lab, "end"))
    out.append(_t(x0 + W / 2, y0 + H + 17, b_lab))
    hx, hy = (A[0] + C[0]) / 2, (A[1] + C[1]) / 2
    out.append(_t(hx + 16, hy - 4, h_lab, "start"))
    if alpha:
        out.append(_t(A[0] + 9, A[1] + 20, ALFA, "middle", False, ANG, 13))
    if beta:
        out.append(_t(C[0] - 16, C[1] - 7, BETA, "middle", False, ANG, 13))
    return _svg(W + PL + PR, H + PT + PB, out,
                aria or f"Triángulo rectángulo con cateto {v_lab}, base {b_lab} e hipotenusa {h_lab}")


def tri2(v_lab, b_lab, h_lab, v_val, b_val, top=None, br=None,
         box=(150, 110), aria=None):
    """Como tri(), pero dibuja el arquito del ángulo con la etiqueta que se le
    pase: `top` en el vértice superior, `br` en el inferior derecho.
    Ejemplos de etiqueta: grados(35), ALFA, BETA."""
    PL, PR, PT, PB = 30, 40, 14, 24
    s = min(box[0] / b_val, box[1] / v_val)
    W, H = b_val * s, v_val * s
    x0, y0 = PL, PT
    A, B, C = (x0, y0), (x0, y0 + H), (x0 + W, y0 + H)
    hyp = math.hypot(W, H)
    r = 16.0
    out = _cuerpo_recto(A, B, C)
    if br:   # del lado de la base hacia la hipotenusa
        rr = min(r, W * .5, hyp * .3)
        ex, ey = C[0] - rr * W / hyp, C[1] - rr * H / hyp
        out.append(f'<path d="M {C[0]-rr:.1f},{C[1]:.1f} A {rr:.1f},{rr:.1f} 0 0 1 '
                   f'{ex:.1f},{ey:.1f}" fill="none" stroke="{ANG}" stroke-width="1.2"/>')
        out.append(_t(C[0] - rr - 3, C[1] - 5, br, "end", False, ANG, 12))
    if top:  # del cateto vertical hacia la hipotenusa
        rr = min(r, H * .5, hyp * .3)
        ex, ey = A[0] + rr * W / hyp, A[1] + rr * H / hyp
        out.append(f'<path d="M {A[0]:.1f},{A[1]+rr:.1f} A {rr:.1f},{rr:.1f} 0 0 0 '
                   f'{ex:.1f},{ey:.1f}" fill="none" stroke="{ANG}" stroke-width="1.2"/>')
        out.append(_t(A[0] + rr + 3, A[1] + rr + 9, top, "start", False, ANG, 12))
    out.append(_t(x0 - 8, y0 + H / 2 + 4, v_lab, "end"))
    out.append(_t(x0 + W / 2, y0 + H + 17, b_lab))
    hx, hy = (A[0] + C[0]) / 2, (A[1] + C[1]) / 2
    out.append(_t(hx + 15, hy - 3, h_lab, "start"))
    return _svg(W + PL + PR, H + PT + PB, out,
                aria or f"Triángulo rectángulo con cateto {v_lab}, base {b_lab} e hipotenusa {h_lab}")


def recto(v_lab, b_lab, h_lab=None, v_val=None, b_val=None, box=(110, 85), aria=None):
    """Triángulo rectángulo mínimo, sin ángulos. La hipotenusa se etiqueta sólo
    si se pasa `h_lab`. Es el que se usa para los pares edificio/poste."""
    v_val = 1.0 if v_val is None else v_val
    b_val = 1.0 if b_val is None else b_val
    PL, PR, PT, PB = 28, (30 if h_lab else 16), 12, 22
    s = min(box[0] / b_val, box[1] / v_val)
    W, H = b_val * s, v_val * s
    x0, y0 = PL, PT
    A, B, C = (x0, y0), (x0, y0 + H), (x0 + W, y0 + H)
    out = _cuerpo_recto(A, B, C, marca=8)
    out.append(_t(x0 - 7, y0 + H / 2 + 4, v_lab, "end"))
    out.append(_t(x0 + W / 2, y0 + H + 16, b_lab))
    if h_lab:
        out.append(_t((A[0] + C[0]) / 2 + 13, (A[1] + C[1]) / 2 - 3, h_lab, "start"))
    return _svg(W + PL + PR, H + PT + PB, out,
                aria or f"Triángulo rectángulo de cateto {v_lab} y base {b_lab}")


def oblicuo(izq, der, base, w=110, h=72, apex=0.34, aria=None):
    """Triángulo cualquiera con los tres lados etiquetados.
    Para que un par se vea SEMEJANTE hay que darles el mismo `apex` y distinto
    tamaño; si se cambia el apex dejan de tener la misma forma."""
    PL, PR, PT, PB = 26, 26, 16, 22
    A = (PL + apex * w, PT)
    B = (PL, PT + h)
    C = (PL + w, PT + h)
    out = [f'<polygon points="{B[0]:.1f},{B[1]:.1f} {C[0]:.1f},{C[1]:.1f} {A[0]:.1f},{A[1]:.1f}" '
           f'fill="{MAG}" fill-opacity="{FILL}" stroke="{MAG}" stroke-width="2" stroke-linejoin="round"/>',
           _t((A[0] + B[0]) / 2 - 10, (A[1] + B[1]) / 2 + 4, izq, "end"),
           _t((A[0] + C[0]) / 2 + 10, (A[1] + C[1]) / 2 + 4, der, "start"),
           _t((B[0] + C[0]) / 2, C[1] + 17, base)]
    return _svg(w + PL + PR, h + PT + PB, out,
                aria or f"Triángulo de lados {izq}, {der} y {base}")


def anidado(v_lab, total_lab, der_lab, int_lab, H, Btot, Bder,
            box=(150, 115), aria=None):
    """Triángulo rectángulo con una vertical interna: el pequeño de la derecha
    es semejante al grande.

    H, Btot, Bder son los valores numéricos (altura del grande, base total y
    tramo derecho). La altura interna NO se pasa: sale de la semejanza, así la
    figura nunca miente.

    La base total va con línea de cota debajo; el tramo derecho, justo bajo la
    base. Hace falta distinguirlas: en el LaTeX de Lety esas dos etiquetas
    aparecen en posiciones inconsistentes de un ejercicio a otro y sin la cota
    no se sabe cuál es cuál."""
    PL, PR, PT, PB = 28, 26, 14, 44
    s = min(box[0] / Btot, box[1] / H)
    W, Ht = Btot * s, H * s
    x0, y0 = PL, PT
    A, B, C = (x0, y0), (x0, y0 + Ht), (x0 + W, y0 + Ht)
    xi = C[0] - Bder * s                    # pie de la vertical interna
    yi = C[1] - (H * Bder / Btot) * s       # su altura, por semejanza
    out = _cuerpo_recto(A, B, C, marca=8)
    out.insert(1, f'<line x1="{xi:.1f}" y1="{C[1]:.1f}" x2="{xi:.1f}" y2="{yi:.1f}" '
                  f'stroke="{MAG}" stroke-width="1.6"/>')
    out.append(_t(x0 - 7, y0 + Ht / 2 + 4, v_lab, "end"))
    out.append(_t(xi + 6, (C[1] + yi) / 2 + 4, int_lab, "start"))
    out.append(_t((xi + C[0]) / 2, C[1] + 15, der_lab))
    yc = C[1] + 30                          # línea de cota de la base total
    out += [f'<line x1="{B[0]:.1f}" y1="{yc:.1f}" x2="{C[0]:.1f}" y2="{yc:.1f}" '
            f'stroke="{RECTA}" stroke-width="1"/>',
            f'<line x1="{B[0]:.1f}" y1="{yc-3:.1f}" x2="{B[0]:.1f}" y2="{yc+3:.1f}" '
            f'stroke="{RECTA}" stroke-width="1"/>',
            f'<line x1="{C[0]:.1f}" y1="{yc-3:.1f}" x2="{C[0]:.1f}" y2="{yc+3:.1f}" '
            f'stroke="{RECTA}" stroke-width="1"/>',
            _t((B[0] + C[0]) / 2, yc + 14, total_lab)]
    return _svg(W + PL + PR, Ht + PT + PB, out,
                aria or f"Triángulo rectángulo de altura {v_lab} y base {total_lab}, "
                        f"con una vertical interna {int_lab}")


def par(*figuras, gap=14):
    """Dos o más figuras lado a lado (pide .par-figs en el CSS de la página)."""
    return f'<div class="par-figs" style="gap:{gap}px">' + "".join(figuras) + '</div>'


if __name__ == "__main__":
    R = math.radians
    piezas = [
        ("tri() — Pitágoras, ejercicio 1 (8, x, 16)",
         tri("8", "x", "16", 8, math.sqrt(192), alpha=True, beta=True, box=(150, 110))),
        ("tri2() — razones trigonométricas, ejemplo (35°)",
         tri2("x", "y", "12", 12 * math.sin(R(35)), 12 * math.cos(R(35)),
              top=BETA, br=grados(35), box=(165, 120))),
        ("oblicuo() — par semejante para las proporciones",
         par(oblicuo("a", "z", "b", 92, 60), oblicuo("y", "x", "c", 122, 80))),
        ("anidado() — semejanza, ejemplo de x (H=9, base 12, tramo 8)",
         anidado("x", "12", "8", "6", 9, 12, 8, box=(140, 105))),
        ("recto() — par edificio / poste",
         par(recto("X", "8.5", None, 13.03, 8.5, (78, 105)),
             recto("2.3", "1.5", None, 2.3, 1.5, (38, 52)))),
    ]
    html = ['<!doctype html><meta charset="utf-8">',
            '<style>body{background:#FDF4F2;font-family:system-ui;padding:24px;color:#1A0828}',
            'h2{font-size:.95rem;font-weight:600;margin:1.8rem 0 .4rem}',
            '.par-figs{display:flex;align-items:flex-end;gap:14px;flex-wrap:wrap}</style>']
    for titulo, svg in piezas:
        html.append(f"<h2>{titulo}</h2>{svg}")
    ruta = "/tmp/triangulos-preview.html"
    open(ruta, "w", encoding="utf-8").write("\n".join(html))
    print(f"Vista previa escrita en {ruta}")
