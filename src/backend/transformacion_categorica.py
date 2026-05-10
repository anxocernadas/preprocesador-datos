import pandas as pd


def detectar_columnas_categoricas(datos, features):
    """
    Detecta columnas categóricas dentro de las variables de entrada.
    """
    categoricas = []

    for columna in features:
        if (
            pd.api.types.is_object_dtype(datos[columna])
            or pd.api.types.is_string_dtype(datos[columna])
            or pd.api.types.is_categorical_dtype(datos[columna])
        ):
            categoricas.append(columna)

    return categoricas


def hay_columnas_categoricas(datos, features):
    """
    Indica si existen columnas categóricas en las features seleccionadas.
    """
    return len(detectar_columnas_categoricas(datos, features)) > 0

from sklearn.preprocessing import LabelEncoder

def aplicar_one_hot_encoding(datos, columnas):
    """
    Aplica One-Hot Encoding a las columnas categóricas seleccionadas.
    """
    return pd.get_dummies(
        datos,
        columns=columnas,
        dtype=int,
    )


def aplicar_label_encoding(datos, columnas):
    """
    Aplica Label Encoding a las columnas categóricas seleccionadas.
    """
    datos_copia = datos.copy()

    for columna in columnas:
        encoder = LabelEncoder()

        datos_copia[columna] = encoder.fit_transform(
            datos_copia[columna]
        )

    return datos_copia