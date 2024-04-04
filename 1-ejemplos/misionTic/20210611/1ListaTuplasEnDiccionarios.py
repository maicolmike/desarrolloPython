"""
Autor: Carlos A Delgado
Fecha: 11 de Junio de 2021


En una tienda se necesita una aplicación para manejar el consolidado de ventas. Cada venta es una tupla con los códigos de los productos, los cuales son

100 -> Papaya -> 200
200 -> Mango -> 400
300 -> Uva -> 400
400 -> Pan -> 500
500 -> Manzana -> 800

El consolidado llega como una lista de tuplas por cada venta realizada

[(100, 100,100, 200, 300, 300),
(100, 200, 200, 200,300,400 ),
(500,500,500,200,200,300,500,500)]

Salida quiero que sea un lista de diccionarios de la siguiente manera, que cada elemento eval

{
	"numero_elementos":numero_elementos,
	"papaya":pagado_papaya,
	"mango":pagado_mango,
	"uva": pagado_uva,
	"pan": pagado_pan,
	"manzana": pagado_manzana,
	"total_venta": total_venta
}

[{....},{.....},{.....}]
"""

def consolidar_ventas(ventas:list)->list:
	salida = []

	for venta in ventas:
		dic_ven = {
							"numero_elementos":0,
							"papaya":0,
							"mango":0,
							"uva": 0,
							"pan": 0,
							"manzana": 0,
							"total_venta": 0
						}
		for item in venta:
			dic_ven["numero_elementos"]+=1

			if(item==100):
				dic_ven["papaya"]+=200
				dic_ven["total_venta"]+=200
			elif(item==200):
				dic_ven["mango"]+=400
				dic_ven["total_venta"]+=400
			elif(item==300):
				dic_ven["uva"]+=400
				dic_ven["total_venta"]+=400
			elif(item==400):
				dic_ven["pan"]+=500
				dic_ven["total_venta"]+=500
			elif(item==500):
				dic_ven["manzana"]+=800
				dic_ven["total_venta"]+=800
			else:
				print(f"El item {item} no se encuentra")

		salida.append(dic_ven)

	return salida

print(consolidar_ventas([(100, 100,100, 200, 300, 300),(100, 200, 200, 200,300,400 ),(500,500,500,200,200,300,500,500)]))

import math

print(math.ceil(2323.3))