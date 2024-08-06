# guia de estilo PEP-8 - reglas ya establecidas

# para las clases se utiliza CamelCase donde se pone el primer caracter de cada palabra en mayusculas - 
class UserAdmin():
    def __init__(self, username, password=''):
        self.username = username
        self.password = password
    # metodos y funciones - snake_case
    def set_password(self):
        pass

# para las variables debe poseer caracteres en minusculas, si tiene mas de dos palabras utilizar guion bajo - snake_case
cody_user = UserAdmin('cody')
print(cody_user)
print('hola mundo')