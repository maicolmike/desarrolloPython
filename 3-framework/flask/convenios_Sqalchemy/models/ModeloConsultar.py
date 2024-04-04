class ModeloConsultar():
    
    @classmethod #colocarlo
    def listar_consulta (self, conexOracle,asociado):
        try:
            cursor = conexOracle.connection.cursor()
            sql = "select AP014.AANUMNIT, AP014.NNASOCIA , AP014.I_ESTASO from AP014MCLIENTE AP014 where AP014.AANUMNIT = '{0}'".format(asociado)
            cursor.execute(sql)
            data=cursor.fetchall()
            listaConsulta = []  #lista vacia
            for row in data:
                tuplaConsulta = row[0], row[1], row[2] # tupla
                listaConsulta.append(tuplaConsulta)  #llenando la lista
            return listaConsulta
        except Exception as ex:
            raise Exception (ex)