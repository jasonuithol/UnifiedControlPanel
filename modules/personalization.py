# ============================================================================
# FILE: modules/personalization.py
# ============================================================================

from .base_module import *

class PersonalizationModule(BaseModule):
    """Personalization settings module"""
    
    def get_name(self) -> str:
        return "Personalization"
    
    def get_icon(self) -> str:
        return "🎨"
    
    def get_color(self) -> str:
        return "#ec4899"
    
    def get_settings(self) -> List[ModuleSetting]:
        return [
            ModuleSetting("Personalization", "Customize Windows", "ms-settings:personalization"),
            ModuleSetting("Background", "Change wallpaper", "ms-settings:personalization-background"),
            ModuleSetting("Colors", "Accent colors and themes", "ms-settings:colors"),
            ModuleSetting("Lock Screen", "Lock screen settings", "ms-settings:lockscreen"),
            ModuleSetting("Taskbar", "Taskbar preferences", "ms-settings:taskbar"),
        ]

