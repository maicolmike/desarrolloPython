import pandas as pd

datos = pd.read_csv("game.csv")

lista = datos.values.tolist()

#print(lista)
"""
lista es una lista con listas internas, donde cada lista tiene esta estructura
0 -> Temporada
1 -> Numero del episodio
2 -> Nombre episodio
3 -> Fecha de emisión
4 -> Calificación
5 -> Numero de votos
"""
def determinar_ultima_temprada(lista_episodios:list)->int:
	maxi = 1
	for episodio in lista_episodios:
		if episodio[0]>maxi:
			maxi = episodio[0]

	return maxi


def promedio_temporadas(lista_episodios:list)->lista:
	"""
	list que recibe es una matriz con la información de toda la temporada


	int que recibe es el número de temporada va 1 a 8.

	Retorna una lista de diccionarios

	{
		"temporada":temporada
		"promedio_rating":promedio_rating,
		"promedio_votes":promedio_votos

	}

	Los promedios están redondeados a un decimal round(x,1)
	"""
	salida = []
	ultima_temporada = determinar_ultima_temprada(lista_episodios)
	for temporada in range(1,ultima_temporada):
		num_episodios = 0
		suma_rating = 0
		suma_votos = 0
		for episodio in lista_episodios:
			if episodio[0] == temporada:
				num_episodios+=1
				suma_rating+=episodio[4]
				suma_votos+=episodio[5]

		promedio_rating = round(suma_rating/num_episodios,2)
		promedio_votos = round(suma_votos/num_episodios,2)

		diccionario = {
			"temporada":temporada,
			"promedio_rating":promedio_rating,
			"promedio_votes":promedio_votos
		}
		salida.append(diccionario)

	return salida

(print (promedio_temporadas(lista)))