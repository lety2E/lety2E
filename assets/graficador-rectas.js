/* Simulador de rectas y = mx + b — lety2E. Arriba los parámetros, luego la regla de correspondencia y al final la gráfica.
   Se pone en cualquier tema con:
     <div class="graficador-recta"></div>
   y al final de la página:
     <script src="../../assets/graficador-rectas.js"></script>
   El alumno escoge los parámetros (signo de la pendiente, ordenada, Δy y Δx) y ve formarse la
   gráfica: primero el punto de la ordenada, luego la escalera (a la derecha primero en y y después
   en x; a la izquierda al revés) y al final la recta, junto con su regla de correspondencia.
   Colores como en el video: lo alto (Δy) magenta, lo ancho (Δx) turquesa, recta y ordenada moradas.
   Sin librerías; funciona con file://. */
(function () {
  'use strict';
  var R = 10, U = 20, M = 12, W = 2 * R * U + 2 * M;   /* plano de −10 a 10, 1 cuadro = 1 unidad */
  var C = { reja: '#E0C4BC', eje: '#7B5A50', alto: '#FF00AA', ancho: '#00A896', recta: '#7B2CBF', punto: '#1A0828' };
  var NS = 'http://www.w3.org/2000/svg';
  var QUIETO = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  var CSS =
    '.graficador-recta{background:var(--bg-card,#fff);border:1px solid var(--border,#E0C4BC);border-radius:14px;padding:1rem;max-width:460px;margin:0 auto}' +
    '.gr-regla{display:flex;align-items:center;justify-content:center;gap:.3rem;font-size:1.7rem;font-weight:600;color:var(--text,#3D2525);min-height:4.2rem;white-space:nowrap;margin-top:.6rem;border-top:1px solid var(--border,#E0C4BC);padding-top:.6rem}' +
    '.gr-regla i{font-family:Georgia,serif;font-weight:400}' +
    '.gr-fr{display:inline-flex;flex-direction:column;align-items:center;line-height:1.05;font-size:1.35rem;margin:0 .1rem}' +
    '.gr-fr b{display:block;padding:0 .2rem}.gr-fr .gr-raya{display:block;width:100%;height:2px;background:currentColor;margin:.1rem 0}' +
    '.gr-c-alto{color:#D6008F}.gr-c-ancho{color:#008577}.gr-c-recta{color:#7B2CBF}' +
    '.graficador-recta svg{display:block;width:100%;max-width:400px;height:auto;margin:.4rem auto .8rem}' +
    '.gr-fila{display:grid;grid-template-columns:6.2rem 1fr 2.2rem;align-items:center;gap:.6rem;margin:.55rem 0;font-size:.95rem;color:var(--text,#3D2525)}' +
    '.gr-fila output{font-weight:700;text-align:right;font-size:1.05rem}' +
    '.gr-fila input[type=range]{width:100%;accent-color:var(--gr-c,#7B2CBF)}' +
    '.gr-gen{display:flex;justify-content:center;align-items:center;flex-wrap:wrap;gap:.3rem 1.6rem;font-size:1.25rem;color:var(--text,#3D2525);padding-bottom:.55rem;margin-bottom:.4rem;border-bottom:1px solid var(--border,#E0C4BC)}' +
    '.gr-gen i,.gr-tit i,.gr-fila label i{font-family:Georgia,serif}' +
    '.gr-gen .gr-fr{font-size:1rem}.gr-gen>span{display:inline-flex;align-items:center;gap:.3rem}' +
    '.gr-tit{font-weight:700;font-size:.92rem;color:var(--accent,#4A0080);margin:.7rem 0 .1rem}' +
    '.gr-sig{display:flex;gap:.4rem}' +
    '.gr-sig button{flex:1;font:inherit;font-weight:600;padding:.4rem .2rem;border-radius:10px;border:1.5px solid var(--border,#E0C4BC);background:#fff;color:var(--text,#3D2525);cursor:pointer}' +
    '.gr-sig button[aria-pressed=true]{background:#FF00AA;border-color:#FF00AA;color:#fff}' +
    '';

  function el(tag, at, padre) {
    var e = document.createElementNS(NS, tag);
    for (var k in at) e.setAttribute(k, at[k]);
    if (padre) padre.appendChild(e);
    return e;
  }
  function X(x) { return M + (x + R) * U; }
  function Y(y) { return M + (R - y) * U; }
  function dentro(x, y) { return Math.abs(x) <= R + 1e-9 && Math.abs(y) <= R + 1e-9; }

  function plano(svg) {
    var g = el('g', {}, svg);
    for (var i = -R; i <= R; i++) {
      el('line', { x1: X(i), y1: Y(-R), x2: X(i), y2: Y(R), stroke: C.reja, 'stroke-width': 0.5 }, g);
      el('line', { x1: X(-R), y1: Y(i), x2: X(R), y2: Y(i), stroke: C.reja, 'stroke-width': 0.5 }, g);
    }
    el('line', { x1: X(-R), y1: Y(0), x2: X(R), y2: Y(0), stroke: C.eje, 'stroke-width': 1.4 }, g);
    el('line', { x1: X(0), y1: Y(-R), x2: X(0), y2: Y(R), stroke: C.eje, 'stroke-width': 1.4 }, g);
    var tx = el('text', { x: X(R) - 4, y: Y(0) + 15, 'font-size': 13, fill: C.eje, 'text-anchor': 'end', 'font-style': 'italic' }, g); tx.textContent = 'x';
    var ty = el('text', { x: X(0) + 7, y: Y(R) + 12, 'font-size': 13, fill: C.eje, 'font-style': 'italic' }, g); ty.textContent = 'y';
  }

  /* Pasos de la escalera desde (0, b), alternando hacia la derecha y hacia la izquierda. */
  function pasos(s, dy, dx, b) {
    var D = [], I = [], x = 0, y = b, k;
    for (k = 0; k < 12; k++) {
      var y1 = y + s * dy, x1 = x + dx; if (!dentro(x1, y1)) break;
      D.push({ a: [x, y], b: [x, y1], c: C.alto }, { a: [x, y1], b: [x1, y1], c: C.ancho, p: true }); x = x1; y = y1;
    }
    x = 0; y = b;
    for (k = 0; k < 12; k++) {
      var x2 = x - dx, y2 = y - s * dy; if (!dentro(x2, y2)) break;
      I.push({ a: [x, y], b: [x2, y], c: C.ancho }, { a: [x2, y], b: [x2, y2], c: C.alto, p: true }); x = x2; y = y2;
    }
    var out = [];
    for (k = 0; k < Math.max(D.length, I.length); k += 2) out = out.concat(D.slice(k, k + 2), I.slice(k, k + 2));
    return out;
  }

  function regla(s, dy, dx, b) {
    var n = dy, d = dx, h = '<i>y</i> =';   /* sin simplificar: la fracción es la misma escalera que se dibuja */
    var signo = s < 0 ? '−' : '';
    if (d === 1) h += ' <b class="gr-c-alto">' + signo + (n === 1 ? '' : n) + '</b><i>x</i>';
    else h += ' <b class="gr-c-alto">' + signo + '</b><span class="gr-fr"><b class="gr-c-alto">' + n + '</b><span class="gr-raya"></span><b class="gr-c-ancho">' + d + '</b></span><i>x</i>';
    if (b !== 0) h += ' <b class="gr-c-recta">' + (b < 0 ? '−' : '+') + ' ' + Math.abs(b) + '</b>';
    return h;
  }

  function montar(caja) {
    var id = 'gr' + Math.random().toString(36).slice(2, 7);
    caja.innerHTML =
      '<div class="gr-gen"><span><i>y</i> = <i>m</i><i>x</i> + <i>b</i></span>' +
        '<span><i>m</i> = <span class="gr-fr"><b class="gr-c-alto">Δ<i>y</i></b><span class="gr-raya"></span><b class="gr-c-ancho">Δ<i>x</i></b></span></span></div>' +
      '<div class="gr-tit">Pendiente <i>m</i></div>' +
      '<div class="gr-fila"><span>Signo</span><div class="gr-sig">' +
        '<button type="button" data-s="1" aria-pressed="true">positiva</button>' +
        '<button type="button" data-s="-1" aria-pressed="false">negativa</button></div><span></span></div>' +
      '<div class="gr-fila" style="--gr-c:#FF00AA"><label for="' + id + 'y">Δ<i>y</i></label>' +
        '<input id="' + id + 'y" class="gr-dy" type="range" min="1" max="5" value="3"><output class="gr-c-alto"></output></div>' +
      '<div class="gr-fila" style="--gr-c:#00A896"><label for="' + id + 'x">Δ<i>x</i></label>' +
        '<input id="' + id + 'x" class="gr-dx" type="range" min="1" max="5" value="4"><output class="gr-c-ancho"></output></div>' +
      '<div class="gr-tit">Ordenada al origen <i>b</i></div>' +
      '<div class="gr-fila" style="--gr-c:#7B2CBF"><label for="' + id + 'b"><i>b</i></label>' +
        '<input id="' + id + 'b" class="gr-b" type="range" min="-5" max="5" value="2"><output class="gr-c-recta"></output></div>' +
      '<div class="gr-regla" aria-live="polite"></div>' +
      '<div class="gr-plano"></div>';
    var q = function (c) { return caja.querySelector(c); };
    var svg = el('svg', { viewBox: '0 0 ' + W + ' ' + W, role: 'img', 'aria-label': 'Gráfica de la recta' }, q('.gr-plano'));
    plano(svg);
    var capa = el('g', {}, svg), s = 1, raf = 0;

    function dibujar() {
      cancelAnimationFrame(raf);
      var dy = +q('.gr-dy').value, dx = +q('.gr-dx').value, b = +q('.gr-b').value, m = s * dy / dx;
      q('.gr-dy + output').textContent = dy; q('.gr-dx + output').textContent = dx;
      q('.gr-b + output').textContent = (b < 0 ? '−' : '') + Math.abs(b);
      q('.gr-regla').innerHTML = regla(s, dy, dx, b);
      while (capa.firstChild) capa.removeChild(capa.firstChild);

      var P = pasos(s, dy, dx, b), segs = [], pts = [];
      P.forEach(function (p) {
        segs.push(el('line', { x1: X(p.a[0]), y1: Y(p.a[1]), x2: X(p.a[0]), y2: Y(p.a[1]), stroke: p.c, 'stroke-width': 3, 'stroke-linecap': 'round' }, capa));
        pts.push(p.p ? el('circle', { cx: X(p.b[0]), cy: Y(p.b[1]), r: 0, fill: C.punto }, capa) : null);
      });
      var xa = Math.max(-R, Math.min((R - b) / m, (-R - b) / m)), xb = Math.min(R, Math.max((R - b) / m, (-R - b) / m));
      var recta = el('line', { x1: X(xa), y1: Y(m * xa + b), x2: X(xa), y2: Y(m * xa + b), stroke: C.recta, 'stroke-width': 2.6, 'stroke-linecap': 'round', opacity: 0.9 }, capa);
      var ord = el('circle', { cx: X(0), cy: Y(b), r: 0, fill: C.recta }, capa);

      /* tiempos: ordenada 0–0.35 s · cada tramo 0.28 s · recta 0.6 s */
      var T0 = 0.35, TS = 0.28, TR = 0.6, total = T0 + P.length * TS + TR, t0 = null;
      function cuadro(ts) {
        if (t0 === null) t0 = ts;
        var t = QUIETO ? total : (ts - t0) / 1000;
        ord.setAttribute('r', 6 * Math.min(1, t / T0));
        P.forEach(function (p, i) {
          var f = Math.max(0, Math.min(1, (t - T0 - i * TS) / TS));
          segs[i].setAttribute('x2', X(p.a[0] + (p.b[0] - p.a[0]) * f)); segs[i].setAttribute('y2', Y(p.a[1] + (p.b[1] - p.a[1]) * f));
          if (pts[i]) pts[i].setAttribute('r', f >= 1 ? 3.6 : 0);
        });
        var fr = Math.max(0, Math.min(1, (t - T0 - P.length * TS) / TR)), xe = xa + (xb - xa) * fr;
        recta.setAttribute('x2', X(xe)); recta.setAttribute('y2', Y(m * xe + b));
        if (t < total) raf = requestAnimationFrame(cuadro);
      }
      raf = requestAnimationFrame(cuadro);
    }

    caja.querySelectorAll('.gr-sig button').forEach(function (bt) {
      bt.addEventListener('click', function () {
        s = +bt.getAttribute('data-s');
        caja.querySelectorAll('.gr-sig button').forEach(function (o) { o.setAttribute('aria-pressed', o === bt ? 'true' : 'false'); });
        dibujar();
      });
    });
    caja.addEventListener('input', dibujar);
    dibujar();
  }

  function iniciar() {
    var cajas = document.querySelectorAll('.graficador-recta');
    if (!cajas.length) return;
    var st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
    for (var i = 0; i < cajas.length; i++) montar(cajas[i]);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
