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
      name: 'lety2E Lupián',
      links: [
        { text: 'Cantos', href: 'cantos/index.html' },
        { text: 'Escritos', href: 'escritos/index.html' }
      ]
    },
    apuntes: {
      name: 'lety2E Apuntes',
      links: []
    },
    math: {
      name: 'lety2E Math',
      links: [
        { text: 'Mat 1', href: 'matematicas-1/index.html' },
        { text: 'Mat 2', href: 'matematicas-2/index.html' },
        { text: 'Mat 3', href: 'matematicas-3/index.html' },
        { text: 'Mat 4', href: 'matematicas-4/index.html' },
        { text: 'Mat 5', href: 'matematicas-5/index.html' }
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
  var iconPath = root + 'assets/logos/icono-2e-magenta.png';
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

  /* ── Inyectar ────────────────────────────────── */
  var brandHTML;
  if (sectionHref) {
    // Sección/subsección: icono → home, nombre → índice de sección
    brandHTML =
      '<div class="nav-brand">' +
        '<a href="' + homePath + '" class="nav-icon-link" aria-label="Ir a lety2E inicio">' +
          '<div class="nav-badge" style="background-image:url(\'' + iconPath + '\')"></div>' +
        '</a>' +
        '<a href="' + sectionHref + '" class="nav-name-link">' +
          '<span class="nav-name">' + brandName + '</span>' +
        '</a>' +
      '</div>';
  } else {
    // Raíz: todo va a home
    brandHTML =
      '<a href="' + homePath + '" class="nav-brand">' +
        '<div class="nav-badge" style="background-image:url(\'' + iconPath + '\')"></div>' +
        '<span class="nav-name">' + brandName + '</span>' +
      '</a>';
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
