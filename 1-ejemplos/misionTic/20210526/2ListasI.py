'''
Autor: Carlos A Delgado
Fecha: 26-Mayo-2021
'''
#Append
elementos = list() #[]
print(elementos)
elementos.append(2)
print(elementos)
a = elementos.append(4) #No se debe de hacer
print(a)
print(elementos)
help(list.append)
#Extend
listaA = [1,2,3]
listaB = [2,3,4]
listaA.extend(listaB) #Modifica listaA agregandole listaB
print(listaA)
listaA = [1,2,3]
listaB = [2,3,4]
listaC = listaA+listaB #Retorna la list combinada
print(listaC)
#Rebanadas
listaF = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

print(listaF[0:3])
print(listaF[1:4])

print(listaF[:5])
print(listaF[4:])

print(listaF[100:])

listaF.sort()
print(listaF)

listaG = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
listaF.sort(reverse=True)
print(listaF)

listaC = [0,1,2,3]
print(listaC[3:])

listaC[0] = 10
print(listaC)