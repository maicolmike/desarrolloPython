from flask import Flask 
from flask import request

app = Flask(__name__) 

@app.route('/')  
def index():
    return 'Hola mundo rutas 2'

# http://127.0.0.1:8000/params/maicol
# http://127.0.0.1:8000/params/maicol/yela/

@app.route('/params/')  
@app.route('/params/<name>/')  
@app.route('/params/<name>/<last_name>/')  
def params(name='Valor default', last_name = 'Valor 2 default'):
    return 'El parametro es {} {}'.format(name,last_name)

@app.route('/params2/') 
@app.route('/params2/<name>/')  
@app.route('/params2/<name>/<int:num>/') 
def params2(name='Valor default', num = 'Valor 2 default'):
    return 'El parametro es {} {}'.format(name,num)
    
if __name__ == '__main__':
    app.run( debug = True, port= 8000)