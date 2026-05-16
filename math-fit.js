/* math-fit.js — auto-escala cualquier ecuación KaTeX que se desborde de su
   contenedor visual real, sin importar la estructura HTML del tema.

   Estrategia universal: para cada .katex / .ej-line / .sol, subir por el árbol
   hasta encontrar el primer ancestro de tipo block/flex/grid que NO tenga
   white-space: nowrap. Ese es el ancho visual disponible. Si el contenido
   excede ese ancho, aplica font-size reducido proporcionalmente.

   Cubre temas con cualquier wrapper: .ejemplo-block, .mini-card-body,
   .ejemplo-item, .ejemplo-inline, .tri-info, .apunte-box, <p> directos, etc. */
(function () {
  'use strict';

  if (document.body && document.body.getAttribute('data-section') !== 'math') return;

  // Wrappers internos que agrupan un renglón completo (.ej-line/.sol con
  // nowrap): cuando los detectemos, escalamos el wrapper completo para que
  // el .katex + <strong> resultado se reduzcan juntos.
  var LINE_SELECTOR = '.ej-line, .sol';

  /** Sube hasta encontrar el primer ancestro block/flex/grid sin nowrap. */
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
      - 4; // colchón
  }

  function scaleToFit(el, maxW) {
    var w = el.scrollWidth;
    if (w > maxW) {
      var ratio = maxW / w;
      if (ratio < 0.5) ratio = 0.5; // mínimo legible
      var sz = parseFloat(window.getComputedStyle(el).fontSize);
      el.style.fontSize = (sz * ratio * 0.98).toFixed(2) + 'px';
      el.dataset.mf = '1';
      return true;
    }
    return false;
  }

  function fit() {
    // Reset: borrar font-size inline previo para re-medir limpio.
    document.querySelectorAll('[data-mf="1"]').forEach(function (el) {
      el.style.fontSize = '';
      el.dataset.mf = '0';
    });
    void document.body.offsetWidth; // reflow

    // (a) Escalar renglones .ej-line / .sol (que agrupan katex + <strong>)
    //     contra su ancestro block sin nowrap.
    document.querySelectorAll(LINE_SELECTOR).forEach(function (line) {
      var anc = findWidthAncestor(line);
      if (!anc) return;
      var maxW = availableWidth(anc);
      if (maxW > 0) scaleToFit(line, maxW);
    });

    // (b) Para .katex sueltos (sin .ej-line/.sol padre): escalar el .katex
    //     individual contra su ancestro block sin nowrap.
    document.querySelectorAll('.katex').forEach(function (eq) {
      if (eq.closest(LINE_SELECTOR)) return; // ya manejado en (a)
      var anc = findWidthAncestor(eq);
      if (!anc) return;
      var maxW = availableWidth(anc);
      if (maxW > 0) scaleToFit(eq, maxW);
    });
  }

  function whenKatexReady(cb) {
    if (document.querySelectorAll('.katex').length > 0) cb();
    else setTimeout(function () { whenKatexReady(cb); }, 80);
  }

  function init() {
    whenKatexReady(fit);
    setTimeout(fit, 400);
    setTimeout(fit, 1200); // después de carga de fuentes web
  }

  if (document.readyState === 'complete') init();
  else window.addEventListener('load', init);

  var resizeTimer;
  function scheduleFit() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(fit, 150);
  }
  window.addEventListener('resize', scheduleFit);
  window.addEventListener('orientationchange', scheduleFit);
})();
