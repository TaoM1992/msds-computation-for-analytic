"""Check for 3rd party package, if not present, pip install it.

This is potentially dangerous code. Should only be used for educational purposes.
Defining a requirements.txt is one of many better options
"""

from importlib import import_module

module_name = 'pytest'

try:
    module = import_module(module_name, package=None) 
    exec(f'{module_name} = module')
except ModuleNotFoundError:
    import pip
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_name])
    module = import_module(module_name, package=None)
    exec(f'{module_name} = module')