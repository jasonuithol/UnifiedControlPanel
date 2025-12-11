# ============================================================================
# FILE: general_ui.py
# ============================================================================

import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Dict, Any

class UITheme:
    """Color scheme and styling constants"""
    BG_DARK = "#1e293b"
    BG_DARKER = "#0f172a"
    BG_CARD = "#334155"
    BG_HOVER = "#475569"
    TEXT_PRIMARY = "#ffffff"
    TEXT_SECONDARY = "#94a3b8"
    
    # Category colors
    COLORS = {
        "blue": "#3b82f6",
        "green": "#10b981",
        "purple": "#8b5cf6",
        "pink": "#ec4899",
        "orange": "#f97316",
        "red": "#ef4444",
        "indigo": "#6366f1",
        "teal": "#14b8a6",
        "cyan": "#0ea5e9",
    }


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


class SettingCard(tk.Frame):
    """Card widget for displaying individual settings"""
    
    def __init__(self, parent, name: str, description: str, 
                 command: Callable, color: str, **kwargs):
        super().__init__(
            parent,
            bg=UITheme.BG_CARD,
            relief=tk.FLAT,
            bd=0,
            highlightthickness=1,
            highlightbackground=UITheme.BG_HOVER,
            **kwargs
        )
        
        self.color = color
        
        # Content container
        content = tk.Frame(self, bg=UITheme.BG_CARD)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # Left side - setting info
        left_frame = tk.Frame(content, bg=UITheme.BG_CARD)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.name_label = tk.Label(
            left_frame,
            text=name,
            font=("Segoe UI", 13, "bold"),
            bg=UITheme.BG_CARD,
            fg=UITheme.TEXT_PRIMARY,
            anchor="w"
        )
        self.name_label.pack(anchor="w")
        
        self.desc_label = tk.Label(
            left_frame,
            text=description,
            font=("Segoe UI", 9),
            bg=UITheme.BG_CARD,
            fg=UITheme.TEXT_SECONDARY,
            anchor="w"
        )
        self.desc_label.pack(anchor="w", pady=(2, 0))
        
        # Right side - action button
        self.action_btn = ModernButton(
            content,
            text="Open →",
            command=command,
            color=color
        )
        self.action_btn.pack(side=tk.RIGHT)
        
        # Store all widgets for hover effects
        self.widgets = [self, content, left_frame, self.name_label, self.desc_label]
        
        # Bind hover effects
        for widget in self.widgets:
            widget.bind("<Enter>", self._on_enter)
            widget.bind("<Leave>", self._on_leave)
    
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


class ScrollableFrame(tk.Frame):
    """Frame with scrollbar support"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg=UITheme.BG_DARK, **kwargs)
        
        # Create canvas and scrollbar
        self.canvas = tk.Canvas(
            self,
            bg=UITheme.BG_DARK,
            highlightthickness=0
        )
        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.canvas.yview
        )
        
        # Create the scrollable frame
        self.scrollable_frame = tk.Frame(self.canvas, bg=UITheme.BG_DARK)
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack scrollbar and canvas
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create window in canvas
        self.canvas_frame = self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw"
        )
        
        # Configure scrolling
        self.scrollable_frame.bind("<Configure>", self._configure_scroll)
        self.canvas.bind("<Configure>", self._configure_canvas)
        
        # Mouse wheel scrolling
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
    
    def _configure_scroll(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def _configure_canvas(self, event):
        self.canvas.itemconfig(self.canvas_frame, width=event.width)
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def get_frame(self) -> tk.Frame:
        """Get the inner scrollable frame"""
        return self.scrollable_frame


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
        