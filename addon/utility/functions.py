import bpy

from .constants import ADDON_NAME

def get_prefs() -> None:
    return bpy.context.preferences.addons[ADDON_NAME].preferences


