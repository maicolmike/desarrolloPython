class Usuario:

    def __init__(self,nombre): # metodo constructor
        self.nombre = nombre
    
    def saludar (self, saludo):
        print (saludo + self.nombre + " desde el metodo padre")
        
class Empleado(Usuario): # heredando de la clase usuario
    salario = 0
    
    def modificar_salario(self, salario):
        self.salario = salario
        
    def ver_salario(self):
        print ("El salario es: ", self.salario)
        
    def saludar (self):
        print ("Mi nombre es: " + self.nombre + " y gano: "+ str(self.salario)+" desde el metodo heredado")

empleado = Empleado("Maicol") # crear objeto a partir de una clase
empleado.saludar("Hola me llamo: ")
empleado.modificar_salario(1000)
empleado.ver_salario()
#empleado.saludar()