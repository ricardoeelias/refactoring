# Catálogo de películas

API de ejemplo para consultar y administrar un catálogo de películas con
FastAPI, más un menú interactivo de consola.

## Requisitos

- Python 3.10 o posterior.
- Dependencias de `requirements.txt`.

## Instalación

Desde la raíz del proyecto, crea y activa un entorno virtual e instala las
dependencias:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

En Linux o macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Ejecutar la API

Desde la raíz del proyecto:

```console
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Abre <http://127.0.0.1:8000/docs> para probar la API interactiva. Los endpoints
de películas están agrupados bajo el prefijo `/movies`:

| Operación | Endpoint |
| --- | --- |
| Listar películas y filtrar por género | `GET /movies/` |
| Buscar una película por ID | `GET /movies/{movie_id}` |
| Crear una película | `POST /movies/` |
| Actualizar una película | `PUT /movies/{movie_id}` |
| Eliminar una película | `DELETE /movies/{movie_id}` |

Creación y actualización utilizan el modelo Pydantic `Movie`, definido en
`schemas.py`. La actualización identifica la película por el ID de la ruta y
recibe también un `id` en el cuerpo; el ID del cuerpo no reemplaza el de la ruta.
Las películas iniciales están definidas en `main.py`. El almacenamiento es en
memoria y se restablece al reiniciar el servidor.

## Menú de consola

Con la API ejecutándose, abre otra terminal en la raíz del proyecto y ejecuta:

```console
python cli.py
```

El menú se conecta por defecto a `http://127.0.0.1:8000`. Para usar otra
dirección, define la variable de entorno `MOVIES_API_URL`.

## Datos de prueba

El directorio `docs/` contiene un PDF con ejemplos para probar la validación de
los endpoints.
