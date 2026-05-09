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