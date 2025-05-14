
# 🛠️ Procesamiento de Archivos Fusionados de Individuos y Hogares

Me encargué del procesamiento de los archivos fusionados de **individuos** y **hogares**. Usé `pathlib` para definir rutas limpias y un módulo llamado `fusionar_csv` para unir automáticamente los archivos por trimestre.

Luego, traduje columnas con valores codificados (como `CH04`) a texto y generé nuevas columnas como `MATERIAL_TECHUMBRE` y `CONDICION_DE_HABITABILIDAD` a partir de múltiples condiciones de calidad.

Al final, guardamos todo en nuevos archivos `.csv` con los datos listos para análisis, **sin modificar los originales**.

---

## 📊 Procesamiento e Información a Obtener

### 🧩 Sección A: Generación del Dataset Principal

1. Definir una carpeta (vía una variable configurable) donde se almacenan los archivos de **individuos** y **hogares**.  
2. Implementar código en el notebook que lea todos los archivos disponibles de ambos tipos y los combine automáticamente.

> 📌 Tip: Las columnas de año y trimestre permiten identificar fácilmente a qué período pertenece cada fila una vez fusionadas.

---

## 1️⃣ Manejo de Rutas con `pathlib` y Configuración por Variables

Para este proyecto se usó `pathlib`, el módulo estándar de Python, para manejar rutas y archivos de forma clara y multiplataforma.

### ❓ ¿Por qué hacer configurable la ruta?

- 🚫 Evita rutas *hardcodeadas* que fallan en otras máquinas.
- 🔁 Permite reutilizar rutas entre módulos y notebooks.
- 🔧 Facilita la portabilidad y mantenimiento del código.

### 🧪 Ejemplo de implementación

```python
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent.parent.parent
FILES_PATH = PROJECT_PATH / "files_eph"
FUSION_PATH = PROJECT_PATH / "fusion_eph"
```

| Variable       | Propósito                                                                 |
|----------------|---------------------------------------------------------------------------|
| `PROJECT_PATH` | Apunta a la raíz del proyecto, sin importar desde dónde se ejecute.       |
| `FILES_PATH`   | Carpeta con los datasets originales por trimestre.                        |
| `FUSION_PATH`  | Carpeta donde se guardan los archivos fusionados listos para análisis.    |

### ✅ Ventajas de usar `pathlib`

- Código legible: `FILES_PATH / "T124" / "usu_individual_T124.txt"`
- Multiplataforma: sin problemas con `/` o `\`
- Métodos útiles: `.exists()`, `.is_file()`, `.open()`
- Reutilizable y consistente en todo el proyecto

---

## 2️⃣ Fusión de Archivos de "Individuos" y "Hogares"

Trabajamos con múltiples archivos `.txt` por trimestre del relevamiento EPH. Se desarrolló un módulo que automatiza la unión de estos archivos para facilitar el análisis.

### ❓ ¿Por qué unir los archivos?

- Cada trimestre tiene su propio archivo de individuos y hogares.
- Para analizarlos como un conjunto, deben combinarse.
- La fusión debe conservar solo un encabezado, sin duplicarlo.

### ⚙️ Función del módulo `fusionar_csv`

```python
def fusionar_csv(nombre_prefijo: str, carpeta_entrada: Path, archivo_salida: Path):
    for subcarpeta in carpeta_entrada.iterdir():
        for archivo in subcarpeta.glob(f"{nombre_prefijo}*"):
            # Abre el archivo, lee encabezado una sola vez
            # Agrega líneas restantes al archivo final
```

- Recorre subcarpetas como `files_eph/T124`, `T224`, etc.
- Busca archivos por nombre (`usu_individual_*`, `usu_hogar_*`)
- Usa `encoding="utf-8"` para evitar errores de codificación
- Funciona con `.txt` o `.csv` sin modificar el código

### ✅ Ventajas del enfoque

| Característica  | Detalle                                                                 |
|-----------------|-------------------------------------------------------------------------|
| 🔁 Modular       | Se puede importar desde cualquier notebook                              |
| ♻️ Reutilizable   | Funciona para individuos y hogares sin duplicar código                 |
| 🛡️ Seguro         | Evita encabezados duplicados                                            |
| ⚙️ Automatizado   | Detecta archivos automáticamente por nombre                            |

---

## 📁 Archivos Generados

- `fusion_eph/individuos_fusionado.csv`
- `fusion_eph/hogares_fusionado.csv`

Estos archivos fusionados se utilizan para análisis posteriores, visualizaciones y generación de nuevas columnas derivadas.

---
# 🧠 Objetivo de la función
Fusionar varios archivos .txt de un tipo (por ejemplo, usu_individual_*.txt) que están organizados en subcarpetas (una por trimestre), 
generando un único archivo de salida que contenga todos los datos, con un solo encabezado.

from pathlib import Path

def fusionar_csv(nombre_prefijo: str, carpeta_entrada: Path, archivo_salida: Path):
    """
    Fusiona todos los archivos de texto que comienzan con nombre_prefijo dentro de las subcarpetas de carpeta_entrada,
    generando un único archivo con un solo encabezado.
    """

    esta_encabezado = False  

    with archivo_salida.open("w", encoding="utf-8") as salida:

        # .iterdir() devuelve todos los archivos y carpetas dentro de una carpeta.
        # subcarpeta en este caso puede ser una carpeta o un archivo.
        for subcarpeta in carpeta_entrada.iterdir(): # recorre todos los elementos dentro de carpeta_entrada
            # verifico que realmente es una carpeta
            if not subcarpeta.is_dir():
                continue  # 🟨 sólo queremos procesar carpetas que contengan archivos .txt, no archivos sueltos.

            # .glob() Busca dentro de cada subcarpeta los archivos que: Comienzan con el nombre_prefijo (ej. "usu_individual_") y Terminan con .txt
            for archivo in subcarpeta.glob(f"{nombre_prefijo}*.txt"):
                # Abrir el archivo y escribir su contenido
                with archivo.open(encoding="utf-8") as f:
                    encabezado = f.readline()  # Leer el encabezado

                    # ✔️ Escribir encabezado solo una vez
                    if not esta_encabezado:
                        salida.write(encabezado)
                        esta_encabezado = True

                    # 🧾 Escribir el resto del archivo
                    for linea in f:
                        salida.write(linea)

    # ✅ Mensaje de confirmación
    print(f"fusión de archivos generado: {archivo_salida.name}")
---
🔈 **Traducimos campos codificados:**

- `CH04` → `CH04_str`: "Masculino" / "Femenino"
- `NIVEL_ED` → `NIVEL_ED_str`: nivel educativo en texto
- `V4` → `MATERIAL_TECHUMBRE`: tipo de material

🔧 **Creamos `CONDICION_DE_HABITABILIDAD` con reglas combinadas**  
Basadas en calidad de piso, baño, cocina, acceso al agua y techo.

🧠 **¿Por qué así?**

- “No podíamos usar `pandas`, así que usamos `csv.DictReader` para leer fila por fila en forma de diccionario. Es eficiente y nos permite trabajar con claves entendibles.”
- “Usamos `pathlib` en lugar de `os.path` porque es más moderno, legible y seguro para manipular rutas.”
- “Guardamos los archivos con las columnas nuevas en archivos como `*_fusionado_actualizado.csv` para separar los originales de los procesados y evitar sobrescribir.”

💬 **Preguntas:**

❓ *¿Por qué no usaron pandas?*  
“Porque estaba explícitamente prohibido en la consigna. Por eso usamos solo módulos estándar como `csv` y `pathlib`.”

❓ *¿Por qué usan DictReader en lugar de leer línea por línea?*  
“Porque `DictReader` convierte cada fila en un diccionario. Eso hace que sea más claro acceder a los campos por nombre (`fila['CH04']` en lugar de usar índices).”

❓ *¿Qué pasa si hay valores faltantes?*  
“Los manejamos con `get()` y validamos `if valor == '' or valor is None`. Así evitamos que el código se rompa.”

❓ *¿Qué ventajas tuvo modularizar (`fusionar_csv`, `constantes.py`)?*  
“Nos permitió reutilizar la lógica y mantener el notebook limpio, dejando ahí solo la parte explicativa y los resultados.”
