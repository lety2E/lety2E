# lety2e.com — Guía de Desarrollo

**Proyecto:** Sitio personal de Lety (Math · Lupián · Apuntes) · HTML + CSS + JS vanilla · GitHub Pages
**Repo:** `github.com/lety2E/lety2E` (branch `main`) · **Dominio:** `lety2e.com`
**Local:** `~/Desktop/lety2E 2/`

> Esta guía documenta **decisiones, preferencias y fuentes externas** que no se pueden inferir leyendo el código. La estructura, paleta y rutas se ven directamente en el repo (`ls`, `style.css`, `nav.js`).

---

## 📋 Filosofía

- **Minimalista** — "paquetitos" en vez de muros de texto.
- **Mantenible** — un único `style.css`, `nav.js`, `footer.js`. Variantes con `body[data-section]`.
- **Real first** — nunca inventar contenido para llenar. Lo que no existe se marca `próximamente`. Si una respuesta en captura tiene error aritmético, publicar la correcta y avisar.
- **Orgánica** — Apuntes y Relatos crecen como listas planas; sólo se subdividen cuando un tipo se acumula.
- **File:// compatible** — todas las rutas relativas; el sitio funciona local o en GitHub Pages.

---

## 🗂️ Fuentes de contenido para Math (críticas)

### 1. Doc LaTeX en Drive — fuente de verdad para procedimiento y respuestas
- **ID:** `1hTzKA2zC98FwfSiR9nR21gExC2hT4nrea-BANrbkd4I` ("latex matematicas 1")
- Cada tema separado por `# N nombre` (ej. `# 5 expresiones algebraicas`)
- Contiene: ejemplos resueltos, ejercicios, resoluciones (a veces parciales), extras
- **Cuidado con duplicados:** ocasionalmente una sección tiene contenido copy/paste del tema previo (header dice X pero el `\textbf{...}` interno dice Y). Si discrepa, **avisar a Lety y saltar el tema** hasta que ella lo arregle. Nunca inventar para llenar.

### 2. Capturas — referencia visual
- Ruta: `~/Desktop/capturas/matematicas N/M tema-nombre/`
- Si el doc LaTeX y la captura difieren, **prevalece el LaTeX**.

### 3. CSV de videos de YouTube
- Ruta: `~/Desktop/capturas/lista_videos_youtube.csv`
- Si un tema no aparece: **omitir sección de Video** (no es error).
- Lety pasa videos nuevos directo en chat. **No hacer fetch a `letymath.com`** (bloqueado, desperdicia tokens).

---

## 🏗️ Arquitectura (lo no obvio)

La estructura de carpetas se ve con `ls`. Lo importante saber:

- **Una sola fuente de verdad** para chrome: `style.css`, `nav.js`, `footer.js`. Variaciones por `body[data-section]`.
- **Apuntes son self-contained**: cada `.html` lleva su propio CSS y JS inline. No usa los archivos globales.
- **Temas de Math** sí usan `style.css` global + un bloque `<style>` inline con clases específicas del paquetito.

### Valores de `data-section`

| Valor | Dónde |
|-------|-------|
| `home` | Portada |
| `math` | Todo dentro de `math/` (índices **y** temas) — siempre `math`, nunca `letymath` |
| `lupian` | `lupian/index.html` y `lupian/cantos/` |
| `relatos` | `lupian/relatos/` |
| `apuntes` | Todo dentro de `apuntes/` (index y artefactos) |

### Sistema de color por sección

El CSS usa `--section-color` y `--section-hover`:

| Sección | `--section-color` | `--section-hover` | h1 cuerpo |
|---------|-------------------|-------------------|-----------|
| Home, Lupián, Cantos | Magenta | Turquesa | Magenta |
| Math, Apuntes | Turquesa | Magenta | Morado (`--P`) |
| Relatos | Magenta | Turquesa | Magenta (override en `.relato-morado` → morado) |

**Regla:** NUNCA inventar colores fuera del palette de `style.css`. Excepción: pills de fórmula en math (ver § Estilo de resoluciones).

---

## 📦 Patrón "Paquetitos" para temas de Math

Referencias canónicas (ground truth — si algo aquí contradice estos archivos, **gana el archivo**):
- `math/matematicas-1/operaciones-basicas.html` — sin video, bloques 3 col, respuestas línea simple
- `math/matematicas-1/jerarquia.html` — 1 video, bloques 2 col, respuestas con `\begin{aligned}`
- `math/matematicas-1/area-perimetro.html` — con SVG de triángulos
- `math/matematicas-1/pendiente-ordenada.html` — con SVG de recta + comprobación

### Orden de secciones (variante clásica)
1. Video(s) — opcional, 1-2 lado a lado
2. Apuntes — opcional, si Lety provee texto
3. Ejemplo(s) — 1 a 5, en `.ejemplo-block` con `.ejemplo-grid` (2 col)
4. Ejercicios — `.bloques-2` o `.bloques-3` siempre visibles
5. Respuestas — colapsables
6. Ejercicios extra — colapsables, sin respuestas (igual que en el doc)
7. Navegación prev/next

### Selección de grid

| Tipo | Grid |
|------|------|
| Operaciones simples 6×6 | `.bloques-3` |
| Ecuaciones, expresiones, monomios | `.bloques-2` |
| Si dudas | `.bloques-2` |

---

## 🎨 Estilo de resoluciones (confirmado por Lety)

Para temas con fórmulas (geometría, exponentes, mcm/MCD) usa estilo cuaderno con highlighters.

### Notación
- Área: `a` (minúscula, no `A`)
- Lados/distancias en triángulos: `m`, `n` (no `l_1`, `l_2`)
- Distancia entre dos puntos: Pitagórica explícita `c = √(a² + b²)`
- Resultado final con `=` directo, no `≈`

### Pills coloridas (única excepción al palette)

| Color | Hex bg / border | Uso |
|-------|------|-----|
| `.formula-pill` (amarillo) | `#FFF1A8` / `#F5DC6A` | Fórmulas conceptuales: `c = √(a²+b²)`, `P = b + m + n` |
| `.formula-pill.salmon` | `#FFD9B8` / `#F5B584` | Fórmulas de cálculo principal: `área = (b·h)/2` |
| `.resultado-pill` (rosa) | `#FFD0E5` / `#FF8AC0` (texto `--M`) | Resultados finales: `12 u²`, `16.12 u` |

### Procedimiento conciso (no desde coordenadas)

❌ `m = √((3-(-1))² + (7-2)²) = √(4²+5²) = 6.40`
✅ `m = √(4² + 5²) = √(16+25) = √41 = 6.40`

Catetos identificados implícitamente del diagrama.

---

## 📐 Gráficas SVG inline

Para rectas y triángulos: SVG inline (no TikZ, no libs externas — file:// compatible).

### Reglas
- **1 cuadro = 1 unidad** en ambos ejes (viewBox proporcional al rango).
- Grid `#E0C4BC` stroke 0.5, ejes `#7B5A50` stroke 1.2, recta `#FF00AA` stroke 2.2.
- Triángulo: relleno magenta 15% opacity + contorno sólido.
- Puntos: círculo `#1A0828` r=3.
- CSS: `max-width: 240px; max-height: 380px; height: auto;`. **Nunca** `width: auto; height: auto` sin atributos — colapsa a 0×0 en flex.
- Si necesitas varias gráficas, escribe un helper Python en `/tmp/`.

---

## 🚧 Contenido faltante o duplicado

| Caso | Tratamiento |
|------|-------------|
| Curso de Math sin temas | `.proximamente-card` + `.pronto` + `.pronto-badge` en `math/index.html` |
| Curso con algunos temas | Index muestra reales + `.proximamente-nota` al final |
| Tema con header pero contenido duplicado en doc | **Saltar** y avisar a Lety |
| Tema sin video en CSV | Omitir sección de Video (no es error) |
| Tema sin respuestas | Sólo ejercicios + extras. Si hay que calcularlas, paso a paso |
| Card sin destino real | Borrarla. Nunca dejar `href="#"` |
| Respuesta en captura con error aritmético | Publicar la correcta + flag corto al final |

---

## ✍️ Reglas de redacción para respuestas Math

- ❌ Sin flechas `→`, sin etiquetas tipo "Pos:", "Neg:", sin explicaciones de libro de texto
- ✅ Simple: `= operación = **resultado**`
- ✅ Multi-paso: `\begin{aligned}` con `\\` entre líneas
- ✅ Potencias siempre en 3 pasos: `(−4)³ = (−4)(−4)(−4) = 16(−4) = −64`
- ✅ Resultado final en `\mathbf{...}` o `<strong>` color `--M`
- ✅ Reducción de polinomios: orden por grado descendente

---

## 🚀 Workflow para agregar un tema de Math

**Cómo llega el contenido (división de trabajo con Lety):**
- **Migración (lo común):** Lety genera el borrador (código LaTeX/HTML) **con Gemini + sus capturas** (lo hace en Gemini para ahorrar tokens; el borrador no se queda ahí) y lo sube al **doc de Drive, un tema por pestaña**. Luego avisa: *"checa el tema X de tal curso"* + enlaces de YouTube. Claude revisa, arma el HTML y sube.
- **Desde cero:** algunos temas no vienen de capturas; se arman entre los dos con el mismo formato.
- Referencia para Lety: `Sistema (cómo funciona).md` en la raíz.

Detalle procedimental completo en `.claude/skills/letymath-html/SKILL.md` (skill on-demand). Aquí el resumen:

1. Verificar header `# N nombre` vs `\textbf{...}` interno en el doc LaTeX.
2. Buscar slug en el CSV de videos.
3. Generar gráficas SVG si aplica (helper Python en `/tmp/`).
4. Crear `.html` siguiendo referencias canónicas (slug en kebab-case sin tildes).
5. Botón siguiente en el tema previo, anterior en este.
6. Agregar card al index del curso (color rotando `--M`/`--T`/`--P`).
7. Commit + push a `main`.

KaTeX: ver template en cualquier tema existente — patrón estándar `katex@0.16.9` con `auto-render` y delimiters `$..$` / `$$..$$`.

---

## ➕ Agregar contenido no-Math (resumen)

- **Apunte nuevo:** archivo self-contained en `apuntes/` (guía: `apuntes/Templete-apuntes.md`; referencia canónica: `segunda-guerra-mundial.html`) + card `<a class="apunte-card">` en `apuntes/index.html`.
- **Relato nuevo:** archivo en `lupian/relatos/` (.html, .mp3, .mp4 o imagen) + `<a class="entrada-item">` en `.lista-organica` del index de relatos.
- **Cover de cantos:** `<article class="video-cover">` con iframe de YouTube en `lupian/cantos/index.html` (canal: `@Lety2eLupian`).
- **Sección nueva:** carpeta + `index.html` con su `data-section` + alta en `SECTIONS`/`ROOT_LINKS` de `nav.js` + card en el `index.html` raíz.

---

## 📱 Mobile-safety (muchos alumnos lo ven en celular — IMPORTANTE)

**Regla núm. 1**: cada renglón de ejercicio dentro de `.mini-card-body` debe ser un bloque (`<div class="ej-line">` o `<div class="sol">`), **NUNCA** `$...$<br>$...$<br>`. Con `<br>` y line-height ajustado por la media query global, las raíces tipo `\sqrt{\dfrac{a}{b}}` se traslapan con la fila anterior (la barra superior del √ queda oculta tras la fila previa).

✅ **Patrón correcto** para ejercicios:
```html
<div class="mini-card-body">
  <div class="ej-line">$-\dfrac{4}{8} + \dfrac{1}{4} =$</div>
  <div class="ej-line">$\sqrt{\dfrac{25}{36}} =$</div>
</div>
```

CSS en el `<style>` del tema:
```css
.mini-card-body { line-height: 1.6; }
.mini-card-body .ej-line {
  padding: .6rem 0;
  border-bottom: 1px solid var(--border-s);
  line-height: 2.2; /* radical-safe */
}
.mini-card-body .ej-line:last-child { border-bottom: none; padding-bottom: .25rem; }
.mini-card-body .ej-line:first-child { padding-top: .25rem; }
```

❌ **Anti-patrón** (causa raíces invisibles y cards sobresaliendo en móvil):
```html
<div class="mini-card-body" style="line-height: 4.2">  <!-- ¡NO! -->
  $\sqrt{\dfrac{25}{36}} =$<br>
  $\dfrac{3}{4} \div \dfrac{-2}{6} =$<br>
</div>
```

**Por qué**: la media query global en `style.css` hace `body[data-section="math"] .mini-card-body { line-height: 2.2 }` en móvil. Eso es suficiente para `$$...$$` y filas simples, pero `\sqrt{\dfrac{}{}}` necesita aún más altura. Por eso `.ej-line`/`.sol` traen su propia `line-height: 2.4` radical-safe (declarada también globalmente para garantizarlo en todas las páginas).

**Antes de commit, verificar en viewport 390×844 (iPhone 12) y 360×800 (Android medio)**:
- Las cards no se salen del contenedor
- Cada `\sqrt` muestra su barra superior completa
- Las fracciones no se traslapan verticalmente
- El topic-tag y el `<h1>` caben sin overflow horizontal

### Regla núm. 2 — ecuaciones jamás se parten al medio

KaTeX por defecto puede romper una ecuación inline en dos renglones cuando no cabe (rompe en `=` o en un `−` binario). Esto confunde al alumno porque parece otra operación. **Solución global** en `style.css`:

```css
body[data-section="math"] .katex { white-space: nowrap; }
body[data-section="math"] .ej-line,
body[data-section="math"] .sol   { white-space: nowrap; }
```

Consecuencia consciente: si una ecuación es más ancha que el celular, **se sale** del ancho del viewport y la página entera permite pinch-zoom + pan. Las cards NO tienen scroll horizontal interno (se removió el `overflow-x: auto` y las scroll-shadows). Mejor que el alumno haga zoom a que vea una ecuación cortada.

Por eso también el **bloque Ejemplo** (no sólo los ejercicios) debe usar `.ej-line`:

```html
<div class="ejemplo-block">
  <div class="ej-line">$2(-3)(4) = -6(4) = $ <strong>$-24$</strong></div>
  <div class="ej-line">$\sqrt{36} = $ <strong>$\pm 6$</strong></div>
</div>
```

❌ NO usar `$...$<br>$...$<br>` dentro de `.ejemplo-block` — el espacio HTML entre la ecuación y `<strong>$resultado$</strong>` sí es breakable y separa el resultado de su ecuación.

---

## 🚢 Deploy

```bash
cd ~/Desktop/lety2E\ 2/
git add . && git commit -m "..." && git push   # GitHub Pages rebuilea en 1-2 min
```

Verificar en **incógnito**. Si el favicon no aparece: `lety2e.com/favicon.svg?v=2`.

### Preview local (antes de publicar)

- Arrancar: `python3 .claude/serve.py &` → sirve el sitio en `http://127.0.0.1:8765/` (la ruta del proyecto va fija dentro del script).
- Verificar con `curl` y/o abriendo esa URL en Chrome (MCP de Chrome).
- El **panel de preview** de la app (preview_start / `.claude/launch.json`) hoy **no funciona aquí**: macOS le bloquea la carpeta Desktop a ese proceso y responde 500. No insistir por esa vía. Si algún día se quiere el panel: dar a la app Claude "Acceso total al disco" (Ajustes del Sistema → Privacidad y seguridad) y copiar `.claude/serve.py` a `/tmp/lety_serve.py`.

**Bitácora:** al hacer commit de un cambio terminado, agregar también un renglón en `bitacora.md` (raíz del proyecto, lo más reciente arriba). Los pendientes van en `Notas por revisar.md`, no en la bitácora.

### Issues conocidos
- VS Code "Unable to create HEAD.lock" → `rm -f .git/HEAD.lock`.
- "This repository moved" → `git remote set-url origin https://github.com/lety2E/lety2E.git`.
- DNS intermitente → toggle wifi.

---

## 🎯 Preferencias confirmadas (no obvias)

| Aspecto | Preferencia |
|---------|-------------|
| Colores | Solo variables de `style.css`, salvo pills de fórmula |
| Tono | Minimalista, sin explicaciones de más |
| Notación área | `a` (minúscula) |
| Lados de triángulo | `m`, `n` |
| Fórmula distancia | `c = √(a² + b²)` con "distancia entre dos puntos" |
| Procedimiento | Desde catetos, no desde coordenadas |
| Potencias | Expandidas en 3 pasos |
| Triángulos | Relleno magenta 15% + contorno sólido |
| Contenido vacío | `próximamente` (nunca inventar) |
| Tema duplicado en doc | Saltar y avisar |
| Doc fuente | Drive `1hTzKA2zC98FwfSiR9nR21gExC2hT4nrea-BANrbkd4I` |
| Videos | CSV en `~/Desktop/capturas/lista_videos_youtube.csv` |

---

*Guía mantenida por Claude · Julio 2026*
