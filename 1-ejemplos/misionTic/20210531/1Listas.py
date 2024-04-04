'''
Autor: Carlos A Delgado
Fecha: 31 de Mayo de 2021
'''

listaA = [1,2,3,4]
listaB = ["Carlos","Ana","Paola"]
listaC = [True,False,True,True]
listaD = [1.2,3.2,2.3]
listaE = ["Carlos",1.2,True] #No usar porque nosotros las iteramos

#Las listas son mutables

print(listaA)
listaA[0]=100
print(listaA)

lista = []

for i in range(0,101):
	lista.append(i)

print(lista)

lista.remove(95)
print(lista)

print(lista[1:3])
print(lista[10:14])
suma = 0
for elm in lista:
	suma += elm

print(suma)

"""Rangos"
"""
a = 8

#[1,3)
if a>=1 and a<3:
	print("xd")