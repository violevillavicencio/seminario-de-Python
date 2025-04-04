Para ver este proyecto, primero hay que clonar el repositorio. 
Se puede hacer con checkout parcial para descargar solamente la carpeta necesaria. 

Desde la terminal, ejecutá los siguientes comandos: 
git clone --depth 1 --filter=blob:none --sparse https://github.com/violevillavicencio, luego cd seminario-de-Python, después git sparse-checkout set Entrega-2, y por último cd Entrega-2.

Una vez dentro de la carpeta, se recomienda crear un entorno virtual. En Windows se hace con python -m venv venv y se activa con venv\Scripts\activate. En sistemas macOS o Linux, se usa python3 -m venv venv y se activa con source venv/bin/activate.

Con el entorno virtual activado, hay que instalar las dependencias del proyecto usando el comando pip install -r requirements.txt. Si no tenés instalado Jupyter, podés agregarlo también con pip install notebook.

Para ejecutar el proyecto, hay dos formas. Podés abrir el notebook directamente con Jupyter usando el comando jupyter notebook notebooks/resultados.ipynb, o bien ejecutar el script desde la terminal con python src/resultados.py.
