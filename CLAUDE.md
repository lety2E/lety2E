# lety2e.com — Guía de Desarrollo Optimizada

**Última actualización:** Abril 2026 (post-migración a GitHub Pages)  
**Proyecto:** lety2e.com — Sitio personal con Escritos, Apuntes, LetyMath y Cantos  
**Stack:** HTML5 + CSS3 + Vanilla JS | GitHub Pages | file:// compatible  
**Repo:** `github.com/letymath/lety2E` (branch `main`)  
**Dominio:** `lety2e.com` (CNAME → GitHub Pages)  
**Carpeta local de trabajo:** `~/Desktop/lety2E 2/` ← esta es la que está clonada al repo

---

## 📋 Resumen Ejecutivo

Este documento define la arquitectura consolidada del proyecto lety2e.com y establece patrones claros para agregar contenido, secciones y funcionalidades. **Todas las decisiones aquí tomadas se basan en preferencias de la usuaria y en la metodología de "paquetitos" probada en LetyMath.**

---

## 🏗️ Arquitectura del Proyecto

### Estructura Consolidada (Sin Duplicados)

```
Lety2E/
├── index.html              [Portada principal]
├── style.css               [Estilos únicos del sitio entero]
├── nav.js                  [Navegación global]
├── footer.js               [Pie de página global]
├── CLAUDE.md               [Este archivo]
│
├── escritos/
│   ├── index.html          [Índice de Escritos]
│   └── [categoria]/
│       ├── [titulo].html
│       └── ...
│
├── apuntes/
│   ├── index.html          [Índice de Apuntes]
│   └── [topico]/
│       └── [tema].html
│
├── math/
│   ├── index.html          [Índice de LetyMath]
│   └── matematicas-N/      [Cursos 1-5 + Optativa]
│       └── [tema].html
│
└── [PRÓXIMAS SECCIONES]    [Ej: alojamiento/, otros/]
    ├── index.html
    └── ...
```

**Principio clave:** Un único `style.css`, un único `nav.js`, un único `footer.js`. Variaciones visuales se logran con `body[data-section]` en CSS.

---

## 🎨 Paleta de Colores y Tipografía

### Colores (Variables CSS Globales)
```css
--M: #FF00AA              /* Magenta / Rosa primario */
--T: #00DEC8              /* Turquesa / Accent */
--P: #4A0080              /* Morado / Secundario */
--course-1: #4A0080       /* (Alias de --P) Para encabezados de LetyMath */
--dark: #1A0828           /* Fondo oscuro base */
--bg-card: [Card BG]       /* Fondo de tarjetas */
--border: [Border color]   /* Bordes sutiles */
--accent-light: [Light]    /* Acentos claros / Bordes dashed extras */
```

### Tipografía
- **Display:** Playfair Display (títulos, headings)
- **Body:** DM Sans (texto, párrafos)
- Importadas vía Google Fonts

**Regla:** NUNCA inventar colores. Siempre usar variables de `style.css`.

---

## 🧭 Detección Automática de Navegación

### nav.js y footer.js — Detección de Profundidad

Ambos scripts detectan **automáticamente** la profundidad del HTML mediante conteo de `../` en el atributo `src`:

```html
<!-- Profundidad 0 (raíz) -->
<script src="nav.js"></script>

<!-- Profundidad 1 (dentro de carpeta de sección) -->
<script src="../nav.js"></script>

<!-- Profundidad 2 (dentro de subcarpeta) -->
<script src="../../nav.js"></script>
```

### SECTIONS en nav.js

Toda nueva sección debe ser agregada a `SECTIONS` en `nav.js`:

```javascript
const SECTIONS = {
  escritos: { label: "Escritos", icon: "✍️" },
  apuntes: { label: "Apuntes", icon: "📚" },
  math: { label: "LetyMath", icon: "∑" },
  cantos: { label: "Cantos", icon: "🎵" },
  // Nueva sección aquí:
  // alojamiento: { label: "Alojamiento", icon: "🏠" },
};

const ROOT_LINKS = [
  // Links para la portada
  { href: "escritos/", label: "Escritos", icon: "✍️" },
  { href: "apuntes/", label: "Apuntes", icon: "📚" },
  { href: "math/", label: "LetyMath", icon: "∑" },
  { href: "https://www.youtube.com/@Lety2eLupian", label: "Cantos", icon: "🎵", external: true },
];
```

---

## 📝 Patrón "Paquetitos" para LetyMath

La metodología de "paquetitos" es el corazón de LetyMath. Los estudiantes reciben **paquetes compactos, minimalistas, sin explicaciones innecesarias**.

### Estructura Canónica (operaciones-basicas.html)

Toda página de tema debe seguir este orden:

1. **Videos** — 2 videos lado a lado (`.videos-row`)
2. **Apuntes Intro** — Párrafos cortos + reglas en cards
3. **Ejemplo** — 1 bloque centrado, siempre visible
4. **Ejercicios** — 6 ejercicios, siempre visibles
5. **Respuestas** — Colapsables (header `.sec-toggle`)
6. **Ejercicios Extra** — Colapsables, con borde dashed
7. **Navegación** — Links prev/next al tema anterior/siguiente

### Reglas Específicas del Patrón

#### Videos
```html
<div class="videos-row">
  <iframe src="https://www.youtube.com/embed/..." title="Video 1"></iframe>
  <iframe src="https://www.youtube.com/embed/..." title="Video 2"></iframe>
</div>
```
Grid de 2 columnas, lado a lado.

#### Apuntes / Reglas
```html
<div class="mini-card">
  <div class="card-header" style="color: var(--course-1);">Regla: Suma de Enteros</div>
  <p>+a +b = +(a+b)</p>
  <p>−a −b = −(a+b)</p>
</div>
```

#### Ejemplo (Centrado, Destacado)
```html
<div class="example-block" style="background: var(--bg-card); border: 1px solid var(--border);">
  <h3 style="color: var(--M); font-style: italic;">🎯 Ejemplo</h3>
  <p><strong>Resuelve:</strong> (−4)³ + (−2)²</p>
  <p>= (−4)(−4)(−4) + (−2)(−2)<br/>
     = 16(−4) + 4<br/>
     = −64 + 4<br/>
     = −60</p>
</div>
```

#### Ejercicios (Grid 3 Columnas, Siempre Visibles)
```html
<div class="section-block">
  <h3 class="sec-head" style="color: var(--course-1);">Ejercicios</h3>
  <div class="bloques-3">
    <div class="mini-card">
      <strong>1.</strong> (−5) + 3 = ?
    </div>
    <div class="mini-card">
      <strong>2.</strong> (−2) × (−8) = ?
    </div>
    <!-- ... 4 más, total 6 -->
  </div>
</div>
```

#### Respuestas (Colapsables)
```html
<div class="section-block">
  <h3 class="sec-toggle" onclick="toggleSection(this)">
    Respuestas ▼
  </h3>
  <div class="toggled-content" style="display: none;">
    <div class="bloques-3">
      <div class="mini-card">
        <strong>1.</strong> = −5 + 3 = **−2**
      </div>
      <!-- ... -->
    </div>
  </div>
</div>
```

#### Extras (Mismo patrón, pero borde dashed)
```html
<div class="section-block">
  <h3 class="sec-toggle" onclick="toggleSection(this)">
    Ejercicios Extra ▼
  </h3>
  <div class="toggled-content" style="display: none; border-left: 2px dashed var(--accent-light);">
    <div class="bloques-3">
      <!-- 6 ejercicios más -->
    </div>
  </div>
</div>
```

### Formato de Respuestas

**Formato obligatorio:**
```
= operación = **resultado**
```

❌ **NUNCA:**
- Flechas `→`
- Etiquetas "Pos:", "Neg:"
- Explicaciones tipo libro de texto

✅ **SIEMPRE:**
- Potencias expandidas en 3 pasos: `(−4)³ = (−4)(−4)(−4) = 16(−4) = −64`
- Directas al procedimiento

### Espaciado y Margins

```css
.section-block {
  margin-bottom: 2.5rem;  /* Entre secciones */
}

.bloques-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}
```

---

## 🔢 Matemáticas: KaTeX y Fórmulas

### Incrustar KaTeX

En el `<head>` de toda página de math:
```html
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/auto-render@0.16.0/dist/auto-render.min.js"></script>
```

### Uso de LaTeX Inline y Display

```html
<!-- Inline: $x^2 + y^2 = z^2$ -->
<p>La fórmula es $x^2 + y^2 = z^2$ en el Teorema de Pitágoras.</p>

<!-- Display: $$...$$ o \[...\] -->
<p>$$\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$</p>
```

KaTeX renderizará automáticamente.

---

## 🎁 Favicon: Logo 2E

### Crear favicon.svg

Crea un archivo **`favicon.svg`** en la raíz del proyecto (`Lety2E/`) con el siguiente contenido:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
  <!-- Fondo magenta/rosa (#FF00AA) -->
  <rect width="200" height="200" fill="#FF00AA"/>
  
  <!-- Texto "2E" en turquesa (#00DEC8) -->
  <text 
    x="100" 
    y="130" 
    font-family="Playfair Display, serif" 
    font-size="120" 
    font-weight="bold"
    text-anchor="middle" 
    fill="#00DEC8"
  >2E</text>
</svg>
```

### Linkarlo en el HTML

**En archivos de profundidad 0** (raíz - `index.html`):
```html
<link rel="icon" href="favicon.svg" type="image/svg+xml">
```

**En archivos de profundidad 1** (dentro de sección - `escritos/index.html`):
```html
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
```

**En archivos de profundidad 2** (dentro de subcarpeta - `math/matematicas-1/tema.html`):
```html
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
```

**Ubicación en el `<head>`:**
```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>lety2e.com</title>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">  <!-- Aquí -->
  <link rel="stylesheet" href="style.css">
  <!-- más contenido... -->
</head>
```

**Ventajas del SVG:**
- ✅ Escalable en cualquier tamaño
- ✅ Súper ligero
- ✅ Compatible con navegadores modernos
- ✅ Usa los colores de la paleta oficial (--M y --T)

---

## 📂 Pasos para Agregar una Nueva Sección

### Paso 1: Crear Estructura
```bash
mkdir -p Lety2E/nueva-seccion
touch Lety2E/nueva-seccion/index.html
```

### Paso 2: Crear index.html
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Nueva Sección — lety2e.com</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body data-section="nueva-seccion">
  <nav id="nav-container"></nav>
  
  <main>
    <h1>Nueva Sección</h1>
    <p>Contenido aquí...</p>
  </main>

  <footer id="footer-container"></footer>

  <script src="../nav.js"></script>
  <script src="../footer.js"></script>
</body>
</html>
```

### Paso 3: Registrar en nav.js

```javascript
const SECTIONS = {
  // ... otras secciones
  "nueva-seccion": { label: "Nueva Sección", icon: "🔗" },
};

const ROOT_LINKS = [
  // ... otros links
  { href: "nueva-seccion/", label: "Nueva Sección", icon: "🔗" },
];
```

### Paso 4: (Opcional) Override de CSS

En `style.css`, agregar:
```css
body[data-section="nueva-seccion"] {
  --primary: var(--T);  /* Override de variables si lo necesitas */
}
```

---

## 🔄 Migración LetyMath → HTML

**Estado:** Listos para comenzar (estructura + mapeo de imágenes completado)

### Estructura de Cursos
```
Lety2E/math/
├── index.html              [Índice principal de LetyMath]
├── matematicas-1/
│   ├── index.html          [Índice del Curso 1]
│   ├── operaciones-basicas.html   [REFERENCIA CANÓNICA]
│   ├── jerarquia.html
│   └── ... (9 tópicos)
├── matematicas-2/
│   └── ... (fracciones, trigonometría, proporcionalidad)
├── matematicas-3/
│   └── ... (sistemas, cuadráticas, cónicas, 11+ tópicos)
├── matematicas-4/
│   └── ... (funciones avanzadas, 7 tópicos)
├── matematicas-5/
│   └── ... (cálculo, 3 tópicos)
└── optativa/
    └── ... (temas complementarios)
```

### Profundidad de Rutas

Todas las páginas de temas están a profundidad 2:
```
Lety2E/math/matematicas-N/tema.html
       ^    ^              ^
       |    |              └─ Profundidad 2
       |    └─ Profundidad 1
       └─ Profundidad 0
```

Por lo tanto, el src debe ser:
```html
<script src="../../nav.js"></script>
<script src="../../footer.js"></script>
<link rel="stylesheet" href="../../style.css">
```

### Contenido por Tópico (Mínimo)

- ✅ Concepto teórico (2-3 párrafos)
- ✅ Fórmulas en LaTeX/KaTeX
- ✅ 1-2 videos de YouTube (CSV lista_videos_youtube.csv)
- ✅ Ejemplos resueltos paso a paso
- ✅ 6 ejercicios (visible)
- ✅ Respuestas (colapsables)
- ✅ 6 ejercicios extra (colapsables, borde dashed)

### Mapeo de Imágenes Antiguas

- **Archivo:** `letymath/mapeo_imagenes_completo.csv`
- **Estrategia:** Transcribir imágenes JPG a LaTeX/HTML (no incrustar)
- **Ventajas:** Más limpio, indexable por Google, responsive, editable

---

## 🎯 Preferencias de Diseño (Confirmadas)

| Aspecto | Preferencia |
|---------|------------|
| **Colores** | Magenta (#FF00AA), Turquesa (#00DEC8), Morado (#4A0080) |
| **Tipografía** | Playfair Display (títulos), DM Sans (body) |
| **Estructura** | Minimalista, sin explicaciones innecesarias |
| **Ejercicios** | Grid 3 col, sin numeración dentro, respuestas directas |
| **Potencias** | Siempre expandidas en 3 pasos |
| **Respuestas** | Formato "= paso = **resultado**", NUNCA flechas |
| **Colapsables** | Respuestas y Extras, Ejercicios siempre visibles |
| **Videos** | 2 lado a lado (grid 2 col) |
| **Margins** | 2.5rem entre secciones |
| **GitHub Pages** | Rutas relativas (file:// compatible y servibles desde `/`) |

---

## 🚀 Flujo de Trabajo Típico

### Para agregar un tema de LetyMath:
1. Copiar `TEMPLATE-TOPICO.html` → `tema-nuevo.html`
2. Editar: título, videos (YouTube URLs del CSV), fórmulas LaTeX
3. Escribir 1-2 párrafos de concepto
4. Crear 6 ejercicios (grid 3 col, `.mini-card`)
5. Agregar respuestas (colapsables, mismo grid)
6. Agregar 6 extras (colapsables, borde dashed)
7. Verificar rutas (profundidad 2 = `../../nav.js`)
8. Testing: abrir en navegador (file://) y móvil

### Para agregar una nueva sección:
1. Crear carpeta + `index.html` con `data-section`
2. Actualizar `SECTIONS` y `ROOT_LINKS` en `nav.js`
3. Agregar botón en portada principal (`index.html`)
4. (Opcional) Override de variables CSS si necesario

---

## 🔗 Archivo de Referencia

| Archivo | Propósito |
|---------|-----------|
| `CLAUDE.md` | Este documento — guía definitiva |
| `style.css` | Estilos únicos para todo el sitio |
| `nav.js` | Navegación automática (detecta profundidad) |
| `footer.js` | Pie de página automático |
| `TEMPLATE-TOPICO.html` | Template para copiar en LetyMath |
| `mapeo_imagenes_completo.csv` | Mapeo de JPGs antiguos a tópicos |
| `list_videos_youtube.csv` | URLs de videos por tópico |

---

## ✅ Checklist para Todo Nuevo Contenido

- [ ] Favicon SVG creado en raíz con logo 2E (magenta + turquesa)
- [ ] Favicon linkado con profundidad correcta en `<head>`
- [ ] Estructura de carpeta creada (`/seccion/tema/`)
- [ ] HTML con profundidad correcta (`../../../nav.js` si aplica)
- [ ] `body[data-section="..."]` incluido
- [ ] Colores SOLO de variables CSS (--M, --T, --P, etc.)
- [ ] Tipografía correcta (Playfair Display + DM Sans)
- [ ] Grid 3 columnas para ejercicios (`.bloques-3`)
- [ ] Respuestas en formato "= paso = **resultado**"
- [ ] Potencias expandidas en 3 pasos (si aplica)
- [ ] Respuestas/Extras colapsables, Ejercicios visibles
- [ ] KaTeX renderizado correctamente (si es math)
- [ ] Rutas relativas funcionales (probadas en file://)
- [ ] Testing responsive (móvil + desktop)
- [ ] Links prev/next a temas (si es LetyMath)

---

## 🚢 Deploy a GitHub Pages

El sitio se publica automáticamente desde el branch `main` del repo `letymath/lety2E`.

### Flujo estándar después de cualquier cambio
```bash
cd ~/Desktop/lety2E\ 2/
git status                       # ver qué cambió
git add .                        # stage de todo lo modificado
git commit -m "mensaje claro"    # ej: "favicon: agregar link en páginas de math"
git push                         # publica a GitHub → Pages actualiza en ~1-2 min
```

### Archivos críticos del deploy
- `CNAME` → contiene `lety2e.com` (NO borrar, es el que liga el dominio)
- `index.html` raíz → portada
- `favicon.svg` y `favicon.ico` raíz → ícono del sitio

### Verificación después de push
1. Esperar 1-2 min para que GitHub Pages rebuilde
2. Abrir `lety2e.com` en **ventana de incógnito** (evita caché)
3. Si el favicon no aparece, probar `lety2e.com/favicon.svg?v=2` directo
4. Revisar en GitHub: repo → Settings → Pages → ver status del último deploy

---

## 💡 Notas Finales

- **Proyecto en crecimiento:** Nuevas secciones agregadas frecuentemente (próxima: Alojamiento)
- **Minimalista:** La filosofía es "paquetitos" — menos explicación, más estructura
- **Mantenible:** Un único CSS + Nav + Footer = cambios globales sin duplicados
- **Responsive:** Compatible con móvil, tablet, desktop
- **File-compatible:** Funciona tanto servido por GitHub Pages como con file:// local

**Cualquier duda o cambio futuro:** Actualizar este CLAUDE.md para mantener coherencia.

---

*Guía mantenida por Claude 🤖 | Versión actual: Abril 2026*
