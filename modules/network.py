# ============================================================================
# FILE: modules/network.py
# ============================================================================

from .base_module import *

class NetworkModule(BaseModule):
    """Network settings module"""
    
    def get_name(self) -> str:
        return "Network"
    
    def get_icon(self) -> str:
        return "🌐"
    
    def get_color(self) -> str:
        return "#10b981"
    
    def get_settings(self) -> List[ModuleSetting]:
        return [
            ModuleSetting("Network Connections", "View all network adapters", "ncpa.cpl"),
            ModuleSetting("Network Status", "Check connection status", "ms-settings:network-status"),
            ModuleSetting("Wi-Fi Settings", "Manage wireless networks", "ms-settings:network-wifi"),
            ModuleSetting("Firewall", "Windows Firewall settings", "firewall.cpl"),
            ModuleSetting("Internet Options", "Browser and proxy settings", "inetcpl.cpl"),
        ]

