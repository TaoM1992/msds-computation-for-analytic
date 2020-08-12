import importlib

module_name = 'pytest'

try:
    module = importlib.import_module(module_name, package=None)
except ModuleNotFoundError:
    import pip
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_name])
    module = importlib.import_module(module_name, package=None)