 # Funciones para cargar datos (CSV, Excel, SQLite)

import os
import pandas as pd
import sqlite3

def cargar_csv(ruta_archivo: str) -> pd.DataFrame:
    """
    Carga un archivo CSV y devuelve su contenido como DataFrame.
    Soporta separadores habituales como coma o punto y coma.
    """
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No existe el archivo: {ruta_archivo}")

    if not ruta_archivo.lower().endswith(".csv"):
        raise ValueError("El archivo debe tener extensión .csv")

    try:
        return pd.read_csv(ruta_archivo, sep=None, engine="python")
    except Exception as error:
        raise ValueError(f"No se pudo cargar el archivo CSV: {error}")
    
def obtener_hojas_excel(ruta_archivo: str) -> list[str]:
    """
    Devuelve la lista de hojas disponibles en un archivo Excel.
    """
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No existe el archivo: {ruta_archivo}")

    if not ruta_archivo.lower().endswith(".xlsx"):
        raise ValueError("El archivo debe tener extensión .xlsx")

    try:
        return pd.ExcelFile(ruta_archivo).sheet_names
    except Exception as error:
        raise ValueError(f"No se pudieron leer las hojas del archivo Excel: {error}")


def cargar_excel(ruta_archivo: str, hoja: str | None = None) -> pd.DataFrame:
    """
    Carga un archivo Excel y devuelve su contenido como DataFrame.
    Si no se indica hoja, carga la primera hoja.
    """
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No existe el archivo: {ruta_archivo}")

    if not ruta_archivo.lower().endswith(".xlsx"):
        raise ValueError("El archivo debe tener extensión .xlsx")

    try:
        return pd.read_excel(ruta_archivo, sheet_name=hoja if hoja else 0)
    except Exception as error:
        raise ValueError(f"No se pudo cargar el archivo Excel: {error}")
    

def obtener_tablas_sqlite(ruta_archivo: str) -> list[str]:
    """
    Devuelve las tablas disponibles en una base de datos SQLite.
    """
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No existe el archivo: {ruta_archivo}")

    if not ruta_archivo.lower().endswith((".sqlite", ".db")):
        raise ValueError("El archivo debe tener extensión .sqlite o .db")

    try:
        conexion = sqlite3.connect(ruta_archivo)
        cursor = conexion.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = [fila[0] for fila in cursor.fetchall()]

        conexion.close()
        return tablas

    except Exception as error:
        raise ValueError(f"No se pudieron obtener las tablas: {error}")


def cargar_sqlite(ruta_archivo: str, tabla: str) -> pd.DataFrame:
    """
    Carga una tabla de una base de datos SQLite.
    """
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No existe el archivo: {ruta_archivo}")
    
    if not ruta_archivo.lower().endswith((".sqlite", ".db")):
        raise ValueError("El archivo debe tener extensión .sqlite o .db")    

    try:
        conexion = sqlite3.connect(ruta_archivo)
        df = pd.read_sql_query(f"SELECT * FROM {tabla}", conexion)
        conexion.close()
        return df

    except Exception as error:
        raise ValueError(f"No se pudo cargar la tabla: {error}")