#type:ignore

import bpy
                
class ALINKER_AddonMainProps(bpy.types.PropertyGroup):
    
    addon_name : bpy.props.StringProperty(name="Addon Name", default="")
    addon_directory_path : bpy.props.StringProperty(name="Addon Directory Path", subtype='DIR_PATH')
 

  
    
    
    
    

    
    
