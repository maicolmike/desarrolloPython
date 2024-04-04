"""
Autor: Carlos A Delgado
Fecha: 24 de Mayo de 2021
"""
def gaussito(n):
	"""
	n es el valor del limite de la sumatoria

	retorna int que es la suma desde 0 hasta n
	"""
	suma = 0
	for i in range(0,n+1):
		suma += i

	return suma


def gaussito_dec(n):
	"""
	n es el valor del limite de la sumatoria

	retorna int que es la suma desde 0 hasta n
	"""
	suma = 0
	for i in range(n,-1,-1):
		suma += i

	return suma

def gaussito_while(n):
	"""
	n es el valor del limite de la sumatoria

	retorna int que es la suma desde 0 hasta n
	"""
	contador = 0
	suma = 0
	while contador<=n:
		suma += contador
		contador+=1
	
	return suma

def gaussito_while_dec(n):
	"""
	n es el valor del limite de la sumatoria

	retorna int que es la suma desde 0 hasta n
	"""
	contador = n
	suma = 0
	while contador>=0:
		suma += contador
		contador-=1
	
	return suma

print(gaussito(100))
print(gaussito(10000))
print(gaussito(1000000))
print(gaussito_while(100))
print(gaussito_while(10000))
print(gaussito_while(1000000))

print(gaussito_dec(100))
print(gaussito_while_dec(100))
