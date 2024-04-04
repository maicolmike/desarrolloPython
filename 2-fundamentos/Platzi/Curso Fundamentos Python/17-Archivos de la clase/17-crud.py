"""
Métodos de las listas

    append(): Añade un ítem al final de la lista.
    clear(): Vacía todos los ítems de una lista.
    extend(): Une una lista a otra.
    count(): Cuenta el número de veces que aparece un ítem.
    index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
    insert(): Agrega un ítem a la lista en un índice específico.
    pop(): Extrae un ítem de la lista y lo borra.
    remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
    reverse(): Le da la vuelta a la lista actual.
    sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
"""

# CRUD = CREATE READ UPDATE DELETE
numbers = [1,2,3,4,5] #create
print(numbers)  # read
print(numbers[1])  # read
numbers[-1]= 10  # update 
print(numbers)

numbers.append(11) # create agrega al final de la lista por defecto
print(numbers)

# al insertar se agrega un espacio y se corren los otros datos de la lista
numbers.insert(0,"hola") # insertar una campo en la posicion que elijamos
print(numbers)

numbers.insert(5,5)
print(numbers)

#fusionar listas
task = ["h", "m"]
new_list = numbers + task
print(new_list)

# saber la posicion de un elemento
posicion = new_list.index("h")
print(posicion)
new_list[posicion]= "MM"
print(new_list)

# eliminar elementos de la lista
new_list.remove("m")
print(new_list)

new_list.pop() # elimina por defecto el ultimo elemento de una lista en especifico
print(new_list)

new_list.pop(2) # elimino segun la posicion que le indique
print(new_list)

#CAMBIAR EL ORDEN DE LA LISTA
new_list.reverse()
print(new_list)

# ordenar lista
num = [1,4,2,9,1]
print(num)
num.sort()
print(num)

strin = ["r", "z", "b", "h"]
print(strin)
strin.sort()
print(strin)

# si se tiene diferente tipos de datos en la lista no se puede ordenar