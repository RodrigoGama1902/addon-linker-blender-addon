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

