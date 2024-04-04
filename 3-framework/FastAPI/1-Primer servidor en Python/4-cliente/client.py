from urllib import request

URL = 'http://localhost:8000/'

response = request.urlopen(URL)


print("Sin propiedades", response)

#para mostrar propiedades
print("Con propiedades", response.__dict__)

#imprimir en consola la respueta del servidor lo muestra en arreglo de bites
print("Respueta servidor", response.read())