import bpy

from .constants import ADDON_NAME

def get_prefs():
    return bpy.context.preferences.addons[ADDON_NAME].preferences


