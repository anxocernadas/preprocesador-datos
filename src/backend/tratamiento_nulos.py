import pandas as pd

def obtener_columnas_seleccionadas(features, target):
    """
    Devuelve la lista de columnas seleccionadas para el preprocesado.
    """
    return features + [target]


def contar_valores_faltantes(datos, features, target):
    """
    Cuenta los valores faltantes solo en las columnas seleccionadas.
    """
    columnas = obtener_columnas_seleccionadas(features, target)

    faltantes = {}

    for columna in columnas:
        cantidad = int(datos[columna].isnull().sum())

        if cantidad > 0:
            faltantes[columna] = cantidad

    return faltantes


def hay_valores_faltantes(datos, features, target):
    """
    Indica si hay valores faltantes en las columnas seleccionadas.
    """
    faltantes = contar_valores_faltantes(datos, features, target)
    return len(faltantes) > 0


def eliminar_filas_con_nulos(datos, columnas):
    """
    Elimina filas con valores faltantes en las columnas seleccionadas.
    """
    return datos.dropna(subset=columnas)


def rellenar_con_media(datos, columnas):
    """
    Rellena valores faltantes con la media de cada columna numérica.
    """
    datos_copia = datos.copy()

    for columna in columnas:
        if pd.api.types.is_numeric_dtype(datos_copia[columna]):
            media = datos_copia[columna].mean()
            datos_copia[columna] = datos_copia[columna].fillna(media)

    return datos_copia


def rellenar_con_mediana(datos, columnas):
    """
    Rellena valores faltantes con la mediana de cada columna numérica.
    """
    datos_copia = datos.copy()

    for columna in columnas:
        if pd.api.types.is_numeric_dtype(datos_copia[columna]):
            mediana = datos_copia[columna].median()
            datos_copia[columna] = datos_copia[columna].fillna(mediana)

    return datos_copia


def rellenar_con_moda(datos, columnas):
    """
    Rellena valores faltantes con la moda de cada columna.
    """
    datos_copia = datos.copy()

    for columna in columnas:
        moda = datos_copia[columna].mode()

        if not moda.empty:
            datos_copia[columna] = datos_copia[columna].fillna(moda[0])

    return datos_copia


def rellenar_con_valor_constante(datos, columnas, valor):
    """
    Rellena valores faltantes con un valor constante.
    """
    datos_copia = datos.copy()

    for columna in columnas:
        datos_copia[columna] = datos_copia[columna].fillna(valor)

    return datos_copia