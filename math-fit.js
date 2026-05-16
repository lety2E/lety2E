/* math-fit.js v3 — auto-escala cualquier ecuación KaTeX que se desborde de su
   contenedor visual. Funciona en cualquier estructura HTML del tema, y se
   re-ejecuta cuando se expanden colapsables (.collapsible) o cambia el viewport.

   Estrategia universal:
   - Para cada renglón (.ej-line, .sol), .katex-display, o .katex inline suelto,
     sube por el árbol hasta encontrar el primer ancestor block/flex/grid SIN
     white-space: nowrap. Ese es el ancho visual disponible.
   - Si el contenido excede ese ancho, aplica font-size reducido.
   - Se re-ejecuta al expandir cualquier .sec-toggle (las respuestas viven
     dentro de .collapsible que arranca con clientWidth=0).

   Cubre: .ejemplo-block, .mini-card-body, .ejemplo-item, .ejemplo-inline,
   .ej-bloque, .ej-row, .tri-info, .apunte-table <td>, <p>, <li>, etc. */
(function () {
  'use strict';

  if (document.body && document.body.getAttribute('data-section') !== 'math') return;

  var LINE_SELECTOR = '.ej-line, .sol';

  function findWidthAncestor(el) {
    var current = el.parentElement;
    while (current && current !== document.documentElement) {
      var cs = window.getComputedStyle(current);
      var d = cs.display;
      var isBlock = (d === 'block' || d === 'flex' || d === 'grid' ||
                     d === 'list-item' || d === 'table' || d === 'table-cell');
      var notNowrap = cs.whiteSpace !== 'nowrap';
      if (isBlock && notNowrap && current.clientWidth > 0) {
        return current;
      }
      current = current.parentElement;
    }
    return null;
  }

  function availableWidth(card) {
    var cs = window.getComputedStyle(card);
    return card.clientWidth
      - (parseFloat(cs.paddingLeft)  || 0)
      - (parseFloat(cs.paddingRight) || 0)
      - 4;
  }

  function scaleToFit(el, maxW) {
    if (maxW <= 0) return false;
    var w = el.scrollWidth;
    if (w > maxW) {
      var ratio = maxW / w;
      if (ratio < 0.5) ratio = 0.5;
      var sz = parseFloat(window.getComputedStyle(el).fontSize);
      el.style.fontSize = (sz * ratio * 0.98).toFixed(2) + 'px';
      el.dataset.mf = '1';
      return true;
    }
    return false;
  }

  function fit() {
    // Reset
    document.querySelectorAll('[data-mf="1"]').forEach(function (el) {
      el.style.fontSize = '';
      el.dataset.mf = '0';
    });
    void document.body.offsetWidth;

    // (a) Renglones agrupados (.ej-line, .sol): escalar el wrapper.
    document.querySelectorAll(LINE_SELECTOR).forEach(function (line) {
      // Saltar si está oculto (dentro de un .collapsible cerrado).
      if (line.clientWidth === 0 && line.offsetParent === null) return;
      var anc = findWidthAncestor(line);
      if (anc) scaleToFit(line, availableWidth(anc));
    });

    // (b) KaTeX-display (bloques de $$...$$): escalar el bloque entero.
    document.querySelectorAll('.katex-display').forEach(function (el) {
      if (el.closest(LINE_SELECTOR)) return;
      if (el.clientWidth === 0 && el.offsetParent === null) return;
      var anc = findWidthAncestor(el);
      if (anc) scaleToFit(el, availableWidth(anc));
    });

    // (c) KaTeX inline sueltos (sin .ej-line/.sol/.katex-display padre).
    document.querySelectorAll('.katex').forEach(function (eq) {
      if (eq.closest(LINE_SELECTOR + ', .katex-display')) return;
      if (eq.clientWidth === 0 && eq.offsetParent === null) return;
      var anc = findWidthAncestor(eq);
      if (anc) scaleToFit(eq, availableWidth(anc));
    });
  }

  function whenKatexReady(cb) {
    if (document.querySelectorAll('.katex').length > 0) cb();
    else setTimeout(function () { whenKatexReady(cb); }, 80);
  }

  function init() {
    whenKatexReady(fit);
    setTimeout(fit, 400);
    setTimeout(fit, 1200);
  }

  if (document.readyState === 'complete') init();
  else window.addEventListener('load', init);

  // Re-fit en resize / orientación.
  var resizeTimer;
  function scheduleFit() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(fit, 150);
  }
  window.addEventListener('resize', scheduleFit);
  window.addEventListener('orientationchange', scheduleFit);

  // Re-fit cuando se expande un colapsable (.sec-toggle abre el .collapsible
  // siguiente; las ecuaciones adentro estaban a clientWidth=0 al cargar y
  // por eso no se medían correctamente).
  document.addEventListener('click', function (e) {
    var toggle = e.target.closest('.sec-toggle');
    if (!toggle) return;
    // El CSS tiene transition max-height .4s. Re-correr fit después de que
    // la animación complete y los elementos tengan su ancho real.
    setTimeout(fit, 80);
    setTimeout(fit, 500);
    setTimeout(fit, 1000);
  }, true);
})();
