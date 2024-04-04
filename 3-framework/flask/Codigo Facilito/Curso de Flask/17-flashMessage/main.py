

from flask import Flask 
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from flask_wtf.csrf import CSRFProtect #from flask import CsrfProtect asi se colocaba antes
import forms

app = Flask(__name__) 
app.secret_key = ('myv_mike11')
csrf = CSRFProtect(app)

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

@app.route('/comment', methods = ['GET','POST'])
def comment():
    return render_template ('comment.html')
 
if __name__ == '__main__':
    app.run( debug = True, port= 8000)