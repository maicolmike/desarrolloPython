
listaA = [[1,2,3],[4,5,6],[7,8,9]]

#Iterativo
for elm in listaA:
	for interno in elm:
		print(interno)

#Indices
for i in range(0,len(listaA)):
	for j in range(0,len(listaA[i])):
		print(listaA[i][j])

listaA[0][1] = 200
print(listaA)

listaB = [(10,11,12),(13,14,15),(16,17,18)]

for tupla in listaB:
	for elm in tupla:
		print(elm)


tupla = ([1,2,3],[4,5,6],[7,8,9])
print(tupla)
tupla[0][1] = 4
print(tupla)
