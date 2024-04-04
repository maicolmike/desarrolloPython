from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = SQLAlchemy()

#Aqui creamos una clase en la cual va a tener el modelo a crear en nuestra base de datos
class User(db.Model):
    #Aqui le decimos a q tabla 
    __tablename__ = 'usuario'  #indico el nombre que quiero darle a la tabla sino el toma por defecto el de la clase
    #Y aqui creamos los datos q va a tener nuestra tabla
    id = db.Column( db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique= True)
    password = db.Column(db.String(166))
    tipousuario = db.Column(db.String(166))
    created_date = db.Column(db.DateTime, default= datetime.datetime.now)
    
    #para poder agragar datos al a base de datos
    def __init__(self, usuario,password,tipousuario):
        self.usuario = usuario
        self.password = self.create_password(password)
        self.tipousuario = tipousuario
    
    #generamos la contraseña encriptada   
    def create_password(self, password):
        return generate_password_hash(password)
        
    #haccemos la verificacion de la contraseña en archivo plano con la encriptada
    def verify_password(self, password):
        return check_password_hash(self.password, password) 