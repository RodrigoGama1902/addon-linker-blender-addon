import bpy

class ALINKER_UL_AddonModules(bpy.types.UIList):
        
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        
        row = layout.row()
        
        row.prop(item, "link", text="", emboss=True)
        row.prop(item, "name", text="", emboss=True)
        row.prop(item, "version", text="", emboss=False)

                
