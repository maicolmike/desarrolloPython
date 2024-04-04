
"""
Autor: Carlos A Delgado
Fecha: 07 de Junio de 2021

Una tienda tiene un inventario de productos, cada producto tiene un código (numerico)
tiene un nombre (str), una disponibilidad (int) un valor (float)

Esto va estar codificado en un diccionario

inventario = {
                       01: {"nombre":"pollo", disponibilidad: 10, valor:10000},
                       02: {"nombre":"chocorramo", disponibilidad: 100, valor: 2000},
                       }
Diseñe la función venta que recibe una lista de codigos de productos a comprar, por ejemplo
[01,01,01,02,02], entonces usted debe
1) Si algun producto no está en el diccionario emitir un mensaje de error
2) Si todos los productos están, entonces verificar
a) Que el inventario no quede negativo, en ese caso retornar un mensaje de error
b) Que si todo está bien, retornar el valor de la compra.

inventario = {
                       1: {"nombre":"pollo", disponibilidad: 7, valor:10000},
                       2: {"nombre":"chocorramo", disponibilidad: 98, valor: 2000},
                       }			
[1,1,1,2,2]
Valor total: 34000.      
vender_producto(..)   inventario={}	
"""
inventario = { 1: {"nombre":"pollo", "disponibilidad": 7, "valor":10000},
              2: {"nombre":"chocorramo", "disponibilidad": 98, "valor":2000}
							}	

def vender_producto(productos:list)->float:
	"""
	productos:lista de código de inventario

	retorna un float que es el precio de venta
	"""
	venta = {}
	total = 0.0
	for prod in productos:
		if venta.get(prod)!=None: #que esta
			venta[prod]+=1
		else:
			venta[prod]=1

	for codigo,num_unidades in venta.items():
		if inventario.get(codigo)!=None:
			if inventario[codigo]["disponibilidad"]>=num_unidades:
				total += num_unidades*inventario[codigo]["valor"]
			else:
				print(f"El producto {codigo} tiene disponible únicamente {inventario[codigo]['disponibilidad']} y por ello se no puede vender {num_unidades}")
				return 0.0
		else:
			print(f"El producto {codigo} no está disponible")
			return 0.0

	#Actualizo el inventario
	for codigo,num_unidades in venta.items():
		inventario[codigo]["disponibilidad"]-=num_unidades

	return total

def agregar_inventario():
	num_elementos = int(input("Ingrese el número de productos "))

	for i in range(0,num_elementos):
		codigo = int(input("Ingrese el código "))
		num_unidades = int(input("Ingrese el número unidades "))
		if inventario.get(codigo)!=None:
			inventario[codigo]["disponibilidad"]+=num_unidades
		else:
			nombre = input("Ingres el nombre producto ")
			valor =float(input("Ingrese el valor del producto "))

			producto = {
				"nombre":nombre,
				"disponibilidad":num_unidades,
				"valor":valor
			}

			inventario[codigo]=producto


print(vender_producto([1,1,1,2,2]))
print(inventario)

print(vender_producto([1,1,1,1,1,2,2]))

agregar_inventario()
print(inventario)