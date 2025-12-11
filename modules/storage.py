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
            ModuleSetting("Disk Management", "Partition and format drives", "diskmgmt.msc"),
            ModuleSetting("Storage Settings", "Manage disk space", "ms-settings:storagesense"),
        ]
