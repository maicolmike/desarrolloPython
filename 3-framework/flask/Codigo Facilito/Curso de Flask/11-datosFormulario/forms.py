from wtforms import Form
from wtforms import StringField , TextAreaField
from wtforms.fields import EmailField

class CommentForm(Form):
    username= StringField('Usuario')
    email= EmailField('Correo')
    comment = TextAreaField('Comentario')