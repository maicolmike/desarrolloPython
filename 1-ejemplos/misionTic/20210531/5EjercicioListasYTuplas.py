"""
Autor: Carlos A Delgado
Fecha: 31 de Mayo de 2021

Ejercicio 1:

Declarar una lista de listas con esta caracteristica, el primer elemento de cada lista
va incrementando 1 en 1, de 1 hasta 5, el segundo elemento es dos veces el primero y el tercero es
tres veces el primero,

[1,2,3],[2,4,6] ....

Declarar una lista de tuplas (cinco tuplas) en la cual cada tupla tiene en su primera posición
el nombre de una persona, en la segunda posición su edad y en la tercera posición
su salario.

[ ("Carlos",23,2320000), ]

De estas listas acceder a algunos elementos internos. 
"""

listaA = [[1,2,3],[2,4,6],[3,6,9],[4,8,12],[5,10,15]]

print(listaA[4][1])
print(listaA[2][1])

listaB = [ ("Carlos",23,2320000), ("Paola",22,200000),("Pedro",34,100000),("Juana",55,200000),("Lucas",32,2000000) ]


print(listaB[3][0])
print(listaB[4][2])