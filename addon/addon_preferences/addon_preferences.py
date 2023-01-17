import bpy

from ..utility.constants import ADDON_NAME

from .draw_preferences import draw_preferences

class ALINKER_AddonPrefs(bpy.types.AddonPreferences):    
    bl_idname = ADDON_NAME

    def draw(self, context):
        draw_preferences(self, context)
        


              
            
            

            
            
 
            
            