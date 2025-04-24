import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Reusable helper functions for Selenium-based automation.
These are commonly used across multiple page objects or test cases.
"""

# Wait until an element is clickable and return it
def wait_for_clickable(driver, by_locator, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(by_locator))

# Wait until an element is present in the DOM and return it
def wait_for_presence(driver, by_locator, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(by_locator))

# Switch to the newest browser tab (typically used after a new tab opens)
def switch_to_new_tab(driver):
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])

# Switch back to the original (first) tab
def switch_to_main_tab(driver):
    driver.switch_to.window(driver.window_handles[0])

# Take a screenshot with a timestamp for debugging purposes
def take_screenshot(driver, name="screenshot"):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{name}_{timestamp}.png"
    driver.save_screenshot(filename)
    print(f"📸 Screenshot saved: {filename}")

# Simple step logger to track progress in console
def log_step(message):
    print(f"🟢 {message}")
