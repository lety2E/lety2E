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
- **Sin numeración** de ejercicios.
- **Sin puntaje**, ni por tema ni total.
- **Sin espacio rayado** para operaciones: se resuelve en hoja aparte.
- Arriba a la derecha, chiquito, **solo el identificador**: `Matemáticas 1a`.
- **Sin pestañas de color** en las tarjetas: una barra sólida por tema gasta
  tinta de más al fotocopiar. El nombre del tema va en negritas y ya.
- Se ve **igual que los ejercicios de su sitio**: mismas tarjetas, misma
  tipografía, mismo KaTeX, mismo aire entre renglones.

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
| **ejercicios sueltos** | reparto plano | los temas que todavía no se definen |

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
  usa en Expresiones algebraicas (tres sin cuadrado y tres con cuadrado) y en
  Ecuaciones.

Cuando el sitio traía los bloques desordenados (todos los del tipo A y luego los
del B), **se reordenaron en el sitio** para que alternen. Al reordenar
ejercicios hay que **reordenar también sus resoluciones**, para que sigan
correspondiendo.

## 5. Ejercicios extra 1 y extra 2

**Decidido por Lety.** Idea suya, para que el alumno sepa qué estudiar mirando
la página, sin que se lo digan:

- **Ejercicios extra 1**: de aquí sale el examen.
- **Ejercicios extra 2**: práctica, no entra nunca.

La página es la fuente de verdad: el generador lee de "extra 1" y jamás del 2.
Si el tema no tiene la separación, usa "Ejercicios extra" como siempre. Así no
hay dos listas que mantener sincronizadas.

**Solo se parte donde sobra material.** Donde los extras alcanzan justo,
partirlos no diría nada. Y en Operaciones básicas, que tiene seis bloques y el
examen usa seis, se dejaron juntos a propósito.

Lo mismo aplica a los ejercicios con resolución: en Expresiones algebraicas hay
dos bloques resueltos y **solo el primero entra al examen**; el segundo queda de
práctica resuelta.

## 6. El examen lleva todos los temas

**Decidido por Lety** (8 de septiembre de 2026). Se descartó la idea de partir
cada versión en dos secciones, una exentable y otra no. **El examen incluye
todos los temas del corte**, porque es también para los alumnos que faltaron y
no juntaron participaciones. Lo de "exentable" era, en realidad, la observación
de que sus alumnos suelen exentar los últimos temas; de ahí quedó la regla del
corte entre hojas (§6), no una partición del examen.

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
mirarlo cada vez. Si ya no cabe, la regla de Lety es **irse a dos hojas antes
que apretar más**.

### Cuando son dos hojas, el corte respeta el orden de los temas

**Decidido por Lety** (8 de septiembre de 2026). El emparejado por altura puede
reacomodar los temas **dentro de una hoja**, pero **no a través del corte**: la
primera hoja se lleva los primeros temas en el orden del sitio y la segunda los
que siguen. En palabras suyas: *"no me pongas un último tema en la primera
hoja."*

Por qué importa: sus alumnos suelen exentar los últimos temas con
participaciones, así que la segunda hoja es la que muchos ya traen ganada. Si un
tema tardío se cuela arriba, la hoja deja de leerse como el avance del curso.

**Ojo con el acomodo de hoy.** El Examen 1 de Matemáticas 1 todavía cabe en una
hoja, así que no lo incumple, pero su primera fila empareja *Operaciones
básicas* (tema 1) con *Ecuaciones con ángulos* (tema 9). El día que ese examen
pase a dos hojas —y va para allá, conforme se cierren los temas pendientes— hay
que **rehacer las filas** para que el corte quede limpio.

## 9. Las versiones

**Decidido por Lety.**

- Son **seis versiones**, que es lo que dan de sí los seis bloques de Operaciones
  básicas.
- Se identifican con **letra corrida**: `Matemáticas 1a` a `1f` para el primer
  examen, `1g` a `1l` para el segundo. Las letras no se repiten entre exámenes,
  así cada hoja repartida en el salón tiene identificador único y corto.
- El identificador va **arriba a la derecha**.

## 10. Cómo se parte el curso

**Decidido por Lety.** Matemáticas 1 se evalúa en **dos exámenes**: el primero
con los nueve primeros temas en el orden del sitio, el segundo con los cuatro
restantes. El corte es por orden de la página y **no coincide con los cortes del
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

- **Los temas que siguen con reparto provisional** (propuesta del asistente, sin
  revisar): Monomios, Gráfica con tabulación, Pendiente y ordenada, Área y
  perímetro, Ecuaciones con ángulos, Reglas de exponentes, mcm y MCD, Lenguaje
  algebraico y Problemas de ecuaciones.
- **Matemáticas 2 y 5**, que están completos en el sitio y todavía no se tocan.

## 13. Estado al 8 de septiembre de 2026

Cerrados y dando las seis versiones completas:

| Tema | Modo | Ejercicios por versión |
|---|---|---|
| Operaciones básicas | bloque entero | 12 |
| Jerarquía de operaciones | por renglón, uno y uno | 4 |
| Ecuaciones | uno resuelto y uno de cada bloque extra | 3 |
| Expresiones algebraicas | igual que Ecuaciones | 3 |

Sin definir, corriendo con reparto provisional: los nueve restantes. De esos,
**Área y perímetro** y **Ecuaciones con ángulos** ya no alcanzan para la sexta
versión, y **mcm y MCD** cae a un solo ejercicio.

## Dónde está el material

Desde el 8 de septiembre de 2026 todo vive **dentro de este mismo proyecto**, `lety2E`.

- Generador: `cuadros/generador/` — `extraer.py` lee las páginas de `math/`, `banco.py` arma
  el banco y guarda la receta de cada tema, `seleccion.py` reparte las versiones,
  `acomodo.py` decide qué lleva cada examen y cómo se acomoda la hoja, `resoluciones.py`
  arma el banco de resoluciones, `generar.py` escribe los exámenes autocontenidos y
  `sitio.py` escribe la sección `cuadros/`. Se corren desde esa carpeta.
- El sitio de exámenes: `cuadros/`, servido en **lety2e.com/cuadros** (no enlazado desde el
  nav). Cada versión, dos veces: en blanco para imprimir y resuelta para calificar.
- Exámenes listos para imprimir, autocontenidos: `~/Desktop/IEMS/4 Materiales y
  evaluación/Exámenes/Matemáticas 1/`, y ahí los sigue escribiendo `generar.py`.
- Los temas de donde salen los reactivos: `math/matematicas-1/` — **aquí mismo**, así que ya
  no hay regla de "solo lectura": agregar los extras que falten y regenerar es un solo
  trabajo, en una sola sesión. Al hacerlo, respeta el manual del sitio (`CLAUDE.md`).
