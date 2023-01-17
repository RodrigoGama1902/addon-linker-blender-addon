import os

from ..utility.functions import get_prefs
from ..utility.parse_init_file import parse_init_file

def get_addon_name_from_directory(self, context):
    
    prefs = get_prefs()
    
    if not prefs.auto_get_addon_name:
        return None
    
    if not os.path.exists(self.addon_directory_path):
        return None
    
    if prefs.get_addon_name_mode == 'DIRECTORY_NAME':
        
        addon_name = os.path.dirname(self.addon_directory_path).split("\\")[-1]
        self.addon_name = addon_name
        return None
    
    if prefs.get_addon_name_mode == 'PREVIOUS_DIRECTORY_NAME':
        addon_name = os.path.dirname(self.addon_directory_path).split("\\")[-2]
        self.addon_name = addon_name
        return None
    
    if prefs.get_addon_name_mode == 'INIT_INFO':
        init_path = os.path.join(self.addon_directory_path, "__init__.py")
        
        if not os.path.exists(init_path):
            print("No __init__.py found")
            return None
        
        init_dict = parse_init_file(init_path)
        self.addon_name = init_dict["name"]



      