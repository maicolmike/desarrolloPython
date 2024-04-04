from wtforms import Form
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import PasswordField
from wtforms import HiddenField
from wtforms import validators
from wtforms.fields import EmailField
from models import User  

def length_honeypot (form, field):
    if len (field.data)> 0:
        raise validators.ValidationError('EL campo debe estar vacio')

class CommentForm(Form):
    username= StringField('Usuario',
                          [validators.DataRequired(message='El nombre de usuario es requerido'),
                           validators.length(min=4, max=25, message='Ingrese un nombr de usuario valido minimo 4 caracteres')
                            
                          ]
                         )
    email= EmailField('Correo',
                          [validators.DataRequired(message='El correo electronico es requerido'),
                           validators.Email( message='Ingrese un correo electronico valido')
                            
                          ])
    comment = TextAreaField('Comentario')
    honeypot =  HiddenField ('', [length_honeypot])
    
class LoginForm (Form):
    username= StringField('Usuario',
                          [
                            validators.DataRequired(message='El nombre de usuario es requerido'),
                            validators.length(min=4, max=25, message='Ingrese un nombr de usuario valido minimo 4 caracteres')
                          ])
    password = PasswordField ('Contraseña', [validators.DataRequired(message='La contraseña es requerida')])
    
class CreateForm(Form):
    username= StringField('Usuario',
                          [validators.DataRequired(message='El nombre de usuario es requerido'),
                           validators.length(min=4, max=25, message='Ingrese un nombr de usuario valido minimo 4 caracteres')
                            
                          ]
                         )
    
    password = PasswordField ('Contraseña', [validators.DataRequired(message='La contraseña es requerida')])
    
    email= EmailField('Correo',
                          [validators.DataRequired(message='El correo electronico es requerido'),
                           validators.Email( message='Ingrese un correo electronico valido')
                            
                          ])
    honeypot =  HiddenField ('', [length_honeypot])
    #validar que al momento de registar un usuario este no se encuentre en la base de datos
    def validate_username(form,field):
        username = field.data
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError('El nombre de usuario ya existe')
