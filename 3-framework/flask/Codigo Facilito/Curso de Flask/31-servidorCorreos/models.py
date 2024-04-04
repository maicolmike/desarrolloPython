from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
#from datetime import datetime
import datetime

db = SQLAlchemy()
#Aqui creamos una clase en la cual va a tener el modelo a crear en nuestra base de datos
class User(db.Model):
    #Aqui le decimos a q tabla 
    __tablename__ = 'users'  #indico el nombre que quiero darle a la tabla sino el toma por defecto el de la clase
    #Y aqui sencillamente creamos los datos q va a tener nuestra tabla
    id = db.Column( db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique= True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(166))
    comments = db.relationship('Comment') # se crea esta ralacion si es un a muchos
    created_date = db.Column(db.DateTime, default= datetime.datetime.now)
    
    def __init__(self, username,password,email):
        self.username = username
        self.password = self.create_password(password)  #se puede utilizar asi
        #self.password = generate_password_hash(password)   #asi tambien se puede utilizar
        self.email= email
        
    def create_password(self, password):
        return generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)
#CREAR COMMENT
class Comment(db.Model):
    #Aqui le decimos a q tabla 
    __tablename__ = 'comments'  #indico el nombre que quiero darle a la tabla sino el toma por defecto el de la clase
    #Y aqui sencillamente creamos los datos q va a tener nuestra tabla
    id = db.Column( db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    text = db.Column(db.Text())
    created_date = db.Column(db.DateTime, default= datetime.datetime.now)
    
        