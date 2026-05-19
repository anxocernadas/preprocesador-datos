from src.backend.exportacion_datos import (
    exportar_csv,
    exportar_excel,
)


def menu_exportacion(datos):
    """
    Interfaz CLI para exportar los datos procesados.
    """
    print("\n=============================")
    print("Exportación de Datos")
    print("=============================")

    print("Seleccione el formato de exportación:")
    print("  [1] CSV (.csv)")
    print("  [2] Excel (.xlsx)")
    print("  [3] Volver al menú principal")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre_archivo = input(
            "Ingrese el nombre del archivo de salida (sin extensión): "
        )

        ruta_salida = exportar_csv(
            datos,
            nombre_archivo,
        )

        print(f'Datos exportados correctamente como "{ruta_salida}".')
        return True

    elif opcion == "2":
        nombre_archivo = input(
            "Ingrese el nombre del archivo de salida (sin extensión): "
        )

        ruta_salida = exportar_excel(
            datos,
            nombre_archivo,
        )

        print(f'Datos exportados correctamente como "{ruta_salida}".')
        return True

    elif opcion == "3":
        return False

    else:
        print("Error: opción no válida.")
        return False

   