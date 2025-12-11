# ============================================================================
# FILE: zoom_manager.py
# ============================================================================

import tkinter as tk
from theme import Theme


class ZoomManager:
    """Manages font zoom/scaling for the entire application"""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.widgets_to_update = []
        
        # Bind Ctrl+MouseWheel globally
        self.root.bind_all("<Control-MouseWheel>", self._on_zoom)
        # Also support Ctrl+Plus and Ctrl+Minus
        self.root.bind_all("<Control-plus>", lambda e: self._zoom_in())
        self.root.bind_all("<Control-equal>", lambda e: self._zoom_in())  # + without shift
        self.root.bind_all("<Control-minus>", lambda e: self._zoom_out())
        self.root.bind_all("<Control-Key-0>", lambda e: self._reset_zoom())
    
    def register_widget(self, widget, base_font: tuple):
        """Register a widget to be updated when zoom changes"""
        self.widgets_to_update.append((widget, base_font))
    
    def register_multiple(self, widget_font_pairs: list):
        """Register multiple widgets at once"""
        for widget, font in widget_font_pairs:
            self.register_widget(widget, font)
    
    def _on_zoom(self, event):
        """Handle Ctrl+MouseWheel zoom"""
        if event.delta > 0:
            self._zoom_in()
        else:
            self._zoom_out()
    
    def _zoom_in(self):
        """Zoom in"""
        Theme.zoom_in()
        self._update_all_fonts()
        print(f"Zoom: {int(Theme.get_zoom_level() * 100)}%")
    
    def _zoom_out(self):
        """Zoom out"""
        Theme.zoom_out()
        self._update_all_fonts()
        print(f"Zoom: {int(Theme.get_zoom_level() * 100)}%")
    
    def _reset_zoom(self):
        """Reset zoom to 100%"""
        Theme.set_zoom_level(1.0)
        self._update_all_fonts()
        print("Zoom: 100% (reset)")
    
    def _update_all_fonts(self):
        """Update fonts for all registered widgets"""
        for widget, base_font in self.widgets_to_update:
            try:
                if widget.winfo_exists():
                    scaled_font = Theme.scale_font(base_font)
                    widget.configure(font=scaled_font)
            except tk.TclError:
                # Widget no longer exists
                pass
        
        # Clean up dead widgets
        self.widgets_to_update = [
            (w, f) for w, f in self.widgets_to_update 
            if self._widget_exists(w)
        ]
    
    def _widget_exists(self, widget):
        """Check if widget still exists"""
        try:
            return widget.winfo_exists()
        except tk.TclError:
            return False
