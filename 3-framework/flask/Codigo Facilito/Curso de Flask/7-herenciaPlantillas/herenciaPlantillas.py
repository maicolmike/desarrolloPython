from flask import Flask 
from flask import render_template

app = Flask(__name__) 

@app.route('/')  
def index():
    nombre= 'maicol'
    return render_template('index.html',nomb=nombre)

@app.route('/cliente')  
def cliente():
    lista_nombre= ['test1', 'test2','test3']
    return render_template('cliente.html',lista=lista_nombre)
    
if __name__ == '__main__':
    app.run( debug = True, port= 8000)