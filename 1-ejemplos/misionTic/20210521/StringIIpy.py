'''
Autor: Carlos A Delgado
Fecha: 21 de Mayo de 2021
'''

cadena = "Hola mundo"
print(cadena.find("o"))
print(cadena.find("un"))

print(cadena.find("o",2))

'''
Diseñe una función que permita extraer el servidor de correo de un mensaje que trae al remitente, destinatario y la fecha del correo

De: paquita_gallego@vagancia.com A: radio@todelar.com 15-Marzo-2019

R/ vagancia.com

De: contacto@ucaldas.edu.co A: aspirante@mintic.gov.co 19-Mayo-2021

R/ ucaldas.edu.co
'''

def extraer_servidor_correo_remitente(men:str)->str:
	'''
	men: str. Es el mensaje que tiene la información de los correos

	retorna: str: Que es el servidor de correo que extraigo
	'''
	pos_arroba = men.find("@") #Posición del arroba
	pos_espacio = men.find(" ",pos_arroba) #Posición del espacio

	servidor_correo = men[pos_arroba+1:pos_espacio]

	return servidor_correo

resultadoA = extraer_servidor_correo_remitente("De: paquita_gallego@vagancia.com A: radio@todelar.com 15-Marzo-2019")

mensajeB = "De: contacto@ucaldas.edu.co A: aspirante@mintic.gov.co 19-Mayo-2021"
resultadoB = extraer_servidor_correo_remitente(mensajeB)

print(resultadoA)
print(resultadoB)


def extraer_servidor_correo_destinatario(men:str)->str:
	'''
	men: str. Es el mensaje que tiene la información de los correos

	retorna: str: Que es el servidor de correo que extraigo

	De: paquita_gallego@vagancia.com A: radio@todelar.com 15-Marzo-2019

	R/ todelar.com

	De: contacto@ucaldas.edu.co A: aspirante@mintic.gov.co 19-Mayo-2021

	R/ mintic.gov.co
	'''
	posicion_primera_arroba = men.find("@")

	posicion_segundo_arroba = men.find("@", posicion_primera_arroba+1)

	posicion_espacio = men.find(" ",posicion_segundo_arroba)

	servidor_destinatario = men[posicion_segundo_arroba+1:posicion_espacio]


	return servidor_destinatario


  