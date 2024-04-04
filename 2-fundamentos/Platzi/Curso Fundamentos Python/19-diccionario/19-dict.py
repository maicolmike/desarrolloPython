my_dict = {}

my_dict = {
    "nombre": "Maicol",
    "apellido" : "yela",
    "edad" : 12
}

print(my_dict)
print(len(my_dict))

#acceder a elemento del diccionario
print(my_dict["apellido"])  # sino encuentra la llave el progama no compila
print(my_dict.get("apellido")) # devuelve None si no encuentra la llave


# si la llave esta en el diccionario saldra True si no False
print("nombre" in my_dict)
print("nombre2" in my_dict)