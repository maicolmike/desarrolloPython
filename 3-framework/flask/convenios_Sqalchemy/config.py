import os
import cx_Oracle
#si se llega a presentar el ellor de falta Oracle Client library se pondria la siguiente linea de comando 
#cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_8") #descargar la libreria Oracle Client library y extraerla en una carpeta luego decirle donde deve enlazarse

class Config (object):
    SECRET_KEY = 'myv_mike11'
    
class DevelopmentConfig(Config):
    DEBUG = True #se actualize sin nesecidad de vovler a correrlo
    #configuracion base de datos libreria SQLALCHEMY
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/convenios1'
    SQLALCHEMY_DATABASE_URI = 'mysql://sistemas:sistemas@192.168.17.82/convenios1'
    SQLALCHEMY_TRACK_MODIFICATIONS= False # por si sale algun mensaje de warning
    
    #oracle
    connection = cx_Oracle.connect(user='LINIX', password= 'LNXPROD2022', dsn= '10.180.131.2:1521/LINIX', encoding = 'UTF-8')