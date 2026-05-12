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


def aplicar_min_max_scaling(datos, columnas):
    """
    Aplica Min-Max Scaling a las columnas numéricas seleccionadas.
    """
    datos_copia = datos.copy()

    for columna in columnas:
        minimo = datos_copia[columna].min()
        maximo = datos_copia[columna].max()

        if maximo != minimo:
            datos_copia[columna] = (
                (datos_copia[columna] - minimo)
                / (maximo - minimo)
            )

    return datos_copia


def aplicar_z_score(datos, columnas):
    """
    Aplica normalización Z-score a las columnas numéricas seleccionadas.
    """
    datos_copia = datos.copy()

    for columna in columnas:
        media = datos_copia[columna].mean()
        desviacion = datos_copia[columna].std()

        if desviacion != 0:
            datos_copia[columna] = (
                (datos_copia[columna] - media)
                / desviacion
            )

    return datos_copia