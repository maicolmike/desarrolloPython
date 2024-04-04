#si genera error por la conexion oracle debemos comentariar connectionOracle=DevelopmentConfig.connection y en config.py tambien
from flask import Flask 
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import flash
from flask import g
from flask import session
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import DevelopmentConfig # para que tome las configuraciones del archivo config.py
from models.ModeloCreate import ModeloCreate
from models.ModeloListarUsuarios import ModeloListarUsuarios
from flask import jsonify
from flask_mail import Mail #envio de correos
from flask_mail import Message
from flask import copy_current_request_context # trabajar en segundo plano

import threading #enviar correos segundo plano
import time
import random
import string

from forms import CreateForm # para que tome la validacion de usuario no repetido

from models.entities.Usuario import Usuario
from models.ModeloUsuario import ModeloUsuario
from models.ModeloConsultar import ModeloConsultar 
from models.ModeloUpdate import ModeloUpdate

from datetime import timedelta  # para que la sesion se cierre si no hay actividad

import forms

app = Flask(__name__) # toda aplicacion de flask debe llevar esta linea
app.config.from_object(DevelopmentConfig) # para que tome el archivo de config.py
#csrf = CSRFProtect() # para poder utilizar el cifrado
csrf = CSRFProtect(app) # para poder utilizar el cifrado en linux

login_manager_app = LoginManager (app)  #iniciar flask-login
db = MySQL (app)
connectionOracle = DevelopmentConfig.connection #para que me tome la conexion de Oracle

mail= Mail(app)

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5) # para que la sesion se cierre si no hay actividad 

@login_manager_app.user_loader #iniciar flask-login 2da parte
def load_user(id):
    return ModeloUsuario.obtener_por_id(db, id)

@app.errorhandler(404) # manejo del error 404
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/')
@login_required #para que no accedan sin iniciar sesion
def index():
    title="Index"
    return render_template('index.html',title=title)

#para enviar correos creacion usuarios
def send_email(email,user,contra):
    msg = Message ('Usuario y clave - COOTEP LTDA',
                    #sender = app.config['MAIL_USERNAME'], #solo envia el correo
                    sender = app.config['MAIL_DEFAULT_SENDER'], # envia correo y el alias
                    recipients = [email])
       
    msg.html = render_template('emailUsuario.html', passwordTemporal = contra, user=user)
    mail.send(msg)
#fin enviar correo

@app.route('/create', methods = ['GET','POST'])
@login_required #para que no accedan sin iniciar sesion
def create():
    title="Create"
    create_form = forms.CreateForm(request.form)
    if request.method== 'POST' and create_form.validate():
        user = create_form.usuario.data # creo variable para tomar el nombre de usuario e imprimirlo
        email = create_form.email.data
        contra = create_form.password.data
        tipoUser = create_form.tipousuario.data
        ModeloCreate.agregar(db, user,email,contra,tipoUser,None) #envio la coneccion mysql y los datos que necesita la classe ModeloCreate funcion agregar
        #decorador para poder trabajar en segundo plano para el envio de correos
        @copy_current_request_context
        def send_message(email,contra,user):
            send_email(email, contra,user)

        #envio de correos
        sender = threading.Thread(name ='mail_sender',
                                  target = send_message, 
                                  args = (email, contra,user))
        sender.start()   
        #Fin envio de correos    
        success_message = 'Usuario registrado correctamente'
        flash(success_message)
        
    return render_template('create.html',title=title, form= create_form) 

@app.route('/consultar', methods = ['GET','POST'])
@login_required #para que no accedan sin iniciar sesion
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
                #print("Consulta",consulta)
                #print("Data",data)
                #print("Data consulta",data['dataConsulta'])
                for datos in data['dataConsulta']:
                    if (datos[2] == None or datos[2] <= 0) and (datos[3] == None or datos[3] <= 0) and (datos[4] == None or datos[4] <= 0) and (datos[5] == None or datos[5] <= 0):
                        success_message = 'Activo para convenios'
                        flash (success_message, 'success')
                    else:
                        success_message = 'No apto para convenio'
                        flash (success_message, 'danger')        
                #time.sleep(100) #funcion para que se demore en redireccionar
        return render_template('consultar.html', title= title, form= consultar_form, data=data)
    except Exception as ex:
        return (ex)
     
@app.route('/login', methods = ['GET','POST'])
def login():
    title="Login"
    login_form = forms.LoginForm(request.form)
    if request.method== 'POST' and login_form.validate():
        user = login_form.usuario.data # creo variable para tomar el nombre de usuario e imprimirlo
        contra = login_form.password.data
        usuario = Usuario(None, user, contra, None, None) #utilizo la clase usuario
        usuario_logeado = ModeloUsuario.login(db, usuario)
        if usuario_logeado != None:
            login_user(usuario_logeado)
            success_message = 'Bienvenido {}'.format(user)
            flash (success_message, 'success')
            return redirect(url_for('index'))
        else:
            error_message = 'Usuario o contraseña no valida'
            flash (error_message, 'danger')
            return render_template('login.html',title=title, form = login_form)
    else:
        return render_template('login.html',title=title, form = login_form)
    
@app.route('/update', methods = ['GET','POST'])
@login_required #para que no accedan sin iniciar sesion
def update():
    title="update"
    update_form = forms.UpdateForm(request.form)
    if request.method== 'POST' and update_form.validate():
        password = update_form.usuario.data # creo variable para tomar la contraseña actual
        passwordNew = update_form.passwordNew.data
        passwordNewConfirmation = update_form.passwordNewConfirmation.data
        user = current_user.usuario
        usuario = Usuario(None, user, password,None,None) #utilizo la clase usuario
        contra_confirmada = ModeloUpdate.password(db, usuario)
        if contra_confirmada != None:
            if password == passwordNew :
                success_message = 'La nueva contraseña debe ser diferente a la actual'
                flash (success_message, 'warning')
                #return redirect(url_for('update'))
            elif passwordNew != passwordNewConfirmation:
                success_message = 'La confirmación de la contraseña no concuerda con la nueva contraseña'
                flash (success_message, 'warning')
                #return redirect(url_for('update'))
            else :
                contraEncriptada = ModeloCreate.create_password(passwordNew)
                ModeloUpdate.actualizar(db, contraEncriptada,user)
                success_message = 'La contraseña ha sido cambiada exitosamente'
                flash (success_message, 'success')
                return redirect(url_for('update'))
        else:
            error_message = 'Contraseña actual inválida. Verifique la información registrada.'
            flash (error_message, 'warning')
            #return render_template('update.html',title=title, form = update_form)
        
    return render_template('update.html',title=title, form = update_form) 

@app.route('/usuarios', methods = ['GET','POST'])
@login_required #para que no accedan sin iniciar sesion
def usuarios():
    title="usuarios"
    try:
        listado = ModeloListarUsuarios.listar_usuarios(db)
        data = {
            'dataConsulta': listado
        }
        return render_template('usuarios.html', title=title, data=data)
        #return render_template('usuarios copy.html', title=title, data=data)
    except Exception as ex:
        return (ex)
    
#esta funcion no la estoy utilizando para utilizarla toca en la funcion def usuarios(): cambiar el return render_template('usuarios.html', title=title, data=data) por usuarios1.html o usuarios2.html
@app.route('/listarUsuarios', methods=['POST'])
@login_required
def listarUsuarios():
    data_request = request.get_json()
    data = {}
    data_request=request.get_json()
    #print("Data request",data_request)
    data={}
    try:
        #libro=data_request['isbn'],None,None,None,None
        #compra= None,libro,current_user
        data['exito']= ModeloUpdate.registrar_usuario(db)
    except Exception as ex:
        data['mensaje']=format(ex)
        data['exito']= False
    return jsonify(data)

@app.route('/edit/<string:id>', methods=['GET','POST'])
@login_required
def edit(id):
    username = request.form['username']
    email = request.form['userEmail']
    tipousuario = request.form['tipousuario']
    ModeloUpdate.editar(db, username,email,tipousuario,id)
    time.sleep(1.5) #funcion para que se demore en redireccionar
    return redirect(url_for('usuarios'))   
    
@app.route('/cambiar/<string:id>', methods=['GET','POST'])
@login_required
def cambiar(id):
    passnew = request.form['passnew']
    ModeloUpdate.cambiarpass(db, passnew, id)
    time.sleep(1.5) #funcion para que se demore en redireccionar
    return redirect(url_for('usuarios'))

#@app.route('/delete/<string:id>') #para utilziarlo en la vista usuarios.html en <a> href="{{url_for('delete', id=datos[0])}}"
@app.route('/delete/<string:id>', methods=['GET','POST'])
@login_required
def delete(id):
    ModeloUpdate.eliminar(db, id)
    time.sleep(1.5) #funcion para que se demore en redireccionar
    return redirect(url_for('usuarios'))

#para enviar correos y recuperar contraseña
def send_email2(emails, passnew,usuario):
    msg = Message ('Nueva Clave - COOTEP LTDA',
                    #sender = app.config['MAIL_USERNAME'], #solo envia el correo
                    sender = app.config['MAIL_DEFAULT_SENDER'], # envia correo y el alias
                    recipients = [emails])
       
    msg.html = render_template('email.html', passwordTemporal = passnew, user=usuario)
    mail.send(msg)
#fin enviar correo

@app.route('/recuperarClave', methods = ['GET','POST'])
def recuperarClave():
    title= "Recuperar clave"
    if request.method == 'POST':
        usuario = request.form['usuario']  # para utilizar esto debo primero poner el request.method
        consultaUsuario = ModeloUsuario.recuperarUsuario(db, usuario) # en la variable consultaUsuario guardo un diccionario con los datos que arroja la consulta 
        if consultaUsuario != None:
            #combinadas = string.printable # numeros letras minusculas letras mayusculas caracteres especiales
            cadenaModificada = string.digits + string.ascii_letters + "*#$&!?"
            # proceso para seleccionar una cadena aleatoria
            passnew = "" 
            for _ in range(6):
                passnew += random.SystemRandom().choice(cadenaModificada)
            #passnew = consultaUsuario[1] # en esta variable envio el nombre de usuario que tendo de la consulta
            id = consultaUsuario[0] # en esta variable estoy guardado el id
            ModeloUpdate.cambiarpass(db, passnew, id) # hago el proceso de ponerle contraseña con el mismo numero de usuario y encriptandola
            emails=consultaUsuario[2]
            
            #codigo envio correo sencillo sin utilziar el segundo plano
            #msg = Message('Usuario recuperado',sender=app.config['MAIL_USERNAME'],recipients=[emails])
            #msg.html= render_template('email.html', passwordTemporal = passnew)
            #mail.send(msg)
            #fin condigo envio correo
            
            #decorador para poder trabajar en segundo plano para el envio de correos
            @copy_current_request_context
            def send_message2(emails,passnew,usuario):
                send_email2(emails, passnew,usuario)

            #envio de correos
            sender = threading.Thread(name ='mail_sender',
                                  target = send_message2, 
                                  args = (emails, passnew,usuario))
            sender.start()   
            #Fin envio de correos    
            
            success_message = 'La Contraseña fue enviada al correo registrado {}'.format(consultaUsuario[2])
            flash (success_message, 'success')
            return redirect(url_for('login'))
        else:
            error_message = 'Usuario no registra en la base de datos'
            flash (error_message, 'danger')
            return render_template('recuperarClave.html',title=title)
    return render_template('recuperarClave.html', title= title)
    #return redirect(url_for('recuperarClave')) 
    
#cerrar sesion
@app.route('/logout')  #cerrar sesion
def logout():
    logout_user() # al importar flask login, importamos logout_user que sirve para cerrar sesion
    success_message = 'Sesion cerrada'
    flash(success_message)
    return redirect(url_for('login')) 
    
@app.errorhandler(401) # manejo del error 401
def pagina_no_autorizada(error):
    return redirect(url_for('login'))    

@app.errorhandler(400) # manejo del error 400
def pagina_no_autorizada(error):
    return redirect(url_for('login'))   
    
if __name__ == '__main__':
    csrf.init_app(app) #inicializar el cifrado
    mail.init_app(app) #inicializar el correo
    
    app.register_error_handler(401,pagina_no_autorizada) # para que cuando no este logeado lo redirija al login
    app.run() #inicializar la app con el host y puerto predeterminados  host: 127.0.0.1:   port: 5000
    #app.run(port= 8000) #inicializar la app con el host por defecto y el puerto seleccionado
    #app.run(host='192.168.17.63', port= 8000) #inicializar la app con el host y puerto que seleccionemos