from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
#from datetime import datetime
import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users' #indico el nombre que quiero darle a la tabla sino el toma por defecto el de la clase
    id = db.Column( db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique= True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(166))
    created_date = db.Column(db.DateTime, default= datetime.datetime.now)
    
    def __init__(self, username,password,email):
        self.username = username
        #self.password = self.__create_password(password)  #de esta forma genera error
        self.password = self.create_password(password)  #se puede utilizar asi
        #self.password = generate_password_hash(password)   #asi tambien se puede utilizar
        self.email= email
        
    def create_password(self, password):
        return generate_password_hash(password)