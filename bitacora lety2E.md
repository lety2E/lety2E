# Bitácora — lety2E

> Registro de lo que vamos haciendo en el sitio. Lo más reciente arriba.
> (Los pendientes van en `Pendientes lety2E.md`, no aquí.)

---

## 2026-09-08 (3) — Exámenes: negro sobre blanco y una hoja carta por examen

Tres decisiones de Lety para `cuadros/`, todas ya en el generador y en
`Recursos lety2E/Reglas de mis exámenes.md`:

- **Negro sobre blanco, ni un color.** La letra pasó de `#3D2525` a negro y el borde de
  las tarjetas de `#E0C4BC` a negro de 1 px (el negro pesa más, por eso adelgazó). Las
  figuras que vienen de `math/` se pasan a escala de grises con CSS —cuadrícula clarita,
  ejes gris medio, lo demás negro—, sin tocar el origen. En las hojas resueltas el morado
  de las resoluciones se vuelve negro **al imprimir** y se queda morado en pantalla.
- **Cada versión cabe en una hoja carta**: puede sobrar espacio, no excederse. Se agregó
  `cuadros/generador/medida.py`, que calcula la altura con las medidas reales del CSS
  (calibradas contra el navegador: 723 px medidos, 723 estimados) y la reporta al generar.
  Hoy el Examen 1 va al **73%** de la hoja y el Examen 2 al **36%**, así que hay aire.
  Arriba del 92% avisa; arriba del 100% grita ¡NO CABE!
- **Dos exámenes por semestre y, dentro de cada uno, el orden da igual.** Sólo importa el
  reparto: la primera parte de los temas en el primero, la segunda en el segundo. Eso
  **sustituye** la regla de "no me pongas un último tema en la primera hoja", que era para
  cuando un examen se iba a dos hojas. `acomodo.py` ahora avisa si un tema se quedó fuera
  de los dos exámenes.

Regenerados los doce exámenes de IEMS y las doce versiones del sitio.

---

## 2026-09-08 (2) — Math 3: se publican los dos temas de la elipse

`math/matematicas-3/elipse-general.html` y `elipse-regreso.html` (temas 19 y 20) ya estaban
escritos y enlazados desde el índice del curso; se les corrió `prerender-katex.js` antes de
publicar —141 y 169 fórmulas— y se subieron. Con eso Math 3 va en **20 de 23**.

Quedaron **sin publicar a propósito**, por decisión de Lety: `math/matematicas-1/decimales.html`
y `math/matematicas-3/hiperbola-general.html`. Están escritos y sin commitear, en el árbol de
trabajo.

---

## 2026-09-08 — Nace `cuadros/`: el sitio de exámenes se vuelve una sección de aquí

El generador de exámenes venía armándose desde el 7-sep en el proyecto **IEMS**, y en la
mañana se sacó a un proyecto aparte del Escritorio. Al aterrizar el diseño, Lety decidió
traerlo **aquí adentro**: una carpeta más de este repo, `cuadros/`, servida en
**lety2e.com/cuadros**. El proyecto aparte se disolvió el mismo día.

**Por qué aquí y no aparte.** Se valoró tenerlo en su propio repositorio (incluso en una
organización propia, al estilo de GICAIA, para que nada lo ligara a este dominio), y lo que
lo decidió fue que a Lety **no le preocupa que lo descubran**: *"me vale queso, de todas
maneras se lo tendrán que aprender"*. Sin esa preocupación, el proyecto aparte solo agregaba
fricción: dos carpetas, dos bitácoras, una regla de "solo lectura" y un brinco de sesión cada
vez que agregar ejercicios a un tema implicaba regenerar los exámenes. Ahora es una sola
carpeta, un solo `push`, y las rutas del generador son relativas al repo.

**Qué hay.** `cuadros/index.html` con una tarjeta por materia (Mate 1 a 5 y la optativa; solo
Mate 1 tiene contenido), `cuadros/matematicas-1/` con los dos exámenes y **dos páginas por
versión** —`a.html` en blanco para imprimir y `a-resuelta.html` con la resolución debajo de
cada ejercicio, para calificar—, y `cuadros/generador/` con la maquinaria. Se decidió página
por versión y no una sola con doce pestañas: el cuerpo de una versión pesa ~60 KB y las doce
juntas habrían hecho una página de ~720 KB. La barra de arriba hace de pestañas y cambia
entre la hoja en blanco y la resuelta.

**No pesa nada para el resto del sitio**: son ~1.5 MB en el repo y GitHub Pages sirve archivo
por archivo, así que ninguna otra página baja un byte de más. Al contrario, `cuadros/` usa el
`assets/katex/`, el `style.css` y las tipografías que ya están aquí, en vez de duplicarlos
(los exámenes que van a **IEMS** sí llevan todo incrustado, porque se abren offline).
**No hace falta pasarlo por `prerender-katex.js`**: el generador ya escribe las fórmulas en
HTML.

**Novedad de fondo, las hojas resueltas.** Salió que en `math/` solo la sección *Ejercicios*
trae respuestas: los *Ejercicios extra* no tienen ninguna, **y así debe seguir**, porque son
los que se evalúan. O sea que las resoluciones de `cuadros/` hay que escribirlas. Se armó
`resoluciones.py`, que cosecha del sitio lo ya publicado —empareja *Ejercicios* con su
sección de respuestas por posición— y suma lo escrito a mano en `resoluciones-manuales.json`,
que no se pisa al recosechar. Hoy trae **90 de 271**; el resto se escribe sobre la marcha,
tema por tema, verificando cada una. Lo que falta sale en gris como "pendiente" en la hoja
resuelta.

**Documentación:** las reglas de los exámenes quedaron en
`Recursos lety2E/Reglas de mis exámenes.md` (léelo antes de tocar un examen), la sección
técnica en `CLAUDE.md`, la parte para Lety en `Manual lety2E.md` y lo que falta en
`Pendientes lety2E.md`.

---

## 2026-09-07 (9) — Operaciones básicas tenía reactivos repetidos

Al subir el examen a **seis versiones** se destapó que varios reactivos estaban duplicados entre
bloques: a un alumno le habría tocado `\sqrt{49}` **dos veces en la misma hoja**. El bloque 12 era
casi una copia de piezas de otros bloques (cinco de sus seis ejercicios ya existían).

- **`math/matematicas-1/operaciones-basicas.html`** — nueve reactivos cambiados, **todos en
  bloques de extras**, así que ninguna resolución publicada se tocó:

  | Bloque | Antes | Ahora |
  |---|---|---|
  | 7 | `\sqrt{49}` | `\sqrt{225}` |
  | 9 | `\sqrt{25}` | `\sqrt{100}` |
  | 10 | `\sqrt{36}` | `\sqrt{169}` |
  | 11 | `(-9)^3` | `(-3)^3` |
  | 12 | `2(-3)(-6)`, `-3(-4-2)`, `\sqrt{49}`, `(-8)^3`, `5(-2)^2` | `4(-3)(-5)`, `-5(-2-6)`, `\sqrt{144}`, `(-5)^3`, `9(-2)^2` |

  Cada reemplazo respeta el molde de su posición en el bloque, y se comprobó que ninguno de los
  nuevos existiera ya en otro lado. Los 72 reactivos del tema son ahora distintos entre sí.

- **`math/matematicas-1/expresiones-algebraicas.html`** — se repartió al estilo de Ecuaciones, que
  es como quedó mejor: **cada bloque mezcla los dos tipos**, tres sin cuadrado y tres con cuadrado,
  alternados. *Ejercicios* con Bloque 1 (del que sale el examen) y Bloque 2 (práctica resuelta que
  no entra); *Ejercicios extra* con Bloque A y Bloque B. Las doce resoluciones se reordenaron otra
  vez para seguir correspondiendo una a una.

Nota: los dos desbordes que se ven en las Respuestas de Operaciones básicas (bloques 4 y 6) ya
estaban y son el comportamiento buscado: mejor que la ecuación se salga a que se parta al medio.

---

## 2026-09-07 (8) — Un bloque por tipo, y material para seis versiones

Idea de Lety, viendo cómo quedó Ecuaciones: en vez de bloques mezclados, **cada bloque reúne los
ejercicios de un mismo tipo**, y el examen toma un renglón de cada bloque. Y se pasa a **seis
versiones**, que es lo que dan de sí los seis bloques de Operaciones básicas.

- **`math/matematicas-1/jerarquia.html`** — las cuatro secciones se reagruparon por tipo:
  *Ejercicios* con Bloque 1 (6 expresiones con potencias) y Bloque 2 (6 corchetes anidados), y las
  *Respuestas* en el mismo orden. **Un par nuevo, con su resolución**:
  `7-3(2)(-4)+5(-6+2)-2(3)^2=` (da $-7$) y `-5[2(-6(4-9))]=` (da $-300$).
  *Ejercicios extra 1* con seis de cada tipo, *extra 2* con los cuatro de cada tipo que sobran.
- **`math/matematicas-1/expresiones-algebraicas.html`** — igual: Bloque 1 con los seis sin
  cuadrado y Bloque 2 con los seis con cuadrado, y lo mismo en los extra. **Un par nuevo con su
  resolución** (`4[(3x-2)(1-4x)+5x]-3=` y `3(-2x+5)^2+4(-3+2x)-8=`) y **un par nuevo de extras**.
  Las doce resoluciones se reordenaron para seguir correspondiendo una a una con sus ejercicios.
- Todo lo nuevo se verificó **numéricamente, paso por paso**: cada renglón de cada resolución da
  el mismo valor que el ejercicio original.

Cuidado para la próxima: la sección *Ejercicios resueltos* de Expresiones algebraicas **no usa
`mini-card` sino `ejemplo-block` / `ejemplo-grid` / `ejemplo-item`**, con `<hr class="resueltos-sep">`
entre pares. Un script que busque `bloques-2` ahí se salta la sección y va a dar a la siguiente.

Revisado en local a 1000px y en móvil (375px).

---

## 2026-09-07 (7) — Ecuaciones: le faltaban dos resoluciones y todos los extras

Al armar el examen de IEMS salió que **este tema estaba incompleto**: seis ejercicios pero solo
cuatro resoluciones publicadas, y **ninguna sección de ejercicios extra**. Queda completo y con la
estructura que pidió Lety.

- **`math/matematicas-1/ecuaciones.html`**
  - *Ejercicios*: los bloques 1 y 2 se unieron en **un solo bloque de 6**, a lo ancho.
  - *Respuestas*: **se escribieron las dos que faltaban**, las de `-2+3(4+7x)=1-3(x-6)` (da
    $x=\tfrac{3}{8}$) y `-3(-2x-8)+6=7x+5(4-2x)` (da $x=-\tfrac{10}{9}$), en el mismo formato de
    seis pasos que las otras cuatro. Ahora las seis corresponden a sus seis ejercicios, en orden.
  - *Ejercicios extra 1* (nueva): **dos bloques de 6**. De aquí sale el examen: toma uno de cada
    bloque.
  - *Ejercicios extra 2* (nueva): **un bloque de 6**, práctica que no entra al examen.
- Los 18 ejercicios nuevos **se calcaron de los seis publicados**, molde por molde y en el mismo
  orden: cada bloque recorre los mismos seis tipos de ecuación (paréntesis a los dos lados, con
  las variantes de signo de cada uno). Se resolvieron todos para verificar que ninguno degenera
  (que la $x$ no se cancele) y que las soluciones quedan en el mismo registro que las publicadas,
  fracciones incluidas.
- Se agregó `.bloques-1` al CSS de la página: no existía la rejilla de una sola columna.

Revisado en local a 1000px y en móvil (375px): ningún bloque se desborda.

---

## 2026-09-07 (6) — Los extras de Jerarquía, partidos en 1 y 2

Idea de Lety, para que **el alumno sepa qué estudiar mirando la página, sin que se lo digan**:
los ejercicios extra se parten en dos secciones. De **"Ejercicios extra 1"** sale el examen; el
**2** es práctica adicional y no entra. La separación lo insinúa sin declararlo.

- **`math/matematicas-1/jerarquia.html`** — la sección de extras se dividió en dos, con sus cinco
  bloques cada una: **extra 1** con los bloques A a E, **extra 2** con los F a J. Los veinte
  ejercicios son los mismos de siempre; no se agregó ni se quitó ninguno.
- El generador de exámenes de IEMS ya lee esta convención: si el tema tiene "Ejercicios extra 1"
  toma de ahí y **nunca** del 2; si no la tiene, sigue usando "Ejercicios extra" como antes. Así
  **la página es la fuente de verdad** y no hay dos listas que mantener sincronizadas.

Solo se partió Jerarquía, que es donde de verdad sobra material (diez bloques y el examen usa
cinco). En los temas donde los extras alcanzan justo —Expresiones algebraicas, Área y perímetro,
Ecuaciones con ángulos— partirlos no diría nada. Operaciones básicas tiene seis bloques y el
examen usa cinco: se dejaron los seis juntos a propósito, para que el alumno estudie los seis sin
saber cuál se queda fuera.

Revisado en local a 1000px y en móvil (375px): las dos secciones colapsables, ningún bloque se
desborda.

---

## 2026-09-07 (5) — Jerarquía: bloques de dos, para que sirvan de examen

El cambio viene del proyecto IEMS: allá se están armando **5 versiones del examen de
Matemáticas 1**, y cada tema del examen toma un bloque de los ejercicios y otro de los extra.
Con bloques de 4 y de 10 no salían las cinco versiones, y los tipos quedaban desbalanceados.

Cada bloque de Jerarquía mezcla dos tipos: **expresión con potencias** (`4-2(-1)(-5)+...`) y
**corchetes anidados** (`5[-3(4(-1-2))]`). Antes iban agrupados (los dos del primer tipo y luego
los dos del otro); ahora cada bloque es **una pareja, uno de cada tipo**.

- **`math/matematicas-1/jerarquia.html`**
  - *Ejercicios*: de 2 bloques de 4 a **5 bloques de 2**. Los 8 publicados se reacomodaron en
    pareja sin cambiar ninguno; el **Bloque 5 es nuevo**: `-3+4(-2)(6)-5(3-8)+2(-4)^2=` (da **6**)
    y `6[-4(3(-5+2))]=` (da **216**), con su resolución paso a paso en el estilo de las demás.
  - *Respuestas*: reordenadas en el mismo orden que sus ejercicios, más las dos nuevas.
  - *Ejercicios extra*: de 2 bloques de 10 a **10 bloques de 2**. No se quitó ni se agregó
    ninguno; los 20 ya publicados daban justo 10 parejas.
- Cada ejercicio va ahora en su `.ej-line`, como en `operaciones-basicas` y en
  `expresiones-algebraicas`. **Sin esto se pegaban dos en el mismo renglón**: los `<span>` de
  KaTeX son inline, y con bloques de 4 nunca se notó porque siempre desbordaban.
- Las fórmulas nuevas se renderizaron con el mismo KaTeX del sitio. Ojo para la próxima:
  `prerender-katex.js` **salta las páginas que ya están pre-renderizadas**, así que no sirve para
  agregarle fórmulas a un tema ya publicado; hay que renderizarlas aparte.

Revisado en local a 1000px y en móvil (375px): una columna, ningún bloque se desborda, ningún
ejercicio pegado a otro.

---

## 2026-09-07 (4) — Math 4, tema 2: "Representación de funciones"

Las capturas de este tema **no traen hoja de resueltos**: son doce tablas de valores y ya. Las
doce respuestas se calcularon aquí y se verificaron — las doce son lineales con pendiente y
ordenada enteras, y cada respuesta comprueba los tres puntos de su tabla.

- **`math/matematicas-4/representacion-funciones.html`** (Tema 2) — sin video (no está en el CSV,
  no es error): apuntes, el ejemplo con las **seis representaciones** de la captura, las 12 tablas
  con sus respuestas y **12 tablas extra** sin respuesta.
- Cada respuesta trae parejas ordenadas, el despeje de la regla ($m$, luego $b$), dominio, rango,
  comprobación y **su gráfica**.
- **Generador nuevo**: `Recursos lety2E/puntos-recta-svg-math.py` — puntos sueltos con su recta
  guía, y el diagrama sagital (dos óvalos con flechas). La recta va **punteada a propósito**:
  cuando el dominio son sólo tres valores, la gráfica son los puntos, no la recta.

## 2026-09-07 (3) — Arranca Matemáticas 4: "Evaluación de funciones" (tema 1)

Empieza la migración del cuarto curso. Como en Math 3, **no hay LaTeX**: la única fuente son las
capturas (`~/Desktop/capturas/matematicas 4/`), 20 carpetas de las que **17 tienen material**
(13 transformación de funciones, 19 modelo matemático y 20 historia están vacías). Del CSV salen
**9 videos para 7 temas**; escalonada y dominio máximo llevan dos cada uno.

- **`math/matematicas-4/evaluacion-funciones.html`** (Tema 1) — video, apuntes, dos ejemplos,
  los **6 bloques** de ejercicios de las capturas con sus 48 resoluciones, y **4 bloques de
  extras** (32 evaluaciones nuevas, sin respuesta).
- **Las 57 respuestas verificadas con sympy** — las 48 de los bloques más las de los dos
  ejemplos. Las capturas de este tema salieron limpias: ni un error aritmético.
- **Único detalle**: el Bloque 6 deja $m(5) = \frac{4}{72}$ sin simplificar, aunque en los demás
  bloques sí se simplifica. Se publicó el paso completo hasta $\frac{1}{18}$, sin nota al pie.
- **Sección de Apuntes**, que Math 3 no llevaba: aquí las capturas sí traen texto de Lety a mano
  (qué es la regla de correspondencia y qué es la imagen) y se aprovechó tal cual.
- Los extras se numeran **Bloque 7 a 10**, continuando la cuenta de los ejercicios: llamarlos
  "Bloque 1 y 2" como en Math 3 chocaría con los bloques que ya trae la captura.
- **Herramienta nueva**: `Recursos lety2E/generador-paginas-math4.py`, hermano del de Math 3, con
  los ayudantes de este curso (tarjeta "dadas las funciones / encuentra", bloques de respuestas y
  video doble). De ahí salen los temas que faltan.
- El índice del curso dejó de ser una `.proximamente-card` y ya es rejilla con su primera card.
  En `math/index.html` la insignia de *próximamente* sigue puesta hasta que el curso avance.

## 2026-09-07 (2) — Se recortaron las tipografías: 104 → 78 KB por carga

Quitado KaTeX, el rubro más pesado del sitio pasaron a ser **las tipografías: 105 KB**, más que
todo lo demás junto. Herramienta nueva: `Recursos lety2E/subset-fuentes.py`.

**Dónde estaba la grasa.** DM Sans es una fuente **variable** con dos ejes: `wght` 100–1000 y
`opsz` (tamaño óptico) 9–40. El sitio sólo usa pesos **300–700**, así que medio eje era peso
muerto: recortarlo bajó el archivo de 61 a 41 KB. Playfair es estática (peso 900); ahí sólo se
recortaron caracteres.

**Dos decisiones conservadoras**, ambas tomadas midiendo y no a ojo:

1. **El eje `opsz` se conserva.** Fijarlo ahorraba 16 KB más, pero se midió que ensancha
   **10.2%** los números a 40 px de las tarjetas de `math/index.html`. Con el eje vivo el render
   es idéntico: la peor desviación en todo el sitio es **0.375 px en una línea de 568 px
   (0.066%)**, y Playfair queda en **cero** exacto.
2. **Se conserva el bloque Latin-1 completo (`À–ÿ`)** aunque hoy no se use entero. Cuesta ~8 KB
   más que recortar a lo mínimo, pero evita que un nombre como *Gödel* o *François* salga con una
   letra de otra fuente a media palabra cuando agregues contenido.

Los archivos `*-latin-ext.woff2` **no se tocaron a propósito**: con contenido en español su
`unicode-range` nunca coincide, así que jamás se descargan — no cuestan nada y quedan como red
de seguridad si algún día aparece un carácter raro.

| archivo | antes | ahora |
|---|---|---|
| `DMSans-normal-latin` | 61.1 KB | **41.1 KB** (−33%) |
| `PlayfairDisplay-normal-latin` | 21.9 KB | **18.9 KB** (−14%) |
| `PlayfairDisplay-italic-latin` | 21.3 KB | **18.5 KB** (−13%) |
| **por carga de página** | **104.3 KB** | **78.5 KB (−25%)** |

Verificado: **cero caracteres del sitio perdidos** en las tres fuentes, ningún elemento cae a
fuente del sistema, y las 239 letras y símbolos que el sitio usa siguen cubiertos.

- Los originales quedaron en `assets/fonts/originales/`. El script **siempre parte de ahí**, así
  que se puede volver a correr sin degradar la fuente recortando sobre lo ya recortado.
- **No hace falta correrlo al publicar un tema.** Sólo si cambian las fuentes o si aparece un
  carácter nuevo que salga con la letra equivocada.

---

## 2026-09-07 — Velocidad: se pre-renderizó KaTeX y las páginas bajaron 86%

Los alumnos seguían reportando lentitud. Lo primero fue medir, y la red **no era el problema**:
GitHub Pages responde en ~200 ms, todo va comprimido, no quedó ningún CDN y los facades de
YouTube del 2-sep funcionan. El peso era **JavaScript**.

`katex.min.js` pesa **74 KB comprimidos y 271 KB al parsear**, y se cargaba en las 67 páginas
con fórmulas — el 86% del peso de una página de tema. Además provocaba un parpadeo feo: el
alumno veía los `$$y = x^2$$` en crudo hasta que el JS terminaba y todo brincaba de golpe.

**La solución: pre-renderizar las fórmulas aquí, una sola vez.** Herramienta nueva en
`Recursos lety2E/prerender-katex.js` (Node). Convierte los `$...$` a HTML de KaTeX y quita el
`<script>`; se queda sólo `katex.min.css`, que sí hace falta. **63 páginas, 4157 fórmulas, cero
errores.** El LaTeX original no se pierde: KaTeX lo guarda en cada fórmula
(`<annotation encoding="application/x-tex">`), así que se puede recuperar y volver a correr.

Los simuladores (UNAM y COMIPEMS) **no se pre-renderizan** — arman las preguntas con JS desde
`data.js`, así que ahí no hay fórmulas en el HTML estático y quitarles KaTeX las rompería. El
script las detecta solo y las salta. A cambio, ahí KaTeX pasó a **cargarse bajo demanda**: su
`<main id="app">` arranca vacío, así que antes el alumno veía la pantalla en blanco hasta bajar
~128 KB. La pantalla de inicio no tiene ni una fórmula, así que KaTeX ahora se adelanta en
`requestIdleCallback` sin bloquear el primer pintado.

**Resultado (KB comprimidos que descarga el alumno):**

| | antes | ahora |
|---|---|---|
| página de tema típica | 86 KB | 16 KB |
| la más pesada (`recta-tangente`, 305 fórmulas) | 85 KB | 24 KB |
| simulador UNAM (antes de ver nada) | 128 KB | 52 KB |
| **promedio de las 65 páginas** | **81 KB** | **12 KB (−86%)** |

Dos cosas que se descartaron midiendo: el `nav.js` bloqueante **no cuesta nada** (baja en
paralelo con `style.css`, que ya bloquea el pintado de todos modos), y el archivo de 370 KB del
simulador offline es sólo un enlace de descarga — nadie lo abre como página.

- **Ojo al agregar temas nuevos**: hay que correr el pre-render antes de publicar
  (`node "Recursos lety2E/prerender-katex.js"`). Es idempotente, se puede correr sobre todo el
  sitio sin miedo. Está anotado en `CLAUDE.md`.
- Un detalle que costó encontrar: el escáner del script debe tratar `<` como etiqueta **sólo**
  si le sigue letra, `/`, `!` o `?` — igual que el navegador. Sin eso, una fórmula como
  `$x < 3$` se parte a la mitad y deja el `$` crudo en pantalla.
- Los `$` de `proporcionalidad.html` son **signos de peso** ($100, $250), no fórmulas. Lety los
  envolvió en `<span class="peso">$</span>` justo para que KaTeX no los emparejara; el
  pre-render los respeta igual.

---

## 2026-09-07 — Math 3: "Ecuación general de la elipse" (tema 19), armado desde cero

Las carpetas 19–23 de capturas siguen **vacías**, así que este tema **no viene de las hojas de
Lety**: se construyó entre los dos en el chat, con el molde de circunferencia y parábola.
Decisiones que tomó ella y que valen para los tres que faltan:

- **Datos de partida**: centro, vértices y focos. De ahí se leen $a$ y $c$; $b$ sale de Pitágoras.
- **Convención**: $a$ es siempre el semieje mayor, así que $a^2$ **cambia de lugar** según la
  orientación. Por eso el apunte muestra **las dos formas** de la canónica, no sólo la horizontal.
- **Horizontales y verticales mezcladas** en los ejercicios.
- **Sección de Apuntes separada del Ejemplo**, con las fórmulas y un dibujo donde se ve el
  **triángulo rectángulo** que forman $a$, $b$ y $c$ ($b$ y $c$ catetos, hipotenusa $a$).
- **Orden de la solución, definido por Lety**: datos → localizar los puntos en el plano →
  medir ahí $a$ y $c$ → calcular $b$ con Pitágoras → **ya con $b$** trazar la elipse → sustituir →
  comprobar. La gráfica dejó de ser ilustración final: va donde de verdad se puede trazar.
  Por eso cada resolución lleva **dos gráficas**.
- **Las medidas van en cotas separadas del eje**, con ganchos en los extremos (Lety mandó el
  croquis): puestas encima del eje se encimaban con los puntos.
- Antes de sustituir, una pill dice **"La elipse es horizontal/vertical, así que $a^2 = 25$ va
  debajo de $x$/$y$"**, y el $a^2$ va **resaltado en amarillo** dentro de la canónica.
- La **comprobación es con los dos vértices**, escritos antes de las cuentas.

Generador nuevo: `Recursos lety2E/elipses-svg-math.py` — la elipse con centro, vértices y focos,
la vista de sólo puntos con las cotas, y el dibujo del apunte con el triángulo.

**Tema 20, "Regreso de la elipse"**, mismo día y misma estructura, de vuelta: ecuación general →
agrupar y factorizar el coeficiente → completar los trinomios (ojo: lo que se suma del otro lado
es **el coeficiente por la mitad al cuadrado**, no la mitad al cuadrado a secas) → dividir para
llegar a la canónica → ahí $a^2$ es el denominador mayor y **su posición dice la orientación** →
$a$, $b$ y $c$ → centro, vértices y focos → gráfica → comprobación con los dos vértices. Los cinco
casos son **los mismos del tema 19 al revés**, igual que circunferencia y parábola.

## 2026-09-06 (3) — Matemáticas 3 completo: 18 temas armados desde las capturas

Se migró el curso entero en una sesión, **sin LaTeX**: la única fuente fueron las capturas
(`~/Desktop/capturas/matemáticas 3/`). Alcanzaron de sobra — las hojas de `resultados` traen
el procedimiento completo y la comprobación de cada ejercicio.

Los 18: sumas y restas, sustitución, gráfico, igualación, determinantes 2×2 y 3×3, cuadráticas
incompletas, fórmula general, trinomio cuadrado perfecto, gráfica de la cuadrática, productos,
factorización, desigualdades, regiones, y las cónicas de ida y vuelta (circunferencia y parábola).
**10 de los 18 tienen video** del CSV; los otros ocho van sin esa sección.

- **Un solo error en las capturas**: tema 7, Bloque 1, ejercicio 1 — la hoja da $x_2 = 5$ pero al
  factorizar $5x(x-2)=0$ la solución es $x_2 = 2$. Se publicó **la respuesta correcta y sin nota al
  pie**: Lety prefiere que la página quede limpia, la corrección no se anuncia. Todo lo demás (unas
  70 resoluciones) cuadró contra las capturas.
- **Los ejercicios extra los generé yo**: las capturas de Math 3 no traen extras. Van **10 por tema**
  (el mínimo que pide el banco de exámenes), verificados uno por uno con sympy o por determinante —
  solución entera y única salvo donde el caso pide lo contrario.
- **Cinco generadores de SVG nuevos**, guardados en `Recursos lety2E/`: rectas (dos en el mismo
  plano, para el método gráfico), parábolas (por vértice y por foco-directriz), rectas numéricas
  con intervalo, regiones (semiplano sombreado) y circunferencias. También quedó
  `generador-paginas-math3.py`, el armador de páginas que produjo los 18 archivos.
- **Bug de CSS que se repitió en cuatro páginas**: la regla que da formato a las etiquetas de las
  cajitas (`b | mitad | cuadrado`) estaba escrita como `.mitad-box span`, y eso alcanzaba también a
  los `<span>` internos que genera KaTeX: las fórmulas se desarmaban letra por letra. Va acotada a
  `> div > span:first-child`. **Si se copia una cajita de éstas a otro tema, cuidado con eso.**
- El índice del curso conserva el `.proximamente-nota`: **faltan 5 temas** (elipse, hipérbola e
  historia), cuyas carpetas de capturas están vacías. En cambio en `math/index.html` la card del
  curso **ya perdió su `pronto-badge`**: con 18 temas publicados el curso cuenta como abierto,
  aunque adentro siga la nota de los que faltan. También se corrigió ahí la descripción, que decía
  "Trigonometría, exponenciales y logaritmos" y no es lo que trae el curso.

## 2026-09-06 (2) — Math 3 arranca: "Método de sumas y restas" (tema 1)

**Math 3 no tiene LaTeX**: la única fuente son las capturas (`~/Desktop/capturas/matemáticas 3/`),
y son suficientes — traen `ejemplo`, `ejercicios` y `resultados`, y las de resultados vienen con
el procedimiento completo y la comprobación. Son 18 carpetas con contenido (temas 1–18, igual que
letymath.com); las carpetas 19–23 (elipse, hipérbola, historia) están **vacías**.

- **`math/matematicas-3/sumas-restas.html`** (Tema 1) — video, ejemplo, 4 ejercicios con sus
  resoluciones y 10 extras. Verifiqué la aritmética del ejemplo y de los 4 ejercicios: todo
  correcto, no hubo nada que corregir.
- **Los multiplicadores van como en su cuaderno**: sin `\times`, sólo el paréntesis — `(-5)` `(2)`
  a la izquierda y `(3)` `(4)` a la derecha, **fuera de la llave**, con el sistema en medio.
  Morado (#7B2CBF) los de la izquierda y magenta los de la derecha, amarrados por color con los
  títulos *Eliminamos x* / *Eliminamos y*. Lety pidió explícitamente que la `×` no aparezca:
  se confunde con la incógnita. **Aplica a todos sus cursos**, no sólo a este tema.
- **Sin sección de Apuntes**: las capturas de este curso no traen texto de apuntes y no se inventa.
- **Los 10 extras los generé yo** — las capturas de Math 3 no traen extras (a diferencia del LaTeX
  de Math 1 y 2). Son sistemas con solución entera única, verificados por determinante. Van en dos
  tarjetas de cinco, **sin numerar**: Lety rechazó el "Extra 1, Extra 2…" por ruidoso.
- Se corrigió la descripción del índice de Math 3: decía "trigonometría, exponenciales, logaritmos"
  y el curso es sistemas, cuadráticas, factorización, desigualdades y geometría analítica.

## 2026-09-06 — Los ejercicios extras quedan marcados como el banco de exámenes

Lety va a armar exámenes con **5 versiones por curso**. Se decidió que **los exámenes se
hacen y se guardan en el proyecto IEMS** (`4 Materiales y evaluación/`), no aquí: el repo
del sitio es público y ese material no se publica. De este lado solo se leen los reactivos.

Su criterio de evaluación: ~3 ejercicios por tema, uno de los que traen respuesta y dos de
los **ejercicios extra**. Con 5 versiones sin repetir, cada tema necesita **10 extras como
mínimo**. Conteo aproximado del banco actual: la mayoría alcanza (todo Math 5 trae 12+;
`operaciones-fracciones` 40, `operaciones-basicas` 36, `reglas-exponentes` 28), pero
`ecuaciones` (M1) **no tiene sección de extras**, `algebra-fracciones` (M2) tampoco, y
`expresiones-algebraicas` y `mcm-mcd` (M1) traen solo 8. Los temas con figuras hay que
contarlos a mano.

Que los extras estén publicados es **a propósito**: Lety quiere que sus alumnos sepan de
dónde sale el examen. Los extras nuevos se piden tema por tema, conforme prepare cada examen
— no se adelantan. Todo el contexto quedó en `Pendientes lety2E.md`.

## 2026-09-05 (6) — Math 2 completa: temas 13 y 14

Los dos que **no venían en el LaTeX** (su último documento trae dentro "Operaciones con
Fracciones", no lo que dice su encabezado). Se armaron de otras fuentes.

- **`math/matematicas-2/problemas-fracciones.html`** (Tema 13) — de la captura
  (`13 problemas con fracciones/`). Once problemas más la pregunta de apertura de Lety
  ("¿Cómo resolvemos un problema de fracciones?"), que se deja como está: es abierta y no
  lleva respuesta.
  **Las respuestas de este tema las calculé yo**, porque la captura no las trae: la guía
  dice que en ese caso se resuelven paso a paso. Están verificadas una por una, pero
  conviene que Lety les dé una pasada por si quiere otro camino de solución.
- **`math/matematicas-2/historia-matematica-griega.html`** (Tema 14) — de letymath.com,
  que lo tiene en texto (no hay captura; la carpeta `14 matematica griega/` está vacía).
  Investigación con siete preguntas, mismo patrón que "Sistemas de numeración" de Math 1.
  Sin KaTeX: no tiene una sola fórmula.
- Se retiró el `.proximamente-nota` del índice de Matemáticas 2: **el curso ya está
  completo, 14 de 14**.

---

## 2026-09-05 (5) — Math 2: "Proporcionalidad y regla de tres" (tema 12)

- **`math/matematicas-2/proporcionalidad.html`** (Tema 12) — apunte con la regla de tres
  directa y la indirecta, 4 ejemplos, 16 ejercicios en cuatro bloques con todas sus
  resoluciones y 16 extras. Verifiqué las 20 resoluciones del LaTeX: correctas. Lety
  **trunca** a dos decimales en vez de redondear (10.93, 26.66, 23.07, 48.38…) y es
  consistente en todas, así que se respetaron sus valores tal cual.
- **Caja de regla de tres** (`.rt-box`): el `\fbox` del LaTeX con las dos filas
  `A → B` / `C → X`. Aquí las flechas sí van: son la notación del método, no una
  explicación de más.
- **Los enunciados van sin KaTeX.** El signo de pesos suelto ("$250") haría que
  auto-render tomara desde ahí hasta el siguiente `$` y se comiera medio párrafo. Van en
  `<span class="peso">$</span>`, que aísla el nodo de texto; KaTeX queda sólo para las
  resoluciones. De paso la página carga menos.

---

## 2026-09-05 (4) — Math 2: "Semejanza de triángulos" (tema 11)

- **`math/matematicas-2/semejanza-triangulos.html`** (Tema 11) — apunte, cuatro ejemplos
  (seis proporciones, dos triángulos anidados y un problema de sombras), 6 ejercicios en
  dos bloques con sus resoluciones y 12 extras. Verifiqué las nueve resoluciones del
  LaTeX: todas correctas.
- **Tres figuras nuevas** (`tri3.py` en el scratchpad), porque el tema no es de triángulos
  rectángulos sueltos:
  - `oblicuo()` — triángulo con los tres lados etiquetados, para las proporciones. Los
    pares se dibujan con el mismo ápice y distinto tamaño, así se *ven* semejantes.
  - `anidado()` — el triángulo con la vertical interna. La base total va con línea de cota
    abajo y el tramo derecho justo bajo la base: en el LaTeX esas dos etiquetas viven en
    posiciones inconsistentes entre un ejercicio y otro, y sin la cota no se sabe cuál es
    cuál. La altura interna no se pone a mano, sale de la semejanza.
  - `recto()` — el par edificio/poste de los problemas de sombra.
- Los ejemplos conservan el paso de Lety de **"separando los triángulos"**: debajo de la
  figura anidada aparecen el grande y el pequeño por separado, que es donde se ve de dónde
  sale la proporción.

---

## 2026-09-05 (3) — Math 2: "Razones trigonométricas" (tema 10)

- **`math/matematicas-2/razones-trigonometricas.html`** (Tema 10) — apunte con seno,
  coseno y tangente, ejemplo resuelto (arranca con las dos preguntas de Lety: qué lado
  conoces respecto al ángulo, y qué función usar), 4 ejercicios con resoluciones y 6 extras.
- **Los triángulos ahora dibujan el ángulo.** El helper creció a `tri2()`: además de los
  lados, marca con un arquito morado el ángulo del vértice superior o el del inferior
  derecho, con su etiqueta ($35^\circ$, $\alpha$, $\beta$). Todo a escala real, calculada
  con la trigonometría del propio ejercicio.
- **Se corrigió una resolución del LaTeX.** En el ejercicio 1 venían intercambiados $x$ y
  $y$: respecto al ángulo de $42^\circ$, $x$ es el cateto opuesto, así que
  $x = 16\,Sen\,42^\circ = 10.70$ y $y = 16\,Cos\,42^\circ = 11.89$, no al revés. Es un
  desliz aislado — el ejemplo del tema y el ejercicio 2, que son la misma figura, lo hacen
  bien. Se publicó la correcta con una nota al pie de las respuestas (clase
  `.nota-correccion`, primera vez que se usa).

---

## 2026-09-05 (2) — Math 2: "Teorema de Pitágoras" (tema 9)

Lety mandó el LaTeX de Matemáticas 2 y con eso arranca el tramo que faltaba del curso
(temas 9 a 14). El primero ya está.

- **`math/matematicas-2/pitagoras.html`** (Tema 9) — mini apunte con el teorema y las tres
  razones trigonométricas, un ejemplo resuelto en tres pasos, 6 ejercicios, sus 6
  resoluciones y 12 extras en dos bloques. Verifiqué la aritmética de las seis
  resoluciones del LaTeX: correctas.
- **Los 20 triángulos son SVG inline generados a escala real** con un helper de Python
  (`tri.py` en el scratchpad de la sesión): ángulo recto abajo-izquierda, cateto vertical
  a la izquierda, hipotenusa de arriba-izquierda a abajo-derecha — la misma convención que
  las hojas de Lety. Relleno magenta 12 % y contorno sólido, como en `area-perimetro.html`.
- **Ojo con esto:** la primera versión salió con los triángulos invisibles. Un `<svg>` sin
  atributos `width`/`height` colapsa a 0×0 dentro de un grid o un flex — está advertido en
  la guía, y aun así pasó. El helper ahora los escribe siempre.
- **Las resoluciones van con un paso por renglón**, como en el LaTeX. La primera versión
  juntaba varios pasos en una línea y en 375 px la ecuación se salía del viewport (con
  `white-space: nowrap` no se parte). Un paso por renglón lo resuelve de raíz.

**El LaTeX de Math 2 trae dos duplicados** (header que no corresponde al contenido):
el documento del tema 1 tiene adentro el de jerarquía, y el último —encabezado
"13 problemas con fracciones / 14 matematica griega"— trae "Operaciones con Fracciones".
O sea que de ahí no salen los temas 13 ni 14. El 14 (historia griega) es texto puro y se
puede tomar de letymath.com; el 13 sólo tiene la captura.

Aparte: los ejercicios de Pitágoras en la captura eran 8, y dos estaban mal —el séptimo
daba los tres lados (8, 15, 5) y además era imposible. El LaTeX trae sólo 6 y ésos son los
que se publicaron.

---

## 2026-09-05 — Math 1 completa: se sube "Sistemas de numeración"

Lety pasó el doc LaTeX de Matemáticas 1 (temas 2 a 13) para ver si faltaba algo. Comparado
ejercicio por ejercicio contra el sitio: los 12 ya estaban publicados y coinciden, así que
de ahí no salía ningún tema nuevo.

La pista buena estuvo en **letymath.com**, el sitio viejo: su menú de Matemáticas 1 tiene
14 temas y lety2E tenía 13. De los dos candidatos, "divisibilidad" resultó ser el mismo
mcm/MCD que ya existe aquí (allá se llama distinto), y el faltante real era
**Sistemas de numeración**, que cierra el curso.

- **`math/matematicas-1/sistemas-de-numeracion.html`** (Tema 14). No es un tema de
  ejercicios sino una **investigación**, así que sigue el patrón de `historia-calculo.html`
  de Math 5: "De qué se trata" + dos bloques de puntos ("Los sistemas antiguos" /
  "El sistema hindú-arábigo"), sin sección de respuestas. El texto es el de letymath.com
  tal cual (sólo se acentuó "súper").
- **Sin KaTeX.** La página no tiene una sola fórmula, así que no carga el CSS ni los dos
  JS de KaTeX. Tres archivos menos por visita.
- Botón *siguiente* en `problemas-ecuaciones.html` y card en el índice del curso
  (🏛️, acento `#4A0080`, siguiendo la rotación).

**Nota para después:** en `expresiones-algebraicas.html` los ejercicios de lety2E no son
los del doc LaTeX ni los de letymath.com (allá son 5+5, aquí 4+4 y tres cambiados). Lety
prefiere cómo quedó aquí, así que se deja como está — queda anotado sólo para que no
sorprenda en una comparación futura.

---

## 2026-09-02 (3) — "Primeros pasos": segunda ronda con Lety

*(cierre del día)* Último recorte: en "Antes de empezar" se quitó el "síguelo y vas a ver
a dónde llega" — el resaltado amarillo ya invita solo a seguir el nombre. Y desde el sitio
de GICAIA el enlace de Recursos ya apunta directo a la guía (antes iba al índice de
Docencia) y perdió su nota de "en escritura"; el texto del enlace ya decía "Primeros pasos".

Ronda de recortes y dos cosas nuevas. La guía adelgazó bastante: Lety fue quitando todo
lo que explicaba de más y quedó sólo lo que se hace.

- **El nombre de ejemplo ahora se sigue con la vista.** `profelety`, resaltado en amarillo
  (`.nombre`, el mismo amarillo de las pills de Math), aparece seis veces y deja ver su
  recorrido: nombre → carpeta → cuenta → dirección → repositorio → la frase que le dictan.
  Se descartaron `lety2E` (existe, pero `lety2e.github.io` da **404**: el repo de Lety se
  llama `lety2E` y el sitio vive en `lety2e.com` por CNAME, o sea la versión avanzada que
  la guía todavía no enseña) y `letymath` (está libre y es su marca; publicarlo de ejemplo
  era regalarlo). También se verificó que **GitHub no acepta guion bajo** en el usuario,
  así que el `profe_lety` que Lety propuso las habría rebotado.
- **Paso 5 partido en "Lo que haces tú" / "Lo que le pides al agente"** (`.quien`). Era el
  único paso que mezclaba las dos cosas y por eso se leía raro. Ahora trae su frase para
  dictar, como los pasos 2 y 3.
- **No hace falta el conector de GitHub.** Lety preguntó; se verificó en la documentación:
  el conector es un MCP para la API (issues, PRs), mientras que publicar es `git`, que el
  agente ya corre solo. Lo único necesario es autorizar GitHub una vez desde el navegador
  — que es justo el recuadro rosa que ya estaba. Se le sumó ahí la línea de "puede que
  también te pida instalar algo que le falta a tu computadora; acéptalo".
- **Paso 4 y cierre, a lo mínimo.** Se fueron: leer el nombre en voz alta, el recuadro de
  la verificación del correo, "el nombre no es un detalle de forma", "la primera vez tarda
  uno o dos minutos" y el cierre largo.
- **Se acabó el "diez minutos, y si no sale, el jueves".** Era una de las dos reglas de
  escritura del encargo original (permiso explícito de parar en cada atorón); Lety la fue
  quitando renglón por renglón y al final también salió el "trae el jueves lo que se haya
  atorado". Quedan dos recuadros rosas que sólo describen qué va a pasar. Consecuencia
  consciente: la guía ya no promete acompañamiento, se sostiene sola.

---

## 2026-09-02 (2) — Docencia estrena guía: "Primeros pasos"

La primera pieza real de Docencia. Le habla a **dos compañeras del IEMS, profesoras de
matemáticas**, que nunca han hecho una página: montar la carpeta, dictarle el contexto al
agente, crear la cuenta de GitHub y publicar. Termina cuando abren su dirección desde el
celular y ahí está su tema. Se publicó y luego se trabajó en vivo con Lety toda una ronda
de ajustes; esto es el estado final del día.

- **Se llama "Primeros pasos"**, no "Aula propia" como decía la card en `próximamente`.
  La card del índice ya es enlace real (`docencia/primeros-pasos.html`).
- **Instalar NO es por terminal.** El primer borrador daba por hecho la instalación por
  línea de comandos y marcaba ese momento como "aquí es normal atorarse". Se verificó en
  la documentación: **la app de escritorio de Claude ya incluye Claude Code** — no hay que
  instalar Node ni el CLI, no hay terminal. Se quitó ese aviso y el paso 1 se reescribió
  al flujo real: abrir la app, pestaña **Code**, escoger la carpeta.
- **Un solo nombre para todo.** Idea de Lety y es la que ordena la guía: el nombre del
  sitio es el nombre de la carpeta, la usuaria de GitHub y la dirección. Los criterios para
  escogerlo (corto, sin acentos, fácil de deletrear) pasaron al paso 4 como revisión final,
  justo antes de que ese nombre quede fijo.
- **El archivo de contexto se nombra: `CLAUDE.md`.** Única excepción a la regla de "ningún
  nombre de archivo en la guía", y se la gana: es el archivo que van a seguir tocando cuando
  la guía ya no exista. Verificado en la documentación: **Claude Code lee `CLAUDE.md`, no
  `AGENTS.md`** — con AGENTS.md solo, el contexto no se lee y no avisa.
- **El ejemplo de contexto es un sistema de tres colores**, no un archivo ajeno que se
  copia: turquesa = de qué trata el bloque o la pregunta a pensar (no se escribe);
  rosa = el ejemplo, lo que cambian por lo suyo; negro = se dicta tal cual. El turquesa usa
  `#008878` (el de `.nb-apr` en `style.css`), porque el `--T` de marca no da contraste para
  texto chico. "Cómo quiero que me hables" es el único bloque sin ejemplo, a propósito.
- **Paso 3, "Tu página"** (antes "Los archivos"): incluye la opción de partir de material
  propio — apuntes, ejercicios, fotos del pizarrón — metiéndolo a la carpeta. Evita de paso
  que el agente invente ejercicios y respuestas.
- **Quedan tres puntos marcados como "aquí es normal atorarse"** (permiso a los archivos,
  verificación de correo de GitHub, autorización de GitHub desde el navegador), ya sin
  título: el recuadro rosa marca solo.
- **El paso 5 (el repositorio) se escribió a media altura a propósito:** dice lo que la
  pantalla les va a pedir (repositorio nuevo, nombre exactamente igual a su dirección,
  público) pero nunca dónde clickear. Los botones de GitHub cambian; lo que pide, no.
- **La suscripción va escrita**, seca, en "Antes de empezar" — unos 20 dólares al mes, cada
  quien la suya, y el plan gratuito no la incluye.

Sin CDNs ni imágenes: HTML y el `style.css` global, con un bloque `<style>` propio.
Verificada en 375×812 sin desbordes.

---

## 2026-09-02 (1) — El sitio abre rápido: fuera los embeds de YouTube

Los alumnos reportaron que la página tardaba en abrir. La causa medida no era el
contenido matemático sino los **`<iframe>` de YouTube**: cada uno arrastra ~1 MB de
JavaScript de Google y **retiene el evento `load`** de la página. En una página de
tema con 2 videos, servida desde `localhost` (o sea sin excusa de red), el navegador
seguía cargando a los **5.4 s** y el evento `load` no llegaba nunca. Ahora esa misma
página termina de cargar en **~110 ms** y no toca YouTube hasta que el alumno da clic.

- **Facade de video (`.yt-lite`).** Los 21 iframes del sitio (10 temas de Math,
  3 covers de Cantos, 3 relatos, más la plantilla de la skill) se cambiaron por un
  `<button class="yt-lite" data-yt="ID">`. Muestra la miniatura de YouTube (~8 KB) y
  **sólo al dar clic** inserta el iframe real, ya con `autoplay=1` para que el video
  arranque solo — un clic, igual que antes. Lógica al final de `footer.js` (que todas
  las páginas ya cargaban), estilos `.yt-lite` en `style.css`.
- Se usa la miniatura `mqdefault` y no `hqdefault`: la segunda pesa el doble, viene en
  4:3 con barras negras y al recortarla a 16:9 se comía el encabezado de los videos.
- Es un `<button>` de verdad: se abre con Enter/Espacio y el lector de pantalla anuncia
  "Reproducir video: <título>". Sin internet queda la tarjeta oscura con el botón ▶.
- **Hero de la portada: 300 KB → 31 KB en celular.** Estaba guardado a 2528 px cuando el
  sitio nunca lo muestra a más de 1200. Ahora hay `hero-nocturno-800.webp` (31 KB) y
  `-1600.webp` (76 KB) con `srcset`, respaldo `.jpg`, y `width`/`height` para que no
  brinque el layout. Los dos archivos viejos se borraron.
- **Fuentes: un viaje de red menos.** `style.css` traía las tipografías con
  `@import url('assets/fonts/fonts.css')`, lo que obliga al navegador a bajar el CSS
  entero *antes* de enterarse de que existen las fuentes. Las `@font-face` ahora van
  pegadas dentro de `style.css`; `assets/fonts/fonts.css` se queda sólo como referencia
  para actualizarlas.
- **Retratos de Lupián** recomprimidos: 43 → 26 KB y 41 → 25 KB, mismo tamaño en pantalla.
- Lo que se revisó y **ya estaba bien**: KaTeX y las tipografías son self-hosted (cero
  CDNs), GitHub Pages sirve todo con gzip (`style.css` viaja en 12 KB, KaTeX en 77 KB) y
  `font-display: swap` ya estaba puesto. El HTML pesado de los simuladores no es problema
  porque va comprimido.
- Las reglas quedaron escritas en `CLAUDE.md` (§ Velocidad de carga) y en la skill
  `letymath-html`, para que los temas nuevos ya nazcan con el facade y no con un iframe.
- Verificado en el navegador a 375×812: portada, Cantos, un relato vertical y tres temas
  de Math — miniaturas correctas, clic reproduce, KaTeX renderea, cero errores de consola.

## 2026-09-01 (12) — Mate 5 reordenado al orden de letymath.com
- **El índice de Mate 5 pasa al orden del sitio viejo**, que es el que Lety quiere (lo mandó en
  capturas de `letymath.com/matemáticas-5`). Historia del cálculo queda al final, como allá.
- Cambios de fondo respecto al orden de publicación: **recta tangente sube del 20 al 11**
  (queda pegada a las reglas de derivación, que es donde se usa la derivada como pendiente),
  máximos y mínimos y área máxima suben a 12 y 13, y **derivada por definición baja al 19**.
- Dos temas del doc **no existen en el sitio viejo**: `suma-riemann` y `derivada-definicion`.
  Derivada por definición quedó en la 18, donde el sitio viejo tiene *"Derivada / Integrales"*,
  y **suma de Riemann de penúltima (19), como pidió Lety** — primero se había metido en la 16,
  entre integrales definidas y área bajo la curva, y ella la movió al final.
- El script quedó guardado como `Recursos lety2E/reordenar-temas-math.py`: se edita su lista
  `ORDEN` y él solo recoloca las cards, recalcula la rotación de color, reescribe los números
  de Tema, regenera los botones prev/next y verifica que no queden enlaces rotos ni desfases.
  Reordenar el curso a mano son 20 cards + 20 números + 38 botones; con esto es cambiar
  una lista.
- El reordenamiento se hizo con un script, no a mano: recoloca las 20 cards recalculando la
  rotación de color (magenta · turquesa · morado por posición), reescribe los 20 números de
  Tema y regenera los 38 botones prev/next tomando la etiqueta del `<h1>` de cada página.
- Verificado por script: 20 cards, 0 enlaces rotos, 0 desfases entre orden del índice, número
  de Tema y cadena prev/next.

## 2026-09-01 (11) — Matemáticas 5 queda completo
- **Temas 18, 19 y 20:** `puntos-criticos.html` (criterio de la segunda derivada),
  `optimizacion-areas.html` (área máxima de un rectángulo con perímetro dado) y
  `recta-tangente.html` (el más grande del curso: 6 desarrollos, 12 tablas de valores y
  6 gráficas). Ninguno tiene video.
- **Con esto el índice de Mate 5 llega a 20 cards** y la cadena anterior/siguiente va completa
  de reglas básicas hasta recta tangente. Verificado por script: 0 enlaces rotos, 0 desfases
  entre el orden del índice, la cadena prev/next y el número de Tema de cada página.
- **Las figuras de optimización** (el rectángulo con lados $y$ y $x+n$) son SVG hechos con
  `rect.py`; llevan clase `.figura-rect` para que no hereden el `max-width: 260px` de las
  gráficas y salgan gigantes.
- **En recta tangente la recta va en turquesa (`#00A896`) y la parábola en magenta**, para que
  se distingan de un vistazo; el punto de tangencia va en morado y más grande. Las 6 gráficas,
  las 12 tablas y los 6 desarrollos se generan con `gen_tangente.py` a partir de los parámetros
  $(a, h, k, m, b, x_1, y_1)$ de cada caso — nada se tecleó a mano, así que las tablas no
  pueden desincronizarse de la gráfica.
- Verificación de las gráficas por geometría, no por captura: se mide que el punto de tangencia
  caiga sobre la recta (distancia 0 en las 6) y sobre la parábola (menos de 1.6px).
- Verificadas a mano las resoluciones de los tres temas: 4 de puntos críticos, 4 de
  optimización y 5 de recta tangente. Todas correctas.
- Verificado en 375×812: cero errores de KaTeX, nada se sale, ninguna tabla desborda.

**Pendiente para Lety:** el orden del índice es el orden en que se publicaron (el del doc), no
el didáctico. Si quiere moverlos —historia y derivada por definición al principio, velocidad
media entre las aplicaciones— es una pasada aparte que toca las 20 cards, los 20 números de
Tema y los 38 botones de la cadena.

## 2026-09-01 (10)
- **Temas 16 y 17:** `area-bajo-curva-p1.html` (bajo una recta) y `area-bajo-curva-p2.html`
  (bajo una parábola). Ambos con tabulación, gráfica y resolución analítica.
- **Primeras gráficas SVG de Mate 5.** Las del doc venían en TikZ, que no sirve en el sitio;
  se rehicieron como SVG inline con el helper `svgplot.py` del scratchpad, respetando la paleta
  de `CLAUDE.md` (cuadrícula `#E0C4BC`, ejes `#7B5A50`, curva magenta, puntos `#1A0828`,
  región con magenta al 15%) y la regla de 1 cuadro = 1 unidad.
- **Truco de verificación que sí sirve:** en vez de mirar la captura —el panel no permite
  recortar—, se mide por JS la distancia de cada punto marcado al trazo de la curva. Así se
  cachó que en la parábola el punto $(0,11)$ quedaba a 59px de la curva, porque el dominio del
  trazo empezaba en $x=0.4$. Ahora los seis puntos caen sobre la curva (menos de 1.7px).
- **Ojo con los heredoc de bash al armar estas páginas**: sin comillas en el delimitador, un
  `$[a,\,b]` se interpreta como expresión aritmética y revienta. Los cuerpos van con
  `<<'BODYEOF'` (comillado) y la gráfica se inyecta después sobre un marcador `@@GRAFICA@@`.
- Verificadas a mano las 5 resoluciones de P1 y las 5 de P2, más los 2 ejemplos: todas correctas.
- Verificado: cero errores de KaTeX, nada se sale.

## 2026-09-01 (9)
- **Temas 14 y 15:** `integrales-definidas.html` (regla de Barrow) y `suma-riemann.html`
  (la integral como límite de sumas de rectángulos, con el desarrollo algebraico completo).
  Sin video ninguno.
- **Corrección publicada en Riemann, ejercicio 2** ($\int_2^6 (3-x^2)dx$): el doc trae
  `-16/n` donde va `-4/n` —el término constante $-1$ multiplicado por $\Delta x = 4/n$ da
  $-4/n$, no $-16/n$— y arrastra ese `16` a la línea siguiente. Con los números del doc las
  constantes suman $-208/3$, no el $-172/3$ que él mismo da como resultado. **El resultado
  final del doc es el correcto** (comprobado integrando directo: $-172/3 \approx -57.33$);
  lo que estaba mal eran dos pasos intermedios. Aquí se publican corregidos. **Conviene
  arreglarlo también en el doc de Lety.**
- Los decimales del doc venían truncados en vez de redondeados (31.66, 46.66 para $95/3$ y
  $140/3$). Aquí van redondeados: 31.67 y 46.67.
- Verificadas a mano las 6 resoluciones de integrales definidas y las 4 de Riemann, más los
  2 ejemplos.
- Verificado en 375×812: cero errores de KaTeX, nada se sale.

## 2026-09-01 (8)
- **Temas 11, 12 y 13:** `derivada-definicion.html`, `historia-calculo.html` e
  `integrales-indefinidas.html`. Ninguno tiene video.
- **Historia del cálculo no lleva sección de respuestas**: en el doc son 12 preguntas de
  investigación (biografías, la disputa Newton–Leibniz, hasta hacer un meme), no ejercicios con
  resultado. La página lo dice de entrada para que nadie busque un desplegable que no existe.
- **Ojo con `.ej-line` cuando el contenido es texto y no fórmula.** `style.css` le pone
  `white-space: nowrap` a todo `.ej-line` de Math —para que las ecuaciones no se partan a la
  mitad—, así que un párrafo dentro de un `.ej-line` se saldría de la pantalla sin cortar nunca.
  Historia usa una clase propia `.pregunta`, con `white-space: normal` y alineada a la izquierda.
- Integrales indefinidas: el formulario va como 8 `.regla-card` (como la tabla de senos y
  cosenos) en vez de tabla; los ejercicios y las respuestas a ancho completo, porque cada
  integral trae seis o siete términos.
- Verificadas a mano las 8 resoluciones de derivada por definición y las 6 de integrales,
  más los 3 ejemplos: todas correctas.
- Verificado en 375×812: cero errores de KaTeX, nada se sale en las tres.

## 2026-09-01 (7)
- **Nacen los Temas 9 y 10: `regla-cadena-p1.html` y `regla-cadena-p2.html`.** Sin video ninguno.
  P1 con potencias y raíces de polinomios (3 ejemplos, 6 resoluciones, 4 bloques de extras);
  P2 con trigonométricas, logaritmos y raíces (4 ejemplos, 8 resoluciones, 2 bloques de 8 extras).
- **El doc titula la P2 "Cálculo Diferencial: Derivadas"**, que no dice nada: su contenido es
  cadena con cos, sen, ln y raíces. Aquí se publica como "Regla de la cadena (P2)".
- La notación `\sqrt[3]{...}^2` del doc (radical con exponente colgando) se escribe aquí como
  `\left(\sqrt[3]{...}\right)^2`: es lo mismo, pero sin la ambigüedad visual de un superíndice
  pegado al radicando.
- A partir de aquí las páginas se arman con dos ayudantes en el scratchpad —`css-tema.txt` (el
  bloque `<style>` común) y `mkpage.sh` (ensambla head + CSS + cuerpo)—, más `addcard.py` y
  `addnext.py` para el índice y la cadena prev/next. Bajan el riesgo de que se desincronicen
  los estilos entre temas.
- Verificado en 375×812: cero errores de KaTeX, nada se sale en ninguna de las dos.

## 2026-09-01 (6)
- **Nace `math/matematicas-5/regla-cociente-p2.html` — Tema 8.** Sin video. La misma regla del
  cociente, ahora con senos, cosenos y tangentes. 2 ejemplos, **3 bloques de ejercicios (4, 4 y 6)
  con sus 14 resoluciones** y 2 bloques de 6 extras. Es el tema más cargado del curso hasta ahora.
- **Las respuestas van a ancho completo, una debajo de otra (`.bloques-1`), no en columnas.**
  Aquí el numerador de cada derivada es la resta cruzada sin simplificar —cosas como
  `(-7 sen x)(2x² - 4 sen x) - (7 cos x)(4x - 4 cos x)`—; en dos o tres columnas no cabía.
  Los ejercicios sí van en 3 columnas, porque ahí las fracciones son cortas.
- Verificadas a mano las **14 resoluciones** y los 2 ejemplos: todas correctas.
- Verificado en 375×812 y 1200px: nada se sale. En escritorio el peor caso mide 482px contra
  528px de card. Cero errores de KaTeX.
- Con esto quedan cerrados los cuatro pares de reglas: producto P1/P2 y cociente P1/P2.

## 2026-09-01 (5)
- **Nace `math/matematicas-5/regla-cociente-p1.html` — Tema 7.** Sin video (no está en el CSV).
  Apunte con las dos fórmulas ($f = u/v$ y su derivada), el ejemplo del doc, 2 bloques de 3
  ejercicios con sus resoluciones y **3 bloques de 6 extras**.
- Primera página del sitio que usa **`.bloques-3`** (los extras vienen en tres bloques en el doc,
  y en 2 columnas quedaba uno huérfano). Colapsa a 2 columnas abajo de 980px y a 1 abajo de 700.
- `.ej-line` con `line-height: 2.6` en vez de 2.4: aquí cada ejercicio es una fracción apilada
  (numerador y denominador), que pide más aire que una raíz.
- Verificadas a mano el ejemplo y las 6 resoluciones: todas correctas. Estas son las más largas
  del curso hasta ahora (cuatro pasos con la resta cruzada expandida).
- Verificado en 375×812 y en 1200px: **nada se sale** — la fórmula más ancha mide 245px contra
  341px de caja en móvil, y en escritorio el peor caso queda con 13px de holgura. Cero errores
  de KaTeX.

## 2026-09-01 (4)
- **Nace `math/matematicas-5/regla-producto-p2.html` — Tema 6.** La misma regla del producto,
  ahora con trigonométricas, logaritmos, exponenciales y raíces. Sin video (no está en el CSV).
  4 ejemplos en 2×2, 2 bloques de 5 ejercicios con sus resoluciones y 2 bloques de 6 extras.
- **El doc escribe `\sin`; aquí va `\operatorname{sen}`**, como en `senos-cosenos.html` — el sitio
  usa la notación en español. Vale para todos los temas que vengan: hay que traducirlo al pasar
  del doc al HTML.
- Verificadas a mano las 10 resoluciones y los 4 ejemplos: todas correctas. Ojo con dos que el
  doc deja sin simplificar del todo (`∛(x⁵)/x` y `x^{5/3}/x`) — son correctas, sólo no reducidas;
  se respetaron tal cual porque así las enseña Lety.
- El índice de Mate 5 llega a **6 cards** y la cadena prev/next va completa de reglas básicas
  hasta aquí.
- Verificado en 375×812: la fórmula más ancha mide 154px contra 315px de caja. Cero errores
  de KaTeX.

## 2026-09-01 (3)
- **Nace `math/matematicas-5/regla-producto-p1.html` — Tema 5.** Con video (sí estaba en el CSV:
  `6rf8dzKTXvU`), apunte de la regla $f = uv \implies f' = u'v + uv'$, el ejemplo del doc,
  2 bloques de 3 ejercicios con sus resoluciones y 2 bloques de 6 extras.
- Se nombró `regla-producto-p1` (no `regla-producto`) porque el doc trae una **P2** con las
  mismas reglas aplicadas a trigonométricas y logaritmos; así el par queda parejo.
- **Las resoluciones van en una sola línea, como en el doc** — Lety lo pidió así.
  (Primero se habían partido en dos renglones en la costura de la regla, `u'v` arriba y
  `+ uv'` abajo, suponiendo que las expansiones de ocho términos no cabrían en el celular.
  **La suposición estaba mal medida**: sin corte, la línea más ancha de las resoluciones mide
  188px contra 320px de card en 375×812. Caben de sobra. Regla para la próxima: medir el ancho
  real de la fórmula —el `.base` que renderiza KaTeX, no el `.katex-html`, que siempre reporta
  el ancho del contenedor— antes de partir nada.)
- Verificadas a mano las 6 resoluciones y el ejemplo: todas correctas, ninguna corrección
  que publicar.
- Verificado en 375×812 y escritorio: nada desborda, cero errores de KaTeX.

## 2026-09-01 (2)
- **Nace `math/matematicas-5/raices.html` — Tema 4, derivadas de raíces.** Sin video (no está en
  el CSV, y no es error). Apunte de una sola regla ($\sqrt[n]{x^m} = x^{m/n}$), 3 ejemplos en
  columna triple, 2 bloques de 6 ejercicios, sus respuestas y 2 bloques de extras.
- Los ejemplos usan una `.ejemplo-grid` de **3 columnas** (las otras páginas de Mate 5 usan 2):
  los tres desarrollos del doc son angostos y caben bien; colapsan a 1 columna abajo de 860px.
- En las respuestas, cada resolución **arranca con la raíz original** antes de la forma con
  exponente. El doc empezaba ya convertido; así el alumno ve de dónde salió. También se dejó el
  paso de la resta de exponentes (`x^{2/3 - 3/3}`) en los 12, porque el doc lo traía sólo en
  la mitad.
- **Bug global de móvil, arreglado en `style.css`:** las media queries de Math ponían font-size
  tanto a `.katex` como a `.katex-display`, y como KaTeX anida `.katex` **dentro** de
  `.katex-display`, los dos se multiplicaban: las fórmulas en `$$` salían a ~8px en vez de ~13px
  (un 36% más chicas de lo previsto). Se agregó
  `body[data-section="math"] .katex-display > .katex { font-size: 1.21em }` en las dos media
  queries (1.21em es el valor propio de KaTeX). **Afecta a todas las páginas de Math con
  display math** — no sólo a raíces: velocidad media, por ejemplo, ya se lee bien en el celular.
- Verificado en 375×812 y en escritorio: sin overflow de página, ninguna card desborda, cada
  `\sqrt` muestra su barra superior completa y cero errores de KaTeX.
- Vuelve el botón "Derivadas de raíces →" al pie de senos y cosenos, ahora sí con destino real.

## 2026-09-01
- **Mate 5: dos páginas huérfanas quedaron enlazadas.** `velocidad-media.html` y
  `senos-cosenos.html` ya estaban hechas y subidas, pero el índice sólo mostraba una card
  (reglas básicas), así que nadie las alcanzaba. Ahora tienen su card, con la rotación de color
  del curso: magenta · turquesa · morado.
- **Se cerró la cadena anterior/siguiente**: reglas básicas → velocidad media → senos y cosenos.
  Reglas básicas no tenía ningún botón (hubo que agregarle también el CSS de `.topic-nav-btns`
  a su `<style>` inline) y velocidad media no tenía el de siguiente.
- **Se quitó un enlace roto ya publicado**: senos y cosenos remataba con "Derivadas de raíces →"
  apuntando a `raices.html`, que no existe — daba 404 en vivo. Vuelve cuando publiquemos raíces.
- Arreglado un renglón cortado en el ejemplo a) de velocidad media: `x(2) = 16(2) − (2)² =
  32 − 4 = 28` se salía del borde de la card y tapaba el resultado. Se partió en dos líneas del
  `aligned` (sin perder ningún paso).
- Verificado en escritorio y en 375×812: sin overflow horizontal en ninguna de las tres.
- Se revisó el `.docx` de Matemáticas 5 que pasó Lety: son **20 LaTeX independientes** pegados
  uno tras otro, en orden de captura y no didáctico. No hay temas duplicados por error — los
  títulos que se repiten son pares P1/P2 (uno algebraico, el otro trigonométrico). El único
  título engañoso es "Cálculo Diferencial: Derivadas", que en realidad es **cadena P2**.

## 2026-08-31
- **Enlace al canal de WhatsApp al pie de los índices de Math** (Mate 1, 2 y 5 — los cursos que
  hoy tienen temas). Va después de "Más temas en construcción", como pastilla discreta a
  propósito: es un aviso, no un tema, y no debe competir con las cards del curso.
- Estilo nuevo `.enlace-canal` / `.canal-wrap` en `style.css` (junto a `.enlace-grupo`, que es el
  otro enlace que sale del sitio). **Sin el verde de WhatsApp** — se queda en el palette:
  turquesa, el color de sección de Math. Flecha ↗ porque lleva fuera, `target="_blank"`.
- Verificado en escritorio y en 375×812: el texto se parte en dos renglones y no desborda.

## 2026-08-26
- **Nace `docencia/` — cuarta sección del menú principal.** Es la primera sección del sitio que
  **le habla a colegas docentes** y no a estudiantes: ahí va la metodología de Lety (sus flujos,
  sus prompts, cómo construye un sitio de clase con agentes de IA). Va en el menú y no dentro de
  Apuntes justamente por eso — todo lo de Apuntes (COMIPEMS, ingreso a licenciatura) le habla a
  alumnos. El nombre sigue el patrón del sitio: una palabra, el oficio (`math`, `lupian`,
  `apuntes`, `docencia`).
- **Lo que urgía:** el sitio de GICAIA ya está publicado y su pestaña Recursos enlaza a
  `lety2e.com/docencia` — el enlace estaba **roto**. Ya no: `/docencia` redirige a `/docencia/`
  y ahí hay una página real que dice qué viene.
- Cinco toques: carpeta `docencia/index.html` · `docencia` sumada al bloque académico de
  `style.css:65` (turquesa + títulos morados, igual que Math y Apuntes) · alta en `SECTIONS` y
  `ROOT_LINKS` de `nav.js` · card morada en el `index.html` raíz (+ su meta-descripción) ·
  nueva regla `.apunte-card.pronto` en `style.css` para cards sin destino real.
- **Decisiones de Lety:** color académico (no magenta — Docencia es trabajo, no arte);
  la portada se queda en grid de 3 columnas, así que Docencia cae sola en el segundo renglón
  (3+1); y la card de **"Aula propia"** ya se ve, marcada `próximamente`, para que el colega que
  llegue de GICAIA sepa qué esperar. Como todavía no hay destino, la card es un `<div>`
  (nunca `href="#"`, por la regla del `CLAUDE.md`).
- Las páginas de Docencia usarán `style.css` global + `data-section="docencia"` (patrón de Math),
  **no** el patrón self-contained de Apuntes: esas son self-contained porque llegan de fuera como
  artefactos sueltos; las de Docencia se escriben aquí y así heredan nav, footer y mobile-safety.
- Quedó escrita en `CLAUDE.md` la **regla de propiedad** que explica por qué esto vive aquí y no
  en GICAIA: *"lo que hace una persona sola es de esa persona y vive en su sitio; lo que sale de
  una sesión del grupo es del grupo"*. Así ninguna sesión futura propone mudarla.
- Verificado en local (`serve.py`): `/docencia` → 301 → 200, nav con las cuatro secciones,
  h1 morado, y en 375×812 y 360×800 sin overflow horizontal y la card dentro del contenedor.

### Segunda pasada, el mismo día
- **La portada pasó a 2×2.** Lety lo repensó y tiene razón: con cuatro secciones el 3+1 dejaba
  a Docencia sola y descolgada. `.root-cards-grid` ahora es `repeat(2, 1fr)` con `max-width: 720px`
  centrado, así que Math·Lupián arriba y Apuntes·Docencia abajo, todas del mismo ancho. Si algún
  día son 5 o 6 secciones, se vuelve a `repeat(3, 1fr)` (queda anotado en el CSS).
- **Card de ida y vuelta hacia GICAIA** al final del índice de Docencia, bajo el grupo "El grupo".
  Clase nueva `.enlace-grupo`: fondo oscuro (`--dark`, la misma superficie del nav y el footer),
  filo magenta que se vuelve turquesa al pasar el cursor, y la flecha ↗ en la etiqueta. Se ve
  **distinta a propósito** — es la única card del sitio que lleva fuera. Trae el nombre completo
  del grupo, qué es, y la regla de propiedad dicha para el lector.
- **Hallazgo al revisar el sitio de GICAIA:** el enlace de su pestaña Recursos no se llama
  "Docencia" sino **"Aula propia — la guía para arrancar"** y apunta a `lety2e.com/docencia`.
  O sea que promete la guía, no el índice. Mientras la guía siga en `próximamente`, el colega
  que llega de allá encuentra menos de lo que el enlace ofrecía. Anotado en `CLAUDE.md` y en
  pendientes. (También descubrimos que GICAIA enlaza a `lety2e.com/math`.)
- Verificado: 2×2 real (350px cada card, dos renglones), la card de GICAIA con `target="_blank"`
  y `rel="noopener"`, sin overflow horizontal en 375, 420 ni 1100 de ancho.

---

## 2026-08-05
- **KaTeX ahora vive en el repo: el sitio dejó de depender del CDN.** Se descargó KaTeX 0.16.9
  (css + js + auto-render + 40 archivos de fuente en `woff2`/`woff`, ~940 KB) a
  **`assets/katex/`**, y se reapuntaron los **28 archivos** que lo cargaban desde
  `cdn.jsdelivr.net`: los 24 temas de Math, los 2 simuladores (3 archivos) y la plantilla de
  la skill `letymath-html` — así los temas nuevos ya nacen apuntando a la copia local.
  Salió de una duda de Lety sobre qué necesita internet; el detonante fue que
  `simulador-unam-offline.html` **se llamaba "offline" pero jalaba KaTeX del CDN**.
- No se tocó el CSS de KaTeX (queda idéntico al de upstream, más fácil de actualizar).
  Se omitieron los `.ttf` a propósito: los navegadores toman el primer formato que soportan
  y ninguno pide `.ttf` teniendo `woff2`/`woff` (solo lo usaría un Android anterior a 2013).
- Verificado: **cero referencias al CDN** en todo el repo, 131 fórmulas dibujadas en
  `operaciones-fracciones.html`, ninguna sin renderizar, sin errores de consola y sin
  peticiones fallidas. El **simulador COMIPEMS quedó 100% sin recursos externos**.
- **Las tipografías también se trajeron al repo.** Playfair Display y DM Sans se
  self-hostean desde **`assets/fonts/`** (6 archivos `woff2`, 184 KB) con sus reglas
  `@font-face` en `assets/fonts/fonts.css`; `style.css:6` dejó de importar de
  `fonts.googleapis.com`. Sólo se guardaron los subsets **latin y latin-ext** (el sitio es en
  español; cyrillic y vietnamese nunca se usarían). DM Sans es fuente variable, así que un
  solo archivo cubre los pesos 300–700.
- **Hallazgo:** el simulador COMIPEMS traía su propio `@import` de Google Fonts, pero estaba
  **colocado después del bloque `:root`** — el navegador ignora un `@import` que no va al
  inicio, así que llevaba tiempo cayendo a fuentes del sistema sin que se notara. Se cambió
  por un `<link>` a `assets/fonts/fonts.css`: ahora **sí** se ve con Playfair Display.
  Se revisó todo el repo en busca de otros `@import` mal colocados — no hay más.
- **Estado final:** la portada, los índices y los dos simuladores cargan **cero recursos
  externos**. Lo único que sigue saliendo a internet son los **iframes de YouTube** en los
  temas de Math que traen video — eso no tiene arreglo, un video embebido necesita conexión.
- **Apuntes reorganizado por nivel escolar y estrenada la subsección de ingreso a la UNAM.**
  El índice de Apuntes ahora se parte en bloques (`<h2 class="apuntes-grupo">` + su
  `.apuntes-grid`): **Ingreso a licenciatura (UNAM · Área 2)** e **Ingreso a bachillerato
  (COMIPEMS)**. Separarlos fue petición de Lety — son niveles distintos y estaban revueltos.
  El patrón es extensible: un grupo nuevo se crea copiando ese par de líneas.
- **Publicadas 9 guías en `apuntes/ingreso-licenciatura/`** (fuente: proyecto Artefactos,
  carpeta `Ingreso licenciatura`), agrupadas en Empieza aquí · Ciencias · Humanidades ·
  Formularios · Practicar: temario, biología, química, español, literatura, historia de
  México, historia universal y formularios de física y geografía.
- Venían como **artefactos sueltos**: sin `data-section` y sin un solo link interno — quien
  llegaba se quedaba atorado sin salida. Se les inyectó una barra `.l2e-volver`
  (breadcrumb `Inicio › Apuntes › Ingreso UNAM › <materia>`, prefijo propio para no chocar
  con el CSS de cada página). **No se tocó su contenido.** Helper del script en el
  scratchpad de la sesión.
- **Los dos simuladores NO se movieron** — sus URLs siguen vivas; la separación por nivel se
  resolvió en la agrupación del índice, no moviendo carpetas.
- **Retirados** `mcp.html`, `compresion.html` y `segunda-guerra-mundial.html` (a Lety dejó de
  convencerle el formato). Ojo: el tercero era la **referencia canónica** del patrón zoom
  N1–N5, así que —idea de Lety— en vez de dejarlo solo en el historial de git se guardó en
  `Recursos lety2E/formato-apunte-zoom-N1-N5 (segunda-guerra-mundial).html`, disponible para
  copiar componentes pero sin card en ningún índice. `CLAUDE.md` y `apuntes/Templete-apuntes.md`
  apuntan ahí. Las guías nuevas usan otro formato, así que no se ascendió ninguna a "referencia"
  del template viejo.
- **Dejados fuera a propósito:** `Guias-unam.html` (636 KB, duplica el contenido de las
  individuales) y `hist mex.html` / `hist mex 2.html` (borradores viejos; el segundo además
  está roto, muestra `{sel?.title}` sin procesar). `simulador-unam-area2.html` ya estaba
  publicado — md5 idéntico al del sitio.
- **Hueco conocido:** de las 9 materias de Área 2 faltan páginas completas de **Física** y
  **Geografía** (solo hay formulario); el contenido de Física sí existe dentro de `Guias-unam.html`.
- Verificado en local: los 13 links de ambos índices dan 200, cero referencias colgando a los
  borrados, sin errores de consola y **sin overflow horizontal en 390 y 360** de ancho.

- **Sitio caído y recuperado — el dominio ya no apuntaba a GitHub Pages.** `lety2e.com`
  resolvía al CDN de Hostinger (`92.112.198.67` / `147.79.120.81`) por un registro
  **ALIAS `@` → `lety2e.com.cdn.hstgr.net`**, y ese servidor tenía el certificado SSL
  **vencido desde el 27-jun-2026**: el navegador bloqueaba la entrada. Encima Hostinger
  servía una versión **vieja** del sitio (botones `/escritos/`, `/musica/`, `/la-turquesa/`).
- **Arreglo (lo hizo Lety en el panel de Hostinger, guiada paso a paso):** borrados el
  `ALIAS @` y el `CNAME www → www.lety2e.com.cdn.hstgr.net`; agregados los 4 registros A de
  GitHub Pages (`185.199.108/109/110/111.153`, TTL 3600) y `CNAME www → lety2E.github.io`.
  Se conservó el `A ftp` (inofensivo). Hostinger advierte al añadir varios A con el mismo
  nombre: es round-robin normal, GitHub lo requiere — se confirma sin problema.
- **Verificado:** DNS propagado, `https://lety2e.com` → 200, `http` → 301 a https,
  `www` → 301 al dominio raíz, y las tres secciones (`math/`, `lupian/`, `apuntes/`) cargan.
  Certificado nuevo de Let's Encrypt emitido por GitHub, vigente al 8-sep-2026.
- **Enforce HTTPS** ya estaba activo en Settings → Pages; el aviso "DNS Check in Progress"
  es la re-verificación normal tras el cambio y se resuelve solo.
- **Causa raíz (confirmada por Lety):** ya **no renovó el hosting** de Hostinger, solo paga
  el dominio. Al caducar el plan, Hostinger dejó de renovar el certificado de su CDN — venció
  el 27-jun-2026 — pero el `ALIAS` seguía apuntando ahí. O sea: **el sitio llevaba caído
  desde finales de junio**, no fue algo reciente.
- **Lo que esto cambia hacia adelante:** el certificado ahora lo emite y **renueva GitHub
  automáticamente**, así que el problema de SSL vencido no se repite. Y como no hay plan de
  hosting activo, **nadie va a reponer el `ALIAS`**: la configuración de hoy es estable.
  En Hostinger solo queda el **registro del dominio**, que sí se debe seguir renovando: vence
  el **2-feb-2027** y Lety dejó activada la **renovación automática** ese mismo día.
- Nota: el cambio **no tuvo relación** con el renombre de la carpeta local (`lety2E 2` →
  `lety2E`); el repo estaba limpio y sincronizado todo el tiempo.

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
