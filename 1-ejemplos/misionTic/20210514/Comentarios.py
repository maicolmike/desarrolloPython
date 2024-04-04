'''
Autor: Carlos A Delgado
Fecha: 14 de Mayo de 2021
Este problema es un ejemplo de clase
'''
# Esto es un comentario de una sola línea

'''
Comentarios de varías lineas
'''
"""
Esto es un comentario de varias líneas
"""
#Esto es un comentario de una sola líneas
a = 3
b = 2 
def promedio(a,b,c):
  """
  a: int Es un número natural
  b: int Es un número natural
  c: int Es un número natual
  retorno: int Que es el promedio de la entrada
  """
  #Es es el calculo del promedio
  salida = (a+b+c)/3 

  if a > b:
    a = 8
    if a > c:
      b = 9
  
  return salida


print(promedio(1,2,3))