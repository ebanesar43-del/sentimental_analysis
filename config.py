"""
Configuration file for E-Commerce Application
"""

# Application Settings
APP_NAME = "E-Commerce Store"
APP_VERSION = "1.0.0"

# Display Settings
PRODUCTS_PER_PAGE = 5
BORDER_WIDTH = 70

# Review Settings
MIN_RATING = 1
MAX_RATING = 5
SENTIMENT_POSITIVE_THRESHOLD = 4  # 4-5 stars
SENTIMENT_NEGATIVE_THRESHOLD = 2  # 1-2 stars
SENTIMENT_NEUTRAL_RANGE = (3, 3)  # 3 stars

# Color codes (for future terminal coloring)
COLOR_POSITIVE = "\033[92m"  # Green
COLOR_NEGATIVE = "\033[91m"  # Red
COLOR_NEUTRAL = "\033[93m"   # Yellow
COLOR_RESET = "\033[0m"      # Reset

# Messages
WELCOME_MESSAGE = "🛍️  WELCOME TO E-COMMERCE STORE 🛍️"
THANK_YOU_MESSAGE = "👋 Thank you! Goodbye!"
INVALID_INPUT = "❌ Invalid input!"
PRODUCT_NOT_FOUND = "❌ Product not found!"

# Menu Options
MENU_OPTIONS = {
    "1": "View All Products",
    "2": "View Product Reviews",
    "3": "View Review Summary",
    "4": "Exit"
}
