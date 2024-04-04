def datos_ventas(consolidado_ventas:list)->int:
  suma=0
  dict_ventas={100:23000,101:42000,102:33500,103:37200,104:57400,105:83800,106:41250} #creo el diccionario
  dict_ventas[107]=56400 #envio un indice mas al diccionario
  for codigo in consolidado_ventas:    
    if codigo==100:
      suma += dict_ventas[100]
    elif codigo==101:
      suma += dict_ventas[101]
    elif codigo==102:
      suma += dict_ventas[102]
    elif codigo==103:
      suma += dict_ventas[103]
    elif codigo==104:
      suma += dict_ventas[104]
    elif codigo==105:
      suma += dict_ventas[105]
    elif codigo==106:
      suma += dict_ventas[106] 
    elif codigo==107:
      suma += dict_ventas[107]
    else:
        print(f"el codigo {codigo} no existe")

  return f"El valor total de las ventas realizadas durante el día es: ${suma}"
 #inicio aplicacion
consolidado_ventas_dia=[100, 100,100,101,101,106, 107,107,107,100, 101,101, 102,112]
resultado=datos_ventas(consolidado_ventas_dia)
print(resultado)