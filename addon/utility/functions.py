import bpy
import ctypes

from .constants import ADDON_NAME

def get_prefs():
    return bpy.context.preferences.addons[ADDON_NAME].preferences

def check_running_as_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False




