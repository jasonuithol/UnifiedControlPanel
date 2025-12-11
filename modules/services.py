
# ============================================================================
# FILE: modules/services.py
# ============================================================================

from .base_module import *

class ServicesModule(BaseModule):
    """Services management module"""
    
    def get_name(self) -> str:
        return "Services"
    
    def get_icon(self) -> str:
        return "⚙️"
    
    def get_color(self) -> str:
        return "#14b8a6"
    
    def get_settings(self) -> List[ModuleSetting]:
        return [
            ModuleSetting("Services", "Windows services", "services.msc"),
            ModuleSetting("Task Scheduler", "Scheduled tasks", "taskschd.msc"),
            ModuleSetting("Event Viewer", "System logs", "eventvwr.msc"),
            ModuleSetting("Registry Editor", "Edit registry (Advanced)", "regedit"),
            ModuleSetting("Task Manager", "Process manager", "taskmgr"),
        ]
