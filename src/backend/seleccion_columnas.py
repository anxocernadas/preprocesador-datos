def obtener_columnas(datos):
    """
    Devuelve la lista de columnas disponibles en el dataset.
    """
    return list(datos.columns)


def validar_seleccion_columnas(columnas, indices_features, indice_target):
    """
    Valida que la selección de features y target sea correcta.
    """
    if not indices_features:
        raise ValueError("Debe seleccionar al menos una columna de entrada.")

    if indice_target is None:
        raise ValueError("Debe seleccionar una columna de salida.")

    if indice_target in indices_features:
        raise ValueError("El target no puede estar incluido en las features.")

    total_columnas = len(columnas)

    for indice in indices_features:
        if indice < 1 or indice > total_columnas:
            raise ValueError("Una o más columnas de entrada no son válidas.")

    if indice_target < 1 or indice_target > total_columnas:
        raise ValueError("La columna de salida no es válida.")


def seleccionar_columnas(datos, indices_features, indice_target):
    """
    Devuelve las columnas seleccionadas como features y target.
    """
    columnas = obtener_columnas(datos)

    validar_seleccion_columnas(columnas, indices_features, indice_target)

    features = [columnas[indice - 1] for indice in indices_features]
    target = columnas[indice_target - 1]

    return features, target