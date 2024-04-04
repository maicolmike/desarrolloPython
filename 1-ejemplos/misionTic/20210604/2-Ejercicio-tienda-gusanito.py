"""
La tienda el gusanito desea conocer el total de ventas por día, una venta
se puede ver como una tupla que contiene el número de producto comprado
y su precio unitario.

La tienda desea saber cuanto dinero ha obtenido durante el día considerando las 
ventas.

Una venta (10,2000)

Las ventas del dia se representan como una lista de tuplas, donde cada tupla representa
una venta realizada

[(10,2000),(3,200),(5,10000),(4,2300)]

Total 20000+600+50000+9200 = 79800

calcular_ventas(lista_ventas:list)->float:
"""

def calcular_ventas(lista_ventas:list)->float:
	"""
	lista_ventas es una lista de tuplas, donde cada tupla representa una cantidad de elementos comprados y su precio unitario

	retorna un float que indica el total de las ventas realizas en un periodo de tiempo
	"""
	total_ventas = 0

	#for j in range(0,len(lista_ventas))
  #  venta = lista_ventas[j]
	for venta in lista_ventas:
		total = 1
		#total = venta[0]*venta[1] #esta es otra manera de hacerlo, pero se debe comentariar lo del for y el total=1
		for i in range(0,len(venta)):
			total*=venta[i]
		total_ventas+=total

	return total_ventas

print(calcular_ventas([(10,2000),(3,200),(5,10000),(4,2300)]))

print(calcular_ventas([(4,150),(30,175),(6,12300),(10,2000),(3,200),(5,10000),(4,2300)]))