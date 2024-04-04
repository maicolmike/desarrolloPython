'''
Autor: Carlos A Delgado
Fecha: 19 de Mayo de 2021
'''

def guardia_seguridad_discoteca(edad):
	'''
	edad: int: Indica la edad de la persona
	salida: str que nos indica la respuesta del guarda
	'''
	if edad >= 18:
		return "Puede entrar"
	else:
		return "No puede entrar"


respuestaA = guardia_seguridad_discoteca(12)
respuestaB = guardia_seguridad_discoteca(19)
respuestaC = guardia_seguridad_discoteca(30)

print(respuestaA)
print(respuestaB)
print(respuestaC)
print("==========================")
print("      Discoteca Bogotana   ")
print("==========================")
'''
[0,18)  "No puede entrar"
[18,25) "Entre a sección jovenes"
[25,35) "Entre a sección adulto joven"
[35,45) "Entre a sección adulto maduro"
[45,55) "Entre a sección ochentas"
[55,65] "Entre a seccion setentas"
(65, inf) "Entre a viejoteca
'''
def guardia_discoteca_bogotana(edad):
	'''
	edad: int
	str: Es el mensaje que nos emite el guardia
	'''
	if edad >= 0 and edad < 18:
		return "No puede entrar"
	elif edad >= 18 and edad < 25:
		return "Entre a sección jovenes"
	elif edad >= 25 and edad < 35:
		return "Entre a sección adulto joven"
	elif edad >= 35 and edad < 45:
		return "Entre a sección adulto maduro"
	elif edad >= 45 and edad < 55:
		return "Entre a sección ochentas"
	elif edad >= 55 and edad <= 65:
		return "Entre a seccion setentas"
	elif edad > 65:
		return "Entre a viejoteca"
	else:
		return "Intente de nuevo"

respuestaD = guardia_discoteca_bogotana(12)
respuestaE = guardia_discoteca_bogotana(19)
respuestaF = guardia_discoteca_bogotana(30)

print(respuestaD)
print(respuestaE)
print(respuestaF)

respuestaG = guardia_discoteca_bogotana(38)
respuestaH = guardia_discoteca_bogotana(50)
respuestaI = guardia_discoteca_bogotana(62)
respuestaJ = guardia_discoteca_bogotana(90)

print(respuestaG)
print(respuestaH)
print(respuestaI)
print(respuestaJ)

respuestaK = guardia_discoteca_bogotana(-20)
print(respuestaK)

def guardia_discoteca_bogotana_V2(edad):
	'''
	edad: int
	str: Es el mensaje que nos emite el guardia
	
	Esta versión tiene que hacer verificaciones de más, NO La recomiendo.
	'''
	salida = ""
	if edad >= 0 and edad < 18:
		salida = "No puede entrar"
	if edad >= 18 and edad < 25:
		salida = "Entre a sección jovenes"
	if edad >= 25 and edad < 35:
		salida = "Entre a sección adulto joven"
	if edad >= 35 and edad < 45:
		salida = "Entre a sección adulto maduro"
	if edad >= 45 and edad < 55:
		salida = "Entre a sección ochentas"
	if edad >= 55 and edad <= 65:
		salida = "Entre a seccion setentas"
	if edad > 65:
		salida = "Entre a viejoteca"
	if edad < 0:
		salida = "Intente de nuevo"

	return salida
