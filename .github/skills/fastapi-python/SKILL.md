---
name: fastapi-python
description: "Use when implementing, debugging, documenting, or validating FastAPI routes, Pydantic models, request validation, responses, or API integration in this Python project."
---

# FastAPI avanzado en Python

## Propósito

Implementar y mantener endpoints FastAPI con validación explícita, respuestas
predecibles y contratos documentados, siguiendo la arquitectura ya usada por
el proyecto.

## Cuándo usar esta skill

- Al crear o modificar endpoints o routers.
- Al cambiar modelos Pydantic, validaciones o respuestas.
- Al depurar errores HTTP, validación de solicitudes o integración de clientes.
- Al verificar que el menú de consola y la API continúan interoperando.

## Arquitectura de referencia

- `main.py` construye `FastAPI`, inicializa `app.state.movies` y registra
  `movies_router`.
- `routers/movies.py` define `router = APIRouter(prefix="/movies")`; accede al
  catálogo con `_movies(request)` y recibe el `Request` para acceder al estado.
- `schemas.py` es el lugar actual para el modelo Pydantic `Movie`, incluidas las
  restricciones de ID, título, descripción, fecha, calificación, categoría y
  recaudación.
- `cli.py` consume la API mediante HTTP y transforma los errores de validación
  para mostrarlos en español.
- FastAPI publica la documentación interactiva en `/docs`.

## Procedimiento

1. Inspecciona la aplicación, router, esquemas, clientes y documentación antes de
   cambiar un contrato.
2. Define y conserva método HTTP, prefijo, ruta, parámetros, cuerpo, modelo de
   respuesta y semántica de errores.
3. Añade rutas de películas al `APIRouter` existente y registra routers nuevos
   desde `main.py`; no mezcles su lógica con la interfaz de consola.
4. Centraliza los tipos y reglas de validación en los modelos Pydantic
   correspondientes. Comprueba qué campos son requeridos y cuáles tienen
   valores predeterminados antes de asumirlo.
5. Usa `response_model` y anotaciones coherentes con el valor realmente devuelto.
   Para recursos inexistentes, responde con un `HTTPException` adecuado en vez
   de devolver una estructura incompatible.
6. Accede al estado de la aplicación a través de `Request` y del helper
   existente; no crees copias del catálogo que diverjan.
7. Verifica con pruebas focalizadas o solicitudes HTTP: caso válido, datos
   inválidos, recurso ausente y comportamiento del cliente si es relevante.
   Confirma también que `/docs` refleja los contratos previstos.
8. Actualiza la documentación si cambian los endpoints, el esquema o las
   instrucciones de ejecución.

## Restricciones

- No cambies silenciosamente rutas, formatos, restricciones ni mensajes de error.
- No declares un modelo de respuesta incompatible con el objeto o colección que
  devuelve la función.
- No asumas que un ID duplicado está rechazado: comprueba la lógica existente y
  solo añade esa regla si el requisito lo establece.
- No cambies el almacenamiento en memoria por una base de datos, ni el ciclo de
  vida de la aplicación, sin una solicitud explícita.
- No captures toda excepción para devolver una respuesta de éxito.
- Mantén los errores que verá el usuario de la consola en español, de acuerdo
  con el patrón actual del cliente.
