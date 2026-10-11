---
name: refactorizacion-y-reutilizacion
description: "Use when reorganizing Python code, refactoring modules, reducing duplication, reusing existing helpers, or preserving behavior and API contracts in this project."
---

# Refactorización y reutilización en Python

## Propósito

Reorganizar y mejorar el código con cambios pequeños, verificables y basados en
la estructura y el comportamiento reales del proyecto. Prioriza reutilización
sin alterar contratos existentes ni añadir abstracciones innecesarias.

## Cuándo usar esta skill

- Al separar responsabilidades entre módulos o paquetes.
- Al reducir lógica duplicada o buscar una implementación reutilizable.
- Al reorganizar la API, los esquemas o el cliente de consola.
- Al corregir un defecto causado por una refactorización.

## Arquitectura de referencia

- `main.py` crea `FastAPI`, inicializa `app.state.movies` e incluye el router.
- `schemas.py` define el modelo Pydantic `Movie` y sus restricciones.
- `routers/movies.py` agrupa las operaciones de películas en un `APIRouter`.
- `cli.py` es un cliente HTTP independiente; usa la API en lugar de importar
  o modificar directamente el almacenamiento del servidor.
- `requirements.txt` declara las dependencias de la aplicación.

Mantén estas responsabilidades separadas salvo que la tarea requiera
explícitamente otro diseño. La lista de películas vive en memoria y el cliente
de consola comparte cambios con FastAPI mediante solicitudes HTTP.

## Procedimiento

1. Lee los módulos afectados y localiza sus rutas, modelos, llamadores y pruebas.
2. Anota el comportamiento y los contratos que deben permanecer: rutas, métodos,
   parámetros, formato de datos, validación y mensajes observables.
3. Busca primero helpers o patrones existentes; reutilízalos antes de duplicar
   lógica.
4. Extrae o mueve solo la responsabilidad necesaria. Conserva imports claros y
   evita ciclos de importación, capas innecesarias y dependencias nuevas.
5. Actualiza la documentación directamente relacionada con la estructura o el
   modo de ejecución.
6. Ejecuta la comprobación más pequeña que cubra los cambios: sintaxis, lint,
   pruebas focalizadas y, si se toca la API, una comprobación HTTP apropiada.
7. Resume qué se reorganizó y qué se verificó; identifica cualquier límite no
   probado.

## Restricciones

- No trates una refactorización como autorización para cambiar el comportamiento.
- No dupliques el estado del catálogo en el menú de consola ni en otro módulo.
- No edites el entorno virtual (`venv`) para almacenar código de aplicación.
- No suprimas errores mediante excepciones amplias, valores por defecto
  silenciosos o respuestas exitosas ficticias.
- No añadas dependencias o capas de abstracción sin necesidad demostrable.
