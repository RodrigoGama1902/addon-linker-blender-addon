import bpy

from .utils.obj_panel import ObjPanel

class ALINKER_PT_MainPanel(ObjPanel, bpy.types.Panel):
    bl_label = "AddonLinker"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self,context):
        
        props = context.scene.addon_linker
        
        layout = self.layout

        row = layout.row()
        row.use_property_split = True
        row.use_property_decorate = False
        row.prop(props, "addon_directory_path")
               
        row = layout.row()

        row.template_list("ALINKER_UL_AddonModules", 
                            "", 
                            props, 
                            "addons_to_link_list",
                            props,
                            "addons_to_link_list_custom_index",
                            rows=3)
        
        row = layout.row()
        row.scale_y = 1.5
        
        row.operator("alinker.link_single_addon", text="Addon Directory", icon='LINKED')
