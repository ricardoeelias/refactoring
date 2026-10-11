# Skills del proyecto

Este archivo cataloga las dos skills especializadas del proyecto. Las
instrucciones que VS Code carga como agent skills están en `.github/skills/`;
cada skill tiene su propio `SKILL.md` con metadatos y procedimiento.

## Refactorización y reutilización de Python

Consulta [refactorizacion-y-reutilizacion](../.github/skills/refactorizacion-y-reutilizacion/SKILL.md)
para reorganizar módulos, reutilizar lógica y mantener el comportamiento y los
contratos existentes.

## Desarrollo avanzado con FastAPI

Consulta [fastapi-python](../.github/skills/fastapi-python/SKILL.md) para
implementar o mantener endpoints, routers, modelos Pydantic, validación,
respuestas e integración del cliente.

## Agente personalizado

El agente de proyecto [Python Refactor y FastAPI](../.github/agents/python-refactor-fastapi.agent.md)
lee y aplica la skill correspondiente antes de trabajar. Si una tarea combina
refactorización y desarrollo de la API, aplica ambas.
