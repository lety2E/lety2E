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

/* ================================================
   lety2E — facade de video (.yt-lite)
   Los <iframe> de YouTube pesan ~1 MB cada uno y detienen
   la carga de la página. En su lugar el HTML trae
   <button class="yt-lite" data-yt="ID" data-title="...">;
   aquí le pintamos la miniatura y sólo al dar clic se
   inserta el iframe real (ya con autoplay).
   Estilos: ver .yt-lite en style.css
   ================================================ */
(function () {
  'use strict';

  function pintar(btn) {
    if (btn.dataset.listo) return;
    btn.dataset.listo = '1';

    var id = btn.getAttribute('data-yt');
    if (!id || id.indexOf('{{') === 0) return;   /* placeholder del template */

    var img = document.createElement('img');
    img.className = 'yt-thumb';
    img.alt = '';
    img.loading = 'lazy';
    img.decoding = 'async';
    /* mqdefault es la única miniatura 16:9 que YouTube garantiza (320x180,
       ~8 KB). hqdefault pesa el doble y viene en 4:3 con barras negras, y al
       recortarla a 16:9 se comía el encabezado de los videos de Lety. */
    img.width = 320; img.height = 180;
    img.referrerPolicy = 'no-referrer';
    img.onerror = function () { img.remove(); };   /* sin internet: queda el fondo oscuro + play */
    img.src = 'https://i.ytimg.com/vi/' + id + '/mqdefault.jpg';
    btn.appendChild(img);

    var play = document.createElement('span');
    play.className = 'yt-play';
    btn.appendChild(play);
  }

  function reproducir(btn) {
    var id = btn.getAttribute('data-yt');
    if (!id) return;

    var iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube.com/embed/' + id + '?rel=0&autoplay=1';
    iframe.title = btn.getAttribute('data-title') || 'Video';
    iframe.setAttribute('frameborder', '0');
    iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
    iframe.setAttribute('allowfullscreen', '');

    btn.parentNode.replaceChild(iframe, btn);
  }

  var botones = document.querySelectorAll('.yt-lite[data-yt]');
  for (var i = 0; i < botones.length; i++) pintar(botones[i]);

  /* Delegado: sirve también si alguna página inyecta videos después. */
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('.yt-lite[data-yt]');
    if (btn) reproducir(btn);
  });
})();
