for element in range(20):
    print ("Primera lista",element)

for element in range(1,20):
    print ("2da lista",element)

lista=[1,4,2,9,3]
for element2 in lista:
    print ("3da lista",element2)

product = {
    'name': 'Moto',
    'price': 200
}

for element3 in product:
    print("ELment3",element3)

for key in product:
    print("ELment3b",product[key])

for key in product:
    print(key, "=" ,product[key])

for key, value in product.items():
    print(key, "=" , value)

people = [
    {
        'name': 'John',
        'apellidos': 'yela',
        'edad': 23
    },
    {
        'name': 'myv',
        'apellidos': 'lopez',
        'edad': 43
    },
    {
        'name': 'wilmer',
        'apellidos': 'perez',
        'edad': 73
    }
]

for person in people:
    print(person)

for person in people:
    print("Nombre: ",person['name'])