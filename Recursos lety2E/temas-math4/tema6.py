"""Math 4 · Tema 6 · Área como función de la longitud. Fuente: capturas (ejemplo, 4 ejercicios, resueltos)."""
from comun import g, cargar, CSS_COMUN, card, dato, resol
graf = cargar("funciones-svg-math").grafica
recta = cargar("rectas-numericas-svg-math").recta

# un rectángulo = (P, k): perímetro P, lados a = y, b = x + k
def datos(P, k):
    assert P % 4 == 0
    c = P // 2 - k                      # y = c - x
    assert c > 0 and (c - k) % 2 == 0
    return c, c - k, c * k              # A(x) = -x^2 + (c-k)x + ck

def sg(v, primero=False):               # término con signo
    if primero:
        return str(v)
    return f"{'+' if v >= 0 else '-'} {abs(v)}"

def poli(b, c0):
    s = "-x^2"
    if b:
        s += f" {'+' if b > 0 else '-'} {abs(b) if abs(b) != 1 else ''}x"
    return s + f" + {c0}"

def rect_svg(k):
    return ('<div class="grafica-wrap"><svg viewBox="0 0 180 96" xmlns="http://www.w3.org/2000/svg" role="img" '
            'class="figura-rect" aria-label="Rectángulo con sus lados">'
            '<rect x="12" y="12" width="112" height="52" fill="#FF00AA" fill-opacity="0.15" stroke="#7B5A50" stroke-width="1.6" rx="2"/>'
            '<text x="68" y="82" font-size="14" font-style="italic" font-family="Georgia, serif" fill="#1A0828" text-anchor="middle">y</text>'
            f'<text x="132" y="43" font-size="14" font-style="italic" font-family="Georgia, serif" fill="#1A0828" text-anchor="start">x + {k}</text>'
            '</svg></div>')

def figura(P, k):
    return f'<div class="ej-line">{rect_svg(k)}$P = {P}$</div>'

def al(lineas):
    return '<div class="sol">$$\\begin{aligned} ' + " \\\\ ".join(lineas) + ' \\end{aligned}$$</div>'

def resolucion(P, k):
    c, b, c0 = datos(P, k)
    f = lambda x: -x * x + b * x + c0
    # 1 · área en función de x
    per = al(["P &= 2a + 2b", f"2(y) + 2(x + {k}) &= {P}", f"2y + 2x + {2 * k} &= {P}",
              f"2y &= {P} - 2x - {2 * k}", f"2y &= {P - 2 * k} - 2x",
              f"y &= \\dfrac{{{P - 2 * k} - 2x}}{{2}}", f"y &= {c} - x"])
    cx = "x" if c == 1 else f"{c}x"
    kx = "x" if k == 1 else f"{k}x"
    area = al(["A &= ab", f"A(x) &= ({c} - x)(x + {k})", f"A(x) &= {cx} + {c * k} - x^2 - {kx}",
               f"A(x) &= \\boldsymbol{{{poli(b, c0)}}}"])
    # 2 · dominio
    d1 = al([f"{c} - x &\\ge 0", f"-x &\\ge -{c}", f"x &\\le \\dfrac{{-{c}}}{{-1}}", f"x &\\le {c}"])
    d2 = al([f"x + {k} &\\ge 0", f"x &\\ge -{k}"])
    marcas = list(range(-k - 1, c + 2))
    rn = f'<div class="graf-wrap">{recta(-k - 1, c + 1, marcas, -k, c, True, True)}</div>'
    # 3 · gráfica y área máxima
    xs = list(range(-k, c + 1))
    filas = []
    for x in xs:
        cuad, lin = x * x, b * x
        izq = f"-({x})^2" + (f" {'+' if b > 0 else '-'} {abs(b)}({x})" if b else "") + f" + {c0}"
        med = f"-({cuad})" + (f" {'+' if (lin > 0 or (lin == 0 and b > 0)) else '-'} {abs(lin)}" if b else "") + f" + {c0}"
        pasos = [izq, med]
        if cuad:
            pasos.append(f"-{cuad} {sg(lin + c0)}")
        assert -cuad + lin + c0 == f(x)
        filas.append(f"A({x}) &= {pasos[0]} \\\\ &= " + " = ".join(pasos[1:]) + f" = \\mathbf{{{f(x)}}}")
    pares = [f"({x},\\,{f(x)})" for x in xs]
    trozos = [",\\,".join(pares[i:i + 4]) for i in range(0, len(pares), 4)]
    pares_tex = "\\begin{gathered} " + ", \\\\ ".join(trozos) + " \\end{gathered}"
    mx = max(f(x) for x in xs)
    assert mx == f((c - k) // 2) == ((c + k) // 2) ** 2
    paso = 1 if mx <= 10 else (2 if mx <= 20 else 5)
    svg = graf([(f, -k, c)], puntos=[(x, f(x)) for x in xs], paso_y=paso,
               ventana=(-k - 1, c + 1, 0 if paso > 1 else -1, (mx // paso + 1) * paso),
               etiqueta="Gráfica del área en función de x")
    dom_html = dato("dominio", "[-%d,\\,%d]" % (k, c))
    return (
        '<div class="paso-titulo">1 · El área en función de x</div>\n'
        f'<div class="dos-col">{per}{area}</div>\n'
        '<div class="paso-titulo">2 · Dominio</div>\n'
        f'<div class="dos-col">{d1}{d2}</div>\n{rn}\n'
        f'{dom_html}\n'
        '<div class="paso-titulo">3 · Área máxima</div>\n'
        '<div class="sol evals">$$\\begin{aligned} ' + " \\\\[.45em] ".join(filas) + ' \\end{aligned}$$</div>\n'
        f'<div class="dato"><span class="et">parejas ordenadas</span>$${pares_tex}$$</div>\n'
        f'<div class="graf-wrap">{svg}</div>\n'
        f'<div class="dato"><span class="et">área máxima</span><span class="resultado-pill">${mx}$</span></div>'), (c, b, c0, mx)

EJEMPLO = (12, 1)
EJERCICIOS = [(16, 2), (12, 5), (20, 4), (28, 3)]
EXTRAS = [[(20, 2), (16, 4), (24, 3), (8, 1), (24, 5)],
          [(20, 6), (16, 1), (28, 6), (12, 2), (24, 1)]]
todos = [EJEMPLO] + EJERCICIOS + [e for b in EXTRAS for e in b]
assert len(set(todos)) == len(todos)
for e in todos:
    datos(*e)

# lo que dice la captura: (y = c - x, A(x) = -x^2 + bx + c0, área máxima)
CAPTURA = {(12, 1): (5, 4, 5, 9), (16, 2): (6, 4, 12, 16), (12, 5): (1, -4, 5, 9),
           (20, 4): (6, 2, 24, 25), (28, 3): (11, 8, 33, 49)}
for e, esperado in CAPTURA.items():
    assert resolucion(*e)[1] == esperado, (e, resolucion(*e)[1])

PIDE = ("<strong>1.</strong> Expresa el área del rectángulo en función de $x$. "
        "<strong>2.</strong> Determina su dominio. "
        "<strong>3.</strong> A partir de su gráfica, encuentra el área máxima del rectángulo dado su perímetro.")

ejemplo = g.seccion_ejemplo(
    f'        <p class="enunciado">{PIDE}</p>\n        {figura(*EJEMPLO)}\n'
    f'        <p class="enunciado nota">Los lados son $a = y$ y $b = x + 1$. Con la fórmula del perímetro se expresa '
    f'$y$ en términos de $x$; el dominio sale de pedir que los dos lados no sean negativos.</p>\n'
    f'        {resolucion(*EJEMPLO)[0]}')
ejercicios = g.seccion("Ejercicios", "ejercicios",
    f'      <p class="enunciado">{PIDE}</p>\n'
    + g.grid([card(i + 1, figura(*e)) for i, e in enumerate(EJERCICIOS)], 2))
respuestas = g.seccion("Respuestas", "respuestas",
    g.resol_grid([resol(f"Ejercicio {i + 1}", figura(*e) + "\n" + resolucion(*e)[0])
                  for i, e in enumerate(EJERCICIOS)]), colapsable=True)
extras = g.seccion("Ejercicios extra", "extra",
    f'      <p class="enunciado">{PIDE}</p>\n'
    + g.grid([card(f"Bloque {i + 1}", "".join(figura(*e) for e in b)) for i, b in enumerate(EXTRAS)], 2),
    colapsable=True)

CSS = CSS_COMUN + """
    @media (max-width: 380px) { .sol.evals .katex-display { font-size: .72em; } .dato .katex-display { font-size: .74em; } }
    .enunciado.nota { margin-top: .8rem; color: var(--text-3); font-size: .88rem; }
    .grafica-wrap { display: flex; justify-content: center; margin: .2rem 0 .4rem; }
    .grafica-wrap svg.figura-rect { max-width: 150px; max-height: 90px; height: auto; }
    .ejemplo-block > .ej-line, .resol-item > .ej-line { text-align: center; }
    .dos-col { display: grid; grid-template-columns: 1fr 1fr; gap: .5rem 1.5rem; align-items: start; }
    @media (max-width: 620px) { .dos-col { grid-template-columns: 1fr; } }
    .paso-titulo { margin-top: 1.4rem; }
    @media (max-width: 480px) { .sol.evals .katex-display { font-size: .8em; } .sol .katex-display { font-size: .92em; } .dato .katex-display { font-size: .82em; } }
    .recta-svg { max-width: 100%; height: auto; display: block; margin: .3rem auto 0; }
    .graf-wrap { margin: .6rem 0; }
    .dato .resultado-pill { display: inline-block; }
"""
g.pagina("area-funcion-longitud", 6, "Área como función de la longitud",
         "Área de un rectángulo como función de la longitud: expresión del área, dominio y área máxima a partir de la gráfica.",
         [ejemplo, ejercicios, respuestas, extras],
         prev=("funcion-cuadratica.html", "Función cuadrática"), sig=("analisis-funcion.html", "Análisis de una función"), css_extra=CSS)
print("ok tema 6")
