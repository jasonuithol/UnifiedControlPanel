# ============================================================================
# FILE: theme.py
# ============================================================================

class Theme:
    """Unified theming and UI configuration"""
    
    # ========================================================================
    # WINDOW CONFIGURATION
    # ========================================================================
    WINDOW_TITLE = "Unified Control Panel"
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    WINDOW_ICON = 'default'
    
    # ========================================================================
    # COLORS
    # ========================================================================
    BG_DARK = "#1a1a1a"
    BG_DARKER = "#0d0d0d"
    BG_CARD = "#2d2d2d"
    BG_CARD_HOVER = "#3d3d3d"
    
    TEXT_PRIMARY = "#ffffff"
    TEXT_SECONDARY = "#888888"
    
    ACCENT_BLUE = "#0078d4"
    ACCENT_GREEN = "#10b981"
    ACCENT_RED = "#ef4444"
    ACCENT_PURPLE = "#8b5cf6"
    ACCENT_ORANGE = "#f97316"
    
    # Sidebar button colors
    SIDEBAR_ACTIVE = "#2d2d2d"
    SIDEBAR_HOVER = "#1f1f1f"
    
    # ========================================================================
    # FONTS
    # ========================================================================
    FONT_FAMILY = "Segoe UI"
    
    FONT_TITLE = (FONT_FAMILY, 20, "bold")
    FONT_VERSION = (FONT_FAMILY, 9)
    FONT_CATEGORY = (FONT_FAMILY, 9, "bold")
    FONT_MODULE_HEADER = (FONT_FAMILY, 24, "bold")
    FONT_MODULE_SUBTITLE = (FONT_FAMILY, 10)
    FONT_SEARCH_HEADER = (FONT_FAMILY, 20, "bold")
    FONT_NO_RESULTS = (FONT_FAMILY, 14)
    FONT_SIDEBAR_BUTTON = (FONT_FAMILY, 10)
    FONT_CARD_NAME = (FONT_FAMILY, 12, "bold")
    FONT_CARD_DESCRIPTION = (FONT_FAMILY, 9)
    FONT_SEARCH_BAR = (FONT_FAMILY, 10)
    FONT_BUTTON = (FONT_FAMILY, 10, "bold")
    
    # ========================================================================
    # LAYOUT DIMENSIONS
    # ========================================================================
    # Header
    HEADER_HEIGHT = 80
    HEADER_PADDING_X = 20
    HEADER_PADDING_Y = 20
    VERSION_PADDING_X = 5
    
    # Main container
    MAIN_CONTAINER_PADDING = 20
    
    # Sidebar
    SIDEBAR_WIDTH = 250
    SIDEBAR_PADDING_RIGHT = 20
    SIDEBAR_TITLE_PADDING_Y = (10, 15)
    SIDEBAR_TITLE_PADDING_X = 20
    SIDEBAR_BUTTON_PADDING_Y = 2
    SIDEBAR_BUTTON_PADDING_X = 5
    SIDEBAR_BUTTON_INTERNAL_PADDING_X = 15
    SIDEBAR_BUTTON_INTERNAL_PADDING_Y = 12
    
    # Content area
    CONTENT_MODULE_HEADER_PADDING_Y = (0, 20)
    CONTENT_MODULE_SUBTITLE_PADDING_Y = (5, 0)
    CONTENT_SEARCH_HEADER_PADDING_Y = (0, 20)
    CONTENT_NO_RESULTS_PADDING_Y = 50
    CONTENT_CARD_PADDING_Y = 5
    
    # Setting cards
    CARD_PADDING_X = 20
    CARD_PADDING_Y = 15
    CARD_BORDER_RADIUS = 8
    CARD_LEFT_BORDER_WIDTH = 4
    
    # Search bar
    SEARCH_BAR_WIDTH = 300
    SEARCH_BAR_PADDING_X = 15
    SEARCH_BAR_PADDING_Y = 10
    SEARCH_BAR_BORDER_RADIUS = 20
    
    # Modern buttons
    BUTTON_PADDING_X = 20
    BUTTON_PADDING_Y = 8
    BUTTON_BORDER_WIDTH = 0
    BUTTON_CURSOR = "hand2"
    
    # ========================================================================
    # TEXT CONTENT
    # ========================================================================
    APP_TITLE = "⚙️ Unified Control Panel"
    APP_VERSION = "v2.0 Modular"
    SIDEBAR_TITLE = "CATEGORIES"
    SEARCH_PLACEHOLDER = "Search settings..."
    NO_RESULTS_MESSAGE = "No settings found matching your search"
    
    @staticmethod
    def settings_count_text(count: int) -> str:
        """Generate settings count text"""
        return f"{count} settings available"
    
    @staticmethod
    def search_results_text(query: str) -> str:
        """Generate search results header text"""
        return f"🔍 Search results for: \"{query}\""
