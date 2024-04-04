"""
Tipos de datos primitivos

    Integers: números Enteros
    Floats: números de punto flotante (decimales)
    Strings: cadena de caracteres (texto)
    Boolean: boolenaos (Verdadero o Falso)

Tipos de dato adicionales

    Datos en texto: str
    Datos numéricos: int, float, complex
    Datos en secuencia: list, tuple, range
    Datos de mapeo: dict
    Set Types: set, frozenset
    Datos booleanos: bool
    Datos binarios: bytes, bytearray, memoryview

"""
#string
my_name = "mario"
my_name2 = 'pedro'
print (my_name, my_name2)
print("Tipo de dato",type(my_name))
print("Tipo de dato",type(my_name2))

# enteros int
my_number = 12
print (my_number)
print("Tipo de dato",type(my_number))

#bolean
is_single = True
is_double = False
print(is_single)
print(is_double)
print("Tipo de dato",type(is_single))

#input el dato lo toma siemrpe como string
my_prueba = input("Cual es tu numero favorito: ")
print("Tipo de dato",type(my_prueba))