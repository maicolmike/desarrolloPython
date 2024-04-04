if True :
    print("verdadero")
    
if False :
    print("false")

stock = int(input("Digite el stock disponible:"))    
if stock >= 10 and stock <= 100 :
    print("EL stock es correcto")
else :
    print("El stock no esta disponible")
    
    
pet = input("Ingresa cual es tu mascota:")
if pet == "perro":
    print("Tienes una gran mascota")
elif pet == "gato":
    print("tienes un bruno")
elif pet == "conejo":
    print("tienes un bugs bunny")
else :
    print("No tienes ninguna mascota interesante")
    
    
numero = int(input("Ingresa un numero:"))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")