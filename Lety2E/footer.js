// ================================================
//   lety2E — footer.js
//   Footer compartido — se inyecta en todas las páginas
//   Uso: <script src="/footer.js"></script>  (o la ruta relativa correcta)
//   Se inserta automáticamente al final del body
// ================================================

(function() {
  const year = new Date().getFullYear();
  const footer = `
  <footer class="site-footer">
    &copy; ${year} <strong>lety2E</strong> &nbsp;·&nbsp; todos los derechos reservados
  </footer>`;

  document.body.insertAdjacentHTML('beforeend', footer);
})();
