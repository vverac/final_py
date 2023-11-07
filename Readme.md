# Mi Proyecto

To-do

## Descripción

Mi Proyecto es una aplicación web que utiliza el framework de Fastapi para crear una aplicacion de tareas pendientes o To-do.

## Instalación

1. Clona el repositorio: `git clone https://github.com/vverac/final_py`

instalar Fastapi: pip install "fastapi[all]",
esto se utiliza para instalar FastAPI y todas sus dependencias opcionales en un entorno Python

La opción[all] en el comando de instalación indica a pip que también debe instalar todas las dependencias opcionales de FastAPI. Estas dependencias opcionales pueden incluir, pero no se limitan a:

jinja2: Necesario si quieres utilizar la configuración predeterminada de templates.
python-multipart: Necesario si quieres soporte con "parsing" de formulario, con request.form().
itsdangerous: Necesario para soporte a SessionMiddleware.
pyyaml: Necesario para soporte a SchemaGenerator de Starlette(probablemente no necesitarás esto con FastAPI).
uvicorn: Para el servidor que carga y sirve tu aplicación.
orjson: Necesario si quieres utilizar ORJSONResponse

## Uso

Para usar Mi Proyecto, ejecuta el siguiente comando:

uvicorn main:app --reload
