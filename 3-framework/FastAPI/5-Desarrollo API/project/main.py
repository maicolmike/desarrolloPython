from fastapi import FastAPI
from database import database as connection 




app = FastAPI(title='Proyecto peliculas',
              description='Hola esta es una muestra de como hacer apis',
              version='1')

# inicio eventos
@app.on_event('startup')
def startup():
    #print('El servidor va a comenzar')
    if connection.is_closed():
        connection.connect()
        print('Exitosa la conneccion')

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