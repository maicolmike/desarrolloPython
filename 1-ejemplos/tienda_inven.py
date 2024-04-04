dict_inventario={
        "01":{"nombre":"pollo", "disponibilidad":4, "valor":10000},
        "02":{"nombre":"chocorramo", "disponibilidad":100, "valor":2000}
    }

def ventas(consolidado_ventas:list)->float:
    venta = {}
    total = 0.0
    #cuento cuantos codigo hay, y los asisno a una lista
    for i in consolidado_ventas:
        if venta.get(i)!=None: # si el codigo esta
            venta[i]+=1  #va aunmentando la cantidad de codigos que encuentre y los agrega al diccionario venta
            #print(venta)
        else:
            venta[i]=1
    for codigo,num_unidades in venta.items(): #por cada elemento se hara el recorrido, 
        #print("num unidades",codigo,num_unidades)
        if dict_inventario.get(codigo)!=None: # si el codigo esta
            if dict_inventario[codigo]["disponibilidad"]>=num_unidades:
                total += num_unidades*dict_inventario[codigo]["valor"]
            else:
                print(f"El producto {codigo} tiene disponible únicamente {dict_inventario[codigo]['disponibilidad']} y por ello se no puede vender {num_unidades}")
                return 0.0
        else:
            print(f"El producto {codigo} no está disponible")
            return 0.0        
#Actualizo el inventario
    for codigo,num_unidades in venta.items():
        dict_inventario[codigo]["disponibilidad"]-=num_unidades
    
    return total

def agregar_inventario():
    num_elementos = int(input("Ingrese el numero total de productos que va a ingresar"))
    for i in range(0,num_elementos):
        codigo = int(input("Ingrese el código del producto"))
        num_unidades = int(input("Ingrese el número unidades disponibles"))
        if dict_inventario.get(codigo)!=None:
            dict_inventario[codigo]["disponibilidad"]+=num_unidades
        else:
            nombre = input("Ingres el nombre producto ")
            valor =float(input("Ingrese el valor del producto "))
            producto = {
				"nombre":nombre,
				"disponibilidad":num_unidades,
				"valor":valor
			}
            dict_inventario[codigo]=producto


#inicio de la aplicacion

consolidado_ventas_dia=["01","01","01","02","02"]
resultado=ventas(consolidado_ventas_dia)
print(resultado)
print(dict_inventario)

agregar_inventario()
print(dict_inventario)