from fastapi import FastAPI, Request, Form, status
# libreria para usar cualquier motor de plantillas
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

import models
from database import engine, sessionlocal
# SQLAlchemy para manejar operaciones CRUD en un modelo de usuario, para interactuar con la base de datos.
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
# indicamos desdedonde importaremos nuestros templates, para ello crearemos la carpeta templates
templates = Jinja2Templates(directory='./templates')

# se crea una instancia de FastAPI
app = FastAPI()


# funcion que crea una nueva sesión de base de dato
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/addnew')
async def add(request: Request):
    return templates.TemplateResponse('addnew.html', {'request': request})


@app.post('/add')
async def add(request: Request, tarea: str = Form(...)):
    print(tarea)
    return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)
