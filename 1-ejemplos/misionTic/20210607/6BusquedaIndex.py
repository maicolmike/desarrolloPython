
listaA = [1,2,3,4,5,6,12,7,8]
print(listaA.index(5))
print(listaA.index(12))

try:
	print(listaA.index(18))
except:
	print("El elemento no está")

print(listaA.index(4))



  
 


opcion = 0
while True:
	try:
		opcion = int(input("Ingrese un número "))
		break
	except:
		print("Por favor ingrese un número")
