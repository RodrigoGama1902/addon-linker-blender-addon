import os
import bpy

def get_addons_path():
        
    scripts_folder = os.path.join(bpy.utils.resource_path('USER'), "scripts")
    
    if not os.path.exists(scripts_folder):
        os.mkdir(scripts_folder)

    addons_folder = os.path.join(scripts_folder, "addons")
    
    if not os.path.exists(addons_folder):
        os.mkdir(addons_folder)
    
    return addons_folder

def convert_to_absolute_path(path):
    
    if path.startswith("//"):
        return os.path.abspath(bpy.path.abspath(path))
    return path