from src.backend.valores_atipicos import (
    detectar_columnas_numericas,
    contar_valores_atipicos,
    eliminar_filas_con_atipicos,
    reemplazar_atipicos_con_mediana,
)


def menu_valores_atipicos(datos, features):
    """
    Interfaz CLI para detección y manejo de valores atípicos.
    """
    numericas = detectar_columnas_numericas(
        datos,
        features,
    )

    atipicos = contar_valores_atipicos(
        datos,
        features,
    )

    print("\n=============================")
    print("Detección y Manejo de Valores Atípicos")
    print("=============================")

    if not atipicos:

        print(
            "No se han detectado valores atípicos "
            "en las columnas seleccionadas."
        )

        print("No es necesario aplicar ninguna estrategia.")

        return datos, True

    print(
        "Se han detectado valores atípicos "
        "en las siguientes columnas numéricas seleccionadas:"
    )

    for columna, cantidad in atipicos.items():
        print(f"  - {columna}: {cantidad} valores atípicos detectados")

    print("\nSeleccione una estrategia para manejar los valores atípicos:")
    print("  [1] Eliminar filas con valores atípicos")
    print("  [2] Reemplazar valores atípicos con la mediana")
    print("  [3] Mantener valores atípicos sin cambios")
    print("  [4] Volver al menú principal")

    opcion = input("Seleccione una opción: ")

    try:

        if opcion == "1":

            datos = eliminar_filas_con_atipicos(
                datos,
                numericas,
            )

            print(
                "\nFilas con valores atípicos eliminadas correctamente."
            )

            return datos, True

        elif opcion == "2":

            datos = reemplazar_atipicos_con_mediana(
                datos,
                numericas,
            )

            print(
                "\nValores atípicos reemplazados con la mediana."
            )

            return datos, True

        elif opcion == "3":

            print(
                "\nLos valores atípicos se mantuvieron sin cambios."
            )

            return datos, True

        elif opcion == "4":
            return datos, False

        else:
            print("\n⚠ Error: opción no válida.")
            return datos, False

    except Exception as error:
        print(f"\n⚠ Error: {error}")
        return datos, False