# ============================================================================
# FILE: main.py
# ============================================================================

import subprocess
from tkinter import messagebox
from pathlib import Path
import json
import traceback
import os
import tkinter as tk

from ui import SettingCard, UITheme
from modules import *
from layout import MainLayout


class UnifiedControlPanel:
    """Main application class - handles business logic and coordination"""
    
    def __init__(self, root):
        self.root = root
        
        # Load configuration
        self.config_file = Path.home() / ".unified_control_panel" / "config.json"
        self.load_config()
        
        # Load all modules
        self.modules = self.load_modules()
        
        # Create UI layout
        self.layout = MainLayout(root, on_search_callback=self.on_search)
        
        # Build sidebar with module buttons
        self.build_sidebar()
        
        # Show default module
        self.show_module("System")
        
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
    
    def build_sidebar(self):
        """Build the category sidebar with module buttons"""
        for module_name, module in self.modules.items():
            self.layout.add_sidebar_button(
                module_name=module_name,
                module_icon=module.get_icon(),
                command=lambda name=module_name: self.show_module(name)
            )
    
    def build_card(self, module: BaseModule, setting: ModuleSetting) -> SettingCard:
        """Build a setting card for display"""
        card = SettingCard(
            self.layout.get_content_frame(),
            name=setting.name,
            description=f"{setting.description} ({setting.command})",
            command=lambda s=setting: self.execute_command(s),
            color=module.get_color()
        )
        return card
    
    def show_module(self, module_name: str):
        """Display settings for a specific module"""
        self.active_module = module_name
        
        # Update sidebar
        self.layout.set_active_sidebar_button(module_name)
        
        # Clear and rebuild content
        self.layout.clear_content()
        
        module = self.modules[module_name]
        settings = module.get_settings()
        
        # Create header
        self.layout.create_module_header(
            module_icon=module.get_icon(),
            module_name=module_name,
            settings_count=len(settings)
        )
        
        # Add setting cards
        for setting in settings:
            card = self.build_card(module, setting)
            self.layout.add_setting_card(card)
    
    def execute_command(self, setting: ModuleSetting):
        """Execute a control panel command"""
        print(f"Executing: {setting.command}")
        try:
            cmd = setting.command

            if '%' in cmd:
                cmd = os.path.expandvars(cmd)
    
            if cmd.startswith("shell:"):
                subprocess.Popen(['explorer', cmd], shell=True)
            elif cmd.startswith("ms-settings:") or cmd == "windowsdefender:":
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
        
        # If empty query, show active module
        if not query:
            if hasattr(self, 'active_module'):
                self.show_module(self.active_module)
            else:
                self.show_module("System")
            return
        
        # Clear content and show search header
        self.layout.clear_content()
        self.layout.create_search_header(query)
        
        # Search through all modules
        found = False
        for module_name, module in self.modules.items():
            for setting in module.get_settings():
                if (query in setting.name.lower() or 
                    query in setting.description.lower() or
                    query in setting.command):
                    card = self.build_card(module, setting)
                    self.layout.add_setting_card(card)
                    found = True
        
        # Show no results message if nothing found
        if not found:
            self.layout.show_no_results_message()


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
