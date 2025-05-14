
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
