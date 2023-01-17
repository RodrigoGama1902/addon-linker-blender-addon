

from .op_link_addon import ALINKER_OP_LinkSingleAddon


classes = (
    ALINKER_OP_LinkSingleAddon,
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)