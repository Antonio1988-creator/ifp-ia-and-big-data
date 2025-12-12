# Ejemplo simple: consultar PokeAPI y mostrar datos en DataFrame
# Advertencia: en el ejercicio/trabajo que tendréis que hacer tendréis que usar
# todas las convenciones y buenas prácticas (como comprobar el estado de la respuesta)

import requests
import pandas as pd

# 1. Hacer petición GET a la API
pokemon = input("Nombre del Pokémon: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
respuesta = requests.get(url)

# 2. Obtener JSON
datos = respuesta.json()

# 3. Extraer algunos datos
nombre = datos["name"]
id_num = datos["id"]
tipos = [t["type"]["name"] for t in datos["types"]]
peso = datos["weight"]
altura = datos["height"]

# 4. Crear DataFrame
df = pd.DataFrame([{
    "Nombre": nombre,
    "ID": id_num,
    "Tipos": ", ".join(tipos),
    "Peso": peso,
    "Altura": altura
}])

# 5. Mostrar DataFrame
print("\n--- Datos del Pokémon ---")
print(df)

# 6. Descargar y mostrar imagen
url_imagen = datos["sprites"]["front_default"]
imagen = requests.get(url_imagen)

# Guardar imagen
with open(f"{pokemon}.png", "wb") as f:
    f.write(imagen.content)

'''
Método tradicional para guardar(sin with):
f = open(f"{pokemon}.png", "wb")
f.write(imagen.content)
f.close()  # ¡Importante! Hay que cerrar manualmente el archivo

Ventaja del 'with': cierra el archivo automáticamente aunque haya errores
'''

print(f"\nImagen guardada: {pokemon}.png")

for move in datos["moves"][:5]:  # Mostrar solo los primeros 5 movimientos
    print(f"- {move['move']['name']}")