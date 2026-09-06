# Pendientes — lety2E

**Migrar Matemáticas 3 y 4** — son las dos carpetas que siguen vacías (solo el índice con
*próximamente*). En letymath.com cada una tiene **18 temas**. Math 1 y Math 2 ya quedaron
completas el 5-sep-2026. Falta que Lety pase el LaTeX de esos dos cursos; el flujo que ya
funcionó es: LaTeX por tema → verificar la aritmética → armar el HTML → card en el índice
y botones prev/next. Los triángulos SVG salen de `Recursos lety2E/triangulos-svg-math.py`; para las cónicas de Math 3 y las funciones de Math 4 va a hacer falta un generador nuevo, ése sirve de molde.

**Math 5 se queda como está** — letymath.com tiene un tema más, *"Dx. Con x en el
denominador"*, que **no se va a migrar**: Lety lo dio por incorporado dentro de
*Reglas básicas*. O sea que Math 5 está completo aunque el conteo contra el sitio viejo
dé 19 vs 20. No volver a proponerlo.

**Avisar a GICAIA: la guía ya existe y cambió de nombre** — se publicó el 2-sep-2026 como
**"Primeros pasos"** (`docencia/primeros-pasos.html`), no como "Aula propia". En la pestaña
Recursos de GICAIA el enlace todavía se llama *"Aula propia — la guía para arrancar"* y apunta
al índice `lety2e.com/docencia`. Hay que cambiar allá **las dos cosas**: el texto del enlace y
el destino, que ahora sí puede ir directo a `lety2e.com/docencia/primeros-pasos.html`.

**Seguir ajustando "Primeros pasos"** — Lety quiere continuar la ronda de ajustes (pausada
el 2-sep-2026 por la noche). Lo que quedó sobre la mesa: el bloque "Quién soy" es el único
con ejemplo lleno y se ve solo entre los demás; también se puede volver pregunta y dejar el
archivo 100% plantilla. Al publicar quedó tal cual está descrito en la bitácora de ese día.

**Probar la guía con las dos compañeras** — la escriben solas antes del jueves y lo que se
atore se ve en persona (aula invertida aplicada a ellas). Después de esa sesión, corregir la
guía con lo que de verdad las paró: los cuatro puntos marcados como "aquí es normal atorarse"
son una apuesta, no un dato. El paso 5 (el repositorio) es el que más rápido envejece porque
depende de pantallas de GitHub — revisarlo cada tanto.

**Física y Geografía de Área 2** — hoy solo tienen formulario, no guía completa. Lety va a
revisar si con el formulario basta. Si decide que no, el contenido completo de Física ya
existe dentro de `Guias-unam.html` (proyecto Artefactos, carpeta `Ingreso licenciatura`) y de
ahí se puede sacar. Ella avisa.

**`apuntes/Templete-apuntes.md`** — documenta el formato viejo de zoom N1–N5; ninguna página
viva lo usa desde el 5-ago-2026. **Dejarlo por si acaso**; Lety decide después si se conserva.
El prototipo está guardado en `Recursos lety2E/formato-apunte-zoom-N1-N5 (segunda-guerra-mundial).html`.

Historia del Cálculo — idea: trabajos de historia de las matemáticas como cierre de cursos; no publicar cuestionario todavía

**Los ejercicios extras del sitio son el banco de sus exámenes** (6-sep-2026) — Lety va a
armar exámenes con **5 versiones por curso**; los exámenes se hacen y se guardan en el
proyecto **IEMS** (`4 Materiales y evaluación/`, no se publican). Pero los reactivos salen de
aquí: cada tema se evalúa con ~3 ejercicios, uno de los que **sí traen respuesta** y dos de
los **extras** (la mezcla varía según el tema). De ahí que cada tema necesite **al menos 10
ejercicios extra** para que las 5 versiones no se repitan.

Es **a propósito** que esos ejercicios estén publicados: Lety quiere que los alumnos sepan de
dónde va a salir el examen, a ver si así lo pasan más fácil. O sea que ampliar los extras no
es solo para el examen, también es práctica para ellos.

**No hay que adelantarse a crearlos**: ella los va pidiendo tema por tema conforme prepara
cada examen ("necesito 6 extras más de mcm-mcd"). Del inventario del 6-sep-2026, los que ya se
sabe que quedan cortos: `ecuaciones` (M1) **no tiene sección de extras**, `algebra-fracciones`
(M2) tampoco, y `expresiones-algebraicas` y `mcm-mcd` (M1) traen solo 8. Los temas con figuras
(area-perimetro, ecuaciones-angulos, pitagoras, semejanza-triangulos, razones-trigonometricas,
proporcionalidad, representacion-fracciones) hay que contarlos a mano y son más laboriosos:
cada ejercicio nuevo lleva su SVG.
