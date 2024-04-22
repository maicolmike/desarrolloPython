from peewee import *

database = MySQLDatabase('fastapi_project',
                         user='root',
                         password='',
                         host='localhost',
                         port=3306)