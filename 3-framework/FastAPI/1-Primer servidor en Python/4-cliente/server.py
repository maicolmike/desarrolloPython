from jinja2 import Environment, FileSystemLoader
from wsgiref.simple_server import make_server

# Define la ruta al directorio donde se encuentran tus plantillas
templates_dir = '/home/cootep/Documents/programacion/desarrolloPython/3-framework/FastAPI/1-Primer servidor en Python/3-paginasDinamicas/templates'

def application(env, start_response):
    headers = [('Content-Type', 'text/html')]
    
    start_response('200 OK', headers)
    
    # Carga el entorno de Jinja2 con el cargador de sistema de archivos apuntando a tu directorio de plantillas
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('index.html')

    html= template.render(
        {
            'title': 'servidor en python',
            'name': 'maicol Yela'
        }
    )
    
    return [bytes(html, 'utf-8')]

# Crea el servidor usando la función application definida anteriormente
server = make_server('localhost', 8000, application)
print("Servidor en ejecución en http://localhost:8000")
server.serve_forever()
