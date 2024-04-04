matriz = [
    [1,2,4],
    [7,8,9],
    [5,6,3]
]

print(matriz[0]) # imprime todo lo de la lista seleccioada
print(matriz[0][1]) # imprime un elemento de la cordenada seleccioanda
print(" ")

#ciclos aninados
for row in matriz:
    print(row)
    for column in row:
        print(column)