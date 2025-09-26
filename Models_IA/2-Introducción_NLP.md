### 0. Introducción a los **NLP (Natural Language Processing)**

El **Procesamiento de Lenguaje Natural (NLP, por sus siglas en inglés)** es un área de la inteligencia artificial que estudia cómo lograr que las máquinas entiendan, interpreten y produzcan el lenguaje humano. Su propósito principal es **reducir la distancia entre la forma en que las personas nos comunicamos (con palabras, frases, textos) y la manera en que las computadoras funcionan (con datos y números).**

Podemos pensarlo así:

* Las **personas** usamos un lenguaje lleno de matices, significados ocultos, expresiones coloquiales, emociones, ironías, etc.
* Las **máquinas**, en cambio, procesan información de manera estricta, siguiendo reglas matemáticas y estadísticas.

El NLP busca un **punto de encuentro** entre ambos mundos, permitiendo que los sistemas informáticos realicen tareas como:

* **Clasificación de textos** (por ejemplo, distinguir entre spam y no spam en un correo).
* **Traducción automática** (de un idioma a otro).
* **Reconocimiento de sentimientos** (detectar si un comentario en redes sociales es positivo, negativo o neutro).
* **Asistentes virtuales** (como los que entienden preguntas y generan respuestas).

En pocas palabras: el NLP es el **puente** que hace posible que el lenguaje humano se transforme en algo que una computadora pueda **analizar**, y que a su vez, la computadora nos devuelva un resultado que podamos **comprender**.

---

## 1. ¿De qué partes se compone el NLP?

El NLP combina **lingüística** (el estudio del lenguaje) con **informática** y **estadística**. Para hacerlo posible, se suelen distinguir varias etapas o módulos principales:

1. **Preprocesamiento del lenguaje**

   * Consiste en “limpiar” y preparar el texto antes de analizarlo.
   * Ejemplos:

     * **Tokenización**: dividir un texto en unidades más pequeñas (palabras o frases).
     * **Lematización**: reducir las palabras a su forma base (*correr → correr, corría, corrimos*).
     * **Eliminación de “stop words”**: quitar palabras muy frecuentes que no aportan mucho sentido (*el, la, de, que*).

2. **Análisis morfosintáctico**

   * Identificar la función de cada palabra en la oración: sustantivos, verbos, adjetivos…
   * Determinar la estructura de la oración (quién hace qué a quién).

3. **Análisis semántico**

   * Tratar de comprender el **significado** de las palabras en su contexto.
   * Ejemplo: distinguir entre “banco” como institución financiera o “banco” como asiento.

4. **Análisis pragmático y discursivo**

   * Considerar el contexto más amplio: la intención del hablante, la situación de comunicación, lo que se dijo antes y después.

---

## 2. Tipos de enfoques en el NLP

El NLP ha evolucionado a lo largo del tiempo, y con ello los métodos para abordarlo:

1. **Reglas lingüísticas (enfoque clásico)**

   * Al inicio, se intentó enseñar a las computadoras a través de reglas gramaticales explícitas.
   * Problema: el lenguaje humano es demasiado complejo y lleno de excepciones.

2. **Enfoque estadístico**

   * A partir de los años 90, se empezó a usar probabilidad y estadística.
   * Ejemplo: modelos que calculan cuál es la palabra más probable que siga a otra.

3. **Aprendizaje automático (Machine Learning)**

   * Los sistemas ya no dependen de reglas escritas por humanos, sino de **aprender patrones** a partir de grandes conjuntos de datos.

4. **Aprendizaje profundo (Deep Learning)**

   * La etapa más actual, donde las **redes neuronales profundas** permiten modelos mucho más potentes y flexibles.
   * Aquí se ubican los modelos que hoy usamos en chatbots, traducción automática y asistentes virtuales.

---

## 3. Desarrollo histórico del NLP

El NLP no apareció de la nada; ha recorrido varias fases:

* **Década de 1950**: Primeras traducciones automáticas, basadas en reglas.
* **Década de 1980-1990**: Auge de los métodos estadísticos y corpus (grandes bases de datos de textos).
* **Década de 2000**: Integración del *Machine Learning*.
* **Desde 2010**: Con el *Deep Learning* y los modelos de redes neuronales, el NLP logra avances sorprendentes, como la traducción casi instantánea o los chatbots conversacionales.

---

## 🌍 Ejemplos cotidianos del NLP

1. **Correos electrónicos (filtro de spam)**

   * Cuando Gmail u otro servicio decide si un correo es *spam* o no, está usando NLP.
   * El sistema analiza las palabras, expresiones y patrones típicos de mensajes fraudulentos.

2. **Traductores automáticos (Google Translate, DeepL, etc.)**

   * Permiten pasar de un idioma a otro en segundos.
   * Usan NLP para **entender el sentido** del texto original y **reproducirlo** en la otra lengua.

3. **Asistentes virtuales (Siri, Alexa, Google Assistant, ChatGPT)**

   * Reconocen lo que el usuario dice o escribe.
   * Interpretan la intención y generan una respuesta adecuada.

4. **Motores de búsqueda (Google, Bing, etc.)**

   * Cuando escribimos “restaurantes cerca de mí”, el buscador no solo busca esas palabras, sino que **interpreta la intención** detrás de la consulta.

5. **Redes sociales (análisis de sentimientos)**

   * Empresas y plataformas usan NLP para saber si un comentario es positivo, negativo o neutro.
   * Ejemplo: detectar reacciones a una campaña publicitaria en Twitter/X.

6. **Correctores ortográficos y sugerencias de texto (Word, teclado del móvil)**

   * El NLP permite que tu celular te sugiera la próxima palabra o detecte errores gramaticales.

7. **Subtítulos automáticos (YouTube, TikTok, Netflix)**

   * El sistema convierte audio en texto (*speech-to-text*) y lo sincroniza con el video.

---

# 📝 Del NLP al NLG (Natural Language Generation)

## 1. ¿Qué es el NLG?

El **Natural Language Generation (Generación de Lenguaje Natural)** es la parte del NLP encargada no solo de **entender el lenguaje**, sino de **producirlo de manera automática y comprensible para los humanos**.

Mientras que en el NLP hablamos de *procesar, analizar y comprender*, en el NLG el objetivo es **crear frases, párrafos o textos completos** que tengan coherencia, gramática correcta y un estilo natural.

👉 En pocas palabras: **NLP interpreta, NLG habla.**

---

## 2. Etapas del NLG

La generación de lenguaje natural suele dividirse en tres fases:

1. **Determinación de contenido**

   * El sistema decide *qué información* se quiere comunicar.
   * Ejemplo: un software meteorológico selecciona los datos de temperatura, viento y lluvia.

2. **Planificación del texto**

   * Organiza esa información en un orden lógico y estructurado.
   * Ejemplo: primero dice la temperatura, luego la probabilidad de lluvia.

3. **Realización del lenguaje**

   * Convierte la información estructurada en frases gramaticales y fluidas.
   * Ejemplo: *“Hoy la temperatura máxima será de 25 grados y existe un 40% de probabilidad de lluvia por la tarde.”*

---

## 3. Ejemplos de NLG en la vida real

* **Reportes automáticos**

  * Empresas financieras generan reportes diarios sobre el mercado sin intervención humana.

* **Noticias automáticas**

  * Algunos periódicos usan NLG para crear notas simples (como resultados deportivos o estadísticas electorales).

* **Asistentes conversacionales**

  * Cuando un chatbot responde a una pregunta con un texto completo y natural, está usando NLG.

* **Aplicaciones de accesibilidad**

  * Sistemas que generan descripciones automáticas de imágenes para personas con discapacidad visual.

---

## 4. Relación NLP ↔ NLG

* El **NLP analiza y comprende** lo que decimos.
* El **NLG genera** una respuesta entendible.

Ejemplo con un asistente virtual:

1. El usuario dice: *“¿Va a llover mañana en l'Hospitalet del Llobregat?”*
2. El **NLP** interpreta la pregunta (intención: saber el clima; lugar: l'Hospitalet del Llobregat; tiempo: mañana).
3. El sistema consulta los datos meteorológicos.
4. El **NLG** construye la respuesta: *“Mañana en l'Hospitalet del Llobregat se esperan lluvias ligeras durante la tarde.”*

---

# 🤖 De NLP y NLG a los LLM (Large Language Models)

## 1. ¿Qué es un LLM?

Un **Large Language Model** es un modelo de inteligencia artificial entrenado con **cantidades masivas de texto** (libros, artículos, conversaciones, páginas web, etc.) para aprender los **patrones del lenguaje humano**.

* “Large” se refiere a la **escala**: millones o incluso **billones de parámetros** (las conexiones internas del modelo).
* Son modelos capaces de **predecir la siguiente palabra** en una secuencia de texto, pero al entrenarse con tanto material y tantas capas neuronales, terminan siendo capaces de:

  * Responder preguntas.
  * Escribir ensayos, resúmenes o historias.
  * Traducir idiomas.
  * Mantener conversaciones fluidas.

👉 En pocas palabras: un LLM es como un **gran cerebro artificial del lenguaje**, construido a partir de muchísimos ejemplos.

---

## 2. Relación entre NLP, NLG y LLM

* **NLP** = Procesar y entender el lenguaje.
* **NLG** = Generar lenguaje natural.
* **LLM** = El motor que hoy hace posible ambos procesos a gran escala y con gran naturalidad.

Es decir:

* Antes, NLP y NLG eran procesos **separados** y con limitaciones.
* Con los **LLM**, ambas tareas se **fusionan**: el mismo modelo puede entender y generar con sorprendente fluidez.

---

## 3. Ejemplos de LLM en acción

* **Chatbots avanzados**: ChatGPT, Bard, Claude…
* **Herramientas de escritura**: asistentes que corrigen estilo o proponen mejoras (Grammarly, Notion AI).
* **Traducciones instantáneas** de alta calidad.
* **Programación asistida**: modelos como GitHub Copilot que generan código a partir de instrucciones en lenguaje natural.
* **Educación personalizada**: tutores virtuales que adaptan explicaciones al nivel del estudiante.

---

## 4. ¿Por qué los LLM son tan revolucionarios?

* Porque ya no dependen de reglas o de bases de datos específicas, sino de haber aprendido **patrones generales del lenguaje humano**.
* Esto les da una flexibilidad enorme: un mismo modelo puede responder a temas muy distintos (ciencia, literatura, deportes, programación).
* Han hecho posible un **salto cualitativo** en la interacción humano-máquina: ya no solo nos entienden, ahora también **conversan y crean**.

---

📌 Entonces, el recorrido queda así:

* **NLP**: entender y procesar el lenguaje.
* **NLG**: generar lenguaje humano de forma automática.
* **LLM**: modelos gigantes que combinan ambas cosas y las llevan a otro nivel.

---

