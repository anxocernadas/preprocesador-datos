# Interfaz CLI para carga de datos

from src.backend.carga_datos import (
    cargar_csv,
    cargar_excel,
    cargar_sqlite,
    obtener_hojas_excel,
    obtener_tablas_sqlite,
)


def mostrar_resumen_dataset(df):
    print("\nDatos cargados correctamente.")
    print(f"Número de filas: {df.shape[0]}")
    print(f"Número de columnas: {df.shape[1]}")

    print("\nTipos de datos:")
    print(df.dtypes)

    print("\nPrimeras 5 filas:")
    print(df.head())


def seleccionar_hoja_excel(ruta_archivo):
    hojas = obtener_hojas_excel(ruta_archivo)

    print("\nHojas disponibles:")
    for i, hoja in enumerate(hojas, start=1):
        print(f"  [{i}] {hoja}")

    opcion = input("Seleccione una hoja: ")

    try:
        indice = int(opcion) - 1
        return hojas[indice]
    except (ValueError, IndexError):
        raise ValueError("La hoja seleccionada no es válida.")


def seleccionar_tabla_sqlite(ruta_archivo):
    tablas = obtener_tablas_sqlite(ruta_archivo)

    if not tablas:
        raise ValueError("La base de datos no contiene tablas.")

    print("\nTablas disponibles en la base de datos:")
    for i, tabla in enumerate(tablas, start=1):
        print(f"  [{i}] {tabla}")

    opcion = input("Seleccione una tabla: ")

    try:
        indice = int(opcion) - 1
        return tablas[indice]
    except (ValueError, IndexError):
        raise ValueError("La tabla seleccionada no es válida.")


def menu_carga_datos():
    print("\n=============================")
    print("Carga de Datos")
    print("=============================")
    print("Seleccione el tipo de archivo a cargar:")
    print("  [1] CSV")
    print("  [2] Excel")
    print("  [3] SQLite")
    print("  [4] Volver al menú principal")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == "1":
            ruta = input("Ingrese la ruta del archivo CSV: ")
            df = cargar_csv(ruta)
            mostrar_resumen_dataset(df)
            return df, ruta

        elif opcion == "2":
            ruta = input("Ingrese la ruta del archivo Excel: ")
            hoja = seleccionar_hoja_excel(ruta)
            df = cargar_excel(ruta, hoja)
            mostrar_resumen_dataset(df)
            return df, ruta

        elif opcion == "3":
            ruta = input("Ingrese la ruta de la base de datos SQLite: ")
            tabla = seleccionar_tabla_sqlite(ruta)
            df = cargar_sqlite(ruta, tabla)
            print(f'\nDatos de la tabla "{tabla}" cargados correctamente.')
            mostrar_resumen_dataset(df)
            return df, ruta

        elif opcion == "4":
            return None, None

        else:
            print("Error: opción no válida.")
            return None, None

    except Exception as error:
        print(f"Error: {error}")
        return None, None