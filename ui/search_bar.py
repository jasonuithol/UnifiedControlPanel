import tkinter as tk
from typing import Callable
from theme import Theme


class SearchBar(tk.Frame):
    """Search bar widget"""
    
    def __init__(self, parent, on_search: Callable, **kwargs):
        super().__init__(parent, bg=Theme.BG_DARKER, **kwargs)
        
        tk.Label(
            self,
            text="🔍",
            bg=Theme.BG_DARKER,
            font=Theme.FONT_SEARCH_BAR
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        self.search_var = tk.StringVar()
        self.search_var.trace_add('write', lambda *args: on_search(self.search_var.get()))
        
        self.entry = tk.Entry(
            self,
            textvariable=self.search_var,
            font=Theme.FONT_SEARCH_BAR,
            width=30,
            bg=Theme.BG_CARD,
            fg=Theme.TEXT_PRIMARY,
            insertbackground=Theme.TEXT_PRIMARY,
            relief=tk.FLAT,
            bd=0
        )
        self.entry.pack(pady=Theme.SEARCH_BAR_PADDING_Y, 
                       ipady=Theme.SEARCH_BAR_PADDING_Y, 
                       padx=Theme.SEARCH_BAR_PADDING_X)
