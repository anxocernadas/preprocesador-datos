## Descripción

Preprocesador de Datos es una aplicación desarrollada en Python que permite realizar tareas de preprocesamiento sobre conjuntos de datos de forma interactiva mediante una interfaz de línea de comandos.

La aplicación permite cargar datos desde distintos formatos, seleccionar variables, tratar valores faltantes, transformar variables categóricas, normalizar datos, detectar valores atípicos, visualizar los resultados obtenidos y exportar los datos procesados.

## Funcionalidades

- Carga de datos desde archivos CSV, Excel (.xlsx) y bases de datos SQLite (.db).
- Selección de variables predictoras (features) y variable objetivo (target).
- Tratamiento de valores faltantes mediante distintas estrategias.
- Transformación de variables categóricas.
- Normalización y escalado de variables numéricas.
- Detección y tratamiento de valores atípicos mediante el método IQR.
- Visualización de datos mediante:
  - Resumen estadístico.
  - Histogramas.
  - Gráficos de dispersión.
  - Heatmap de correlación.
- Exportación de datos procesados en formato CSV y Excel.
- Confirmación de salida de la aplicación.

## Requisitos

- Python 3.10 o superior.
- pip.

## Instalación

### 1. Clonar el repositorio

### 2. Crear un entorno virtual

### 3. Activar el entorno virtual

### 4. Instalar dependencias


## Dependencias principales

Las dependencias utilizadas por el proyecto se encuentran definidas en el archivo requirements.txt.

Entre ellas destacan:

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- openpyxl

## Ejecución

Una vez instalado el proyecto, ejecutar:

python main.py 

## Uso básico

### 1. Cargar datos

Seleccionar la opción correspondiente para cargar un archivo:

- CSV
- Excel (.xlsx)
- SQLite (.db)

Los archivos de datos deben colocarse en la carpeta:

text data/ 

### 2. Preprocesar los datos

Seguir el flujo secuencial de preprocesamiento:

1. Selección de columnas.
2. Tratamiento de valores faltantes.
3. Transformación de variables categóricas.
4. Normalización y escalado.
5. Detección y tratamiento de valores atípicos.

### 3. Visualizar los datos

La aplicación permite generar:

- Resumen estadístico.
- Histogramas.
- Gráficos de dispersión.
- Heatmap de correlación.

### 4. Exportar los datos

Los datos procesados pueden exportarse en:

- CSV (.csv)
- Excel (.xlsx)

### 5. Salir de la aplicación

La aplicación solicita confirmación antes de cerrarse.

## Estructura del proyecto

- data/: directorio destinado al almacenamiento de los conjuntos de datos utilizados por la aplicación.
- src/: contiene el código fuente de la aplicación, dividido en:
  - backend/: lógica de procesamiento y manipulación de datos.
  - frontend/: interfaz de línea de comandos e interacción con el usuario.
- tests/: contiene las pruebas unitarias y la documentación de pruebas manuales.
- .gitignore: define los archivos y directorios que no deben incluirse en el control de versiones.
- main.py: punto de entrada principal de la aplicación.
- requirements.txt: lista de dependencias necesarias para ejecutar el proyecto junto con sus versiones.

## Pruebas

El proyecto incluye pruebas unitarias y pruebas manuales para verificar el correcto funcionamiento de todas las funcionalidades implementadas.


## Versión

Versión estable: v1.0