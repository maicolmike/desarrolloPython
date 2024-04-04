lista_notas = [1.2,2.5,4.5,3.4,5.0,3.8,4.5,1.3,2.9,2.8,4.5]
'''
Iteramos sobre la lista
'''
print(len(lista_notas))

notas_mayor_3 = 0 #Contador
for nota in lista_notas:
	if nota >= 3.0:
		notas_mayor_3+=1

print(notas_mayor_3)
'''
Revisar indice por indice
'''
notas_mayor_3 = 0
for i in range(0,len(lista_notas)):
	if lista_notas[i]>=3.0:
		notas_mayor_3+=1

print(notas_mayor_3)


