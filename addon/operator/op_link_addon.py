import bpy
import os

from ..utility.paths import get_addons_path


class ALINKER_OP_LinkSingleAddon(bpy.types.Operator):
    """Base Operator Description"""

    bl_idname = "alinker.link_single_addon"
    bl_label = "Link Single Add-on"
    bl_options = {'REGISTER', 'UNDO'}
    
    addon_name : bpy.props.StringProperty(name="Addon Name", default="") #type:ignore
    original_addon_path : bpy.props.StringProperty(name="Addon Directory Path", subtype='DIR_PATH') #type:ignore
    
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
        return os.path.join(get_addons_path(), self.addon_name)

    def execute(self, context):
        
        if not self.original_addon_path:
            self.report({'ERROR'}, "No addon directory path specified")
            return {'CANCELLED'}

        if not os.path.isdir(self.original_addon_path):
            self.report({'ERROR'}, "Addon directory path is not a directory")
            return {'CANCELLED'}
        
        try:
            self.create_mklink(self.original_addon_path, self.get_new_addon_path(self.addon_name))
        except OSError:
            self.report({'ERROR'}, "Permission denied, restart Blender as administrator")
            return {'CANCELLED'}
     
        self.report({'INFO'},"FINISHED")
        return {'FINISHED'}

