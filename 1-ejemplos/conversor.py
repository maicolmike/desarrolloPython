def conversor_dolares(moneda,pesos):
    result=""
    valor_dolar=3875
    if moneda==1:
        dolar=pesos/valor_dolar
        dolar=round(dolar,2)
        dolar=str(dolar) #convierto el valor de dolar que es un float a un str para imprimirlo
        result="El valor es: $"+dolar+" dolares"
    elif moneda==2:
        dolar=pesos*valor_dolar
        #dolar=round(dolar,0)
        dolar=int(dolar)
        dolar=str(dolar) #convierto el valor de dolar que es un float a un str para imprimirlo
        result="El valor es: $"+dolar+" pesos"

    return (result)
#inicio de aplicacion
moneda=int(input("""Ingrese el numero de la conversion que desea hacer:
1) convertir de pesos a dolares
2) convertir de dolares a pesos
selecciona:"""))
pesos=input("Ingrega el valor a calcular: ")
pesos=float(pesos) #el valor de la variable pesos es un str, por eso la convierto en un float
#print(type(pesos)) una pequeña prueba para saber que tipo de datos es la variable
resultado=conversor_dolares(moneda,pesos)
print(resultado)