// ================================================
//   lety2E — nav.js
//   Navegación compartida — se inyecta en todas las páginas
//   Uso: <script src="/nav.js"></script>  (o la ruta relativa correcta)
//   Se inserta automáticamente antes del primer elemento del body
// ================================================

(function() {
  const nav = `
  <header class="site-nav">
    <div class="nav-inner">
      <a href="/" class="nav-brand">
        <div class="nav-badge"><span>2E</span></div>
        <span class="nav-name">lety2E</span>
      </a>
      <nav>
        <ul class="nav-links">
          <li><a href="https://letymath.com" target="_blank">LetyMath</a></li>
          <li><a href="/cantos/">Cantos</a></li>
          <li><a href="/escritos/">Escritos</a></li>
          <li><a href="/apuntes/">Apuntes</a></li>
          <li><a href="/la-turquesa/">La Turquesa</a></li>
        </ul>
      </nav>
      <button class="nav-ham" aria-label="menú" onclick="this.closest('.site-nav').querySelector('.nav-links').classList.toggle('open')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <line x1="3" y1="6" x2="21" y2="6"/>
          <line x1="3" y1="12" x2="21" y2="12"/>
          <line x1="3" y1="18" x2="21" y2="18"/>
        </svg>
      </button>
    </div>
  </header>`;

  // Insertar al inicio del body
  document.body.insertAdjacentHTML('afterbegin', nav);

  // Marcar link activo según URL actual
  const links = document.querySelectorAll('.nav-links a');
  links.forEach(link => {
    if (link.href !== 'https://letymath.com' &&
        window.location.pathname.startsWith(new URL(link.href).pathname) &&
        new URL(link.href).pathname !== '/') {
      link.classList.add('active');
    }
  });
})();
