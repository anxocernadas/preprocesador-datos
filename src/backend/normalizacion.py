import pandas as pd


def detectar_columnas_numericas(datos, features):
    """
    Detecta columnas numéricas dentro de las variables de entrada.
    """
    numericas = []

    for columna in features:
        if pd.api.types.is_numeric_dtype(datos[columna]):
            numericas.append(columna)

    return numericas


def hay_columnas_numericas(datos, features):
    """
    Indica si existen columnas numéricas en las features seleccionadas.
    """
    return len(detectar_columnas_numericas(datos, features)) > 0