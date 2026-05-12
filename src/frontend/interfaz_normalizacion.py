from src.backend.normalizacion import (
    detectar_columnas_numericas,
    aplicar_min_max_scaling,
    aplicar_z_score,
)


def menu_normalizacion(datos, features):
    """
    Interfaz CLI para normalizar columnas numéricas seleccionadas.
    """
    numericas = detectar_columnas_numericas(datos, features)

    print("\n=============================")
    print("Normalización y Escalado")
    print("=============================")

    if not numericas:
        print(
            "No se han detectado columnas numéricas "
            "en las variables de entrada seleccionadas."
        )
        print("No es necesario aplicar ninguna normalización.")
        return datos, True

    print(
        "Se han detectado columnas numéricas "
        "en las variables de entrada seleccionadas:"
    )

    for columna in numericas:
        print(f"  - {columna}")

    print("\nSeleccione una estrategia de normalización:")
    print("  [1] Min-Max Scaling (escala valores entre 0 y 1)")
    print("  [2] Z-score Normalization (media 0, desviación estándar 1)")
    print("  [3] Volver al menú principal")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == "1":
            datos = aplicar_min_max_scaling(datos, numericas)
            print("\nNormalización completada con Min-Max Scaling.")
            return datos, True

        elif opcion == "2":
            datos = aplicar_z_score(datos, numericas)
            print("\nNormalización completada con Z-score.")
            return datos, True

        elif opcion == "3":
            return datos, False

        else:
            print("\n⚠ Error: opción no válida.")
            return datos, False

    except Exception as error:
        print(f"\n⚠ Error: {error}")
        return datos, False