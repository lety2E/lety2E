"""Math 4 · Tema 11 · Dominio máximo. Fuente: capturas (4 hojas de ejemplo, 4 bloques, resueltos).

Cada función es una tupla con su tipo; de ahí salen el enunciado, los pasos y el dominio:
  ("poli", tex)            polinomio                      → R
  ("cub", tex_de_adentro)  raíz cúbica                    → R
  ("rac", n, k)            n / (x² − k²)                  → R \\ {−k, k}
  ("racl", n, a, b)        n / (ax − b)                   → R \\ {b/a}
  ("raizc", k)             √(x² − k²)                     → (−∞, −k] ∪ [k, ∞)
  ("logc", k)              log(x² − k²)                   → (−∞, −k) ∪ (k, ∞)
  ("invraizc", n, k)       n / √(x² − k²)                 → (−∞, −k) ∪ (k, ∞)
  ("raizl", a, b)          √(ax − b)                      → [b/a, ∞)
  ("invraizl", n, a, b)    n / √(ax − b)                  → (b/a, ∞)
  ("logl", a, b)           log(ax + b)   (b con signo)    → (−b/a, ∞)
"""
from fractions import Fraction
from comun import g as G, CSS_COMUN, apuntes

INF = "\\infty"

def lin(a, b):                       # ax + b con signo
    ax = "x" if a == 1 else f"{a}x"
    return ax + (f" {'+' if b > 0 else '-'} {abs(b)}" if b else "")

def fr(q):
    q = Fraction(q)
    if q.denominator == 1:
        return str(q.numerator)
    return ("-" if q < 0 else "") + f"\\dfrac{{{abs(q.numerator)}}}{{{q.denominator}}}"

def cociente(num, den, op):
    """x op num/den, y si se puede simplificar, otro renglón."""
    q = Fraction(num, den)
    cruda = ("-" if num * den < 0 else "") + f"\\dfrac{{{abs(num)}}}{{{abs(den)}}}"
    l = [f"x &{op} {cruda}"]
    if fr(q) != cruda:
        l.append(f"x &{op} {fr(q)}")
    return l, q

def rayos(k, cerrado):
    """Recta con los dos rayos |x| > k (no va a escala, como el esquema de las hojas)."""
    W, H, y = 220, 44, 18
    xa, x0, xb = 70, 110, 150
    o = [f'<svg class="recta-svg" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'role="img" aria-label="Recta numérica con el dominio">',
         f'<line x1="8" y1="{y}" x2="{W - 8}" y2="{y}" stroke="#7B5A50" stroke-width="1.2"/>',
         f'<line x1="14" y1="{y}" x2="{xa}" y2="{y}" stroke="#FF00AA" stroke-width="3.2" stroke-linecap="round"/>',
         f'<line x1="{xb}" y1="{y}" x2="{W - 14}" y2="{y}" stroke="#FF00AA" stroke-width="3.2" stroke-linecap="round"/>',
         f'<path d="M8,{y} l7,-4.5 v9 z" fill="#FF00AA"/>', f'<path d="M{W - 8},{y} l-7,-4.5 v9 z" fill="#FF00AA"/>',
         f'<line x1="{x0}" y1="{y - 8}" x2="{x0}" y2="{y + 8}" stroke="#7B5A50" stroke-width="1.6"/>']
    for x, t in ((xa, -k), (xb, k)):
        if cerrado:
            o.append(f'<circle cx="{x}" cy="{y}" r="4.6" fill="#FF00AA"/>')
        else:
            o.append(f'<circle cx="{x}" cy="{y}" r="4.6" fill="#FBF2EF" stroke="#FF00AA" stroke-width="2.2"/>')
        o.append(f'<text x="{x}" y="{y + 20}" font-size="10" fill="#6E4F4F" text-anchor="middle" '
                 f'font-family="system-ui, sans-serif">{t}</text>')
    return "".join(o) + "</svg>"

def analiza(F):
    """→ (tex de f(x), pasos [renglones de aligned], svg o '', dominio tex)"""
    t = F[0]
    R = f"\\mathbb{{R}} \\quad (-{INF},\\,{INF})"
    if t == "poli":
        return F[1], [], "", R
    if t == "cub":
        return f"\\sqrt[3]{{{F[1]}}}", [], "", R
    if t == "racl":
        n, a, b = F[1:]
        l, q = cociente(b, a, "=")
        return (f"\\dfrac{{{n}}}{{{lin(a, -b)}}}", [f"{lin(a, -b)} &= 0", f"{a}x &= {b}"] + l, "",
                f"\\mathbb{{R}} \\setminus \\left\\{{{fr(q)}\\right\\}}")
    if t in ("rac", "raizc", "logc", "invraizc"):
        if t in ("rac", "invraizc"):
            n, k = F[1:]
        else:
            k = F[1]
        k2 = k * k
        if t == "rac":
            return (f"\\dfrac{{{n}}}{{x^2 - {k2}}}",
                    [f"x^2 - {k2} &= 0", f"x^2 &= {k2}", f"\\sqrt{{x^2}} &= \\sqrt{{{k2}}}", f"x &= \\pm {k}"], "",
                    f"\\mathbb{{R}} \\setminus \\{{-{k},\\,{k}\\}}")
        op = "\\ge" if t == "raizc" else ">"
        enun = {"raizc": f"\\sqrt{{x^2 - {k2}}}", "logc": f"\\log(x^2 - {k2})",
                "invraizc": f"\\dfrac{{{n if t == 'invraizc' else ''}}}{{\\sqrt{{x^2 - {k2}}}}}"}[t]
        dom = (f"(-{INF},\\,-{k}] \\cup [{k},\\,{INF})" if t == "raizc" else f"(-{INF},\\,-{k}) \\cup ({k},\\,{INF})")
        return (enun, [f"x^2 - {k2} &{op} 0", f"x^2 &{op} {k2}", f"\\sqrt{{x^2}} &{op} \\sqrt{{{k2}}}", f"|x| &{op} {k}"],
                rayos(k, t == "raizc"), dom)
    if t in ("raizl", "invraizl"):
        if t == "raizl":
            a, b = F[1:]; op = "\\ge"; enun = f"\\sqrt{{{lin(a, -b)}}}"
        else:
            n, a, b = F[1:]; op = ">"; enun = f"\\dfrac{{{n}}}{{\\sqrt{{{lin(a, -b)}}}}}"
        l, q = cociente(b, a, op)
        dom = f"[{fr(q)},\\,{INF})" if t == "raizl" else f"({fr(q)},\\,{INF})"
        return enun, [f"{lin(a, -b)} &{op} 0", f"{a}x &{op} {b}"] + l, "", dom
    if t == "logl":
        a, b = F[1:]
        l, q = cociente(-b, a, ">")
        return f"\\log({lin(a, b)})", [f"{lin(a, b)} &> 0", f"{a}x &> {-b}"] + l, "", f"\\left({fr(q)},\\,{INF}\\right)"
    raise ValueError(t)

def enunciado(F):
    return f"f(x) = {analiza(F)[0]}"

def resolucion(F, clase="dom-item"):
    enun, pasos, svg, dom = analiza(F)
    h = f'<div class="{clase}">\n<div class="ej-line">$f(x) = {enun}$</div>\n'
    if pasos:
        h += '<div class="sol">$$\\begin{aligned} ' + " \\\\ ".join(pasos) + ' \\end{aligned}$$</div>\n'
    if svg:
        h += f'<div class="graf-wrap">{svg}</div>\n'
    return h + f'<div class="dato"><span class="et">dominio</span>$\\boldsymbol{{{dom}}}$</div>\n</div>'

EJEMPLOS = [
    (("poli", "5x^8 - 6x^4 + 7x^2 - 3"),
     "Cuando es un <strong>polinomio</strong> el dominio es todos los números reales, de $-\\infty$ a $+\\infty$. "
     "Los polinomios pueden tener diferentes coeficientes, un solo término, etc.: cualquier forma que tengan, el dominio será $\\mathbb{R}$."),
    (("racl", 3, 5, 4),
     "En una <strong>fracción</strong> se toma el polinomio del denominador y se iguala a 0. Ese resultado es el único que "
     "no va en el dominio, pues con él queda 0 en el denominador."),
    (("raizl", 4, 20),
     "En una <strong>raíz cuadrada</strong> lo de adentro no puede dar un número negativo, pues la raíz cuadrada de un negativo no existe: "
     "se pone $\\ge$. Para el 5 se usa corchete porque sí se incluye; para el infinito siempre se usa paréntesis."),
    (("logl", 5, -3),
     "En un <strong>logaritmo</strong> lo de adentro tiene que ser siempre positivo, mayor a 0: se pone $>$. "
     "El $\\frac{3}{5}$ va con paréntesis porque no se incluye."),
    (("logc", 4),
     "Cuando uno de los términos está al cuadrado se resuelve igual, como desigualdad; el valor absoluto se expresa como un intervalo."),
    (("raizc", 2),
     "El valor absoluto de un número siempre es positivo: $|x| \\ge 2$ significa que el valor absoluto de $x$ es mayor o igual a dos."),
    (("invraizc", 7, 1),
     "Con la <strong>raíz en el denominador</strong> la única condición es que el denominador no puede ser igual a 0: "
     "se resuelve como desigualdad, estrictamente mayor a 0."),
]

def bloque(p1, c, k1, rl, rac, k2, ll, kl, p2, inv):
    return [("poli", p1), ("cub", c), ("raizc", k1), ("raizl",) + rl, ("rac",) + rac,
            ("raizc", k2), ("logl",) + ll, ("logc", kl), ("poli", p2), ("invraizl",) + inv]
BLOQUES = [
    bloque("2x^2 + 3", "x^3", 5, (3, 12), (3, 2), 3, (2, 1), 4, "4 - 8x", (5, 2, 6)),
    bloque("5x^2 - 1", "x^3 - 1", 2, (5, 20), (5, 1), 4, (5, -2), 10, "3 - 5x", (1, 3, 15)),
    bloque("7x^2 + 5", "x^3 + 125", 9, (2, 8), (4, 3), 5, (6, -4), 7, "2 - 7x", (8, 5, 10)),
    bloque("-3x^2 - 7", "x^3 - 8", 6, (7, 28), (2, 5), 8, (9, 5), 2, "6x - 3", (7, 6, 42)),
]
EXTRAS = [
    bloque("4x^3 - 2x + 9", "x^3 + 27", 7, (6, 18), (6, 6), 1, (4, -3), 3, "5 - 2x", (3, 4, 8)),
    bloque("-x^4 + 6x^2", "x^3 - 64", 10, (9, 27), (9, 8), 11, (7, 2), 9, "8x + 1", (2, 7, 35)),
]

# ── dominios de la hoja de resueltos, en el orden de la hoja de ejercicios ──
def doms(B):
    return [analiza(F)[3].replace("\\,", "").replace("\\left", "").replace("\\right", "") for F in B]
Rr = "\\mathbb{R} \\quad (-\\infty,\\infty)"
def esperado(k1, v_rl, kr, k2, v_ll, kl, v_inv):
    I = "\\infty"
    return [Rr, Rr, f"(-{I},-{k1}] \\cup [{k1},{I})", f"[{v_rl},{I})", f"\\mathbb{{R}} \\setminus \\{{-{kr},{kr}\\}}",
            f"(-{I},-{k2}] \\cup [{k2},{I})", f"({v_ll},{I})", f"(-{I},-{kl}) \\cup ({kl},{I})", Rr, f"({v_inv},{I})"]
assert doms(BLOQUES[0]) == esperado(5, 4, 2, 3, "-\\dfrac{1}{2}", 4, 3), doms(BLOQUES[0])
assert doms(BLOQUES[1]) == esperado(2, 4, 1, 4, "\\dfrac{2}{5}", 10, 5), doms(BLOQUES[1])
assert doms(BLOQUES[2]) == esperado(9, 4, 3, 5, "\\dfrac{2}{3}", 7, 2), doms(BLOQUES[2])   # la hoja deja 4/6 sin simplificar
assert doms(BLOQUES[3]) == esperado(6, 4, 5, 8, "-\\dfrac{5}{9}", 2, 7), doms(BLOQUES[3])
for B in EXTRAS:
    doms(B)
fuente = {F for B in BLOQUES for F in B} | {e[0] for e in EJEMPLOS}      # las hojas sí repiten algunas entre bloques
nuevas = [F for B in EXTRAS for F in B]
assert len(set(nuevas)) == len(nuevas) and not (set(nuevas) & fuente), "un extra repite un ejercicio"
print("dominios = hoja")

def card_bloque(titulo, B):
    filas = "\n".join(f'          <div class="ej-line">${enunciado(F)}$</div>' for F in B)
    return (f'        <div class="mini-card">\n          <div class="mini-card-head">{titulo}</div>\n'
            f'          <div class="mini-card-body">\n{filas}\n          </div>\n        </div>')

ej_html = "\n".join(
    f'        <div class="dom-ejemplo">\n{resolucion(F, "dom-item sin-borde")}\n'
    f'        <p class="enunciado nota">{nota}</p>\n        </div>' for F, nota in EJEMPLOS)
ejemplo = G.seccion_ejemplo(
    '        <p class="enunciado">Encuentra el dominio de las siguientes funciones.</p>\n'
    f'        <div class="dom-ejemplos">\n{ej_html}\n        </div>', titulo="Ejemplos")
video = G.seccion_video(["XVAAzSoEvMc", "slz13tHd7LU"], "Dominio máximo")
ejercicios = G.seccion("Ejercicios", "ejercicios",
    '      <p class="enunciado">Encuentra el dominio de las siguientes funciones.</p>\n'
    + G.grid([card_bloque(f"Bloque {i + 1}", B) for i, B in enumerate(BLOQUES)], 2))
respuestas = G.seccion("Respuestas", "respuestas",
    G.resol_grid([f'          <div class="resol-item">\n            <div class="resol-num">Bloque {i + 1}</div>\n'
                  f'            <div class="dom-grid">\n' + "\n".join(resolucion(F) for F in B)
                  + '\n            </div>\n          </div>' for i, B in enumerate(BLOQUES)]), colapsable=True)
extras = G.seccion("Ejercicios extra", "extra",
    '      <p class="enunciado">Encuentra el dominio de las siguientes funciones.</p>\n'
    + G.grid([card_bloque(f"Bloque {i + 1}", B) for i, B in enumerate(EXTRAS)], 2), colapsable=True)

CSS = CSS_COMUN + """
    .enunciado.nota { margin: .5rem 0 0; color: var(--text-3); font-size: .88rem; }
    .dom-ejemplos { display: grid; grid-template-columns: 1fr 1fr; gap: 1.6rem 1.4rem; }
    @media (max-width: 760px) { .dom-ejemplos { grid-template-columns: 1fr; } }
    .dom-ejemplo { border: 1.5px solid var(--border); border-radius: var(--r-md); padding: 1rem 1rem 1.1rem; }
    .dom-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: .9rem; }
    @media (max-width: 900px) { .dom-grid { grid-template-columns: 1fr 1fr; } }
    @media (max-width: 520px) { .dom-grid { grid-template-columns: 1fr; } }
    .dom-item { border: 1px solid var(--border-s); border-radius: var(--r-md); padding: .7rem .6rem; text-align: center; }
    .dom-item.sin-borde { border: none; padding: 0; }
    .dom-item .ej-line { text-align: center; }
    .recta-svg { max-width: 100%; height: auto; display: block; margin: .2rem auto 0; }
    .dato { font-size: .95rem; color: var(--M); }
    .mini-card-body { text-align: center; }
"""
G.pagina("dominio-maximo", 11, "Dominio máximo",
         "Dominio máximo de una función: polinomios, fracciones, raíces y logaritmos, con ejemplos y ejercicios resueltos.",
         [video, ejemplo, ejercicios, respuestas, extras],
         prev=("composicion-funciones.html", "Composición de funciones"),
         sig=("ecuaciones-exponenciales-logaritmicas.html", "Ecuaciones exponenciales y logarítmicas"), css_extra=CSS)
print("ok tema 11")
