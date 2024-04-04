lives= 3
print ("Tipo de dato",type(lives))
age= 12
budget = 100

temperature = 12.12
print ("Tipo de dato",type(temperature))

lives = lives + 27
print(lives)
lives = lives -1
print(lives)
lives -= 1
print(lives)
lives -= 8
print(lives)
lives += 5
print(lives)

number = 4500000000000000000000000.1
print(number)
number = 0.0000000000000000000000001
print(number)

# el input el valor me lo toma como string lo que hago con int es que me convierta el valor a numero
sueldo_enero = int(input("Digite el valor del sueldo: "))
sueldo_febrero = int(input("Digite el valor del sueldo: "))
sueldo_marzo = int(input("Digite el valor del sueldo: "))
sueldo_promedio= (sueldo_enero + sueldo_febrero + sueldo_marzo)/3
print("V1 El sueldo promedio es",sueldo_promedio)
print(f"V2 El sueldo promedio es {sueldo_promedio}")