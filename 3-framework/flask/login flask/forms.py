from wtforms import Form
from wtforms import StringField
from wtforms import PasswordField
from wtforms import HiddenField
from wtforms import validators
from models import User  

def length_honeypot (form, field):
    if len (field.data)> 0:
        raise validators.ValidationError('EL campo debe estar vacio')

class CreateForm(Form):
    username= StringField('Usuario',
                          [validators.DataRequired(message='El nombre de usuario es requerido'),
                           validators.length(min=4, max=25, message='Ingrese un nombr de usuario valido minimo 4 caracteres')
                          ]
                         )
    
    password = PasswordField ('Contraseña', [validators.DataRequired(message='La contraseña es requerida')])
    
    honeypot =  HiddenField ('', [length_honeypot])
    def validate_username(form,field):
        username = field.data
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError('El nombre de usuario ya existe')
    
class LoginForm (Form):
  username= StringField('Usuario',
                        [
                        validators.DataRequired(message='El nombre de usuario es requerido'),
                        validators.length(min=4, max=25, message='Ingrese un nombr de usuario valido minimo 4 caracteres')
                          ])
  password = PasswordField ('Contraseña', [validators.DataRequired(message='La contraseña es requerida')])