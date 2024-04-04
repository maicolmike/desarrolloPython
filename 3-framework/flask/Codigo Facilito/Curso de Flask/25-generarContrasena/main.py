

from flask import Flask 
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from flask import g
from werkzeug.security import generate_password_hash

from config import DevelopmentConfig

from models import db
from models import User

from flask_wtf.csrf import CSRFProtect #from flask import CsrfProtect asi se colocaba antes
import forms
import json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
#app.secret_key = ('myv_mike11')
#csrf = CSRFProtect(app)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    print("1")
    g.test = "test1"
    #prueba local
    #print (request.endpoint) #tomar nombre de la url
    #if 'username' not in session:
       # print ("Usuario no esta logeado")
        

@app.route('/')  
def index():
    print("2")
    print ("Index ",g.test)
    if 'username' in session:
        username = session['username']
        print (username)
    title="Index"
    return render_template('index.html',title=title)

@app.after_request
def after_request(response):
    print("3")
    print ("After ",g.test)
    variable= g.test
    print ("Variable ",g.test)
    return response

@app.route('/login', methods = ['GET','POST'])
def login():
    title="Login"
    login_form = forms.LoginForm(request.form)
    if request.method== 'POST' and login_form.validate():
        username = login_form.username.data
        success_message = 'Bienvenido {}'.format(username)
        flash (success_message)
        
        session['username']= login_form.username.data
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

@app.route('/ajax-login', methods=['POST'])  
def ajax_login():
    print(request.form)
    username=request.form['username']
    response = { 'status':200, 'username':username, 'id':1 } 
    return json.dumps(response)

@app.route('/comment', methods = ['GET','POST'])
def comment():
    comment_form = forms.CommentForm(request.form)
    
    if request.method== 'POST' and comment_form.validate():
        print (comment_form.username.data)
        print (comment_form.email.data)
        print (comment_form.comment.data)
    else: 
        print ("Error formulario")

    title="Formulario"
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
        
        success_message = 'Usuario registrado en la bd'
        flash(success_message)
    else: 
        print ("Error formulario")

    title="Create"
    return render_template('create.html',title=title, form= create_form) 

if __name__ == '__main__':
    csrf.init_app(app) #inicializar el cifrado
    db.init_app(app) #inicializar la base de datos
    
    with app.app_context():
        db.create_all()
        
    app.run(port= 8000) #inicializar la app en este puerto