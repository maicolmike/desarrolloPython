"""
Tuplas
Estructura de datos inmutables que contiene una secuencia ordenada de elementos

Tupla = (1, 2, 3, 4)

Los elementos están separados por espacios luego de las comas
Puede contener cualquier tipo de datos
Cada posición de la tupla tiene un índice
Es inmutable y por lo tanto no puede ser modificada, lo que permite proteger mejor la data si no queremos que se modifique por error
Acceder a un elemento
Tupla = (”A”, “B”, “C”)

Tupla [0] Indice a consultar

“A” Nos retorna el resultado de la posición 0 en la tupla

Encontrar un elemento
Tupla = (”A”, “B”, “C”)

“A” in Tupla

True

“Z” in Tupla

False

Metodos
Buscar el Indice de un elemento

Tupla = (”A”, “B”, “C”)

Tupla.index(”A”)

0 Nos devuelve el indice del elemento que buscamos

Numero de veces que un elemento aparece en la Tupla

Tupla = (”A”, “B”, “C”)

Tupla.count(elemento)

Tupla.count(”B”)

1 Retorna el numero de veces del elemento en la Tupla

"""
num = (1,2,6,5)
strings = ("h","hola", "hola")
print(num)
print(type(num)) 
print(num[0]) # se accede igual que en las listas

# recordar que no se pueden agregar mas cosas a las tuplas esa es una diferencia con las listas
# tampoco se puede modificar elementos

print(strings)
print(type(strings)) 
print(strings.index("hola"))  # buscar la posicion de un elemento
print(strings.count("hola")) # ver cuantas veces se repite un elemento

#convertir la tupla a lista
my_list = list(strings)
print(my_list)
print(type(my_list))
my_list[0]= "Maicol" # como ya es una lista puedo modificar algo
print(my_list)

#convertir la lista a tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))