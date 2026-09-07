#!/usr/bin/env node
/* ================================================================
   prerender-katex.js — lety2E
   Convierte las fórmulas $...$ / $$...$$ a HTML de KaTeX aquí, una
   sola vez, para que las páginas NO tengan que cargar katex.min.js
   (74 KB gzip + 271 KB de parseo) en el celular del alumno.

   Además del peso, quita el parpadeo: sin esto el alumno ve los
   "$$y = x^2$$" en crudo hasta que el JS termina y todo brinca.

   Uso:
     node "Recursos lety2E/prerender-katex.js" --check      (no escribe)
     node "Recursos lety2E/prerender-katex.js"              (escribe)
     node "Recursos lety2E/prerender-katex.js" math/matematicas-4

   Es idempotente: una página ya pre-renderizada se salta sola.
   El LaTeX original NO se pierde — KaTeX lo guarda dentro de cada
   fórmula en <annotation encoding="application/x-tex">, así que se
   puede recuperar y volver a correr.
   ================================================================ */
'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const katex = require(path.join(ROOT, 'assets/katex/katex.min.js'));

/* Mismos tags que ignora auto-render.min.js (sus ignoredTags por
   defecto). Si tocáramos el $ de un <style> o un <script> romperíamos
   la página. */
const IGNORED = new Set(['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'option']);

const ENTIDADES = { '&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&#39;': "'", '&apos;': "'", '&nbsp;': ' ' };
const decodificar = (s) => s.replace(/&(?:amp|lt|gt|quot|#39|apos|nbsp);/g, (m) => ENTIDADES[m]);

/* ── Escáner: parte el HTML en tags y texto ──────────────────────
   Sólo el texto se toca; lo que va entre < y > (incluidos los
   valores de atributos, que pueden traer $) queda intacto. */
function partirEnTrozos(html) {
  const trozos = [];
  /* Un < sólo abre etiqueta si le sigue letra, /, ! o ? — igual que el
     navegador. Sin esto, una fórmula como $x < 3$ se partiría a la
     mitad y quedaría el $ crudo en pantalla. */
  const re = /<!--[\s\S]*?-->|<[a-zA-Z\/!?][^>]*>/g;
  let i = 0, m;
  while ((m = re.exec(html)) !== null) {
    if (m.index > i) trozos.push({ tipo: 'texto', valor: html.slice(i, m.index) });
    trozos.push({ tipo: 'tag', valor: m[0] });
    i = m.index + m[0].length;
  }
  if (i < html.length) trozos.push({ tipo: 'texto', valor: html.slice(i) });
  return trozos;
}

const nombreDeTag = (tag) => {
  const m = /^<\/?\s*([a-zA-Z][a-zA-Z0-9-]*)/.exec(tag);
  return m ? m[1].toLowerCase() : null;
};
const esCierre = (tag) => /^<\//.test(tag);
const esAutoCerrado = (tag) => /\/>$/.test(tag);

/* ── Render de un trozo de texto ─────────────────────────────────
   Primero $$..$$ (display), luego $..$ (inline) — el mismo orden y
   los mismos delimitadores que configuran las páginas en el onload
   de auto-render. */
function renderTexto(texto, estado) {
  if (texto.indexOf('$') === -1) return texto;

  const render = (tex, display) => {
    const limpio = decodificar(tex).trim();
    if (!limpio) return null;
    try {
      estado.ok++;
      return katex.renderToString(limpio, { displayMode: display, throwOnError: true, strict: false });
    } catch (e) {
      estado.ok--;
      estado.errores.push({ tex: limpio.slice(0, 70), msg: e.message.slice(0, 90) });
      return null;                       /* se deja el $...$ tal cual */
    }
  };

  let salida = texto.replace(/\$\$([\s\S]+?)\$\$/g, (m, tex) => render(tex, true) ?? m);
  salida = salida.replace(/\$([^$\n]+?)\$/g, (m, tex) => render(tex, false) ?? m);
  return salida;
}

/* ── Procesar un archivo ─────────────────────────────────────────*/
function procesar(archivo) {
  const original = fs.readFileSync(archivo, 'utf8');

  if (!/katex\.min\.js/.test(original)) return { estado: 'sin-katex' };
  if (/class="katex(?:[ "])/.test(original)) return { estado: 'ya-hecho' };

  const trozos = partirEnTrozos(original);
  const est = { ok: 0, errores: [] };
  const pila = [];

  const salida = trozos.map((t) => {
    if (t.tipo === 'tag') {
      const nombre = nombreDeTag(t.valor);
      if (nombre && IGNORED.has(nombre) && !esAutoCerrado(t.valor)) {
        if (esCierre(t.valor)) { if (pila[pila.length - 1] === nombre) pila.pop(); }
        else pila.push(nombre);
      }
      return t.valor;
    }
    return pila.length ? t.valor : renderTexto(t.valor, est);
  }).join('');

  return { estado: 'hecho', salida, formulas: est.ok, errores: est.errores, antes: original.length };
}

/* ── Quitar el <script> de KaTeX (ya no hace falta) ──────────────
   Se conserva katex.min.css: sin él las fórmulas se ven desarmadas. */
function quitarScriptsKatex(html) {
  return html
    .replace(/[ \t]*<script[^>]*src="[^"]*katex\.min\.js"[^>]*>\s*<\/script>\r?\n?/g, '')
    .replace(/[ \t]*<script[^>]*src="[^"]*auto-render\.min\.js"[\s\S]*?<\/script>\r?\n?/g, '');
}

/* ── Main ────────────────────────────────────────────────────────*/
const args = process.argv.slice(2);
const soloCheck = args.includes('--check');
const objetivos = args.filter((a) => !a.startsWith('--'));

function listarHtml(dir, acc = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.name === '.git' || e.name === 'node_modules' || e.name.startsWith('.')) continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) {
      if (e.name === 'Recursos lety2E') continue;   /* recursos, no se publica */
      listarHtml(p, acc);
    } else if (e.name.endsWith('.html')) acc.push(p);
  }
  return acc;
}

const archivos = objetivos.length
  ? objetivos.flatMap((o) => {
      const p = path.resolve(ROOT, o);
      return fs.statSync(p).isDirectory() ? listarHtml(p) : [p];
    })
  : listarHtml(ROOT);

let nHechos = 0, nFormulas = 0, kbAntes = 0, kbDespues = 0;
const fallidos = [];

for (const archivo of archivos) {
  const r = procesar(archivo);
  if (r.estado !== 'hecho') continue;

  const rel = path.relative(ROOT, archivo);

  /* ── Protección: páginas que usan KaTeX en tiempo real ──────────
     Los simuladores arman las preguntas con JS desde data.js y luego
     llaman a renderMathInElement sobre lo que acaban de inyectar. Ahí
     el pre-render no sirve (no hay fórmulas en el HTML estático) y
     quitarles el <script> las rompería: las preguntas saldrían con
     los $...$ en crudo. Esas páginas se dejan intactas. */
  const restante = quitarScriptsKatex(r.salida);
  if (/renderMathInElement|katex\s*\.\s*render|window\.katex/.test(restante)) {
    console.log(`  ⏭️  ${rel} — usa KaTeX en tiempo real (JS), se deja como está`);
    continue;
  }
  if (r.formulas === 0) {
    console.log(`  ⏭️  ${rel} — sin fórmulas, se deja como está`);
    continue;
  }

  if (r.errores.length) {
    fallidos.push({ rel, errores: r.errores });
    console.log(`  ⚠️  ${rel} — ${r.errores.length} fórmula(s) no compilaron, NO se tocó`);
    r.errores.slice(0, 3).forEach((e) => console.log(`        ${e.tex}  →  ${e.msg}`));
    continue;                                   /* no escribir páginas con errores */
  }

  const final = restante;
  nHechos++; nFormulas += r.formulas;
  kbAntes += r.antes; kbDespues += final.length;

  if (!soloCheck) fs.writeFileSync(archivo, final);
  console.log(`  ✅ ${rel} — ${r.formulas} fórmulas`);
}

console.log('\n' + '─'.repeat(56));
console.log(`${soloCheck ? 'SIMULACRO (--check, no se escribió nada)' : 'Escrito'}`);
console.log(`páginas: ${nHechos}   fórmulas: ${nFormulas}`);
console.log(`HTML en disco: ${(kbAntes / 1024).toFixed(0)} KB → ${(kbDespues / 1024).toFixed(0)} KB`);
console.log(`JS que el alumno YA NO baja: ${(nHechos * 75.8).toFixed(0)} KB gzip (75.8 KB por página)`);
if (fallidos.length) console.log(`\n⚠️  ${fallidos.length} página(s) con errores, sin tocar (arriba el detalle)`);
