def buscar_par(lista:list)->int:
	for elemento in lista:
		if elemento % 2== 0:
			return elemento


print(buscar_par([1,4,3,8,5]))

def buscar_id(lista:list,id_buscar:str)->str:
	for elemento in lista:
		if elemento == id_buscar:
			return elemento

print(buscar_id(["ADSDAS","ASSSSS","AAAAAA"],"AAAAAA"))

print(buscar_id(["ADSDAS","ASSSSS","AAAAAA"],"AAAAADA"))

