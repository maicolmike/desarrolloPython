from pydantic import BaseModel # pydantic validar informacion que ingresa y sale
from pydantic import validator

class UserBaseModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls,username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('Longitud debe estar entre 3 a 50 caracteres')
        
        return username