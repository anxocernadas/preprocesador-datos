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


def obtener_mascara_atipicos(datos, columna):
    """
    Devuelve una máscara booleana indicando qué filas tienen valores atípicos
    usando el método IQR.
    """
    q1 = datos[columna].quantile(0.25)
    q3 = datos[columna].quantile(0.75)
    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    return (
        (datos[columna] < limite_inferior)
        | (datos[columna] > limite_superior)
    )


def contar_valores_atipicos(datos, features):
    """
    Cuenta valores atípicos en columnas numéricas seleccionadas.
    """
    numericas = detectar_columnas_numericas(datos, features)

    atipicos = {}

    for columna in numericas:
        cantidad = int(obtener_mascara_atipicos(datos, columna).sum())

        if cantidad > 0:
            atipicos[columna] = cantidad

    return atipicos