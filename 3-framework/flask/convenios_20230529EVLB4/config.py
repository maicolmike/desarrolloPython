import os
import oracledb

#import cx_Oracle
#si se llega a presentar el ellor de falta Oracle Client library se pondria la siguiente linea de comando 
#cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_8") #descargar la libreria Oracle Client library y extraerla en una carpeta luego decirle donde deve enlazarse

class Config (object):
    SECRET_KEY = 'myv_mike11'
    
    #configuracion envio de correos
    #MAIL_SERVER = 'mail.cootep.com.co' # funciona para el correo institucional cootep
    #MAIL_SERVER = 'smt-relay.gmail.com' # funciona con MAIL_USERNAME = 'notificacion@cootep.com.co' correo institucional cootep 
    MAIL_SERVER = 'smtp.gmail.com' # funciona con MAIL_USERNAME = 'cootepptyo@gmail.com'  
    MAIL_PORT = 587 # se utiliza activando TLS = True y poniendo SSL = False
    #MAIL_PORT = 465 # se utiliza activando SSl = True y poniendo TLS = False
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    
    MAIL_USERNAME = 'soportesistemas@cootep.com.co' # funciona con MAIL_SERVER = 'mail.cootep.com.co'
    MAIL_DEFAULT_SENDER = 'Servicio de notificacion', MAIL_USERNAME # configurar el alias
    MAIL_PASSWORD = ('bpxnuyscoegaehhy')
    #MAIL_SERVER = 'smtp.gmail.com' # funciona con MAIL_USERNAME = 'cootepptyo@gmail.com'  #'smtp-mail.outlook.com' # funciono con el correo hotmail
    #MAIL_USERNAME = 'cootepptyo@gmail.com' #funciona con MAIL_SERVER = 'smtp.gmail.com'
    #MAIL_SERVER = 'smtp.office365.com'
    
    # se utiliza cuando la cuenta gmail tiene Activada verificacion en 2 pasos
    # administrar tu cuenta de google - seguridad - Verificación en 2 pasos - contraseñas de aplicaciones - seleccionar app (otra) - poner un nombre - copiar la contraseña de 16 digitos que se genera
    #MAIL_PASSWORD = ('ztyfjzymjcrwggnt') #contraseña de 16 digitos que se genera
    #se utilzia cuando gmail dejaba activar aplicaciones no seguras
    #MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_CF')
    
class DevelopmentConfig(Config):
    DEBUG = True #se actualize sin nesecidad de vovler a correrlo
    #configuracion base de datos libreria SQLALCHEMY
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/convenios1'
    #SQLALCHEMY_DATABASE_URI = 'mysql://sistemas:sistemas@192.168.17.82/convenios1'
    #SQLALCHEMY_TRACK_MODIFICATIONS= False # por si sale algun mensaje de warning
    #configuracion base de datos libreria MYSQL
    #MYSQL_HOST = 'localhost'
    #MYSQL_USER = 'root'
    #MYSQL_PASSWORD = ''
    MYSQL_HOST = '192.168.17.82'
    MYSQL_USER = 'cootep'
    MYSQL_PASSWORD = 'Cootep2023!'
    MYSQL_DB = 'convenios1'
    #oracle
    #connection = cx_Oracle.connect(user='LINIX', password= 'LNXPROD2022', dsn= '10.180.131.2:1521/LINIX', encoding = 'UTF-8')
    connection = oracledb.connect(user='LINIX', password= 'LNXPROD2022', dsn= '10.180.131.2:1521/LINIX', encoding = 'UTF-8')