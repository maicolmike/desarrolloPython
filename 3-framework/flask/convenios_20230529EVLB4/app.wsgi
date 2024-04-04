
import os
import sys
import logging

# Ruta del directorio raíz de tu aplicación
app_root = '/var/www/html/convenios'

# Añade el directorio raíz de la aplicación al PATH de Python
sys.path.insert(0, app_root)

# Activa el entorno virtual
activate_this = os.path.join(app_root, 'env', 'bin', 'activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Configuración básica de logging
logging.basicConfig(stream=sys.stderr)

# Importa la aplicación Flask
from main import app as application