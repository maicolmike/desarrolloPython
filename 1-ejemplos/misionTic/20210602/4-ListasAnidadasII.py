listaA = [[1,2,3],[4,5,6],[7,8,9]]

suma = 0
for lst in listaA:
	for elm in lst:
		suma+=elm

"""
suma = 0
for i in range(0,len(listaA)):
	for j in range(0,len(listaA[i])):
		suma+=lista[i][j]
"""

print(suma)

def maximo(lista:lst)->int:
	"""
	lista: Es un lst anidado que tiene números

	retorno es el valor máximo
	"""
	maximo = lista[0][0]

	for lst in lista:
		for elm in lst:
			if elm > maximo:
				maximo = elm

	return maximo

print(maximo([[1,2,3],[4,5,6],[7,8,9]]))

print(maximo([[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]))

def suma_condicionada(lista:lst)->int:
	"""
	lista es una lista anidada de números enteros

	retorna int: Que es la suma de los segundo elementos de la listas internas
	"""
	suma = 0

	for lst in lista:
		suma+=lst[1]
	
	return suma

print(suma_condicionada([[1,2,3],[4,5,6],[7,8,9]]))

print(suma_condicionada([[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]))