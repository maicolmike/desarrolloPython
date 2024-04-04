palabra="hola mundo como estas"
print("cadena de string:",palabra)
palabra_dividida=palabra.split() #convierte un string en lista utilizando los espacios
print("se convierte en una lista",palabra_dividida) 

palabra="hola-mundo-como-estas"
palabra_dividida=palabra.split("-") #convierte un string en lista utilizando un caracter -
print("se convierte en una lista",palabra_dividida) 

palabra="hola-mundo-como-estas-tu-don"
palabra_dividida=palabra.split("-",2) #convierte un string en lista utilizando un caracter y solo los dos primeros valores-
print("se convierte en una lista",palabra_dividida) 


palabra=["hola", "mundo", "como", "estas", "tu", "don"]
print("lista",palabra)
palabra_nueva=" ".join(palabra)
print("el string es:",palabra_nueva)
print(type(palabra_nueva))

nombre="maicol"
apellido="yela"
nombre_completo=nombre+" "+apellido
print("1ra forma Mi nombre es", nombre_completo)

palabra="hola como hola estas hi"
busqueda=palabra.count("hola")
print("hay: ",busqueda, "palabras")
print("hola"in palabra)