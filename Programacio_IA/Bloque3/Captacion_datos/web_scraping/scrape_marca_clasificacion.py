# Script para extraer la clasificación de LaLiga desde Marca.com
# Guarda los datos en clasificacion_laliga.csv

import requests
from bs4 import BeautifulSoup
import sys
import csv
from datetime import datetime

URL = "https://www.marca.com/resultados/futbol/barcelona/clasificacion/2025/C178.html"


def fetch_html(url, timeout=15):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Scraper/1.0; +https://example.com)"
    }
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def find_standings_tables(soup):
    # Buscar tablas que parezcan una clasificación
    possible_tables = []
    keywords = {"Equipo", "Puntos", "P.J", "PJ", "P", "P.G", "PG", "J", "J."}

    for table in soup.find_all("table"):
        headers = [th.get_text(strip=True) for th in table.find_all("th")]
        header_text = " ".join(headers).upper()
        if any(k.upper() in header_text for k in keywords):
            possible_tables.append((table, headers))

    return possible_tables


def find_table_ranking_url(soup):
    # Marca usa un componente que carga datos con JavaScript
    tag = soup.find(lambda t: t.has_attr("table-ranking-url") if t and hasattr(t, 'attrs') else False)
    if tag:
        return tag.attrs.get("table-ranking-url")
    
    tag2 = soup.find("ue-table-ranking")
    if tag2 and tag2.has_attr("table-ranking-url"):
        return tag2["table-ranking-url"]
    return None


def fetch_json(url, timeout=15):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; Scraper/1.0; +https://example.com)", "Accept": "application/json"}
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def save_to_csv(data, filename):
    if not data:
        print("No hay datos para guardar.")
        return
    
    fieldnames = list(data[0].keys())
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"\nDatos guardados en: {filename}")
    print(f"Total de equipos: {len(data)}")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def parse_table(table):
    rows = []
    for tr in table.find_all("tr"):
        cols = [td.get_text(" ", strip=True) for td in tr.find_all(["td", "th"])]
        if not cols:
            continue
        rows.append(cols)
    return rows


def extract_team_and_points(row):
    team = None
    points = None
    
    # Identificar columnas numéricas
    numeric_cols = []
    for i, c in enumerate(row):
        # eliminar miles y otros caracteres
        raw = c.replace(".", "").replace(",", "")
        if raw.isdigit():
            numeric_cols.append(i)

    # Si hay columnas numéricas y la última es numérica, tomarla como puntos
    if numeric_cols:
        if numeric_cols[-1] == len(row) - 1:
            points = row[-1]
    # elegir team como primera columna no numérica (excepto si empieza por '#')
    for i, c in enumerate(row):
        raw = c.strip()
        if raw == "":
            continue
        # ignorar columnas que sólo contienen números o signos de posición
        if raw.replace(".", "").isdigit() or raw.startswith("#"):
            continue
        team = raw
        break

    return team, points


def main():
    print("Extrayendo:", URL)
    try:
        html = fetch_html(URL)
    except Exception as e:
        print("Error al descargar la página:", e)
        sys.exit(1)

    soup = BeautifulSoup(html, "lxml")

    # Primero: buscar si la página inyecta la tabla mediante un componente que
    # tiene un endpoint JSON (esto es lo que hace Marca con `ue-table-ranking`).
    ranking_url = find_table_ranking_url(soup)
    if ranking_url:
        # BeautifulSoup decodifica entidades, así que &amp; -> & estará bien.
        print("Componente dinámico detectado. Solicitando datos JSON desde:", ranking_url)
        try:
            data = fetch_json(ranking_url)
        except Exception as e:
            print("Error al obtener JSON desde el endpoint:", e)
            sys.exit(1)

        # La estructura esperada: {status:..., data: [ { rank: [...] } ] }
        try:
            block = data.get("data", [])[0]
            ranks = block.get("rank", [])
        except Exception:
            print("Estructura JSON inesperada. Imprimiendo keys:", list(data.keys()))
            sys.exit(1)

        if not ranks:
            print("No hay elementos de 'rank' en el JSON.")
            sys.exit(1)

        print("\nClasificación (desde API JSON):")
        csv_data = []
        for item in ranks:
            pos = item.get("standing", {}).get("position") or "?"
            name = item.get("name") or item.get("fullName") or ""
            points = item.get("standing", {}).get("points") or "0"
            played = item.get("standing", {}).get("played") or "0"
            won = item.get("standing", {}).get("won") or "0"
            drawn = item.get("standing", {}).get("drawn") or "0"
            lost = item.get("standing", {}).get("lost") or "0"
            goals_for = item.get("standing", {}).get("for") or "0"
            goals_against = item.get("standing", {}).get("against") or "0"
            
            print(f"{pos:>2s}. {name:30s} PJ:{played:>2s} Pts:{points:>3s} Gf:{goals_for:>3s} Ga:{goals_against:>3s}")
            
            csv_data.append({
                "Posición": pos,
                "Equipo": name,
                "Partidos Jugados": played,
                "Ganados": won,
                "Empatados": drawn,
                "Perdidos": lost,
                "Goles a Favor": goals_for,
                "Goles en Contra": goals_against,
                "Puntos": points
            })

        # Guardar en CSV
        save_to_csv(csv_data, "clasificacion_laliga.csv")
        
        # Mostrar fila de Barcelona si existe
        print("\nFila buscada para 'Barcelona':")
        for item in ranks:
            if item.get("name", "").lower().startswith("barcelona"):
                print(f"  Posición: {item.get('standing', {}).get('position')}")
                print(f"  Equipo: {item.get('name')}")
                print(f"  Puntos: {item.get('standing', {}).get('points')}")
                print(f"  Partidos: {item.get('standing', {}).get('played')}")
                break
        else:
            print("No se encontró 'Barcelona' en los resultados JSON.")
        return

    # Si no hay componente dinámico, intentar parsear tablas estáticas con BeautifulSoup
    tables = find_standings_tables(soup)
    if not tables:
        print("No se encontraron tablas de clasificación claramente identificables.")
        # Como fallback, intentar coger la primera tabla grande
        first_table = soup.find("table")
        if not first_table:
            print("No hay tablas en la página.")
            sys.exit(1)
        tables = [(first_table, [])]

    # Tomar la primera tabla candidata
    table, headers = tables[0]
    print("Usando una tabla candidata con encabezados:", headers)
    rows = parse_table(table)

    parsed = []
    for row in rows:
        team, points = extract_team_and_points(row)
        if team:
            parsed.append({"row": row, "team": team, "points": points})

    if not parsed:
        print("No se pudo extraer filas con equipos desde la tabla seleccionada.")
        sys.exit(1)

    print("\nClasificación (lista simplificada):")
    csv_data = []
    for i, item in enumerate(parsed, start=1):
        team = item["team"]
        points = item["points"] or "0"
        print(f"{i:2d}. {team:40s} Puntos: {points}")
        
        csv_data.append({
            "Posición": str(i),
            "Equipo": team,
            "Puntos": points
        })
    
    # Guardar en CSV
    save_to_csv(csv_data, "clasificacion_laliga.csv")

    # Buscar específicamente la fila del Barça
    print("\nFila buscada para 'Barcelona':")
    for item in parsed:
        if "barcelona" in item["team"].lower():
            print(f"  Equipo: {item['team']}")
            print(f"  Puntos: {item['points']}")
            break
    else:
        print("No se encontró 'Barcelona' en la tabla (la ciudad/club puede aparecer con otro formato).")


if __name__ == "__main__":
    main()
