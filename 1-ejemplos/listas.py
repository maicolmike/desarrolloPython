lista=[9,3,2,8,6,7,4,1,5,10]
lista2=[50,30,40]
print("lista inicial",lista)
print("lista inicial 2",lista2)
lista[9]=30 #asi se actualiza un elemento de la lista
print("se actualizo un elemento de la lista",lista)
lista.append(20) #agregar elementos a la lista los ubica de ultimos
lista.append(11)
print("se añadieron elementos nuevos a la lista",lista)
lista.insert(1, 30) # agregare un elemento a la lista en el indice 1
print("se añadieron un elementos nuevo en el indice[1] a la lista",lista)
lista.extend(lista2)
print("a la lista original le añadimos la lista 2",lista)
lista.remove(40)
print("Eliminaremos el numero 30 de la lista",lista) #si hay 2 valores iguales solo elimina el primero que encuentre
del lista[0]
print("Eliminamos el elemento de la posicio [0]",lista)

print("Longuitud de la lista ",len(lista))
print("impresion del un elemento de la lista indice [0]",lista[0]) #imprimo el primer elemento de la lista
print("Lista invertida",lista[::-1]) #utilizamos el slide para invertir toda la lista,si le quito el -1 imrpime todo normal
lista.sort() #ordenar la lista de menor a mayor
print("Lista organizada de menor a mayor",lista)
print("Elemento menor de la lista",lista[0]) 
print("Elemento mayor de la lista",lista[-1]) 
print("Elemento menor de la lista con funcion",min(lista)) 
print("Elemento mayor de la lista con funcion",max(lista)) 
print("El elemento 5 esta dentro de la lista:",5 in lista) #saber si un elemento esta dentro de la lista, devolvera true si es verdadero
print("El elemento 5 no esta dentro de la lista:",5 not in lista)
print("El elemento 5 en que indice esta:",lista.index(5)) #si hay varios elementos solo toma el primero que encuentre

lista.sort(reverse=True) #los organiza de mayor a menor
print("Lista organizada de mayor a menor",lista)
sub_lista= lista[0:6] #asi se crea una sub lista
print("cree una sub lista",sub_lista)
sub_lista= lista[0:6:2] #creo una sub lista omitiendo de 2 en 2
print("cree una sub lista omitiendo de 2",sub_lista)
lista.clear()
print("Eliminamos todos los elementos de la lista",lista)

lista3=[4,10,30]
print("Lista 3",lista3)
lista3_tupla=tuple(lista3)
print("Lista 3 convertida a tupla",lista3_tupla)
print("Lista 3 de tipo ",type(lista3_tupla))

ejem_tupla=(2,5,6)
print("Valores de la tupla",ejem_tupla)
ejem_tupla_lista= list(ejem_tupla)
print("ejem_tupla convertida a lista",ejem_tupla_lista)