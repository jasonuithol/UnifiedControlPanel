# ============================================================================
# FILE: modules/base_module.py
# ============================================================================

from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ModuleSetting:
    """Represents a single setting within a module"""
    
    def __init__(self, name: str, description: str, command: str):
        self.name = name
        self.description = description
        self.command = command


class BaseModule(ABC):
    """Base class for all control panel modules"""
    
    def __init__(self):
        self.name: str = ""
        self.icon: str = ""
        self.color: str = ""
        self.settings: List[ModuleSetting] = []
    
    @abstractmethod
    def get_name(self) -> str:
        """Return the module name"""
        pass
    
    @abstractmethod
    def get_icon(self) -> str:
        """Return the module icon (emoji)"""
        pass
    
    @abstractmethod
    def get_color(self) -> str:
        """Return the module color"""
        pass
    
    @abstractmethod
    def get_settings(self) -> List[ModuleSetting]:
        """Return list of settings for this module"""
        pass
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert module to dictionary format"""
        return {
            "icon": self.get_icon(),
            "color": self.get_color(),
            "items": [
                {
                    "name": s.name,
                    "desc": s.description,
                    "cmd": s.command
                }
                for s in self.get_settings()
            ]
        }

