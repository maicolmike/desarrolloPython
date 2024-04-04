from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
#from flask_bcrypt import Bcrypt

db = SQLAlchemy()
#bcrypt = Bcrypt()

#Aqui creamos una clase en la cual va a tener el modelo a crear en nuestra base de datos
class User(db.Model):
    #Aqui le decimos a q tabla 
    __tablename__ = 'users'  #indico el nombre que quiero darle a la tabla sino el toma por defecto el de la clase
    #Y aqui sencillamente creamos los datos q va a tener nuestra tabla
    id = db.Column( db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique= True)
    password = db.Column(db.String(166))
    created_date = db.Column(db.DateTime, default= datetime.datetime.now)
    
    def __init__(self, username,password):
        self.username = username
        self.password = self.create_password(password)
        
    def create_password(self, password):
        return generate_password_hash(password)
        #return bcrypt.generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)
        #return bcrypt.check_password_hash(self.password, password)