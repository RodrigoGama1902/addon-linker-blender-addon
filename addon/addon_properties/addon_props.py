#type:ignore

import bpy

from .update import get_addon_name_from_directory
                
class ALINKER_AddonMainProps(bpy.types.PropertyGroup):
    
    addon_name : bpy.props.StringProperty(name="Addon Name", default="")
    addon_directory_path : bpy.props.StringProperty(name="Addon Directory Path",
                                                    subtype='DIR_PATH',
                                                    update = get_addon_name_from_directory)
 

  
    
    
    
    

    
    
