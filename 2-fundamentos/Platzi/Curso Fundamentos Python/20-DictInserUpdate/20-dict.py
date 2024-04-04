person = {
    'name': "maicol" ,
    'last_name': "yela" ,
    'age': 30 ,
    'langs': ['python','go', 'Js'] 
}
print(person)

#Insertar o modificar datos
person['name'] = 'myvmike'
person['age'] -= 2
person ['langs'].append('html')
person['twitter'] = '@nicobytes'
print(person)

# eliminar
del person['last_name'] # hay que enviar la llave sino genera error
person.pop('age') # hay que enviar la llave sino genera error en las listas no sucede este problema
print(person)


# metodos
print("items") # devuelve una tupla con la llave y el valor
print (person.items())

print ("keys")  # devuelve una lista con las llaves que tiene el dicccionario
print (person.keys())

print ("Values") # devuelve una lista con los valores que tiene el dicccionario
print (person.values())