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
  var isHomeIndex = (depth === 0);
  var logoTag = isHomeIndex ? 'div' : 'a';
  var logoHref = isHomeIndex ? '' : ' href="' + homePath + '"';

  var footer =
    '<footer class="site-footer">' +
      '<div class="footer-inner">' +
        '<div class="footer-row-1">' +
          '<' + logoTag + logoHref + ' class="footer-brand">' +
            '<div class="footer-icon">' +
              '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="nav-badge-svg" aria-hidden="true">' +
                '<rect width="100" height="100" rx="18" class="badge-bg"/>' +
                '<text x="50" y="73" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-style="italic" font-weight="900" font-size="58" class="badge-text">2E</text>' +
              '</svg>' +
            '</div>' +
            '<span class="footer-brand-name">lety2E</span>' +
          '</' + logoTag + '>' +
          '<a href="https://www.facebook.com/profile.php?id=61575397726538" target="_blank" rel="noopener" class="footer-social" title="Sígueme en Facebook">' +
            '<span class="social-icon">f</span>' +
          '</a>' +
        '</div>' +
        '<span class="footer-copy">&copy; ' + year + ' lety2E &nbsp;&middot;&nbsp; todos los derechos reservados</span>' +
      '</div>' +
    '</footer>';

  document.body.insertAdjacentHTML('beforeend', footer);
})();
