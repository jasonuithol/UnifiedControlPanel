# ============================================================================
# FILE: modules/storage.py
# ============================================================================

from .base_module import *

class StorageModule(BaseModule):
    """Storage management module"""
    
    def get_name(self) -> str:
        return "Storage"
    
    def get_icon(self) -> str:
        return "💾"
    
    def get_color(self) -> str:
        return "#0ea5e9"
    
    def get_settings(self) -> List[ModuleSetting]:
        return [
            ModuleSetting("Disk Cleanup", "Free up disk space", "cleanmgr"),
            ModuleSetting("Disk Management", "Partition and format drives", "diskmgmt.msc"),
            ModuleSetting("Storage Settings", "Manage disk space", "ms-settings:storagesense"),
            ModuleSetting("Recycle Bin", "View and manage deleted files", "shell:RecycleBinFolder"),
            ModuleSetting("Downloads", "View and manage downloaded files", "shell:Downloads"),
            ModuleSetting("App Data", "View and manage application data files", "shell:AppData"),
            ModuleSetting("Temp Files (User)", "Open user temporary files folder", "shell:Local AppData\\Temp"),
        ]
