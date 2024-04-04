"""
Carlos A Delgado
02-Junio de 2021
"""

diccionario = {"palmira":{"departamento":"valle",
                           "poblacion": 350000,
                           "num_museos":3},
                "manizales":{"departamento":"caldas",
                             "poblacion":434403,
                             "num_museos":4},
                "bogota":{"departamento":"bogota",
                          "poblacion":8500000,
                          "num_museos":20}
                }
def insertar_ciudad(ciudad):
	if(diccionario.get(ciudad)==None):
		departamento = input("Ingrese el departamento ")
		poblacion = int(input("Ingrese la población "))
		num_museos = int(input("Ingrese el número de muses "))

		datos = {}
		datos["departamento"] = departamento
		datos["poblacion"] = poblacion
		datos["num_museos"] = num_museos

		diccionario[ciudad] = datos
		print("Se ha agregado con éxito la nueva ciudad")
	else:
		print("La ciudad ya existe")

def elminar_ciudad(ciudad):
	if diccionario.get(ciudad)!=None:
		diccionario.pop(ciudad)
	else:
		print("La ciudad no existe")

def consultar_ciudad(ciudad):
	if diccionario.get(ciudad)!=None:
		datos_ciudad = diccionario[ciudad]
		for llave, valor in datos_ciudad.items():
			print(f"{llave} es {valor}")
	else:
		print("La ciudad no existe")

def consultar_todo():
	for llave, ciudad in diccionario.items():
		print(f"La ciudad de {llave}")
		for llave2, valor2 in ciudad.items():
			print(f"{llave2} es {valor2}")

def menu():
	while True:
		print("Ingrese una opción:")
		print("1. Insertar nueva ciudad")
		print("2. Eliminar ciudad")
		print("3. Consulta ciudad")
		print("4. Consultar todo")
		print("5. Salir")
		opcion = int(input())

		if opcion == 1:
			ciudad = input("Ingrese la nueva ciudad sin espacios ")
			insertar_ciudad(ciudad)
		elif opcion == 2:
			ciudad = input("Ingrese la nueva ciudad sin espacios ")
			elminar_ciudad(ciudad)
		elif opcion == 3:
			ciudad = input("Ingrese la nueva ciudad sin espacios ")
			consultar_ciudad(ciudad)
		elif opcion == 4:
			consultar_todo()
		elif opcion == 5:
			break
		else:
			print("Opción no válida\n")

menu()