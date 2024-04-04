import math
def estudio_credito(prestamos:list)->list:
    salida = []  #listaque almacenara los diccionarios que se van a crear
    porcentaje_interes = 0
    interes_total=0
    valor_total=0
    valor_cuota=0

    for valor_credito, numero_meses in prestamos:
        dic_ven = {
            "valor_cuota":0,
            "valor_total":0
        }

        if numero_meses >=1 and numero_meses <=12:
            porcentaje_interes=0.035 # 3.5 se lo divide en 100s
            #porcentaje_interes=math.ceil(porcentaje_interes)
        elif numero_meses >12 and numero_meses <=24:
            porcentaje_interes=0.03 # 3
            #porcentaje_interes=math.ceil(porcentaje_interes)
        elif numero_meses >=25 and numero_meses <=36:
            porcentaje_interes= 0.023 #2.3
            #porcentaje_interes=math.ceil(porcentaje_interes)
        elif numero_meses >36 and numero_meses <=60:
            porcentaje_interes= 0.018 #1.8  # 1,8
            #porcentaje_interes=math.ceil(porcentaje_interes)
        elif numero_meses >60:
            porcentaje_interes= 0.01 #1
            #porcentaje_interes=math.ceil(porcentaje_interes)
        else:
            print("EL número de meses no se encuentra en el rango, por favor verifique")           
        #operaciones
        interes_total=(porcentaje_interes*numero_meses)
        valor_total= valor_credito*(1+interes_total)  #calculo del valor total
        valor_cuota= valor_total/numero_meses #calculo del valor de cada cuota
        # utilizare la funcion math.ceil para aproximar el resultado y evitar numeros decimales 
        
        #interes_total=math.ceil(interes_total)
        valor_total=math.ceil(valor_total)
        valor_cuota=math.ceil(valor_cuota)
       # valor_total= round(valor_total,1)
        #agrego al diccionario los valores obtenidos     
        for item in prestamos:
            dic_ven["valor_cuota"]=valor_cuota
            dic_ven["valor_total"]=valor_total
        salida.append(dic_ven)  #agregar a la lista los diccionarios creados
    return salida
# inicio de la aplicacion
print("Calculo 1",estudio_credito([(50000000,24),(50000000,65),(24000000,48)]))
print("Calculo 2",estudio_credito([(10000000,24),(20000000,65),(44000000,48), (50000000,10),(50000000,12),(24000000,18)]))
print("Calculo 3",estudio_credito([(10000000,12),(20000000,31),(44000000,21), (50000000,52),(50000000,18),(24000000,4)]))
print("Calculo 4",estudio_credito([(12000000,33),(20000000,18),(34000000,16), (18000000,22),(10000000,12),(34000000,28)]))