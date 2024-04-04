from .entities.Usuario import Usuario
from .ModeloCreate import ModeloCreate

class ModeloUpdate():
    
    @classmethod
    def password(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            cursor.execute("SELECT password FROM usuario WHERE usuario = %s", (usuario.usuario,))
            #cursor.execute("""SELECT password FROM usuario WHERE usuario = '{0}'""".format(usuario.usuario))    
            data = cursor.fetchone()
            if data != None:
                coincide = Usuario.verificar_password(data[0], usuario.password)
                if coincide:
                    #contra_coincide = Usuario(data[0],None, None, None)
                    contra_coincide = data[0]
                    return contra_coincide
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def actualizar(self, db, contraEncriptada,user):
        try:
            cursor = db.connection.cursor()
            cursor.execute("UPDATE usuario SET password = %s WHERE usuario = %s",(contraEncriptada,user))
            #cursor.execute("""SELECT password FROM usuario WHERE usuario = '{0}'""".format(usuario.usuario))    
            db.connection.commit() # para guardar los cambios
            #data =cursor.fetchone()  # guardar valor de la consulta en una variable
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def registrar_usuario(self, db):
        try:
            cursor = db.connection.cursor()
            cursor.execute("SELECT * FROM usuario")

            data=cursor.fetchall()
            #print (data)

            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def editar(self, db,username,email,tipousuario,id): #este modelo esta enlazada a usuarios.html y controlador def edit(id):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE usuario SET usuario = %s , email = %s, tipousuario = %s WHERE id = %s"
            data = (username, email,tipousuario, id)
            cursor.execute(sql, data)
            db.connection.commit() # para guardar los cambios
            data = cursor.fetchone()
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def cambiarpass(self, db, passnew, id): #este modelo esta enlazada a usuarios.html y controlador def cambiar(id):
        try:
            contraEncriptada = ModeloCreate.create_password(passnew) #creo la contraseña encriptada 
            cursor = db.connection.cursor()
            sql = "UPDATE usuario SET password = %s WHERE id = %s"
            data = ( contraEncriptada, id)
            cursor.execute(sql, data)
            db.connection.commit() # para guardar los cambios
            data = cursor.fetchone()
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def eliminar(self, db, id): #este modelo esta enlazada a usuarios.html y controlador def cambiar(id):
        try:
            cursor = db.connection.cursor()
            #sql = "DELETE FROM usuario WHERE id= %s"
            #data = (id)
            #cursor.execute(sql, data)
            cursor.execute("DELETE FROM usuario WHERE id= %s", (id,))  
            db.connection.commit() # para guardar los cambios
            #data = cursor.fetchone()
        except Exception as ex:
            raise Exception(ex)