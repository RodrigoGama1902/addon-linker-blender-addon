

def draw_preferences(self, context):
    
    layout = self.layout
    layout.use_property_split = True
    
    box = layout.box()
    box.prop(self, "auto_get_addon_name")
    box.prop(self, "get_addon_name_mode")