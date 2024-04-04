def registrarPersona(n):
    person={"Nombre":'',"Edad":'',"Peso":''}
    for key in person:
        person[key]=input(f"Persona {n+1} digite su {key}:")
    
    return person

lista=[]
for i in range(3):
    lista.append(registrarPersona(i))
    
for i in lista:
    print(i)