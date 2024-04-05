#BaseModel hace que si digito un numero donde mencione que va a ser texto lo convierte en texto
#Optional un valor es opcional para que no genere error
#field_validator validar 

from pydantic import BaseModel, field_validator
from typing import Optional

class User(BaseModel):
    username: str
    password: str
    email: str
    age: Optional[int] = None

    @field_validator('username')
    def username_validation_lenght(cls, username):
        if len(username) < 4:
            raise ValueError('La longitud mínima es de 4 caracteres')
        
        if len(username) > 50:
            raise ValueError('La longitud máxima es de 50 caracteres')
        
        return username
    
user1 = User(
    username='maic',
    password="1234",
    email='maicol-yela@hotmail.com',
    age=11
)

print(user1)
