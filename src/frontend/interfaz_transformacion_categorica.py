from src.backend.transformacion_categorica import (
    detectar_columnas_categoricas,
    aplicar_one_hot_encoding,
    aplicar_label_encoding,
)


def menu_transformacion_categorica(datos, features):
    """
    Interfaz CLI para transformación de datos categóricos.
    """
    categoricas = detectar_columnas_categoricas(
        datos,
        features,
    )

    print("\n=============================")
    print("Transformación de Datos Categóricos")
    print("=============================")

    if not categoricas:
        print(
            "No se han detectado columnas categóricas "
            "en las variables de entrada seleccionadas."
        )

        print("No es necesario aplicar ninguna transformación.")

        return datos, True

    print(
        "Se han detectado columnas categóricas "
        "en las variables de entrada seleccionadas:"
    )

    for columna in categoricas:
        print(f"  - {columna}")

    print("\nSeleccione una estrategia de transformación:")
    print("  [1] One-Hot Encoding")
    print("  [2] Label Encoding")
    print("  [3] Volver al menú principal")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == "1":
            datos = aplicar_one_hot_encoding(
                datos,
                categoricas,
            )

            print(
                "\nTransformación completada "
                "con One-Hot Encoding."
            )

            return datos, True

        elif opcion == "2":
            datos = aplicar_label_encoding(
                datos,
                categoricas,
            )

            print(
                "\nTransformación completada "
                "con Label Encoding."
            )

            return datos, True

        elif opcion == "3":
            return datos, False

        else:
            print("\n⚠ Error: opción no válida.")
            return datos, False

    except Exception as error:
        print(f"\n⚠ Error: {error}")
        return datos, False