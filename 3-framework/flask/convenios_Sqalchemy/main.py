from flask import Flask 
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from flask import g
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from config import DevelopmentConfig
#importar para que funcione Modelo Usuario
from models.ModeloUsuario import db
from models.ModeloUsuario import User
from models.ModeloConsultar import ModeloConsultar 

#from models.entities.Usuario import Usuario


from flask_wtf.csrf import CSRFProtect
import forms

app = Flask(__name__) # toda aplicacion de flask debe llevar esta linea
app.config.from_object(DevelopmentConfig) # para que tome el archivo de config.py
csrf = CSRFProtect() # para poder utilizar el cifrado
#csrf = CSRFProtect(app) # para poder utilizar el cifrado en linux

login_manager_app = LoginManager (app)  #iniciar flask-login
#db = MySQL (app)
connectionOracle=DevelopmentConfig.connection #para que me tome la conexion de Oracle

@login_manager_app.user_loader #iniciar flask-login 2da parte
def load_user():
    pass #ModeloUsuario.obtener_por_id(db, id)

@app.errorhandler(404) # manejo del error 404
def page_not_found(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    if 'usuario' not in session and request.endpoint in ['index','create']:
        return redirect(url_for('login'))
    
    elif 'usuario' in session and request.endpoint in ['login']:
        return redirect(url_for('index'))

@app.route('/')
#@login_required #para que no accedan sin iniciar sesion
def index():
    title="Index"
    if 'usuario' in session:
        username = session['usuario']
        print ('Usuario index:',username)
        user = User.query.filter_by(usuario = username).first() # me devolvera un objeto de tipo User, sino hay nada me devolvera NONE
        dataTipousuario = user.tipousuario
    return render_template('index.html',title=title, dataTipousuario=dataTipousuario, username=username)

@app.after_request
def after_request(response):
    return response

@app.route('/create', methods = ['GET','POST'])
def create():
    title="Create"
    create_form = forms.CreateForm(request.form)
    #compra= Usuario(None,libro,current_user,None)
    if request.method== 'POST' and create_form.validate():
        usuario= User(create_form.usuario.data,
                    create_form.password.data,
                    create_form.tipousuario.data)
        
        db.session.add(usuario)
        db.session.commit()
        
        success_message = 'Usuario registrado en la bd'
        flash(success_message)
        
    return render_template('create.html',title=title, form= create_form) 

@app.route('/consultar', methods = ['GET','POST'])
def consultar():
    title= "Consultar"
    consultar_form = forms.ConsultarForm(request.form)
    conexOracle=connectionOracle.cursor()  #conexOracle variable que guardo la coneccion
    asociado= consultar_form.usuario.data #tomo el dato que se ingresa en el formulario ConsultarForm form.usuario.data
    try:
        consulta = ModeloConsultar.listar_consulta(conexOracle,asociado)
        #creo un diccionario donde almacenare el resultado de consulta para luego pasarselo a la vista consultar.html y poder manipular cada elemento
        data = {
                'dataConsulta': consulta
        }
        if request.method== 'POST' and consultar_form.validate():
            if consulta == []: # valido que cuando se haga la consulta del asociado este tenga un documento valido, si la consulta arroja diccionario vacio indicamos que no existe el asociado
                error_message = 'Numero de documento no existe'
                flash (error_message, 'warning')
            else:
                success_message = 'Consulta exitosa'
                flash (success_message, 'success')
        return render_template('consultar.html', title= title, form= consultar_form, data=data)
    except Exception as ex:
        return (ex)

@app.route('/login', methods = ['GET','POST'])
def login():
    title="Login"
    login_form = forms.LoginForm(request.form)
    if request.method== 'POST' and login_form.validate():
        username = login_form.usuario.data
        password = login_form.password.data
        #haremos una consulta para ver si los datos que nos envia el formulario coincide con los de la bd
        user = User.query.filter_by(usuario = username).first() # me devolvera un objeto de tipo User, sino hay nada me devolvera NONE
        # es como decir esto select * from users where username = username limit 1
        print('Usuario:', user)
        
        if user is not None and user.verify_password(password):
            success_message = 'Bienvenido {}'.format(username)
            flash (success_message, 'success')
            session['usuario']= username
            return redirect(url_for('index'))
        else:
            error_message = 'Usuario o contraseña no valida'
            flash (error_message, 'warning')
    return render_template('login.html',title=title, form = login_form)

#cerrar sesion
@app.route('/logout')  #cerrar sesion
def logout():
    if 'usuario' in session:
        session.pop('usuario')
        success_message = 'Sesion cerrada'
        flash(success_message)
    return redirect(url_for('login'))
    
if __name__ == '__main__':
    csrf.init_app(app) #inicializar el cifrado
    db.init_app(app) #inicializar la base de datos de ModeloCreate SQLAlchemy()
    
    with app.app_context():
        db.create_all()
    
    #app.run(host='192.168.17.63', port= 8000) #inicializar la app con el host y puerto que seleccionemos
    app.run() #inicializar la app por defecto con el puerto seleccionado