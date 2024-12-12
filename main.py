import os
import importlib.util

scripts_dir = 'skripts/'

for filename in os.listdir(scripts_dir):
    if filename.endswith('.py'):
        script_path = os.path.join(scripts_dir, filename)
        spec = importlib.util.spec_from_file_location(filename[:-3], script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        if hasattr(module, 'run'):
            module.run()
