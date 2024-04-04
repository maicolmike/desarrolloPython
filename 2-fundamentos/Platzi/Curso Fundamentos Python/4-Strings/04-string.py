name= "maicol"
last_name = "Yela"
edad = 30

# concatenando
nom_completo = name + ' ' + last_name
nom_completo2 = name + " " + last_name
print (nom_completo)
print (nom_completo2)

#colocando comillas en comillas dobles y poniendo comillas dobles en comillas
cuota= "I'm Maicol"
cuota2= 'She said "Mike"'
print (cuota)
print (cuota2)

#format
plantilla = "Hola, mi nombres es "+ name + " y mi apellido es "+ last_name
print ("V1",plantilla)
plantilla = "Hola, mi nombres es {} y mi apellido es {}".format(name, last_name)
print ("V2",plantilla)
plantilla = f"Hola, mi nombres es {name} y mi apellido es {last_name}"
print ("V3",plantilla)

# reto 3 variables
plantilla = f"Hola, mi nombres es {name} y mi apellido es {last_name} y mi edad es {edad}"
print ("Reto",plantilla)