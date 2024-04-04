n_m=int(input("digite su numero de documento: "))
while n_m !=0:  #mientras la variable n_m sea diferente de 0, el programa se ejecutara
    nombre=input("digite su nombre: ")
    n_t=int(input("digite su numero de telefono: "))
    id_service=(input("digite su identidicador de servicio: "))
    if id_service=="100A" or id_service=="101A" or id_service=="102A" or id_service=="103A":
        cilindraje="menos de 100"
        if id_service=="100A":
         tipo_mantenimiento="Inspeccion"
         valor_servicio=30000
         valor_descuento=0.05
         total=valor_servicio-(valor_servicio*valor_descuento)
        elif id_service=="101A":
         tipo_mantenimiento="Lubricacion"
         valor_servicio=40000
         valor_descuento=0.1
         total=valor_servicio-(valor_servicio*valor_descuento)
        elif id_service=="102A":
         tipo_mantenimiento="Ajuste motor"
         valor_servicio=120000
         valor_descuento=0.12
         total=valor_servicio-(valor_servicio*valor_descuento)
        elif id_service=="103A":
         tipo_mantenimiento="Combo"
         valor_servicio=160000
         valor_descuento=0.15 
         total=valor_servicio-(valor_servicio*valor_descuento) 
    elif id_service=="100B" or id_service=="101B" or id_service=="102B" or id_service=="103B": 
        cilindraje="100 a 200" 
        if id_service=="100B":
         tipo_mantenimiento="Inspeccion"
         valor_servicio=32000
         valor_descuento=0.05 
         total=valor_servicio-(valor_servicio*valor_descuento)
        elif id_service=="101B":
         tipo_mantenimiento="Lubricacion"
         valor_servicio=40000
         valor_descuento=0.1
         total=valor_servicio-(valor_servicio*valor_descuento)
        elif id_service=="102B":
         tipo_mantenimiento="Ajuste motor"
         valor_servicio=180000
         valor_descuento=0.12
         total=valor_servicio-(valor_servicio*valor_descuento)
        elif id_service=="103B":
         tipo_mantenimiento="Combo"
         valor_servicio=210000
         valor_descuento=0.15
         total=valor_servicio-(valor_servicio*valor_descuento)
    elif id_service=="100C" or id_service=="101C" or id_service=="102C" or id_service=="103C": 
        cilindraje="200 o mas" 
        if id_service=="100C":
         tipo_mantenimiento="Inspeccion"
         valor_servicio=42000
         valor_descuento=0.05
         total=valor_servicio-(valor_servicio*valor_descuento)
        elif id_service=="101C":
         tipo_mantenimiento="Lubricacion"
         valor_servicio=60000
         valor_descuento=0.1
         total=valor_servicio-(valor_servicio*valor_descuento)
        elif id_service=="102C":
         tipo_mantenimiento="Ajuste motor"
         valor_servicio=210000
         valor_descuento=0.12
         total=valor_servicio-(valor_servicio*valor_descuento)
        elif id_service=="103C":
         tipo_mantenimiento="Combo"
         valor_servicio=290000
         valor_descuento=0.15
         total=valor_servicio-(valor_servicio*valor_descuento)      
    else:
        print("----------------------------------")
        print("Numero invalido, intente de nuevo")
        print("----------------------------------")
        cilindraje="No se puede calcular" 
        tipo_mantenimiento="No se puede calcular"
        valor_servicio="No se puede calcular"
        valor_descuento="No se puede calcular"
        total="No se puede calcular"
    print("*********************************")
    print("El documento del usuario es:",n_m)
    print("El nombre del usuario es:",nombre)
    print("El numero de telefono del usuario es:",n_t)
    print("Su cilindraje es de:",cilindraje)
    print("El tipo de mantenimiento es:",tipo_mantenimiento)
    print("El valor del servicio es:",valor_servicio)
    print("El porcetanje de descuento aplicado es:",valor_descuento)
    print("El valor total a pagar es:",total)
    print("*********************************")
    print("______________________________________")
    print("Digite los datos del siguiente usuario")
    print("______________________________________")

    n_m=int(input("digite su numero de documento: "))
print("*------------------------------*")
print("fin de ejecucion del programa")
print("*------------------------------*")

