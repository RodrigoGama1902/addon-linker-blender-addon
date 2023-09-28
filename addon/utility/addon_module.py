import os
import ast

from ..utility.functions import get_prefs

def adjust_line(line):
    return line.rstrip().strip(" ") 

def parse_init_file(filepath) -> dict:

    print("Parsing init file: " + filepath)
    
    dict_lines = []
    
    with open(filepath, 'r') as file:
        lines = file.readlines()

        add_lines = False
        
        for line in lines:

            if add_lines:
                if "#" in line: # Remove comments
                    line = line.split("#")[0]
                dict_lines.append(adjust_line(line))
            
            if "bl_info={" in line.replace(" ", ""):
                start_dict_line = adjust_line("{" + line.split("{")[1])
                print(start_dict_line)
                dict_lines.append(adjust_line(start_dict_line))
                add_lines = True
            if "}" in line and add_lines:
                add_lines = False
                break

    dict_string = "".join(dict_lines)
    return ast.literal_eval(dict_string)
    
def get_addon_module_name(init_path):
    
    addon_directory = os.path.dirname(init_path)
    prefs = get_prefs()

    if prefs.get_addon_name_mode == 'DIRECTORY_NAME':
        
        addon_name = os.path.dirname(addon_directory).split("\\")[-1]
        return addon_name
    
    if prefs.get_addon_name_mode == 'PREVIOUS_DIRECTORY_NAME':
        
        addon_name = os.path.dirname(addon_directory).split("\\")[-2]
        return addon_name
    
    if prefs.get_addon_name_mode == 'INIT_INFO':
        
        init_dict = parse_init_file(init_path)
        return init_dict["name"]

def get_addon_version(init_path) -> str:
    
    init_dict = parse_init_file(init_path)
    
    version_string = "v " + str(init_dict["version"]).replace("(", "").replace(")", "").replace(",", ".").replace(" ", "")
    
    return version_string

    
    