from fastapi import FastAPI
from .database import database as connection

from fastapi import FastAPI
from fastapi import APIRouter

from fastapi import status
from fastapi import Depends
from fastapi import HTTPException

from .database import User
from .database import Movie
from .database import UserReview

from fastapi.security import OAuth2PasswordRequestForm

from .routers import user_router
from .routers import review_router

#from .common import create_access_token

from .database import database as connection

app = FastAPI(title='Proyecto peliculas',
              description='Hola esta es una muestra de como hacer apis',
              version='1')
#crear rutas 
api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)
api_v1.include_router(review_router)

app.include_router(api_v1) # incluirlas sobre la aplicacion



# inicio eventos
@app.on_event('startup')
def startup():
    #print('El servidor va a comenzar')
    if connection.is_closed():
        connection.connect()
        #print('Exitosa la conneccion')

    connection.create_tables([User,Movie,UserReview])

@app.on_event('shutdown')
def shutdown():
    #print('El servidor se encuentra finalizando')
    if not connection.is_closed():
        connection.close()
        print('Cerrando connecion')


#final eventos

@app.get('/')
async def index():
    return 'Hola mundo desde un servidor en FastAPI'


@app.get('/about')
async def about():
    return 'About'