# This file must be used with "source activate" command
# You cannot run it directly

import os

# Get the directory of this script, regardless of the current working directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Get the path to the virtual environment directory by following the symbolic links
VIRTUAL_ENV = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Set the required environment variables
os.environ['PATH'] = os.path.join(VIRTUAL_ENV, 'bin') + os.pathsep + os.environ.get('PATH', '')
os.environ['VIRTUAL_ENV'] = VIRTUAL_ENV

# Set up the shell prompt to indicate the virtual environment
old_ps1 = os.environ.get('PS1', '')
if old_ps1:
    new_ps1 = '({}) {}'.format(os.path.basename(VIRTUAL_ENV), old_ps1)
    os.environ['PS1'] = new_ps1

# Deactivate function to undo these changes
def deactivate():
    os.environ['PATH'] = os.environ['PATH'].replace(os.path.join(VIRTUAL_ENV, 'bin') + os.pathsep, '')
    os.environ.pop('VIRTUAL_ENV', None)
    if old_ps1:
        os.environ['PS1'] = old_ps1