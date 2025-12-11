import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Dict, Any

from .ui_theme import *

class SidebarButton(tk.Button):
    """Sidebar navigation button with hover and active states"""
    
    def __init__(self, parent, text: str, command: Callable, **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 11),
            bg=UITheme.BG_CARD,
            fg=UITheme.TEXT_PRIMARY,
            activebackground=UITheme.BG_HOVER,
            activeforeground=UITheme.TEXT_PRIMARY,
            relief=tk.FLAT,
            anchor="w",
            padx=20,
            pady=12,
            cursor="hand2",
            bd=0,
            **kwargs
        )
        
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
    
    def _on_enter(self, event):
        if self['bg'] != UITheme.BG_HOVER:
            self.configure(bg=UITheme.BG_HOVER)
    
    def _on_leave(self, event):
        if not hasattr(self, 'is_active') or not self.is_active:
            self.configure(bg=UITheme.BG_CARD)
    
    def set_active(self, active: bool):
        self.is_active = active
        self.configure(bg=UITheme.BG_HOVER if active else UITheme.BG_CARD)