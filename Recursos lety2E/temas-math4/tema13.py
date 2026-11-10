"""Math 4 · Tema 13 · Transformación de funciones — página con graficador integrado.

Fuente: letymath.com/matemáticas-4/transformación-de-funciones-y-clasificacion (la lista de
funciones de la Actividad 2) + lo acordado con Lety el 9-nov-2026: explorador con deslizadores
(subir/bajar, izquierda/derecha, reflejar, estirar/comprimir), sus ejercicios con "ver gráfica",
una práctica con objetivo (encimar la gráfica morada) y una evaluación de 10 reactivos al azar
(5 de acomodar la gráfica dada la regla, 5 de elegir la regla entre cinco opciones) que sólo dice el
resultado al final; pasa con 8. Ella evalúa uno a uno en su cubículo.

El JS vive en tema13.js (junto a este archivo) y se incrusta en la página: sin librerías. La
página NO lleva fórmulas en $…$ — se arman en HTML desde el JS, con las tipografías de KaTeX
que ya trae el sitio — así que prerender-katex.js no tiene nada que convertir aquí.
"""
import pathlib, re
from comun import g as G, CSS_COMUN

AQUI = pathlib.Path(__file__).parent
V = "<i>x</i>"
F = lambda s: f'<span class="tf-formula tf-enlinea">{s}</span>'

MOVS = [
    (F(f"<i>f</i>({V}) + <i>k</i>"), "sube <i>k</i> unidades"),
    (F(f"<i>f</i>({V}) − <i>k</i>"), "baja <i>k</i> unidades"),
    (F(f"<i>f</i>({V} − <i>h</i>)"), "se mueve <i>h</i> unidades a la <strong>derecha</strong>"),
    (F(f"<i>f</i>({V} + <i>h</i>)"), "se mueve <i>h</i> unidades a la <strong>izquierda</strong>"),
    (F(f"−<i>f</i>({V})"), "se refleja respecto al eje <i>x</i>"),
    (F(f"<i>a</i> <i>f</i>({V}), con <i>a</i> mayor que 1"), "se estira"),
    (F(f"<i>a</i> <i>f</i>({V}), con <i>a</i> entre 0 y 1"), "se comprime"),
]
filas = "\n".join(f'          <div class="tf-regla"><span>{a}</span><span>{b}</span></div>' for a, b in MOVS)
ap = G.seccion("Apuntes", "apuntes",
    '      <div class="regla-unica">\n'
    '        <p>Cada familia de funciones tiene una <strong>forma</strong>. Si conoces la forma de la función base, '
    'los números de la regla te dicen cómo se <strong>mueve</strong> la gráfica.</p>\n'
    f'        <div class="tf-reglas">\n{filas}\n        </div>\n'
    '        <p>Ojo: lo que está <strong>dentro</strong> con la <i>x</i> se mueve al revés de lo que parece — '
    f'{F(f"({V} − 3)")} va a la derecha y {F(f"({V} + 3)")} a la izquierda.</p>\n'
    '      </div>')

explorador = G.seccion("Explora", "video",
    '      <p class="enunciado">Elige una familia y mueve los controles. La línea punteada es la función base.</p>\n'
    '      <div id="tf-explorador" class="tf-caja">\n        <div class="tf-fams"></div>\n        <div class="tf-lab"></div>\n      </div>'
).replace("<polygon points=\"5 3 19 12 5 21 5 3\" stroke-width=\"0\" fill=\"white\"/>",
          '<path d="M3 17c4-12 6-12 9 0s5 12 9 0"/>')

practica = G.seccion("Práctica: llega a la gráfica morada", "ejemplo",
    '      <p class="enunciado">Ahora hay un <strong>objetivo</strong>: mueve tu gráfica rosa hasta que quede '
    'exactamente encima de la <strong class="tf-morada">morada</strong>. Cuando llegues, lee la regla que se formó.</p>\n'
    '      <div id="tf-practica" class="tf-caja">\n        <p class="tf-fam"></p>\n        <div class="tf-lab"></div>\n'
    '        <p class="tf-aviso tf-pend"></p>\n'
    '        <div class="tf-acciones"><button type="button" class="tf-btn tf-otra-meta">Otra gráfica</button></div>\n      </div>')

ejercicios = G.seccion("Ejercicios", "ejercicios",
    '      <p class="enunciado">Ahora sin controles: con los movimientos que ya conoces, haz el esbozo de cada función '
    '<strong>en tu cuaderno</strong>. Toca la función <strong>sólo después</strong> de dibujarla, para verificar.</p>\n'
    '      <div id="tf-ejercicios" class="bloques-2"></div>')

evalua = G.seccion("Evaluación", "respuestas",
    '      <div id="tf-evalua" class="tf-caja">\n'
    '        <div class="tf-inicio">\n'
    '          <p class="enunciado">Son <strong>10 reactivos</strong> al azar con todos los movimientos:</p>\n'
    '          <div class="tf-modos">\n'
    '            <div class="tf-modo">\n              <h3>5 de acomodar</h3>\n'
    '              <p>Aparece la regla de correspondencia y tú acomodas la gráfica con los controles, sin ver la respuesta.</p>\n            </div>\n'
    '            <div class="tf-modo">\n              <h3>5 de elegir</h3>\n'
    '              <p>Aparece la gráfica ya transformada y eliges su regla de correspondencia entre cinco opciones.</p>\n            </div>\n'
    '          </div>\n'
    '          <p class="enunciado">La revisión es <strong>hasta el final</strong>. Se pasa con <strong>8 de 10</strong> y se presenta con tu profesora.</p>\n'
    '          <div class="tf-arranque">\n'
    '            <label class="tf-lbl" for="tf-nombre">Tu nombre</label>\n'
    '            <input id="tf-nombre" class="tf-nombre" type="text" autocomplete="off" maxlength="60">\n'
    '            <button type="button" class="tf-btn tf-go-eval">Presentar evaluación</button>\n          </div>\n'
    '          <p class="enunciado nota">Para acreditar el tema también se entrega la <strong>infografía</strong> sobre transformación de funciones.</p>\n'
    '        </div>\n'
    '        <div class="tf-corre" hidden>\n'
    '          <p class="tf-num"></p>\n          <p class="tf-fam"></p>\n          <p class="tf-pide"></p>\n'
    '          <div class="tf-lab"></div>\n'
    '          <div class="tf-elige" hidden>\n            <div class="tf-plano"></div>\n            <div class="tf-ops"></div>\n          </div>\n'
    '          <div class="tf-acciones"><button type="button" class="tf-btn tf-sig">Siguiente</button></div>\n'
    '        </div>\n'
    '        <div class="tf-fin" hidden>\n          <div class="tf-resultado"></div>\n'
    '          <div class="tf-acciones"><button type="button" class="tf-btn tf-otra">Nuevo intento</button></div>\n'
    '        </div>\n'
    '      </div>')

CSS = CSS_COMUN + """
    /* ── fórmulas en HTML, con las tipografías de KaTeX del sitio ── */
    .tf-formula { font-family: KaTeX_Main, 'Times New Roman', serif; font-size: 1.3rem; line-height: 1.5;
                  text-align: center; color: var(--text); white-space: nowrap; min-height: 2.4rem; }
    .tf-formula i { font-family: KaTeX_Math, KaTeX_Main, serif; font-style: italic; }
    .tf-formula sup { font-size: .7em; }
    .tf-formula.tf-enlinea { display: inline-block; font-size: 1.1em; min-height: 0; line-height: 1.2; }
    .tf-formula .fr { display: inline-flex; flex-direction: column; vertical-align: middle; text-align: center; margin: 0 .15em; line-height: 1.15; }
    .tf-formula .fr > span:first-child { border-bottom: 1px solid currentColor; padding: 0 .25em; }
    .tf-formula .fr > span:last-child { padding: 0 .25em; }
    .tf-formula .rz > span { border-top: 1px solid currentColor; padding: 0 .12em; margin-left: -.05em; }

    .tf-reglas { display: grid; gap: .1rem; margin: .8rem auto; max-width: 30rem; text-align: left; }
    .tf-regla { display: grid; grid-template-columns: 1fr 1.2fr; gap: .8rem; align-items: center;
                padding: .35rem .2rem; border-bottom: 1px solid var(--border-s); font-size: .93rem; color: var(--text-2); }
    .tf-regla:last-child { border-bottom: none; }
    .tf-regla > span:first-child { text-align: right; white-space: normal; }
    @media (max-width: 480px) { .tf-regla { grid-template-columns: 1fr; gap: 0; text-align: center; }
                                .tf-regla > span:first-child { text-align: center; } }

    .tf-caja { background: var(--bg-card); border: 1.5px solid var(--border); border-radius: var(--r-md); padding: 1.1rem; }
    .tf-fams, .tf-lista { display: flex; flex-wrap: wrap; gap: .4rem; justify-content: center; }
    .tf-fams { margin-bottom: .8rem; }
    .tf-chip, .tf-fn { border: 1.5px solid var(--border); background: var(--bg-card); color: var(--text-2);
                       border-radius: 99px; padding: .35rem .8rem; font: inherit; font-size: .88rem; cursor: pointer; }
    .tf-chip[aria-pressed="true"], .tf-fn[aria-pressed="true"] { background: var(--accent); border-color: var(--accent); color: #fff; }
    .tf-fn { font-family: KaTeX_Main, 'Times New Roman', serif; font-size: 1.02rem; border-radius: 12px; white-space: nowrap; color: var(--text); }
    .tf-fn i { font-family: KaTeX_Math, KaTeX_Main, serif; }
    .tf-fn sup { font-size: .7em; }
    .tf-fn .fr { display: inline-flex; flex-direction: column; vertical-align: middle; text-align: center; margin: 0 .15em; line-height: 1.1; }
    .tf-fn .fr > span:first-child { border-bottom: 1px solid currentColor; padding: 0 .2em; }
    .tf-fn .rz > span { border-top: 1px solid currentColor; padding: 0 .12em; }
    .tf-ver { margin-top: .9rem; text-align: center; }

    .tf-plano, .tf-ver { text-align: center; }
    .tf-svg { width: 100%; max-width: 380px; height: auto; background: var(--bg-card); }
    .tf-mov { text-align: center; font-size: .85rem; color: var(--text-3); min-height: 1.4rem; margin: .2rem 0 .5rem; }
    .tf-ctls { display: grid; gap: .5rem; max-width: 420px; margin: 0 auto; }
    .tf-ctl { display: grid; grid-template-columns: 2.2rem 1fr 2.2rem 2rem; gap: .4rem; align-items: center; }
    .tf-ctl-n { grid-column: 1 / -1; font-size: .72rem; font-weight: 700; text-transform: uppercase; letter-spacing: .06em;
                color: var(--text-3); margin-bottom: -.3rem; }
    .tf-ctl input[type=range] { width: 100%; accent-color: var(--M); min-width: 0; }
    .tf-ctl output { font-weight: 700; color: var(--accent); text-align: center; }
    .tf-paso { width: 2.2rem; height: 2.2rem; border-radius: 50%; border: 1.5px solid var(--border); background: var(--bg-card);
               color: var(--accent); font-size: 1.2rem; line-height: 1; cursor: pointer; }
    .tf-ctl-ref { grid-template-columns: 1fr 1fr; margin-top: .3rem; }
    .tf-ref, .tf-cero { border: 1.5px solid var(--border); background: var(--bg-card); color: var(--text-2); border-radius: 99px;
                        padding: .5rem .6rem; font: inherit; font-size: .88rem; cursor: pointer; }
    .tf-ref[aria-pressed="true"] { background: var(--M); border-color: var(--M); color: #fff; }

    .tf-modos { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: .4rem 0 .8rem; }
    @media (max-width: 620px) { .tf-modos { grid-template-columns: 1fr; } }
    .tf-modo { border: 1px solid var(--border-s); border-radius: var(--r-md); padding: 1rem; text-align: center; display: flex; flex-direction: column; gap: .5rem; }
    .tf-modo h3 { margin: 0; color: var(--accent); font-size: 1.05rem; }
    .tf-modo p { margin: 0; font-size: .9rem; color: var(--text-2); line-height: 1.6; flex: 1; }
    .tf-lbl { font-size: .72rem; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: var(--text-3); }
    .tf-nombre { font: inherit; padding: .5rem .7rem; border: 1.5px solid var(--border); border-radius: 10px; text-align: center; width: 100%; box-sizing: border-box; }
    .tf-btn { border: none; background: var(--accent); color: #fff; border-radius: 99px; padding: .65rem 1.4rem; font: inherit; font-weight: 600; cursor: pointer; }
    .tf-btn:hover { background: var(--M); }
    .tf-acciones { text-align: center; margin-top: 1rem; }
    .tf-num { margin: 0; text-align: center; font-size: .72rem; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; color: var(--course-1); }
    .tf-fam { margin: .2rem 0 0; text-align: center; font-weight: 700; color: var(--accent); }
    .tf-pide { margin: .3rem 0 .7rem; text-align: center; color: var(--text-2); line-height: 2; }
    .tf-morada { color: #7B2CBF; }
    .tf-aviso { text-align: center; margin: .8rem 0 0; padding: .6rem; border-radius: 12px; line-height: 2; }
    .tf-bien { color: var(--accent); }
    .tf-mal { color: var(--M); }
    .tf-aviso.tf-bien, .tf-aviso.tf-mal { background: var(--accent-light); }
    .tf-aviso.tf-pend { color: var(--text-3); font-size: .9rem; }
    .tf-aviso.tf-bien { font-weight: 700; }
    .tf-arranque { display: grid; gap: .5rem; max-width: 20rem; margin: 1rem auto .6rem; text-align: center; }
    .tf-ops { display: grid; gap: .5rem; max-width: 22rem; margin: .8rem auto 0; }
    .tf-op { border: 1.5px solid var(--border); background: var(--bg-card); color: var(--text); border-radius: 14px;
             padding: .55rem .8rem; cursor: pointer; font-family: KaTeX_Main, 'Times New Roman', serif; font-size: 1.15rem; white-space: nowrap; }
    .tf-op i { font-family: KaTeX_Math, KaTeX_Main, serif; }
    .tf-op sup { font-size: .7em; }
    .tf-op .fr { display: inline-flex; flex-direction: column; vertical-align: middle; text-align: center; margin: 0 .15em; line-height: 1.1; }
    .tf-op .fr > span:first-child { border-bottom: 1px solid currentColor; padding: 0 .2em; }
    .tf-op .rz > span { border-top: 1px solid currentColor; padding: 0 .12em; }
    .tf-op[aria-pressed="true"] { background: var(--accent); border-color: var(--accent); color: #fff; }
    [hidden] { display: none !important; }
    .tf-mov-in { font-size: .85rem; color: var(--text-3); }
    .tf-quien { text-align: center; margin: 0; color: var(--text-3); font-size: .9rem; }
    .tf-marca { text-align: center; margin: .2rem 0 0; font-family: 'Playfair Display', serif; font-size: 3rem; font-weight: 700; color: var(--accent); line-height: 1.2; }
    .tf-veredicto { text-align: center; margin: 0 0 1rem; font-weight: 700; font-size: 1.15rem; }
    .tf-tabla { display: grid; gap: .1rem; max-width: 30rem; margin: 0 auto; }
    .tf-fila { display: grid; grid-template-columns: 1.6rem 1fr 1.6rem; gap: .5rem; align-items: center; padding: .45rem .2rem; border-bottom: 1px solid var(--border-s); }
    .tf-fila .tf-n { font-weight: 700; color: var(--text-3); font-size: .85rem; }
    .tf-fila .tf-que { color: var(--text); display: flex; flex-direction: column; }
    .tf-fila small { color: var(--text-3); font-size: .78rem; }
    .tf-fila .tf-res { font-weight: 700; font-size: 1.1rem; text-align: right; }
    .enunciado.nota { margin: .4rem 0 0; color: var(--text-3); font-size: .88rem; }
"""

G.pagina("transformacion-funciones", 13, "Transformación de funciones",
         "Transformación de funciones: mueve, refleja, estira y comprime la gráfica con un graficador, y presenta la evaluación.",
         [ap, explorador, practica, ejercicios, evalua],
         prev=("ecuaciones-exponenciales-logaritmicas.html", "Ecuaciones exponenciales y logarítmicas"),
         sig=("sucesiones-series.html", "Sucesiones y series"), css_extra=CSS)

# La página no usa KaTeX JS: se quitan sus <script> y se incrusta el del graficador.
p = G.RAIZ / G.DIR / "transformacion-funciones.html"
s = p.read_text()
s, n = re.subn(r'\s*<script defer src="\.\./\.\./assets/katex/katex\.min\.js"></script>\s*<script defer src="\.\./\.\./assets/katex/contrib/auto-render\.min\.js".*?</script>',
               "", s, flags=re.S)
assert n == 1
js = (AQUI / "tema13.js").read_text()
assert "$" not in js and "</script" not in js
s = s.replace('  <script src="../../nav.js"></script>', '  <script>\n' + js + '  </script>\n  <script src="../../nav.js"></script>')
assert "$" not in s, "la página no debe llevar signos de pesos"
p.write_text(s)
print("ok tema 13")
