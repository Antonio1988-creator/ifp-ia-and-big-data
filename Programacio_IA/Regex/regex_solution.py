import re

"""
EJERCICIOS DE EXPRESIONES REGULARES - SOLUCIONES COMPLETAS
==========================================================
"""

print("=" * 60)
print("EJERCICIOS DE EXPRESIONES REGULARES")
print("=" * 60)

# ====================================================================
# EJERCICIO 1 — Encuentra todas las palabras que comienzan con "a"
# ====================================================================
print("""
EJERCICIO 1: Palabras que comienzan con 'a'
--------------------------------------------------
ENUNCIADO:
Dado el texto: 'Ana compró arroz, avena y almendras.'
• Encuentra todas las palabras que empiecen con la letra 'a' (mayúscula o minúscula)
• Usa re.findall() y un patrón con \\b (inicio de palabra) y [Aa]
""")

texto1 = "Ana compró arroz, avena y almendras."
patron1 = r'\b[Aa]\w*'
resultado1 = re.findall(patron1, texto1)

print(f"""Texto: {texto1}
Patrón usado: {patron1}
Palabras que empiezan con 'a': {resultado1}

EXPLICACIÓN:
• \\b: marca el inicio de una palabra
• [Aa]: coincide con 'A' mayúscula o 'a' minúscula
• \\w*: coincide con cero o más caracteres de palabra (letras, dígitos, guiones bajos)

LIMITACIÓN IMPORTANTE - Acentos:""")
texto_acentos = "Ana compró árbol, águila, ángel y almendras."
resultado_acentos = re.findall(patron1, texto_acentos)
print(f"""Texto con acentos: {texto_acentos}
Resultado con [Aa]: {resultado_acentos}
¡NO encuentra: árbol, águila, ángel! porque [Aa] no incluye á, Á

SOLUCIÓN para incluir acentos:""")
patron_con_acentos = r'\b[AaÁáÀàÂâÄäÃã]\w*'
resultado_con_acentos = re.findall(patron_con_acentos, texto_acentos)
print(f"""Patrón con acentos: {patron_con_acentos}
Resultado corregido: {resultado_con_acentos}
Ahora SÍ encuentra todas las palabras que empiezan por 'a' con o sin acentos""")

# ====================================================================
# EJERCICIO 2 — Extraer números de un texto
# ====================================================================
print("""

EJERCICIO 2: Extraer números de un texto
--------------------------------------------------
ENUNCIADO:
Dado el texto: 'Tengo 3 manzanas, 12 naranjas y 1 plátano.'
• Extrae todos los números usando \\d+
• Convierte los resultados a enteros y suma todos los números
""")

texto2 = "Tengo 3 manzanas, 12 naranjas y 1 plátano."
patron2 = r'\d+'
numeros_str = re.findall(patron2, texto2)
numeros_int = [int(num) for num in numeros_str] # lista de comprehensión
'''
Línea anterior es equivlente a esto:
numeros_int = []
for num in numeros_str:
    numeros_int.append(int(num))
'''
suma_total = sum(numeros_int)

print(f"""Texto: {texto2}
Patrón usado: {patron2}
Números encontrados (strings): {numeros_str}
Números convertidos a enteros: {numeros_int}
Suma total: {suma_total}

EXPLICACIÓN:
• \\d+: coincide con uno o más dígitos consecutivos
• re.findall() devuelve una lista de strings que coinciden con el patrón
• Convertimos cada string a entero con int() y sumamos todos""")

# ====================================================================
# EJERCICIO 3 — Validar un código postal
# ====================================================================
print("""

EJERCICIO 3: Validar códigos postales
--------------------------------------------------
ENUNCIADO:
Los códigos postales tienen 5 dígitos:
codigos = ['28013', '0800A', '5000', '12345']
• Escribe una expresión regular para validar códigos postales correctos (solo 5 dígitos)
• Imprime cuáles son válidos usando re.fullmatch()
""")

codigos = ["28013", "0800A", "5000", "12345"]
patron3 = r'\d{5}'

print(f"""Códigos a validar: {codigos}
Patrón usado: {patron3}
Validación de códigos postales:""")

'''
EXPLICACIÓN DETALLADA DEL BUCLE DE VALIDACIÓN DE CÓDIGOS POSTALES
================================================================

CÓDIGO ANALIZADO:
for codigo in codigos:
    es_valido = re.fullmatch(patron3, codigo) is not None
    print(f"  {codigo}: {'✓ VÁLIDO' if es_valido else '✗ INVÁLIDO'}")

DESGLOSE LÍNEA POR LÍNEA:
------------------------

1. for codigo in codigos:
   • Bucle for que itera sobre cada elemento de la lista 'codigos'
   • codigos = ["28013", "0800A", "5000", "12345"]
   • En cada iteración, 'codigo' toma el valor de un elemento:
     - Iteración 1: codigo = "28013"
     - Iteración 2: codigo = "0800A"
     - Iteración 3: codigo = "5000"
     - Iteración 4: codigo = "12345"

2. es_valido = re.fullmatch(patron3, codigo) is not None
   
   a) re.fullmatch(patron3, codigo):
      • patron3 = r'\d{5}' (exactamente 5 dígitos)
      • Verifica si TODA la cadena coincide con el patrón
      • Devuelve:
        - Objeto Match si hay coincidencia completa
        - None si no hay coincidencia
   
   b) is not None:
      • Convierte el resultado a booleano:
        - Objeto Match → True (válido)
        - None → False (inválido)
   
   c) Ejemplos paso a paso:
      • "28013": re.fullmatch(r'\d{5}', "28013") → <Match object>
                 <Match object> is not None → True
      • "0800A": re.fullmatch(r'\d{5}', "0800A") → None
                 None is not None → False
      • "5000":  re.fullmatch(r'\d{5}', "5000") → None (solo 4 dígitos)
                 None is not None → False

3. print(f"  {codigo}: {'✓ VÁLIDO' if es_valido else '✗ INVÁLIDO'}")
   
   a) f"..." (f-string):
      • String formateado que permite insertar variables con {}
   
   b) {codigo}:
      • Inserta el valor actual de la variable 'codigo'
   
   c) {'✓ VÁLIDO' if es_valido else '✗ INVÁLIDO'}:
      • OPERADOR TERNARIO (expresión condicional)
      • Sintaxis: valor_si_true if condicion else valor_si_false
      • Si es_valido es True → muestra '✓ VÁLIDO'
      • Si es_valido es False → muestra '✗ INVÁLIDO'
      
      Equivalente a:
      if es_valido:
          mensaje = '✓ VÁLIDO'
      else:
          mensaje = '✗ INVÁLIDO'
      print(f"  {codigo}: {mensaje}")

OBJETO MATCH - ¿QUÉ CONTIENE?
-----------------------------
Cuando re.fullmatch() encuentra una coincidencia, devuelve un objeto Match que contiene:

• .group(): El texto que coincidió
• .start(): Posición inicial de la coincidencia
• .end(): Posición final de la coincidencia
• .span(): Tupla (inicio, fin)
• .string: La cadena original que se buscó
• .re: El patrón compilado usado

Ejemplo:
match = re.fullmatch(r'\d{5}', "28013")
print(match)           # <re.Match object; span=(0, 5), match='28013'>
print(match.group())   # 28013
print(match.span())    # (0, 5)

DIFERENCIAS ENTRE FUNCIONES RE:
------------------------------
• re.findall(): Encuentra TODAS las coincidencias, devuelve lista
• re.search(): Encuentra la PRIMERA coincidencia en cualquier parte
• re.match(): Coincidencia solo al INICIO de la cadena
• re.fullmatch(): Coincidencia de TODA la cadena completa

SALIDA ESPERADA:
---------------
  28013: ✓ VÁLIDO    (5 dígitos exactos)
  0800A: ✗ INVÁLIDO  (contiene letra)
  5000: ✗ INVÁLIDO   (solo 4 dígitos)
  12345: ✓ VÁLIDO    (5 dígitos exactos)

CONCEPTOS CLAVE:
---------------
• Bucle for: itera sobre elementos de una lista
• re.fullmatch(): valida coincidencia completa
• is not None: convierte objeto/None a True/False
• Operador ternario: if/else compacto en una línea
• f-strings: formato de cadenas con variables insertadas
• Objeto Match: contiene información detallada de la coincidencia
'''

for codigo in codigos:
    es_valido = re.fullmatch(patron3, codigo) is not None
    print(f"  {codigo}: {'✓ VÁLIDO' if es_valido else '✗ INVÁLIDO'}")

print("""
EXPLICACIÓN:
• \\d{5}: coincide exactamente con 5 dígitos
• re.fullmatch() verifica que toda la cadena coincida con el patrón
• '0800A' es inválido porque contiene una letra
• '5000' es inválido porque solo tiene 4 dígitos""")

# ====================================================================
# EJERCICIO 4 — Reemplazar todas las vocales por "*"
# ====================================================================
print("""

EJERCICIO 4: Reemplazar vocales por '*'
--------------------------------------------------
ENUNCIADO:
Dado el texto: 'Hola mundo, esto es una prueba de regex.'
• Usa re.sub() para reemplazar todas las vocales (a, e, i, o, u) por *
• Ten en cuenta mayúsculas y minúsculas
""")

texto4 = "Hola mundo, esto es una prueba de regex."
patron4 = r'[aeiouAEIOU]'
resultado4 = re.sub(patron4, '*', texto4)

print(f"""Texto original: {texto4}
Patrón usado: {patron4}
Texto modificado: {resultado4}

EXPLICACIÓN:
• [aeiouAEIOU]: clase de caracteres que coincide con cualquier vocal
• re.sub(patrón, reemplazo, texto): reemplaza todas las coincidencias
• Incluimos tanto minúsculas como mayúsculas en la clase de caracteres""")

# ====================================================================
# EJERCICIO 5 — Extraer el dominio de emails
# ====================================================================
print("""

EJERCICIO 5: Extraer dominios de emails
--------------------------------------------------
ENUNCIADO:
Dado el texto: 'contacto@ejemplo.com, soporte@miweb.org, admin@test.net'
• Usa una expresión regular con grupos para extraer solo el dominio de cada email
• Imprime los dominios encontrados
""")

emails = "contacto@ejemplo.com, soporte@miweb.org, admin@test.net"
patron5 = r'\w+@(\w+\.\w+)'
dominios = re.findall(patron5, emails)

print(f"""Texto con emails: {emails}
Patrón usado: {patron5}
Dominios extraídos: {dominios}

EXPLICACIÓN:
• \\w+: coincide con el nombre del usuario (uno o más caracteres de palabra)
• @: coincide literalmente con el símbolo @
• (\\w+\\.\\w+): grupo que captura el dominio
  - \\w+: nombre del dominio
  - \\.: punto literal (escapado)
  - \\w+: extensión del dominio
• Los paréntesis crean un grupo de captura, re.findall() devuelve solo los grupos

DEMOSTRACIÓN - ¿Dominio o email completo?:""")
# Comparemos diferentes patrones
patron_con_grupo = r'\w+@(\w+\.\w+)'
resultado_con_grupo = re.findall(patron_con_grupo, emails)
patron_sin_grupo = r'\w+@\w+\.\w+'
resultado_sin_grupo = re.findall(patron_sin_grupo, emails)

print(f"""1. CON GRUPO (patrón actual):
   Patrón: {patron_con_grupo}
   Resultado: {resultado_con_grupo}
   → Solo devuelve el DOMINIO (contenido del grupo)

2. SIN GRUPO (email completo):
   Patrón: {patron_sin_grupo}
   Resultado: {resultado_sin_grupo}
   → Devuelve el EMAIL COMPLETO

3. ANÁLISIS DETALLADO:""")
for i, email in enumerate(['contacto@ejemplo.com', 'soporte@miweb.org', 'admin@test.net']):
    match = re.search(r'\w+@(\w+\.\w+)', email)
    if match:
        print(f"   Email {i+1}: {email}")
        print(f"     - Coincidencia completa: '{match.group()}'")
        print(f"     - Solo el dominio (grupo 1): '{match.group(1)}'")
        print(f"     - re.findall() devuelve: '{match.group(1)}'")

# ====================================================================
# EJERCICIO 6 — Detectar URLs en un texto
# ====================================================================
print("""

EJERCICIO 6: Detectar URLs
--------------------------------------------------
ENUNCIADO:
Dado el texto: 'Visita https://www.ejemplo.com o http://blog.ejemplo.org/post.'
• Encuentra todas las URLs que comiencen con http o https
• Usa re.findall() con un patrón que incluya https?:// y caracteres alfanuméricos, puntos o barras
""")

texto6 = "Visita https://www.ejemplo.com o http://blog.ejemplo.org/post."
patron6 = r'https?://[\w.-]+(?:/[\w.-]*)*'
urls = re.findall(patron6, texto6)

print(f"""Texto: {texto6}
Patrón usado: {patron6}
URLs encontradas: {urls}

EXPLICACIÓN:
• https?: 'http' seguido opcionalmente de 's'
• ://: coincide literalmente con '://'
• [\\w.-]+: uno o más caracteres de palabra, puntos o guiones (dominio)
• (?:/[\\w.-]*)*: grupo no capturador para la ruta opcional
  - /: barra literal
  - [\\w.-]*: cero o más caracteres válidos en la ruta
  - *: cero o más repeticiones del grupo completo""")

print(f"""
{'=' * 70}
EXPLICACIÓN COMPLETA DEL PATRÓN r'https?://[\\w.-]+(?:/[\\w.-]*)*'
{'=' * 70}

1. DESGLOSE PARTE POR PARTE:
------------------------------""")
patron_completo = r'https?://[\w.-]+(?:/[\w.-]*)*'
print(f"Patrón completo: {patron_completo}")
print()

partes = [
    ("https?", "Protocolo con 's' opcional"),
    ("://", "Separador de protocolo literal"), 
    ("[\\w.-]+", "Dominio (nombre + extensión)"),
    ("(?:/[\\w.-]*)*", "Ruta opcional (puede repetirse)")
]

for i, (parte, descripcion) in enumerate(partes, 1):
    print(f"{i}. '{parte}' → {descripcion}")

print("""
2. ANÁLISIS DETALLADO DE CADA COMPONENTE:
---------------------------------------------

🔹 PARTE 1: 'https?'
   • 'http' → coincide literalmente con las letras h-t-t-p
   • 's?' → la letra 's' es OPCIONAL (? = cero o una vez)
   • Coincide con: 'http' O 'https'
   • Ejemplos que coinciden:
     ✓ http://ejemplo.com
     ✓ https://ejemplo.com 
   • Ejemplos que NO coinciden:
     ✗ ftp://ejemplo.com (no empieza con http)
     ✗ httpss://ejemplo.com (doble s)

🔹 PARTE 2: '://'
   • Coincide LITERALMENTE con los 3 caracteres: :
   • : → dos puntos literal
   • // → dos barras literales
   • NO son metacaracteres aquí, se usan tal como están
   • Separador estándar entre protocolo y dominio

🔹 PARTE 3: '[\\w.-]+'
   • [\\w.-] → CLASE DE CARACTERES que incluye:
     - \\w → letras, dígitos, guión bajo (a-z, A-Z, 0-9, _)
     - . → punto literal (DENTRO de [] no es metacarácter)
     - - → guión literal
   • + → UNO O MÁS caracteres de la clase
   • Propósito: capturar el DOMINIO completo
   • Ejemplos que coinciden:
     ✓ www.ejemplo.com
     ✓ blog.ejemplo.org
     ✓ mi-sitio.net
     ✓ sitio123.co.uk
   • Ejemplos que NO coinciden:
     ✗ sitio con espacios.com (espacios no están en [\\w.-])

🔹 PARTE 4: '(?:/[\\w.-]*)*' (LA MÁS COMPLEJA)
   • (?:...) → GRUPO NO CAPTURADOR
     - Los paréntesis agrupan pero NO crean grupo de captura
     - ?: al inicio indica 'no capturar'
   • /[\\w.-]* → RUTA INDIVIDUAL:
     - / → barra literal (inicio de ruta)
     - [\\w.-]* → cero o más caracteres válidos en ruta
   • * exterior → el grupo completo puede repetirse cero o más veces
   • Propósito: capturar RUTAS OPCIONALES como /post, /blog/articulo

3. ¿POR QUÉ GRUPO NO CAPTURADOR (?:...)?
---------------------------------------------
• Si usáramos grupo capturador (/[\\w.-]*), re.findall() devolvería
  solo el contenido de los grupos, no la URL completa
• Con (?:...) agrupamos para aplicar * sin crear captura
• Así re.findall() devuelve la URL completa

4. EJEMPLOS PASO A PASO:
-------------------------""")

urls_ejemplo = [
    "https://www.ejemplo.com",
    "http://blog.ejemplo.org/post",
    "https://mi-sitio.net/blog/articulo"
]

for url in urls_ejemplo:
    print(f"\nAnalizando: {url}")
    match = re.search(patron_completo, url)
    if match:
        print(f"  ✓ Coincide completa: '{match.group()}'")
        print(f"  • Protocolo: {url.split('://')[0]}")
        print(f"  • Dominio: {url.split('://')[1].split('/')[0]}")
        if '/' in url.split('://')[1]:
            ruta = '/' + '/'.join(url.split('://')[1].split('/')[1:])
            print(f"  • Ruta: {ruta}")
        else:
            print(f"  • Ruta: (ninguna)")

# Comparación de patrones
patron_simple = r'https?://[\w.-]+'
patron_complejo = r'https?://[\w.-]+(?:/[\w.-]*)*'
texto_prueba = "Visita https://www.ejemplo.com o http://blog.ejemplo.org/post."
resultado_simple = re.findall(patron_simple, texto_prueba)
resultado_complejo = re.findall(patron_complejo, texto_prueba)

print(f"""
5. COMPARACIÓN CON PATRÓN SIN RUTA:
----------------------------------------
Patrón SIMPLE (sin ruta): {patron_simple}
Resultado: {resultado_simple}
¡PROBLEMA: No captura la ruta '/post'!

Patrón COMPLEJO (con ruta): {patron_complejo}  
Resultado: {resultado_complejo}
✓ CORRECTO: Captura URLs completas con rutas

6. CASOS EXTREMOS Y LIMITACIONES:
----------------------------------------""")

casos_extremos = [
    ("https://ejemplo.com/ruta/con/muchos/niveles", "✓ Funciona"),
    ("http://sub.dominio.ejemplo.com", "✓ Funciona"),
    ("https://sitio-con-guiones.com", "✓ Funciona"),
    ("https://ejemplo.com/ruta con espacios", "✗ Falla (espacios no permitidos)"),
    ("https://ejemplo.com/ruta?param=valor", "✗ Falla (? no incluido)"),
    ("https://ejemplo.com#seccion", "✗ Falla (# no incluido)")
]

for caso, resultado in casos_extremos:
    print(f"  {resultado} {caso}")

patron_mejorado = r'https?://[\w.-]+(?:/[\w./?=#&%-]*)*'
print(f"""
7. VERSIÓN MEJORADA PARA MÁS CASOS:
----------------------------------------
Patrón mejorado: {patron_mejorado}
• Añade: ? = # & % para parámetros y anclas
• Captura URLs con query strings y fragmentos

8. CONCEPTOS CLAVE UTILIZADOS:
-----------------------------------""")
conceptos = [
    "? → cuantificador opcional (cero o uno)",
    "+ → cuantificador (uno o más)",  
    "* → cuantificador (cero o más)",
    "[...] → clase de caracteres",
    "(?:...) → grupo no capturador",
    "\\w → caracteres de palabra",
    "Literales → caracteres sin significado especial"
]

for concepto in conceptos:
    print(f"  • {concepto}")

print("""
9. APLICACIONES PRÁCTICAS:
------------------------------
• Extraer enlaces de páginas web
• Validar URLs en formularios 
• Limpiar texto convirtiendo URLs en enlaces
• Análisis de logs de servidor
• Detectar URLs maliciosas en texto

# ====================================================================
# EJERCICIO 7 — Validar contraseñas simples
# ====================================================================

EJERCICIO 7: Validar contraseñas
--------------------------------------------------
ENUNCIADO:
Una contraseña válida debe:
• Tener al menos 6 caracteres
• Incluir una letra mayúscula y un dígito
contrasenas = ['abc123', 'Password1', 'pass', '123456A']
• Usa re.fullmatch() para validar cada contraseña y muestra cuáles son correctas
""")

contrasenas = ["abc123", "Password1", "pass", "123456A"]
# Patrón que requiere: al menos 6 caracteres, al menos 1 mayúscula, al menos 1 dígito
patron7 = r'^(?=.*[A-Z])(?=.*\d).{6,}$'

print(f"""Contraseñas a validar: {contrasenas}
Patrón usado: {patron7}
Validación de contraseñas:""")

for password in contrasenas:
    es_valida = re.fullmatch(patron7, password) is not None
    print(f"  {password}: {'✓ VÁLIDA' if es_valida else '✗ INVÁLIDA'}")

print("""
EXPLICACIÓN:
• ^: inicio de cadena
• (?=.*[A-Z]): lookahead positivo - debe contener al menos una mayúscula
• (?=.*\\d): lookahead positivo - debe contener al menos un dígito
• .{6,}: cualquier carácter, mínimo 6 veces
• $: fin de cadena
• Los lookaheads verifican condiciones sin consumir caracteres""")

# ====================================================================
# EJERCICIO 8 — Extraer hashtags de un texto
# ====================================================================
print("""

EJERCICIO 8: Extraer hashtags
--------------------------------------------------
ENUNCIADO:
Dado el texto: 'Hoy es un gran día #sol #vacaciones #Python3'
• Encuentra todos los hashtags que comiencen con # y contengan letras, números o guiones bajos (\\w)
• Usa re.findall() y captura solo el texto del hashtag sin el #
""")

texto8 = "Hoy es un gran día #sol #vacaciones #Python3"
patron8 = r'#(\w+)'
hashtags = re.findall(patron8, texto8)

print(f"""Texto: {texto8}
Patrón usado: {patron8}
Hashtags encontrados: {hashtags}

EXPLICACIÓN:
• #: coincide literalmente con el símbolo #
• (\\w+): grupo que captura uno o más caracteres de palabra
• \\w incluye letras, dígitos y guiones bajos
• Los paréntesis hacen que re.findall() devuelva solo el contenido del grupo
• Así obtenemos los hashtags sin el símbolo #""")

# ====================================================================
# EJERCICIO 9 — Separar palabras por múltiples delimitadores
# ====================================================================
print("""

EJERCICIO 9: Separar por múltiples delimitadores
--------------------------------------------------
ENUNCIADO:
Dado el texto: 'manzana, pera; uva-mango naranja'
• Separa las palabras usando ,, ;, - o espacios como delimitadores
• Usa re.split() y elimina los posibles espacios extra alrededor de las palabras
""")

texto9 = "manzana, pera; uva-mango naranja"
patron9 = r'[,;\-\s]+'
palabras_raw = re.split(patron9, texto9)
palabras = [palabra.strip() for palabra in palabras_raw if palabra.strip()]

print(f"""Texto: {texto9}
Patrón usado: {patron9}
Palabras separadas (raw): {palabras_raw}
Palabras limpias: {palabras}

EXPLICACIÓN:
• [,;\\-\\s]+: clase de caracteres que incluye:
  - ,: coma
  - ;: punto y coma
  - \\-: guión (escapado porque está en una clase de caracteres)
  - \\s: cualquier espacio en blanco
  - +: uno o más de estos delimitadores consecutivos
• re.split() divide la cadena en cada coincidencia del patrón
• strip() elimina espacios y filter() elimina cadenas vacías""")

# ====================================================================
# EJERCICIO 10 — Encontrar palabras repetidas consecutivas
# ====================================================================
print("""

EJERCICIO 10: Palabras repetidas consecutivas
--------------------------------------------------
ENUNCIADO:
Dado el texto: 'Hola hola mundo mundo test test test'
• Encuentra las palabras que se repiten una o más veces consecutivas
• Usa un patrón con grupos y cuantificadores, y re.findall()
""")

texto10 = "Hola hola mundo mundo test test test"
patron10 = r'\b(\w+)(?:\s+\1)+\b'
repetidas = re.findall(patron10, texto10, re.IGNORECASE)

print(f"""Texto: {texto10}
Patrón usado: {patron10}
Palabras que se repiten: {repetidas}

EXPLICACIÓN:
• \\b: límite de palabra
• (\\w+): grupo que captura la primera palabra
• (?:\\s+\\1)+: grupo no capturador que busca repeticiones:
  - \\s+: uno o más espacios
  - \\1: referencia al primer grupo (la palabra capturada)
  - +: una o más repeticiones de este patrón
• re.IGNORECASE: hace la búsqueda insensible a mayúsculas/minúsculas
• \\1 es una referencia hacia atrás que coincide con el mismo texto del primer grupo

{('=' * 60)}
TODOS LOS EJERCICIOS COMPLETADOS
{('=' * 60)}""")
