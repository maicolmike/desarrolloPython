'''
Carlos A Delgado
28 de Mayo de 2021


Se requiere mayoria absoluta de todos los votos o sólo mayoría simple (50%+1) aprueba
'''
import math as md
def evaluar_propuesta(lista_votos,sexo):
	'''
	lista_votos: Lista de booleanos, si es True el voto por SI, si el false el voto es por NO

	return booleano, True si se aprueba la propuesta, False si no se aprueba
	'''
	mayoria_absoluta = md.ceil(0.7*len(lista_votos)) #Mayoría absoluta
	mayoria_simple = md.ceil(0.5*len(lista_votos))

	votos_favor = 0
	votos_favor_mujeres = 0
	for i in range(0,len(lista_votos)):

		if lista_votos[i] and sexo[i] == 'f':
			votos_favor+=1
			votos_favor_mujeres+=1
		
		if lista_votos[i] and sexo[i] == 'm':
			votos_favor+1
		
		if votos_favor >= mayoria_absoluta or votos_favor_mujeres >= mayoria_simple:
			return True
	
	return False

votacion_1 = [True,False,True,True,True,False,False]

sexo_1 = ['m','f','m','m','m','f','f']

sexo_2 = ['f','m','f','f','f','m','m']

print(evaluar_propuesta(votacion_1,sexo_1))

print(evaluar_propuesta(votacion_1,sexo_2))