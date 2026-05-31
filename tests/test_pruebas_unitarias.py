import pandas as pd

from src.backend.seleccion_columnas import validar_seleccion_columnas
from src.backend.tratamiento_nulos import (
    contar_valores_faltantes,
    rellenar_con_media,
)
from src.backend.transformacion_categorica import (
    detectar_columnas_categoricas,
    aplicar_label_encoding,
)
from src.backend.normalizacion import (
    detectar_columnas_numericas,
    aplicar_min_max_scaling,
)
from src.backend.valores_atipicos import contar_valores_atipicos
from src.backend.exportacion_datos import exportar_csv


def test_validar_seleccion_columnas_correcta():
    columnas = ["edad", "salario", "compra"]

    resultado = validar_seleccion_columnas(
        columnas,
        [1, 2],
        3,
    )

    assert resultado is None


def test_contar_valores_faltantes():
    datos = pd.DataFrame(
        {
            "edad": [20, None, 30],
            "salario": [1000, 2000, None],
            "compra": [1, 0, 1],
        }
    )

    faltantes = contar_valores_faltantes(
        datos,
        ["edad", "salario"],
        "compra",
    )

    assert faltantes == {
        "edad": 1,
        "salario": 1,
    }


def test_rellenar_con_media():
    datos = pd.DataFrame(
        {
            "edad": [20, None, 30],
        }
    )

    resultado = rellenar_con_media(
        datos,
        ["edad"],
    )

    assert resultado["edad"].isnull().sum() == 0
    assert resultado.loc[1, "edad"] == 25


def test_detectar_columnas_categoricas():
    datos = pd.DataFrame(
        {
            "edad": [20, 30],
            "sexo": ["M", "F"],
        }
    )

    categoricas = detectar_columnas_categoricas(
        datos,
        ["edad", "sexo"],
    )

    assert categoricas == ["sexo"]


def test_aplicar_label_encoding():
    datos = pd.DataFrame(
        {
            "sexo": ["M", "F", "M"],
        }
    )

    resultado = aplicar_label_encoding(
        datos,
        ["sexo"],
    )

    assert resultado["sexo"].dtype != object
    assert set(resultado["sexo"].unique()) == {0, 1}


def test_detectar_columnas_numericas():
    datos = pd.DataFrame(
        {
            "edad": [20, 30],
            "sexo": ["M", "F"],
        }
    )

    numericas = detectar_columnas_numericas(
        datos,
        ["edad", "sexo"],
    )

    assert numericas == ["edad"]


def test_aplicar_min_max_scaling():
    datos = pd.DataFrame(
        {
            "edad": [10, 20, 30],
        }
    )

    resultado = aplicar_min_max_scaling(
        datos,
        ["edad"],
    )

    assert resultado["edad"].min() == 0
    assert resultado["edad"].max() == 1


def test_contar_valores_atipicos():
    datos = pd.DataFrame(
        {
            "edad": [10, 11, 12, 13, 100],
        }
    )

    atipicos = contar_valores_atipicos(
        datos,
        ["edad"],
    )

    assert "edad" in atipicos


def test_exportar_csv(tmp_path):
    datos = pd.DataFrame(
        {
            "edad": [20, 30],
        }
    )

    ruta = tmp_path / "salida"

    archivo = exportar_csv(
        datos,
        str(ruta),
    )

    assert archivo.endswith(".csv")