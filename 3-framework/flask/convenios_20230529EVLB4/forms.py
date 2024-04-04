from wtforms import Form, StringField, PasswordField, HiddenField, validators, SelectField,IntegerField, EmailField

from models.ModeloCreate import ModeloCreate

from flask_mysqldb import MySQL
db = MySQL ()

#para evitar ataques 
def length_honeypot (form, field):
    if len (field.data)> 0:
        raise validators.ValidationError('EL campo debe estar vacio')

class CreateForm(Form):
    usuario= StringField('Usuario',
                          [validators.DataRequired(message='El nombre de usuario es requerido'),
                           validators.length(min=4, max=25, message='Ingrese un nombr de usuario valido minimo 4 caracteres')
                          ]
                         )
    email= EmailField('Email',
                          [validators.DataRequired(message='El correo electronico es requerido'),
                           validators.length(min=6, message='Ingrese una correo electronico valido minimo 6 caracteres')
                            
                          ])
    password = PasswordField ('Contraseña', [validators.DataRequired(message='La contraseña es requerida'),validators.length(min=4, max=25, message='Ingrese una contraseña valida minimo 4 caracteres')])
    tipousuario = SelectField(u'Tipo usuario', [validators.DataRequired(message='El tipo de usuario es requerido')], choices=[('', ''),('1', 'Administrador'), ('2', 'Cliente')])
    
    honeypot =  HiddenField ('', [length_honeypot]) #para evitar ataques
    
    @classmethod
    def validate_usuario(form,field,none): #validar el nombre de usuario no este repetido
        usuario = field.data # me devuelve los datos en un diccionario
        #print("Validatedb",db)
        #print("Validate1",usuario["usuario"])
        cursor = db.connection.cursor()
        cursor.execute("SELECT id, usuario, password FROM usuario WHERE usuario = %s", (usuario["usuario"],)) 
        usuario = cursor.fetchone()
        #usuario = ModeloCreate.agregar.query.filter_by(usuario = usuario).first()
        #print("Validate2",usuario)
        if usuario is not None:
            raise validators.ValidationError('El nombre de usuario ya existe')

class LoginForm (Form):
    usuario= StringField('Usuario',
                        [
                        validators.DataRequired(message='El nombre de usuario es requerido'),
                        validators.length(min=4, max=25, message='Ingrese un nombr de usuario valido minimo 4 caracteres')
                          ])
    password = PasswordField ('Contraseña', [validators.DataRequired(message='La contraseña es requerida'),validators.length(min=4, max=25, message='Ingrese una contraseña valida minimo 4 caracteres')])
  
class ConsultarForm (Form):
    usuario= IntegerField('Asociado',[validators.DataRequired(message='El nombre de usuario es requerido')])
    
class UpdateForm (Form):
    usuario = PasswordField ('Contraseña actual', [validators.DataRequired(message='La contraseña actual es requerida'),validators.length(min=4, max=25, message='Ingrese una contraseña valida minimo 4 caracteres')])
    passwordNew = PasswordField ('Contraseña nueva', [validators.DataRequired(message='La contraseña nueva es requerida'),validators.length(min=4, max=25, message='Ingrese una contraseña valida minimo 4 caracteres')])
    passwordNewConfirmation = PasswordField ('Confirmar Contraseña', [validators.DataRequired(message='La confirmacion de contraseña es requerida'),validators.length(min=4, max=25, message='Ingrese una contraseña valida minimo 4 caracteres')])