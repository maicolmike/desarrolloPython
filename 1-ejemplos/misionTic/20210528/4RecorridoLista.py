"""
Autor: Carlos A Delgado
Fecha: 28 de Mayo de 2021

Tengo una lista de nombres
["Carlos","Andres","Paola", "Ana", "Lucia"]

Deseo saber cuantos nombres hay que tengan 5 
caracteres o menos

Retorna 3.

Diseña la función contar_nombres_cortos(lista):
"""

def contar_nombres_cortos(lista_nombres):
	'''
	lista_nombres: Lista de strings
	retorna int que es el número de nombres cortos, es decir cuya longitud es menor o igual 5.
	'''
	nombres_cortos = 0
	for nombre in lista_nombres:
		if len(nombre)<=5:
			nombres_cortos+=1

	return nombres_cortos

lst = ["Carlos","Andres","Paola", "Ana", "Lucia"]

print(contar_nombres_cortos(lst))