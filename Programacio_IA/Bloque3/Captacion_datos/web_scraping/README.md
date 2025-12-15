# Web Scraping - Clasificación LaLiga

Proyecto para extraer la clasificación de LaLiga desde Marca.com y guardarla en CSV.

## Archivos

- `scrape_marca_clasificacion.py` - Script principal para extraer datos
- `ver_clasificacion.py` - Visualiza los datos del CSV
- `requirements.txt` - Librerías necesarias
- `clasificacion_laliga.csv` - Datos extraídos (se genera automáticamente)

## Como usar

### 1. Crear entorno virtual

**Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar scraper

```bash
python scrape_marca_clasificacion.py
```

Esto genera el archivo `clasificacion_laliga.csv` con todos los datos.

### 4. Ver resultados

```bash
python ver_clasificacion.py
```

Muestra la tabla formateada y estadísticas (líder, goleador, mejor defensa, etc.)

## Datos extraídos

- Posición
- Nombre del equipo
- Partidos jugados (PJ)
- Ganados, Empatados, Perdidos
- Goles a favor y en contra
- Puntos

## Técnicas usadas

- Detección de componentes dinámicos (JavaScript)
- Uso de APIs JSON cuando están disponibles
- Fallback con BeautifulSoup si no hay API
- Exportación a CSV para análisis

## Requisitos

- Python 3.8+
- requests
- beautifulsoup4
- lxml
- pandas

## Notas

- Uso educativo solamente
- Respetar robots.txt y términos de uso del sitio
