from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__='users' #indico el nombre que quiero darle a la tabla sino el toma por defecto el de la clase
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique= True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(66))
    created_date = db.Column(db.DateTime, default= datetime.datetime.now)
    