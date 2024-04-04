import os

class Config (object):
    SECRET_KEY = 'myv_mike11'
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587 # se utiliza activando TLS = True y poniendo SSL = False
    #MAIL_PORT = 465 # se utiliza activando SSl = True y poniendo TLS = False
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'maicol.yela@gmail.com'
    #MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_CF')  #se utilzia cuando gmail dejaba activar aplicaciones no seguras
    
    #se utiliza cuando la cuenta gmail tiene Activada verificacion en 2 pasos
    # administrar tu cuenta de google - seguridad - contraseñas de aplicaciones - seleccionar app (otra) - poner un nombre - copiar la contraseña de 16 digitos que se genera
    MAIL_PASSWORD = ('agggiltwyikpkhtp') #contraseña de 16 digitos que se genera
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS= False #por si sale algun mensaje de warning