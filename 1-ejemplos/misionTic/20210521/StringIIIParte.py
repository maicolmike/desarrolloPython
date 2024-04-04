'''
Autor: Carlos A Delgado
Fecha: 21 de Mayo de 2021

Explicación Strings
'''

mensaje ="De: mision_mintic@ucaldas.edu.co Para: pepito@gmail.com, juan@hotmail.com, sandra@gmail.com, Paola@gmail.com"

#En este problema puede haber más destinatarios

print(mensaje.count("@"))
print(mensaje.count("gmail"))

nombre = "Carlos"
edad = 33
profesion = "Docente"

mensaje = f"Me llamo {nombre}, tengo {edad} años y mi profesión es {profesion}"
print(mensaje)

mensajeB = "Me llamo {}, tengo {} años y mi profesión es {}".format(nombre,edad,profesion)

print(mensajeB)