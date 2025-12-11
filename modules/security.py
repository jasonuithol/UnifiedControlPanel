# ============================================================================
# FILE: modules/security.py
# ============================================================================

from .base_module import *

class SecurityModule(BaseModule):
    """Security settings module"""
    
    def get_name(self) -> str:
        return "Security"
    
    def get_icon(self) -> str:
        return "🛡️"
    
    def get_color(self) -> str:
        return "#ef4444"
    
    def get_settings(self) -> List[ModuleSetting]:
        return [
            ModuleSetting("Windows Security", "Virus & threat protection", "windowsdefender:"),
            ModuleSetting("Windows Update", "Check for updates", "ms-settings:windowsupdate"),
            ModuleSetting("Privacy Settings", "App permissions", "ms-settings:privacy"),
            ModuleSetting("Backup", "Backup settings", "ms-settings:backup"),
        ]
