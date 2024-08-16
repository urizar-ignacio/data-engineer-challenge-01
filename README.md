# Data Engineer Challenge

### Ignacio Urízar
### Agosto, 2024

## Contenido del repositorio:
- El código con las soluciones se encuentra en la ruta `app/src/`
- El desarrollo y análisis completo del proyecto se encuentra en el archivo `app/src/challenge.ipynb`
- Se incluye un archivo con dependencias necesarias para el correcto funcionamiento del proyecto en `app/requirements.txt`
- Data de muestra se encuentra en archivo comprimido en `app/data/tweets.json.zip` (leer sección **Antes de comenzar**)
- Archivos de configuración de ambiente de desarrollo: `Dockerfile` y `docker-compose.yaml` con detalle de contenedor en que se ejecutó el proyecto.
- El archivo `CHALLENGE_README.md` contiene el enunciado del proyecto y las preguntas a responder. 

## Antes de comenzar:
Dado que el límite de tamaño de archivos en GitHub es de 100 MB, se incluyó la versión comprimida de la muestra de datos en formato zip en la ruta `app/data/`. Es necesario descomprimir este archivo antes de ejecutar cualquier método de este proyecto.

**NOTA:** El tamaño máximo recomendado de GitHub es de 50 MB, por lo que incluso la versión comprimida genera warnings al ser subida. Es recomendable incluir manualmente el archivo de muestra de datos descomprimido en la ruta `app/data/`.

## Fomas de ejecución:
### Docker (recomendada):
Este repositorio incluye una `Dockerfile` y un archivo `docker-compose.yaml`. Estos archivos permiten levantar un contenedor que incluye todas las dependencias necesarias y además asegura que el entorno de ejecución sea idéntico al que se usó durante su desarrollo y al que corresponden los outputs que se encuentran en el archivo `app/src/challenge.ipynb`.

Esta imagen usa Python 3.11.6.

Para levantar el contenedor se debe ejecutar el siguiente comando en la ruta razís de este repositorio:

```sh
docker-compose up --build -d
```

Esto ejecutará el contenedor en segundo plano, copiará todos los archivos de la carpeta `app/` al contenedor, instalará dependencias y además disponibilizará un jupyter server en el puerto 8888 del equipo.

Se puede ingresar jupyter desde `localhost:8888` e ingresar al notebook ubicado en `app/src/challenge.ipynb`.

### Ambiente local:
El archivo `app/src/challenge.ipynb` se puede revisar y ejecutar localmente siempre y cuando se cuente con una instalación de Python compatible con las dependencias incluídas en el archivo `app/requirements.txt`, y requerirá que se instalen en caso de no estar ya disponibles con `pip install -r app/requirements.txt`.