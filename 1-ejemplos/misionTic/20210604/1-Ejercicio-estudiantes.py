"""
Autor: Carlos A Delgado
Fecha: 4 de Junio de 2021

En la universidad de caldas, desean un aplicativo para calcular la nota final de los
tripulantes (estudiantes) del programa de programación del MinTIC.

La universidad cuenta con la información del nombre de la cedula del estudiante y
las notas de los retos 1,2,3,4,5 y la nota de inglés, cuya poderación es 10%,10%,
20%,20%, 20%, 20%.  Función: notas_mintic(notas_estudiantes:dict)->dict:

Se desea calcular nota definitiva de un estudiante redondeada a 2 decimales y
sabe SI aprueba o NO aprueba, si la nota es >= 3.0
{
   112312: [5, 4.5, 3.8, 5, 5, 4],
   123123: [2, 0, 1, 3, 4, 2]
}
Salida
{
	112312: {"nota_final": 4.51  , "aprobo":"SI"},
	123123: {"nota_final": 2.2  , "aprobo":"NO"}
}
"""

def notas_mintic(notas_estudiantes:dict)->dict:
	"""
	notas_estudiante es un diccionario cuyas claves son los cédulas de los estudiantes y contien un diccionario con las 6 notas del ciclo I

	Retorna un diccionario que tiene como llave la cédula del estudiante, e internamente tiene un diccionario que tiene la nota final y si aprobó o no el curso (para aprobar nota_final >= 3.0)
	"""
	salida = {}
	porcentajes = [0.1,0.1,0.2,0.2,0.2,0.2]

	for clave,notas in notas_estudiantes.items():
		nota_final = 0

		for i in range(0,len(notas)):
			nota_final+=notas[i]*porcentajes[i]

		aprobo = ""

		if nota_final >= 3.0:
			aprobo = "SI"
		else:
			aprobo = "NO"

		resultado_estudiante = {
			"nota_final":round(nota_final,2),
			"aprobo":aprobo
		}

		salida[clave] = resultado_estudiante


	return salida

print(notas_mintic({
   112312: [5, 4.5, 3.8, 5, 5, 4],
   123123: [2, 0, 1, 3, 4, 2]
}))
"""
{
	112312: {"nota_final": 3.79  , "aprobo":"SI"},
	123123: {"nota_final": 2.2  , "aprobo":"NO"}
}
"""
print(notas_mintic({
	112312: [5, 4.5, 3.8, 5, 5, 4],
	123123: [2, 0, 1, 3, 4, 2],
	23123: [2, 4, 4.1, 3.8, 4, 2.7],
	123122: [2, 3.2, 1, 3, 4, 2.7],
	123124: [3.2, 4.1, 1, 3, 4, 2],
	123100: [4, 5, 1.5, 3.5, 4, 2]
}))