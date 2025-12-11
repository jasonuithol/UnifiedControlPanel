# ============================================================================
# FILE: modules/accounts.py
# ============================================================================

from .base_module import *

class AccountsModule(BaseModule):
    """User accounts module"""
    
    def get_name(self) -> str:
        return "Accounts"
    
    def get_icon(self) -> str:
        return "👤"
    
    def get_color(self) -> str:
        return "#f97316"
    
    def get_settings(self) -> List[ModuleSetting]:
        return [
            ModuleSetting("User Accounts", "Manage user accounts", "netplwiz"),
            ModuleSetting("Sign-in Options", "Password, PIN, biometrics", "ms-settings:signinoptions"),
            ModuleSetting("Family & Users", "Add other users", "ms-settings:otherusers"),
        ]
