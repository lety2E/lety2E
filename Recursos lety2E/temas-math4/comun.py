"""Carga los generadores de Recursos (tienen guiones en el nombre)."""
import importlib.util, pathlib
REC = pathlib.Path("/Users/letymath/Desktop/lety2E/Recursos lety2E")

def cargar(nombre):
    spec = importlib.util.spec_from_file_location(nombre.replace("-", "_"), REC / f"{nombre}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

g = cargar("generador-paginas-math4")

CSS_COMUN = """
    /* ── Apuntes ── */
    .regla-unica {
      background: var(--bg-card); border: 1.5px solid var(--border);
      border-radius: var(--r-md); padding: 1.4rem 1.5rem;
      text-align: center; color: var(--text);
    }
    .regla-unica p { margin: 0 0 .4rem; line-height: 1.75; color: var(--text-2); font-size: .95rem; }
    .regla-unica p:not(:first-child) { margin-top: .6rem; }
    .enunciado {
      margin: 0 0 1rem; font-size: .95rem; line-height: 1.8;
      color: var(--text-2); text-align: center;
    }
    .parte-titulo {
      font-size: .78rem; font-weight: 700; text-transform: uppercase; letter-spacing: .08em;
      color: var(--course-1); text-align: center; margin: 1.6rem 0 .3rem;
    }
    .parte-titulo:first-of-type { margin-top: .2rem; }
    .bloques-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
    @media (max-width: 700px) { .bloques-3 { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 480px) { .bloques-3 { grid-template-columns: 1fr; } }
    .video-pair { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
    @media (max-width: 700px) { .video-pair { grid-template-columns: 1fr; } }
    .resol-2col { display: grid; grid-template-columns: 1fr auto; gap: 1.3rem; align-items: center; }
    @media (max-width: 700px) { .resol-2col { grid-template-columns: 1fr; justify-items: center; } }
    .dato { padding: .3rem 0; text-align: center; }
    .dato .et {
      display: block; font-size: .7rem; font-weight: 700; text-transform: uppercase;
      letter-spacing: .06em; color: var(--text-3); margin-bottom: .1rem;
    }
    .graf-wrap { text-align: center; }
    .graf-svg { max-width: 240px; max-height: 380px; height: auto; }
    .mini-card-body { text-align: center; }
"""

def apuntes(parrafos):
    ps = "\n".join(f"        <p>{p}</p>" for p in parrafos)
    return g.seccion("Apuntes", "apuntes", f'      <div class="regla-unica">\n{ps}\n      </div>')

def card(titulo, cuerpo, ind="        "):
    return (f'{ind}<div class="mini-card">\n{ind}  <div class="mini-card-head">{titulo}</div>\n'
            f'{ind}  <div class="mini-card-body">{cuerpo}</div>\n{ind}</div>')

def dato(et, tex):
    return f'<div class="dato"><span class="et">{et}</span>${tex}$</div>'

def resol(titulo, cuerpo, ind="          "):
    return f'{ind}<div class="resol-item">\n{ind}  <div class="resol-num">{titulo}</div>\n{ind}  {cuerpo}\n{ind}</div>'
