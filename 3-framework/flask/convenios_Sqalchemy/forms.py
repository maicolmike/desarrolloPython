from wtforms import Form
from wtforms import StringField
from wtforms import PasswordField
from wtforms import HiddenField
from wtforms import validators
from wtforms import SelectField
#from models.entities.Usuario import Usuario
from models.ModeloUsuario import User
from wtforms import IntegerField


def length_honeypot (form, field):
    if len (field.data)> 0:
        raise validators.ValidationError('EL campo debe estar vacio')

class CreateForm(Form):
    usuario= StringField('Usuario',
                          [validators.DataRequired(message='El nombre de usuario es requerido'),
                           validators.length(min=4, max=25, message='Ingrese un nombr de usuario valido minimo 4 caracteres')
                          ]
                         )
    password = PasswordField ('Contraseña', [validators.DataRequired(message='La contraseña es requerida')])
    tipousuario = SelectField(u'Tipo usuario', [validators.DataRequired(message='El tipo de usuario es requerido')], choices=[('', ''),('1', 'Administrador'), ('2', 'Cliente')])
    
    honeypot =  HiddenField ('', [length_honeypot])

    def validate_usuario(form,field): #validar el nombre de usuario no este repetido
        usuario = field.data
        usuario = User.query.filter_by(usuario = usuario).first()
        if usuario is not None:
            raise validators.ValidationError('El nombre de usuario ya existe')
    
class LoginForm (Form):
    usuario= StringField('Usuario',
                        [
                        validators.DataRequired(message='El nombre de usuario es requerido'),
                        validators.length(min=4, max=25, message='Ingrese un nombr de usuario valido minimo 4 caracteres')
                          ])
    password = PasswordField ('Contraseña', [validators.DataRequired(message='La contraseña es requerida')])

class ConsultarForm (Form):
    usuario= IntegerField('Asociado',[validators.DataRequired(message='El nombre de usuario es requerido')])