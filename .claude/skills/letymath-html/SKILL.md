---
name: letymath-html
description: Generar páginas HTML de temas de matemáticas para LetyMath (lety2e.com) a partir del documento LaTeX de Lety. Usar cuando se pida crear una página para un tema específico (jerarquía, ecuaciones, monomios, etc.) o convertir contenido de Google Doc a HTML con el diseño "paquetitos" aprobado.
---

# LetyMath — generar página HTML de tema

## Contexto

Lety migra su sitio letymath.com a lety2e.com. Tiene todas sus lecciones transcritas a LaTeX en un Google Doc (ID `1hTzKA2zC98FwfSiR9nR21gExC2hT4nrea-BANrbkd4I`, "latex matematicas 1"). Cada tema del doc se separa por `# N nombre`. La skill convierte cada tema en un HTML con su diseño minimalista de "paquetitos".

## Referencias canónicas

Antes de empezar cualquier trabajo, leer:
- `references/template.html` — plantilla base con todos los estilos v6
- `/sessions/cool-pensive-ramanujan/mnt/Lety2E/math/matematicas-1/operaciones-basicas.html` — tema 1, sin video (vs. con videos cortos), bloques de 6×6, respuestas en una línea
- `/sessions/cool-pensive-ramanujan/mnt/Lety2E/math/matematicas-1/jerarquia.html` — tema 2, con 1 video, bloques de 2×4, respuestas multi-línea con `\begin{aligned}`

Estos dos archivos son el ground truth. Si algo en esta skill contradice el HTML ya aprobado, el HTML gana.

## Workflow

### 1. Obtener el contenido LaTeX del tema

```bash
# Parsear el doc de Drive a texto plano (solo si no existe ya)
jq -r '.[0].text' /ruta/al/archivo.txt | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['text'])" > /tmp/latex_content.txt

# Encontrar rango de líneas del tema
grep -n "^# [0-9]" /tmp/latex_content.txt

# Extraer (ejemplo para tema que va de línea X a Y-1)
sed -n "X,Yp" /tmp/latex_content.txt > /tmp/tema.tex
```

Si el usuario ya te dio el contenido directo (pegado o en archivo), usar ese.

### 2. Preguntar por el video (si aplica)

No todos los temas tienen video. Si no sabes, pregunta al usuario: "¿Este tema tiene video de YouTube? Si sí, pásame el link."

Formato del link: `https://youtu.be/XXXXX` → extraer ID `XXXXX` para usar en `https://www.youtube.com/embed/XXXXX?rel=0`.

### 3. Decidir estructura

Analizar el LaTeX extraído para decidir:

| Elemento | Criterio |
|---|---|
| Video | 0, 1, 2 — si hay 1 usar `.video-single`, si hay 2 usar `.videos-row` (grid 2 col) |
| Apuntes | Solo si el usuario provee texto. Si no está en el LaTeX, omitir la sección |
| Ejemplo | Siempre — extraer de `Ejemplos` en LaTeX |
| Bloques de ejercicios | Contar `\subsection*{\centering Bloque N}` en el LaTeX |
| Grid: 2 vs 3 cols | Ver tabla abajo |

**Decisión de grid según complejidad:**

- `bloques-3` (3 columnas) cuando: 6 bloques de 6 ejercicios simples/cortos (ej. operaciones-basicas)
- `bloques-2` (2 columnas) cuando: 2-4 bloques de 4-10 ejercicios, o ejercicios largos con paréntesis anidados (ej. jerarquia)
- Si dudas, usa `bloques-2` (más legible para ejercicios complejos)

### 4. Formato de las respuestas

**Respuestas de 2-3 pasos** (operaciones-basicas): una línea con `=` encadenados
```
$-5+6-3+2-1 = 8-9 = $ <strong>$-1$</strong>
```

**Respuestas de 4+ pasos** o con paréntesis anidados (jerarquia): `\begin{aligned}` en display math
```html
<div class="sol">
  $$\begin{aligned}
    4-2(-1)(-5)+6(-1+4)-3(-5)^2 &= \\
    4-10+6(3)-3(25) &= \\
    4-10+18-75 &= \\
    22-85 &= \mathbf{-63}
  \end{aligned}$$
</div>
```

**Potencias: SIEMPRE 3 pasos** (expansión → producto → resultado):
- `(-4)^3 = (-4)(-4)(-4) = 16(-4) = -64`
- `4(-5)^2 = 4(-5)(-5) = 4(25) = 100`
- `-6(5)^3 = -6(5)(5)(5) = -6(125) = -750`

### 5. Transformaciones LaTeX → KaTeX

| LaTeX original | HTML/KaTeX |
|---|---|
| `\mathbf{X}` | `<strong>$X$</strong>` dentro de inline, o `\mathbf{X}` dentro de `aligned` |
| `\\[3pt]`, `\\` en align | `\\` (KaTeX lo soporta) |
| `\begin{align*}` | `\begin{aligned}` (KaTeX no tiene `align*`, usa `aligned`) |
| `\sqrt[3]{27}` | `\sqrt[3]{27}` (igual) |
| `\pm 6` | `\pm 6` (igual) |
| `\mathbb{R}` | `\mathbb{R}` (igual) |
| Texto del doc con `\-`, `\+`, `\[`, `\]` escapados | Desescapar: `-`, `+`, `[`, `]` |
| `\\_` | `_` |

El doc de Drive viene con muchos escapes raros porque pasa por Markdown. Limpia con:
```python
text = text.replace('\\-', '-').replace('\\+', '+').replace('\\[', '[').replace('\\]', ']').replace('\\_', '_').replace('\\\\', '\\')
```

### 6. Generar el HTML

Copiar `references/template.html` y reemplazar placeholders. Secciones en orden:

1. **Video** (opcional) — 1 o 2 videos
2. **Apuntes** (opcional) — solo si Lety provee texto
3. **Ejemplo** — siempre, con intro tipo "Resuelve las siguientes operaciones..."
4. **Ejercicios** — siempre visibles (no colapsable), `.sec-head` + `.bloques-N`
5. **Respuestas** — colapsable (`.sec-toggle` + `.collapsible`), empieza oculto
6. **Ejercicios extra** — colapsable, empieza oculto
7. **Navegación** — botones prev/next

### 7. Paths y archivos

- Carpeta: `/sessions/cool-pensive-ramanujan/mnt/Lety2E/math/matematicas-1/`
- Nombre del archivo: kebab-case sin tildes, ej. `jerarquia.html`, `ecuaciones.html`, `expresiones-algebraicas.html`
- Links CSS/JS: `../../style.css`, `../../nav.js`, `../../footer.js` (depth 2)
- Orden según numeración en el doc de Lety (tema 2 = jerarquia, tema 3 = ecuaciones, etc.)

### 8. Navegación prev/next

Tabla de orden (actualizar `index.html` si es nuevo):

```
1. operaciones-basicas
2. jerarquia
3. ecuaciones
4. monomios
5. expresiones-algebraicas
6. grafica-tabulacion
7. pendiente-ordenada
8. area-perimetro
9. ecuaciones-angulos
10. regla-exponentes
11. mcm-mcd
12. lenguaje-algebraico
13. problemas-ecuaciones-lineales
14. divisibilidad
15. sistemas-numeracion
```

En los botones:
```html
<a href="PREV.html" class="btn-anterior">← Nombre anterior</a>
<a href="NEXT.html" class="btn-siguiente">Nombre siguiente →</a>
```

## Diseño (v6 — aprobado por Lety)

**Metodología "paquetitos"**: el alumno recibe paquetes compactos y sabe qué hacer sin etiquetas ni explicaciones innecesarias. Minimalista, directo.

**Paleta (solo variables de `style.css`, nunca inventar):**
- `--course-1` / `--P` / `--accent` = `#4A0080` (morado — headers, iconos)
- `--M` = `#FF00AA` (rosa — títulos, acentos, resultados strong)
- `--T` = `#00DEC8` (turquesa — disponible si hace falta)
- `--bg-card` = `#FBF2EF` (fondo de tarjetas)
- `--border` = `#E0C4BC`
- `--accent-light` = `#F0E0F5`

**Reglas visuales:**
- Headers de `mini-card` en morado (`var(--course-1)`), texto blanco
- Resultados finales en `<strong>` color rosa (`var(--M)`)
- Ejemplo: icono morado + título "Ejemplo" en rosa itálicas Playfair, fondo `--bg-card`
- Sin numeración interna en los bloques (`1.`, `2.`) — solo `<br>` entre ejercicios
- Sin flechas `→` en respuestas — usar `=`
- Sin explicaciones tipo "Pos:", "Neg:" — directo al procedimiento
- Espaciado: `.section-block { margin-bottom: 2.5rem }`

## Checklist antes de entregar

- [ ] ¿Las respuestas usan `=`, no `→`?
- [ ] ¿Las potencias muestran los 3 pasos expandidos?
- [ ] ¿Los bloques usan el grid correcto (2 o 3 cols) según la complejidad?
- [ ] ¿Respuestas y Extras son colapsables con `.sec-toggle` + `.collapsible`?
- [ ] ¿Ejercicios están siempre visibles (sin toggle)?
- [ ] ¿El Ejemplo tiene su intro tipo "Resuelve..." + bloque llamativo?
- [ ] ¿Los colores son solo `var(--...)`, ninguno inventado?
- [ ] ¿La navegación prev/next tiene los nombres correctos?
- [ ] ¿El archivo está en `math/matematicas-1/` (no `letymath/`)?
- [ ] ¿El video (si hay) usa el ID correcto en `youtube.com/embed/ID?rel=0`?
- [ ] ¿Los delimitadores KaTeX son `$...$` inline y `$$...$$` display?
- [ ] ¿Los escapes del doc (`\-`, `\+`, `\[`) están limpios?

## Notas de trabajo con Lety

- Lety es la creadora — llama a su metodología "paquetitos"
- Prefiere iterar visualmente. Si dudas sobre el diseño, generar y preguntar
- Odia la numeración interna, los colores inventados, los gradientes raros
- Los cambios se ven directo en su carpeta (no hay deploy manual para preview local)
- Ella puede proveer apuntes, videos, o ajustes al orden de los temas
