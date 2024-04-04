text = 'futbol baloncesto voly'
#imprime el caracter dependiendo de su posicion recordando que en sistemas la mayoria de veces empieza en 0
print("Primer digito ",text[0])
print(text[3])

tamano = len(text)
print("Ultimo digito 1ra forma ",text[tamano - 1])
print("Ultimo digito 2da forma ",text[- 1])

# slicing sacar subtexto quee esta en ese rango
print(text[0:6])
print(text[3:6])
print(text[:6]) #sino se digita el primer valor el lo toma como predeterminado el 0
print(text[3:-1])
print(text[3:]) #sino se digita el ultimo valor el lo toma como predeterminado el final de la cadena
print(text[:]) #imprimir todo el texto
print(text[0:6:1]) #de ese rango hacer saltos 1
print(text[0:6:2]) #de ese rango hacer saltos 2
print(text[::2]) #de ese rango hacer saltos 2