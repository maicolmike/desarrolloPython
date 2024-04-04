from wtforms import Form
from wtforms import StringField , TextAreaField
from wtforms.fields import EmailField

from wtforms import validators

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