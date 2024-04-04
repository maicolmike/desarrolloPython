"""
Listas
Lista = [1, 2, 3, 4, 5]

Puede ser modificada
Cada elemento esta separado por una coma
Puede contener todo tipo de datos
Metodos para listas
Lista.metodo(indice,elemento) o

Lista.metodo(elemento)

Metodos importantes
.count(elemento) cuenta cuantas veces un elemento esta en una lista

.extend(lista) permite extender una lista agregándole los elementos de otra lista

.pop() elimina y retorna el ultimo elemento de la lista

.reverse() reversa el orden de la lista

.sort() ordena la lista de manera ascendente o descendente

Actualizar un valor

Lista = [1, 2, 3, 4, 5]

Lista[0] = -8

Lista = [-8, 2, 3, 4, 5], resultado de la lista luego de actualizar el valor

Agregar un elemento

Lista.append(indice,elemento) o

Lista.append(elemento) en este caso el nuevo elemento se agrega al final de la lista

Eliminar un elemento

Lista.remove(indice, elemento)

"""
num = [1,2,3,4]
print(num)
print(type(num))

task = ['make in mike','play stations']
print(task)

varios = [1, True, 'maicol']
print(varios)

print(num[0])
print(task[0])

task[0] = 'hola mundo'
print(task)

print(num[:3])

print("hola mundo" in task)