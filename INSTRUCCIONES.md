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
| Bg body   | `#F2DBD5` | Fondo general rosado                      |
| Bg card   | `#FBF2EF` | Fondo de cards (blanco en apuntes/relatos)|

**Tipografía:**
- Display/Logo: Playfair Display Italic 900 (Google Fonts)
- Cuerpo: DM Sans 300/400/500 (Google Fonts)

**Logos:** en `assets/logos/`
- `icono-2e-magenta.png` — usado en nav
- `icono-2e-morado.png`
- `wordmark-lety2e-claro.png` / `wordmark-lety2e-oscuro.png`

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
│   └── relatos/            ← Escritos, audio, imagen, video (lista plana)
│
├── apuntes/                ← Notas
│   ├── index.html          ← Grid de apunte-cards con hover hint
│   ├── mcp.html            ← Artefacto self-contained
│   └── compresion.html     ← Artefacto self-contained
│
└── math/                   ← lety2E Math
    ├── index.html          ← 6 cards (Mat 1-5 + Optativa); vacíos llevan badge "próximamente"
    ├── matematicas-1/      ← operaciones-basicas + jerarquia
    ├── matematicas-2/      ← placeholder próximamente
    ├── matematicas-3/      ← placeholder próximamente
    ├── matematicas-4/      ← evaluacion + representacion + función escalonada
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

### Nuevo apunte
1. Pegar el `.html` self-contained en `apuntes/`.
2. Añadir un `<a class="apunte-card">` al grid en `apuntes/index.html` con tipo (artefacto / infografía / texto), título y hint.

### Nuevo relato
1. Pegar el archivo en `lupian/relatos/` (puede ser .html, .mp3, .mp4, imagen).
2. Añadir un `<a class="entrada-item">` a `.lista-organica` en el index.

### Nuevo cover de cantos
1. Tomar el ID del video de YouTube.
2. Añadir un `<article class="video-cover">` con su iframe en `lupian/cantos/index.html`.

### Nuevo tema de Math
1. Copiar `math/TEMPLATE-TOPICO.html` → `tema-nuevo.html` en la carpeta del curso.
2. Editar título, videos, fórmulas, ejercicios.
3. Añadir card al `index.html` del curso.
4. Si era el primer tema del curso, quitar el `.proximamente-card` del index del curso y la `.pronto` de la portada de Math.

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

- Llenar Mat 2, 3, 5 y Optativa con temas reales (cuando estén, **revisar las descripciones** de cada curso porque las actuales son del sitio viejo y no coinciden — ej: Mat 5 es derivadas/integrales, no álgebra lineal).
- Posibles secciones futuras: Alojamiento (renta vacacional), etc.

---

*Última actualización: Abril 2026 (post-restructura Lupián/Relatos/Math)*
