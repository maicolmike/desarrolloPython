import os

class Config (object):
    SECRET_KEY = 'myv_mike11'
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS= False #por si sale algun mensaje de warning