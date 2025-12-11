import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Dict, Any

from .ui_theme import *

class ModernButton(tk.Button):
    """Modern styled button with hover effects"""
    
    def __init__(self, parent, text: str, command: Callable, 
                 color: str = UITheme.COLORS["blue"], **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 10, "bold"),
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            relief=tk.FLAT,
            cursor="hand2",
            bd=0,
            padx=20,
            pady=8,
            **kwargs
        )
