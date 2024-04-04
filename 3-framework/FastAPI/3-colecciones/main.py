from typing import List
from typing import Tuple
from typing import Union
from typing import Dict

# Listas
calificaciones: List[int] = [1,2,3,4,5]

def promedio(calificaciones: List[int]) -> float:
    return sum(calificaciones)/ len (calificaciones)


print ("EL promedio de la lista es: ", promedio(calificaciones))

#tuplas
configuraciones: Tuple[str] = ('localhost','3306','root')
print ("Listado de tuplas",configuraciones)


#union
onfiguraciones: Tuple[Union[str,str,bool,int]] = ('root','local',3306, True)
print ("Listaado Union tuplas ",configuraciones)

# diccionario
usuarios: Dict [str, int ] = {
    'maicol': 10,
    'cody': 10
} 

print("Ejemplo diccionario",usuarios)