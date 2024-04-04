"""
Autor: Carlos A Delgado
Fecha: 31 de Mayo de 2021
""" 
#https://docs.python.org/es/3/library/collections.html#collections.namedtuple
from collections import namedtuple

Circulo = namedtuple('Circulo','x y radio color')

circulo_A = Circulo(4,2,3,"Rojo")
circulo_B = Circulo(3,2,3,"Verde")
print(circulo_A)
print(circulo_B)

print(circulo_A.x)
print(circulo_B.color)

'''
Esto permite usar nombres dentro de tuplas para extraer más facilmente
'''
Persona = namedtuple("Persona","nombre edad color_pelo email")

personaA = Persona("Carlos", 18,"Negro","carlos@gmail.com")
personaB = Persona("Juan",22,"Rojo","Juan@gmail.com")
personaC = Persona("Maria",34,"Amarillo","maria@presidencia.gov.co")

print(personaA)
print(personaA.nombre)
print(personaB.edad)
print(personaC.email)
