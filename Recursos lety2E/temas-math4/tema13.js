/* Tema 13 · Transformación de funciones — graficador, ejercicios y evaluación.
   f(x) = a·base(x − h) + k.  Sin librerías; las fórmulas se arman en HTML. */
(function () {
  'use strict';
  var V = '<i>x</i>';
  var FAM = {
    lin: { n: 'Lineal',         f: function (u) { return u; } },
    cua: { n: 'Cuadrática',     f: function (u) { return u * u; } },
    abs: { n: 'Valor absoluto', f: function (u) { return Math.abs(u); } },
    rad: { n: 'Con radical',    f: function (u) { return u < 0 ? NaN : Math.sqrt(u); } },
    rac: { n: 'Racional',       f: function (u) { return u === 0 ? NaN : 1 / u; } },
    exp: { n: 'Exponencial',    f: function (u, p) { return Math.pow(p.b || 2, u); } },
    sen: { n: 'Seno',           f: function (u) { return Math.sin(u); } },
    cos: { n: 'Coseno',         f: function (u) { return Math.cos(u); } }
  };
  var ORDEN = ['lin', 'cua', 'abs', 'rad', 'rac', 'exp', 'sen', 'cos'];
  var AV = [0.5, 1, 2, 3];                       /* comprimir … estirar */

  function val(p, x) {
    var u = (p.fx ? -1 : 1) * (x - (p.h || 0));
    if (Math.abs(u) < 1e-9) u = 0;
    return p.a * FAM[p.fam].f(u, p) + (p.k || 0);
  }
  function base(fam, p) { return { fam: fam, a: 1, h: 0, k: 0, b: p && p.b, fx: false }; }

  /* ── fórmula en HTML ── */
  function coef(a) {
    var m = Math.abs(a);
    if (m === 1) return '';
    if (m === 0.5) return '½';
    if (Math.abs(m - 1 / 3) < 1e-9) return '⅓';
    return String(m);
  }
  function frac(n, d) { return '<span class="fr"><span>' + n + '</span><span>' + d + '</span></span>'; }
  function formula(p) {
    var h = p.h || 0, k = p.k || 0, c = coef(p.a), s = p.a < 0 ? '−' : '';
    var inner = (p.fx ? '−' + V : V) + (h > 0 ? ' − ' + h : h < 0 ? ' + ' + (-h) : '');
    var par = '(' + inner + ')', b;
    switch (p.fam) {
      case 'lin': b = h ? ((c || s) ? c + par : inner) : c + V; break;
      case 'cua': b = c + (h ? par : V) + '<sup>2</sup>'; break;
      case 'abs': b = c + '|' + inner + '|'; break;
      case 'rad': b = c + '<span class="rz">√<span>' + inner + '</span></span>'; break;
      case 'rac':
        var m = Math.abs(p.a);
        b = m >= 1 ? frac(m, inner) : frac(1, Math.round(1 / m) + (h ? par : V));
        break;
      case 'exp': b = (p.b || 2) + '<sup>' + inner + '</sup>'; if (c) b = c + '(' + b + ')'; break;
      default: b = (c ? c + ' ' : '') + p.fam + (h ? par : ' ' + V);
    }
    return '<i>f</i>(' + V + ') = ' + s + b + (k > 0 ? ' + ' + k : k < 0 ? ' − ' + (-k) : '');
  }
  function describe(p) {
    var t = [], h = p.h || 0, k = p.k || 0, m = Math.abs(p.a);
    if (p.a < 0) t.push('reflejada');
    if (m > 1) t.push(m === 2 ? 'estirada al doble' : m === 3 ? 'estirada al triple' : 'estirada');
    if (m < 1) t.push('comprimida a la mitad');
    if (h > 0) t.push('derecha ' + h);
    if (h < 0) t.push('izquierda ' + (-h));
    if (k > 0) t.push('sube ' + k);
    if (k < 0) t.push('baja ' + (-k));
    return t.length ? t.join(' · ') : 'sin movimientos';
  }

  /* ── plano: 1 cuadro = 1 unidad, de −8 a 8 ── */
  var U = 20, R = 8.5, T = 2 * R * U;
  function X(x) { return (x + R) * U; }
  function Y(y) { return (R - y) * U; }
  var FONDO = (function () {
    var o = '', i;
    for (i = -8; i <= 8; i++) {
      o += '<line x1="' + X(i) + '" y1="0" x2="' + X(i) + '" y2="' + T + '" stroke="#E0C4BC" stroke-width="0.5"/>';
      o += '<line x1="0" y1="' + Y(i) + '" x2="' + T + '" y2="' + Y(i) + '" stroke="#E0C4BC" stroke-width="0.5"/>';
    }
    o += '<line x1="0" y1="' + Y(0) + '" x2="' + T + '" y2="' + Y(0) + '" stroke="#7B5A50" stroke-width="1.2"/>';
    o += '<line x1="' + X(0) + '" y1="0" x2="' + X(0) + '" y2="' + T + '" stroke="#7B5A50" stroke-width="1.2"/>';
    for (i = -8; i <= 8; i++) {
      if (!i) continue;
      o += '<text x="' + X(i) + '" y="' + (Y(0) + 11) + '" text-anchor="middle" font-size="8" fill="#7B5A50">' + i + '</text>';
      o += '<text x="' + (X(0) - 4) + '" y="' + (Y(i) + 3) + '" text-anchor="end" font-size="8" fill="#7B5A50">' + i + '</text>';
    }
    return o;
  })();
  function trazo(p) {
    var d = '', abierto = false, py = null, i, x, y;
    for (i = 0; i <= 850; i++) {
      x = Math.round((-R + i * 0.02) * 100) / 100;
      y = val(p, x);
      if (!isFinite(y) || (p.fam === 'rac' && py !== null && Math.abs(y - py) > 6)) { abierto = false; py = null; continue; }
      py = y;
      y = Math.max(-30, Math.min(30, y));
      d += (abierto ? 'L' : 'M') + X(x).toFixed(1) + ' ' + Y(y).toFixed(1);
      abierto = true;
    }
    return d;
  }
  function plano(capas, etiqueta) {
    var o = '<svg class="tf-svg" viewBox="0 0 ' + T + ' ' + T + '" width="' + T + '" height="' + T +
            '" role="img" aria-label="' + etiqueta + '">' + FONDO;
    capas.forEach(function (c) {
      if (!c) return;
      o += '<path d="' + trazo(c.p) + '" fill="none" stroke="' + c.color + '" stroke-width="' + c.w +
           '" stroke-linecap="round" stroke-linejoin="round"' + (c.dash ? ' stroke-dasharray="' + c.dash + '"' : '') +
           (c.op ? ' opacity="' + c.op + '"' : '') + '/>';
    });
    return o + '</svg>';
  }
  var C_BASE = { color: '#7B5A50', w: 1.2, dash: '4 3' };
  var C_META = { color: '#7B2CBF', w: 6, op: 0.38 };
  var C_MIA  = { color: '#FF00AA', w: 2.4 };
  function capa(estilo, p) { return { p: p, color: estilo.color, w: estilo.w, dash: estilo.dash, op: estilo.op }; }

  /* ── laboratorio: plano + deslizadores ── */
  function ctl(nombre, clave, min, max) {
    return '<div class="tf-ctl"><span class="tf-ctl-n">' + nombre + '</span>' +
      '<button type="button" class="tf-paso" data-c="' + clave + '" data-d="-1" aria-label="' + nombre + ': menos">−</button>' +
      '<input type="range" min="' + min + '" max="' + max + '" step="1" data-c="' + clave + '" aria-label="' + nombre + '">' +
      '<button type="button" class="tf-paso" data-c="' + clave + '" data-d="1" aria-label="' + nombre + ': más">+</button>' +
      '<output data-o="' + clave + '"></output></div>';
  }
  /* La regla con sus números en cajitas: cada una se cambia con sus flechas. Los números van
     COMO SE ESCRIBEN en la regla (adentro es x + c, con c = −h), para que se vea la relación. */
  var AS = [-3, -2, -1, -0.5, 0.5, 1, 2, 3], SIN_C = { lin: 1, sen: 1, cos: 1 };
  /* Práctica: la forma general con letras a, b, c de colores; la regla ya sustituida, limpia;
     y aparte "a = 2" con flechitas. Internamente: a = coeficiente, b = −h (adentro es x + b), c = k. */
  function letra(l) { return '<i class="tf-l tf-l-' + l + '">' + l + '</i>'; }
  function general(fam, p) {
    var inner = V + (SIN_C[fam] ? '' : ' + ' + letra('b')), A = letra('a'), g;
    switch (fam) {
      case 'lin': g = A + V; break;
      case 'cua': g = A + '(' + inner + ')<sup>2</sup>'; break;
      case 'abs': g = A + '|' + inner + '|'; break;
      case 'rad': g = A + '<span class="rz">√<span>' + inner + '</span></span>'; break;
      case 'rac': g = frac(A, inner); break;
      case 'exp': g = A + '(' + (p.b || 2) + '<sup>' + inner + '</sup>)'; break;
      default: g = A + ' ' + fam + (SIN_C[fam] ? ' ' + V : '(' + inner + ')');
    }
    return '<i>f</i>(' + V + ') = ' + g + ' + ' + letra('c');
  }
  function num(n) { var m = Math.abs(n); return (n < 0 ? '−' : '') + (m === 0.5 ? '½' : m); }
  function paso(l, par, valor) {
    return '<span class="tf-par">' + letra(l) + ' = <b>' + num(valor) + '</b><span class="tf-fls">' +
      '<button type="button" class="tf-fl" data-p="' + par + '" data-d="1" aria-label="' + l + ': aumentar">▲</button>' +
      '<button type="button" class="tf-fl" data-p="' + par + '" data-d="-1" aria-label="' + l + ': disminuir">▼</button></span></span>';
  }
  function valores(p) {
    return '<span class="tf-vals">' + letra('a') + ' = ' + num(p.a) + (SIN_C[p.fam] ? '' : ', ' + letra('b') + ' = ' + num(-(p.h || 0))) +
           ', ' + letra('c') + ' = ' + num(p.k || 0) + '</span>';
  }
  function editor(p, sinRegla) {
    return '<div class="tf-forma">' + general(p.fam, p) + '</div>' +
           (sinRegla ? '' : '<div class="tf-real">' + formula(p) + '</div>') +
           '<div class="tf-pars">' + paso('a', 'a', p.a) + (SIN_C[p.fam] ? '' : paso('b', 'c', -(p.h || 0))) +
           paso('c', 'k', p.k || 0) + '</div>';
  }
  function Lab(raiz, modo) {
    if (modo === 'regla') raiz.classList.add('tf-modo-regla');
    var est = { fam: 'cua', k: 0, h: 0, ai: 1, ref: false }, meta = null, verFormula = true, alCambiar = null, ciego = false;
    raiz.innerHTML =
      '<div class="tf-formula" aria-live="polite"></div>' +
      '<div class="tf-plano"></div>' +
      '<div class="tf-mov"></div>' +
      '<div class="tf-ctls">' + ctl('Subir / bajar', 'k', -6, 6) + ctl('Izquierda / derecha', 'h', -6, 6) +
        ctl('Comprimir / estirar', 'ai', 0, 3) +
        '<div class="tf-ctl tf-ctl-ref"><button type="button" class="tf-ref" aria-pressed="false">Reflejar</button>' +
        '<button type="button" class="tf-cero">' + (modo === 'regla' ? 'Volver a la función básica' : 'Regresar al inicio') + '</button></div></div>';
    var q = function (s) { return raiz.querySelector(s); };
    function p() { return { fam: est.fam, a: (est.ref ? -1 : 1) * AV[est.ai], h: est.h, k: est.k, b: est.b, fx: false }; }
    function pinta() {
      var yo = p();
      q('.tf-plano').innerHTML = plano([capa(C_BASE, base(est.fam, est)), meta && capa(C_META, meta), !ciego && capa(C_MIA, yo)],
                                       'Gráfica de la función');
      q('.tf-formula').innerHTML = !verFormula ? '' : modo === 'regla' ? editor(yo, ciego) : formula(yo);
      q('.tf-formula').style.display = verFormula ? '' : 'none';
      q('.tf-mov').textContent = verFormula && !ciego ? describe(yo) : '';
      q('.tf-mov').style.display = verFormula && !ciego ? '' : 'none';
      ['k', 'h', 'ai'].forEach(function (c) {
        raiz.querySelector('input[data-c="' + c + '"]').value = est[c];
        raiz.querySelector('output[data-o="' + c + '"]').textContent = c === 'ai' ? (est.ai === 0 ? '½' : AV[est.ai]) : est[c];
      });
      q('.tf-ref').setAttribute('aria-pressed', est.ref ? 'true' : 'false');
      if (alCambiar) alCambiar(yo);
    }
    raiz.addEventListener('input', function (e) {
      var c = e.target.getAttribute && e.target.getAttribute('data-c');
      if (c && e.target.type === 'range') { est[c] = +e.target.value; pinta(); }
    });
    raiz.addEventListener('click', function (e) {
      var b = e.target.closest ? e.target.closest('button') : null;
      if (!b) return;
      if (b.classList.contains('tf-paso')) {
        var c = b.getAttribute('data-c'), inp = raiz.querySelector('input[data-c="' + c + '"]');
        est[c] = Math.max(+inp.min, Math.min(+inp.max, est[c] + (+b.getAttribute('data-d'))));
        pinta();
      } else if (b.classList.contains('tf-fl')) {
        var par = b.getAttribute('data-p'), d = +b.getAttribute('data-d');
        if (par === 'k') est.k = Math.max(-6, Math.min(6, est.k + d));
        if (par === 'c') est.h = Math.max(-6, Math.min(6, est.h - d));
        if (par === 'a') {
          var i = Math.max(0, Math.min(AS.length - 1, AS.indexOf((est.ref ? -1 : 1) * AV[est.ai]) + d));
          est.ref = AS[i] < 0; est.ai = AV.indexOf(Math.abs(AS[i]));
        }
        pinta();
        var foco = raiz.querySelector('.tf-fl[data-p="' + par + '"][data-d="' + d + '"]');
        if (foco) foco.focus();
      } else if (b.classList.contains('tf-ref')) { est.ref = !est.ref; pinta(); }
      else if (b.classList.contains('tf-cero')) { api.cero(); }
    });
    var api = {
      familia: function (f, b) { est.fam = f; est.b = b; api.cero(); },
      cero: function () { est.k = 0; est.h = 0; est.ai = 1; est.ref = false; pinta(); },
      valor: p,
      meta: function (m) { meta = m; pinta(); },
      formula: function (v) { verFormula = v; pinta(); },
      ciego: function (v) { ciego = v; raiz.classList.toggle('tf-ciego', v); pinta(); },
      alCambiar: function (f) { alCambiar = f; }
    };
    pinta();
    return api;
  }

  /* ══ 1 · Explorador ══ */
  var exp = document.getElementById('tf-explorador');
  if (exp) {
    var chips = exp.querySelector('.tf-fams'), lab = Lab(exp.querySelector('.tf-lab'));
    chips.innerHTML = ORDEN.map(function (f, i) {
      return '<button type="button" class="tf-chip" data-f="' + f + '" aria-pressed="' + (f === 'cua') + '">' +
             FAM[f].n + '</button>';
    }).join('');
    chips.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      [].forEach.call(chips.children, function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      lab.familia(b.getAttribute('data-f'));
    });
  }

  /* ══ 2 · Ejercicios: la lista de Lety, con "ver gráfica" ══ */
  function P(fam, a, h, k, extra) { var o = { fam: fam, a: a, h: h || 0, k: k || 0 }; if (extra) for (var z in extra) o[z] = extra[z]; return o; }
  var LISTA = [
    ['Lineales', [P('lin', 1), P('lin', -1), P('lin', 1, 0, -4), P('lin', 1, 0, 3), P('lin', 0.5), P('lin', 3),
                  P('lin', -1, 0, 3), P('lin', -1, 0, -1), P('lin', -4), P('lin', -2, 0, 5), P('lin', -1 / 3, 0, 2),
                  P('lin', -1, 0, 2, { lbl: '<i>f</i>(' + V + ') = 2 − ' + V })]],
    ['Cuadráticas', [P('cua', 1, 0, -3), P('cua', 1, 0, 1), P('cua', -1), P('cua', -1, 0, 4), P('cua', 1, -4), P('cua', 1, 1),
                     P('cua', -1, -1), P('cua', -1, 4), P('cua', 1, -2, 4), P('cua', 1, 1, -3), P('cua', -1, 1, 1), P('cua', -1, -2, -3)]],
    ['Valor absoluto', [P('abs', 1), P('abs', -1), P('abs', 1, 0, 2), P('abs', -1, 0, -3), P('abs', 1, 4), P('abs', -1, -1),
                        P('abs', 1, -3, -2), P('abs', -1, 2, 3)]],
    ['Trigonométricas', [P('sen', 1), P('cos', 1), P('sen', -1), P('cos', -1), P('sen', 1, 0, 1), P('sen', 1, 0, -3),
                         P('cos', 1, 0, -3), P('cos', 1, 0, 4)]],
    ['Racionales', [P('rac', 1, 4, 1), P('rac', 1, -3, 2), P('rac', 1, 1, -2), P('rac', 1, -2, -3), P('rac', 1, -4, -5)]],
    ['Exponenciales', [P('exp', 1), P('exp', -1), P('exp', 1, 0, 0, { fx: true }), P('exp', 1, 0, 0, { b: 3 }),
                       P('exp', -1, 0, 0, { b: 3 }), P('exp', 1, 0, 0, { b: 3, fx: true })]],
    ['Con radicales', [P('rad', 1, 0, 2), P('rad', -1, 0, -3), P('rad', 1, -1), P('rad', -1, 5), P('rad', 1, 4, 3), P('rad', -1, -1, -4)]]
  ];
  var ej = document.getElementById('tf-ejercicios');
  if (ej) {
    ej.innerHTML = LISTA.map(function (g, gi) {
      return '<div class="mini-card"><div class="mini-card-head">' + g[0] + '</div><div class="mini-card-body">' +
        '<div class="tf-lista">' + g[1].map(function (p, i) {
          return '<button type="button" class="tf-fn" data-g="' + gi + '" data-i="' + i + '">' + (p.lbl || formula(p)) + '</button>';
        }).join('') + '</div><div class="tf-ver" hidden></div></div></div>';
    }).join('');
    ej.addEventListener('click', function (e) {
      var b = e.target.closest('.tf-fn'); if (!b) return;
      var cuerpo = b.closest('.mini-card-body'), ver = cuerpo.querySelector('.tf-ver');
      var ya = b.getAttribute('aria-pressed') === 'true';
      [].forEach.call(cuerpo.querySelectorAll('.tf-fn'), function (x) { x.setAttribute('aria-pressed', 'false'); });
      if (ya) { ver.hidden = true; ver.innerHTML = ''; return; }
      var p = LISTA[+b.getAttribute('data-g')][1][+b.getAttribute('data-i')];
      b.setAttribute('aria-pressed', 'true');
      ver.hidden = false;
      ver.innerHTML = '<div class="tf-formula">' + (p.lbl || formula(p)) + '</div>' +
        plano([capa(C_BASE, base(p.fam, p)), capa(C_MIA, p)], 'Gráfica de la función elegida') +
        '<div class="tf-mov">punteada: la función base</div>';
    });
  }

  /* ══ 3 · Reactivos al azar (sirven a la práctica y a la evaluación) ══ */
  function azar(n) { return Math.floor(Math.random() * n); }
  function revuelve(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = azar(i + 1), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  var SIN_H = { lin: 1, sen: 1, cos: 1 }, SIN_A = { exp: 1 };
  function arma() {
    var simples = revuelve([['k+'], ['k-'], ['h+'], ['h-'], ['ref'], ['est'], ['com']]);
    var todasDobles = revuelve([['h+', 'k-'], ['ref', 'k+'], ['h-', 'est'], ['ref', 'h+', 'k+'], ['com', 'k-'], ['ref', 'h-'], ['est', 'k+'], ['com', 'h+']]);
    var recetas = revuelve(simples.concat(todasDobles)), tipos = revuelve('BBBBBCCCCCDDDDD'.split(''));
    var bolsa = [];
    return recetas.map(function (rec, n) {
      var sirve = function (f) {
        return !rec.some(function (m) { return (m.charAt(0) === 'h' && SIN_H[f]) || ((m === 'est' || m === 'com') && SIN_A[f]); });
      };
      if (!bolsa.some(sirve)) bolsa = bolsa.concat(revuelve(ORDEN));
      var fam = bolsa.filter(sirve)[0];
      bolsa.splice(bolsa.indexOf(fam), 1);
      var p = { fam: fam, a: 1, h: 0, k: 0 };
      rec.forEach(function (m) {
        if (m === 'k+') p.k = 1 + azar(4);
        if (m === 'k-') p.k = -(1 + azar(4));
        if (m === 'h+') p.h = 1 + azar(4);
        if (m === 'h-') p.h = -(1 + azar(4));
        if (m === 'est') p.a *= 2 + azar(2);
        if (m === 'com') p.a *= 0.5;
        if (m === 'ref') p.a *= -1;
      });
      var it = { tipo: tipos[n], p: p };
      if (it.tipo === 'C') it.ops = opciones(p);
      return it;
    });
  }
  function iguales(p, q) {
    for (var x = -8; x <= 8; x += 0.25) {
      var a = val(p, x), b = val(q, x), fa = isFinite(a), fb = isFinite(b);
      if (fa !== fb) return false;
      if (fa && Math.abs(a - b) > 1e-6) return false;
    }
    return true;
  }
  /* Cinco reglas: la correcta y cuatro con los errores típicos (signo de h, signo de k,
     h y k cambiados, reflejo, estirar por comprimir). Ninguna da la misma gráfica que otra. */
  function opciones(p) {
    function c(d) { var o = { fam: p.fam, a: p.a, h: p.h, k: p.k }; for (var z in d) o[z] = d[z]; return o; }
    var m = Math.abs(p.a), s = p.a < 0 ? -1 : 1, otro = m === 2 ? 0.5 : m === 0.5 ? 2 : m === 3 ? 0.5 : 2;
    var cand = [c({ h: -p.h }), c({ k: -p.k }), c({ a: -p.a }), c({ h: p.k, k: p.h }), c({ h: -p.h, k: -p.k }),
                c({ a: s * otro }), c({ a: -p.a, k: -p.k }), c({ h: -p.k, k: -p.h }), c({ a: -p.a, h: -p.h })];
    cand = revuelve(cand.filter(function (q) { return !(SIN_H[q.fam] && q.h) && !(SIN_A[q.fam] && Math.abs(q.a) !== 1); }));
    var lista = [p], guarda = 0;
    function mete(q) {
      if (lista.length < 5 && Math.abs(q.h) <= 6 && Math.abs(q.k) <= 6 &&
          !lista.some(function (r) { return iguales(r, q); })) lista.push(q);
    }
    cand.forEach(mete);
    while (lista.length < 5 && guarda++ < 200) {
      var d = { k: p.k + (azar(2) ? 1 : -1) * (1 + azar(3)) };
      if (azar(2)) d.a = (azar(2) ? 1 : -1) * (SIN_A[p.fam] ? 1 : AV[azar(4)]);
      if (!SIN_H[p.fam] && azar(2)) d.h = p.h + (azar(2) ? 1 : -1) * (1 + azar(2));
      mete(c(d));
    }
    return revuelve(lista);
  }

  /* ══ 4 · Práctica: llegar a la gráfica morada ══ */
  var pr = document.getElementById('tf-practica');
  if (pr) {
    var labP = Lab(pr.querySelector('.tf-lab'), 'regla'), objetivo = null, avisoP = pr.querySelector('.tf-aviso'), logradas = 0;
    function otra() {
      var it = arma()[azar(15)];
      objetivo = it.p;
      pr.querySelector('.tf-fam').textContent = FAM[objetivo.fam].n;
      labP.familia(objetivo.fam);
      labP.meta(objetivo);
    }
    labP.alCambiar(function (yo) {
      if (!objetivo) return;
      var ok = iguales(yo, objetivo);
      avisoP.className = 'tf-aviso ' + (ok ? 'tf-bien' : 'tf-pend');
      var enBase = iguales(yo, base(objetivo.fam, objetivo));
      avisoP.innerHTML = ok
        ? '✓ ¡Llegaste! Los parámetros de la morada son ' + valores(objetivo) + '.'
        : (enBase ? 'Estás en la función básica: ' + valores(base(objetivo.fam, objetivo)) + '. ' : '') +
          'Cambia ' + (SIN_C[objetivo.fam] ? 'a y c' : 'a, b y c') + ' hasta llegar a los parámetros de la morada.';
    });
    pr.addEventListener('click', function (e) {
      var b = e.target.closest('.tf-otra-meta'); if (b) otra();
    });
    otra();
  }

  /* ══ 5 · Evaluación: 5 de acomodar + 5 de elegir la regla + 5 de parámetros a, b, c; se revisa hasta el final ══ */
  var ev = document.getElementById('tf-evalua');
  if (ev) {
    var inicio = ev.querySelector('.tf-inicio'), corre = ev.querySelector('.tf-corre'), fin = ev.querySelector('.tf-fin');
    var cajaLab = corre.querySelector('.tf-lab'), cajaElige = corre.querySelector('.tf-elige');
    var cajaPar = corre.querySelector('.tf-labp'), labE = Lab(cajaLab), labD = Lab(cajaPar, 'regla'), S = null, TOTAL = 15, PASA = 12;
    var NOMBRE = { B: 'acomodar', C: 'elegir la regla', D: 'parámetros a, b, c' };
    labD.ciego(true);
    function muestra(panel) { [inicio, corre, fin].forEach(function (x) { x.hidden = x !== panel; }); }
    function reactivo() {
      var it = S.items[S.i], esB = it.tipo === 'B', esD = it.tipo === 'D';
      corre.querySelector('.tf-num').textContent = 'Evaluación · reactivo ' + (S.i + 1) + ' de ' + TOTAL;
      corre.querySelector('.tf-fam').textContent = FAM[it.p.fam].n;
      cajaLab.hidden = !esB; cajaPar.hidden = !esD; cajaElige.hidden = esB || esD;
      if (esD) {
        corre.querySelector('.tf-pide').innerHTML = 'La punteada es la función básica y la <strong class="tf-morada">morada</strong> es la transformada. ' +
          '<strong>Escribe los parámetros de la morada</strong> con las flechas. Aquí tu gráfica no se dibuja.';
        labD.familia(it.p.fam); labD.meta(it.p);
      } else if (esB) {
        corre.querySelector('.tf-pide').innerHTML = 'Acomoda la gráfica de <span class="tf-formula tf-enlinea">' + formula(it.p) + '</span>';
        labE.formula(false); labE.familia(it.p.fam); labE.meta(null);
      } else {
        corre.querySelector('.tf-pide').innerHTML = 'La punteada es la función base y la rosa es la transformada. ' +
          '<strong>Elige la regla de correspondencia de la rosa.</strong>';
        cajaElige.querySelector('.tf-plano').innerHTML =
          plano([capa(C_BASE, base(it.p.fam, it.p)), capa(C_MIA, it.p)], 'Función base y función transformada');
        cajaElige.querySelector('.tf-ops').innerHTML = it.ops.map(function (o, i) {
          return '<button type="button" class="tf-op" data-i="' + i + '" aria-pressed="false">' + formula(o) + '</button>';
        }).join('');
        it.sel = null;
      }
      corre.querySelector('.tf-sig').textContent = S.i === TOTAL - 1 ? 'Terminar' : 'Siguiente';
    }
    function siguiente() {
      var it = S.items[S.i];
      it.resp = it.tipo === 'B' ? labE.valor() : it.tipo === 'D' ? labD.valor() : (it.sel === null ? null : it.ops[it.sel]);
      it.ok = !!it.resp && iguales(it.resp, it.p);
      S.i++;
      if (S.i < TOTAL) { reactivo(); corre.scrollIntoView({ block: 'start' }); } else termina();
    }
    function termina() {
      var buenas = S.items.filter(function (x) { return x.ok; }).length, pasa = buenas >= PASA, f = new Date();
      var h = '<p class="tf-quien">' + (S.nombre ? S.nombre.replace(/[<>&]/g, '') + ' · ' : '') +
              f.toLocaleDateString('es-MX', { day: 'numeric', month: 'long', year: 'numeric' }) + ' · ' +
              f.toLocaleTimeString('es-MX', { hour: '2-digit', minute: '2-digit' }) + '</p>' +
              '<p class="tf-marca">' + buenas + ' de ' + TOTAL + '</p>' +
              '<p class="tf-veredicto ' + (pasa ? 'tf-bien' : 'tf-mal') + '">' +
              (pasa ? 'Pasaste tu evaluación' : 'Todavía no: necesitas ' + PASA + ' de ' + TOTAL) + '</p>';
      h += '<div class="tf-tabla">' + S.items.map(function (it) {
        return '<div class="tf-fila ' + (it.ok ? 'tf-bien' : 'tf-mal') + '">' +
          '<span class="tf-formula tf-enlinea">' + formula(it.p) + '</span>' +
          '<span class="tf-res" aria-label="' + (it.ok ? 'correcto' : 'incorrecto') + '">' + (it.ok ? '✓' : '✗') + '</span></div>';
      }).join('') + '</div>';
      fin.querySelector('.tf-resultado').innerHTML = h;
      muestra(fin);
      fin.scrollIntoView({ block: 'start' });
    }
    ev.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      if (b.classList.contains('tf-go-eval')) {
        S = { items: arma(), i: 0, nombre: (ev.querySelector('.tf-nombre').value || '').trim() };
        muestra(corre); reactivo(); corre.scrollIntoView({ block: 'start' });
      } else if (b.classList.contains('tf-op')) {
        var it = S.items[S.i]; it.sel = +b.getAttribute('data-i');
        [].forEach.call(cajaElige.querySelectorAll('.tf-op'), function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      } else if (b.classList.contains('tf-sig')) siguiente();
      else if (b.classList.contains('tf-otra')) { muestra(inicio); ev.scrollIntoView({ block: 'start' }); }
    });
    muestra(inicio);
  }
  window.__tf = { arma: arma, iguales: iguales, formula: formula, describe: describe, val: val, LISTA: LISTA, opciones: opciones };
})();
