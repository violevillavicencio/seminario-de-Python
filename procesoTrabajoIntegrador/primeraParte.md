# 🛠️ Procesamiento de Archivos Fusionados de Individuos y Hogares

En mi parte me encargué del procesamiento de los archivos fusionados de individuos y hogares. Usé `pathlib` para definir rutas limpias, y un módulo llamado `fusionar_csv` para unir automáticamente los archivos por trimestre.

Luego traduje columnas con valores codificados (como `CH04`) a texto, y generé nuevas columnas como `MATERIAL_TECHUMBRE` y `CONDICION_DE_HABITABILIDAD` con base en múltiples condiciones de calidad.

Al final, guardamos todo en nuevos archivos `.csv` que contienen los datos listos para análisis, **sin tocar los originales**.

---

## 📊 Procesamiento e Información a Obtener

### 🧩 Sección A: Generación del Dataset Principal

1. Se debe definir una carpeta, cuyo *path* debe ser configurable vía una variable, donde se almacenarán el conjunto de archivos de **individuos** y **hogares**.  
2. Se debe generar una sección de código dentro del notebook que busque en la mencionada carpeta cada uno de los archivos “individuos” y “hogares” y los una.  

Por ejemplo:  
Si en la carpeta tenemos tres archivos de individuos (2023-T1, 2023-T2, 2024-T1), se debe leer la información de cada uno y generar un único dataset combinado.  

> 📌 Recordá que dentro de las columnas se encuentra el **año** y **trimestre**, por lo que luego de unirse se puede conocer fácilmente el período al cual pertenece cada fila.

Esta operación se debe realizar tanto para los archivos de **individuos** como de **hogares**.

---

1️⃣ Manejo de Rutas con `pathlib` y Configuración mediante Variables

En este proyecto se usó el módulo estándar de Python `pathlib` para manejar archivos y rutas en lugar de cadenas de texto con rutas absolutas.

### ❓ ¿Por qué se requiere que la ruta sea configurable?

- ✅ Evita rutas *hardcodeadas*.
- ✅ Permite reutilizar rutas de forma clara en distintos módulos o notebooks.
- ✅ Facilita el mantenimiento y portabilidad del código.

### 🧪 Ejemplo de uso:

```python
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent.parent.parent
FILES_PATH = PROJECT_PATH / "files_eph"
FUSION_PATH = PROJECT_PATH / "fusion_eph"

- PROJECT_PATH: apunta a la raíz del proyecto, sin importar desde dónde se ejecute.

- FILES_PATH: carpeta donde están los datasets originales.

- FUSION_PATH: carpeta donde se guardan los archivos fusionados.

✅ Ventajas de pathlib.Path

| Ventaja              | Descripción                                       |
| -------------------- | ------------------------------------------------- |
| Código legible       | `FILES_PATH / "T124" / "usu_individual_T124.txt"` |
| Multiplataforma      | Funciona en Windows, Linux y macOS                |
| Métodos integrados   | `.exists()`, `.is_file()`, `.open()`              |
| Reutilización segura | Se usa en todo el proyecto                        |


Gracias a esta implementación:

- El proyecto funciona en cualquier entorno (Visual Studio Code, Jupyter, terminal).

- Todos los miembros del grupo pueden trabajar sin preocuparse por rutas absolutas.

- Se puede cambiar de carpeta con solo cambiar una variable (PROJECT_PATH).

2️⃣ Fusión de Archivos "Individuos" y "Hogar"

- En este proyecto se trabajó con múltiples archivos .txt por cada trimestre del relevamiento de la EPH. Para facilitar el análisis, se desarrolló un módulo que automatiza la unificación (fusión) de los archivos de cada tipo: usu_individual_* y usu_hogar_*

❓ ¿Por qué unir los archivos?
Cada trimestre tiene su propio archivo de individuos y hogares.

Para analizarlos como un conjunto, deben combinarse.

La fusión conserva el encabezado y evita duplicaciones.

📦 ¿Qué hace el módulo fusionar_csv?

def fusionar_csv(nombre_prefijo: str, carpeta_entrada: Path, archivo_salida: Path):

Recorre todas las subcarpetas de la ruta carpeta_entrada (por ejemplo, files_eph/T124, T224, etc.).

Busca archivos cuyo nombre comience con nombre_prefijo (como "usu_individual_" o "usu_hogar_").

Lee cada archivo encontrado y los concatena en un único archivo CSV de salida, escribiendo el encabezado una sola vez.

for subcarpeta in carpeta_entrada.iterdir():
    for archivo in subcarpeta.glob(f"{nombre_prefijo}*"):
        # Abre el archivo, lee el encabezado solo una vez
        # Agrega las demás líneas al archivo final
        
Usa pathlib para manejar las rutas.

Usa encoding="utf-8" para evitar errores de codificación.

Es flexible: funciona con archivos .txt o .csv sin necesidad de cambiar la función.

✅ Ventajas de este enfoque

| Característica | Detalle                                                |
| -------------- | ------------------------------------------------------ |
| Modular        | Se importa desde cualquier notebook                    |
| Reutilizable   | Funciona para individuos y hogares sin duplicar código |
| Seguro         | Evita encabezados duplicados                           |
| Automatizado   | Busca los archivos por nombre, sin indicar cada uno    |


📁 Archivos generados
fusion_eph/individuos_fusionado.csv

fusion_eph/hogares_fusionado.csv

Estos archivos se utilizan luego para análisis, visualizaciones y creación de nuevas columnas.
