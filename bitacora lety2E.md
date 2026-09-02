# Bitácora — lety2E

> Registro de lo que vamos haciendo en el sitio. Lo más reciente arriba.
> (Los pendientes van en `Pendientes lety2E.md`, no aquí.)

---

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
