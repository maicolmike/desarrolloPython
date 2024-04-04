import random

def run():
    numero_aleatorio=random.randint(1,100)
    numero_elegido=int(input("Escribe un numero de 1 a 100: "))
    vidas = 5
    while numero_aleatorio != numero_elegido :
        if numero_aleatorio < numero_elegido :
           print("Elige un numero mas pequeño.") 
        else: 
            print("Elige un numero mas grande.")
            vidas -= 1
        numero_elegido = int(input("Escribe un nuevo numero: "))
    print("FELICIDADES GANASTE") 
        
if __name__=="__main__":
    run()