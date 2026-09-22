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

## El método (22-sep-2026)

**Decidido por Lety**, al revisar Mate 5 tema por tema: *"aunque es variable, en general los
ejercicios resueltos y los extras 1 me dan el banco de las preguntas, y dependiendo de los
ejercicios, si son más elaborados o no, sobre la marcha voy decidiendo cuántos ejercicios
tendrá la versión y de esos cuántos de resueltos y cuántos de los extras"*.

O sea, por tema:

1. **El banco es la página**: *Ejercicios* (resueltos) + *Ejercicios extra 1*. Todo lo que
   está ahí entra y cada ejercicio sale en una sola versión. *Extra 2* es repaso: nunca entra.
   Por eso **si sobran resueltos, bajan a extra 2** en el bloque de su tipo, sin respuesta
   (Lety, 22-sep-2026, por el Bloque 4 de Producto P2: *"la regla dice que los ejercicios
   resueltos más los extras 1 es el banco de preguntas; ese bloque puede llevarse a los
   extras 2 donde le corresponda"*).
2. **Se deciden dos números**: cuántos resueltos y cuántos extras lleva cada versión. Los pone
   Lety según lo elaborado del tema — cortos y mecánicos, más (Raíces 3 + 3); de mucho
   proceso, menos (Producto P1 1 + 1).
3. **La cuenta sale sola**: con seis versiones, la página necesita 6 × cada número. Si faltan,
   se escriben en el molde de la página y se verifican (§2).
4. **El 6 manda**: o hay **bloques de 6** y cada versión toma uno de cada bloque (Mate 5), o
   hay **6 bloques** y cada versión toma un bloque entero (Operaciones básicas en Mate 1).
5. **Si hay tipos, se mezclan**: bloques por tipo en el mismo orden en los dos lados (1 ↔ A) y
   a cada versión le tocan tipos distintos (modos `cruzado` y `rotado`, §3).
6. **Siempre hay extra 2**: *"de pasada se podría hacer los extras 2 cuando no hay, hacer
   algunas tandas de ejercicios"*. Si un tema no tiene repaso, se escribe **una tanda por tipo**
   (de 4, sin respuesta) al revisarlo. Raíces y Producto P2 ya la tienen (22-sep-2026).

Lety lo resumió así: *"sólo sabiendo cuántos tipos de ejercicios considero yo, y cuántos de
resueltas y cuántos de extras 1"*. Para arrancar un tema nuevo basta preguntarle **si tiene
tipos** y **cuántos resueltos y cuántos extras por versión**; el asistente arma los bloques, escribe lo que falte y cuida
que la hoja quepa (§8), que es lo único que no sale solo. La tabla de §13b tiene los números
de cada tema de Mate 5.

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
  Operaciones básicas`, `4. Monomios`, `8. Área y perímetro`… El número es **el
  del tema en el curso** (el orden del índice del sitio), no el lugar que ocupa
  en la hoja: la hoja se acomoda como convenga (§8), pero la numeración
  respeta el orden de los temas. El Examen 2 sigue con 10, 11, 12, 13.
  *"Podríamos numerar los cuadros (nunca los ejercicios), tal vez al lado del
  título"* y *"al menos en la numeración debería llevarse el orden de los
  temas de la página"*.

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
| **rotado** | tres tipos o más en bloques paralelos; cada versión lleva uno de cada tipo, unos resueltos y otros extra, rotando cuál va de extra | Cadena P1 de Mate 5: 2 resueltos + 1 extra, cubo, cuadrado y raíz |

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

**Cruzado con dos extras** (Mate 5, 21-sep-2026): cuando el tema tiene tres
tipos (Reglas básicas: polinomios, fracciones, mixtos; Cadena P1: cubos,
cuadrados, raíces), la versión lleva el resuelto de un tipo y **un extra de cada
uno de los otros dos**. Con dos tipos, los dos extras son del otro tipo.

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

### Aprovechar la cuartilla, y que se lea

**Decidido por Lety** (17-sep-2026, después de imprimir la primera hoja): el
espacio que sobre en la hoja **no se deja en blanco, se usa para que el examen
sea más legible**. En este orden: letra más grande, figuras más grandes,
más aire entre renglones, y filas reacomodadas para que ninguna fórmula se
parta. Todo sin pasar de la hoja. La meta es una hoja **llena y legible** —
no una hoja apretada ni una hoja medio vacía con letra chica.

Y la prueba de fuego es **imprimirla**: en pantalla todo se ve bien; fue en el
papel donde los triángulos "casi no se notaban". Cada vez que cambie el formato
o el acomodo, sacar el PDF (`pdf.py`) y mirarlo como hoja.

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
Lety para calificar, no la que se reparte. Desde el 21-sep-2026 va **un tema por
renglón, a lo ancho**, para que las resoluciones largas de Mate 5 no se corten.)

**Cómo mide las fórmulas** (21-sep-2026): por tokens (`ancho.py`), no por número
de caracteres. Con las fórmulas compactas de Mate 5 —exponentes, fracciones— el
conteo por caracteres gritaba *¡NO CABE!* en hojas que cabían al 80 %. Se
calibró contra 45 fórmulas medidas en el navegador y queda dentro de ±8 %. La
última palabra sigue siendo el PDF.

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
- **Matemáticas 5**: los dos exámenes quedaron armados el 21-sep-2026 (§13b)
  con el reparto decidido por el asistente calcando Mate 1; Lety no lo revisó
  tema por tema. Cualquier tema se puede subir o bajar de 1+1 a 1+2 (o al
  revés) cambiando su receta en `banco.py`.
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

## 13b. Matemáticas 5 al 21 de septiembre de 2026

**Los dos exámenes de Matemáticas 5 están armados**, las seis versiones de cada
uno, en blanco y resueltas (294 de 294 resoluciones, verificadas con sympy dos
veces: al escribirlas y con una segunda pasada independiente del resultado).
Lety pidió *"reproducir lo mismo"* que en Mate 1 y *"todos los temas de una vez,
y las 6 versiones"*, así que el reparto lo decidió el asistente calcando Mate 1:
**bloques por tipo en el mismo orden en los dos lados, cada versión 1 resuelto +
extras de tipo distinto (modo cruzado), 1+2 en los temas mecánicos y 1+1 en los
pesados, "Ejercicios extra 1" con exactamente lo que usan las seis versiones y
"Ejercicios extra 2" de práctica.** Donde no alcanzaban los resueltos se
escribieron, calcados del molde de la página y verificados.

Corte: **Examen 1 = temas 1 a 10** (las reglas de derivación, letras a–f, ~82 %
de la hoja); **Examen 2 = temas 11 a 19** (recta tangente, máximos y mínimos,
integrales; letras g–l, ~70 %). Historia del cálculo no entra: no tiene
ejercicios. Los PDF: `Examen 1 Matemáticas 5 (versiones a-f).pdf` y `Examen 2
Matemáticas 5 (versiones g-l).pdf` en `~/Downloads`, una versión por hoja.

| Tema | Tipos (Bloque 1 ↔ A, 2 ↔ B, 3 ↔ C) | Por versión | Escrito el 21-sep |
|---|---|---|---|
| 1 Reglas básicas | polinomios · con $x$ en el denominador (B3 y extra 2: práctica) | **2+2, decidido por Lety** | 2 resueltos, 12 extras |
| 2 Velocidad media | parábola hacia arriba · hacia abajo | 1+1, **visto por Lety: se queda** | 2 resueltos |
| 3 Senos y cosenos | un bloque de 6 resueltos; extra 1 con dos bloques de 6 **igual de largos**; el término lineal sólo $ax$ con $a$ entero | **1+2, decidido por Lety** | 1 resuelto, 12 extras |
| 4 Raíces | exponente mayor que el índice · menor · fracción con raíz abajo (un bloque de 6 por tipo, en los dos lados) | **3+3, decidido por Lety** | 6 resueltos, 6 extras |
| 5 Producto P1 | un bloque de 6 resueltos · un bloque de 6 en extra 1 (el otro, a extra 2) | **1+1, decidido por Lety** | — |
| 6 Producto P2 | monomio × trascendente · trascendente × trascendente · raíz × trascendente: 2 resueltos + 4 extras por tipo (B4 de práctica) | **1+2 rotado, decidido por Lety** | — |
| 7 Cociente P1 | denominador con número suelto · sin él (Bloque 1 ↔ A, 2 ↔ B, 3 y 3) | **1+1 cruzado, decidido por Lety** | — |
| 8 Cociente P2 | cociente simple · con sumas (B3 práctica) | 1+2 | — |
| 9 Cadena P1 | cubos · cuadrados · raíces: 4 resueltos + 2 extras por tipo (B1/A, B2/B, B3/C) | **2+1 rotado, decidido por Lety** | 6 resueltos |
| 10 Cadena P2 | raíz de potencia trig y trig de polinomio · ln y potencia de trig | 1+2 | — |
| 11 Recta tangente | parábola hacia arriba · hacia abajo | 1+1 | 1 resuelto (con gráfica) |
| 12 Puntos críticos | cúbico positivo · negativo | 1+2 | 2 resueltos, 2 extras |
| 13 Optimización | — | 1+1 | 2 resueltos (con figura) |
| 14 Integrales indefinidas | — | 1+2 | — |
| 15 Integrales definidas | — | 1+2 | — |
| 16 Área bajo la curva P1 | pendiente positiva · negativa | 1+1 | 1 resuelto |
| 17 Área bajo la curva P2 | parábola hacia arriba · hacia abajo | 1+1 | 1 resuelto |
| 18 Derivada por definición | lineales · cuadráticas puras · completas | 1+1 | — |
| 19 Suma de Riemann | $x^2$ positivo · negativo | 1+1 | 2 resueltos |

**Reglas básicas lo decidió Lety** (21-sep-2026, por la noche, con dos fotos): *"quiero
que tenga 4 ejercicios, 2 de cada tipo… 2 bloques de ejercicios resueltos con seis
ejercicios, de ahí saldrían dos… igual dos de 6 en extras… en ejercicios extra 2 los de
que sólo hay $x$ en el denominador y otros bloques de cada tipo para repaso"*. Quedó:
Ejercicios B1 = 6 polinomios y B2 = 6 con $x$ en el denominador (B3 = práctica resuelta:
los 4 de sólo $x$ en el denominador + 2 mixtos); extra 1 A = 6 polinomios y B = 6 mixtos;
extra 2 C = sólo $x$ en el denominador, D y E = repaso de cada tipo. Cada versión: uno de
cada bloque, receta `('por bloque', 1, 1, 2, 2)`. Examen 1 sube al 86 % de la hoja.
**Y la forma de los mixtos** (22-sep-2026): *"en las que tienen x en el denominador, que
tenga al menos una de $ax^n$, $ax^{-n}$, $ax$ y $a$"*, y enseguida: *"mejor pon 2 términos
con $ax^{-n}$ además de los otros"*, *"no siempre pongas $a$ al último, varía su posición"*,
*"lo mismo con el término $ax$, y usa también el $ax^{-1}$"*. Así que cada mixto (los 18:
6 resueltos que entran, 2 de práctica, 6 extras que entran, 4 de repaso) trae **cinco
términos: dos $ax^{-n}$ (uno de ellos, en varios, $\frac{a}{x}$), un $ax^n$, un $ax$ y una
constante, en posiciones variadas** — la constante y el $ax$ aparecen al principio, en medio
o al final. Las resoluciones siguen el orden escrito. Los de *sólo* $x$ en el denominador
(B3 y extra 2 C) son otro tipo y no llevan la regla.

**Senos y cosenos lo decidió Lety** (22-sep-2026): *"podían estar todos en un bloque y hacer
dos bloques de 6 en los extras 1, de la misma longitud, y en el examen poner uno de los
resueltos y dos de los extras 1"*. Los 6 resueltos quedaron en un **Bloque único**; se
escribieron **12 extras largos** (la misma forma que los resueltos: trigonométrica, fracción,
polinomio, $\ln$, $e^x$, $a^x$, $ax$ y constante) repartidos en **Bloque A y Bloque B** de 6;
los 12 cortos que había pasaron a extra 2 (repaso). Receta `('por bloque', 1, 1)`: uno del
bloque resuelto y uno de cada bloque de extras. Examen 1 sube al 90 % de la hoja.
**El término lineal, sólo $ax$ con $a$ entero** (Lety, 22-sep-2026): *"este término
[$-\frac{x}{2}$] les confunde derivar; mejor no lo pongas en los resueltos ni extras, sólo de
la forma $ax$, $a$ entero"*. Era el único de todo el curso (un resuelto de Senos); quedó $-3x$,
con su respuesta.

**Raíces lo decidió Lety** (22-sep-2026): *"podría haber 3 bloques de 6 en los ejercicios
resueltos de los tres tipos y la misma cantidad de extras"*. Los tres tipos, en el orden de
los Ejemplos de la página: **1** exponente mayor que el índice ($-6\sqrt[3]{x^4}$), **2**
menor ($5\sqrt[4]{x}$), **3** fracción con la raíz en el denominador
($\frac{-5}{6\sqrt[3]{x^2}}$). Ejercicios B1, B2, B3 y extra 1 A, B, C, seis cada uno;
*extra 2* desapareció porque los 18 extras entran. Se escribieron 6 resueltos ($3\sqrt[3]{x^5}$,
$-2\sqrt[5]{x^7}$, $8\sqrt[4]{x^7}$, $-6\sqrt[4]{x^3}$, $\frac{-4}{6\sqrt[5]{x^3}}$,
$\frac{8}{12\sqrt{x}}$) y 3 extras ($-3\sqrt[6]{x^7}$, $-5\sqrt[6]{x}$, $10\sqrt[5]{x}$).
El conteo por versión no lo dijo; siguiendo su patrón (un bloque de 6 = uno por versión)
cada versión lleva **uno de cada bloque: 3 resueltos + 3 extras**, receta `('por bloque', 1,
1)`. En la hoja va a dos columnas y queda alineado por tipo: a la izquierda los resueltos y
a la derecha los extras. Examen 1 sigue al 90 %.

**Producto P1 y Cociente P1 los decidió Lety** (22-sep-2026): *"como siento que es más
proceso (solo dos ejercicios para examen), podría ser 1 bloque de 6 ejercicios resueltos que
nos da un ejercicio para examen, y un bloque igual de extras 1 que me da un ejercicio para
examen, y los otros a extras 2"*. Así quedaron los dos: Ejercicios en un **Bloque único** de
6, extra 1 con **un bloque de 6** y el resto en extra 2; receta `('por bloque', 1, 1)` = 2 por
versión. Primero dijo *"igual para regla de cociente y de la cadena parte 1"* y enseguida
*"espérame para la cadena P1"*: Cadena P1 se quedó como estaba hasta que decida.
**Cociente P1 se afinó**: Lety notó que tiene **dos tipos** —el denominador **con número
suelto** ($\frac{4x^2-5x}{6x^2+3}$) o **sin él** ($\frac{x^5-6x^2}{2x^3+4x}$)— y pidió *"dos
bloques, bloque 1 de 3 ejercicios resueltos, bloque 2 de 3, y bloques extras A y B igual, y
en el examen tomar del bloque 1 y B, que son de diferente tipo, y del bloque 2 y A, para que
se mezclen"*. Es el **cruzado** de Mate 1: receta `('cruzado', 1, 1)`, las versiones a, c, e
llevan 1 + B y las b, d, f llevan 2 + A. Extra 2 quedó por tipo: C (con número suelto) y D, E,
F (sin él), 3 cada uno. Las respuestas de la página van a todo lo ancho: en dos columnas el
sitio encogía la letra de las más largas.
**Cadena P1 lo decidió después** (22-sep-2026): *"como hay ejercicios de tres tipos, me
gustaría hacer 6 de cada tipo, bloques con 4 ejercicios, los ejercicios extras 1 sólo 2 de
cada tipo, y con eso completamos el banco de preguntas de este ejercicio; tomamos dos de los
resueltos y 1 de extras 1, así tenemos los 3 ejercicios por examen; en este caso dos de estos
estarán en la base"*. O sea 6 por tipo = **4 resueltos + 2 extras**: Bloque 1/A cubos, 2/B
cuadrados, 3/C raíces; 18 en total, y en seis versiones sale cada uno una sola vez. El
asistente agregó que cada versión lleve **uno de cada tipo**: dos resueltos de dos tipos y el
extra del tercero, rotando — modo nuevo `('rotado', 2, 1)` en `seleccion.py`. Se escribieron
6 resueltos ($3(2-5x^2)^3$, $-2(3x^2+4)^3$, $3(4x-x^2)^2$, $-2(3x^3-5x)^2$, $\sqrt[3]{8x^2+1}$,
$\sqrt[5]{4-7x^2}$); los 18 extras que sobran quedaron en extra 2, por tipo (D, E, F).
**Producto P2, decidido por Lety** (22-sep-2026): *"hay tres tipos: monomio con trascendente,
trascendente con trascendente, raíz con trascendente; si quisiera que uno fuera resuelto y dos
vinieran de extras, ¿cómo hacemos los bloques?"*. Es Cadena P1 al revés: **2 resueltos + 4
extras por tipo** (Bloque 1/A, 2/B, 3/C) y receta `('rotado', 1, 2)` — cada versión lleva el
resuelto de un tipo y los dos extras de los otros dos. No se escribió nada: los extras ya eran
4 por tipo; de resueltos había 3, 3 y 4. Los 4 que sobraban primero quedaron en un Bloque 4
de práctica resuelta, y Lety lo corrigió con su regla: el banco es resueltos + extra 1, así que
**bajaron a extra 2**, cada uno en el bloque de su tipo y sin respuesta.

Los ejercicios nuevos, por si Lety quiere cambiar alguno: Velocidad $x(t) = 2t^2
- 6t$ y $x(t) = 12t - 3t^2$; Senos $f(x) = 6\tan x - \frac{2}{x^5} + 5\,\mathrm{sen}\,x -
3x^4 + \ln x - 5^x + 4e^x - 9\cos x + 3$ (resuelto) y los 12 extras largos de los bloques A
y B (todos nuevos, verificados con sympy); Recta tangente $f(x) = -(x+2)^2 + 4$ en
$(-1, 3)$; Puntos críticos $2x^3 - 9x^2$ y $6x^2 - 4x^3$ (y los extras $5x^3 -
3x^2$, $x^3 - 3x^2$); Optimización altura $x+5$ con $P = 32$ y altura $x+1$ con
$P = 20$; Área P1 $-x + 10$ en $[1, 3]$; Área P2 $-x^2 + 4x + 1$ en $[0, 3]$;
Riemann $\int_0^3 (9 - x^2)\,dx$ y $\int_1^4 (5 - 2x^2)\,dx$; extras de Raíces
$\frac{-4}{8\sqrt[5]{x^2}}$, $\frac{6}{9\sqrt{x^5}}$, $-8\sqrt[3]{x^7}$. En Reglas
básicas, con el reparto de Lety: resueltos $-2x^7 + 4x^5 - 3x^2 + 8x - 6$ y $7x^4 - x^3 +
5x^2 - 9x + 3$; extras que entran $-6x^7 + 3x^4 - 8x^2 + 5x - 2$, $7x^5 - \frac{4}{x^3} +
2x - 9$ y $-5x^4 + \frac{6}{x^3} - 3x + 8$; de repaso (extra 2) $-\frac{8}{x^3} +
\frac{5}{x^6} - \frac{2}{x^2}$ y ocho más (cuatro polinomios, cuatro mixtos).

**Ojo:** el extra de Puntos críticos $f(x) = -4x^3 + 88x^2$ (viene así del
doc) da el punto crítico $x = 44/3$; se dejó en *extra 2* (no entra al examen)
por si es una errata de $8x^2$.

## 14. Cómo le gusta a Lety trabajar esto

Salió el 17-sep-2026, cuando retomó los cuadros diciendo *"ando algo perdida"*
y *"me siento un poco saturada"*:

- **Un tema a la vez, en el orden de la página del curso**, y no pasar al
  siguiente hasta cerrar el anterior. Nada de tablas con los trece temas de
  golpe. *Matiz del 21-sep-2026:* para Mate 5 pidió lo contrario —*"todos los
  temas de una vez, y las 6 versiones"*, reproduciendo los patrones de Mate 1—
  y delegó el reparto. Preguntarle qué ritmo quiere al arrancar cada materia.
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
  evaluación/Exámenes/Matemáticas 1/` y `…/Matemáticas 5/`, y ahí los sigue
  escribiendo `generar.py` (una carpeta por curso).
- Las 180 resoluciones de los extras de Mate 5 están en
  `cuadros/generador/resoluciones-manuales.json` ("Matemáticas 5"), escritas por
  un generador con sympy en el estilo de cada página y verificadas dos veces. El
  generador vivía en el scratchpad de la sesión del 21-sep-2026 y se perdió con
  él; si un extra cambia, su resolución se escribe a mano ahí, como en Mate 1.
- Los temas de donde salen los reactivos: `math/matematicas-1/` — **aquí mismo**, así que ya
  no hay regla de "solo lectura": agregar los extras que falten y regenerar es un solo
  trabajo, en una sola sesión. Al hacerlo, respeta el manual del sitio (`CLAUDE.md`).
