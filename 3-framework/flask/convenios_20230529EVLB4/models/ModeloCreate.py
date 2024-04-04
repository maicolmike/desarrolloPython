from werkzeug.security import generate_password_hash
import datetime
from .entities.Usuario import Usuario
from .entities.TipoUsuario import TipoUsuario

class ModeloCreate():
    
    @classmethod
    def agregar(self, db, user,email,contra,tipoUser,created_date):
        try:
            cursor = db.connection.cursor()  #tomo la conexion
            contraEncriptada = self.create_password(contra) #creo la contraseña encriptada
            created_date = datetime.datetime.now() # se crea fecha y hora del registro
            cursor.execute("INSERT INTO usuario(usuario, email,password, tipousuario, created_date) VALUES (%s, %s, %s,%s, %s)",(user, email,contraEncriptada, tipoUser, created_date))  #ejecuto la consulto para agregar
            db.connection.commit() # para guardar los cambios
    
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod   
    def create_password(self, contra):
        return generate_password_hash(contra)