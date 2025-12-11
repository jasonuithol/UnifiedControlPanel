import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Dict, Any

from .ui_theme import *

class SettingCard(tk.Frame):
    """Card widget for displaying individual settings - click anywhere to open"""
    
    def __init__(self, parent, name: str, description: str, 
                 command: Callable, color: str, **kwargs):
        super().__init__(
            parent,
            bg=UITheme.BG_CARD,
            relief=tk.FLAT,
            bd=0,
            highlightthickness=1,
            highlightbackground=UITheme.BG_HOVER,
            cursor="hand2",
            **kwargs
        )
        
        self.color = color
        self.command = command
        
        # Content container
        content = tk.Frame(self, bg=UITheme.BG_CARD, cursor="hand2")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # Setting info
        info_frame = tk.Frame(content, bg=UITheme.BG_CARD, cursor="hand2")
        info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.name_label = tk.Label(
            info_frame,
            text=name,
            font=("Segoe UI", 13, "bold"),
            bg=UITheme.BG_CARD,
            fg=UITheme.TEXT_PRIMARY,
            anchor="w",
            cursor="hand2"
        )
        self.name_label.pack(anchor="w")
        
        self.desc_label = tk.Label(
            info_frame,
            text=description,
            font=("Segoe UI", 9),
            bg=UITheme.BG_CARD,
            fg=UITheme.TEXT_SECONDARY,
            anchor="w",
            cursor="hand2"
        )
        self.desc_label.pack(anchor="w", pady=(2, 0))
        
        # Arrow indicator on the right
        arrow_label = tk.Label(
            content,
            text="→",
            font=("Segoe UI", 16),
            bg=UITheme.BG_CARD,
            fg=color,
            cursor="hand2"
        )
        arrow_label.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Store all widgets for hover effects and clicks
        self.widgets = [self, content, info_frame, self.name_label, self.desc_label, arrow_label]
        
        # Bind hover effects and clicks to all widgets
        for widget in self.widgets:
            widget.bind("<Enter>", self._on_enter)
            widget.bind("<Leave>", self._on_leave)
            widget.bind("<Button-1>", self._on_click)
    
    def _on_click(self, event):
        """Handle click event"""
        self.command()
    
    def _on_enter(self, event):
        self.configure(bg=UITheme.BG_HOVER, highlightbackground=self.color)
        for widget in self.widgets:
            if isinstance(widget, tk.Frame) or isinstance(widget, tk.Label):
                widget.configure(bg=UITheme.BG_HOVER)
    
    def _on_leave(self, event):
        self.configure(bg=UITheme.BG_CARD, highlightbackground=UITheme.BG_HOVER)
        for widget in self.widgets:
            if isinstance(widget, tk.Frame) or isinstance(widget, tk.Label):
                widget.configure(bg=UITheme.BG_CARD)