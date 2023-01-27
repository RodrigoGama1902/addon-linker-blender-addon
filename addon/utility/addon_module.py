import os

from ..utility.functions import get_prefs
from ..utility.parse_init_file import parse_init_file

def get_addon_module_name(addon_directory):
    
    prefs = get_prefs()

    if prefs.get_addon_name_mode == 'DIRECTORY_NAME':
        
        addon_name = os.path.dirname(addon_directory).split("\\")[-1]
        return addon_name
    
    if prefs.get_addon_name_mode == 'PREVIOUS_DIRECTORY_NAME':
        
        addon_name = os.path.dirname(addon_directory).split("\\")[-2]
        return addon_name
    
    if prefs.get_addon_name_mode == 'INIT_INFO':
        
        init_path = os.path.join(addon_directory, "__init__.py")
        init_dict = parse_init_file(init_path)
        return init_dict["name"]
    
    