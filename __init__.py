bl_info = {
    "name": "AddonLinker",
    "description": "Link any add-on from directory",
    "author": "Rodrigo Gama",
    "version": (0, 1, 2, 1),
    "blender": (3, 3, 0),
    "location": "View3D",
    "category": "3D View"}


def register():
    from .addon.register import register_addon
    register_addon()


def unregister():
    from .addon.register import unregister_addon
    unregister_addon()