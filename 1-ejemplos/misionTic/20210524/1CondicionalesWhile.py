'''
Autor: Carlos A Delgado
Fecha: 24-Mayo-2021
'''
"""
while <condicion>:
	-----
"""
i = 0
while i<=10:
	print(i)
	i+=1

print(f"Valor final de i es {i}")

j = 1000
while j>=0:
	print(j)
	j-=1
	if j % 13 == 0:
		break

while True:
	print("Por favor ingrese una opción")
	print("1. Para compras")
	print("2. Para reportes")
	print("3. Para despedir al jefe")
	print("4. Cargar nuevo información")
	print("5 Salir")

	opcion = int(input("Ingrese una opción numérica "))

	if opcion==1:
		print("No implementada")
	elif opcion==2:
		print("En el futuro quizas")
	elif opcion==3:
		print("Ojala estuviera hecho")
	elif opcion==4:
		print("Ya quisieras estuviera hecha")
	elif opcion==5:
		break
	else:
		print("Opción no válida")
	


