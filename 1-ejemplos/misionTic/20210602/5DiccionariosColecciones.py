"""
Autor: Carlos A Delgado
Fecha: 02 de Junio de 2021
"""
diccionario = {"nombre":"Carlos","edad":33}
diccionario["ciudad"] = "Palmira"

print(diccionario)

for llave in diccionario:
    print(llave, diccionario[llave])

for llave, valor in diccionario.items():
    print(llave,valor)

diccionarioB={"nombres":["Carlos","Ana","Pedro"],
              "apellidos":["Delgado","Suarez","Ramirez"],
              "edades":[33,19,23]}

for llave,valor in diccionarioB.items():
    for elm in valor:
        print(elm)


diccionarioC = {"palmira":{"departamento":"valle",
                           "poblacion": 350000,
                           "num_museos":3},
                "manizales":{"departamento":"caldas",
                             "poblacion":434403,
                             "num_museos":4},
                "bogota":{"departamento":"bogota",
                          "poblacion":8500000,
                          "num_museos":20}
                }

for llave, valor in diccionarioC.items():
    print(f"Ciudad {llave}")
    for llave2, valor2 in valor.items():
        print(f" {llave2} : {valor2}")























