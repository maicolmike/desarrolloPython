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

#para enviar respuesta
class UserResponseModel(BaseModel):
    id : int
    username : str
    #password : str
    #create: datetime
    #si serializamos utilziamos esto
    
    class condif:
        orm_mode = True
        getter_dict = PeeweeGetterDict

