mi_lista = [[1,2,3],["a","b"],[4,6,8]]
print(mi_lista)

print(mi_lista[0])
print(mi_lista[1])
print(mi_lista[2])

print(mi_lista[0][0])
print(mi_lista[0][1])
print(mi_lista[0][2])

print(mi_lista[2][1])

mi_listaB = [[1,2,3],[4,5,6],[7,8,9]]

print(mi_listaB[0])
print(mi_listaB[1])
print(mi_listaB[2])

print(mi_listaB[2][1])
print(mi_listaB)
mi_listaB[2][1] = 100
print(mi_listaB)

mi_listaB[1].append(3)
print(mi_listaB)