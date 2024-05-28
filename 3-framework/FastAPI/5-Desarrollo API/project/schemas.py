from pydantic import BaseModel # pydantic validar informacion que ingresa y sale
from pydantic import validator
from datetime import datetime  # Importa datetime

from pydantic.utils import GetterDict
from typing import Any
from peewee import ModelSelect

class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls,username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('Longitud debe estar entre 3 a 50 caracteres')
        
        return username


#Serializar objetos
class PeeweeGetterDict(GetterDict):
    def get(self, key:Any, default: Any= None):
        res= getattr(self._obj, key , default)
        if isinstance(res,ModelSelect):
            return list(res)
        return res  

#configurar
class ResponseModel(BaseModel):
    
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

#para enviar respuesta
class UserResponseModel(ResponseModel):
    id : int
    username : str
    #password : str
    #create: datetime
    #si serializamos utilziamos esto

# --------- movie -----

class MovieResponseModel(ResponseModel):
    id: int
    title: str

# -------- review   ----- 
class ReviewValidator():
    @validator('score')
    def score_validator(cls, score):
        
        if score < 1 or score > 5:
            raise ValueError('El rango para score es de 1 a 5.')

        return score

class ReviewRequestModel(BaseModel,ReviewValidator):
    user_id: int
    movie_id: int
    review: str
    score: int

class ReviewResponseModel(ResponseModel):
    id: int
    #movie_id: int
    movie: MovieResponseModel # relacionandolo
    review: str
    score: int

class ReviewRequestPutModel(BaseModel,ReviewValidator):
    review: str
    score: int