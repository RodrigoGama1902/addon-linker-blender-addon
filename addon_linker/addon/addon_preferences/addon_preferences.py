import bpy

from ..utility.constants import ADDON_NAME

from .draw_preferences import draw_preferences

class ALINKER_AddonPrefs(bpy.types.AddonPreferences):    
    bl_idname = ADDON_NAME
        
    get_addon_name_mode : bpy.props.EnumProperty(
        name="Get Addon Name Mode",
        default = 'ADDON_MODULE_NAME',
        items = [
            ('ADDON_MODULE_NAME', "Addon Module Name", "Get addon name from addon module name"),
            ('DIRECTORY_NAME', "Directory Name", "Get addon name from selected directory name"),      
            ('PREVIOUS_DIRECTORY_NAME', "Previous Directory Name", "Get addon name from previous directory name"),
            ('INIT_INFO', "Init Info", "Get addon name from __init__.py info"),
        ]
    ) #type:ignore
    
    delete_old_addon_directory_if_exists : bpy.props.BoolProperty(default = True,
                                                                  name = "Delete Old Add-on Directory If Exists",
                                                                  description = "When linking new add-ons, Automatically remove old addon modules if exists") #type:ignore
    
    auto_restart_blender : bpy.props.BoolProperty(
        default = True, 
        description="Automatically restart Blender after linking add-ons",
        name = "Auto Restart Blender") #type:ignore
    
    auto_activate_addons : bpy.props.BoolProperty(
        default = True, 
        description="Automatically activate add-ons after restarting Blender",
        name = "Auto Activate Add-ons") #type:ignore
    
    auto_save_preferences : bpy.props.BoolProperty(
        default = True, 
        description="Automatically save preferences after restarting Blender",
        name = "Auto Save Preferences") #type:ignore

    def draw(self, context):
        draw_preferences(self, context)
        


              
            
            

            
            
 
            
            