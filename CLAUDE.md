# lety2e.com — Guía de Desarrollo

**Última actualización:** Abril 2026
**Proyecto:** lety2e.com — Sitio personal de Lety con Math, Lupián y Apuntes
**Stack:** HTML5 + CSS3 + Vanilla JS · GitHub Pages · file:// compatible
**Repo:** `github.com/letymath/lety2E` (branch `main`)
**Dominio:** `lety2e.com` (CNAME → GitHub Pages)
**Carpeta local:** `~/Desktop/lety2E 2/` ← esta es la clonada al repo

---

## 📋 Filosofía

- **Minimalista** — "paquetitos" en vez de muros de texto.
- **Mantenible** — un único `style.css`, `nav.js`, `footer.js`. Variantes con `body[data-section]`.
- **Real first** — nunca inventar contenido para llenar. Lo que no existe se marca como `próximamente`.
- **Orgánica** — Apuntes y Relatos crecen como listas planas; sólo se subdividen cuando un tipo se acumula.
- **File:// compatible** — todas las rutas relativas; el sitio funciona abierto local o desde GitHub Pages.

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
├── assets/
│   ├── img/                [hero-nocturno.png/.webp y otras]
│   └── logos/              [íconos 2E]
│
├── lupian/                 [Sección artística]
│   ├── index.html          [2 puertas grandes: Cantos · Relatos]
│   ├── assets/             [lety-cantos.jpeg, lety-relatos.jpeg]
│   ├── cantos/
│   │   └── index.html      [3 covers de YouTube + link al canal @Lety2eLupian]
│   └── relatos/
│       └── index.html      [Lista plana orgánica: escritos, audio, imagen, video]
│
├── apuntes/                [Sección de notas]
│   └── index.html          [Grid de apunte-cards con hover hint]
│       + mcp.html          [Artefacto self-contained]
│       + compresion.html   [Artefacto self-contained]
│       (cada apunte nuevo se agrega como un .html aquí + una card al grid)
│
└── math/                   [LetyMath]
    ├── index.html          [Grid de 6 course-cards, los vacíos con badge "próximamente"]
    ├── matematicas-1/
    │   ├── index.html      [Grid de temas reales]
    │   ├── operaciones-basicas.html  ← REFERENCIA CANÓNICA paquetito
    │   └── jerarquia.html
    ├── matematicas-2/      [Solo index con placeholder "próximamente"]
    ├── matematicas-3/      [Solo index con placeholder "próximamente"]
    ├── matematicas-4/
    │   ├── index.html
    │   ├── evaluacion-de-funciones.html
    │   ├── representacion-de-funciones.html
    │   └── funcion-escalonada.html
    ├── matematicas-5/      [Solo index con placeholder "próximamente"]
    └── optativa/           [Solo index con placeholder "próximamente"]
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
--bg-card: #FBF2EF /* Fondo card (blanco en apuntes/relatos) */
--course-1: #4A0080 /* Alias de --P para encabezados Math */
```

**Regla:** NUNCA inventar colores. Siempre variables.

### Tipografía
- **Display:** Playfair Display Italic 900 (títulos, "lety2E")
- **Body:** DM Sans 300/400/500 (texto)
- Importadas vía Google Fonts.

---

## 🧭 Nav y footer (auto-detección)

`nav.js` y `footer.js` detectan profundidad contando `../` en su `src`:

| Profundidad | Ejemplo                  | Script          |
|-------------|--------------------------|-----------------|
| 0           | `index.html` (raíz)      | `nav.js`        |
| 1           | `lupian/index.html`      | `../nav.js`     |
| 2           | `math/matematicas-1/x.html` | `../../nav.js`  |

### `SECTIONS` actual en `nav.js`

```javascript
const SECTIONS = {
  lupian: {
    name: 'lety2E Lupián',
    links: [
      { text: 'Cantos',  href: 'cantos/index.html' },
      { text: 'Relatos', href: 'relatos/index.html' }
    ]
  },
  apuntes: {
    name: 'lety2E Apuntes',
    links: []                  // lista plana, sin subsecciones
  },
  math: {
    name: 'lety2E Math',
    links: [
      { text: 'Mat 1',    href: 'matematicas-1/index.html' },
      { text: 'Mat 2',    href: 'matematicas-2/index.html' },
      { text: 'Mat 3',    href: 'matematicas-3/index.html' },
      { text: 'Mat 4',    href: 'matematicas-4/index.html' },
      { text: 'Mat 5',    href: 'matematicas-5/index.html' },
      { text: 'Optativa', href: 'optativa/index.html' }
    ]
  }
};

const ROOT_LINKS = [
  { text: 'Math',    href: 'math/index.html' },
  { text: 'Lupián',  href: 'lupian/index.html' },
  { text: 'Apuntes', href: 'apuntes/index.html' }
];
```

Si una sección tiene `links: []` y entras a una subpágina (no el index), el nav muestra `← Volver` automáticamente.

---

## 🧩 Patrones visuales reutilizables

### `.root-card` — cards de la portada principal
Las 3 grandes (Math · Lupián · Apuntes) en `index.html`.

### `.puerta-card` — Lupián index
2 puertas con foto. Imagen + label, hover suave. Usa `assets/lety-cantos.jpeg` y `assets/lety-relatos.jpeg`. Tiene `onerror` con placeholder por si la imagen no carga.

### `.apunte-card` — grid de Apuntes
Card con `<span class="apunte-tipo">artefacto|infografía|texto</span>`, `<h3>` y `<p class="apunte-hint">` que se intensifica al hover. Color por `style="--card-accent: var(--M|T|P);"`.

### `.lista-organica` + `.entrada-item` — Relatos
Lista plana, sin grid rígido. Cada entrada es `<a class="entrada-item" style="--entry-accent: var(--M);">` con `<h3>` y `<p class="entrada-hint">` opcional. Cuando un tipo crece (≥8), se puede mover a una subcarpeta.

### `.course-card` + `.pronto` — Math portada
Cards normales para cursos con contenido. Cursos vacíos llevan también la clase `.pronto` y un `<span class="pronto-badge">próximamente</span>` arriba a la derecha.

### `.proximamente-card` — index de curso/sección vacía
Card centrada con tag, h2 y descripción corta. Usa `style="--card-accent: var(--M|T|P|...);"`.

### `.proximamente-nota`
Texto pequeño centrado al final de un índice parcialmente lleno (ej: "Más temas en construcción.").

---

## 📦 Patrón "Paquetitos" para temas de Math

Referencia canónica: `math/matematicas-1/operaciones-basicas.html`

### Orden de secciones de un paquetito

1. **Videos** — 1-2 videos lado a lado en `.videos-row`
2. **Apuntes intro** — párrafos cortos + reglas en `.mini-card`
3. **Ejemplo** — 1 bloque destacado, siempre visible
4. **Ejercicios** — 6 ejercicios en `.bloques-3` (grid 3 col), siempre visibles
5. **Respuestas** — colapsables (`.sec-toggle` + `.toggled-content`)
6. **Ejercicios extra** — colapsables, borde dashed
7. **Navegación prev/next** entre temas

### Reglas de redacción

- ❌ NUNCA flechas `→` en respuestas
- ❌ NUNCA etiquetas tipo "Pos:", "Neg:"
- ❌ NUNCA explicaciones tipo libro de texto
- ✅ Formato de respuesta: `= operación = **resultado**`
- ✅ Potencias siempre expandidas en 3 pasos: `(−4)³ = (−4)(−4)(−4) = 16(−4) = −64`
- ✅ Directas al procedimiento

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

---

## 🚧 Cómo manejar contenido faltante

**Regla de oro:** nunca inventar temas, descripciones o ejercicios para llenar el sitio. Si algo no existe, se marca como en construcción.

| Caso                                    | Tratamiento                                                                 |
|-----------------------------------------|------------------------------------------------------------------------------|
| Curso de Math sin temas                 | Su `index.html` muestra `.proximamente-card`. La card en `math/index.html` lleva `.pronto` + `.pronto-badge`. |
| Curso de Math con algunos temas         | Index muestra solo los temas reales + `.proximamente-nota` al final.        |
| Sección con grid vacío (relatos, etc.)  | Comentarios HTML con ejemplos + `.lista-vacia` con texto "Pronto…".         |
| Card sin destino real                   | Borrarla. Nunca dejar `href="#"`.                                            |

---

## 🚀 Flujos típicos

### Agregar un apunte nuevo
1. Pegar el `.html` self-contained en `apuntes/`.
2. Añadir un `<a class="apunte-card">` al grid de `apuntes/index.html` con tipo, título y hint.
3. Color del borde con `--card-accent` (rotar entre `--M`, `--T`, `--P`).

### Agregar un relato nuevo
1. Pegar el archivo (html, mp3, mp4, imagen) en `lupian/relatos/`.
2. Descomentar/añadir un `<a class="entrada-item">` a `.lista-organica` en el index.
3. Si un tipo se acumula (≥8), crear subcarpeta y mover los archivos.

### Agregar un cover a Cantos
1. Tomar el ID del video de YouTube (lo que va después de `youtu.be/`).
2. Añadir un `<article class="video-cover">` con su iframe en `lupian/cantos/index.html`.

### Agregar un tema a Math
1. Copiar `math/TEMPLATE-TOPICO.html` → `tema-nuevo.html`.
2. Editar título, videos, fórmulas, ejercicios.
3. Añadir card al `index.html` del curso.
4. Si era el primer tema del curso, quitar el `.proximamente-card` y la `.pronto` de la portada.

### Agregar una nueva sección al sitio
1. Crear carpeta + `index.html` con `body data-section="nueva"`.
2. Añadir entrada en `SECTIONS` y/o `ROOT_LINKS` de `nav.js`.
3. Añadir card en `index.html` raíz si va a la portada.
4. (Opcional) Override de variables CSS en `style.css`.

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
| `math/TEMPLATE-TOPICO.html`| Template para nuevos temas de Math              |

---

## 🎯 Preferencias confirmadas

| Aspecto         | Preferencia                                                           |
|-----------------|------------------------------------------------------------------------|
| Colores         | Solo de variables (`--M`, `--T`, `--P`, etc.)                          |
| Tipografía      | Playfair Display Italic 900 + DM Sans                                  |
| Tono            | Minimalista, sin explicaciones de más                                  |
| Ejercicios Math | Grid 3 col, 6 visibles + 6 colapsables                                 |
| Respuestas      | `= paso = **resultado**`, NUNCA flechas                                |
| Potencias       | Expandidas en 3 pasos                                                  |
| Contenido vacío | `próximamente` (nunca inventar)                                        |
| Cantos          | 3 covers curados + link al canal `@Lety2eLupian`                       |
| Relatos         | Lista plana orgánica, crece a su ritmo                                 |
| Apuntes         | Grid de cards con hover hint, sin subcarpetas hasta que sea necesario  |

---

*Guía mantenida por Claude · sincronizada con el estado actual del repo*
