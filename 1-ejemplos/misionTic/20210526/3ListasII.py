lista1 = [10,20,30,40,50]
lista2 = [10,20,30,40,50]
print(lista1==lista2)

lista3 = [10,20,30,41,50]
print(lista1==lista3)

lista4 = [50,20,30,40,10]
print(lista1==lista4)
print(lista1!=lista4)

print(lista1<lista2)
#[10,20,30,40,50]
lista5=[10,20,30,41,50]
print(lista1<lista5)

print([10,20,30,40,50]<[10,20,30,40,49])

print([10,20,30,40,50]<[10,20,30,41,49])

print([10,20,30,40,50]<[10,20,30,39,51])

lista = [10,20,30,40,50]
lista[2:4]=[11,23]
print(lista)

lista[1:3] = []
print(lista)
#[10, 23, 50]
#[10,23,100,200,300,50]
lista[2:2]=[100,200,300]
print(lista)

