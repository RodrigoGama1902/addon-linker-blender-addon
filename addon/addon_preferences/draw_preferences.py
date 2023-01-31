

def draw_preferences(self, context):
    
    layout = self.layout
    layout.use_property_split = True
    
    box = layout.box()
    box.prop(self, "get_addon_name_mode")
    box.prop(self, "delete_old_addon_directory_if_exists")
