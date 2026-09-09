// Recibe por stdin {formulas:[tex,...]} y devuelve {html:[...]}.
// Usa el mismo KaTeX del sitio, para que el examen se vea igual que la pagina.
const katex = require(require('os').homedir() + '/Desktop/lety2E/assets/katex/katex.min.js');
let raw = '';
process.stdin.on('data', d => raw += d);
process.stdin.on('end', () => {
  const { formulas } = JSON.parse(raw);
  const html = formulas.map(t => {
    try { return katex.renderToString(t, { displayMode: false, throwOnError: true }); }
    catch (e) { return { error: e.message, tex: t }; }
  });
  process.stdout.write(JSON.stringify({ html }));
});
