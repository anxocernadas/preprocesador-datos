from src.backend.seleccion_columnas import (
    obtener_columnas,
    seleccionar_columnas,
)


def menu_seleccion_columnas(datos):
    """
    Interfaz CLI para seleccionar features y target.
    """
    columnas = obtener_columnas(datos)

    print("\n=============================")
    print("Selección de Columnas")
    print("=============================")

    print("Columnas disponibles en los datos:")

    for i, columna in enumerate(columnas, start=1):
        print(f"  [{i}] {columna}")

    try:
        entrada_features = input(
            "\nIngrese los números de las columnas de entrada (features), separados por comas: "
        )

        indices_features = [
            int(indice.strip())
            for indice in entrada_features.split(",")
        ]

        indice_target = int(
            input(
                "\nIngrese el número de la columna de salida (target): "
            )
        )

        features, target = seleccionar_columnas(
            datos,
            indices_features,
            indice_target
        )

        print(
            f"\nSelección guardada: "
            f"Features = {features}, "
            f"Target = '{target}'"
        )

        return features, target

    except Exception as error:
        print(f"\n⚠ Error: {error}")
        return None, None