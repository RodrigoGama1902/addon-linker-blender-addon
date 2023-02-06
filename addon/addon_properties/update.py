import os

from ..utility.addon_module import get_addon_module_name, get_addon_version
from ..utility.paths import convert_to_absolute_path

def search_for_addons_modules(self, context):
    '''A generator that recursively search for __init__.py files with glob, when find one, stop and return the path'''
        
    found_modules_paths = []
    
    directory = convert_to_absolute_path(self.addon_directory_path)
    addons_to_link_list = self.addons_to_link_list
    
    addons_to_link_list.clear()
     
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file == "__init__.py":
                continue
                
            module_already_found = False
            for found_modules_path in found_modules_paths:
                if root.startswith(found_modules_path):
                    module_already_found = True
            
            if module_already_found:
                continue
            
            init_path = os.path.join(root, "__init__.py")
            
            new_addon = addons_to_link_list.add()
            new_addon.name = get_addon_module_name(init_path)
            new_addon.version = get_addon_version(init_path)
            new_addon.directory = root
            new_addon.link = True
                
            found_modules_paths.append(root)  






      