def datos_ventas(consolidado_ventas:list)->int:
    consolidado_valor=[] #defino una lista vacia para poder guardar alli el valor de cada codigo
    for codigo in consolidado_ventas:        #recorro la lista enviada a la funcion
        if codigo==100:                      #realizo la verificacion de los codigos en la lista
            consolidado_valor.append(23000)  #agredo a la lista consolidado valor el numero que representa el codigo
        elif codigo==101:
            consolidado_valor.append(42000)
        elif codigo==102:
            consolidado_valor.append(33500) 
            print("102",consolidado_valor)
        elif codigo==103:
            consolidado_valor.append(37200) 
        elif codigo==104:
            consolidado_valor.append(57400) 
        elif codigo==105:
            consolidado_valor.append(83800)
        elif codigo==106:
            consolidado_valor.append(41250)
        elif codigo==107:
            consolidado_valor.append(56400)  
        else:
            print(f"el codigo {codigo} no existe")
            consolidado_valor.append(0)     
    suma = 0     #defino una variable para guardar los valores
    for valor in consolidado_valor: #recorro la lista consolidado_valor
        suma += valor               #en la variable suma, realizo la suma de los valores dentro de la lista
    
    return(f"El valor total de las ventas realizadas durante el día es: ${suma}")
#inicio de aplicacion
consolidado_ventas_dia=[100, 100,100,101,101,106, 107,107,107,100, 101,101, 102,112]
resultado=datos_ventas(consolidado_ventas_dia)
print(resultado)