import os
import oracledb

class Config(object):
    SECRET_KEY = 'myv_mike11'
    
    # Configuración envío de correos
    MAIL_SERVER = 'smt-relay.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'notificacion@cootep.com.co'
    MAIL_DEFAULT_SENDER = 'Servicio de notificacion', MAIL_USERNAME
    MAIL_PASSWORD = 'hxbfzqhghlflnrqo'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = '192.168.17.82'
    MYSQL_USER = 'cootep'
    MYSQL_PASSWORD = 'Cootep2023!'
    MYSQL_DB = 'convenios1'

    # Conexión Oracle
    connection = oracledb.connect(user='LINIX', password='LNXPROD2023', dsn='10.180.131.2:1521/LINIX')