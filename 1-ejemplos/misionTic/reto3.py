'''
Autor: Michael Yela Valencia
Fecha: 27/05/2021
'''
#inicio de funcion generarTablaPosicion
def generarTablaPosicion(nombre, cantPartidosGanados, cantPartidosPerdidos, cantPartidosEmpatados, numGolesFavor, numGolesContra):
  puntos_partido_ganado = 3
  puntos_partido_perdido = 0
  puntos_partido_empatado = 1
  puntos=(cantPartidosGanados*puntos_partido_ganado) + (cantPartidosPerdidos*puntos_partido_perdido) + (cantPartidosEmpatados*puntos_partido_empatado)
  diferencia=(numGolesFavor-numGolesContra)
  return(f"Equipo: {nombre} Puntos: {puntos} Diferencia: {diferencia}")
#final de la funcion generarTablaPosicion   
# inico de la aplicacion  
nombre=input("digite el nombre de su equipo:")
cantPartidosGanados=int(input("digite la cantidad de partidos ganados:"))
cantPartidosPerdidos=int(input("digite la cantidad de partidos perdidos:"))
cantPartidosEmpatados=int(input("digite la cantidad de partidos empatados:"))
numGolesFavor=int(input("digite el numero de goles a favor:"))
numGolesContra=int(input("digite el numero de goles en contra:"))
#generarTablaPosicio() asi se llama una funcion, se le envia los parametros al a funcion 
# resultado es una variable que recogera el valor que retornara la funcion generarTablaPosicio
resultado=generarTablaPosicion(nombre,cantPartidosGanados,cantPartidosPerdidos,cantPartidosEmpatados,numGolesFavor,numGolesContra)
print(resultado)