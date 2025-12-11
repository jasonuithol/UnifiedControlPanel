import tkinter as tk
from tkinter import ttk
from theme import Theme


class ScrollableFrame(tk.Frame):
    """Frame with scrollbar support"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg=Theme.BG_DARK, **kwargs)
        
        # Create canvas and scrollbar
        self.canvas = tk.Canvas(
            self,
            bg=Theme.BG_DARK,
            highlightthickness=0
        )
        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.canvas.yview
        )
        
        # Create the scrollable frame
        self.scrollable_frame = tk.Frame(self.canvas, bg=Theme.BG_DARK)
        
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
