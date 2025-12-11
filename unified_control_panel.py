"""
Unified Windows Control Panel
Python 3.14 with tkinter GUI
Consistent interface across all Windows versions

USAGE: python unified_control_panel.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import sys
from pathlib import Path
import json
import traceback

print("Starting Unified Control Panel...")
print(f"Python version: {sys.version}")

class UnifiedControlPanel:
    def __init__(self, root):
        print("Initializing UI...")
        self.root = root
        self.root.title("Unified Control Panel")
        self.root.geometry("1200x800")
        
        # Set icon if available
        try:
            self.root.iconbitmap('default')
        except:
            pass
        
        # Configure colors
        self.bg_dark = "#1e293b"
        self.bg_darker = "#0f172a"
        self.bg_card = "#334155"
        self.bg_hover = "#475569"
        self.text_color = "white"
        
        self.root.configure(bg=self.bg_dark)
        
        # Load configuration
        self.config_file = Path.home() / ".unified_control_panel" / "config.json"
        self.load_config()
        
        # Create main layout
        self.create_ui()
        
        print("UI initialized successfully!")
        
    def load_config(self):
        """Load or create configuration file"""
        try:
            self.config_file.parent.mkdir(exist_ok=True)
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            else:
                self.config = {"favorites": [], "theme": "dark"}
                self.save_config()
        except Exception as e:
            print(f"Config load error: {e}")
            self.config = {"favorites": [], "theme": "dark"}
    
    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Config save error: {e}")
    
    def create_ui(self):
        """Create the main user interface"""
        # Header
        header = tk.Frame(self.root, bg=self.bg_darker, height=80)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="⚙️ Unified Control Panel", 
                        font=("Segoe UI", 20, "bold"),
                        bg=self.bg_darker, fg=self.text_color)
        title.pack(side=tk.LEFT, padx=20, pady=20)
        
        # Version info
        version = tk.Label(header, text="v1.0", 
                          font=("Segoe UI", 9),
                          bg=self.bg_darker, fg="#94a3b8")
        version.pack(side=tk.LEFT, padx=5, pady=20)
        
        # Search bar
        search_frame = tk.Frame(header, bg=self.bg_darker)
        search_frame.pack(side=tk.RIGHT, padx=20)
        
        tk.Label(search_frame, text="🔍", bg=self.bg_darker, 
                font=("Segoe UI", 12)).pack(side=tk.LEFT, padx=(0,5))
        
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.on_search)
        
        search_entry = tk.Entry(search_frame, textvariable=self.search_var,
                               font=("Segoe UI", 11), width=30,
                               bg=self.bg_card, fg=self.text_color, 
                               insertbackground=self.text_color, 
                               relief=tk.FLAT, bd=0)
        search_entry.pack(pady=20, ipady=8, padx=5)
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.bg_dark)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Sidebar
        self.sidebar = tk.Frame(main_container, bg=self.bg_darker, width=250)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))
        self.sidebar.pack_propagate(False)
        
        sidebar_title = tk.Label(self.sidebar, text="CATEGORIES",
                                font=("Segoe UI", 9, "bold"),
                                bg=self.bg_darker, fg="#94a3b8")
        sidebar_title.pack(pady=(10, 15), padx=20, anchor="w")
        
        # Content area with canvas for scrolling
        content_container = tk.Frame(main_container, bg=self.bg_dark)
        content_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(content_container, bg=self.bg_dark, 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(content_container, orient="vertical", 
                                 command=canvas.yview)
        
        self.content_frame = tk.Frame(canvas, bg=self.bg_dark)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        canvas_frame = canvas.create_window((0, 0), window=self.content_frame, 
                                           anchor="nw")
        
        def configure_scroll(e):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(canvas_frame, width=e.width)
        
        self.content_frame.bind("<Configure>", configure_scroll)
        canvas.bind("<Configure>", configure_scroll)
        
        # Mouse wheel scrolling
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", on_mousewheel)
        
        # Define categories
        self.categories = self.get_categories()
        
        # Build sidebar
        self.build_sidebar()
        
        # Show default category
        self.show_category("System")
    
    def get_categories(self):
        """Define all control panel categories and their settings"""
        return {
            "System": {
                "icon": "💻",
                "color": "#3b82f6",
                "items": [
                    {"name": "System Information", "cmd": "msinfo32", "desc": "View detailed system specs"},
                    {"name": "Display Settings", "cmd": "desk.cpl", "desc": "Screen resolution and scaling"},
                    {"name": "Power Options", "cmd": "powercfg.cpl", "desc": "Manage power plans"},
                    {"name": "Advanced System", "cmd": "sysdm.cpl", "desc": "System properties"},
                    {"name": "Device Manager", "cmd": "devmgmt.msc", "desc": "Manage hardware devices"},
                    {"name": "Disk Cleanup", "cmd": "cleanmgr", "desc": "Free up disk space"},
                    {"name": "Performance Monitor", "cmd": "perfmon", "desc": "Monitor system performance"},
                ]
            },
            "Network": {
                "icon": "🌐",
                "color": "#10b981",
                "items": [
                    {"name": "Network Connections", "cmd": "ncpa.cpl", "desc": "View all network adapters"},
                    {"name": "Network Status", "cmd": "ms-settings:network-status", "desc": "Check connection status"},
                    {"name": "Wi-Fi Settings", "cmd": "ms-settings:network-wifi", "desc": "Manage wireless networks"},
                    {"name": "Firewall", "cmd": "firewall.cpl", "desc": "Windows Firewall settings"},
                    {"name": "Internet Options", "cmd": "inetcpl.cpl", "desc": "Browser and proxy settings"},
                ]
            },
            "Devices": {
                "icon": "🖨️",
                "color": "#8b5cf6",
                "items": [
                    {"name": "Bluetooth", "cmd": "ms-settings:bluetooth", "desc": "Manage Bluetooth devices"},
                    {"name": "Printers", "cmd": "ms-settings:printers", "desc": "Add and manage printers"},
                    {"name": "Mouse Settings", "cmd": "main.cpl", "desc": "Configure mouse"},
                    {"name": "Sound Settings", "cmd": "mmsys.cpl", "desc": "Audio devices and volume"},
                ]
            },
            "Personalization": {
                "icon": "🎨",
                "color": "#ec4899",
                "items": [
                    {"name": "Personalization", "cmd": "ms-settings:personalization", "desc": "Customize Windows"},
                    {"name": "Background", "cmd": "ms-settings:personalization-background", "desc": "Change wallpaper"},
                    {"name": "Colors", "cmd": "ms-settings:colors", "desc": "Accent colors and themes"},
                    {"name": "Lock Screen", "cmd": "ms-settings:lockscreen", "desc": "Lock screen settings"},
                    {"name": "Taskbar", "cmd": "ms-settings:taskbar", "desc": "Taskbar preferences"},
                ]
            },
            "Accounts": {
                "icon": "👤",
                "color": "#f97316",
                "items": [
                    {"name": "User Accounts", "cmd": "netplwiz", "desc": "Manage user accounts"},
                    {"name": "Sign-in Options", "cmd": "ms-settings:signinoptions", "desc": "Password, PIN, biometrics"},
                    {"name": "Family & Users", "cmd": "ms-settings:otherusers", "desc": "Add other users"},
                ]
            },
            "Security": {
                "icon": "🛡️",
                "color": "#ef4444",
                "items": [
                    {"name": "Windows Security", "cmd": "windowsdefender:", "desc": "Virus & threat protection"},
                    {"name": "Windows Update", "cmd": "ms-settings:windowsupdate", "desc": "Check for updates"},
                    {"name": "Privacy Settings", "cmd": "ms-settings:privacy", "desc": "App permissions"},
                    {"name": "Backup", "cmd": "ms-settings:backup", "desc": "Backup settings"},
                ]
            },
            "Apps": {
                "icon": "📦",
                "color": "#6366f1",
                "items": [
                    {"name": "Apps & Features", "cmd": "ms-settings:appsfeatures", "desc": "Install/uninstall apps"},
                    {"name": "Default Apps", "cmd": "ms-settings:defaultapps", "desc": "Set default programs"},
                    {"name": "Startup Apps", "cmd": "ms-settings:startupapps", "desc": "Manage startup programs"},
                    {"name": "Programs & Features", "cmd": "appwiz.cpl", "desc": "Classic program list"},
                ]
            },
            "Services": {
                "icon": "⚙️",
                "color": "#14b8a6",
                "items": [
                    {"name": "Services", "cmd": "services.msc", "desc": "Windows services"},
                    {"name": "Task Scheduler", "cmd": "taskschd.msc", "desc": "Scheduled tasks"},
                    {"name": "Event Viewer", "cmd": "eventvwr.msc", "desc": "System logs"},
                    {"name": "Registry Editor", "cmd": "regedit", "desc": "Edit registry (Advanced)"},
                    {"name": "Task Manager", "cmd": "taskmgr", "desc": "Process manager"},
                ]
            },
            "Storage": {
                "icon": "💾",
                "color": "#0ea5e9",
                "items": [
                    {"name": "Disk Management", "cmd": "diskmgmt.msc", "desc": "Partition and format drives"},
                    {"name": "Storage Settings", "cmd": "ms-settings:storagesense", "desc": "Manage disk space"},
                ]
            },
        }
    
    def build_sidebar(self):
        """Build the category sidebar"""
        self.category_buttons = {}
        
        for category_name, category_data in self.categories.items():
            btn = tk.Button(self.sidebar, 
                          text=f"{category_data['icon']}  {category_name}",
                          font=("Segoe UI", 11),
                          bg=self.bg_card, fg=self.text_color,
                          activebackground=self.bg_hover,
                          activeforeground=self.text_color,
                          relief=tk.FLAT,
                          anchor="w",
                          padx=20, pady=12,
                          cursor="hand2",
                          bd=0,
                          command=lambda cat=category_name: self.show_category(cat))
            btn.pack(fill=tk.X, pady=2, padx=5)
            
            self.category_buttons[category_name] = btn
            
            # Hover effect
            def on_enter(e, b=btn):
                if b['bg'] != "#475569":  # Don't change if active
                    b.configure(bg=self.bg_hover)
            def on_leave(e, b=btn, name=category_name):
                if hasattr(self, 'active_category') and self.active_category == name:
                    b.configure(bg=self.bg_hover)
                else:
                    b.configure(bg=self.bg_card)
            
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
    
    def show_category(self, category_name):
        """Display settings for a specific category"""
        self.active_category = category_name
        
        # Update sidebar button states
        for name, btn in self.category_buttons.items():
            if name == category_name:
                btn.configure(bg=self.bg_hover)
            else:
                btn.configure(bg=self.bg_card)
        
        # Clear content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        category = self.categories[category_name]
        
        # Category header
        header = tk.Frame(self.content_frame, bg=self.bg_dark)
        header.pack(fill=tk.X, pady=(0, 20))
        
        title = tk.Label(header, 
                        text=f"{category['icon']} {category_name}",
                        font=("Segoe UI", 24, "bold"),
                        bg=self.bg_dark, fg=self.text_color)
        title.pack(anchor="w")
        
        subtitle = tk.Label(header,
                           text=f"{len(category['items'])} settings available",
                           font=("Segoe UI", 10),
                           bg=self.bg_dark, fg="#94a3b8")
        subtitle.pack(anchor="w", pady=(5, 0))
        
        # Settings grid
        for item in category["items"]:
            self.create_setting_card(item, category["color"])
    
    def create_setting_card(self, item, color):
        """Create a card for each setting"""
        card = tk.Frame(self.content_frame, bg=self.bg_card, 
                       relief=tk.FLAT, bd=0, highlightthickness=1,
                       highlightbackground=self.bg_hover)
        card.pack(fill=tk.X, pady=5)
        
        # Content container
        content = tk.Frame(card, bg=self.bg_card)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # Left side - setting info
        left_frame = tk.Frame(content, bg=self.bg_card)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        name_label = tk.Label(left_frame, text=item["name"],
                            font=("Segoe UI", 13, "bold"),
                            bg=self.bg_card, fg=self.text_color, anchor="w")
        name_label.pack(anchor="w")
        
        if "desc" in item:
            desc_label = tk.Label(left_frame, text=item["desc"],
                                font=("Segoe UI", 9),
                                bg=self.bg_card, fg="#94a3b8", anchor="w")
            desc_label.pack(anchor="w", pady=(2, 0))
        
        # Right side - open button
        btn = tk.Button(content, text="Open →",
                       font=("Segoe UI", 10, "bold"),
                       bg=color, fg="white",
                       activebackground=color,
                       activeforeground="white",
                       relief=tk.FLAT,
                       padx=20, pady=8,
                       cursor="hand2",
                       bd=0,
                       command=lambda: self.execute_command(item))
        btn.pack(side=tk.RIGHT)
        
        # Hover effects
        def on_enter(e):
            card.configure(bg=self.bg_hover, highlightbackground=color)
            content.configure(bg=self.bg_hover)
            left_frame.configure(bg=self.bg_hover)
            name_label.configure(bg=self.bg_hover)
            if "desc" in item:
                desc_label.configure(bg=self.bg_hover)
        
        def on_leave(e):
            card.configure(bg=self.bg_card, highlightbackground=self.bg_hover)
            content.configure(bg=self.bg_card)
            left_frame.configure(bg=self.bg_card)
            name_label.configure(bg=self.bg_card)
            if "desc" in item:
                desc_label.configure(bg=self.bg_card)
        
        for widget in [card, content, left_frame, name_label]:
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
        if "desc" in item:
            desc_label.bind("<Enter>", on_enter)
            desc_label.bind("<Leave>", on_leave)
    
    def execute_command(self, item):
        """Execute a control panel command"""
        print(f"Executing: {item['cmd']}")
        try:
            cmd = item["cmd"]
            if cmd.startswith("ms-settings:"):
                # Windows 10/11 settings
                subprocess.Popen(["start", cmd], shell=True)
            elif cmd == "windowsdefender:":
                subprocess.Popen(["start", cmd], shell=True)
            else:
                # Legacy control panel items
                subprocess.Popen(cmd, shell=True)
            print(f"Command executed successfully: {item['name']}")
        except Exception as e:
            print(f"Error executing {item['name']}: {e}")
            messagebox.showerror("Error", 
                               f"Failed to open {item['name']}:\n{str(e)}")
    
    def on_search(self, *args):
        """Filter settings based on search query"""
        query = self.search_var.get().lower().strip()
        
        if not query:
            # Show last active category or default
            if hasattr(self, 'active_category'):
                self.show_category(self.active_category)
            else:
                self.show_category("System")
            return
        
        # Clear content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Search header
        header_frame = tk.Frame(self.content_frame, bg=self.bg_dark)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        header = tk.Label(header_frame,
                         text=f"🔍 Search results for: \"{query}\"",
                         font=("Segoe UI", 20, "bold"),
                         bg=self.bg_dark, fg=self.text_color)
        header.pack(anchor="w")
        
        # Search through all categories
        found = False
        for cat_name, cat_data in self.categories.items():
            for item in cat_data["items"]:
                if (query in item["name"].lower() or 
                    (query in item.get("desc", "").lower())):
                    self.create_setting_card(item, cat_data["color"])
                    found = True
        
        if not found:
            no_results = tk.Label(self.content_frame,
                                text="No settings found matching your search",
                                font=("Segoe UI", 14),
                                bg=self.bg_dark, fg="#94a3b8")
            no_results.pack(pady=50)


def main():
    try:
        print("Creating main window...")
        root = tk.Tk()
        print("Initializing application...")
        app = UnifiedControlPanel(root)
        print("Starting main loop...")
        root.mainloop()
        print("Application closed normally")
    except Exception as e:
        print(f"\n!!! ERROR !!!")
        print(f"Error: {e}")
        print(f"\nFull traceback:")
        traceback.print_exc()
        input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()