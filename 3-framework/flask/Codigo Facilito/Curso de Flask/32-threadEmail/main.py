

from flask import Flask 
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from flask import g
from flask import copy_current_request_context
from werkzeug.security import generate_password_hash

from config import DevelopmentConfig

from models import db
from models import User
from models import Comment

from flask_wtf.csrf import CSRFProtect #from flask import CsrfProtect asi se colocaba antes
import forms
import json
from helper import date_format 

from flask_mail import Mail
from flask_mail import Message

import threading #enviar correos segundo plano


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()
mail= Mail()

#para enviar correos
def send_email(user_email, username):
    msg = Message ('Gracias por tu registro',
                    sender = app.config['MAIL_USERNAME'],
                    recipients = [user_email])
       
    msg.html = render_template('email.html', username = username)
    mail.send(msg)
#fin enviar correo

def create_session(username = '', user_id =''):
    session['username']= username
    session['user_id']= user_id

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['comment','index']:
        return redirect(url_for('login'))
    
    elif 'username' in session and request.endpoint in ['login','create']:
        return redirect(url_for('index'))
@app.after_request
def after_request(response):
    return response
    
@app.route('/')  
def index():
    if 'username' in session:
        username = session['username']
        print (username)
    title="Index"
    return render_template('index.html',title=title)

@app.route('/login', methods = ['GET','POST'])
def login():
    title="Login"
    login_form = forms.LoginForm(request.form)
    if request.method== 'POST' and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data
        
        #haremos una consulta para ver si los datos que nos envia el formulario coincide con los de la bd
        user = User.query.filter_by(username = username).first() # me devolvera un objeto de tipo User, sino hay nada me devolvera NONE
        # es como decir esto select * from users where username = username limit 1
        if user is not None and user.verify_password(password):
            success_message = 'Bienvenido {}'.format(username)
            flash (success_message)
            session['username']= username
            #session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            error_message = 'Usuario o contraseña no valida'
            flash (error_message)
        
    return render_template('login.html',title=title, form = login_form)

@app.route('/logout')  #cerrar sesion
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

@app.route('/cookie')  
def cookie():
    title="Cookie"
    reponse = make_response( render_template('cookie.html',title=title))
    reponse.set_cookie('custome_cookie','eduardo')
    return reponse

#@app.route('/ajax-login', methods=['POST'])  
#def ajax_login():
   # print(request.form)
    #username=request.form['username']
    #response = { 'status':200, 'username':username, 'id':1 } 
    #return json.dumps(response)

@app.route('/comment', methods = ['GET','POST'])
def comment():
    comment_form = forms.CommentForm(request.form)
    user = User.query.filter_by(id = id).first()
    if request.method== 'POST' and comment_form.validate():
        #user_id = session['user_id']  #tener por sesion el user_id
        username = session['username']
        comment= Comment (#user_id = user_id ,
                          text = comment_form.comment.data
                          )
        
        db.session.add(comment)
        db.session.commit()
        
        success_message = 'Comentario registrado en la bd'
        flash(success_message)
        
    else: 
        print ("Error en el formulario de Comentario")

    title="Comentario"
    return render_template('comment.html',title=title, form= comment_form) 

@app.route('/create', methods = ['GET','POST'])
def create():
    create_form = forms.CreateForm(request.form)
    
    if request.method== 'POST' and create_form.validate():
        
        user= User (username = create_form.username.data,
                   password = create_form.password.data,
                   email =create_form.email.data)
        
        db.session.add(user)
        db.session.commit()
        
        #decorador para poder trabajar en sedundo plano para el envio de correos
        @copy_current_request_context
        def send_message(email,username):
            send_email(email, username)

        #envio de correos
        sender = threading.Thread(name ='mail_sender',
                                  target = send_message, 
                                  args = (user.email, user.username))
        sender.start()   #Fin envio de correos                          

        success_message = 'Usuario registrado en la bd'
        flash(success_message)
        
    title="Create"
    return render_template('create.html',title=title, form= create_form) 

@app.route('/reviews', methods = ['GET'])
@app.route('/reviews/<int:page>', methods = ['GET'])
def reviews(page=1):
    per_page = 2
    title="Reviews"
    #comments = Comment.query.join(User).add_columns(User.id,User.username, Comment.text)
    comments = Comment.query.join(User).add_columns(User.id,User.username, Comment.text,Comment.created_date).paginate(page=page, per_page=per_page, error_out=False)
    return render_template('reviews.html',title=title, comments = comments , date_format = date_format)

@app.route('/email')
def email():
    return render_template('email.html')

if __name__ == '__main__':
    csrf.init_app(app) #inicializar el cifrado
    db.init_app(app) #inicializar la base de datos
    mail.init_app(app) #inicializar el correo
    
    with app.app_context():
        db.create_all()
        
    app.run(port= 8000) #inicializar la app en este puerto