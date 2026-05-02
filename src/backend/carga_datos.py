 # Funciones para cargar datos (CSV, Excel, SQLite)

import os
import pandas as pd


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