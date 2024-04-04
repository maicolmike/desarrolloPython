"""
Autor: Carlos A Delgado
Fecha: 24 Mayo de 2021
"""

for i in range(0,100):
	if i==10:
		break
	else:
		print(i)
print(":::::::::::::::")
for i in range(0,100):
	if i%3==0:
		continue
	
	print(i)

mensaje = "Hola mundo"
for letra in mensaje:
	print(letra)

for letra in "hola crack":
	print(letra.upper())

for letra in "gankee jg manco":
	print(letra.upper()) 