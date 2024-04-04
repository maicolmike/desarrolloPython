def run ():
    listado_habitantes_paises={
        "argentina": 42000,
        "colombia": 25000,
        "brazil": 40000
    }
    print("Elementos de un diccionario:",listado_habitantes_paises) 
    print("Longuitud del diccionario:",len(listado_habitantes_paises)) 
    print("Verificar si una llave existe:", "peru" in listado_habitantes_paises) #devuelve true si existe o false si no existe
    print("Prueba de como imprimir el valor de una llave:",listado_habitantes_paises["argentina"]) #asi se imprime cada llave del diccionario
    print("Imprimir el valor de una llave que no existe sin que tenga error:",listado_habitantes_paises.get("peru")) #sino encuentra el indice devuelve none que significa ausencia de datos
    print("Imprimir el valor de una llave que no existe y dejar un mensaje:",listado_habitantes_paises.get("peru","La llave no existe"))
    print("imprimir el valor de una llave sino existe la llave la agrega con su respectivo valor:",listado_habitantes_paises.setdefault("peru",4050))
    print("Diccionario:",listado_habitantes_paises)
    for llave in listado_habitantes_paises.keys():  #asi se imprime las llaves
        print("Prueba de como imprimir llaves: ",llave)
    for valor in listado_habitantes_paises.values(): #asi se imprime los valores de la llave
        print("Prueba de como imprimir los valores de las llaves: ",valor)
    for llave,valor in listado_habitantes_paises.items():
        print("Prueba de como imprimir la llave ",llave," y el valor: ",valor)   
    
    del listado_habitantes_paises["argentina"]
    print("Eliminar datos de una llave, 1ra forma",listado_habitantes_paises)
    listado_habitantes_paises.pop("colombia")
    print("Eliminar datos de una llave, 2da forma",listado_habitantes_paises)

    listado_habitantes_paises.clear()
    print("Eliminar todos los datos del diccionario",listado_habitantes_paises)

if __name__=="__main__":
    run()