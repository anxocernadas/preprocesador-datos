def exportar_csv(datos, nombre_archivo):
    """
    Exporta los datos procesados a un archivo CSV.
    """
    ruta_salida = f"{nombre_archivo}.csv"
    datos.to_csv(ruta_salida, index=False)

    return ruta_salida


def exportar_excel(datos, nombre_archivo):
    """
    Exporta los datos procesados a un archivo Excel.
    """
    ruta_salida = f"{nombre_archivo}.xlsx"
    datos.to_excel(ruta_salida, index=False)

    return ruta_salida