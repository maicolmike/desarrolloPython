user= input("Usuario Elige entre piedra, papel o tijera: ")
computer = input("Computadora Elige entre piedra, papel o tijera: ")

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