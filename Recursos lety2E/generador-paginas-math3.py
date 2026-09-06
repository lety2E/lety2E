"""Generador de páginas de tema para Matemáticas 3 (lety2e.com).

Reglas del proyecto que respeta:
- Nunca el signo × ; multiplicadores sólo entre paréntesis y en color.
- Cada renglón de ejercicio es un bloque (.ej-line), nunca $..$<br>.
- Video con facade .yt-lite, nunca <iframe> directo.
- Extras: 10 por tema, en dos tarjetas "Bloque 1"/"Bloque 2", SIN numerar.
"""
import pathlib

RAIZ = pathlib.Path("/Users/letymath/Desktop/lety2E")
D, S = "$$", "$"
IZQ, DER = "#7B2CBF", "#FF00AA"

ICONO = {
 "video": '<polygon points="5 3 19 12 5 21 5 3" stroke-width="0" fill="white"/>',
 "ejemplo": '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>',
 "ejercicios": '<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>',
 "respuestas": '<polyline points="20 6 9 17 4 12"/>',
 "extra": '<path d="M12 5v14M5 12h14"/>',
 "apuntes": '<path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>',
}

def estilos(extra=""):
    """El <style> canónico del curso (tomado del tema 1) + lo propio del tema."""
    base = (RAIZ / "math/matematicas-3/sumas-restas.html").read_text()
    st = base[base.index("  <style>"):base.index("</style>") + 8]
    if extra:
        st = st.replace("  </style>", extra + "\n  </style>")
    return st

CSS_GRAFICA = """    .despeje { text-align: center; }
    .formula-pill {
      display: inline-block; background: #FFF1A8;
      padding: .25rem .75rem; border-radius: 99px;
      font-size: .9rem; font-weight: 600; color: var(--text);
      margin: .25rem .2rem; border: 1.5px solid #F5DC6A;
    }
    .formula-pill.salmon { background: #FFD9B8; border-color: #F5B584; }
    .graf-wrap { display: flex; justify-content: center; margin: 1rem 0 .5rem; }
    .graf-svg { max-width: 240px; max-height: 380px; height: auto; }
    /* las pills con raíz o fracción necesitan más alto */
    .resultado-pill { padding: .4rem .8rem; line-height: 1.5; }"""

def aligned(lineas, ind=""):
    return f'{ind}{D}\\begin{{aligned}} ' + " \\\\ ".join(lineas) + f' \\end{{aligned}}{D}'

def cases(a, b):
    return f'{D}\\begin{{cases}} {a} \\\\ {b} \\end{{cases}}{D}'

def columna(titulo, clase, cuerpo, pill=None, ind="              "):
    s = f'{ind}<div class="elim-col">\n{ind}  <div class="paso-titulo {clase}">{titulo}</div>\n'
    s += "\n".join(f'{ind}  {l}' for l in cuerpo.strip().split("\n")) + "\n"
    if pill:
        s += f'{ind}  <span class="resultado-pill">{S}{pill}{S}</span>\n'
    return s + f'{ind}</div>'

def dos_columnas(c1, c2, ind="            "):
    return f'{ind}<div class="elim-grid">\n{c1}\n{c2}\n{ind}</div>'

def comprobacion(l1, l2, ind="            "):
    return (f'{ind}<div class="comprob">\n{ind}  <p class="comprob-titulo">Comprobación</p>\n'
            f'{ind}  <div class="elim-grid">\n'
            f'{ind}    <div class="elim-col">\n{ind}      {aligned(l1)}\n{ind}    </div>\n'
            f'{ind}    <div class="elim-col">\n{ind}      {aligned(l2)}\n{ind}    </div>\n'
            f'{ind}  </div>\n{ind}</div>')

def mini_cards(titulos_y_cuerpos, ind="        "):
    """[(titulo, cuerpo_html)] -> tarjetas dentro de un .bloques-2"""
    return "\n".join(
        f'{ind}<div class="mini-card">\n{ind}  <div class="mini-card-head">{t}</div>\n'
        f'{ind}  <div class="mini-card-body">{c}</div>\n{ind}</div>'
        for t, c in titulos_y_cuerpos)

def cards_extra(items, ind="          "):
    """items: 10 cadenas ya formateadas en LaTeX inline -> dos bloques de cinco."""
    def card(t, grupo):
        ls = "\n".join(f'{ind}    <div class="ej-line">{S}{x}{S}</div>' for x in grupo)
        return (f'{ind}<div class="mini-card">\n{ind}  <div class="mini-card-head">{t}</div>\n'
                f'{ind}  <div class="mini-card-body">\n{ls}\n{ind}  </div>\n{ind}</div>')
    mitad = (len(items) + 1) // 2
    return card("Bloque 1", items[:mitad]) + "\n" + card("Bloque 2", items[mitad:])

def seccion(titulo, icono, cuerpo, colapsable=False):
    ic = f'<div class="sec-icon">\n          <svg viewBox="0 0 24 24">{ICONO[icono]}</svg>\n        </div>'
    if colapsable:
        return (f'    <section class="section-block">\n'
                f'      <div class="sec-toggle" onclick="this.classList.toggle(\'open\'); this.nextElementSibling.classList.toggle(\'show\');">\n'
                f'        {ic}\n        <h2>{titulo}</h2>\n        <span class="chev">▼</span>\n      </div>\n'
                f'      <div class="collapsible">\n{cuerpo}\n      </div>\n    </section>')
    return (f'    <section class="section-block">\n      <div class="sec-head">\n        {ic}\n'
            f'        <h2>{titulo}</h2>\n      </div>\n{cuerpo}\n    </section>')

def seccion_ejemplo(cuerpo, titulo="Ejemplo"):
    ic = f'<div class="sec-icon">\n          <svg viewBox="0 0 24 24">{ICONO["ejemplo"]}</svg>\n        </div>'
    return (f'    <section class="section-block ejemplo-section">\n      <div class="ejemplo-head">\n        {ic}\n'
            f'        <h3>{titulo}</h3>\n      </div>\n      <div class="ejemplo-block">\n{cuerpo}\n      </div>\n    </section>')

def seccion_video(vid, titulo):
    cuerpo = (f'      <div class="video-single">\n        <div class="video-wrapper">\n'
              f'          <button type="button" class="yt-lite" data-yt="{vid}" data-title="{titulo}" '
              f'aria-label="Reproducir video: {titulo}"></button>\n        </div>\n      </div>')
    return seccion("Video", "video", cuerpo)

def pagina(slug, num, titulo, desc, secciones, prev, sig, css_extra=""):
    """prev/sig: (href, texto) o None."""
    nav_prev = (f'<a href="{prev[0]}" class="btn-anterior">← {prev[1]}</a>' if prev
                else '<a href="index.html" class="btn-anterior">← Matemáticas 3</a>')
    nav_sig = (f'<a href="{sig[0]}" class="btn-siguiente">{sig[1]} →</a>' if sig
               else '<a href="index.html" class="btn-siguiente">Índice del curso →</a>')
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{titulo} — Matemáticas 3 — LetyMath</title>
  <meta name="description" content="{desc}" />
  <link rel="icon" href="../../favicon.svg" type="image/svg+xml">
  <link rel="icon" href="../../favicon.ico">
  <link rel="stylesheet" href="../../style.css">
  <link rel="stylesheet" href="../../assets/katex/katex.min.css" />
  <script defer src="../../assets/katex/katex.min.js"></script>
  <script defer src="../../assets/katex/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {{
      delimiters: [
        {{left:'$$', right:'$$', display:true}},
        {{left:'$', right:'$', display:false}}
      ]
    }});"></script>

{estilos(css_extra)}
</head>
<body data-section="math">
  <main class="topic-content">

    <header class="topic-header">
      <p class="breadcrumb">
        <a href="../index.html">Inicio</a> ›
        <a href="index.html">Matemáticas 3</a> ›
        {titulo}
      </p>
      <div class="topic-tag">Matemáticas 3 · Tema {num}</div>
      <h1>{titulo}</h1>
    </header>

{chr(10).join(chr(10).join([s, ""]) for s in secciones)}
    <!-- ══════════ NAVEGACIÓN ══════════ -->
    <div class="topic-nav-btns">
      {nav_prev}
      {nav_sig}
    </div>

  </main>
  <script src="../../nav.js"></script>
  <script src="../../footer.js"></script>
</body>
</html>
'''
    (RAIZ / f"math/matematicas-3/{slug}.html").write_text(html)
    return len(html)

def enlazar(slug_prev, slug_nuevo, texto_nuevo, emoji, titulo_card, desc_card, color):
    """Botón siguiente en el tema previo + card en el índice."""
    p = RAIZ / f"math/matematicas-3/{slug_prev}.html"
    s = p.read_text()
    s = s.replace('<a href="index.html" class="btn-siguiente">Índice del curso →</a>',
                  f'<a href="{slug_nuevo}.html" class="btn-siguiente">{texto_nuevo} →</a>')
    p.write_text(s)

    p = RAIZ / "math/matematicas-3/index.html"
    s = p.read_text()
    card = (f'\n      <a href="{slug_nuevo}.html" class="content-card" style="--card-accent: {color};">\n'
            f'        <span class="card-number">{emoji}</span>\n'
            f'        <h2>{titulo_card}</h2>\n        <p>{desc_card}</p>\n      </a>\n')
    s = s.replace('\n    </div>\n\n    <p class="proximamente-nota">', card + '\n    </div>\n\n    <p class="proximamente-nota">')
    p.write_text(s)

COLORES = ["#FF00AA", "#4A0080", "#00DEC8", "#7B2CBF"]
