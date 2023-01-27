#type:ignore

import bpy

from .update import search_for_addons_modules

class ALINKER_AddonToLink(bpy.types.PropertyGroup):
    
    name : bpy.props.StringProperty(name="Addon Name", default="")
    directory : bpy.props.StringProperty(name="Addon Directory Path", subtype='DIR_PATH')
    version : bpy.props.StringProperty(name="Addon Version", default="")
    link : bpy.props.BoolProperty(name="Link", default=True)
                
class ALINKER_AddonMainProps(bpy.types.PropertyGroup):
    
    addon_name : bpy.props.StringProperty(name="Addon Name", default="")
    addon_directory_path : bpy.props.StringProperty(name="Addon Directory Path",
                                                    subtype='DIR_PATH',
                                                    update = search_for_addons_modules)
    
    addons_to_link_list : bpy.props.CollectionProperty(type=ALINKER_AddonToLink)
    addons_to_link_list_custom_index : bpy.props.IntProperty(name="Index for the custom list", default=0)
 

  
    
    
    
    

    
    
