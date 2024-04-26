from fastapi import FastAPI
from database import database as connection

from database import User
from database import Movie
from database import UserReview

from schemas import UserRequestModel
from fastapi import HTTPException
from schemas import UserResponseModel

app = FastAPI(title='Proyecto peliculas',
              description='Hola esta es una muestra de como hacer apis',
              version='1')

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
'''
@app.post('/users')
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).exists():
        return HTTPException(409,'El username ya se encuentra en uso')

    hash_password = User.create_password(user.password)

    user = User.create(
        username = user.username,
        #password = user.password
        password = hash_password
    )
    #return user.id
    return {
        'id': user.id,
        'username': user.username,
        #'pass': user.password,
        'create': user.created_at
    }
'''

@app.post('/users',response_model = UserResponseModel)
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).exists():
        return HTTPException(409,'El username ya se encuentra en uso')

    hash_password = User.create_password(user.password)

    user = User.create(
        username = user.username,
        #password = user.password
        password = hash_password
    )
    #return UserResponseModel(id= user.id, username= user.username, create= user.created_at)
    return user