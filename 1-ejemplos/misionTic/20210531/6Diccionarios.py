"""
Autor: Carlos A Delgado
Fecha: 31 de Mayo de 2021
"""

diccionarioA = {}
diccionarioB = dict()

print(diccionarioA)
print(diccionarioB)

persona = {"nombre":"carlos","apellido":"delgado","edad":23,"email":"carlos@gmail.com","ciudad":"palmira","direccion":"Calle falsa 123"}

print(persona)
print(persona["nombre"])
print(persona["apellido"])
print(persona["edad"])
persona["edad"]=20
#Insertando un nuevo dato
persona["universidad"]="Universidad del Valle"

print(persona)
print(persona.get("nombre"))

#print(persona["apellido"]) Aqui falla
print(persona.get("apellido"))