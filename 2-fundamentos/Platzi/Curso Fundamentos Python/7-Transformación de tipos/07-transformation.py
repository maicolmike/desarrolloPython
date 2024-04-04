"""
Transformación o Constructor.

Cuando queremos transformar un valor numérico o alfabético, lo realizamos a traves de la transformación, de allí es que podemos decir que Python es un 
lenguaje que está Orientada a Objetos:

int( ) : Construye un entero literal a través de otro litera de tipo entero, un literal flotante (elimina todos los decimales y los convierte en números enteros)
o una cadena ( siempre y cuando sea de tipo entero.

float( ): Construye un numero flotante a partir de un literal entero.

str( ): Construye un literal a través de una gran cantidad de tipo de datos, incluyendo cadenas de textos, enteros y flotantes.

"""

name= "maicol"
print(type(name))
name= 12
print(type(name))
name= True
print(type(name))

age = 12
print("Mi edad es",age)
#print("Mi edad es" + age) # si intentamos esto nos genera error que espera str
print("Mi edad es " + str(age))
print(f"Mi edad es {age}")

age = input('Escribe tu edad: ')
print(type(age))
print(f"Mi edad es {age}")
age= int(age) # se transforma de str a int
print(type(age))