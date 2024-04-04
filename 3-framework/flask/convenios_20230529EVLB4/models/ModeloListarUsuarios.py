class ModeloListarUsuarios():
    
    @classmethod #colocarlo
    def listar_usuarios (self, db):
        try:
            cursor = db.connection.cursor()
            cursor.execute("SELECT * FROM usuario")
            #cursor.execute("""SELECT password FROM usuario WHERE usuario = '{0}'""".format(usuario.usuario))    
            #data = cursor.fetchone()
            data=cursor.fetchall()
            listaUsuarios = []  #lista vacia
            for row in data:
                tuplaListado = row[0], row[1], row[2], row[3] , row[4], row[5] # tupla
                listaUsuarios.append(tuplaListado)  #llenando la lista
            return listaUsuarios
        except Exception as ex:
            raise Exception(ex)