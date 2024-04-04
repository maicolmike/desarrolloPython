"""
Autor: Señor del Mintic
Fecha: 24-Mayo de 2021
"""

def mostrar_dinero_disponible(total_dinero):
	while total_dinero>0:
		precio = float(input("Digite el precio "))

		if precio <= total_dinero:
			total_dinero -= precio
		else:
			print("No tienes dinero para esto")

		print(f"Aun le queda {total_dinero} para gastar")

	return total_dinero

saldo = mostrar_dinero_disponible(100000)
mensaje = f"El saldo final es {saldo}"
print(mensaje)