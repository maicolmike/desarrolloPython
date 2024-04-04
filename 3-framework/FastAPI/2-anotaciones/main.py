#variables
#funciones
# Clases
# colecciones 


# variables
a: str = "hola mundo"
b: int = 11
c: float = 3.14
d: bool = True


#funciones
def suma (numero1: int , numero2: int )-> int :
    return numero1 + numero2


valor1: int = 11
valor2: int = 20
valor3: int

resultado: int = suma(valor1,valor2)
print("La suma es: ", resultado)


#clases
class User():

    def __init__(self, username:str, password:str) -> None:
        self.username = username
        self.password = password

    def saluda (self)-> str:
        return f'hola {self.username}'
    
cody = User('Cody','password123')

print(cody.saluda())