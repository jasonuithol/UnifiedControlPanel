import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Dict, Any

from .ui_theme import *

class SearchBar(tk.Frame):
    """Search bar widget"""
    
    def __init__(self, parent, on_search: Callable, **kwargs):
        super().__init__(parent, bg=UITheme.BG_DARKER, **kwargs)
        
        tk.Label(
            self,
            text="🔍",
            bg=UITheme.BG_DARKER,
            font=("Segoe UI", 12)
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        self.search_var = tk.StringVar()
        self.search_var.trace('w', lambda *args: on_search(self.search_var.get()))
        
        self.entry = tk.Entry(
            self,
            textvariable=self.search_var,
            font=("Segoe UI", 11),
            width=30,
            bg=UITheme.BG_CARD,
            fg=UITheme.TEXT_PRIMARY,
            insertbackground=UITheme.TEXT_PRIMARY,
            relief=tk.FLAT,
            bd=0
        )
        self.entry.pack(pady=20, ipady=8, padx=5)

