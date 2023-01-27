from .ul_addon_modules import ALINKER_UL_AddonModules

classes = (
    ALINKER_UL_AddonModules,
)

def register_ui_lists():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    

def unregister_ui_lists():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)