'''
Autor: Carlos A Delgado
Fecha: 17 de Mayo de 2021
Este archivo es de ejemplo para las variables
'''

a = 3 #Variable global
print(a)

def funcion(x):
  '''
  x, y son locales (declaradas dentro de la función)
  a, b son globales (declaradas por fuera de la función Y antes de su invocación) 
  '''
  y = x + 8*a*b #local
  return x+y

b = 8 #Variable global

print(funcion(5))


###Otro caso

a = 8
b = 9
'''
WARNING: NO NOMBRAR VARIABLES LOCALES CON EL MISMO NOMBRES DE LA GLOBALES

¿Porque de la recomendación?

- La variable no se puede modificar desde el entorno local (excepción global)
- La variable local va ocultar la global

Por esa razón use nombres diferentes
'''
def f(x,y):
  g = x+y
  a = 100 #asignación -- binding (ocultamiento de variable)
  print("El valor de a local",a)
  return g+a+b

print(f(1,2))
print("El valor a global", a)


