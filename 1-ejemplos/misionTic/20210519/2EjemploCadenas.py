'''
Autor: Carlos A Delgado
Fecha: 19 de Mayo de 2021
'''

cadena1 = "Hola mundo"
cadena2 = 'Hola mundo'

print(type(cadena1))
print(type(cadena2))

print(cadena1 == cadena2)

print(cadena1[0])
print(cadena1[4])

print(cadena1[-1])

'''
Los string son tipos inmutables, es no los puedes cambiar
'''
mensaje = "hola"
#mensaje[0] = "H" Esto da un error

cadena = "Hola_mundo"
nueva_cadena = cadena[2:6]
print(nueva_cadena)
print("==================")
nueva_cadena_pro = cadena[:5]+"M"+cadena[6:]

print(nueva_cadena_pro)
print("==================")
nuevo_mensaje = "H"+mensaje[1:]
print(nuevo_mensaje)

nueva_cadena2 = cadena[5:]
print(nueva_cadena2)

nueva_cadena3 = cadena[:4]
print(nueva_cadena3)

palabra1 = "hola"
palabra2 = "perro"

if palabra1 < palabra2:
	print(f"{palabra1} es menor que {palabra2}")
else:
	print(f"{palabra1} es mayor o igual que {palabra2}")	

palabra3 = "hola".lower()
palabra4 = "Perro".lower()

if palabra3 < palabra4:
	print(f"{palabra3} es menor que {palabra4}")
else:
	print(f"{palabra3} es mayor o igual que {palabra4}")	

palabra5 = palabra3.lower()

palabra6 = "HolA Mundo"
print(palabra6.upper())
print(palabra6.capitalize())
print(palabra6)

palabra6_minusculas = palabra6.upper()

palabra7 = 'hola'

print(palabra6[100])