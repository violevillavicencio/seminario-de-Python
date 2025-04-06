Pasos para Ejecutar el Proyecto: 
1. Clonar el repositorio
Primero, clona el repositorio en tu máquina local. En la terminal ejecutá los siguientes comandos:

git clone --depth 1 --filter=blob:none --sparse https://github.com/violevillavicencio/seminario-de-Python.git
cd seminario-de-Python
git sparse-checkout set Entrega-2
cd Entrega-2

2. Crear y activar un entorno virtual
Es recomendable crear un entorno virtual para gestionar las dependencias del proyecto.

En Windows:
python -m venv venv
venv\Scripts\activate

En macOS o Linux:
python3 -m venv venv
source venv/bin/activate

3. Instalar las dependencias
Con el entorno virtual activado, instala las dependencias necesarias del proyecto ejecutando el siguiente comando:

pip install -r requirements.txt

Si no tienes instalado Jupyter, puedes instalarlo también ejecutando:

pip install notebook

4. Ejecutar el proyecto
Tienes dos formas de ejecutar el proyecto:

Opción 1: Ejecutar el notebook con Jupyter
Abre el notebook directamente con Jupyter ejecutando:

jupyter notebook notebooks/resultados.ipynb

Opción 2: Ejecutar el script desde la terminal
Si prefieres ejecutar el script directamente desde la terminal, usa el siguiente comando:

python src/resultados.py
