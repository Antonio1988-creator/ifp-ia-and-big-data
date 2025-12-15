# Script para ver la clasificación guardada en el CSV

import pandas as pd
import os

CSV_FILE = "clasificacion_laliga.csv"

def leer_clasificacion():
    if not os.path.exists(CSV_FILE):
        print(f"Error: No se encuentra el archivo '{CSV_FILE}'")
        print("Ejecuta primero: python scrape_marca_clasificacion.py")
        return None
    
    try:
        df = pd.read_csv(CSV_FILE)
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None


def mostrar_tabla(df):
    print("\n" + "="*80)
    print("  CLASIFICACIÓN LALIGA EA SPORTS 2025-26")
    print("="*80)
    print()
    
    # Configurar pandas
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 150)
    pd.set_option('display.max_columns', None)
    
    # Copiar para renombrar columnas
    df_display = df.copy()
    df_display.columns = ['Pos', 'Equipo', 'PJ', 'G', 'E', 'P', 'GF', 'GC', 'Pts']
    
    print(df_display.to_string(index=False))
    
    print("="*80)
    print(f"\nTotal de equipos: {len(df)}")
    print()


def mostrar_estadisticas(df):
    if df is None or df.empty:
        return
    
    print("\nESTADÍSTICAS DESTACADAS")
    print("-"*50)
    
    # Lider
    lider = df.loc[df['Puntos'].idxmax()]
    print(f"Líder: {lider['Equipo']} con {lider['Puntos']} puntos")
    
    # Mas goles
    goleador = df.loc[df['Goles a Favor'].idxmax()]
    print(f"Mayor goleador: {goleador['Equipo']} con {goleador['Goles a Favor']} goles")
    
    # Mejor defensa
    defensa = df.loc[df['Goles en Contra'].idxmin()]
    print(f"Mejor defensa: {defensa['Equipo']} con {defensa['Goles en Contra']} goles en contra")
    
    # Promedio
    promedio = df['Goles a Favor'].mean()
    print(f"Promedio de goles por equipo: {promedio:.2f}")
    
    # Diferencia goles
    df['Diferencia'] = df['Goles a Favor'] - df['Goles en Contra']
    mejor_diferencia = df.loc[df['Diferencia'].idxmax()]
    print(f"Mejor diferencia de goles: {mejor_diferencia['Equipo']} ({mejor_diferencia['Diferencia']:+d})")
    
    print("-"*50)
    print()


def main():
    print("\nVISUALIZADOR DE CLASIFICACIÓN - LALIGA")
    
    df = leer_clasificacion()
    if df is None or df.empty:
        return
    
    mostrar_tabla(df)
    mostrar_estadisticas(df)
    
    print("Datos leídos desde:", CSV_FILE)
    print()


if __name__ == "__main__":
    main()
