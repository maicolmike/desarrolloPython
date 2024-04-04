'''
Carlos A Delgado
28 de Mayo de 2021
'''
import math as md
def evaluar_propuesta_v1(lista_votos):
	'''
	lista_votos: Lista de booleanos, si es True el voto por SI, si el false el voto es por NO

	return booleano, True si se aprueba la propuesta, False si no se aprueba
	'''
	mayoria_absoluta = md.ceil(0.7*len(lista_votos)) #Mayoría absoluta

	votos_favor = 0
	for voto in lista_votos:
		#Esto lo puede hacer así porque voto es booleano
		if voto == True: #if voto:
			votos_favor+=1

		#Condicionales van separados son preguntas totalmente independientes
		if votos_favor>=mayoria_absoluta:
			return True

	return False

def evaluar_propuesta_v2(lista_votos):
	'''
	lista_votos: Lista de booleanos, si es True el voto por SI, si el false el voto es por NO

	return booleano, True si se aprueba la propuesta, False si no se aprueba
	'''
	mayoria_absoluta = md.ceil(0.7*len(lista_votos)) #Mayoría absoluta
	votos_favor = 0
	for i in range(0, len(lista_votos)):
		if lista_votos[i]:
			votos_favor += 1
		
		if votos_favor >= mayoria_absoluta:
			return True

	return False

def evaluar_propuesta_v3(lista_votos):
	'''
	lista_votos: Lista de booleanos, si es True el voto por SI, si el false el voto es por NO

	return booleano, True si se aprueba la propuesta, False si no se aprueba
	'''
	mayoria_absoluta = md.ceil(0.7*len(lista_votos)) #Mayoría absoluta
	votos_favor = 0
	contador = 0

	while contador < len(lista_votos):
		if lista_votos[contador]:
			votos_favor +=1
		
		if votos_favor >= mayoria_absoluta:
			return True
		
		contador += 1
	
	return False

def evaluar_propuesta_v4(lista_votos):
	'''
	lista_votos: Lista de booleanos, si es True el voto por SI, si el false el voto es por NO

	return booleano, True si se aprueba la propuesta, False si no se aprueba
	'''
	mayoria_absoluta = md.ceil(0.7*len(lista_votos)) #Mayoría absoluta

	votos_favor = 0
	for voto in lista_votos:
		#Esto lo puede hacer así porque voto es booleano
		if voto:
			votos_favor+=1

		#Condicionales van separados son preguntas totalmente independientes
		if votos_favor>=mayoria_absoluta:
			break

	if votos_favor >= mayoria_absoluta:
		return True
	else:
		return False	

votacion_1 = [True, True, False, True, True, True, False]

votacion_2 = [False, True, False, True, True, True, False]


print(evaluar_propuesta_v1(votacion_1))
print(evaluar_propuesta_v1(votacion_2))
print(evaluar_propuesta_v2(votacion_1))
print(evaluar_propuesta_v2(votacion_2))
print(evaluar_propuesta_v3(votacion_1))
print(evaluar_propuesta_v3(votacion_2))
print(evaluar_propuesta_v4(votacion_1))
print(evaluar_propuesta_v4(votacion_2))