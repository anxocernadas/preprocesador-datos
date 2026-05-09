from src.backend.tratamiento_nulos import (
    contar_valores_faltantes,
    obtener_columnas_seleccionadas,
    eliminar_filas_con_nulos,
    rellenar_con_media,
    rellenar_con_mediana,
    rellenar_con_moda,
    rellenar_con_valor_constante,
)


def menu_tratamiento_nulos(datos, features, target):
    """
    Interfaz CLI para el manejo de valores faltantes.
    """
    columnas = obtener_columnas_seleccionadas(features, target)

    faltantes = contar_valores_faltantes(
        datos,
        features,
        target,
    )

    print("\n=============================")
    print("Manejo de Valores Faltantes")
    print("=============================")

    if not faltantes:
        print(
            "No se han detectado valores faltantes "
            "en las columnas seleccionadas."
        )

        print("No es necesario aplicar ninguna estrategia.")

        return datos, True

    print(
        "Se han detectado valores faltantes "
        "en las siguientes columnas seleccionadas:"
    )

    for columna, cantidad in faltantes.items():
        print(f"  - {columna}: {cantidad} valores faltantes")

    print("\nSeleccione una estrategia para manejar los valores faltantes:")
    print("  [1] Eliminar filas con valores faltantes")
    print("  [2] Rellenar con la media de la columna")
    print("  [3] Rellenar con la mediana de la columna")
    print("  [4] Rellenar con la moda de la columna")
    print("  [5] Rellenar con un valor constante")
    print("  [6] Volver al menú principal")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == "1":
            datos = eliminar_filas_con_nulos(datos, columnas)

            print(
                "\nFilas con valores faltantes eliminadas correctamente."
            )

        elif opcion == "2":
            datos = rellenar_con_media(datos, columnas)

            print(
                "\nValores faltantes rellenados con la media."
            )

        elif opcion == "3":
            datos = rellenar_con_mediana(datos, columnas)

            print(
                "\nValores faltantes rellenados con la mediana."
            )

        elif opcion == "4":
            datos = rellenar_con_moda(datos, columnas)

            print(
                "\nValores faltantes rellenados con la moda."
            )

        elif opcion == "5":
            valor = float(
                input("\nIngrese un valor numérico para reemplazar los valores faltantes: ")
            )

            datos = rellenar_con_valor_constante(
                datos,
                columnas,
                valor,
            )

            print(
                f"\nValores faltantes reemplazados con el valor {valor}."
            )

        elif opcion == "6":
            return datos, False

        else:
            print("\n⚠ Error: opción no válida.")
            return datos, False

        return datos, True

    except Exception as error:
        print(f"\n⚠ Error: {error}")
        return datos, False