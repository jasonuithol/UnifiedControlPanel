# ============================================================================
# FILE: layout.py
# ============================================================================

import tkinter as tk
from ui import ScrollableFrame, SearchBar, SidebarButton
from theme import Theme
from typing import Optional


class MainLayout:
    """Handles all UI layout construction for the application"""
    
    def __init__(self, root, on_search_callback, zoom_manager=None):
        self.root = root
        self.on_search_callback = on_search_callback
        self.zoom_manager = zoom_manager
        
        # UI component references
        self.sidebar = None
        self.sidebar_buttons = {}
        self.content_frame = None
        self.scroll_frame = None
        
        self.setup_window()
        self.create_layout()
    
    def setup_window(self):
        """Configure the main window"""
        self.root.title(Theme.WINDOW_TITLE)
        self.root.geometry(f"{Theme.WINDOW_WIDTH}x{Theme.WINDOW_HEIGHT}")
        self.root.configure(bg=Theme.BG_DARK)
        
        # Try to set icon
        try:
            self.root.iconbitmap(Theme.WINDOW_ICON)
        except:
            pass
    
    def create_layout(self):
        """Create the complete UI layout"""
        self.create_header()
        self.create_main_container()
    
    def create_header(self):
        """Create the header with title and search bar"""
        header = tk.Frame(self.root, bg=Theme.BG_DARKER, height=Theme.HEADER_HEIGHT)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)
        
        title = tk.Label(
            header,
            text=Theme.APP_TITLE,
            font=Theme.FONT_TITLE,
            bg=Theme.BG_DARKER,
            fg=Theme.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT, padx=Theme.HEADER_PADDING_X, pady=Theme.HEADER_PADDING_Y)
        if self.zoom_manager:
            self.zoom_manager.register_widget(title, Theme.FONT_TITLE)
        
        version = tk.Label(
            header,
            text=Theme.APP_VERSION,
            font=Theme.FONT_VERSION,
            bg=Theme.BG_DARKER,
            fg=Theme.TEXT_SECONDARY
        )
        version.pack(side=tk.LEFT, padx=Theme.VERSION_PADDING_X, pady=Theme.HEADER_PADDING_Y)
        if self.zoom_manager:
            self.zoom_manager.register_widget(version, Theme.FONT_VERSION)
        
        # Search bar
        search_bar = SearchBar(header, on_search=self.on_search_callback)
        search_bar.pack(side=tk.RIGHT, padx=Theme.HEADER_PADDING_X)
    
    def create_main_container(self):
        """Create the main container with sidebar and content area"""
        main_container = tk.Frame(self.root, bg=Theme.BG_DARK)
        main_container.pack(fill=tk.BOTH, expand=True, 
                          padx=Theme.MAIN_CONTAINER_PADDING, 
                          pady=Theme.MAIN_CONTAINER_PADDING)
        
        # Sidebar
        self.sidebar = self.create_sidebar(main_container)
        
        # Content area
        self.scroll_frame = ScrollableFrame(main_container)
        self.scroll_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.content_frame = self.scroll_frame.get_frame()
    
    def create_sidebar(self, parent):
        """Create the category sidebar"""
        sidebar = tk.Frame(parent, bg=Theme.BG_DARKER, width=Theme.SIDEBAR_WIDTH)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, Theme.SIDEBAR_PADDING_RIGHT))
        sidebar.pack_propagate(False)
        
        sidebar_title = tk.Label(
            sidebar,
            text=Theme.SIDEBAR_TITLE,
            font=Theme.FONT_CATEGORY,
            bg=Theme.BG_DARKER,
            fg=Theme.TEXT_SECONDARY
        )
        sidebar_title.pack(pady=Theme.SIDEBAR_TITLE_PADDING_Y, 
                          padx=Theme.SIDEBAR_TITLE_PADDING_X, 
                          anchor="w")
        if self.zoom_manager:
            self.zoom_manager.register_widget(sidebar_title, Theme.FONT_CATEGORY)
        
        return sidebar
    
    def add_sidebar_button(self, module_name, module_icon, command):
        """Add a button to the sidebar"""
        btn = SidebarButton(
            self.sidebar,
            text=f"{module_icon} {module_name}",
            command=command
        )
        btn.pack(fill=tk.X, 
                pady=Theme.SIDEBAR_BUTTON_PADDING_Y, 
                padx=Theme.SIDEBAR_BUTTON_PADDING_X)
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
        header = tk.Frame(self.content_frame, bg=Theme.BG_DARK)
        header.pack(fill=tk.X, pady=Theme.CONTENT_MODULE_HEADER_PADDING_Y)
        
        title = tk.Label(
            header,
            text=f"{module_icon} {module_name}",
            font=Theme.FONT_MODULE_HEADER,
            bg=Theme.BG_DARK,
            fg=Theme.TEXT_PRIMARY
        )
        title.pack(anchor="w")
        if self.zoom_manager:
            self.zoom_manager.register_widget(title, Theme.FONT_MODULE_HEADER)
        
        subtitle = tk.Label(
            header,
            text=Theme.settings_count_text(settings_count),
            font=Theme.FONT_MODULE_SUBTITLE,
            bg=Theme.BG_DARK,
            fg=Theme.TEXT_SECONDARY
        )
        subtitle.pack(anchor="w", pady=Theme.CONTENT_MODULE_SUBTITLE_PADDING_Y)
        if self.zoom_manager:
            self.zoom_manager.register_widget(subtitle, Theme.FONT_MODULE_SUBTITLE)
        
        return header
    
    def create_search_header(self, query):
        """Create a header for search results"""
        header_frame = tk.Frame(self.content_frame, bg=Theme.BG_DARK)
        header_frame.pack(fill=tk.X, pady=Theme.CONTENT_SEARCH_HEADER_PADDING_Y)
        
        header = tk.Label(
            header_frame,
            text=Theme.search_results_text(query),
            font=Theme.FONT_SEARCH_HEADER,
            bg=Theme.BG_DARK,
            fg=Theme.TEXT_PRIMARY
        )
        header.pack(anchor="w")
        if self.zoom_manager:
            self.zoom_manager.register_widget(header, Theme.FONT_SEARCH_HEADER)
        
        return header_frame
    
    def show_no_results_message(self):
        """Display a 'no results found' message"""
        no_results = tk.Label(
            self.content_frame,
            text=Theme.NO_RESULTS_MESSAGE,
            font=Theme.FONT_NO_RESULTS,
            bg=Theme.BG_DARK,
            fg=Theme.TEXT_SECONDARY
        )
        no_results.pack(pady=Theme.CONTENT_NO_RESULTS_PADDING_Y)
        if self.zoom_manager:
            self.zoom_manager.register_widget(no_results, Theme.FONT_NO_RESULTS)
    
    def add_setting_card(self, card):
        """Add a setting card to the content area"""
        card.pack(fill=tk.X, pady=Theme.CONTENT_CARD_PADDING_Y)
    
    def get_content_frame(self):
        """Get the content frame for direct widget manipulation"""
        return self.content_frame
