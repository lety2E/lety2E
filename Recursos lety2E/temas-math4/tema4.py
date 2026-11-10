"""Math 4 · Tema 4 · Función cuadrática. Fuente: capturas (ejemplos, 3 bloques, resueltos)."""
from comun import g, cargar, CSS_COMUN, card, dato, resol
graf = cargar("funciones-svg-math").grafica

def par(v):                       # valor sustituido, siempre entre paréntesis
    return f"({v})"

def poli(a, b, c):                # a = ±1
    s = "x^2" if a == 1 else "-x^2"
    if b:
        s += f" {'+' if b > 0 else '-'} {abs(b) if abs(b) != 1 else ''}x"
    if c:
        s += f" {'+' if c > 0 else '-'} {abs(c)}"
    return s

def evalua(a, b, c, x):
    """(x)^2 - 6(x) + 5 = 0 - 0 + 5 = 5  — como en la captura."""
    izq = ("" if a == 1 else "-") + f"{par(x)}^2"
    t = [a * x * x]
    if b:
        izq += f" {'+' if b > 0 else '-'} {abs(b)}{par(x)}"
        t.append(b * x)
    if c:
        izq += f" {'+' if c > 0 else '-'} {abs(c)}"
        t.append(c)
    med = str(t[0])
    coef = ([b] if b else []) + ([c] if c else [])
    for v, k in zip(t[1:], coef):          # un término que vale 0 conserva el signo de su coeficiente
        med += f" {'+' if (v > 0 or (v == 0 and k > 0)) else '-'} {abs(v)}"
    return izq, med, sum(t)

def intervalo(p, q, cp, cq):
    return ("[" if cp else "(") + f"{p},\\,{q}" + ("]" if cq else ")")

def analiza(a, b, c, p, q):
    f = lambda x: a * x * x + b * x + c
    xs = list(range(p, q + 1))
    ys = [f(x) for x in xs]
    h = -b // (2 * a)
    assert -b % (2 * a) == 0 and p < h < q, "vértice entero y dentro del dominio"
    mx, mn = max(ys), min(ys)
    raices = [x for x in xs if f(x) == 0]
    disc = b * b - 4 * a * c
    r = int(round(disc ** 0.5)) if disc >= 0 else None
    assert disc >= 0 and r * r == disc, "raíces enteras"
    todas = sorted({(-b - r) // (2 * a), (-b + r) // (2 * a)})
    assert all(p <= x <= q for x in todas), "raíces dentro del dominio"
    cortes = sorted(set([p, q] + raices))
    pos, neg = [], []
    for u, v in zip(cortes, cortes[1:]):
        s = f((u + v) / 2)
        (pos if s > 0 else neg).append(intervalo(u, v, f(u) != 0, f(v) != 0))
    sube, baja = intervalo(h, q, 1, 1), intervalo(p, h, 1, 1)
    if a < 0:
        sube, baja = baja, sube
    pts = lambda val: "\\{" + ",\\,".join(f"({x},\\,{y})" for x, y in zip(xs, ys) if y == val) + "\\}"
    return dict(
        f=f, xs=xs, ys=ys,
        dominio=intervalo(p, q, 1, 1), rango=intervalo(mn, mx, 1, 1),
        maximos=pts(mx), minimos=pts(mn),
        raices="\\{" + ",\\,".join(map(str, raices)) + "\\}",
        crece=sube, decrece=baja,
        positiva=" \\cup ".join(pos) if pos else None,
        negativa=" \\cup ".join(neg) if neg else None)

def enunciado_tex(a, b, c, p, q):
    return f"f(x) = {poli(a, b, c)}", f"f : [{p},\\,{q}] \\to \\mathbb{{R}}"

def card_ej(titulo, lista):
    filas = "".join(
        f'<div class="ej-line">${enunciado_tex(*e)[0]}$ <span class="dom-f">${enunciado_tex(*e)[1]}$</span></div>'
        for e in lista)
    return card(titulo, filas)

def resolucion(e):
    a, b, c, p, q = e
    d = analiza(*e)
    filas = []
    for x in d["xs"]:
        izq, med, val = evalua(a, b, c, x)
        assert val == d["f"](x)
        filas.append(f"f({x}) &= {izq} = {med} = \\mathbf{{{val}}}")
    tabla = '<div class="sol evals">$$\\begin{aligned} ' + " \\\\ ".join(filas) + ' \\end{aligned}$$</div>'
    paso = 2 if (max(d["ys"]) - min(d["ys"])) > 12 else 1
    svg = graf([(d["f"], p, q)], puntos=list(zip(d["xs"], d["ys"])), paso_y=paso)
    sin_pos = '<div class="dato"><span class="et">positiva</span>no toma valores positivos</div>'
    sin_neg = '<div class="dato"><span class="et">negativa</span>no toma valores negativos</div>'
    datos = (dato("dominio", d["dominio"]) + dato("rango", d["rango"])
             + dato("puntos máximos", d["maximos"]) + dato("puntos mínimos", d["minimos"])
             + dato("raíces", d["raices"])
             + dato("crecimiento", d["crece"]) + dato("decrecimiento", d["decrece"])
             + (dato("positiva", d["positiva"]) if d["positiva"] else sin_pos)
             + (dato("negativa", d["negativa"]) if d["negativa"] else sin_neg))
    return (f'{tabla}\n<div class="resol-2col"><div class="datos-grid">{datos}</div>'
            f'<div class="graf-wrap">{svg}</div></div>')

EJEMPLO = (1, -6, 5, 0, 6)
BLOQUES = [
    [(1, -2, -8, -2, 4), (1, -6, 8, 0, 6)],
    [(1, 4, 0, -5, 1), (-1, -4, 0, -5, 1)],
    [(-1, 2, 8, -2, 4), (-1, -10, -24, -8, -2)],
]
EXTRAS = [
    [(1, -4, 3, 0, 4), (1, 2, -3, -4, 2), (-1, 6, -5, 0, 6), (1, 0, -4, -3, 3), (-1, 4, 0, -1, 5), (1, 6, 5, -6, 0)],
    [(-1, -2, 3, -4, 2), (1, -8, 12, 1, 7), (-1, 0, 4, -3, 3), (1, -2, 0, -2, 4), (-1, 8, -12, 1, 7), (1, 8, 12, -7, -1)],
]
todos = [EJEMPLO] + [e for b in BLOQUES + EXTRAS for e in b]
assert len(set(todos)) == len(todos)
for e in todos:
    analiza(*e)      # valida: vértice y raíces enteros, dentro del dominio

# respuestas de la captura, para comparar con lo calculado
CAPTURA = {
    (1, -2, -8, -2, 4): ("[-9,\\,0]", "\\{(-2,\\,0),\\,(4,\\,0)\\}", "\\{(1,\\,-9)\\}", "\\{-2,\\,4\\}", "[1,\\,4]", "[-2,\\,1]"),
    (1, -6, 8, 0, 6): ("[-1,\\,8]", "\\{(0,\\,8),\\,(6,\\,8)\\}", "\\{(3,\\,-1)\\}", "\\{2,\\,4\\}", "[3,\\,6]", "[0,\\,3]"),
    (1, 4, 0, -5, 1): ("[-4,\\,5]", "\\{(-5,\\,5),\\,(1,\\,5)\\}", "\\{(-2,\\,-4)\\}", "\\{-4,\\,0\\}", "[-2,\\,1]", "[-5,\\,-2]"),
    (-1, -4, 0, -5, 1): ("[-5,\\,4]", "\\{(-2,\\,4)\\}", "\\{(-5,\\,-5),\\,(1,\\,-5)\\}", "\\{-4,\\,0\\}", "[-5,\\,-2]", "[-2,\\,1]"),
    (-1, 2, 8, -2, 4): ("[0,\\,9]", "\\{(1,\\,9)\\}", "\\{(-2,\\,0),\\,(4,\\,0)\\}", "\\{-2,\\,4\\}", "[-2,\\,1]", "[1,\\,4]"),
    (-1, -10, -24, -8, -2): ("[-8,\\,1]", "\\{(-5,\\,1)\\}", "\\{(-8,\\,-8),\\,(-2,\\,-8)\\}", "\\{-6,\\,-4\\}", "[-8,\\,-5]", "[-5,\\,-2]"),
}
for e, esperado in CAPTURA.items():
    d = analiza(*e)
    calc = (d["rango"], d["maximos"], d["minimos"], d["raices"], d["crece"], d["decrece"])
    assert calc == esperado, (e, calc, esperado)
    print(e, "pos:", d["positiva"], "| neg:", d["negativa"])

ENUN = ("Encuentra el dominio, el rango, los puntos máximos y mínimos, las raíces, los intervalos de "
        "crecimiento y decrecimiento, y los intervalos donde la función es positiva y donde es negativa.")

video = g.seccion_video("5_xV0GMVpsY", "Función cuadrática")
t, dm = enunciado_tex(*EJEMPLO)
ejemplo = g.seccion_ejemplo(
    f'        <p class="enunciado">{ENUN}</p>\n'
    f'        <div class="ej-line">${t}$ <span class="dom-f">${dm}$</span></div>\n'
    f'        <p class="enunciado nota">Primero se evalúan los valores del intervalo, se grafican los puntos '
    f'y con la gráfica se encuentra lo que se pide.</p>\n'
    f'        {resolucion(EJEMPLO)}')
ejercicios = g.seccion("Ejercicios", "ejercicios",
    f'      <p class="enunciado">{ENUN}</p>\n'
    + g.grid([card_ej(f"Bloque {i + 1}", b) for i, b in enumerate(BLOQUES)], 3))
rs = []
for i, b in enumerate(BLOQUES):
    for e in b:
        t, dm = enunciado_tex(*e)
        rs.append(resol(f"Bloque {i + 1}",
                        f'<div class="ej-line">${t}$ <span class="dom-f">${dm}$</span></div>\n{resolucion(e)}'))
respuestas = g.seccion("Respuestas", "respuestas", g.resol_grid(rs), colapsable=True)
extras = g.seccion("Ejercicios extra", "extra",
    f'      <p class="enunciado">{ENUN}</p>\n'
    + g.grid([card_ej(f"Bloque {i + 1}", b) for i, b in enumerate(EXTRAS)], 2), colapsable=True)

CSS = CSS_COMUN + """
    .dom-f { margin-left: 1.1rem; }
    @media (max-width: 480px) { .sol.evals .katex-display { font-size: .72em; } .dom-f { display: block; margin-left: 0; } }
    .ejemplo-block > .ej-line, .resol-item > .ej-line { text-align: center; }
    @media (max-width: 380px) { .sol.evals .katex-display { font-size: .64em; } }
    .enunciado.nota { margin-top: .8rem; color: var(--text-3); font-size: .88rem; }
    .datos-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0 1rem; }
    @media (max-width: 480px) { .datos-grid { grid-template-columns: 1fr; } }
    .dato { font-size: .95rem; color: var(--text); }
"""
g.pagina("funcion-cuadratica", 4, "Función cuadrática",
         "Función cuadrática: dominio, rango, máximos, mínimos, raíces, crecimiento y signo a partir de su gráfica.",
         [video, ejemplo, ejercicios, respuestas, extras],
         prev=("funcion-escalonada.html", "Función escalonada"), sig=("area-funcion-longitud.html", "Área como función de la longitud"), css_extra=CSS)
print("ok tema 4")
