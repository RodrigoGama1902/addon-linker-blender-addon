import bpy

from .utils.obj_panel import ObjPanel

class ALINKER_PT_MainPanel(ObjPanel, bpy.types.Panel):
    bl_label = "AddonLinker"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self,context):
        
        props = context.scene.addon_linker
        
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        
        row = layout.row()
        row.prop(props, "addon_directory_path")
        row = layout.row()
        row.prop(props, "addon_name")
               
        row = layout.row()
        op = row.operator("alinker.link_single_addon", text="Link Add-on", icon='LINKED')
        op.addon_name = props.addon_name
        op.original_addon_path = props.addon_directory_path
