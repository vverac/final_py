from fastapi import FastAPI, Request
# libreria para usar cualquier motor de plantillas
from fastapi.templating import Jinja2Templates


# indicamos desdedonde importaremos nuestros templates, para ello crearemos la carpeta templates
templates = Jinja2Templates(directory='./templates')

# se crea una instancia de FastAPI
app = FastAPI()


@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/addnew')
async def add(request: Request):
    return templates.TemplateResponse('addnew.html', {'request': request})
