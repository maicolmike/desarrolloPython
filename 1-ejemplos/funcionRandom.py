import random
import string

digitos = string.digits # digitos
print(digitos)

minusculas = string.ascii_lowercase # letras minusculas
print(minusculas)

mayusculas = string.ascii_uppercase # letras mayusculas
print(mayusculas)

letras = string.ascii_letters # letras minusculas y mayusculas
print(letras)

hexa = string.hexdigits # valores hexagecimales
print(hexa)

octa = string.octdigits # valores octagecimales
print(octa)

combinadas = string.printable # numeros letras minusculas letras mayusculas caracteres especiales
print(combinadas)

caracteresEspeciales = string.punctuation # caracteres especiales
print(caracteresEspeciales)

espacio = string.whitespace # espacios
print(espacio)

cadenaModificada = string.digits + string.ascii_letters + "*#$&!?"
print(cadenaModificada)

# proceso para seleccionar una cadena aleatoria
cadena = "" 
for _ in range(6):
    cadena += random.SystemRandom().choice(combinadas)
print(cadena)