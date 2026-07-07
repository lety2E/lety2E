# Bitácora — lety2E

> Registro de lo que vamos haciendo en el sitio. Lo más reciente arriba.
> (Los pendientes van en `Pendientes lety2E.md`, no aquí.)

---

## 2026-07-07
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
