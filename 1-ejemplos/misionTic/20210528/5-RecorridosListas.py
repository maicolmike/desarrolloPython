"""
Autor: Carlos A Delgado
Fecha: 28 de Mayo de 2021

Tengo una lista de números y me gustaria
saber el número de elementos que son divisibles 
por 3 o por 7

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

6+2 = 8 (Respuesta)

Diseñar la función
contar_divisible_3o7(lista_numeros):
"""

def contar_divisible_3o7(lista_numeros):
	"""
	lista_numeros: lista de nùmeros

	retorna un entero que es el número de divisibles entre 3 o 7
	"""

	num_divisores = 0

	for num in lista_numeros:
		if num%3==0 or num%7==0:
			num_divisores+=1

	return num_divisores

listaA = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

print(contar_divisible_3o7(listaA))
