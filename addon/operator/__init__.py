

from .op_link_addons import ALINKER_OP_LinkAddons


classes = (
    ALINKER_OP_LinkAddons,
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)