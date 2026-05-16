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

  const COURSE_TOPICS = {
    'matematicas-1': [
      { text: 'Operaciones básicas', href: 'operaciones-basicas.html' },
      { text: 'Jerarquía de operaciones', href: 'jerarquia.html' },
      { text: 'Lenguaje algebraico', href: 'lenguaje-algebraico.html' },
      { text: 'Ecuaciones', href: 'ecuaciones.html' },
      { text: 'Ecuaciones con ángulos', href: 'ecuaciones-angulos.html' },
      { text: 'Problemas de ecuaciones', href: 'problemas-ecuaciones.html' },
      { text: 'Monomios', href: 'monomios.html' },
      { text: 'Expresiones algebraicas', href: 'expresiones-algebraicas.html' },
      { text: 'mcm y MCD', href: 'mcm-mcd.html' },
      { text: 'Reglas de exponentes', href: 'reglas-exponentes.html' },
      { text: 'Gráfica con tabulación', href: 'grafica-tabulacion.html' },
      { text: 'Pendiente y ordenada', href: 'pendiente-ordenada.html' },
      { text: 'Área y perímetro', href: 'area-perimetro.html' }
    ]
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

  /* ── Detectar sección actual ─────────────────────── */
  var path = window.location.pathname.toLowerCase();
  var section = null;
  var keys = Object.keys(SECTIONS);
  for (var i = 0; i < keys.length; i++) {
    if (path.indexOf('/' + keys[i] + '/') !== -1) {
      section = keys[i];
      break;
    }
  }

  /* ── Calcular rutas base ─────────────────────────── */
  var root = depth === 0 ? './' : new Array(depth + 1).join('../');
  var homePath = root + 'index.html';

  /* ── Determinar contenido del nav ────────────────── */
  var brandName, sectionHref, links;

  if (depth === 0) {
    brandName = 'lety2E';
    sectionHref = null;
    links = ROOT_LINKS;
  } else if (depth === 1 && section && SECTIONS[section]) {
    brandName = SECTIONS[section].name;
    sectionHref = './index.html';
    links = SECTIONS[section].links;
    var isSectionIndex = /\/(index\.html)?$/i.test(path);
    if (!isSectionIndex && (!links || links.length === 0)) {
      links = [{ text: '\u2190 Volver', href: './index.html' }];
    }
  } else if (depth >= 2 && section && SECTIONS[section]) {
    brandName = SECTIONS[section].name;
    sectionHref = '../index.html';
    
    // Buscar si estamos en un curso con temas registrados
    var pathParts = path.split('/');
    var courseId = pathParts[pathParts.length - 2];
    
    if (section === 'math' && COURSE_TOPICS[courseId]) {
      // Si tenemos temas para este curso, creamos un dropdown
      links = [{
        text: 'Temas',
        isDropdown: true,
        items: COURSE_TOPICS[courseId].map(function(t) {
          var isCurrent = path.indexOf(t.href) !== -1;
          return { text: t.text, href: t.href, active: isCurrent };
        })
      }];
    } else {
      links = [{ text: '\u2190 Volver', href: '../index.html' }];
    }
  } else {
    brandName = 'lety2E';
    sectionHref = null;
    links = ROOT_LINKS;
  }

  /* ── Generar HTML de links ───────────────────── */
  var linksHTML = '';
  for (var j = 0; j < links.length; j++) {
    var l = links[j];
    if (l.isDropdown) {
      linksHTML += '<li class="nav-dropdown">';
      linksHTML += '<a class="dropdown-toggle">' + l.text + '</a>';
      linksHTML += '<ul class="dropdown-content">';
      for (var k = 0; k < l.items.length; k++) {
        var item = l.items[k];
        if (item.isDivider) {
          linksHTML += '<li class="dropdown-divider"></li>';
        } else {
          var activeClass = item.active ? ' class="active"' : '';
          linksHTML += '<li><a href="' + item.href + '"' + activeClass + '>' + item.text + '</a></li>';
        }
      }
      linksHTML += '</ul></li>';
    } else {
      var attrs = l.external ? ' target="_blank" rel="noopener"' : '';
      linksHTML += '<li><a href="' + l.href + '"' + attrs + '>' + l.text + '</a></li>';
    }
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

/* ================================================
   Auto-fit KaTeX en páginas de Math
   ------------------------------------------------
   Para cada fórmula KaTeX (inline o display) mide su
   ancho real vs el ancho disponible de su contenedor.
   Si se sale, reduce su font-size justo lo necesario
   para que quepa. Sin wrap, sin scroll horizontal,
   sin pinch-zoom: la fórmula se ajusta sola.
   Solo corre cuando body[data-section="math"].
   ================================================ */
(function () {
  'use strict';
  if (!document.body || document.body.getAttribute('data-section') !== 'math') return;

  /* Encuentra el ancestro no-KaTeX donde la fórmula debe caber. */
  function findContainer(el) {
    var p = el.parentElement;
    while (p && (p.classList.contains('katex') || p.classList.contains('katex-display'))) {
      p = p.parentElement;
    }
    return p;
  }

  /* Ajusta una fórmula. Reset siempre antes de medir. */
  function fitOne(el) {
    el.style.fontSize = '';
    var container = findContainer(el);
    if (!container) return;
    var cs = window.getComputedStyle(container);
    var pl = parseFloat(cs.paddingLeft) || 0;
    var pr = parseFloat(cs.paddingRight) || 0;
    var availW = container.clientWidth - pl - pr;
    if (availW <= 0) return;
    var elW = el.scrollWidth;
    if (elW <= availW) return; /* ya cabe, no tocar */
    var ratio = availW / elW;
    var base = parseFloat(window.getComputedStyle(el).fontSize) || 16;
    /* 0.98 = pequeño margen de seguridad para evitar bordes pegados */
    el.style.fontSize = (base * ratio * 0.98).toFixed(2) + 'px';
  }

  function fitAll() {
    var nodes = document.querySelectorAll('.katex');
    for (var i = 0; i < nodes.length; i++) {
      /* Solo el .katex más externo: si su padre ya está dentro de otro .katex,
         es un span interno (no debería pasar, pero por si acaso) y lo saltamos. */
      if (nodes[i].parentElement && nodes[i].parentElement.closest('.katex')) continue;
      fitOne(nodes[i]);
    }
  }

  /* KaTeX auto-render dispara en DOMContentLoaded / load. Corremos
     varias veces para asegurar que ya rendereó todas las fórmulas. */
  function schedule() {
    fitAll();
    setTimeout(fitAll, 80);
    setTimeout(fitAll, 300);
    setTimeout(fitAll, 900);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', schedule);
  } else {
    schedule();
  }
  window.addEventListener('load', fitAll);

  /* Resize / rotación: re-ajustar con debounce. */
  var resizeTimer = null;
  window.addEventListener('resize', function () {
    if (resizeTimer) clearTimeout(resizeTimer);
    resizeTimer = setTimeout(fitAll, 120);
  });
})();
