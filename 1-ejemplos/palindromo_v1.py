def palindromo(palabra):
    palabra= palabra.replace(" ","") #funcion para remplazar eliminar los espacios
    palabra= palabra.lower()         #funcion para convertir todo en minusculas
    palabra_invertida= palabra[::-1] #utilizamos el slide para invertir toda la cadena de strings
    if palabra==palabra_invertida:
        return (True)
    else :
        return (False)    

def inicio():
    palabra=input("Escribe una palabra: ")
    es_palindomo= palindromo(palabra)
    if es_palindomo==True:
        print("La palabra "+palabra+" es palindroma")
    else :
        print("La palabra "+palabra+" no es palindroma")

if __name__=="__main__":
    inicio()