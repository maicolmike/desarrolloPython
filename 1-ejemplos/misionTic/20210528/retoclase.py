def calcular_divisibles(lista_num):
	
	contador = 0
	for numero in lista_num:
      
		if (numero)%3==0 or (numero)%7==0:
			contador+=1

	return contador

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

print(calcular_divisibles(lst))