import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from utils.browser_setup import get_driver
from utils.helpers import (
    wait_for_clickable,
    wait_for_presence,
    switch_to_new_tab,
    switch_to_main_tab,
    log_step,
)
from utils.file_utils import get_screenshot_path
from pages.login_page import LoginPage
from config.settings import URL, EMAIL, PASSWORD

@pytest.fixture
def browser():
    # Setup
    driver = get_driver()
    yield driver
    # Teardown
    driver.quit()

def test_login_success(browser):
    """Test successful login flow using the login page object."""
    try:
        # Navigate to the login page
        browser.get(URL)
        log_step("Opening login page...")
        time.sleep(2)  # Allow page to load
        
        # Initialize the login page object
        login_page = LoginPage(browser)
        
        # Click on sign in button
        login_page.click_sign_in_button()
        log_step("Clicked Sign in button")
        
        # Switch to new tab that opens for authentication
        login_page.switch_to_new_tab()
        
        # Enter email
        login_page.enter_email(EMAIL)
        log_step("Entered email address")
        
        # Enter password
        login_page.enter_password(PASSWORD)
        log_step("Entered password")
        
        # Handle stay signed in prompt
        login_page.handle_stay_signed_in()
        log_step("Handled 'Stay signed in' prompt")
        
        # Switch back to the main application tab
        login_page.back_to_main_tab()
        log_step("Returned to main application tab")
        
        # Allow time for the page to load after login
        time.sleep(2)
        
        # Verify successful login
        assert browser.current_url != URL, "URL should change after successful login"
        
    except Exception as e:
        # Take screenshot on failure with organized path
        screenshot_path = get_screenshot_path("login_failure")
        browser.save_screenshot(screenshot_path)
        log_step(f"Screenshot saved to: {screenshot_path}")
        raise e

