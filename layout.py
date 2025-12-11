# ============================================================================
# FILE: layout.py
# ============================================================================

import tkinter as tk
from ui import *


class MainLayout:
    """Handles all UI layout construction for the application"""
    
    def __init__(self, root, on_search_callback):
        self.root = root
        self.on_search_callback = on_search_callback
        
        # UI component references
        self.sidebar = None
        self.sidebar_buttons = {}
        self.content_frame = None
        self.scroll_frame = None
        
        self.setup_window()
        self.create_layout()
    
    def setup_window(self):
        """Configure the main window"""
        self.root.title("Unified Control Panel")
        self.root.geometry("1200x800")
        self.root.configure(bg=UITheme.BG_DARK)
        
        # Try to set icon
        try:
            self.root.iconbitmap('default')
        except:
            pass
    
    def create_layout(self):
        """Create the complete UI layout"""
        self.create_header()
        self.create_main_container()
    
    def create_header(self):
        """Create the header with title and search bar"""
        header = tk.Frame(self.root, bg=UITheme.BG_DARKER, height=80)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)
        
        title = tk.Label(
            header,
            text="⚙️ Unified Control Panel",
            font=("Segoe UI", 20, "bold"),
            bg=UITheme.BG_DARKER,
            fg=UITheme.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT, padx=20, pady=20)
        
        version = tk.Label(
            header,
            text="v2.0 Modular",
            font=("Segoe UI", 9),
            bg=UITheme.BG_DARKER,
            fg=UITheme.TEXT_SECONDARY
        )
        version.pack(side=tk.LEFT, padx=5, pady=20)
        
        # Search bar
        search_bar = SearchBar(header, on_search=self.on_search_callback)
        search_bar.pack(side=tk.RIGHT, padx=20)
    
    def create_main_container(self):
        """Create the main container with sidebar and content area"""
        main_container = tk.Frame(self.root, bg=UITheme.BG_DARK)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Sidebar
        self.sidebar = self.create_sidebar(main_container)
        
        # Content area
        self.scroll_frame = ScrollableFrame(main_container)
        self.scroll_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.content_frame = self.scroll_frame.get_frame()
    
    def create_sidebar(self, parent):
        """Create the category sidebar"""
        sidebar = tk.Frame(parent, bg=UITheme.BG_DARKER, width=250)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))
        sidebar.pack_propagate(False)
        
        sidebar_title = tk.Label(
            sidebar,
            text="CATEGORIES",
            font=("Segoe UI", 9, "bold"),
            bg=UITheme.BG_DARKER,
            fg=UITheme.TEXT_SECONDARY
        )
        sidebar_title.pack(pady=(10, 15), padx=20, anchor="w")
        
        return sidebar
    
    def add_sidebar_button(self, module_name, module_icon, command):
        """Add a button to the sidebar"""
        btn = SidebarButton(
            self.sidebar,
            text=f"{module_icon} {module_name}",
            command=command
        )
        btn.pack(fill=tk.X, pady=2, padx=5)
        self.sidebar_buttons[module_name] = btn
        return btn
    
    def set_active_sidebar_button(self, module_name):
        """Update sidebar button states to show active module"""
        for name, btn in self.sidebar_buttons.items():
            btn.set_active(name == module_name)
    
    def clear_content(self):
        """Clear all widgets from the content area"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def create_module_header(self, module_icon, module_name, settings_count):
        """Create a header for a module view"""
        header = tk.Frame(self.content_frame, bg=UITheme.BG_DARK)
        header.pack(fill=tk.X, pady=(0, 20))
        
        title = tk.Label(
            header,
            text=f"{module_icon} {module_name}",
            font=("Segoe UI", 24, "bold"),
            bg=UITheme.BG_DARK,
            fg=UITheme.TEXT_PRIMARY
        )
        title.pack(anchor="w")
        
        subtitle = tk.Label(
            header,
            text=f"{settings_count} settings available",
            font=("Segoe UI", 10),
            bg=UITheme.BG_DARK,
            fg=UITheme.TEXT_SECONDARY
        )
        subtitle.pack(anchor="w", pady=(5, 0))
        
        return header
    
    def create_search_header(self, query):
        """Create a header for search results"""
        header_frame = tk.Frame(self.content_frame, bg=UITheme.BG_DARK)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        header = tk.Label(
            header_frame,
            text=f"🔍 Search results for: \"{query}\"",
            font=("Segoe UI", 20, "bold"),
            bg=UITheme.BG_DARK,
            fg=UITheme.TEXT_PRIMARY
        )
        header.pack(anchor="w")
        
        return header_frame
    
    def show_no_results_message(self):
        """Display a 'no results found' message"""
        no_results = tk.Label(
            self.content_frame,
            text="No settings found matching your search",
            font=("Segoe UI", 14),
            bg=UITheme.BG_DARK,
            fg=UITheme.TEXT_SECONDARY
        )
        no_results.pack(pady=50)
    
    def add_setting_card(self, card):
        """Add a setting card to the content area"""
        card.pack(fill=tk.X, pady=5)
    
    def get_content_frame(self):
        """Get the content frame for direct widget manipulation"""
        return self.content_frame
