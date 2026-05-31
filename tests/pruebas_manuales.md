# Pruebas Manuales

|                  Prueba                   |                        Resultado esperado                         | Resultado |
|-------------------------------------------|-------------------------------------------------------------------|-----------|
| Cargar un archivo CSV válido              | Los datos se cargan correctamente                                    | OK |
| Cargar un archivo XLSX válido             | Los datos se cargan correctamente                                    | OK |
| Seleccionar variables de entrada y salida | La selección se guarda correctamente                                 | OK |
| Aplicar tratamiento de valores faltantes  | Los valores faltantes se procesan correctamente                      | OK |
| Aplicar transformación categórica         | Las variables categóricas se transforman correctamente               | OK |
| Aplicar normalización                     | Las variables numéricas se escalan correctamente                     | OK |
| Detectar y tratar valores atípicos        | Los valores atípicos se detectan y procesan correctamente            | OK |
| Generar resumen estadístico               | Se muestran las estadísticas correctamente                           | OK |
| Generar histogramas                       | Los histogramas se muestran correctamente                            | OK |
| Generar gráficos de dispersión            | Los gráficos se muestran correctamente                               | OK |
| Generar heatmap de correlación            | El heatmap se muestra correctamente                                  | OK |
| Exportar datos a CSV                      | Se genera el archivo CSV correctamente                               | OK |
| Exportar datos a Excel (.xlsx)            | Se genera el archivo XLSX correctamente                              | OK |
| Visualizar sin completar el preprocesado  | La aplicación impide la acción y muestra un mensaje informativo      | OK |
| Exportar sin completar el preprocesado    | La aplicación impide la acción y muestra un mensaje informativo      | OK |
| Cancelar la salida de la aplicación       | Se regresa al menú principal                                         | OK |
| Confirmar la salida de la aplicación      | La aplicación finaliza correctamente                                 | OK |
| Introducir una opción inválida            | Se muestra un mensaje de error y la aplicación continúa funcionando  | OK |

## Resultado

Todas las pruebas manuales fueron ejecutadas satisfactoriamente y el sistema se comportó según lo especificado en las historias de usuario.