'''
Autor: Carlos A Delgado
Fecha: 21 de Mayo de 2021
'''

'''
problema:
El guardia de seguridad de una discoteca le
pregunta a usted su nombre, apellido y edad.
El guardia tiene el siguiente comportamiento de
acuerdo a la edad
[0, 18) "Niño {nombre} {apellido} usted no puede entrar"
[18,35] "Señor {nombre} {apellido} vaya a la sección joven"
(35,65) "Señor {nombre} {apellido} vaya a la sección adultos"
[65, +inf) "Señor {nombre} {apellido} vaya a la viejoteca"
En otro caso responde
"Señor {nombre} {apellido} la edad que usted dice {edad} no
es correcta"

'''

def guardia_seguridad_discoteca(nombre:str, apellido:str, edad:int)->str:
	'''
	nombre: str es el nombre de la persona que desea entrar a la discoteca
	apellido: str es el apellido de la persona que desea entrar a la discote
	edad: int es la edad de la persona que desea entrar a la discoteca
	'''
	respuesta_guardia = ""
	if edad>=0 and edad<18:
		respuesta_guardia = "Niño {} {} usted no puede entrar".format(nombre,apellido)
	elif edad>=18 and edad <= 35:
		respuesta_guardia = f"Señor(a) {nombre} {apellido} vaya a la sección joven"
	elif edad > 35 and edad < 65:
		respuesta_guardia = f"Señor(a) {nombre} {apellido} vaya a la sección adultos"
	elif edad >= 65:
		respuesta_guardia = f"Señor(a) {nombre} {apellido} vaya a la viejoteca"
	else:
		respuesta_guardia = f"Señor(a) {nombre} {apellido} la edad que usted dice {edad} no es correcta"

	return respuesta_guardia

print(guardia_seguridad_discoteca("Carlos","Delgado",17)) 
print(guardia_seguridad_discoteca("Julian","Pachecho",30))
print(guardia_seguridad_discoteca("Sara","Ramirez",38))
print(guardia_seguridad_discoteca("Martha","Velasco",67))
print(guardia_seguridad_discoteca("Wilmar","Cortes",-19))
#print(guardia_seguridad_discoteca("Wilmar","Cortes","deicinueve"))


def manejar_error(edad:int):
	salida = ""
	try:
		if edad < 18:
			salida = "Menor de edad"
		else:
			salida = "Mayor de edad"
	except:
		salida = "Edad no válida"

	return salida


print(manejar_error(9))
print(manejar_error(19))
print(manejar_error("deicinueve"))
