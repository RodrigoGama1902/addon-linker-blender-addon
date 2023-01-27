import bpy
import os

from ..utility.paths import get_addons_path


class ALINKER_OP_LinkAddons(bpy.types.Operator):
    """Base Operator Description"""

    bl_idname = "alinker.link_addons"
    bl_label = "Link Single Add-on"
    bl_options = {'REGISTER', 'UNDO'}
        
    @staticmethod
    def create_mklink(src : str, dst : str) -> None:
        '''Creates a MKlink from src to dst'''
        
        if not os.path.exists(src):
            print(f"SRC: {src} not found")
            return
        
        if os.path.exists(dst):
            print(f"{dst} already exists")
            return
        
        os.symlink(src, dst)
        print(f"Linked {src} to {dst}")
            
    def get_new_addon_path(self, addon_name):
        return os.path.join(get_addons_path(), addon_name)
    
    def draw(self, context):
        
        layout = self.layout
        props = context.scene.addon_linker
        
        box = layout.box()
        box.label(text="You are about to link the following add-ons:")
        
        col = layout.column(align=True)
        
        for addon_module in props.addons_to_link_list:
            
            box = col.box()
            box.scale_y = 0.9
            
            if addon_module.link:
                box.label(text=addon_module.name, icon = 'LINKED') 
        
    def invoke(self, context, event):
        
        props = context.scene.addon_linker
        addons_to_link = [addon_module for addon_module in props.addons_to_link_list if addon_module.link]
        
        if not addons_to_link:
            self.report({'ERROR'}, "No add-ons selected")
            return {'CANCELLED'}
        
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        
        props = context.scene.addon_linker
        
        for addon_module in props.addons_to_link_list:
            
            new_addon_path = self.get_new_addon_path(addon_module.name)
            
            if os.path.exists(new_addon_path):
                self.report({'ERROR'}, "Addon already exists: " + new_addon_path)
            
            try:
                self.create_mklink(addon_module.directory, new_addon_path)
            except OSError:
                self.report({'ERROR'}, "Permission denied, restart Blender as administrator")
     
        self.report({'INFO'},"Finished, restart Blender to load the add-on")
        return {'FINISHED'}

