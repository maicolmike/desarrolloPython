"""
Autor: Carlos A Delgado
Fecha: 14 de Mayo de 2021
Este es un ejemplo de clase para los chicos del mintic G65 Caldas

algoritmo calcular_salario
variables
	salario_base, ibc, salud, pension, total_aportes: float
	aporte_empleador, aporte_trabajador, salario_neto:
		float
inicio
	ibc = salario*0.4
	salud = ibc*0.125
	pension = ibc*0.16
	total_aportes = salud+pension
	aporte_empleador = 0.6*total_aportes
	aporte_trabajador = 0.4*total_aportes
	salario_neto = salario_base - aporte_trabajador
	returnar salario_neto
fin
"""
def calcular_salario(salario_base):
  '''
  salario_base: float que indica el salario base de un trabajador

  retorna str que es el salario neto a pagar al trabajador después de los descuentos
  '''
  ibc = 0.4*salario_base
  
  #Deducciones
  salud = ibc*0.125
  pension = ibc*0.16
  total = salud + pension

  #Repatir entre empleador y trabajador
  aporte_empleador = 0.6*total
  aporte_trabajador = 0.4*total

  #Calculamos el salario final
  salario_neto = salario_base - aporte_trabajador

  return f"El trabajador tiene salario base de ${salario_base}, los descuentos son ${total}, el empleador paga ${aporte_empleador} y el trabajador paga ${aporte_trabajador} y el salario neto que recibe es ${salario_neto}"

salarioTrabajadorA = calcular_salario(1000000)

salarioTrabajadorB = calcular_salario(2000000)

print(salarioTrabajadorA)
print(salarioTrabajadorB)

#Aplicar formato
print("El salario es %.3f" % 1000.2)

mensaje_salto_linea = "Hola\nMundo"
mensaje_tabulacion = "Hola\tMundd"
otraForma = 'Hola\tmundo'

