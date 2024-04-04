from flask_script import Manager, Server
from app import inicializar_app
from config import config

configuracion = config['development']
app= inicializar_app(configuracion)

manager = Manager(app)
#manager.add_command('runserver', Server(host='127.0.0.1', port=5010))
#manager.add_command('runserver', Server(host='localhost', port=5010))
manager.add_command('runserver', Server(host='192.168.0.63', port=5010))
#manager.add_command('runserver', Server(host='192.168.137.1', port=5010))

if __name__ == '__main__':
    manager.run()