import random # modulo para hacer aleatorio una seleccion


options = ("piedra","papel","tijera")

user= input("Usuario Elige entre piedra, papel o tijera: ")
user = user.lower() # lo que elija el usuario se volvera minusculas
computer = random.choice(options) # selecciono aleatoriament algo de la tupla

# mensaje diciendo que no se esta eligiendo una opcion de la tupla
if not user in options:
    print ("Opcion no es valida")

print("EL usuario eligio:", user)
print("La computadora eligio:", computer)

if user == computer:
    print ("Hubo empate")
elif user == "piedra":
    if computer == "tijera":
        print("Piedra gana a tijera")
        print ("Usuario gano")
    else :
        print("Papel gana a piedra")
        print ("Computadora gana")   
elif user == "papel":
    if computer == "piedra":
        print("Papel gana a piedra")
        print ("Usuario gano")
    else :
        print("Tijera gana a papel")
        print ("Computadora gana")   
elif user == "tijera":
    if computer == "papel":
        print("Tijera gana a papel")
        print ("Usuario gano")
    else :
        print("Piedra gana a tijera")
        print ("Computadora gana")   