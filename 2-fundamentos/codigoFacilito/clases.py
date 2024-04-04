class Usuario:
    nombre = "maicol" #propiedades
    
    def __init__(self,cargo): # metodo constructor
        self.cargo = cargo
    
    #asi se declara un metodo
    def saludar (self):
        print ("Hola mi nombre es " + self.nombre + " desde el metodo 1")
        
    def saludar2 (self, saludo):
        print (saludo + self.nombre + " desde el metodo 2")

pep = Usuario() # crear objeto a partir de una clase
pep.nombre = "Maic" # asignar valor a una propiedad de un objeto

familiar = Usuario()
familiar.nombre = "Kevin"


print ("Mi nombre es " + pep.nombre + " desde las propiedades")
print ("Mi nombre es " + familiar.nombre + " desde las propiedades")
pep.saludar()
pep.saludar2("Hola mi nombre es ")