

from flask import Flask 
from flask import render_template
from flask import request
from flask_wtf.csrf import CSRFProtect #from flask import CsrfProtect asi se colocaba antes
import forms

app = Flask(__name__) 
app.secret_key = ('myv_mike11')
csrf = CSRFProtect(app)

@app.route('/')  
def index():
    comment_form = forms.CommentForm(request.form)
    
    if request.method== 'POST' and comment_form.validate():
        print (comment_form.username.data)
        print (comment_form.email.data)
        print (comment_form.comment.data)
    else: 
        print ("Error formulario")

    title="Index"
    return render_template('index.html',title=title, form= comment_form)
    #return render_template('index.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    title = "Login"
    login_form = forms.LoginForm()
    return render_template('login.html',title=title, form = login_form)

@app.route('/cookie')  
def cookie():
    return render_template('cookie.html')

@app.route('/comment', methods = ['GET','POST'])
def comment():
    return render_template ('comment.html')
 
if __name__ == '__main__':
    app.run( debug = True, port= 8000)