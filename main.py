from src.frontend.interfaz_carga_datos import menu_carga_datos


def mostrar_menu_principal(datos, archivo_cargado):
    print("\n=============================")
    print("Menú Principal")
    print("=============================")

    if datos is None:
        print("[-] 1. Cargar datos (ningún archivo cargado)")
        print("[✗] 2. Preprocesado de datos (requiere carga de datos)")
        print("[✗] 3. Visualización de datos (requiere carga y preprocesado)")
        print("[✗] 4. Exportar datos (requiere carga y preprocesado)")
    else:
        print(f"[✓] 1. Cargar datos (archivo: {archivo_cargado})")
        print("[-] 2. Preprocesado de datos (selección de columnas requerida)")
        print("[✗] 3. Visualización de datos (requiere preprocesado)")
        print("[✗] 4. Exportar datos (requiere preprocesado)")

    print("[✓] 5. Salir")


def main():
    datos = None
    archivo_cargado = None

    while True:
        mostrar_menu_principal(datos, archivo_cargado)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevos_datos, nuevo_archivo = menu_carga_datos()

            if nuevos_datos is not None:
                datos = nuevos_datos
                archivo_cargado = nuevo_archivo

        elif opcion == "2":
            if datos is None:
                print("Error: primero debe cargar datos.")
            else:
                print("Preprocesado de datos pendiente de implementar.")

        elif opcion == "3":
            print("Visualización de datos pendiente de implementar.")

        elif opcion == "4":
            print("Exportación de datos pendiente de implementar.")

        elif opcion == "5":
            print("Saliendo de la aplicación.")
            break

        else:
            print("Error: opción no válida.")


if __name__ == "__main__":
    main()