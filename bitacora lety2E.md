# Bitácora — lety2E

> Registro de lo que vamos haciendo en el sitio. Lo más reciente arriba.
> (Los pendientes van en `Pendientes lety2E.md`, no aquí.)

---

## 2026-07-07
- **Publicado el tema 8: Pendiente y ordenada al origen** (`math/matematicas-2/pendiente-ordenada.html`), duplicando y adaptando la página correspondiente de Matemáticas 1 por indicación del temario LaTeX.
- Se enlazaron las páginas agregando el botón Siguiente en `recta-dos-puntos.html` que apunta a `pendiente-ordenada.html`, y se añadió la card de Pendiente y ordenada al origen al index de Matemáticas 2.
- **Publicado el tema 7: Ecuación de la recta dados dos puntos** (`math/matematicas-2/recta-dos-puntos.html`) con apuntes teóricos de la fórmula punto-punto, un ejemplo detallado con su comprobación y gráfica SVG, un bloque de 6 ejercicios de práctica con resoluciones completas (que incluyen el procedimiento, comprobaciones y su gráfica en SVG inline) y 4 tarjetas de ejercicios extra.
- Se enlazaron las páginas agregando el botón Siguiente en `grafica-cuadratica.html` que apunta a `recta-dos-puntos.html`, y se añadió la card de Ecuación de la recta al index de Matemáticas 2.
- **Publicado el tema 6: Funciones cuadráticas** (`math/matematicas-2/grafica-cuadratica.html`) con apuntes teóricos de parábolas, ejemplo con tabla y gráfica SVG inline, 2 bloques de ejercicios de práctica, resoluciones completas paso a paso para todos los ejercicios (incluyendo sus respectivas tablas y gráficas en SVG) y 4 bloques de ejercicios extra estructurados en tarjetas.
- **Pausada migración de Matemáticas 5** para trabajar en **Matemáticas 2** por petición de Lety (fuente: `Recursos lety2E/Latex Matematicas 2.md`).
- **Publicado el tema 5: Ecuaciones con fracciones** (`math/matematicas-2/ecuaciones-fracciones.html`) con video de YouTube (`hRxUBd1SxZo`), apuntes teóricos de ejemplos, 4 bloques de ejercicios prácticos, respuestas KaTeX paso a paso y extras.
- Actualizada la navegación de `algebra-fracciones.html` para incluir el botón Siguiente y añadida la card de Ecuaciones con fracciones al índice de Matemáticas 2.
- Se enlazaron las páginas agregando el botón Siguiente a `ecuaciones-fracciones.html` que apunta a `grafica-cuadratica.html`, y se añadió la card de Funciones cuadráticas al index de Matemáticas 2.
- **Arrancó la migración de Matemáticas 5** (fuente: transcripción de Lety en `~/Downloads/Latex matematicas 5.md`, revisada completa — 19 temas sanos, sin duplicados).
- **Publicado el tema 1: Reglas básicas de derivación** (`math/matematicas-5/reglas-basicas.html`) con 2 videos (reglas básicas + con x en el denominador — fusiona los dos temas del sitio viejo, decisión de Lety), apuntes, 4 ejemplos, 4 bloques de ejercicios con respuestas paso a paso y extras.
- Index de Mat 5 estrenado (adiós `próximamente`; descripción corregida: era "álgebra lineal", es Cálculo) y card del curso activada en el índice de Math.
- Orden del curso y decisiones registradas en `Pendientes lety2E.md` (incl. Historia del Cálculo → para pensar: cierre con IA / trabajos de historia de las matemáticas).
- Arreglado `.claude/serve.py` (apuntaba a la carpeta vieja `lety2E 2`).

## 2026-07-02
- **Simulador UNAM publicado:** ya tiene su card en el índice de Apuntes (antes solo se llegaba por URL directa).
- Puesta a punto para trabajar desde Claude Code (revisión completa del proyecto):
  - Retirado `INSTRUCCIONES.md` (desactualizado y duplicaba a `CLAUDE.md`); lo único que faltaba —cómo agregar apuntes, relatos, cantos y secciones— ahora vive en `CLAUDE.md`.
  - Corregida la URL del repo en los docs (`lety2E/lety2E`, la real).
  - Skill `letymath-html` limpiada de restos de Cowork (rutas `/sessions/...`, color de cards equivocado, nombres de temas desactualizados) y el template corregido (`data-section="math"`).
  - Preview local arreglado y documentado: `python3 .claude/serve.py` (el panel de preview de la app no puede leer Desktop por permisos de macOS).
  - Permisos ordenados: `.claude/settings.json` del proyecto (git + preview) y `settings.local.json` depurado (~130 permisos de tareas ajenas al sitio).
  - Detectado: el simulador UNAM está en línea pero sin card en Apuntes → anotado en `Notas por revisar.md`.
- Limpieza del repo: borradas 7 copias de trabajo viejas (`.claude/worktrees/`, todas ya incorporadas a `main`) y sus ramas. Descartado `temario-biologicas.html` (huérfano de mayo, decisión de Lety).
- Commit del renombre `Bitácora.md` → `bitacora.md` (estándar del sistema) y su referencia en `CLAUDE.md`.

## 2026-06-29
- Organizado el sistema del proyecto para trabajar siempre desde Code: creada `bitacora.md` y `Sistema (cómo funciona).md`; `Notas por revisar.md` poblado con pendientes reales.
- `CLAUDE.md`: agregada la regla de bitácora y el flujo de trabajo de Math (borrador con Gemini + capturas → doc en Drive un tema por pestaña → Claude arma el HTML y sube; + modo "desde cero").
- Definida la **prioridad**: empezar a migrar **Matemáticas 5** (semestre de agosto 2026).

## 2026-06-27
- Creada esta bitácora. A partir de hoy aquí queda el registro del trabajo en el proyecto.

## 2026-06-19
- **COMIPEMS:** agregado el Simulador COMIPEMS (ingreso a bachillerato) en `apuntes/`.
- COMIPEMS: las opciones de respuesta ahora se barajan, para quitar el sesgo hacia la opción A.

## 2026-05-20
- **problemas-ecuaciones:** ecuaciones más grandes en móvil; frase con wrap y mejor balance entre frase y ecuación.
- **reglas-exponentes:** quitados los títulos morados de todas las tarjetas.
- Agregada sección de ejercicios extra con 5 triángulos (ecuaciones con ángulos).
