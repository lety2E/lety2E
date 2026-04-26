/* ================================================
   lety2E — footer.js (unificado)
   Detecta nivel de profundidad automáticamente.
   ================================================ */
(function () {
  'use strict';

  var year = new Date().getFullYear();

  /* ── Detectar profundidad ────────────────────── */
  var scriptSrc = document.currentScript.getAttribute('src');
  var depth = (scriptSrc.match(/\.\.\//g) || []).length;

  /* ── Calcular rutas base ─────────────────────── */
  var root = depth === 0 ? './' : new Array(depth + 1).join('../');
  var iconPath = root + 'assets/logos/icono-2e.png';
  var homePath = root + 'index.html';

  /* ── Inyectar ────────────────────────────────── */
  var footer =
    '<footer class="site-footer">' +
      '<div class="footer-inner">' +
        '<div class="footer-row-1">' +
          '<a href="' + homePath + '" class="footer-brand">' +
            '<div class="footer-icon">' +
              '<img src="' + iconPath + '" alt="lety2E logo" />' +
            '</div>' +
            '<span class="footer-brand-name">lety2E</span>' +
          '</a>' +
          '<a href="https://www.facebook.com/profile.php?id=61575397726538" target="_blank" rel="noopener" class="footer-social" title="Sígueme en Facebook">' +
            '<span class="social-icon">f</span>' +
          '</a>' +
        '</div>' +
        '<span class="footer-copy">&copy; ' + year + ' lety2E &nbsp;&middot;&nbsp; todos los derechos reservados</span>' +
      '</div>' +
    '</footer>';

  document.body.insertAdjacentHTML('beforeend', footer);
})();
