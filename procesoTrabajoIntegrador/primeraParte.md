Procesamiento e información a obtener 
Sección A: generación del dataset principal 
1. Se debe definir una carpeta, cuyo path debe ser configurable vía una variable, donde se almacenarán el conjunto de archivos de “individuos” y “hogares”.   
2. Se debe generar una sección de código dentro del notebook que busque en la mencionada carpeta cada uno de los archivos “individuos” y “hogares” y los una.  Es 
decir, si en la carpeta tenemos tres archivos de individuos (año 2023 trimestre 1, año 2023 trimestre 2, año 2024 trimestre 1) se debe  leer la información de cada uno y 
generar un dataset que contenga toda la información. 
Recordar que dentro de las columnas de información se encuentra el año y trimestre, por lo que luego de unirse se puede conocer fácilmente el período al cual pertenece. 
Esta operación automática de búsqueda y generación de dataset se debe realizar tanto para el archivo de individuos como el de hogares.

1) Manejo de rutas con pathlib y configuración mediante variables

- En este proyecto, el manejo de archivos y directorios se realizó utilizando el módulo estándar de Python pathlib, en lugar de definir rutas absolutas a mano.

¿Por qué se requiere que la ruta sea configurable?

- La consigna indicaba que el path donde se almacenan los datasets debía ser configurable mediante una variable. Esto tiene varias ventajas:

- Evita tener rutas "hardcodeadas" que sólo funcionan en una máquina específica.

- Permite reutilizar rutas de forma clara en distintos módulos o notebooks.

- Facilita el mantenimiento y portabilidad del código dentro del equipo.

✅ Uso de pathlib
En lugar de usar cadenas de texto, usamos objetos Path para componer rutas de forma segura y multiplataforma.

from pathlib import Path

Ejemplo del proyecto:
PROJECT_PATH = Path(__file__).resolve().parent.parent.parent
FILES_PATH = PROJECT_PATH / "files_eph"
FUSION_PATH = PROJECT_PATH / "fusion_eph"

- PROJECT_PATH apunta a la raíz del proyecto, sin importar desde dónde se ejecute el código.

- FILES_PATH representa la carpeta donde están los datasets originales, organizados por trimestre.

- FUSION_PATH representa la carpeta donde se guardan los archivos fusionados.

Ventajas de pathlib.Path
Código legible	FILES_PATH / "T124" / "usu_individual_T124.txt"
Multiplataforma (Windows/Linux)	Sin problemas con / o \
Métodos útiles integrados	.exists(), .is_file(), .open()
Reutilización segura	Se usa en todos los notebooks y módulos

Gracias a esta implementación:

- El proyecto funciona en cualquier entorno (Visual Studio Code, Jupyter, terminal).

- Todos los miembros del grupo pueden trabajar sin preocuparse por rutas absolutas.

- Se puede cambiar de carpeta con solo cambiar una variable (PROJECT_PATH).

