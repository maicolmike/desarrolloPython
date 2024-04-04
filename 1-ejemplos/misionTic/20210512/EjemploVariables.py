a = 9
print(a)
print(type(a))

a = "Hola mundo"
print(a,type(a))

a = 1
print(type(a))
b = 10.4
print(type(b))
c = "hola"
print(type(c))
d = False
print(type(d))

aux = 0
for i in range(0,4):
  aux+=1
print(aux)

arreglo = ["Hola","Maria","Juan"]
aux = arreglo[0]
arreglo[0]=arreglo[1]
arreglo[1]=aux
print(arreglo)

a= 5
c= 7
d= 30
print (d-(c+a))
