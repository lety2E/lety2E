# lety2E — Instrucciones del proyecto

> Sitio web personal de Lety. Proyecto en crecimiento constante:
> se irán agregando nuevas secciones (ej. Alojamiento, etc.).

---

## Identidad de marca

| Color     | Hex       | Uso                                   |
|-----------|-----------|---------------------------------------|
| Magenta   | `#FF00AA` | Logo "lety2E", texto marca, hovers    |
| Turquesa  | `#00DEC8` | Links nav, derechos, acento claro     |
| Morado    | `#4A0080` | Badges subsección, accent por defecto |
| Dark      | `#1A0828` | Fondo nav/footer                      |
| Bg body   | `#F2DBD5` | Fondo general rosado                  |
| Bg card   | `#FBF2EF` | Fondo de cards (blanco en apuntes/escritos) |

**Tipografía:**
- Display/Logo: Playfair Display Italic 900 (Google Fonts)
- Cuerpo: DM Sans 300/400/500 (Google Fonts)

**Logos:** en `assets/logos/`
- `icono-2e-magenta.png` — usado en nav y footer
- `icono-2e-morado.png`
- `wordmark-lety2e-claro.png` / `wordmark-lety2e-oscuro.png`

---

## Arquitectura (optimizada)

```
lety2E/
├── index.html              ← Portada (hero + bio + botones)
├── style.css               ← UN solo CSS para todo el sitio
├── nav.js                  ← UN solo nav inteligente (detecta sección y nivel)
├── footer.js               ← UN solo footer inteligente (detecta nivel)
├── assets/
│   ├── logos/              ← Iconos y wordmarks
│   └── img/               ← Imágenes del sitio
├── escritos/               ← Sección: Escritos
│   ├── index.html          ← Índice (4 categorías)
│   ├── historias/index.html
│   ├── poemas/index.html
│   ├── reflexiones/index.html
│   └── varios/index.html
├── apuntes/                ← Sección: Apuntes
│   ├── index.html          ← Índice (6 tópicos)
│   ├── historia-mexico/index.html
│   ├── fisica/index.html
│   ├── ia/index.html
│   ├── cosmetica-natural/index.html
│   ├── eneagrama/index.html
│   └── bolsa-valores/index.html
└── math/                  ← Sección: lety2E Math
    ├── index.html          ← Índice (5 cursos + optativa)
    ├── matematicas-1/      ← Cada curso tiene index.html + páginas de tema
    ├── matematicas-2/
    ├── matematicas-3/
    ├── matematicas-4/
    └── matematicas-5/
```

---

## Cómo funciona la arquitectura

### CSS unificado (`style.css`)
- Un solo archivo en la raíz con TODOS los estilos
- Variables CSS controlan colores, tipografía y layout
- `body[data-section="apuntes"]` y `body[data-section="escritos"]` → cards blancas
- `body[data-section="home"]` → main más estrecho (820px)
- Incluye: grids de sección (topic-grid, category-grid, course-grid), cards, nav, footer, portada

### Nav inteligente (`nav.js`)
- Detecta profundidad automáticamente contando `../` en su propia ruta src
- Detecta sección actual por la URL del navegador
- **Raíz (depth 0):** Muestra "lety2E" + links principales (Escritos, Apuntes, lety2E Math, lety2E Lupian)
- **Sección (depth 1):** Muestra nombre de sección + links a subsecciones
- **Subsección (depth 2+):** Muestra nombre de sección + "← Volver"

### Footer inteligente (`footer.js`)
- Mismo mecanismo de detección de profundidad
- Ajusta rutas de iconos y link a inicio automáticamente

---

## Cómo agregar una nueva sección

1. **Crear carpeta:** `nueva-seccion/index.html`

2. **En el HTML:**
   ```html
   <link rel="stylesheet" href="../style.css">
   <body data-section="nueva-seccion">
   <script src="../nav.js"></script>
   <!-- contenido -->
   <script src="../footer.js"></script>
   ```

3. **En `nav.js`** — agregar entrada en `SECTIONS`:
   ```js
   'nueva-seccion': {
     name: 'Mi Sección',
     links: [
       { text: 'Sub 1', href: 'sub1/index.html' },
       { text: 'Sub 2', href: 'sub2/index.html' }
     ]
   }
   ```

4. **En `nav.js`** — agregar link en `ROOT_LINKS`:
   ```js
   { text: 'Mi Sección', href: 'nueva-seccion/index.html' }
   ```

5. **En `style.css`** — si necesita override de colores:
   ```css
   body[data-section="nueva-seccion"] {
     --bg-card: #FFFFFF;
   }
   ```

6. **En `index.html` (portada)** — agregar botón correspondiente

---

## Convenciones de rutas

Todas las URLs son **relativas** para compatibilidad con `file://`:

| Desde            | CSS               | nav.js             | footer.js           |
|------------------|-------------------|---------------------|---------------------|
| Raíz             | `style.css`       | `nav.js`            | `footer.js`         |
| Sección (depth 1)| `../style.css`    | `../nav.js`         | `../footer.js`      |
| Subsección (d 2) | `../../style.css` | `../../nav.js`      | `../../footer.js`   |

---

## Datos técnicos

- **Hosting:** GitHub Pages (migrado desde Hostinger en abril 2026)
- **Repo:** `github.com/letymath/lety2E`, branch `main`
- **Carpeta local:** `~/Desktop/lety2E 2/` (la que está clonada al repo)
- **Dominio:** lety2e.com (ligado vía `CNAME`)
- **Tecnología:** HTML puro + CSS + JS vanilla (sin frameworks)
- **Fuentes:** Google Fonts (Playfair Display + DM Sans)
- **KaTeX:** Usado en páginas de LetyMath para fórmulas matemáticas
- **lety2E Lupian:** Link externo a YouTube (@Lety2eLupian)
- **Deploy:** `git add . && git commit -m "…" && git push` → publica automático en ~1-2 min

---

## Secciones futuras planeadas

- Alojamiento (renta vacacional)
- Más temas y categorías dentro de las secciones existentes

---

*Última actualización: Abril 2026*
