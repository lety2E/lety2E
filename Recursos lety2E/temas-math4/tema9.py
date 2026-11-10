"""Math 4 · Tema 9 · Operaciones con funciones. Fuente: capturas (2 hojas de ejemplo, 5 bloques, resueltos).

Un polinomio es una lista de términos (coeficiente, exponente) EN EL ORDEN EN QUE ESTÁ ESCRITO:
los productos y cocientes se publican en el orden en que salen, como en las capturas; sólo las
sumas y restas se reducen y ordenan por grado.
"""
from fractions import Fraction
from comun import g as G, CSS_COMUN, apuntes

def term(c, e, primero):
    a = abs(c)
    cs = "" if (a == 1 and e != 0) else str(a)
    xs = "" if e == 0 else ("x" if e == 1 else f"x^{{{e}}}")
    s = cs + xs
    if primero:
        return ("-" if c < 0 else "") + s
    return (" - " if c < 0 else " + ") + s

def tex(p):
    if not p:
        return "0"
    return "".join(term(c, e, i == 0) for i, (c, e) in enumerate(p))

def reduce(p):
    d = {}
    for c, e in p:
        d[e] = d.get(e, 0) + c
    return [(c, e) for e, c in sorted(d.items(), reverse=True) if c]

def neg(p):
    return [(-c, e) for c, e in p]

def mult(p, q):
    return [(a * b, e + f) for a, e in p for b, f in q]

def entre_monomio(p, m):
    (b, f), = m
    out = []
    for a, e in p:
        assert a % b == 0
        out.append((a // b, e - f))
    return out

def division(f, gp):
    """División larga. Devuelve (cociente, pasos); cada paso = (lo que se resta ya con signo cambiado, residuo)."""
    resto = reduce(f)
    q, pasos = [], []
    while resto and resto[0][1] >= gp[0][1]:
        c, e = resto[0]
        assert c % gp[0][0] == 0
        t = (c // gp[0][0], e - gp[0][1])
        q.append(t)
        resta = neg(mult([t], gp))
        resto = reduce(resto + resta)
        pasos.append((resta, resto))
    assert not resto, "la división no es exacta"
    return q, pasos

def casita(f, gp):
    """La división acomodada 'como una división normal', una columna por grado."""
    q, pasos = division(f, gp)
    grados = sorted({e for _, e in reduce(f)} | {e for r, _ in pasos for _, e in r}, reverse=True)
    col = {e: i for i, e in enumerate(grados)}
    n = len(grados)
    def fila(p, cabeza=""):
        celdas = [""] * n
        for k, (c, e) in enumerate(p):
            celdas[col[e]] = term(c, e, k == 0).strip().replace("+ ", "+").replace("- ", "-")
        return cabeza + " & " + " & ".join(celdas)
    def fila_q(p):
        celdas = [""] * n
        for k, (c, e) in enumerate(p):
            celdas[k] = term(c, e, k == 0).strip().replace("+ ", "+").replace("- ", "-")
        return " & " + " & ".join(celdas)
    filas = [fila_q(q) + " \\\\ \\hline", fila(reduce(f), tex(gp))]
    for resta, resto in pasos:
        filas.append(fila(resta) + " \\\\ \\hline")
        filas.append(fila(resto) if resto else " & " + " & ".join([""] * (n - 1) + ["0"]))
    cuerpo = ""
    for i, fl in enumerate(filas):
        cuerpo += fl + ("" if fl.endswith("\\hline") or i == len(filas) - 1 else " \\\\") + " "
    return f"\\begin{{array}}{{r|{'r' * n}}} {cuerpo}\\end{{array}}", q

def sol(lineas, clase="sol"):
    return f'<div class="{clase}">$$\\begin{{aligned}} ' + " \\\\ ".join(lineas) + ' \\end{aligned}$$</div>'

def resuelve(op, F, bold=True):
    """op: ('suma','h','f') · ('resta','f','h') · ('mult','g','p') · ('div','p','m'). F: dict de funciones."""
    tipo, a, b = op
    A, B = F[a], F[b]
    B_ = lambda s: f"\\boldsymbol{{{s}}}" if bold else s
    if tipo == "suma":
        r = reduce(A + B)
        return sol([f"{a}(x) + {b}(x) &= {tex(A)}", f"&\\quad + {tex(B)}", f"&= {B_(tex(r))}"]), r
    if tipo == "resta":
        r = reduce(A + neg(B))
        nb = tex(neg(B))
        nb = nb if nb.startswith("-") else "+" + nb
        return sol([f"{a}(x) - {b}(x) &= [{tex(A)}]", f"&\\quad - [{tex(B)}]",
                    f"&= {tex(A)}", f"&\\quad {nb}", f"&= {B_(tex(r))}"]), r
    if tipo == "mult":
        r = mult(A, B)
        return sol([f"{a}(x)\\,{b}(x) &= ({tex(A)})({tex(B)})", f"&= {B_(tex(r))}"]), r
    if len(B) == 1:
        r = entre_monomio(A, B)
        return sol([f"\\dfrac{{{a}(x)}}{{{b}(x)}} &= \\dfrac{{{tex(A)}}}{{{tex(B)}}}", f"&= {B_(tex(r))}"]), r
    arr, r = casita(A, B)
    return (sol([f"\\dfrac{{{a}(x)}}{{{b}(x)}} &= \\dfrac{{{tex(A)}}}{{{tex(B)}}}", f"&= {B_(tex(r))}"])
            + f'\n<div class="sol casita">$${arr}$$</div>'), r

def pide_tex(op):
    tipo, a, b = op
    return {"suma": f"{a}(x) + {b}(x)", "resta": f"{a}(x) - {b}(x)", "mult": f"{a}(x)\\,{b}(x)",
            "div": f"\\dfrac{{{a}(x)}}{{{b}(x)}}"}[tipo]

OPS = [("suma", "h", "f"), ("resta", "f", "h"), ("mult", "g", "p"), ("mult", "m", "f"), ("div", "p", "m"), ("div", "f", "g")]
ORDEN = "fghpm"

BLOQUES = [
    dict(f=[(2, 3), (5, 2), (7, 1), (4, 0)], g=[(1, 1), (1, 0)], h=[(-8, 3), (4, 1), (-6, 0)], p=[(4, 5), (-16, 3)], m=[(4, 2)]),
    dict(f=[(4, 3), (-17, 2), (-7, 1), (6, 0)], g=[(4, 1), (3, 0)], h=[(2, 3), (-5, 1), (1, 0)], p=[(5, 7), (-15, 3)], m=[(5, 2)]),
    dict(f=[(8, 3), (-2, 2), (12, 1), (-3, 0)], g=[(4, 1), (-1, 0)], h=[(3, 3), (-4, 2), (-12, 1), (6, 0)], p=[(12, 8), (-18, 4)], m=[(6, 5)]),
    dict(f=[(15, 3), (-16, 2), (7, 1), (-2, 0)], g=[(3, 1), (-2, 0)], h=[(-6, 3), (8, 2), (-4, 1), (-1, 0)], p=[(7, 4), (-14, 8)], m=[(-7, 10)]),
    dict(f=[(-15, 3), (42, 2), (-24, 1)], g=[(3, 1), (-6, 0)], h=[(5, 3), (-20, 2), (12, 0)], p=[(20, 7), (-40, 10)], m=[(-10, 5)]),
]
def nuevo(gp, q, h, p, m):
    return dict(f=reduce(mult(gp, q)), g=gp, h=h, p=p, m=m)
EXTRAS = [
    nuevo([(2, 1), (1, 0)], [(3, 2), (-4, 1), (5, 0)], [(4, 3), (-7, 2), (2, 1), (-9, 0)], [(9, 6), (-12, 4)], [(3, 2)]),
    nuevo([(5, 1), (-2, 0)], [(1, 2), (3, 1), (-4, 0)], [(-2, 3), (6, 2), (-1, 1), (5, 0)], [(16, 9), (-24, 5)], [(-8, 4)]),
]

# respuestas legibles de la hoja de resueltos (bloques 1 y 4), para comparar
def R(F, i):
    return tex(resuelve(OPS[i], F)[1])
b1, b4 = BLOQUES[0], BLOQUES[3]
assert R(b1, 0) == "-6x^{3} + 5x^{2} + 11x - 2"
assert R(b1, 1) == "10x^{3} + 5x^{2} + 3x + 10"        # la captura dice -3x: es +3x (7x - 4x)
assert R(b1, 2) == "4x^{6} - 16x^{4} + 4x^{5} - 16x^{3}"
assert R(b1, 3) == "8x^{5} + 20x^{4} + 28x^{3} + 16x^{2}"
assert R(b1, 4) == "x^{3} - 4x"
assert R(b1, 5) == "2x^{2} + 3x + 4"
assert R(b4, 0) == "9x^{3} - 8x^{2} + 3x - 3"
assert R(b4, 1) == "21x^{3} - 24x^{2} + 11x - 1"
assert R(b4, 2) == "21x^{5} - 42x^{9} - 14x^{4} + 28x^{8}"
assert R(b4, 3) == "-105x^{13} + 112x^{12} - 49x^{11} + 14x^{10}"
assert R(b4, 4) == "-x^{-6} + 2x^{-2}"                   # la captura dice -x^6 + 2x^2: los exponentes son negativos
assert R(b4, 5) == "5x^{2} - 2x + 1"
assert R(BLOQUES[1], 5) == "x^{2} - 5x + 2" and R(BLOQUES[2], 5) == "2x^{2} + 3" and R(BLOQUES[4], 5) == "-5x^{2} + 4x"
assert R(BLOQUES[4], 4) == "-2x^{2} + 4x^{5}" and R(BLOQUES[1], 4) == "x^{5} - 3x"
for F in BLOQUES + EXTRAS:
    for op in OPS:
        resuelve(op, F)
for i, F in enumerate(BLOQUES + EXTRAS):
    print(i + 1, " | ".join(R(F, k) for k in range(6)))

def card_bloque(titulo, F):
    return G.card_funciones(titulo, [f"{n}(x) = {tex(F[n])}" for n in ORDEN], [pide_tex(op) for op in OPS])

# ── ejemplo ──
EJ = dict(f=[(5, 2), (-3, 0)], m=[(3, 2)], h=[(6, 4), (-9, 5)], g=[(-4, 3), (2, 2), (-8, 0)], t=[(5, 3), (-3, 2), (-4, 0)])
EJ2 = dict(f=[(12, 3), (-16, 2), (-4, 1), (8, 0)], g=[(6, 1), (4, 0)])
assert tex(resuelve(("suma", "g", "t"), EJ)[1]) == "x^{3} - x^{2} - 12"
assert tex(resuelve(("resta", "t", "g"), EJ)[1]) == "9x^{3} - 5x^{2} + 4"
assert tex(resuelve(("mult", "m", "g"), EJ)[1]) == "-12x^{5} + 6x^{4} - 24x^{2}"
assert tex(resuelve(("mult", "f", "h"), EJ)[1]) == "30x^{6} - 45x^{7} - 18x^{4} + 27x^{5}"
assert tex(resuelve(("div", "h", "m"), EJ)[1]) == "2x^{2} - 3x^{3}"
assert tex(resuelve(("div", "f", "g"), EJ2)[1]) == "2x^{2} - 4x + 2"

def paso(titulo, nota, cuerpo):
    return (f'        <div class="paso-titulo">{titulo}</div>\n'
            f'        <p class="enunciado nota">{nota}</p>\n        {cuerpo}')

dadas = "".join(f'<div class="ej-line">${n}(x) = {tex(EJ[n])}$</div>' for n in "fmhgt")
dadas2 = "".join(f'<div class="ej-line">${n}(x) = {tex(EJ2[n])}$</div>' for n in "fg")
ejemplo = G.seccion_ejemplo(
    f'        <p class="ej-sub">dadas las funciones</p>\n        <div class="dadas">{dadas}</div>\n'
    + paso("Suma de funciones", "Se juntan los términos semejantes y se resuelve.", resuelve(("suma", "g", "t"), EJ)[0]) + "\n"
    + paso("Resta de funciones", "Se ponen corchetes para que la función que se resta se multiplique por el signo negativo y cambie de signo; después se juntan los términos semejantes.", resuelve(("resta", "t", "g"), EJ)[0]) + "\n"
    + paso("Multiplicación de funciones", "Se multiplica cada término.", resuelve(("mult", "m", "g"), EJ)[0] + "\n        " + resuelve(("mult", "f", "h"), EJ)[0]) + "\n"
    + paso("División de funciones", "Se divide cada término del numerador entre el término del denominador; al dividir, los exponentes se restan.", resuelve(("div", "h", "m"), EJ)[0]) + "\n"
    + f'        <p class="enunciado nota">Cuando el denominador tiene más de un término, se colocan los valores como una división normal y se resuelve. Para este caso se usan otras funciones:</p>\n'
    + f'        <div class="dadas">{dadas2}</div>\n        ' + resuelve(("div", "f", "g"), EJ2)[0], titulo="Ejemplos")

video = G.seccion_video("drvoYqMYqmQ", "Operaciones con funciones")
ejercicios = G.seccion("Ejercicios", "ejercicios",
    G.grid([card_bloque(f"Bloque {i + 1}", F) for i, F in enumerate(BLOQUES)], 2))
respuestas = G.seccion("Respuestas", "respuestas",
    G.resol_grid([G.resol_bloque(f"Bloque {i + 1}", []).replace("\n          </div>",
                  "\n" + "\n".join(resuelve(op, F)[0] for op in OPS) + "\n          </div>")
                  for i, F in enumerate(BLOQUES)]), colapsable=True)
extras = G.seccion("Ejercicios extra", "extra",
    G.grid([card_bloque(f"Bloque {i + 1}", F) for i, F in enumerate(EXTRAS)], 2), colapsable=True)

CSS = CSS_COMUN + """
    .ej-sub {
      font-size: .72rem; font-weight: 700; text-transform: uppercase;
      letter-spacing: .06em; color: var(--text-3);
      margin: 0 0 .35rem; text-align: center;
    }
    .ej-sub-2 { margin-top: .9rem; }
    .mini-card-body .ej-sub + .ej-line { padding-top: .1rem; }
    .pide-lista { display: flex; flex-wrap: wrap; gap: .4rem; justify-content: center; align-items: center; }
    /* OJO: sólo el hijo directo — un `span` suelto alcanzaría a los de KaTeX */
    .pide-lista > span {
      display: inline-block; background: var(--accent-light); color: var(--accent);
      border-radius: 14px; padding: .22rem .65rem; font-weight: 600;
    }
    .dadas { text-align: center; margin-bottom: .4rem; }
    .enunciado.nota { margin: .2rem 0 .3rem; color: var(--text-3); font-size: .88rem; }
    .paso-titulo { margin-top: 1.5rem; }
    .resol-item .sol + .sol { border-top: 1px solid var(--border-s); }
    .sol.casita { border-top: none !important; }
    @media (max-width: 480px) { .sol .katex-display { font-size: .78em; } }
    @media (max-width: 380px) { .sol .katex-display { font-size: .7em; } }
"""
G.pagina("operaciones-funciones", 9, "Operaciones con funciones",
         "Operaciones con funciones: suma, resta, multiplicación y división de funciones polinomiales, con ejemplos y ejercicios resueltos.",
         [video, ejemplo, ejercicios, respuestas, extras],
         prev=("esbozo-grafico.html", "Esbozo gráfico de una función"),
         sig=("composicion-funciones.html", "Composición de funciones"), css_extra=CSS)
print("ok tema 9")
