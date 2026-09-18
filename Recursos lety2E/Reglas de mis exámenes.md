# Reglas de mis exámenes

> Cómo le gustan los exámenes a Lety. Se fue construyendo con ella el 7 y 8 de
> septiembre de 2026, armando los de Matemáticas 1. Este documento es la semilla
> del proyecto nuevo de exámenes; lo que aquí dice **decidido por Lety** es regla,
> lo que dice **propuesta** todavía no lo revisa.

## La esencia

Un examen suyo es **puro reactivo**: una cuadrícula de tarjetas, cada una con el
nombre del tema en negritas y sus ejercicios debajo. Nada más. Y los ejercicios
**no se inventan**: salen de las páginas de temas de su sitio, que es público a
propósito, para que los alumnos sepan de dónde va a salir el examen.

## 1. El formato de la hoja

**Decidido por Lety.**

- **Sin encabezado**: ni nombre, ni grupo, ni fecha, ni plantel, ni logo.
- **Sin instrucciones**: el título del tema es la instrucción.
- **Sin numeración** de ejercicios (los cuadros sí, desde el 17-sep-2026; ver abajo).
- **Sin puntaje**, ni por tema ni total.
- **Sin espacio rayado** para operaciones: se resuelve en hoja aparte.
- Arriba a la derecha, chiquito, **solo el identificador**: `Matemáticas 1a`.
- **Sin pestañas de color** en las tarjetas: una barra sólida por tema gasta
  tinta de más al fotocopiar. El nombre del tema va en negritas y ya.
- **Todo en negro sobre blanco. Ni un color** (8-sep-2026). El examen se imprime
  y se fotocopia por decenas: el negro gasta menos tinta y sale limpio. Los
  rosas del sitio —la letra `#3D2525` y el borde `#E0C4BC`— salían grises y
  lavados al fotocopiar; ahora la letra y el borde son negros, y el borde bajó
  de 1.5 a 1 px porque el negro pesa más que el rosa.
- Las **figuras** llegan del sitio con su tinta de color y en el examen se pasan
  a escala de grises: cuadrícula clarita, ejes gris medio, todo lo demás negro.
  El relleno conserva su transparencia, así que un triángulo queda apenas gris.
- **Cada versión cabe en UNA hoja carta**: puede sobrar espacio, pero no se
  puede exceder (ver §8).
- Se ve **igual que los ejercicios de su sitio**: mismas tarjetas, misma
  tipografía, mismo KaTeX, mismo aire entre renglones — sólo que sin color.
- **Letra a 12pt y figuras a 110px** (17-sep-2026). Lety imprimió la primera
  hoja a 10pt y dijo que *"los triángulos casi no se notan las expresiones"* y
  que *"hay espacio para distribuir mejor y aprovechar el espacio de una
  cuartilla"*. Se subió la letra, las figuras y el aire entre renglones
  (`--renglon` 2.5); las seis versiones siguen cabiendo en una hoja al 86 %.
- **Los cuadros van numerados, los ejercicios nunca** (17-sep-2026): `1.
  Operaciones básicas`, `2. Área y perímetro`… en el orden en que aparecen en
  la hoja, para poder nombrarlos al calificar. *"Podríamos numerar los cuadros
  (nunca los ejercicios), tal vez al lado del título."*

Corrección textual de Lety cuando el primer intento llevaba encabezado,
instrucciones, numeración y puntaje: *"no has captado la esencia de mis
exámenes"*.

### Diferencias necesarias con el sitio

- En el sitio las fórmulas largas hacen scroll horizontal. En papel no hay
  scroll, así que **se parten en dos renglones con sangría francesa**.
- Cada ejercicio va en su propio `.ej-line`. Sin eso, dos ejercicios cortos se
  pegan en el mismo renglón, porque los `<span>` de KaTeX son inline.

## 2. De dónde salen los reactivos

**Decidido por Lety.**

- De las páginas publicadas del sitio (`lety2e.com/math/matematicas-N`), nunca
  inventados aquí. Es a propósito que estén publicados.
- Se probó completar con ejercicios propios los temas a los que no les alcanzaba
  y **se dio marcha atrás**: si el ejercicio no está publicado, el alumno no lo
  pudo practicar.
- Cuando a un tema le faltan reactivos, **se agregan en el sitio**, no en el
  examen. Los nuevos se calcan de los publicados, molde por molde, y se
  verifican resolviéndolos.
- **El examen manda** (17-sep-2026): si a un tema no le alcanzan los resueltos
  o los extras para las seis versiones, **se escriben** — resueltos con su
  respuesta completa en *Ejercicios*, extras sin respuesta en *Ejercicios
  extra 1*. Así se cerró Matemáticas 1: Monomios (dos bloques de cada lado),
  Gráfica con tabulación (tres resueltas), Pendiente y ordenada (tres
  resueltas), Área y perímetro (un resuelto) y Ecuaciones con ángulos (un
  resuelto y un extra, con figura).

## 3. La unidad de selección es el bloque

**Decidido por Lety.** El bloque del sitio **es** el tema: sus renglones
recorren los distintos tipos de ejercicio de ese tema, siempre en el mismo
orden. Los bloques son paralelos entre sí (el renglón 3 es el mismo tipo en
todos), y por eso sirven para versionar.

Hay tres formas de tomar de un bloque, y **cada tema usa la suya**:

| Modo | Qué hace | Ejemplo |
|---|---|---|
| **bloque entero** | el bloque completo entra al examen | Operaciones básicas: 1 bloque de ejercicios + 1 de extras = 12 ejercicios |
| **por renglón** | se toma un renglón de cada bloque | Jerarquía: uno de cada bloque de ejercicios y uno de cada bloque de extras = 4 |
| **cruzado** | los bloques son dos tipos; cada versión lleva un tipo resuelto y el *otro* tipo de extra, alternando | Gráfica con tabulación (pendiente ±), Pendiente y ordenada (ordenada ±) |
| **ejercicios sueltos** | reparto plano | los temas que todavía no se definen |

**Lety quiere mezcla de tipos** (17-sep-2026): que en cada versión al alumno le
toquen tipos distintos, y que entre resueltos y extras se crucen. Cuando un
tema tiene dos tipos claros (pendiente positiva/negativa, con/sin binomio al
cuadrado, base 10/otras bases), los bloques se separan por tipo y el examen
toma de los dos. **Los bloques van en el mismo orden en los dos lados**
(Bloque 1 y Bloque A el mismo tipo, Bloque 2 y Bloque B el otro): el modo
cruzado se apoya en eso.

**La mezcla varía por tema y la decide Lety**: a veces uno resuelto y dos
extras, a veces uno y uno, según lo pesado que sea el tema.

Regla que se sigue en todos los modos: **ningún ejercicio se repite entre
versiones**, y cuando un tema aporta varios ejercicios, cada uno viene de un
molde distinto (a un mismo alumno no le tocan tres veces la misma forma).

## 4. Los bloques se agrupan por tipo

**Decidido por Lety.** Dos maneras, según el tema:

- **Un bloque por tipo**: Bloque 1 con los seis del tipo A, Bloque 2 con los
  seis del tipo B. Se usa en Jerarquía de operaciones.
- **Bloques mezclados**: cada bloque lleva mitad de cada tipo, alternados. Se
  usa en Ecuaciones.

**Expresiones algebraicas cambió de bando el 17-sep-2026**: Lety pidió un
bloque por tipo (Bloque 1 y A sin binomio al cuadrado, Bloque 2 y B con él) y
que el examen tome un resuelto sin cuadrado + un extra sin + un extra con. Al
reordenar ejercicios hay que **reordenar también sus resoluciones**, para que
sigan correspondiendo.

## 5. Ejercicios extra 1 y extra 2

**Decidido por Lety.** Idea suya, para que el alumno sepa qué estudiar mirando
la página, sin que se lo digan:

- **Ejercicios extra 1**: de aquí sale el examen.
- **Ejercicios extra 2**: práctica, no entra nunca.

La página es la fuente de verdad: el generador lee de "extra 1" y jamás del 2.
Si el tema no tiene la separación, usa "Ejercicios extra" como siempre. Así no
hay dos listas que mantener sincronizadas.

**Desde el 17-sep-2026 es regla general, decidida por Lety**: *"los extras
que se usan para las versiones están como Ejercicios extra 1; los demás pueden
ser extras 2"*. En todos los temas cerrados la sección que entra al examen se
llama **"Ejercicios extra 1"**; donde sobran reactivos hay además un
**"Ejercicios extra 2"** de práctica. Donde todos entran (Operaciones básicas,
Monomios, Expresiones, Ecuaciones con ángulos) solo existe la 1.

Lo mismo aplica a los ejercicios con resolución: en Expresiones algebraicas hay
dos bloques resueltos y **solo el primero entra al examen**; el segundo queda de
práctica resuelta.

## 6. El examen lleva todos los temas

**Decidido por Lety** (8 de septiembre de 2026). Se descartó la idea de partir
cada versión en dos secciones, una exentable y otra no. **El examen incluye
todos los temas del corte**, porque es también para los alumnos que faltaron y
no juntaron participaciones. Lo de "exentable" era, en realidad, la observación
de que sus alumnos suelen exentar los últimos temas; de ahí quedó el corte
entre el primer examen y el segundo (§10), no una partición del examen.

## 7. Las resoluciones se escriben sobre la marcha

**Decidido por Lety** (8 de septiembre de 2026). El diseño tiene dos lados: en
**lety2e.com/math** el alumno tiene los *Ejercicios* **con respuesta** para
practicar y los *Ejercicios extra* **sin respuesta**, que son los que se evalúan;
en el **sitio de exámenes**, que es solo de Lety, cada versión está dos veces —
en blanco para imprimir y **resuelta para calificar**.

Por eso: **los *Ejercicios extra* de lety2E nunca llevan respuesta**. Si a un
tema hay que agregarle reactivos, se agregan ahí sin resolución. Y de ahí sale el
trabajo: como de esos extras sale casi todo el examen, Así que las resoluciones **no se recogen, se escriben** — y se escriben **conforme hagan
falta**, no de una sentada: cuando se cierra un tema o se arma una materia, se
resuelve lo que ese paso necesite.

**Y sí puede implicar cambiar el sitio**: si al resolver sale que a un tema le
falta material o que un ejercicio degenera, se corrige en `math/` — que ahora
está en la misma carpeta, así que es el mismo trabajo. Ojo con la regla de las
dos secciones: los reactivos nuevos van en *Ejercicios extra* y **sin
resolución**.

Cada resolución nueva **se verifica resolviéndola**, como se hizo con los 18
ejercicios de Ecuaciones.

## 8. El acomodo de la hoja

**Decidido por Lety**, con su vocabulario: *"una estrategia para hacerlos caber
es usar minipages, así podemos hacer de diferentes tamaños los minipages"*.

La hoja se arma **por filas**. En cada fila los temas se reparten el ancho según
un peso: los de fórmulas largas van a media hoja, los cortos de a tres. Una
tarjeta puede además partir sus ejercicios en columnas internas (Operaciones
básicas, con sus 12 reactivos cortos, va en tres columnas).

Los temas se **emparejan por altura** para que no queden huecos. En Matemáticas 1
eso bajó el desperdicio de 182 a 66 píxeles.

**Al cambiar los contenidos cambian las alturas**: el acomodo hay que volver a
mirarlo cada vez — de eso se encarga `medida.py`, aquí abajo.

### Una hoja por examen, y adentro el orden da igual

**Decidido por Lety** (8 de septiembre de 2026): *"que quepan en hoja tamaño
carta, aunque sobre espacio pero que no se exceda"*, y *"ya cómo se acomoden
esos temas no importa que no estén ordenados, con que estén los
correspondientes"*.

O sea, dos reglas:

- **Cada versión cabe en una hoja carta.** Que sobre espacio no importa; que se
  pase, sí — la impresora suelta una segunda hoja con dos tarjetas huérfanas.
- **Dentro del examen los temas van como convenga.** Lo único que se respeta es
  el reparto entre los dos exámenes (§10): los primeros temas en el primero, los
  que siguen en el segundo. Por eso las filas se emparejan por altura sin
  cuidar el orden del sitio.

Esto **sustituye** a la regla anterior (*"no me pongas un último tema en la
primera hoja"*), que era para cuando un examen se iba a dos hojas. Ahora el
corte que importa es el de los exámenes, no el de las hojas.

**Cómo se sabe si cabe.** `medida.py` calcula la altura de cada versión con las
medidas reales del CSS y lo dice al generar:

    Examen 1 Matemáticas 1a: 19.1 de 26.1 cm de hoja (73%)

Si pasa del 92% avisa que va al tope, y si pasa del 100% grita **¡NO CABE!**. Al
8 de septiembre de 2026 el Examen 1 va al 73% y el Examen 2 al 36%, así que hay
aire de sobra. Si algún día se pasa, las palancas son, en este orden: reacomodar
las filas, bajar `--renglon` en `generar.py`, o mover un tema al otro examen.

(La hoja **resuelta** sí puede irse a dos páginas, y no importa: es la copia de
Lety para calificar, no la que se reparte.)

## 9. Las versiones

**Decidido por Lety.**

- Son **seis versiones**, que es lo que dan de sí los seis bloques de Operaciones
  básicas.
- Se identifican con **letra corrida**: `Matemáticas 1a` a `1f` para el primer
  examen, `1g` a `1l` para el segundo. Las letras no se repiten entre exámenes,
  así cada hoja repartida en el salón tiene identificador único y corto.
- El identificador va **arriba a la derecha**.

## 10. Cómo se parte el curso

**Decidido por Lety.** En general **son dos exámenes por semestre**: el primero
se lleva la primera parte de los temas y el segundo los que siguen (8-sep-2026).
Matemáticas 1 se evalúa así: el primero con los nueve primeros temas en el orden
del sitio, el segundo con los cuatro restantes. El corte es por orden de la página y **no coincide con los cortes del
PAP**, cosa decidida a propósito.

## 11. Lo que hay que cuidar en el sitio

Cosas que salieron al armar los exámenes y que conviene revisar en cada tema:

- **Reactivos duplicados entre bloques.** Operaciones básicas tenía nueve, y con
  seis versiones a un alumno le habría tocado la misma raíz dos veces en la
  misma hoja. Su bloque 12 era casi una copia de piezas de los otros.
- **Resoluciones faltantes.** Ecuaciones tenía seis ejercicios y solo cuatro
  resoluciones publicadas.
- **Ejercicios que aparecen en "Ejercicios" y otra vez en "Ejercicios extra".**
- **Bloques que no alternan** los tipos cuando deberían.
- **Ejercicios sin `.ej-line`**, que se pegan de a dos en un renglón cuando el
  bloque es corto.

## 12. Lo que falta decidir

- **Los cuatro temas del Examen 2 de Matemáticas 1**, todavía con reparto
  provisional: Reglas de exponentes, mcm y MCD, Lenguaje algebraico y
  Problemas de ecuaciones. Lety decidió el 17-sep-2026 dejarlos para cuando
  toque ese examen. Para Reglas de exponentes quedó sobre la mesa la propuesta
  de 4 por versión (1 resuelto + 1 extra de cada tipo: base 10 y otras bases);
  no la revisó.
- **Matemáticas 5** es lo que sigue (es materia de este semestre): la primera
  parte de sus cuadros, tema por tema, con el mismo trato.
- **Matemáticas 2**, completo en el sitio y sin tocar.

## 13. Estado al 17 de septiembre de 2026

**Examen 1 de Matemáticas 1: cerrado.** Los nueve temas definidos por Lety y
las seis versiones completas, al 80 % de la hoja. El PDF para imprimir
(`pdf.py`) va a `~/Downloads`.

| Tema | Modo | Por versión | Qué se escribió el 17-sep |
|---|---|---|---|
| Operaciones básicas | bloque entero | 12 | — |
| Jerarquía de operaciones | por renglón, uno y uno | 4 | — |
| Ecuaciones | uno resuelto y uno de cada bloque extra | 3 | — |
| Monomios | bloque entero (como Operaciones) | 10 | Bloques 5-6 resueltos y 11-12 extra |
| Expresiones algebraicas | un bloque por tipo; 1 resuelto sin cuadrado + 1 extra sin + 1 con | 3 | — (reacomodo) |
| Gráfica con tabulación | cruzado por signo de la pendiente | 2 | 3 resueltas con pendiente positiva |
| Pendiente y ordenada | cruzado por signo de la ordenada | 2 | 3 resueltas con ordenada negativa |
| Área y perímetro | 1 resuelto + 1 extra 1 | 2 | el sexto resuelto |
| Ecuaciones con ángulos | 1 resuelto + 1 extra 1 | 2 | el sexto resuelto y el sexto extra |

Examen 2 (los cuatro restantes): sin definir, con reparto provisional.

## 14. Cómo le gusta a Lety trabajar esto

Salió el 17-sep-2026, cuando retomó los cuadros diciendo *"ando algo perdida"*
y *"me siento un poco saturada"*:

- **Un tema a la vez, en el orden de la página del curso**, y no pasar al
  siguiente hasta cerrar el anterior. Nada de tablas con los trece temas de
  golpe.
- **Mostrarle cómo está el tema** (qué bloques tiene, qué tipos, cuántos
  ejercicios da hoy) y **dejar que ella decida** el reparto. Ella lo dice con
  sus palabras ("uno resuelto y uno de extras 1", "tres y tres"); el asistente
  lo traduce a receta.
- **Enseñarle los ejercicios nuevos antes de meterlos**, y luego **mostrárselos
  en el navegador** (preview local) antes de publicar.
- **Publicar tema por tema** —página, generador, cuadros y bitácora en el mismo
  commit— para que ella lo vea en el sitio de inmediato. Cuando pregunta *"¿ya
  subiste los cambios?"* también quiere los cuadros regenerados.
- Si el asistente pregunta algo técnico (p. ej. cómo escribir un despeje con
  coeficiente negativo), **explicarlo con el ejemplo concreto y las dos
  opciones**; ella escoge ("variado").

## Dónde está el material

Desde el 8 de septiembre de 2026 todo vive **dentro de este mismo proyecto**, `lety2E`.

- Generador: `cuadros/generador/` — `extraer.py` lee las páginas de `math/`, `banco.py` arma
  el banco y guarda la receta de cada tema, `seleccion.py` reparte las versiones,
  `acomodo.py` decide qué lleva cada examen y cómo se acomoda la hoja (y revisa que
  ningún tema se quede fuera), `medida.py` calcula si cabe en la hoja, `resoluciones.py`
  arma el banco de resoluciones, `generar.py` escribe los exámenes autocontenidos,
  `sitio.py` escribe la sección `cuadros/` y `pdf.py` junta las versiones de un examen en
  un PDF (una por hoja) en `~/Downloads`. Se corren desde esa carpeta.
- El sitio de exámenes: `cuadros/`, servido en **lety2e.com/cuadros** (no enlazado desde el
  nav). Cada versión, dos veces: en blanco para imprimir y resuelta para calificar.
- Exámenes listos para imprimir, autocontenidos: `~/Desktop/IEMS/4 Materiales y
  evaluación/Exámenes/Matemáticas 1/`, y ahí los sigue escribiendo `generar.py`.
- Los temas de donde salen los reactivos: `math/matematicas-1/` — **aquí mismo**, así que ya
  no hay regla de "solo lectura": agregar los extras que falten y regenerar es un solo
  trabajo, en una sola sesión. Al hacerlo, respeta el manual del sitio (`CLAUDE.md`).
