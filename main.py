from fastapi import FastAPI, Request, Form, status, Depends
# libreria para usar cualquier motor de plantillas, rendirar plantillas
from fastapi.templating import Jinja2Templates
# redirigir al usuario
from fastapi.responses import RedirectResponse
import models
# estableciendo el motor y la sesión de SQLAlchemy
from database import engine, sessionlocal
# SQLAlchemy para manejar operaciones CRUD en un modelo de usuario, para interactuar con la base de datos.
from sqlalchemy.orm import Session
# crear todas las tablas de la base de datos que están definidas por los modelos
models.Base.metadata.create_all(bind=engine)
# indicamos desdedonde importaremos nuestros templates, para ello crearemos la carpeta templates
templates = Jinja2Templates(directory='./templates')

# se crea una instancia de FastAPI
app = FastAPI()


# app.mount('/static', StaticFiles(directory='static'), name='static')

# funcion que crea una nueva sesión de base de datos


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def home(request: Request, db: Session = Depends(get_db)):
    users = db.query(models.User).order_by(models.User.id.desc())
    return templates.TemplateResponse('index.html', {'request': request, 'users': users})


@app.get('/addnew')
async def add(request: Request):
    return templates.TemplateResponse('addnew.html', {'request': request})


@app.post('/add')
async def add(request: Request, tarea: str = Form(...), db: Session = Depends(get_db)):
    print(tarea)
    users = models.User(tarea=tarea)
    db.add(users)
    db.commit()
    return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)


@app.get('/edit/{user_id}')
async def edit(request: Request, user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return templates.TemplateResponse('edit.html', {'request': request, 'user': user})


@app.post('/update/{user_id}')
async def update(request: Request, user_id: int, tarea: str = Form(...), db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.id == user_id).first()
    users.tarea = tarea
    db.commit()
    return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)


@app.get('/delete/{user_id}')
async def delete(request: Request, user_id: int, db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(users)
    db.commit()
    return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)
