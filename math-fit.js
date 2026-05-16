/* math-fit.js — auto-escala ecuaciones KaTeX que se desbordan de su contenedor.
   Red de seguridad para ecuaciones extra-largas (reducción de polinomios, etc.).
   El CSS de mobile ya reduce font-size en general; este script se encarga sólo
   de los casos extremos en los que aún así no caben.

   Estrategia: para cada .katex renderizado, comparar su scrollWidth contra el
   ancho disponible del contenedor padre (.ej-line, .sol, .ejemplo-inline,
   .ejemplo-block, .mini-card-body). Si excede, aplica font-size escalado.

   Se ejecuta al cargar, después de que KaTeX termina de renderear, y en cada
   resize del viewport (con debounce). */
(function () {
  'use strict';

  if (document.body && document.body.getAttribute('data-section') !== 'math') return;

  var CONTAINER_SELECTORS = [
    '.ej-line',
    '.sol',
    '.ejemplo-inline',
    '.ejemplo-item',
    '.ejemplo-block',
    '.mini-card-body'
  ];

  function fit() {
    // Reset: borrar font-size inline previo para re-medir limpio.
    document.querySelectorAll('.katex').forEach(function (el) {
      if (el.dataset.mfApplied === '1') {
        el.style.fontSize = '';
        el.dataset.mfApplied = '0';
      }
    });

    // Reflow forzado: las medidas siguientes serán con CSS original.
    void document.body.offsetWidth;

    document.querySelectorAll('.katex').forEach(function (el) {
      // Buscar el contenedor más cercano relevante.
      var container = null;
      for (var i = 0; i < CONTAINER_SELECTORS.length; i++) {
        var c = el.closest(CONTAINER_SELECTORS[i]);
        if (c) { container = c; break; }
      }
      if (!container) return;

      // Ancho disponible (restando padding horizontal del contenedor).
      var cs = window.getComputedStyle(container);
      var padL = parseFloat(cs.paddingLeft) || 0;
      var padR = parseFloat(cs.paddingRight) || 0;
      var maxW = container.clientWidth - padL - padR - 4; // 4px de margen
      if (maxW <= 0) return;

      var w = el.scrollWidth;
      if (w > maxW) {
        var ratio = maxW / w;
        // Limita la reducción a 50% mínimo para no volver ilegible.
        if (ratio < 0.5) ratio = 0.5;
        var current = parseFloat(window.getComputedStyle(el).fontSize);
        el.style.fontSize = (current * ratio * 0.98).toFixed(2) + 'px';
        el.dataset.mfApplied = '1';
      }
    });
  }

  function whenKatexReady(cb) {
    // Intenta cuando KaTeX ya renderizó al menos una ecuación visible.
    if (document.querySelectorAll('.katex').length > 0) {
      cb();
    } else {
      setTimeout(function () { whenKatexReady(cb); }, 80);
    }
  }

  function init() {
    // Doble pasada: una rápida, otra después de que cargan fuentes web.
    whenKatexReady(fit);
    setTimeout(fit, 400);
    setTimeout(fit, 1200);
  }

  if (document.readyState === 'complete') {
    init();
  } else {
    window.addEventListener('load', init);
  }

  // Re-fit en resize y cambio de orientación, con debounce.
  var resizeTimer;
  function scheduleFit() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(fit, 150);
  }
  window.addEventListener('resize', scheduleFit);
  window.addEventListener('orientationchange', scheduleFit);
})();
