from src.frontend.interfaz_carga_datos import menu_carga_datos
from src.frontend.interfaz_seleccion_columnas import menu_seleccion_columnas
from src.frontend.interfaz_tratamiento_nulos import menu_tratamiento_nulos
from src.frontend.interfaz_transformacion_categorica import menu_transformacion_categorica
from src.frontend.interfaz_normalizacion import menu_normalizacion
from src.frontend.interfaz_valores_atipicos import menu_valores_atipicos
from src.frontend.interfaz_visualizacion import menu_visualizacion


def mostrar_menu_principal(
    datos,
    archivo_cargado,
    features,
    target,
    nulos_tratados,
    transformacion_categorica_realizada,
    normalizacion_realizada,
    valores_atipicos_tratados,
    visualizacion_realizada,
):
    print("\n=============================")
    print("Menú Principal")
    print("=============================")

    if datos is None:
        print("[-] 1. Cargar datos (ningún archivo cargado)")
        print("[✗] 2. Preprocesado de datos (requiere carga de datos)")
        print("[✗] 3. Visualización de datos (requiere preprocesado)")
        print("[✗] 4. Exportar datos (requiere preprocesado)")

    else:
        print(f"[✓] 1. Cargar datos (archivo: {archivo_cargado})")

        print("[-] 2. Preprocesado de datos")

        if features is not None and target is not None:
            print("      [✓] 2.1 Selección de columnas (completado)")
        else:
            print("      [-] 2.1 Selección de columnas (pendiente)")

        if nulos_tratados:

            print("      [✓] 2.2 Manejo de datos faltantes (completado)")

            if transformacion_categorica_realizada:

                print(
                    "      [✓] 2.3 Transformación de datos categóricos "
                    "(completado)"
                )

                if normalizacion_realizada:

                    print(
                        "      [✓] 2.4 Normalización y escalado "
                        "(completado)"
                    )

                else:

                    print(
                        "      [-] 2.4 Normalización y escalado "
                        "(pendiente)"
                    )
            else:

                print(
                    "      [-] 2.3 Transformación de datos categóricos "
                    "(pendiente)"
                )

                print(
                    "      [✗] 2.4 Normalización y escalado "
                    "(requiere transformación categórica)"
                )

        else:

            print("      [-] 2.2 Manejo de datos faltantes (pendiente)")

            print(
                "      [✗] 2.3 Transformación de datos categóricos "
                "(requiere manejo de valores faltantes)"
            )

            print(
                "      [✗] 2.4 Normalización y escalado "
                "(requiere transformación categórica)"
            )
        if normalizacion_realizada:

            if valores_atipicos_tratados:
                print(
                    "      [✓] 2.5 Detección y manejo de valores atípicos "
                    "(completado)"
                )
            else:
                print(
                    "      [-] 2.5 Detección y manejo de valores atípicos "
                    "(pendiente)"
                )

        else:
            print(
                "      [✗] 2.5 Detección y manejo de valores atípicos "
                "(requiere normalización)"
            )       

        if visualizacion_realizada:
            print("[✓] 3. Visualización de datos (completado)")
            print("[-] 4. Exportar datos (pendiente)")

        elif valores_atipicos_tratados:
            print("[-] 3. Visualización de datos (pendiente)")
            print("[✗] 4. Exportar datos (requiere visualización de datos)")

        else:
            print(
                "[✗] 3. Visualización de datos "
                "(requiere preprocesado completo)"
            )
            print("[✗] 4. Exportar datos (requiere visualización de datos)")

    print("[✓] 5. Salir")


def main():
    datos = None
    archivo_cargado = None
    features = None
    target = None
    nulos_tratados = False
    transformacion_categorica_realizada = False
    normalizacion_realizada = False
    valores_atipicos_tratados = False
    datos_originales = None
    visualizacion_realizada = False

    while True:
        mostrar_menu_principal(
            datos,
            archivo_cargado,
            features,
            target,
            nulos_tratados,
            transformacion_categorica_realizada,
            normalizacion_realizada,
            valores_atipicos_tratados,
            visualizacion_realizada,
        )
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevos_datos, nuevo_archivo = menu_carga_datos()

            if nuevos_datos is not None:
                datos_originales = nuevos_datos.copy()
                datos = nuevos_datos
                archivo_cargado = nuevo_archivo
                features = None
                target = None
                nulos_tratados = False
                transformacion_categorica_realizada = False
                normalizacion_realizada = False
                valores_atipicos_tratados = False
                visualizacion_realizada = False

        elif opcion == "2":

            if datos is None:
                print("Error: primero debe cargar datos.")

            elif features is None or target is None:

                nuevas_features, nuevo_target = menu_seleccion_columnas(datos)

                if nuevas_features is not None:
                    features = nuevas_features
                    target = nuevo_target
                    nulos_tratados = False
                    transformacion_categorica_realizada = False
                    normalizacion_realizada = False
                    valores_atipicos_tratados = False


            elif not nulos_tratados:

                datos, completado = menu_tratamiento_nulos(
                    datos,
                    features,
                    target,
                )

                if completado:
                    nulos_tratados = True

            elif not transformacion_categorica_realizada:

                datos, completado = menu_transformacion_categorica(
                    datos,
                    features,
                )
                
                if completado:
                    features = [
                        columna
                        for columna in features
                        if columna in datos.columns
                    ]

                    transformacion_categorica_realizada = True

            elif not normalizacion_realizada:

                datos, completado = menu_normalizacion(
                    datos,
                    features,
                )

                if completado:
                    normalizacion_realizada = True
            
            elif not valores_atipicos_tratados:

                datos, completado = menu_valores_atipicos(
                    datos,
                    features,
                )

                if completado:
                    valores_atipicos_tratados = True

        elif opcion == "3":

            if not valores_atipicos_tratados:
                print(
                    "No es posible visualizar los datos hasta "
                    "que se complete el preprocesado."
                )
                print(
                    "Por favor, finalice el manejo de valores "
                    "atípicos antes de continuar."
                )

            else:
                menu_visualizacion(
                    datos,
                    features,
                    datos_originales,
                )

                visualizacion_realizada = True

        elif opcion == "4":
            print("Exportación de datos pendiente de implementar.")

        elif opcion == "5":
            print("Saliendo de la aplicación.")
            break

        else:
            print("Error: opción no válida.")


if __name__ == "__main__":
    main()