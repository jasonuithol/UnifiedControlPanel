# ============================================================================
# FILE: modules/system.py
# ============================================================================

from .base_module import *

class SystemModule(BaseModule):
    """System settings module"""
    
    def get_name(self) -> str:
        return "System"
    
    def get_icon(self) -> str:
        return "💻"
    
    def get_color(self) -> str:
        return "#3b82f6"
    
    def get_settings(self) -> List[ModuleSetting]:
        return [
            ModuleSetting("System Information", "View detailed system specs", "msinfo32"),
            ModuleSetting("Display Settings", "Screen resolution and scaling", "desk.cpl"),
            ModuleSetting("Power Options", "Manage power plans", "powercfg.cpl"),
            ModuleSetting("Advanced System", "System properties", "sysdm.cpl"),
            ModuleSetting("Device Manager", "Manage hardware devices", "devmgmt.msc"),
            ModuleSetting("Disk Cleanup", "Free up disk space", "cleanmgr"),
            ModuleSetting("Performance Monitor", "Monitor system performance", "perfmon"),
        ]

