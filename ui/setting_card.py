import tkinter as tk
from typing import Callable
from theme import Theme


class SettingCard(tk.Frame):
    """Card widget for displaying individual settings - click anywhere to open"""
    
    def __init__(self, parent, name: str, description: str, 
                 command: Callable, color: str, **kwargs):
        super().__init__(
            parent,
            bg=Theme.BG_CARD,
            relief=tk.FLAT,
            bd=0,
            highlightthickness=1,
            highlightbackground=Theme.BG_CARD_HOVER,
            cursor=Theme.BUTTON_CURSOR,
            **kwargs
        )
        
        self.color = color
        self.command = command
        
        # Content container
        content = tk.Frame(self, bg=Theme.BG_CARD, cursor=Theme.BUTTON_CURSOR)
        content.pack(fill=tk.BOTH, expand=True, 
                    padx=Theme.CARD_PADDING_X, 
                    pady=Theme.CARD_PADDING_Y)
        
        # Setting info
        info_frame = tk.Frame(content, bg=Theme.BG_CARD, cursor=Theme.BUTTON_CURSOR)
        info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.name_label = tk.Label(
            info_frame,
            text=name,
            font=Theme.FONT_CARD_NAME,
            bg=Theme.BG_CARD,
            fg=Theme.TEXT_PRIMARY,
            anchor="w",
            cursor=Theme.BUTTON_CURSOR
        )
        self.name_label.pack(anchor="w")
        
        self.desc_label = tk.Label(
            info_frame,
            text=description,
            font=Theme.FONT_CARD_DESCRIPTION,
            bg=Theme.BG_CARD,
            fg=Theme.TEXT_SECONDARY,
            anchor="w",
            cursor=Theme.BUTTON_CURSOR
        )
        self.desc_label.pack(anchor="w", pady=(2, 0))
        
        # Arrow indicator on the right
        arrow_label = tk.Label(
            content,
            text="→",
            font=("Segoe UI", 16),
            bg=Theme.BG_CARD,
            fg=color,
            cursor=Theme.BUTTON_CURSOR
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
        self.configure(bg=Theme.BG_CARD_HOVER, highlightbackground=self.color)
        for widget in self.widgets:
            if isinstance(widget, (tk.Frame, tk.Label)):
                widget.configure(bg=Theme.BG_CARD_HOVER)
    
    def _on_leave(self, event):
        self.configure(bg=Theme.BG_CARD, highlightbackground=Theme.BG_CARD_HOVER)
        for widget in self.widgets:
            if isinstance(widget, (tk.Frame, tk.Label)):
                widget.configure(bg=Theme.BG_CARD)
