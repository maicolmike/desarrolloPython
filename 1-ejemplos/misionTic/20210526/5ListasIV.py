listaA = [1,2,3,4,5,6]
listaB = listaA.copy()
print(listaA)
print(listaB)

listaB.append(7)
print(listaB)
print(listaA)

listaC = ["Carlos","Paola","Juan"]
listaD = listaC[:]
listaD[0] = "Maria"
print(listaC)
print(listaD)