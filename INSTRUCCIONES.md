# lety2E — Instrucciones del proyecto

> Sitio web personal de Lety. Proyecto en crecimiento constante:
> se irán agregando nuevos relatos, apuntes y temas de Math.

---

## Identidad de marca

| Color     | Hex       | Uso                                       |
|-----------|-----------|-------------------------------------------|
| Magenta   | `#FF00AA` | Logo "lety2E", texto marca, hovers        |
| Turquesa  | `#00DEC8` | Links nav, accent claro                   |
| Morado    | `#4A0080` | Badges subsección, accent por defecto     |
| Dark      | `#1A0828` | Fondo nav/footer                          |
| Bg body   | `#FBF2EF` | Fondo general (rosado muy claro)          |
| Bg card   | `#FFFFFF` | Fondo de cards (blanco puro)              |
| Texto     | `#3D2525` | Texto principal                           |
| Texto 2   | `#6E4F4F` | Texto secundario                          |
| Border    | `#E0C4BC` | Bordes de cards                           |

**Sistema de secciones:** las secciones artísticas (Home, Lupián) usan magenta como color principal y turquesa en hovers; las académicas (Math, Apuntes) invierten: turquesa principal, magenta en hovers. En **Apuntes**, el título del tema en el cuerpo usa morado (`--P`).

**Tipografía:**
- Display/Logo: Playfair Display Italic 900 (Google Fonts)
- Cuerpo: DM Sans 300/400/500 (Google Fonts)

**Logos:** en `assets/logos/`
- `icono-2e.png` — ícono base
- `lety2E-madre-v3.png` — wordmark principal
- `lety2e-Math-v3.png` / `lety2e-Lupian-v3.png` / `lety2e-Apuntes.jpeg` — brandings por sección

> Nota: El nav y footer usan un SVG inline con el badge "2E" (generado por `nav.js` y `footer.js`), ya no las imágenes PNG.

---

## Arquitectura actual

```
lety2E 2/
├── index.html              ← Portada (hero nocturno + 3 cards: Math · Lupián · Apuntes)
├── style.css               ← UN solo CSS para todo el sitio
├── nav.js                  ← UN solo nav inteligente
├── footer.js               ← UN solo footer inteligente
├── assets/
│   ├── logos/              ← Iconos y wordmarks
│   └── img/                ← hero-nocturno.png/.webp y otras
│
├── lupian/                 ← Faceta artística
│   ├── index.html          ← 2 puertas grandes
│   ├── assets/             ← lety-cantos.jpeg, lety-relatos.jpeg
│   ├── cantos/             ← 3 covers + link al canal @Lety2eLupian
│   └── relatos/            ← 4 relatos (lista plana, crece orgánicamente)
│
├── apuntes/                ← Notas (self-contained, no usan nav.js/footer.js)
│   ├── index.html          ← Grid de apunte-cards con hover hint
│   ├── Templete-apuntes.md ← Guía para crear apuntes nuevos
│   ├── mcp.html            ← Artefacto self-contained
│   ├── compresion.html     ← Artefacto self-contained
│   └── segunda-guerra-mundial.html ← Referencia canónica del template
│
└── math/                   ← lety2E Math
    ├── index.html          ← 6 cards (Mat 1-5 + Optativa); vacíos llevan badge "próximamente"
    ├── matematicas-1/      ← 8 temas (operaciones → área y perímetro) — en crecimiento
    ├── matematicas-2/      ← placeholder próximamente
    ├── matematicas-3/      ← placeholder próximamente
    ├── matematicas-4/      ← placeholder próximamente
    ├── matematicas-5/      ← placeholder próximamente
    └── optativa/           ← placeholder próximamente
```

---

## Cómo funciona la arquitectura

### CSS unificado (`style.css`)
- Un solo archivo en la raíz con TODOS los estilos.
- Variables CSS controlan colores, tipografía y layout.
- `body[data-section="apuntes"]` y `body[data-section="relatos"]` → cards blancas.
- `body[data-section="home"]` → main centrado.
- Patrones reutilizables: `.root-card`, `.puerta-card`, `.apunte-card`, `.entrada-item`,
  `.course-card.pronto`, `.proximamente-card`, `.proximamente-nota`.

### Nav inteligente (`nav.js`)
- Detecta profundidad automáticamente contando `../` en su `src`.
- Detecta sección actual por la URL.
- **Raíz (depth 0):** "lety2E" + 3 links principales (Math, Lupián, Apuntes).
- **Sección (depth 1):** nombre de sección + sublinks.
- **Subsección (depth 2+):** nombre de sección + "← Volver".

### Footer inteligente (`footer.js`)
- Mismo mecanismo de detección.

---

## Cómo agregar contenido

1. Los apuntes son **self-contained**: todo su CSS y JS va inline dentro del `.html` (no usan `style.css`, `nav.js` ni `footer.js`).
2. Tienen un **Header minimalista** con logo, nombre de sección y un **selector de nivel (dropdown)**.
3. El **Título del tema** va en el cuerpo del apunte, centrado y en color morado (`--P`).
4. Usar `apuntes/Templete-apuntes.md` como guía y `segunda-guerra-mundial.html` como referencia canónica.
5. Pegar el `.html` en `apuntes/`.
6. Añadir un `<a class="apunte-card">` al grid en `apuntes/index.html`.

### Nuevo relato
1. Pegar el archivo en `lupian/relatos/` (puede ser .html, .mp3, .mp4, imagen).
2. Añadir un `<a class="entrada-item">` a `.lista-organica` en el index.

### Nuevo cover de cantos
1. Tomar el ID del video de YouTube.
2. Añadir un `<article class="video-cover">` con su iframe en `lupian/cantos/index.html`.

### Nuevo tema de Math
1. Usar como referencia un tema existente de `math/matematicas-1/` (ej. `operaciones-basicas.html`) — el patrón "paquetito" documentado en `CLAUDE.md`.
2. Editar título, videos, fórmulas, ejercicios.
3. Añadir card al `index.html` del curso.
4. Si era el primer tema del curso, quitar el `.proximamente-card` del index del curso y la `.pronto` de la portada de Math.

> ⚠️ `math/TEMPLATE-TOPICO.html` está **obsoleto** — no refleja el formato "paquetito" actual. Usar temas reales como referencia.

### Nueva sección al sitio
1. Crear carpeta + `index.html` con `body data-section="nueva"`.
2. Añadir entrada en `SECTIONS` y/o `ROOT_LINKS` de `nav.js`.
3. Añadir card en `index.html` raíz.
4. (Opcional) Override de variables CSS.

---

## Regla de oro: contenido faltante

**Nunca inventar.** Lo que no existe se marca como `próximamente`:

- Curso vacío de Math → `.proximamente-card` en su index + `.pronto` + `.pronto-badge` en la portada.
- Curso parcial → solo temas reales + `.proximamente-nota` al final.
- Sección con grid vacío → `.lista-vacia` con texto "Pronto…".
- Card sin destino real → borrarla. Nunca dejar `href="#"`.

---

## Convenciones de rutas

Todas relativas para compatibilidad con `file://`:

| Desde            | CSS               | nav.js            | footer.js          |
|------------------|-------------------|-------------------|--------------------|
| Raíz             | `style.css`       | `nav.js`          | `footer.js`        |
| Sección (depth 1)| `../style.css`    | `../nav.js`       | `../footer.js`     |
| Subsección (d 2) | `../../style.css` | `../../nav.js`    | `../../footer.js`  |

---

## Datos técnicos

- **Hosting:** GitHub Pages (migrado desde Hostinger en abril 2026)
- **Repo:** `github.com/letymath/lety2E`, branch `main`
- **Carpeta local:** `~/Desktop/lety2E 2/`
- **Dominio:** lety2e.com (ligado vía `CNAME`)
- **Tecnología:** HTML puro + CSS + JS vanilla (sin frameworks)
- **Fuentes:** Google Fonts (Playfair Display + DM Sans)
- **KaTeX:** Usado en páginas de LetyMath para fórmulas matemáticas
- **Cantos:** Videos embebidos + link al canal externo `@Lety2eLupian`
- **Deploy:** `git add . && git commit -m "…" && git push` → publica automático en ~1-2 min

---

## Issues conocidos del deploy

- VS Code "Unable to create HEAD.lock" → `rm -f .git/HEAD.lock` y reintentar.
- "This repository moved" → `git remote set-url origin https://github.com/letymath/lety2E.git`.
- DNS intermitente → toggle wifi/VPN.
- Caché de favicon → abrir en incógnito o `?v=2`.

---

## Pendientes / planeado

- Mat 1: en crecimiento activo — se siguen agregando temas.
- Llenar Mat 2, 3, 5 y Optativa con temas reales cuando estén listos.
- Mat 5: descripción pendiente de definir por Lety (actualmente tiene texto genérico).
- Posibles secciones futuras: Alojamiento (renta vacacional), etc.

---

*Última actualización: Mayo 2026*
