import bpy

from .addon_props import ALINKER_AddonMainProps

classes = (
    ALINKER_AddonMainProps,
)

def register_properties():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    
    bpy.types.Scene.addon_linker = bpy.props.PointerProperty(type= ALINKER_AddonMainProps)

def unregister_properties():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    
    del bpy.types.Scene.addon_linker