from src.backend.visualizacion_datos import (
    obtener_resumen_estadistico,
    obtener_distribucion_categorica,
    mostrar_histogramas,
    mostrar_graficos_dispersion,
    mostrar_heatmap_correlacion,
)

def menu_visualizacion(datos, features, datos_originales):
    print("\n=============================")
    print("Visualización de Datos")
    print("=============================")

    while True:

        print("Seleccione qué tipo de visualización desea generar:")

        print(
            "  [1] Resumen estadístico "
            "de las variables seleccionadas"
        )

        print("  [2] Histogramas de variables numéricas")

        print(
            "  [3] Gráficos de dispersión "
            "antes y después de la normalización"
        )

        print(
            "  [4] Heatmap de correlación "
            "de variables numéricas"
        )

        print("  [5] Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            resumen = obtener_resumen_estadistico(
                datos,
                features,
            )

            print("\nResumen estadístico de las variables seleccionadas:")
            print("-" * 75)
            print(
                f"{'Variable':<15} | {'Media':<10} | {'Mediana':<10} | "
                f"{'Desv. Est.':<12} | {'Mínimo':<10} | {'Máximo':<10}"
            )
            print("-" * 75)

            for columna, valores in resumen.items():
                print(
                    f"{columna:<15} | "
                    f"{round(valores['media'], 2):<10} | "
                    f"{round(valores['mediana'], 2):<10} | "
                    f"{round(valores['desviacion'], 2):<12} | "
                    f"{round(valores['minimo'], 2):<10} | "
                    f"{round(valores['maximo'], 2):<10}"
                )

        elif opcion == "2":

            mostrar_histogramas(
                datos,
                features,
            )

        elif opcion == "3":

            mostrar_graficos_dispersion(
                datos_originales,
                datos,
                features,
            )

        elif opcion == "4":

            mostrar_heatmap_correlacion(
                datos,
                features,
            )

        elif opcion == "5":
            return True

        else:
            print("Error: opción no válida.")