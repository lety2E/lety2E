/* ================================================
   lety2E — nav.js (unificado)
   Detecta sección y nivel automáticamente.
   Para agregar una nueva sección, solo agrega
   una entrada en SECTIONS.
   ================================================ */
(function () {
  'use strict';

  /* ── Configuración de secciones ─────────────── */
  const SECTIONS = {
    lupian: {
      name: 'Lupián',
      links: [
        { text: 'Cantos', href: 'cantos/index.html' },
        { text: 'Relatos', href: 'relatos/index.html' }
      ]
    },
    apuntes: {
      name: 'Apuntes',
      links: []
    },
    math: {
      name: 'Math',
      links: [
        { text: 'Mat 1', href: 'matematicas-1/index.html' },
        { text: 'Mat 2', href: 'matematicas-2/index.html' },
        { text: 'Mat 3', href: 'matematicas-3/index.html' },
        { text: 'Mat 4', href: 'matematicas-4/index.html' },
        { text: 'Mat 5', href: 'matematicas-5/index.html' },
        { text: 'Optativa', href: 'optativa/index.html' }
      ]
    }
  };

  const ROOT_LINKS = [
    { text: 'Math', href: 'math/index.html' },
    { text: 'Lupián', href: 'lupian/index.html' },
    { text: 'Apuntes', href: 'apuntes/index.html' }
  ];

  /* ── Detectar profundidad (cuántos ../ hay en src) */
  var scriptSrc = document.currentScript.getAttribute('src');
  var depth = (scriptSrc.match(/\.\.\//g) || []).length;
  // depth 0 = raíz, 1 = sección, 2 = subsección

  /* ── Detectar sección actual ─────────────────── */
  var path = window.location.pathname.toLowerCase();
  var section = null;
  var keys = Object.keys(SECTIONS);
  for (var i = 0; i < keys.length; i++) {
    if (path.indexOf('/' + keys[i] + '/') !== -1) {
      section = keys[i];
      break;
    }
  }

  /* ── Calcular rutas base ─────────────────────── */
  var root = depth === 0 ? './' : new Array(depth + 1).join('../');
  var iconPath = root + 'assets/logos/lety2E-madre-v3.png';
  var homePath = root + 'index.html';

  /* ── Determinar contenido del nav ────────────── */
  var brandName, sectionHref, links;

  if (depth === 0) {
    // Raíz: icono y nombre van al mismo lugar
    brandName = 'lety2E';
    sectionHref = null;  // no hay sección, todo va a home
    links = ROOT_LINKS;
  } else if (depth === 1 && section && SECTIONS[section]) {
    // Sección: icono → home, nombre → aquí mismo (index de sección)
    brandName = SECTIONS[section].name;
    sectionHref = './index.html';
    links = SECTIONS[section].links;
    // Si estamos dentro de un HTML de sección (no el index), mostrar volver
    var isSectionIndex = /\/(index\.html)?$/i.test(path);
    if (!isSectionIndex && (!links || links.length === 0)) {
      links = [{ text: '\u2190 Volver', href: './index.html' }];
    }
  } else if (depth >= 2 && section && SECTIONS[section]) {
    // Subsección: icono → home, nombre → index de sección
    brandName = SECTIONS[section].name;
    sectionHref = '../index.html';
    links = [{ text: '\u2190 Volver', href: '../index.html' }];
  } else {
    brandName = 'lety2E';
    sectionHref = null;
    links = ROOT_LINKS;
  }

  /* ── Generar HTML de links ───────────────────── */
  var linksHTML = '';
  for (var j = 0; j < links.length; j++) {
    var l = links[j];
    var attrs = l.external ? ' target="_blank" rel="noopener"' : '';
    linksHTML += '<li><a href="' + l.href + '"' + attrs + '>' + l.text + '</a></li>';
  }

  /* ── Logo unificado en SVG ── */
  var badgeHTML = 
    '<div class="nav-badge">' +
      '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="nav-badge-svg" aria-hidden="true">' +
        '<rect width="100" height="100" rx="18" class="badge-bg"/>' +
        '<text x="50" y="73" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-style="italic" font-weight="900" font-size="58" class="badge-text">2E</text>' +
      '</svg>' +
    '</div>';

  var brandHTML;
  var isHomeIndex = (depth === 0);
  // isSectionIndex was defined above but we might need it
  var isSectionIndex = (depth === 1 && /\/(index\.html)?$/i.test(path));

  // Determine if logo should be a link
  var logoTag = isHomeIndex ? 'div' : 'a';
  var logoHref = isHomeIndex ? '' : ' href="' + homePath + '" aria-label="Ir a lety2E inicio"';
  
  var logoElement = 
    '<' + logoTag + logoHref + ' class="nav-icon-link">' +
      badgeHTML +
    '</' + logoTag + '>';

  if (sectionHref) {
    // Determine if name should be a link
    var nameTag = isSectionIndex ? 'div' : 'a';
    var nameHref = isSectionIndex ? '' : ' href="' + sectionHref + '"';
    
    brandHTML =
      '<div class="nav-brand">' +
        logoElement +
        '<' + nameTag + nameHref + ' class="nav-name-link">' +
          '<span class="nav-name">' + brandName + '</span>' +
        '</' + nameTag + '>' +
      '</div>';
  } else {
    // Root: the whole thing is inside a wrapper
    // We'll wrap both logo and text in nav-brand. If we're on Home, it's a div.
    brandHTML =
      '<' + logoTag + logoHref + ' class="nav-brand">' +
        badgeHTML +
        '<span class="nav-name">' + brandName + '</span>' +
      '</' + logoTag + '>';
  }

  var nav =
    '<header class="site-nav">' +
      '<div class="nav-inner">' +
        brandHTML +
        '<button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">' +
          '<span></span><span></span><span></span>' +
        '</button>' +
        '<nav class="nav-menu">' +
          '<ul class="nav-links">' + linksHTML + '</ul>' +
        '</nav>' +
      '</div>' +
    '</header>';

  document.body.insertAdjacentHTML('afterbegin', nav);

  /* Toggle menu en móviles */
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.querySelector('.nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function() {
      var isOpen = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', !isOpen);
      menu.classList.toggle('open');
    });
    /* Cerrar menú al hacer click en un link */
    menu.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        toggle.setAttribute('aria-expanded', 'false');
        menu.classList.remove('open');
      });
    });
  }
})();
