from flask import Flask 
from flask import request

app = Flask(__name__) 

@app.route('/')  
def index():
    return 'Hola mundo rutas'

# http://127.0.0.1:8000/params?params1=maicol
# http://127.0.0.1:8000/params?params1=maicol&params2=yela
@app.route('/params')  
def params():
    param = request.args.get('params1', 'No contiene este parametro')
    param2 = request.args.get('params2', 'No contiene este parametro')
    return 'El parametro es {},{}'.format(param,param2)
    
if __name__ == '__main__':
    app.run( debug = True, port= 8000)