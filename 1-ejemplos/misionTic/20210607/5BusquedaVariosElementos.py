def buscar_todos_pares(lista:list)->list:
	salida = []
	for elemento in lista:
		if elemento % 2 == 0:
			salida.append(elemento)

	return salida

print(buscar_todos_pares([1,2,3,4,5,6,7,8,9,10,11,12]))

personas= [
	("212312321",True),
	("23123123",False),
	("AS323232",True),
	("223213213",True),
	("232131232",False)
]

def buscar_vacunados(lista:list)->list:
	salida = []

	for elemento in lista:
		if elemento[1]:
			salida.append(elemento)

	return salida

print(buscar_vacunados(personas))