def es_primo(numero):
    contador=0
    for i in range(1,numero+1):
        if i==1 or i==numero:
            continue
        if numero%i==0:
            contador+=1
    if contador==0:
        return (True)  
    else :
        return (False)          

def run():
    numero=int(input("Escribe un numero:"))
    if es_primo(numero):
        print("El numero ",numero," es primo")
    else :
        print("El numero ",numero," no es primo")    

#run() #llamo a la funcion

if __name__== '__main__':
    run()   