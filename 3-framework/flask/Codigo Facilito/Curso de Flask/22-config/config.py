import os

class Config (object):
    SECRET_KEY = 'myv_mike11'
    
class DevelopmentConfig(Config):
    DEBUG = True