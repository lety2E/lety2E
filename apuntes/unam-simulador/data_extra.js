// Banco extra de preguntas — guía de Lety (Síntesis Estructural Progresiva)
// Cada pregunta lleva opcionalmente `explanation` con la justificación.

const EXTRA_QUESTIONS = {
  "fisica": [
    {
      "text": "Una persona camina 30 m hacia el Este y luego 40 m hacia el Norte. Si todo el recorrido lo realiza en un tiempo de 10 s, ¿cuáles son las magnitudes de su velocidad media y su rapidez media, respectivamente?",
      "options": [
        "5 m/s y 7 m/s",
        "7 m/s y 5 m/s",
        "7 m/s y 7 m/s",
        "5 m/s y 5 m/s"
      ],
      "correct": 0
    },
    {
      "text": "Un bloque de 5 kg se encuentra sobre una superficie horizontal lisa. Si se le aplica una fuerza neta constante de 20 N en dirección horizontal, ¿cuál es la magnitud de la aceleración que adquiere el bloque?",
      "options": [
        "100 m/s²",
        "0.25 m/s²",
        "4 m/s²",
        "15 m/s²"
      ],
      "correct": 2
    },
    {
      "text": "De acuerdo con la Ley de la Gravitación Universal, si la distancia entre dos masas se reduce a la mitad (d/2), la fuerza de atracción gravitacional entre ellas:",
      "options": [
        "Se reduce a la mitad.",
        "Disminuye a la cuarta parte.",
        "Se duplica.",
        "Se cuadruplica."
      ],
      "correct": 3
    },
    {
      "text": "Una caja es arrastrada una distancia de 5 m sobre un piso horizontal mediante la aplicación de una fuerza constante de 40 N que actúa de forma paralela al movimiento. ¿Qué trabajo mecánico se realiza sobre la caja?",
      "options": [
        "8 J",
        "45 J",
        "200 J",
        "200 W"
      ],
      "correct": 2
    },
    {
      "text": "En una prensa hidráulica, el émbolo menor tiene un área de 0.02 m² y el émbolo mayor tiene un área de 0.1 m². Si se aplica una fuerza de 50 N en el émbolo menor, ¿qué fuerza se genera en el émbolo mayor?",
      "options": [
        "10 N",
        "50 N",
        "250 N",
        "500 N"
      ],
      "correct": 2
    },
    {
      "text": "Un gas ideal encerrado en un cilindro con un pistón móvil absorbe 500 J de calor del entorno, lo que provoca que el gas se expanda realizando un trabajo mecánico de 300 J. ¿Cuál es el cambio en la energía interna (ΔU) de este gas?",
      "options": [
        "800 J",
        "200 J",
        "-200 J",
        "500 J"
      ],
      "correct": 1
    }
  ],
  "quimica": [
    {
      "text": "¿Cuál de las siguientes opciones clasifica correctamente al aire purificado y al agua destilada?",
      "options": [
        "El aire es un elemento y el agua es una mezcla homogénea.",
        "El aire es una mezcla homogénea y el agua es un compuesto.",
        "El aire es un compuesto y el agua es una mezcla heterogénea.",
        "El aire es una mezcla heterogénea y el agua es un elemento."
      ],
      "correct": 1,
      "explanation": "El aire es una disolución gaseosa compuesta mayoritariamente por nitrógeno y oxígeno en proporciones variables, lo que lo convierte en una mezcla homogénea. El agua destilada está constituida únicamente por moléculas de H₂O en proporción fija, por lo tanto, es un compuesto químico."
    },
    {
      "text": "Un átomo neutro posee un número atómico (Z) de 19 y una masa atómica (A) de 39. ¿Cuántos electrones y neutrones contiene respectivamente?",
      "options": [
        "19 electrones y 39 neutrones.",
        "20 electrones y 19 neutrones.",
        "19 electrones y 20 neutrones.",
        "39 electrones y 20 neutrones."
      ],
      "correct": 2,
      "explanation": "En un átomo neutro, el número de electrones es igual al número atómico Z (19 electrones). Para obtener el número de neutrones restamos el número atómico de la masa atómica: n⁰ = A - Z = 39 - 19 = 20 neutrones."
    },
    {
      "text": "¿Qué tipo de enlace se forma cuando se combina un elemento de muy alta electronegatividad (como el Cloro) con un elemento de muy baja electronegatividad (como el Sodio)?",
      "options": [
        "Covalente polar",
        "Covalente no polar",
        "Metálico",
        "Iónico"
      ],
      "correct": 3,
      "explanation": "La gran diferencia de electronegatividad entre un no metal altamente electronegativo y un metal con muy baja electronegatividad genera una transferencia completa de electrones, formando iones de cargas opuestas que se atraen electrostáticamente."
    },
    {
      "text": "¿Cuál es la masa molar del ácido sulfúrico (H₂SO₄)? (Considere las masas atómicas: H = 1 g/mol, S = 32 g/mol, O = 16 g/mol)",
      "options": [
        "49 g/mol",
        "98 g/mol",
        "142 g/mol",
        "84 g/mol"
      ],
      "correct": 1,
      "explanation": "Calculamos la suma ponderada de las masas: H: (2 x 1) + S: (1 x 32) + O: (4 x 16) = 2 + 32 + 64 = 98 g/mol."
    },
    {
      "text": "¿A qué propiedad intermolecular se debe que el agua requiera una cantidad considerable de energía térmica para elevar su temperatura o cambiar de estado físico?",
      "options": [
        "A la presencia de enlaces covalentes polares.",
        "A las interacciones por fuerzas de Van der Waals inducidas.",
        "A la formación de redes moleculares por puentes de hidrógeno.",
        "A la geometría lineal de sus enlaces."
      ],
      "correct": 2,
      "explanation": "Los puentes de hidrógeno forman una red cohesiva muy firme entre las moléculas de agua. Para cambiar el estado físico o elevar la temperatura del agua líquida, es imperativo suministrar mucha energía térmica dirigida prioritariamente a romper estas interacciones moleculares."
    },
    {
      "text": "De acuerdo con la teoría de Brönsted-Lowry, una sustancia que actúa como base se caracteriza por:",
      "options": [
        "Donar un par de electrones en un enlace covalente coordinado.",
        "Liberar iones hidróxido (OH⁻) en medio acuoso.",
        "Aceptar protones (H⁺) provenientes de un ácido.",
        "Donar protones (H⁺) hacia un disolvente."
      ],
      "correct": 2,
      "explanation": "La teoría de Brönsted-Lowry postula que los ácidos son donadores de protones (H⁺) y las bases son aceptores de protones (H⁺)."
    },
    {
      "text": "¿Cuál es la molaridad (M) de una disolución preparada al disolver 40 g de hidróxido de sodio (NaOH) en agua hasta alcanzar un volumen total de 2.0 Litros? (NaOH = 40 g/mol)",
      "options": [
        "0.5 M",
        "1.0 M",
        "2.0 M",
        "0.25 M"
      ],
      "correct": 0,
      "explanation": "1) Moles de NaOH: 40 g / 40 g/mol = 1 mol. 2) Aplicamos fórmula de Molaridad: M = moles / Litros = 1 mol / 2.0 Litros = 0.5 M."
    },
    {
      "text": "De acuerdo con la ley de Boyle-Mariotte, si el volumen de una muestra de gas confinado se reduce a la mitad manteniendo la temperatura constante, ¿qué sucede con la presión del sistema?",
      "options": [
        "Se reduce a la mitad.",
        "Permanece sin cambios.",
        "Se duplica.",
        "Se cuadruplica."
      ],
      "correct": 2,
      "explanation": "La ley de Boyle establece una relación inversamente proporcional entre presión y volumen. Si el volumen se divide entre dos, la presión necesariamente debe multiplicarse por dos (se duplica)."
    },
    {
      "text": "En la siguiente reacción química: Zn + 2HCl ➔ ZnCl₂ + H₂, se puede afirmar que el Zinc experimenta una:",
      "options": [
        "Reducción, actuando como agente oxidante.",
        "Oxidación, disminuyendo su número de oxidación.",
        "Oxidación, actuando como agente reductor.",
        "Reducción, ganando electrones del hidrógeno."
      ],
      "correct": 2,
      "explanation": "El Zinc pasa de un número de oxidación de 0 (en estado elemental) a +2 (en ZnCl₂). Al aumentar su número de oxidación, significa que ha perdido electrones (se oxidó). Al oxidarse, actúa de manera automática como el agente reductor de la reacción."
    },
    {
      "text": "¿Bajo qué condiciones un compuesto iónico sólido, como el cloruro de potasio (KCl), es capaz de conducir eficazmente la corriente eléctrica?",
      "options": [
        "Exclusivamente cuando se encuentra en estado sólido y a bajas temperaturas.",
        "Únicamente cuando adquiere una geometría molecular lineal.",
        "Cuando se encuentra fundido o disuelto en un medio acuoso.",
        "En cualquier estado físico, debido a la rigidez de sus enlaces electrostáticos."
      ],
      "correct": 2,
      "explanation": "Los compuestos iónicos sólidos tienen sus iones inmóviles en una red cristalina rígida. Al fundirse o disolverse en agua, la red se destruye y los iones adquieren plena movilidad, convirtiéndose en excelentes conductores eléctricos (electrólitos)."
    },
    {
      "text": "¿Qué tipo de enlace químico une de forma covalente el grupo carboxilo de un aminoácido con el grupo amino de otro para dar origen a la estructura primaria de las proteínas?",
      "options": [
        "Glucosídico",
        "Éster",
        "Peptídico",
        "Puente de hidrógeno"
      ],
      "correct": 2,
      "explanation": "El enlace peptídico es una unión de tipo amida covalente que conecta de manera consecutiva a los aminoácidos para dar vida a las cadenas polipeptídicas de las proteínas."
    },
    {
      "text": "Gases cuya emisión desmedida a la atmósfera es señalada como la causa primordial del fenómeno de la lluvia ácida:",
      "options": [
        "CH₄ y CO₂",
        "CO y CFC",
        "SO₂ y NOₓ",
        "O₃ y Ar"
      ],
      "correct": 2,
      "explanation": "El dióxido de azufre (SO₂) y los óxidos de nitrógeno (NOₓ) son gases contaminantes primarios industriales que al reaccionar con el agua de las nubes dan lugar a los ácidos fuertes nítrico (HNO₃) y sulfúrico (H₂SO₄)."
    }
  ],
  "literatura": [
    {
      "text": "¿Cuál es la función de la lengua que predomina en un texto literario para lograr un efecto estético?",
      "options": [
        "Referencial o informativa",
        "Metalingüística",
        "Poética o estética",
        "Apelativa o conativa"
      ],
      "correct": 2,
      "explanation": "La función poética (o estética) se enfoca en el embellecimiento del mensaje y el uso creativo de las palabras, lo cual constituye el núcleo de la creación literaria. Las otras funciones tienen propósitos distintos: la referencial busca informar datos objetivos y la apelativa busca convencer al receptor."
    },
    {
      "text": "Identifica el enunciado que utiliza un lenguaje predominantemente de tipo connotativo:",
      "options": [
        "Sus ojos lucían cansados debido a la falta prolongada de sueño.",
        "El oro es un metal que funde a una temperatura de 1064 °C.",
        "Dos estrellas de fuego iluminaban su rostro pálido en la penumbra.",
        "La luna es el único satélite natural que posee la Tierra."
      ],
      "correct": 2,
      "explanation": "El término 'Dos estrellas de fuego' hace referencia de forma poética y metafórica a los ojos, dándole una interpretación subjetiva que caracteriza al lenguaje connotativo. Los demás enunciados presentan un uso objetivo y literal de los conceptos (lenguaje denotativo)."
    },
    {
      "text": "Género literario caracterizado por ser representado ante el público, prescindiendo de un narrador y basándose en diálogos y acotaciones:",
      "options": [
        "Lírico",
        "Épico",
        "Narrativo",
        "Dramático"
      ],
      "correct": 3,
      "explanation": "El género dramático se crea expresamente para representarse mediante actores en escena. Su estructura interna está construida totalmente de diálogos e indicaciones escénicas llamadas acotaciones, que aparecen de forma habitual entre paréntesis."
    },
    {
      "text": "Identifica el tipo de narrador en el siguiente fragmento: \"Crucé la calle apresurado, sintiendo que el frío calaba mis huesos; miré hacia atrás pero nadie me seguía.\"",
      "options": [
        "Omnisciente",
        "Protagonista",
        "Testigo",
        "Extradiegético"
      ],
      "correct": 1,
      "explanation": "El uso de la primera persona gramatical ('Crucé', 'mi', 'mis') nos indica de manera inmediata que el narrador es el mismo personaje que experimenta la historia en carne propia; es decir, un narrador de tipo protagonista."
    },
    {
      "text": "¿Qué figura retórica se utiliza en los siguientes versos de Sor Juana Inés de la Cruz? \"Al que ingrato me deja, busco amante; / al que amante me sigue, dejo ingrato;\"",
      "options": [
        "Antítesis o Paradoja",
        "Hipérbole",
        "Símil o comparación",
        "Aliteración"
      ],
      "correct": 0,
      "explanation": "Se presenta una contraposición de términos opuestos ('ingrato me deja' frente a 'busco amante' e 'ingrato dejo' frente a 'amante me sigue'). Esta contraposición de ideas lógicas con un sentido lírico profundo configura el uso de la antítesis o la paradoja."
    },
    {
      "text": "Movimiento del siglo XIX que antepone el sentimiento y la libertad creadora por encima de la rigidez neoclásica:",
      "options": [
        "Realismo",
        "Romanticismo",
        "Vanguardismo",
        "Clasicismo"
      ],
      "correct": 1,
      "explanation": "La rebelión contra las reglas estrictas de la razón y el predominio absoluto del sentimiento personal, el amor idealizado, el dolor de vivir y la libertad individual son las marcas registradas del Romanticismo del siglo XIX."
    },
    {
      "text": "Vanguardia artística que se inspira en el psicoanálisis y busca representar el inconsciente y los sueños libres:",
      "options": [
        "Surrealismo",
        "Futurismo",
        "Dadaísmo",
        "Cubismo"
      ],
      "correct": 0,
      "explanation": "Inspirado en el psicoanálisis de Sigmund Freud, el Surrealismo (comandado por André Breton) es la vanguardia del siglo XX que busca liberar la creatividad a través de las expresiones del inconsciente y del mundo de los sueños."
    },
    {
      "text": "¿Cuál es considerada la primera novela propiamente escrita e impresa en Hispanoamérica?",
      "options": [
        "\"Los de abajo\" de Mariano Azuela",
        "\"Pedro Páramo\" de Juan Rulfo",
        "\"El Periquillo Sarniento\" de Fernández de Lizardi",
        "\"Cien años de soledad\" de Gabriel García Márquez"
      ],
      "correct": 2,
      "explanation": "José Joaquín Fernández de Lizardi ('El Pensador Mexicano') publicó 'El Periquillo Sarniento' en 1816 en la Ciudad de México, convirtiéndose oficialmente en la primera novela de todo el continente hispanoamericano."
    },
    {
      "text": "Fiel representante del realismo mágico, autor de la novela \"Pedro Páramo\", caracterizada por sus atmósferas fantasmales:",
      "options": [
        "Carlos Fuentes",
        "Octavio Paz",
        "Juan Rulfo",
        "Mariano Azuela"
      ],
      "correct": 2,
      "explanation": "Juan Rulfo es una figura icónica de la narrativa en México. A través de murmullos de ánimas y fantasmas atrapados por sus culpas en el desértico pueblo de Comala, construyó la obra maestra 'Pedro Páramo'."
    },
    {
      "text": "Tipo de ficha de trabajo que copia textualmente un fragmento, cuyo distintivo para su identificación en el examen es el uso de comillas:",
      "options": [
        "Ficha de paráfrasis",
        "Ficha bibliográfica",
        "Ficha hemerográfica",
        "Ficha de cita textual"
      ],
      "correct": 3,
      "explanation": "La ficha de cita textual tiene la finalidad de registrar un extracto literal de la obra consultada, lo cual se identifica formalmente en la investigación académica mediante el uso obligatorio de las comillas dobles."
    }
  ],
  "geografia": [
    {
      "text": "La geografía es catalogada como una ciencia mixta e interdisciplinaria. Esto se fundamenta primordialmente en que:",
      "options": [
        "Únicamente se enfoca en enlistar la división política y accidentes del relieve de las naciones.",
        "Une conocimientos de ciencias naturales y sociales para comprender el espacio geográfico.",
        "Prescinde de las ciencias de cómputo y cartografía moderna para basarse en testimonios históricos.",
        "Su único objeto de estudio es el impacto de la atmósfera en la producción ganadera continental."
      ],
      "correct": 1
    },
    {
      "text": "¿Cuál de los siguientes acontecimientos representa de forma exacta un hecho geográfico?",
      "options": [
        "La súbita inundación causada por el desbordamiento de un río tras una tormenta.",
        "El terremoto ocurrido el 19 de septiembre en las costas mexicanas de Guerrero.",
        "La lenta y paulatina separación continental de la Falla del Rift de África Oriental a lo largo de millones de años.",
        "El paso destructivo de un tornado de categoría mayor por el centro de Estados Unidos."
      ],
      "correct": 2
    },
    {
      "text": "Al estudiar una epidemia regional transmitida por mosquitos vectores, los geógrafos determinan la posición exacta de los pozos de agua estancada y trazan la ruta del brote. ¿Qué principios metodológicos están aplicando respectivamente?",
      "options": [
        "Relación y Evolución.",
        "Localización y Causalidad.",
        "Localización y Relación.",
        "Evolución y Causalidad."
      ],
      "correct": 2
    },
    {
      "text": "Si en Japón (huso horario $135^\\\\\\\\circ$ Este) son las 21:00 horas del día martes, ¿qué hora y día serán en Tijuana, México, que se localiza en el huso de $120^\\\\\\\\circ$ Oeste?",
      "options": [
        "04:00 horas del mismo día martes.",
        "12:00 horas del día miércoles siguiente.",
        "04:00 horas del día miércoles siguiente.",
        "14:00 horas del día lunes anterior."
      ],
      "correct": 0
    },
    {
      "text": "Un avión vuela de la Ciudad de México ($90^\\\\\\\\circ$ Oeste) a las 08:00 AM rumbo a Madrid, España ($0^\\\\\\\\circ$). Si la travesía aérea tiene una duración neta de 10 horas, ¿qué hora registrará Madrid al aterrizar?",
      "options": [
        "12:00 horas del mismo día.",
        "18:00 horas del mismo día.",
        "24:00 horas del mismo día (medianoche).",
        "02:00 horas del día posterior."
      ],
      "correct": 2
    },
    {
      "text": "El motor principal que impulsa el desplazamiento constante de las placas tectónicas en la litósfera terrestre reside en la astenósfera mediante el mecanismo de:",
      "options": [
        "El campo gravitatorio dipolar del núcleo central.",
        "Las corrientes de convección térmica del magma.",
        "Los movimientos sísmicos inducidos de las profundidades.",
        "La fricción de mareas de los océanos cálidos."
      ],
      "correct": 1
    },
    {
      "text": "La sismicidad recurrente y de gran magnitud en estados como Oaxaca y Guerrero, así como la formación del Eje Volcánico Transversal, obedecen a un límite de tipo:",
      "options": [
        "Divergente por separación de la Placa del Caribe.",
        "Transformante debido a la gran Falla de San Andrés.",
        "Convergente por subducción de la Placa de Cocos bajo la Norteamericana.",
        "Asísmico de las llanuras costeras del Golfo."
      ],
      "correct": 2
    },
    {
      "text": "La desintegración física o descomposición química de los minerales de una roca in situ, es decir, sin transporte, por agentes como los gases atmosféricos, la temperatura o el agua, se define como:",
      "options": [
        "Erosión antrópica.",
        "Intemperismo (Meteorización).",
        "Orogénesis tectónica.",
        "Sedimentación fluvial."
      ],
      "correct": 1
    },
    {
      "text": "¿Qué tipo de relieve continental favorece la mayor concentración humana, la siembra tecnificada extensiva y la construcción barata de redes de transporte terrestre?",
      "options": [
        "Las mesetas.",
        "Las llanuras.",
        "Las cordilleras.",
        "Los macizos alpinos."
      ],
      "correct": 1
    },
    {
      "text": "¿Cuál es la consecuencia socioeconómica y alimentaria de las corrientes marinas frías en las costas de los continentes?",
      "options": [
        "Favorecen el cultivo de maderas tropicales preciosas debido a lluvias torrenciales.",
        "Son ricas en nutrientes y oxígeno, lo que estimula la pesca industrial a gran escala.",
        "Bloquean la navegación marítima mercante debido a marejadas constantes.",
        "Desatan huracanes de gran intensidad debido a su rápida evaporación térmica."
      ],
      "correct": 1
    },
    {
      "text": "La capa gaseosa protectora contra la radiación electromagnética de alta frecuencia ultravioleta nociva ($O_3$) se encuentra localizada en la capa de la:",
      "options": [
        "Troposfera.",
        "Estratósfera.",
        "Termósfera.",
        "Mesósfera."
      ],
      "correct": 1
    },
    {
      "text": "Según el sistema clasificatorio de Köppen, la combinación climática **Aw** designa un clima tropical lluvioso durante el verano. ¿Qué región natural se desarrolla bajo estas condiciones?",
      "options": [
        "La Tundra.",
        "La Sabana.",
        "El Desierto Extremo.",
        "La Estepa."
      ],
      "correct": 1
    }
  ],
  "biologia": [
    {
      "text": "Científico que, al observar láminas de corcho en un microscopio primitivo, acuñó el término \"célula\":",
      "options": [
        "Anton van Leeuwenhoek",
        "Robert Hooke",
        "Theodor Schwann",
        "Rudolf Virchow"
      ],
      "correct": 1
    },
    {
      "text": "¿Cuál de las siguientes opciones describe correctamente la función y composición de los carbohidratos en la célula?",
      "options": [
        "Almacenar material genético y están compuestos de nucleótidos.",
        "Proveer energía inmediata a la célula y están constituidos por cadenas de monosacáridos.",
        "Catalizar reacciones metabólicas y se conforman por largas cadenas de aminoácidos.",
        "Aislar térmicamente a la célula y se integran principalmente de ácidos grasos."
      ],
      "correct": 1
    },
    {
      "text": "Organelo celular membranoso cuya función primordial consiste en llevar a cabo la respiración celular aerobia para la síntesis de ATP:",
      "options": [
        "Cloroplasto",
        "Ribosoma",
        "Aparato de Golgi",
        "Mitocondria"
      ],
      "correct": 3
    },
    {
      "text": "Sustancia orgánica que actúa como el aceptor final de los electrones en la etapa terminal de la cadena respiratoria aerobia:",
      "options": [
        "Nitrógeno",
        "Oxígeno",
        "Piruvato",
        "Dióxido de carbono"
      ],
      "correct": 1
    },
    {
      "text": "¿Cuál es el evento biológico fundamental que ocurre durante la Profase I de la meiosis y que promueve directamente la variabilidad genética en organismos sexuales?",
      "options": [
        "La alineación de cromosomas en el ecuador.",
        "El entrecruzamiento de cromosomas homólogos (crossing-over).",
        "La separación de cromátidas hermanas hacia los polos.",
        "La duplicación del número diploide de cromosomas."
      ],
      "correct": 1
    },
    {
      "text": "Al realizar una cruza de dos individuos heterocigotos híbridos (Aa x Aa), ¿cuál es la proporción fenotípica teórica resultante en la F2 de acuerdo con las Leyes de Mendel?",
      "options": [
        "9:3:3:1",
        "1:2:1",
        "3:1",
        "100% dominantes"
      ],
      "correct": 2
    },
    {
      "text": "Las alas de una mosca y las de un águila cumplen la misma función, pero presentan estructuras internas y origen embrionario diferentes. ¿Cómo se denominan estructuralmente?",
      "options": [
        "Órganos homólogos",
        "Órganos vestigiales",
        "Órganos análogos",
        "Mutaciones puntuales"
      ],
      "correct": 2
    },
    {
      "text": "Proceso de eutrofización en un lago o cuerpo de agua de agua dulce se desencadena fundamentalmente por:",
      "options": [
        "El enfriamiento repentino del agua por corrientes árticas.",
        "El aumento del gas radón liberado por fisuras volcánicas.",
        "El desecho de fertilizantes ricos en nitratos y fosfatos que reducen el oxígeno.",
        "La eliminación masiva de bacterias degradadoras aeróbicas."
      ],
      "correct": 2
    }
  ],
  "historiaMexico": [
    {
      "text": "Relaciona la superárea cultural de México con su descripción geográfica y económica:<br><br><strong>Superáreas:</strong><br>1. Mesoamérica<br>2. Aridoamérica<br>3. Oasisamérica<br><br><strong>Características:</strong><br>a. Clima desértico con presencia de oasis; pueblos semi-sedentarios y agricultores.<br>b. Tierras fértiles con lluvias; cuna de sociedades sedentarias con pirámides y calendarios duales.<br>c. Entorno árido y seco; habitado por pueblos nómadas dedicados a la recolección y caza.",
      "options": [
        "1-a, 2-b, 3-c",
        "1-b, 2-c, 3-a",
        "1-c, 2-a, 3-b",
        "1-b, 2-a, 3-c"
      ],
      "correct": 1,
      "explanation": "Mesoamérica (1) = tierras fértiles, sedentaria (b). Aridoamérica (2) = árido, nómadas (c). Oasisamérica (3) = desértico con oasis, semi-sedentarios (a)."
    },
    {
      "text": "¿Cuál fue el factor político y de estrategia militar clave que facilitó la rendición de México-Tenochtitlan ante las tropas españolas en 1521?",
      "options": [
        "El despliegue de barcos armados en el puerto de Veracruz.",
        "Las alianzas militares pactadas con señoríos locales como los tlaxcaltecas.",
        "El arribo masivo de refuerzos navales enviados por la Corona de Aragón.",
        "El abandono voluntario de la ciudad por mandato del tlatoani Moctezuma."
      ],
      "correct": 1
    },
    {
      "text": "¿Qué impacto generó la aplicación de las Reformas Borbónicas en el virreinato de la Nueva España durante el siglo XVIII?",
      "options": [
        "La autonomía absoluta de los criollos y el cese inmediato de los gravámenes.",
        "La centralización del clero y la abolición del virreinato por mandatos feudales.",
        "El establecimiento de intendencias, la centralización tributaria y la inconformidad criolla.",
        "El abandono voluntario del virrey y el reparto libre de las tierras agrarias."
      ],
      "correct": 2
    },
    {
      "text": "¿Qué tratado diplomático puso fin al conflicto armado de invasión de los Estados Unidos en 1848, oficializando la venta de Alta California y Arizona?",
      "options": [
        "Tratado de Velasco.",
        "Tratado de La Soledad.",
        "Tratado de Guadalupe-Hidalgo.",
        "Tratados de Córdoba."
      ],
      "correct": 2
    },
    {
      "text": "La Ley Lerdo, promulgada en la antesala de la Constitución de 1857, consistió fundamentalmente en:",
      "options": [
        "La anulación de los fueros militares para delitos civiles.",
        "La desamortización de bienes raíces y fincas de corporaciones civiles y religiosas.",
        "La cancelación del cobro por servicios parroquiales y actas de nacimiento.",
        "El reparto agrario absoluto de las tierras confiscadas en el bajío."
      ],
      "correct": 1
    },
    {
      "text": "Durante el Porfiriato, el motor de infraestructura económica que unificó y dinamizó el mercado interior de la nación fue:",
      "options": [
        "El desarrollo urbano de los puertos petroleros en el Golfo de México.",
        "La expansión de la red de vías ferroviarias en el territorio nacional.",
        "La consolidación del telégrafo inalámbrico en las haciendas.",
        "El monopolio estatal sobre la minería de plata y el carbón."
      ],
      "correct": 1
    }
  ],
  "historiaUniversal": [
    {
      "text": "Un investigador localiza el acta oficial de fundación del Congreso de Viena redactada en 1815. ¿Qué clasificación recibe este testimonio documental?",
      "options": [
        "Fuente indirecta o secundaria.",
        "Fuente directa o primaria.",
        "Fuente arqueológica no coetánea.",
        "Fuente heurística alternativa."
      ],
      "correct": 1,
      "explanation": "Al tratarse de un documento oficial elaborado de forma simultánea o coetánea al acontecimiento por los mismos firmantes del suceso, constituye una fuente directa (primaria)."
    },
    {
      "text": "De acuerdo con el pensamiento de la Ilustración, ¿cuál de las siguientes opciones describe el postulado de Jean-Jacques Rousseau plasmado en El contrato social?",
      "options": [
        "La conformación del derecho de la corona por gracia de Dios.",
        "La doctrina de la soberanía popular como origen del poder del estado.",
        "La teoría económica basada en la desregulación de aranceles estatales.",
        "La descentralización política en tres poderes independientes."
      ],
      "correct": 1,
      "explanation": "Rousseau postuló que la soberanía no reside en el monarca sino en la voluntad general del pueblo, la cual se cede de forma consensual mediante un contrato social."
    },
    {
      "text": "Corriente obrera que proponía la destrucción intencionada de máquinas industriales por considerarlas culpables de la cesantía y explotación obrera:",
      "options": [
        "Socialismo Científico.",
        "Anarquismo colectivista.",
        "Cartismo.",
        "Ludismo."
      ],
      "correct": 3,
      "explanation": "El Ludismo fue la reacción obrera espontánea y destructora surgida en el s. XIX, que consistía en irrumpir en las fábricas y destrozar telares y máquinas mecánicas de vapor."
    },
    {
      "text": "¿Qué trascendental suceso geopolítico del año 1917 alteró drásticamente el curso militar de la Primera Guerra Mundial?",
      "options": [
        "La invasión alemana a Polonia y la firma del Tratado de Versalles.",
        "La salida del Imperio Ruso debido al triunfo bolchevique y el ingreso de los Estados Unidos.",
        "El asesinato del heredero Francisco Fernando en Sarajevo.",
        "La celebración de la Conferencia de Berlín para el reparto de territorios."
      ],
      "correct": 1,
      "explanation": "La Revolución Bolchevique obligó a Lenin a pactar la salida de Rusia. Paralelamente, la guerra submarina alemana empujó el ingreso industrial y bélico de EE.UU., decantando la victoria aliada."
    },
    {
      "text": "El detonante directo o causa inmediata de la Segunda Guerra Mundial en septiembre de 1939 fue:",
      "options": [
        "La invasión militar alemana sobre territorio de Polonia.",
        "El bombardeo japonés aéreo sobre la base militar de Pearl Harbor.",
        "La firma militar de rendición nazi en Stalingrado.",
        "La llegada forzada de los planes quinquenales a la URSS."
      ],
      "correct": 0,
      "explanation": "Alemania invadió Polonia el 1 de septiembre de 1939. En respuesta inmediata, Gran Bretaña y Francia declararon formalmente la guerra a Hitler, dando inicio a la WWII."
    },
    {
      "text": "¿Cuál fue el tratado de asistencia militar recíproca firmado en 1955 por el bloque de repúblicas socialistas lideradas por la URSS en el contexto de la Guerra Fría?",
      "options": [
        "El Plan Marshall de apoyo.",
        "La Alianza de la OTAN.",
        "El Pacto de Varsovia.",
        "La Unión aduanera del COMECON."
      ],
      "correct": 2,
      "explanation": "El Pacto de Varsovia fue fundado en 1955 para cohesionar militarmente el área socialista, en directa oposición a la OTAN norteamericana fundada en 1949."
    },
    {
      "text": "Políticas de reestructuración económica y transparencia informativa aplicadas en la Unión Soviética por Mijaíl Gorbachov, respectivamente:",
      "options": [
        "Planes Quinquenales y COMECON.",
        "Perestroika y Glasnost.",
        "Plan Marshall y Doctrina Truman.",
        "Neoliberalismo y Colectivización."
      ],
      "correct": 1,
      "explanation": "La Perestroika flexibilizó y reformó la economía planificada soviética introduciendo mecanismos comerciales libres, mientras la Glasnost trajo apertura y libertad de información."
    }
  ],
  "espanol": [
    {
      "text": "¿Qué función de la lengua predomina en el siguiente fragmento? <em>\"El prefijo bi- significa dos o doble, como en la palabra biología\".</em>",
      "options": [
        "Función Poética",
        "Función Metalingüística",
        "Función Apelativa",
        "Función Referencial"
      ],
      "correct": 1,
      "explanation": "El texto utiliza el lenguaje para explicarse a sí mismo (la regla de formación de palabras de un prefijo). Esto corresponde estrictamente al código y por lo tanto es metalingüística."
    },
    {
      "text": "Identifica la forma del discurso que predomina en el siguiente texto: <em>\"Ayer por la tarde, la profesora de matemáticas entró al aula del IEMS, abrió su portafolio y sacó los exámenes\".</em>",
      "options": [
        "Texto Argumentativo",
        "Texto Descriptivo",
        "Texto Narrativo",
        "Texto Expositivo Puro"
      ],
      "correct": 2,
      "explanation": "Se narra una secuencia de acciones consecutivas y cronológicas realizadas en el pasado (\"entró\", \"abrió\", \"sacó\")."
    },
    {
      "text": "Identifica la opción en la cual las palabras subrayadas corresponden, en estricto orden, a un SUSTANTIVO ABSTRACTO, un ADJETIVO CALIFICATIVO y un PRONOMBRE PERSONAL:",
      "options": [
        "El <u>médico</u> diseñó un tratamiento <u>eficaz</u> para <u>él</u>.",
        "Su <u>paciencia</u> permitió un análisis <u>profundo</u>, lo que <u>le</u> valió el ingreso.",
        "La <u>curiosidad</u> de la alumna la llevó a leer <u>este</u> libro de <u>química</u>.",
        "Aquella <u>melodía</u> provocó una gran <u>alegría</u> en <u>nosotros</u>."
      ],
      "correct": 1,
      "explanation": "\"Paciencia\" es un sustantivo abstracto (depende de un ser para existir), \"profundo\" es un adjetivo que califica a análisis, y \"le\" es un pronombre personal que sustituye a una persona. En la opción D, \"melodía\" es un sustantivo concreto."
    },
    {
      "text": "Selecciona la opción que presenta una redacción y sintaxis CORRECTA:",
      "options": [
        "El grupo de investigadores analizaron las muestras toda la noche.",
        "El médico sugirió de que el paciente guardara reposo absoluto.",
        "Se aprobó la ley de salud, entrando en vigor al día siguiente.",
        "Compró un termo de acero inoxidable para el café."
      ],
      "correct": 3,
      "explanation": "La opción D es sintácticamente impecable. Las otras fallan por: concordancia colectiva errónea (A), dequeísmo (B), y gerundio ilegal de posterioridad (C)."
    },
    {
      "text": "Selecciona la opción que emplee de manera CORRECTA las tildes diacríticas:",
      "options": [
        "Para mi, tu eres la persona más importante.",
        "Para mí, tu eres la persona más importante.",
        "Para mí, tú eres la persona más importante.",
        "Para mi, tú eres la persona más importante."
      ],
      "correct": 2,
      "explanation": "\"mí\" y \"tú\" llevan tilde obligatoria aquí porque funcionan como pronombres personales independientes que sustituyen o refieren a las personas. Si no llevaran tilde serian adjetivos posesivos."
    }
  ]
};
