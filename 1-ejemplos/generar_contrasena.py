import random
def generar_contrasena():
    mayuscula = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minuscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numero = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    caracteres= mayuscula+minuscula+numero+simbolos
    contrasena=[]
    for i in range(15):
        caracter_random= random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena="".join(contrasena)   #convierto a string una nueva forma
    #contrasena=str(contrasena)  #se convierte a string pero queda de una forma no tan llamativa
    return (contrasena)

def run ():
    contrasena = generar_contrasena()
    print("Utilize la siguiente contrasea aleatoria: "+generar_contrasena())


if __name__=="__main__":
    run()