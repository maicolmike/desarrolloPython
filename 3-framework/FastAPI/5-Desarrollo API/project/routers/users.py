from typing import List
from typing import Optional

from fastapi import Cookie
from fastapi import Response
from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException

from fastapi.security import HTTPBasicCredentials

from ..database import User

from ..schemas import UserRequestModel
from ..schemas import UserResponseModel

from ..schemas import ReviewResponseModel

#from ..common import get_current_user


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
# crear nuevos usuarios
# cuando se trabaja con paquetes __init__.py toca hacerlo con router
router = APIRouter(prefix='/users')
@router.post('',response_model = UserResponseModel)
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
