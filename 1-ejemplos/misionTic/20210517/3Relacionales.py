'''
Autor: Carlos A Delgado
Fecha: 17 de Mayo del 2021
Es un archivo de ejemplo de las expresiones relacionales
'''

x = 10
y = 4

print(x>=y) #True
print(x!=y) #True
print(x==y) #False
#Operador not
relacion1 = x>=y
print(not(relacion1))
relacion2 = not(x!=y)
print(relacion2)
relacion3 = x>=7
print(not(relacion3))

'''
x = 10, y = 4
'''
print("Ejercicios")
print(x>=10 or x<=20) #True
print(x!=4 or not(x==y)) #True
print(x>=7 or not(x!=4 and x<=10)) #True
#
print(True and (True or not(True)))

'''
Otros lenguajes
|| = or
&& = and
! = negacion

5>=x || y <= x
!(x>=3)

En Python solo funciona or,and,not

Advertencia no usar input en los retos porque son pruebas automáticas

Respetar los nombres de las funciones
'''
edad = int(input("Ingrese la edad "))
if edad >= 18:
  print("Es mayor de edad")
else:
  print("Es menor de edad")







