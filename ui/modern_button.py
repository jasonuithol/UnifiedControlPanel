import tkinter as tk
from typing import Callable
from theme import Theme


class ModernButton(tk.Button):
    """Modern styled button with hover effects"""
    
    def __init__(self, parent, text: str, command: Callable, 
                 color: str = Theme.ACCENT_BLUE, **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            font=Theme.FONT_BUTTON,
            bg=color,
            fg=Theme.TEXT_PRIMARY,
            activebackground=color,
            activeforeground=Theme.TEXT_PRIMARY,
            relief=tk.FLAT,
            cursor=Theme.BUTTON_CURSOR,
            bd=Theme.BUTTON_BORDER_WIDTH,
            padx=Theme.BUTTON_PADDING_X,
            pady=Theme.BUTTON_PADDING_Y,
            **kwargs
        )
