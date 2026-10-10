"""Generador de páginas de tema para Matemáticas 4 (lety2e.com).

Hermano de `generador-paginas-math3.py`: mismo esqueleto de página, pero apuntando
a `math/matematicas-4/` y con los ayudantes que pide este curso (funciones).

Reglas del proyecto que respeta:
- Nunca el signo × ; multiplicadores sólo entre paréntesis.
- Cada renglón de ejercicio es un bloque (.ej-line / .sol), nunca $..$<br>.
- Video con facade .yt-lite, nunca <iframe> directo.
- Extras: al menos 10 por tema, en tarjetas, SIN numerar uno por uno.
- Las etiquetas dentro de cajitas se estilan con `> div > span:first-child`,
  nunca con un selector suelto de `span` (desarma KaTeX).
"""
import pathlib

RAIZ = pathlib.Path("/Users/letymath/Desktop/lety2E")
CURSO = "Matemáticas 4"
DIR = "math/matematicas-4"
# de dónde se copia el <style> canónico (mismo CSS base que Math 3)
BASE_CSS = RAIZ / "math/matematicas-3/sumas-restas.html"
D, S = "$$", "$"

ICONO = {
 "video": '<polygon points="5 3 19 12 5 21 5 3" stroke-width="0" fill="white"/>',
 "ejemplo": '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>',
 "ejercicios": '<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>',
 "respuestas": '<polyline points="20 6 9 17 4 12"/>',
 "extra": '<path d="M12 5v14M5 12h14"/>',
 "apuntes": '<path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>',
}

def estilos(extra=""):
    base = BASE_CSS.read_text()
    st = base[base.index("  <style>"):base.index("</style>") + 8]
    if extra:
        st = st.replace("  </style>", extra + "\n  </style>")
    return st

def aligned(lineas, ind=""):
    return f'{ind}{D}\\begin{{aligned}} ' + " \\\\ ".join(lineas) + f' \\end{{aligned}}{D}'

# ── Ejercicios: tarjeta "dadas las funciones / encuentra" ──────────────────
def card_funciones(titulo, funciones, pide, ind="        "):
    fs = "\n".join(f'{ind}    <div class="ej-line">{S}{f}{S}</div>' for f in funciones)
    ps = "\n".join(f'{ind}      <span>{S}{p}{S}</span>' for p in pide)
    return (f'{ind}<div class="mini-card">\n'
            f'{ind}  <div class="mini-card-head">{titulo}</div>\n'
            f'{ind}  <div class="mini-card-body">\n'
            f'{ind}    <p class="ej-sub">dadas las funciones</p>\n{fs}\n'
            f'{ind}    <p class="ej-sub ej-sub-2">encuentra</p>\n'
            f'{ind}    <div class="pide-lista">\n{ps}\n{ind}    </div>\n'
            f'{ind}  </div>\n{ind}</div>')

def grid(cards, cols=2, ind="      "):
    return f'{ind}<div class="bloques-{cols}">\n' + "\n".join(cards) + f'\n{ind}</div>'

# ── Respuestas: un .resol-item por bloque, cada solución en su .sol ────────
def resol_bloque(titulo, soluciones, ind="          "):
    ls = "\n".join(f'{ind}    <div class="sol">{s}</div>' for s in soluciones)
    return (f'{ind}<div class="resol-item">\n'
            f'{ind}  <div class="resol-num">{titulo}</div>\n{ls}\n{ind}</div>')

def resol_grid(items, ind="        "):
    return f'{ind}<div class="resol-grid">\n' + "\n".join(items) + f'\n{ind}</div>'

# ── Secciones ─────────────────────────────────────────────────────────────
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

def seccion_video(vids, titulo):
    """vids: un id o una lista de ids (dos videos van lado a lado)."""
    if isinstance(vids, str):
        vids = [vids]
    botones = "\n".join(
        f'        <div class="video-wrapper">\n'
        f'          <button type="button" class="yt-lite" data-yt="{v}" data-title="{titulo}" '
        f'aria-label="Reproducir video: {titulo}"></button>\n        </div>'
        for v in vids)
    clase = "video-single" if len(vids) == 1 else "video-pair"
    return seccion("Video" if len(vids) == 1 else "Videos", "video",
                   f'      <div class="{clase}">\n{botones}\n      </div>')

# ── Página completa ───────────────────────────────────────────────────────
def pagina(slug, num, titulo, desc, secciones, prev, sig, css_extra=""):
    """prev/sig: (href, texto) o None."""
    nav_prev = (f'<a href="{prev[0]}" class="btn-anterior">← {prev[1]}</a>' if prev
                else f'<a href="index.html" class="btn-anterior">← {CURSO}</a>')
    nav_sig = (f'<a href="{sig[0]}" class="btn-siguiente">{sig[1]} →</a>' if sig
               else '<a href="index.html" class="btn-siguiente">Índice del curso →</a>')
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{titulo} — {CURSO} — LetyMath</title>
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
        <a href="index.html">{CURSO}</a> ›
        {titulo}
      </p>
      <div class="topic-tag">{CURSO} · Tema {num}</div>
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
    (RAIZ / f"{DIR}/{slug}.html").write_text(html)
    return len(html)

def enlazar(slug_prev, slug_nuevo, texto_nuevo, emoji, titulo_card, desc_card, color):
    """Botón siguiente en el tema previo + card en el índice del curso."""
    if slug_prev:
        p = RAIZ / f"{DIR}/{slug_prev}.html"
        s = p.read_text()
        s = s.replace('<a href="index.html" class="btn-siguiente">Índice del curso →</a>',
                      f'<a href="{slug_nuevo}.html" class="btn-siguiente">{texto_nuevo} →</a>')
        p.write_text(s)

    p = RAIZ / f"{DIR}/index.html"
    s = p.read_text()
    card = (f'      <a href="{slug_nuevo}.html" class="content-card" style="--card-accent: {color};">\n'
            f'        <span class="card-number">{emoji}</span>\n'
            f'        <h2>{titulo_card}</h2>\n        <p>{desc_card}</p>\n      </a>\n\n')
    s = s.replace('    </div>\n\n    <p class="proximamente-nota">', card + '    </div>\n\n    <p class="proximamente-nota">')
    p.write_text(s)

COLORES = ["#FF00AA", "#4A0080", "#00DEC8", "#7B2CBF"]
