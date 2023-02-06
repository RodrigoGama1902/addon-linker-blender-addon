import bpy
import os
import ctypes

from ..utility.paths import get_addons_path
from ..utility.functions import check_running_as_admin, get_prefs


class ALINKER_OP_LinkAddons(bpy.types.Operator):
    """Base Operator Description"""

    bl_idname = "alinker.link_addons"
    bl_label = "Link Add-ons"
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
            if addon_module.link:
                
                box = col.box()
                box.scale_y = 0.9
            
                box.label(text=addon_module.name, icon = 'LINKED') 
        
    def invoke(self, context, event):
        
        props = context.scene.addon_linker
        addons_to_link = [addon_module for addon_module in props.addons_to_link_list if addon_module.link]
        
        if not addons_to_link:
            self.report({'ERROR'}, "No add-ons selected")
            return {'CANCELLED'}
        
        return context.window_manager.invoke_props_dialog(self)
    
    def restart_blender_process(self):
                
        ctypes.windll.shell32.ShellExecuteW(None, "runas", bpy.app.binary_path, "", None, 1)
        bpy.ops.wm.quit_blender()

    def execute(self, context):
        
        props = context.scene.addon_linker
        prefs = get_prefs()
        
        if not check_running_as_admin():
            self.report({'ERROR'}, "Run Blender as administrator")
            return {'CANCELLED'}
        
        for addon_module in props.addons_to_link_list:
                        
            if not addon_module.link:
                continue
            
            new_addon_path = self.get_new_addon_path(addon_module.name)
            
            if os.path.exists(new_addon_path):
                
                if not prefs.delete_old_addon_directory_if_exists:
                    self.report({'ERROR'}, "Addon module already exists, ignoring: " + new_addon_path)
                    continue
                                
                try:
                    os.remove(new_addon_path)
                except PermissionError:
                    self.report({'ERROR'}, "PermissionError: Add-on module already exists and could not be automatically removed, please remove the add-on and try again: " + addon_module.name)
                    continue

            self.create_mklink(addon_module.directory, new_addon_path)
        
        if prefs.auto_restart_blender:
            self.restart_blender_process()

        self.report({'INFO'},"Finished, restart Blender to load the add-on")
        return {'FINISHED'}

