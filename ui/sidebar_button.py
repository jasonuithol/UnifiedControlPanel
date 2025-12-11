import tkinter as tk
from typing import Callable
from theme import Theme


class SidebarButton(tk.Button):
    """Sidebar navigation button with hover and active states"""
    
    def __init__(self, parent, text: str, command: Callable, **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            font=Theme.FONT_SIDEBAR_BUTTON,
            bg=Theme.SIDEBAR_ACTIVE,
            fg=Theme.TEXT_PRIMARY,
            activebackground=Theme.SIDEBAR_HOVER,
            activeforeground=Theme.TEXT_PRIMARY,
            relief=tk.FLAT,
            anchor="w",
            padx=Theme.SIDEBAR_BUTTON_INTERNAL_PADDING_X,
            pady=Theme.SIDEBAR_BUTTON_INTERNAL_PADDING_Y,
            cursor=Theme.BUTTON_CURSOR,
            bd=0,
            **kwargs
        )
        
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
    
    def _on_enter(self, event):
        if self['bg'] != Theme.SIDEBAR_HOVER:
            self.configure(bg=Theme.SIDEBAR_HOVER)
    
    def _on_leave(self, event):
        if not hasattr(self, 'is_active') or not self.is_active:
            self.configure(bg=Theme.SIDEBAR_ACTIVE)
    
    def set_active(self, active: bool):
        self.is_active = active
        self.configure(bg=Theme.SIDEBAR_HOVER if active else Theme.SIDEBAR_ACTIVE)
