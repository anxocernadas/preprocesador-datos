import pandas as pd


def obtener_columnas_numericas(datos, columnas):
    """
    Devuelve las columnas numéricas dentro de una lista de columnas.
    """
    return [
        columna
        for columna in columnas
        if columna in datos.columns
        and pd.api.types.is_numeric_dtype(datos[columna])
    ]


def obtener_columnas_categoricas(datos, columnas):
    """
    Devuelve las columnas categóricas dentro de una lista de columnas.
    """
    return [
        columna
        for columna in columnas
        if columna in datos.columns
        and not pd.api.types.is_numeric_dtype(datos[columna])
    ]


def obtener_resumen_estadistico(datos, columnas):
    """
    Calcula resumen estadístico de columnas numéricas seleccionadas.
    """
    numericas = obtener_columnas_numericas(datos, columnas)

    resumen = {}

    for columna in numericas:
        resumen[columna] = {
            "media": datos[columna].mean(),
            "mediana": datos[columna].median(),
            "desviacion": datos[columna].std(),
            "minimo": datos[columna].min(),
            "maximo": datos[columna].max(),
            "percentil_25": datos[columna].quantile(0.25),
            "percentil_75": datos[columna].quantile(0.75),
        }

    return resumen


def obtener_distribucion_categorica(datos, columnas):
    """
    Calcula la distribución de valores en columnas categóricas.
    """
    categoricas = obtener_columnas_categoricas(datos, columnas)

    distribuciones = {}

    for columna in categoricas:
        distribuciones[columna] = datos[columna].value_counts().to_dict()

    return distribuciones