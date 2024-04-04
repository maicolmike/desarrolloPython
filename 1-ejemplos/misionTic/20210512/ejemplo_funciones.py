'''
Autor: Carlos A Delgado
Fecha: 12-Mayo-2021
'''
def imprimir(name,date):
  mensaje = f"El nombre es {name} y la fecha es {date}"

  return mensaje

#imprimir("carlos",12,"juan")

resultado1 = imprimir("carlos","12 de Mayo")
resultado2 = imprimir("maria","31 de diciembre")
nombre = "Pedro"
fecha = "01 de Enero"
resultado3 = imprimir(nombre,fecha)
print(resultado1)
print(resultado2)
print(resultado3)

def f(x):
  return x**2

print(f(1))
print(f(2))
resultado = f(3)
print(resultado)

def funcionMisterio(x,y):
  a = x**2
  b = y**3
  return float(a+b)

print(funcionMisterio(2,3))

def calcular_area_rectangulo(largo,ancho):
  area = largo*ancho
  salida = f"El area es igual a {area}"
  return salida

area1 = calcular_area_rectangulo(10,20)
area2 = calcular_area_rectangulo(100,10)
print(area1,area2)
print(5//3)

def cantidad_vueltas_cierra(c):
  c = a**2
  return squrt(c+c)
  print(cantidad_vueltas_cierra(4))