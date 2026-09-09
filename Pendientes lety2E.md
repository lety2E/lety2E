# Pendientes — lety2E

**Matemáticas 3: faltan 5 temas por capturas** — el curso se completó el 6-sep-2026 con **18 de 23**
temas, todos desde las capturas (no hay LaTeX de este curso y no hace falta). Los cinco que faltan
son **ecuación general de la elipse, regreso de la elipse, ecuación general de la hipérbola, regreso
de la hipérbola** e **historia**: sus carpetas en `~/Desktop/capturas/matemáticas 3/` (19 a 23) están
**vacías**. En cuanto Lety suba esas capturas se arman igual que los demás; para las cónicas ya están
los generadores de SVG en `Recursos lety2E/` (circunferencias y parábolas sirven de molde para la
elipse y la hipérbola). El índice del curso sigue con su `.proximamente-nota` hasta entonces.

**Migrar Matemáticas 4** — es el único curso que queda. Hay que ver primero si tiene capturas
(`~/Desktop/capturas/matemáticas 4/` existe) o si Lety pasa el LaTeX. El flujo de Math 3 —capturas →
verificar aritmética → armar con `Recursos lety2E/generador-paginas-math3.py`— sirve tal cual.

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

**Los exámenes viven en `cuadros/`** (8-sep-2026) — el sitio de exámenes se armó como
sección de este proyecto, con su generador en `cuadros/generador/`. **Seis versiones** por
examen, y el trato con los alumnos es el de siempre: los *Ejercicios* traen respuesta para
practicar y los *Ejercicios extra* **no**, porque de ahí sale el examen. Cuando un tema se
quede corto, Lety pide los extras **tema por tema** ("necesito 6 extras más de mcm-mcd"),
nunca por adelantado, y los nuevos van **sin resolución**. Lo que decidió sobre cómo son sus
exámenes está en `Recursos lety2E/Reglas de mis exámenes.md`.

Lo que falta, en orden:

- **Los nueve temas de Mate 1 que corren con reparto provisional** —Monomios, Gráfica con
  tabulación, Pendiente y ordenada, Área y perímetro, Ecuaciones con ángulos, Reglas de
  exponentes, mcm y MCD, Lenguaje algebraico y Problemas de ecuaciones—: los propuso el
  asistente y Lety no los ha revisado. A **Área y perímetro** y **Ecuaciones con ángulos**
  ya no les alcanzan los reactivos para la sexta versión, y **mcm y MCD** cae a uno solo;
  se arregla publicando más extras aquí.
- **Las resoluciones de Matemáticas 1.** La cosecha automática trae 90 de los 271
  ejercicios del examen; los otros 181 son extras y se escriben a mano, sobre la marcha.
  Falta decidir con qué tema empezar.
- **Las secciones "Ejercicios resueltos" no se cosechan.** Tres temas (Expresiones
  algebraicas, Pendiente y ordenada, mcm y MCD) traen la resolución *dentro* de la tarjeta
  del ejercicio, no en una lista paralela como las secciones "Respuestas", así que
  `resoluciones.py` no las empareja: son ~30 resoluciones **ya publicadas** que hoy se
  cuentan como pendientes de escribir.
- **Rehacer las filas del Examen 1 cuando pase a dos hojas.** Hoy cabe en una, pero su
  primera fila empareja *Operaciones básicas* (tema 1) con *Ecuaciones con ángulos* (tema
  9), y la regla es que el corte entre hojas respete el orden de los temas.
- **Matemáticas 2 y 5**, completos en el sitio y sin tocar todavía. Mate 5 es además una de
  las materias de este semestre.
- **`cuadros/generador/propios.py`** quedó de un experimento descartado: borrarlo o dejarlo
  como registro.
