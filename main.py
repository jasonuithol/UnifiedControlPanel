# ============================================================================
# FILE: main.py
# ============================================================================

import subprocess
from tkinter import messagebox
from pathlib import Path
import json
#import sys
import traceback

from general_ui          import *
from modules.base_module import *

from modules.accounts        import *
from modules.apps            import *
from modules.devices         import *
from modules.network         import *
from modules.personalization import *
from modules.security        import *
from modules.services        import *
from modules.storage         import *
from modules.system          import *

class UnifiedControlPanel:
    """Main application class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Unified Control Panel")
        self.root.geometry("1200x800")
        self.root.configure(bg=UITheme.BG_DARK)
        
        # Try to set icon
        try:
            self.root.iconbitmap('default')
        except:
            pass
        
        # Load configuration
        self.config_file = Path.home() / ".unified_control_panel" / "config.json"
        self.load_config()
        
        # Load all modules
        self.modules = self.load_modules()
        
        # Create UI
        self.create_ui()
        
        print("UI initialized successfully!")
    
    def load_modules(self) -> Dict[str, BaseModule]:
        """Load all module instances"""
        modules = {}
        module_classes = [
            SystemModule,
            NetworkModule,
            DevicesModule,
            PersonalizationModule,
            AccountsModule,
            SecurityModule,
            AppsModule,
            ServicesModule,
            StorageModule,
        ]
        
        for module_class in module_classes:
            module = module_class()
            modules[module.get_name()] = module
        
        return modules
    
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
        search_bar = SearchBar(header, on_search=self.on_search)
        search_bar.pack(side=tk.RIGHT, padx=20)
        
        # Main container
        main_container = tk.Frame(self.root, bg=UITheme.BG_DARK)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Sidebar
        self.sidebar = tk.Frame(main_container, bg=UITheme.BG_DARKER, width=250)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))
        self.sidebar.pack_propagate(False)
        
        sidebar_title = tk.Label(
            self.sidebar,
            text="CATEGORIES",
            font=("Segoe UI", 9, "bold"),
            bg=UITheme.BG_DARKER,
            fg=UITheme.TEXT_SECONDARY
        )
        sidebar_title.pack(pady=(10, 15), padx=20, anchor="w")
        
        # Content area
        self.scroll_frame = ScrollableFrame(main_container)
        self.scroll_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.content_frame = self.scroll_frame.get_frame()
        
        # Build sidebar
        self.build_sidebar()
        
        # Show default module
        self.show_module("System")
    
    def build_sidebar(self):
        """Build the category sidebar"""
        self.sidebar_buttons = {}
        
        for module_name, module in self.modules.items():
            btn = SidebarButton(
                self.sidebar,
                text=f"{module.get_icon()}  {module_name}",
                command=lambda name=module_name: self.show_module(name)
            )
            btn.pack(fill=tk.X, pady=2, padx=5)
            self.sidebar_buttons[module_name] = btn
    
    def show_module(self, module_name: str):
        """Display settings for a specific module"""
        self.active_module = module_name
        
        # Update sidebar button states
        for name, btn in self.sidebar_buttons.items():
            btn.set_active(name == module_name)
        
        # Clear content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        module = self.modules[module_name]
        
        # Module header
        header = tk.Frame(self.content_frame, bg=UITheme.BG_DARK)
        header.pack(fill=tk.X, pady=(0, 20))
        
        title = tk.Label(
            header,
            text=f"{module.get_icon()} {module_name}",
            font=("Segoe UI", 24, "bold"),
            bg=UITheme.BG_DARK,
            fg=UITheme.TEXT_PRIMARY
        )
        title.pack(anchor="w")
        
        settings = module.get_settings()
        subtitle = tk.Label(
            header,
            text=f"{len(settings)} settings available",
            font=("Segoe UI", 10),
            bg=UITheme.BG_DARK,
            fg=UITheme.TEXT_SECONDARY
        )
        subtitle.pack(anchor="w", pady=(5, 0))
        
        # Settings cards
        for setting in settings:
            card = SettingCard(
                self.content_frame,
                name=setting.name,
                description=setting.description,
                command=lambda s=setting: self.execute_command(s),
                color=module.get_color()
            )
            card.pack(fill=tk.X, pady=5)
    
    def execute_command(self, setting: ModuleSetting):
        """Execute a control panel command"""
        print(f"Executing: {setting.command}")
        try:
            cmd = setting.command
            if cmd.startswith("ms-settings:") or cmd == "windowsdefender:":
                subprocess.Popen(["start", cmd], shell=True)
            else:
                subprocess.Popen(cmd, shell=True)
            print(f"Command executed successfully: {setting.name}")
        except Exception as e:
            print(f"Error executing {setting.name}: {e}")
            messagebox.showerror("Error", f"Failed to open {setting.name}:\n{str(e)}")
    
    def on_search(self, query: str):
        """Filter settings based on search query"""
        query = query.lower().strip()
        
        if not query:
            if hasattr(self, 'active_module'):
                self.show_module(self.active_module)
            else:
                self.show_module("System")
            return
        
        # Clear content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Search header
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
        
        # Search through all modules
        found = False
        for module_name, module in self.modules.items():
            for setting in module.get_settings():
                if (query in setting.name.lower() or 
                    query in setting.description.lower()):
                    card = SettingCard(
                        self.content_frame,
                        name=setting.name,
                        description=setting.description,
                        command=lambda s=setting: self.execute_command(s),
                        color=module.get_color()
                    )
                    card.pack(fill=tk.X, pady=5)
                    found = True
        
        if not found:
            no_results = tk.Label(
                self.content_frame,
                text="No settings found matching your search",
                font=("Segoe UI", 14),
                bg=UITheme.BG_DARK,
                fg=UITheme.TEXT_SECONDARY
            )
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