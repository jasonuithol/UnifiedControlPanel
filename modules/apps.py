# ============================================================================
# FILE: modules/apps.py
# ============================================================================

from .base_module import *

class AppsModule(BaseModule):
    """Apps management module"""

    def get_name(self) -> str:
        return "Apps"
    
    def get_icon(self) -> str:
        return "📦"
    
    def get_color(self) -> str:
        return "#6366f1"
    
    def get_settings(self) -> List[ModuleSetting]:
        return [
            ModuleSetting("Apps & Features", "Install/uninstall apps", "ms-settings:appsfeatures"),
            ModuleSetting("Default Apps", "Set default programs", "ms-settings:defaultapps"),
            ModuleSetting("Startup Apps", "Manage startup programs", "ms-settings:startupapps"),
            ModuleSetting("Programs & Features", "Classic program list", "appwiz.cpl"),
        ]