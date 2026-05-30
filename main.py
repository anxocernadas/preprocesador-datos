from src.frontend.interfaz_carga_datos import menu_carga_datos
from src.frontend.interfaz_seleccion_columnas import menu_seleccion_columnas
from src.frontend.interfaz_tratamiento_nulos import menu_tratamiento_nulos
from src.frontend.interfaz_transformacion_categorica import menu_transformacion_categorica
from src.frontend.interfaz_normalizacion import menu_normalizacion
from src.frontend.interfaz_valores_atipicos import menu_valores_atipicos
from src.frontend.interfaz_visualizacion import menu_visualizacion
from src.frontend.interfaz_exportacion import menu_exportacion


def confirmar_salida():
    print("\n=============================")
    print("Salir de la Aplicación")
    print("=============================")
    print("¿Está seguro de que desea salir?")
    print("  [1] Sí")
    print("  [2] No")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Cerrando la aplicación...")
        return True

    elif opcion == "2":
        print("Regresando al menú principal...")
        return False

    else:
        print("Error: opción no válida.")
        print("Regresando al menú principal...")
        return False

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
    exportacion_realizada,
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

        if valores_atipicos_tratados:
            print("[✓] 2. Preprocesado de datos")
        else:
            print("[-] 2. Preprocesado de datos")

        if features is None or target is None:
            print("      [-] 2.1 Selección de columnas (pendiente)")
            print(
                "      [✗] 2.2 Manejo de datos faltantes "
                "(requiere selección de columnas)"
            )
            print(
                "      [✗] 2.3 Transformación de datos categóricos "
                "(requiere manejo de datos faltantes)"
            )
            print(
                "      [✗] 2.4 Normalización y escalado "
                "(requiere transformación categórica)"
            )
            print(
                "      [✗] 2.5 Detección y manejo de valores atípicos "
                "(requiere normalización)"
            )

        elif not nulos_tratados:
            print("      [✓] 2.1 Selección de columnas (completado)")
            print("      [-] 2.2 Manejo de datos faltantes (pendiente)")
            print(
                "      [✗] 2.3 Transformación de datos categóricos "
                "(requiere manejo de datos faltantes)"
            )
            print(
                "      [✗] 2.4 Normalización y escalado "
                "(requiere transformación categórica)"
            )
            print(
                "      [✗] 2.5 Detección y manejo de valores atípicos "
                "(requiere normalización)"
            )

        elif not transformacion_categorica_realizada:
            print("      [✓] 2.1 Selección de columnas (completado)")
            print("      [✓] 2.2 Manejo de datos faltantes (completado)")
            print(
                "      [-] 2.3 Transformación de datos categóricos "
                "(pendiente)"
            )
            print(
                "      [✗] 2.4 Normalización y escalado "
                "(requiere transformación categórica)"
            )
            print(
                "      [✗] 2.5 Detección y manejo de valores atípicos "
                "(requiere normalización)"
            )

        elif not normalizacion_realizada:
            print("      [✓] 2.1 Selección de columnas (completado)")
            print("      [✓] 2.2 Manejo de datos faltantes (completado)")
            print(
                "      [✓] 2.3 Transformación de datos categóricos "
                "(completado)"
            )
            print("      [-] 2.4 Normalización y escalado (pendiente)")
            print(
                "      [✗] 2.5 Detección y manejo de valores atípicos "
                "(requiere normalización)"
            )

        elif not valores_atipicos_tratados:
            print("      [✓] 2.1 Selección de columnas (completado)")
            print("      [✓] 2.2 Manejo de datos faltantes (completado)")
            print(
                "      [✓] 2.3 Transformación de datos categóricos "
                "(completado)"
            )
            print("      [✓] 2.4 Normalización y escalado (completado)")
            print(
                "      [-] 2.5 Detección y manejo de valores atípicos "
                "(pendiente)"
            )

        else:
            print("      [✓] 2.1 Selección de columnas (completado)")
            print("      [✓] 2.2 Manejo de datos faltantes (completado)")
            print(
                "      [✓] 2.3 Transformación de datos categóricos "
                "(completado)"
            )
            print("      [✓] 2.4 Normalización y escalado (completado)")
            print(
                "      [✓] 2.5 Detección y manejo de valores atípicos "
                "(completado)"
            )

        if visualizacion_realizada:
            print("[✓] 3. Visualización de datos (completado)")

            if exportacion_realizada:
                print("[✓] 4. Exportar datos (completado)")
            else:
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
    exportacion_realizada = False

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
            exportacion_realizada,
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
                exportacion_realizada = False

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
                    visualizacion_realizada = False
                    exportacion_realizada = False


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

            if not visualizacion_realizada:
                print(
                    "No es posible exportar los datos hasta "
                    "que se complete el preprocesado y la visualización."
                )

                print(
                    "Por favor, finalice todas las etapas "
                    "antes de continuar."
                )

            else:
                completado = menu_exportacion(datos)

                if completado:
                    exportacion_realizada = True

        elif opcion == "5":
            if confirmar_salida():
                break

        else:
            print("Error: opción no válida.")


if __name__ == "__main__":
    main()