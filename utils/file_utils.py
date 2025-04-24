import os
from datetime import datetime
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Run pytest with customizable report name")
    parser.add_argument("--report-name", type=str, default=None,
                       help="Name of the HTML report file (default: report_YYYY-MM-DD_HH-MM-SS.html)")
    return parser.parse_args()

def get_report_path(custom_name=None):
    if custom_name:
        return f"reports/{custom_name}"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"reports/report_{timestamp}.html"

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