lista=[1,2,3,4,5]
tupla=(10,20,30,40,50)
lista2=[100,200,300,400,500]
tupla2=(1000,2000,3000,4000,5000)
print("Lista",lista)
print("Tupla",tupla)
resultado=zip(lista,tupla)
print("Resultado", resultado)
resultado=tuple(resultado)
print("Resultado", resultado)
resultado=zip(tupla,lista)
resultado=tuple(resultado)
print("Resultado", resultado)

resultado=zip(tupla,lista,tupla2,lista2)
resultado=tuple(resultado)
print("Resultado", resultado)

lista=[1,2,3,4,5,6,7]  #cuando hay mas elementos en una lista y en las otras no, el programa no tiene en cuenta esos valores de mas
resultado=zip(tupla,lista,tupla2,lista2)
resultado=list(resultado)
print("Resultado", resultado)