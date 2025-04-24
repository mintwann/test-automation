import os
from datetime import datetime

def ensure_dir_exists(directory):
    """Ensure that the directory exists, creating it if necessary."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def get_screenshot_dir():
    """Get the directory for saving screenshots, organized by date."""
    base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "screenshots")
    date_dir = os.path.join(base_dir, datetime.now().strftime("%Y-%m-%d"))
    return ensure_dir_exists(date_dir)

def get_screenshot_path(test_name):
    """Generate a full path for a screenshot with timestamp."""
    timestamp = datetime.now().strftime("%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    return os.path.join(get_screenshot_dir(), filename)