# ============================================================================
# FILE: modules/devices.py
# ============================================================================

from .base_module import *

class DevicesModule(BaseModule):
    """Devices settings module"""
    
    def get_name(self) -> str:
        return "Devices"
    
    def get_icon(self) -> str:
        return "🖨️"
    
    def get_color(self) -> str:
        return "#8b5cf6"
    
    def get_settings(self) -> List[ModuleSetting]:
        return [
            ModuleSetting("Bluetooth", "Manage Bluetooth devices", "ms-settings:bluetooth"),
            ModuleSetting("Printers", "Add and manage printers", "ms-settings:printers"),
            ModuleSetting("Mouse Settings", "Configure mouse", "main.cpl"),
            ModuleSetting("Sound Settings", "Audio devices and volume", "mmsys.cpl"),
        ]
