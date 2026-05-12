# lety2e.com — Guía de Desarrollo

**Última actualización:** Mayo 2026
**Proyecto:** lety2e.com — Sitio personal de Lety con Math, Lupián y Apuntes
**Stack:** HTML5 + CSS3 + Vanilla JS · GitHub Pages · file:// compatible
**Repo:** `github.com/letymath/lety2E` (branch `main`)
**Dominio:** `lety2e.com` (CNAME → GitHub Pages)
**Carpeta local:** `~/Desktop/lety2E 2/` ← esta es la clonada al repo

---

## 📋 Filosofía

- **Minimalista** — "paquetitos" en vez de muros de texto.
- **Mantenible** — un único `style.css`, `nav.js`, `footer.js`. Variantes con `body[data-section]`.
- **Real first** — nunca inventar contenido para llenar. Lo que no existe se marca como `próximamente`. Si una respuesta en captura tiene error aritmético, publicar la correcta y avisar.
- **Orgánica** — Apuntes y Relatos crecen como listas planas; sólo se subdividen cuando un tipo se acumula.
- **File:// compatible** — todas las rutas relativas; el sitio funciona abierto local o desde GitHub Pages.

---

## 🗂️ Fuentes de contenido para Mate

Tres fuentes complementarias, cada una autoritativa para algo distinto:

### 1. Doc LaTeX en Google Drive — fuente de verdad para procedimiento y respuestas
- **ID Drive:** `1hTzKA2zC98FwfSiR9nR21gExC2hT4nrea-BANrbkd4I` (titulado "latex matematicas 1")
- Cada tema separado por `# N nombre` (ej. `# 5 expresiones algebraicas`)
- Contiene: ejemplos resueltos, ejercicios, resoluciones (a veces parciales), extras
- **Cuidado con duplicados:** ocasionalmente una sección tiene contenido copy/paste del tema previo (header dice X pero contenido es Y). Detectar comparando el título dentro de `\Huge \textbf{...}` con el header `# N nombre`. Si discrepa, **avisar a Lety y saltar el tema** hasta que ella lo arregle. Nunca inventar contenido para llenar el hueco.

### 2. Carpeta de capturas — referencia visual
- Ruta: `~/Desktop/capturas/matematicas N/M tema-nombre/`
- Contiene `.jpg` con ejercicios, ejemplos, respuestas y extras manuscritos por Lety
- Útiles para verificar que mi versión digital coincide con su intención
- Si el doc LaTeX y la captura difieren, prevalece el LaTeX (es la versión "limpia")

### 3. CSV de videos de YouTube
- Ruta: `~/Desktop/capturas/lista_videos_youtube.csv`
- Mapea slug del tema → ID del video de YouTube
- Si un tema no aparece en el CSV: **omitir la sección de Video** (no es error)
- Lety pasa cualquier video nuevo directo en chat. **No hacer fetch a `letymath.com`** (bloqueado por allowlist y desperdicia tokens).

---

## 🏗️ Arquitectura actual

```
lety2E 2/
├── index.html              [Portada: hero nocturno + 3 cards]
├── style.css               [Estilos únicos del sitio entero]
├── nav.js                  [Nav global, detecta sección y profundidad]
├── footer.js               [Footer global]
├── favicon.svg / .ico
├── CNAME                   [lety2e.com — NO borrar]
├── CLAUDE.md               [Este archivo]
├── INSTRUCCIONES.md        [Resumen corto de la arquitectura]
│
├── assets/img/, assets/logos/
│
├── lupian/                 [Sección artística]
│   ├── index.html          [2 puertas: Cantos · Relatos]
│   ├── cantos/index.html
│   └── relatos/index.html
│
├── apuntes/                [Grid de apunte-cards]
│   ├── index.html
│   └── *.html              [Cada apunte como artefacto self-contained]
│
└── math/                   [LetyMath]
    ├── index.html          [Grid de 6 course-cards]
    ├── matematicas-1/      [Mate 1 — en construcción activa]
    │   ├── index.html
    │   ├── operaciones-basicas.html  [Tema 1]
    │   ├── jerarquia.html             [Tema 2]
    │   ├── ecuaciones.html            [Tema 3]
    │   ├── monomios.html              [Tema 4]
    │   ├── expresiones-algebraicas.html [Tema 5]
    │   ├── grafica-tabulacion.html    [Tema 6 — con SVG]
    │   ├── pendiente-ordenada.html    [Tema 7 — con SVG]
    │   └── area-perimetro.html        [Tema 8 — con SVG triángulos]
    ├── matematicas-2/      [Solo placeholder]
    ├── matematicas-3/      [Solo placeholder]
    ├── matematicas-4/      [próximamente]
    ├── matematicas-5/      [Solo placeholder]
    └── optativa/           [Solo placeholder]
```

**Principio:** una sola fuente de verdad por archivo (style/nav/footer). Variaciones por `body[data-section]`.

---

## 🎨 Identidad visual

### Colores (variables en `style.css`)

```css
--M:  #FF00AA      /* Magenta primario — logo, hovers, accent fuerte */
--T:  #00DEC8      /* Turquesa — links, accent claro */
--P:  #4A0080      /* Morado — accent secundario */
--dark: #1A0828    /* Fondo nav/footer */
--bg:   #F2DBD5    /* Fondo body rosado */
--bg-card: #FBF2EF /* Fondo card */
--course-1: #4A0080 /* Alias de --P para encabezados Math */
--border: #E0C4BC  /* Borde de cards y grid de SVG */
```

**Regla:** NUNCA inventar colores fuera del palette. Excepción: los pills de fórmula (ver § Estilo de resoluciones).

### Tipografía
- **Display:** Playfair Display Italic 900 (títulos, "lety2E")
- **Body:** DM Sans 300/400/500
- Importadas vía Google Fonts.

---

## 🧭 Nav y footer (auto-detección)

`nav.js` y `footer.js` detectan profundidad contando `../` en su `src`:

| Profundidad | Ejemplo                         | Script              |
|-------------|---------------------------------|---------------------|
| 0           | `index.html` (raíz)             | `nav.js`            |
| 1           | `lupian/index.html`             | `../nav.js`         |
| 2           | `math/matematicas-1/x.html`     | `../../nav.js`      |

Si una sección tiene `links: []` y entras a una subpágina, el nav muestra `← Volver` automáticamente.

---

## 📦 Patrón "Paquetitos" para temas de Math

Tres variantes según la complejidad del tema:

### A. Paquetito clásico — para temas con sólo cálculos algebraicos
**Referencias canónicas:** `operaciones-basicas.html`, `jerarquia.html`, `ecuaciones.html`, `monomios.html`, `expresiones-algebraicas.html`

Orden de secciones:
1. **Video(s)** — opcional, 1-2 lado a lado en `.videos-row`
2. **Apuntes** — opcional, sólo si Lety provee texto en el doc o en chat
3. **Ejemplo(s)** — 1 a 5 según el tema, en `.ejemplo-block` con `.ejemplo-grid` (2 col)
4. **Ejercicios** — bloques en `.bloques-2` o `.bloques-3` siempre visibles
5. **Respuestas** — colapsables, formato según tema (línea simple o `\begin{aligned}`)
6. **Ejercicios extra** — colapsables, sin respuestas (igual que en el doc)
7. **Navegación prev/next**

### B. Paquetito con tabulación + gráfica — para `grafica-tabulacion.html`
- Layout especial `.tabulacion-block` (grid 2 col: info izq / gráfica der)
- Tabla X/Y + procedimiento al lado de la tabla
- SVG inline con la recta y los 5 puntos

### C. Paquetito con gráfica + comprobación — para `pendiente-ordenada.html` y `area-perimetro.html`
- Layout `.po-block` o `.tri-block` (grid 2 col: info / SVG)
- En pendiente-ordenada: comprobación de 3 puntos en `.comprobacion-grid` (3 col)
- En area-perimetro: lista de cálculos con `.formula-pill` y `.resultado-pill`

### Selección de grid según complejidad de los ejercicios

| Tipo de ejercicio                                      | Grid             |
|--------------------------------------------------------|------------------|
| Operaciones simples, 6×6 (operaciones-basicas)         | `.bloques-3`     |
| Ecuaciones, expresiones, monomios (4-5 por bloque)     | `.bloques-2`     |
| Ejercicios "pesados" o con paréntesis anidados         | `.bloques-2`     |
| Si dudas                                               | `.bloques-2`     |

---

## 🎨 Estilo de resoluciones (confirmado por Lety, mayo 2026)

Para temas con **fórmulas y cálculos paso a paso** (geometría, exponentes, mcm/MCD, etc.) Lety usa un estilo de cuaderno con highlighters:

### Notación
- Área: `a` (minúscula, no `A`)
- Lados/distancias en triángulos: `m`, `n` (no `l_1`, `l_2`)
- Distancia entre dos puntos: forma Pitagórica explícita `c = √(a² + b²)`
- Resultado final con `=` directo, no `≈`

### Pills coloridas para fórmulas y resultados

```css
.formula-pill {
  display: inline-block;
  background: #FFF1A8;          /* amarillo cremoso */
  border: 1.5px solid #F5DC6A;
  padding: .25rem .75rem;
  border-radius: 99px;
  font-weight: 600;
}
.formula-pill.salmon {
  background: #FFD9B8;          /* salmón */
  border-color: #F5B584;
}
.resultado-pill {
  display: inline-block;
  background: #FFD0E5;          /* rosa */
  color: var(--M);
  border: 1.5px solid #FF8AC0;
  padding: .15rem .65rem;
  border-radius: 99px;
  font-weight: 700;
}
```

| Color    | Uso                                                              |
|----------|------------------------------------------------------------------|
| Amarillo | Fórmulas conceptuales: `c = √(a²+b²)`, `P = b + m + n`           |
| Salmón   | Fórmulas de cálculo principal: `área = (b·h)/2`                  |
| Rosa     | Resultados finales: `12 u²`, `16.12 u`                           |

### Procedimiento conciso (no desde coordenadas)

❌ **Antes (verboso):**
```
m = √((3-(-1))² + (7-2)²) = √(4²+5²) = 6.40
```

✅ **Ahora (estilo Lety):**
```
m = √(4² + 5²) = √(16+25) = √41 = 6.40
```

Los catetos se identifican implícitamente del diagrama o por contexto.

---

## 📐 Gráficas SVG inline (rectas y triángulos)

Para temas que requieren gráficas, usar SVG inline (no TikZ, no librerías externas — file:// compatible).

### Regla principal: 1 cuadro = 1 unidad

Cada cuadrito del grid debe representar la misma unidad en X y en Y. Esto significa que el viewBox tiene proporciones distintas según el rango Y del problema.

```python
PX_PER_UNIT = 14   # mismo px en ambos ejes
PAD = 14
W = (x_max - x_min) * PX_PER_UNIT + 2*PAD
H = (y_max - y_min) * PX_PER_UNIT + 2*PAD
viewBox = f"0 0 {W} {H}"
```

### CSS para el SVG

```css
.grafica-svg {
  width: 100%;
  max-width: 240px;        /* limita ancho en columna */
  max-height: 380px;       /* evita que res4 se dispare */
  height: auto;
  display: block;
}
```

> ⚠️ Nunca usar `width: auto; height: auto` en SVG sin atributos width/height — colapsa a 0×0 en flex containers.

### Estilo visual de las gráficas

| Elemento     | Estilo                                                        |
|--------------|---------------------------------------------------------------|
| Grid         | Líneas `#E0C4BC` (rosa pálido) stroke 0.5, opacity 0.7        |
| Ejes         | Líneas `#7B5A50` (café) stroke 1.2                            |
| Recta        | `#FF00AA` (--M magenta) stroke 2.2                            |
| Triángulo    | Relleno `#FF00AA` 15% opacity + contorno magenta              |
| Puntos       | Círculo `#1A0828` r=3                                         |
| Labels       | DM Sans 7.5–9px, color `#1A0828` o `#7B5A50`                  |

### Helper Python para generar SVGs

Cuando se requieran muchas gráficas, escribir un script Python en `/tmp/gen_grafica.py` o `/tmp/gen_triangulo_svg.py` que reciba parámetros (m, b, vértices, rangos) y genere SVGs consistentes. Ver historial: `tema 6` y `tema 8`.

---

## 🚧 Cómo manejar contenido faltante o duplicado

| Caso                                                | Tratamiento                                                                          |
|-----------------------------------------------------|--------------------------------------------------------------------------------------|
| Curso de Math sin temas                             | `index.html` con `.proximamente-card`. Card en `math/index.html` lleva `.pronto` + `.pronto-badge` |
| Curso de Math con algunos temas                     | Index muestra solo los temas reales + `.proximamente-nota` al final                  |
| Tema con header pero contenido duplicado en doc     | **Saltar** y avisar a Lety. Reincorporar cuando ella corrija el doc                  |
| Tema sin video en CSV                               | Omitir sección de Video, no es error                                                 |
| Tema sin respuestas en doc                          | Sólo ejercicios + extras. Si las respuestas hay que calcularlas, hacerlo paso a paso |
| Card sin destino real                               | Borrarla. Nunca dejar `href="#"`                                                     |
| Respuesta en captura con error aritmético           | Publicar la correcta + flag corto al final del mensaje                               |

---

## 🚀 Flujos típicos

### Agregar un tema de Math (workflow completo)

1. **Verificar fuentes:**
   - Buscar el tema en el doc LaTeX (Drive ID al inicio)
   - Verificar que el header `# N nombre` y el `\textbf{...}` interno coincidan (si no, saltar)
   - Buscar slug en `lista_videos_youtube.csv` para el video
   - Revisar carpeta `capturas/matematicas N/M tema/` para referencia visual

2. **Generar gráficas si aplica:**
   - Escribir helper Python en `/tmp/gen_*.py`
   - Validar dimensiones del viewBox (1:1 en ambos ejes)
   - Generar SVGs en `/tmp/grafica_*.svg`

3. **Crear el `.html`:**
   - Slug en kebab-case sin tildes (`expresiones-algebraicas.html`, `pendiente-ordenada.html`)
   - Estructura paquetito según variante (A/B/C arriba)
   - KaTeX en `<head>` (template abajo)
   - SVGs embebidos inline (no link externo)
   - Estilo de resoluciones con pills si el tema usa fórmulas

4. **Actualizar navegación:**
   - Botón siguiente en el tema previo
   - Botón anterior en este tema
   - Si el tema próximo aún no existe, dejar el link al slug previsto (se romperá hasta que se cree, pero el patrón se mantiene)

5. **Agregar card al index del curso:**
   - `math/matematicas-N/index.html`
   - Color rotando entre `--M`, `--T`, `--P` (o `#4A0080`, `#00DEC8`, `#FF00AA`)
   - Ícono emoji simple (🔢 ⚖️ ✖️ 🧮 📈 📐 📏 etc.)

6. **Avisar a Lety con git block listo para pegar:**
   ```bash
   cd ~/Desktop/lety2E\ 2/
   git add math/matematicas-N/
   git commit -m "Tema N Mate K: descripción corta"
   git push
   ```

### KaTeX en el `<head>` de cada tema

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, { delimiters: [
    {left:'$$', right:'$$', display:true},
    {left:'$', right:'$', display:false}
  ]});"></script>
```

Inline: `$x^2 + y^2 = z^2$` · Display: `$$\frac{-b \pm \sqrt{b^2-4ac}}{2a}$$`

### Reglas de redacción para respuestas

- ❌ NUNCA flechas `→`
- ❌ NUNCA etiquetas tipo "Pos:", "Neg:"
- ❌ NUNCA explicaciones tipo libro de texto
- ✅ Formato simple: `= operación = **resultado**`
- ✅ Multi-paso: `\begin{aligned}` con `\\` entre líneas
- ✅ Potencias siempre en 3 pasos: `(−4)³ = (−4)(−4)(−4) = 16(−4) = −64`
- ✅ Resultado final en `\mathbf{...}` o `<strong>` color `--M`
- ✅ Reducción polinomios: orden por grado descendente ($x^2$, luego $x$, luego constantes)

---

## 🚢 Deploy a GitHub Pages

```bash
cd ~/Desktop/lety2E\ 2/
git status                       # ver qué cambió
git add .
git commit -m "mensaje claro"
git push                         # GitHub Pages rebuilea en 1-2 min
```

### Verificación post-push
1. Esperar 1-2 min.
2. Abrir `lety2e.com` en **ventana de incógnito** (evita caché).
3. Si el favicon no aparece, probar `lety2e.com/favicon.svg?v=2`.

### Issues conocidos
- **VS Code "Unable to create HEAD.lock"** → `rm -f .git/HEAD.lock` y reintentar.
- **"This repository moved"** → `git remote set-url origin https://github.com/letymath/lety2E.git`.
- **DNS falla intermitente** → toggle wifi/VPN, reintentar.

---

## 🎯 Preferencias confirmadas

| Aspecto                | Preferencia                                                                    |
|------------------------|--------------------------------------------------------------------------------|
| Colores                | Solo de variables (`--M`, `--T`, `--P`, etc.) salvo pills de fórmula           |
| Tipografía             | Playfair Display Italic 900 + DM Sans                                          |
| Tono                   | Minimalista, sin explicaciones de más                                          |
| Notación área          | `a` (minúscula)                                                                |
| Lados de triángulo     | `m`, `n` (no $l_1$, $l_2$)                                                     |
| Fórmula distancia      | `c = √(a² + b²)` con texto "distancia entre dos puntos"                        |
| Procedimiento          | Desde catetos, no desde coordenadas                                             |
| Respuestas algebraicas | `= paso = **resultado**` o `\begin{aligned}` para multi-paso                   |
| Potencias              | Expandidas en 3 pasos                                                          |
| Gráficas               | SVG inline, 1 cuadro = 1 unidad, magenta para curva                            |
| Triángulos             | Relleno magenta 15% opacity + contorno sólido                                  |
| Contenido vacío        | `próximamente` (nunca inventar)                                                |
| Errores en captura     | Publicar versión correcta + flag al final                                      |
| Tema duplicado en doc  | Saltar y avisar; reincorporar cuando Lety actualice                            |
| Doc fuente             | Drive `1hTzKA2zC98FwfSiR9nR21gExC2hT4nrea-BANrbkd4I`                           |
| Videos                 | CSV en `~/Desktop/capturas/lista_videos_youtube.csv` (no fetch a letymath.com) |

---

## 📂 Archivos críticos

| Archivo                    | Propósito                                       |
|----------------------------|-------------------------------------------------|
| `CLAUDE.md`                | Esta guía                                        |
| `INSTRUCCIONES.md`         | Resumen corto de arquitectura                   |
| `style.css`                | Estilos únicos del sitio                         |
| `nav.js`                   | Navegación auto-detect                          |
| `footer.js`                | Footer auto-detect                              |
| `CNAME`                    | Liga lety2e.com (NO borrar)                      |
| `favicon.svg` / `.ico`     | Ícono del sitio                                  |

---

*Guía mantenida por Claude · sincronizada con el estado actual del repo*
