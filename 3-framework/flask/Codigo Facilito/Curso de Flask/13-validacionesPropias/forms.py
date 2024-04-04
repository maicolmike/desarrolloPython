from wtforms import Form
from wtforms import StringField , TextAreaField
from wtforms.fields import EmailField
from wtforms import HiddenField
from wtforms import validators

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