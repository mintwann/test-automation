from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from utils.helpers import wait_for_clickable, wait_for_presence, switch_to_new_tab, switch_to_main_tab
from config.settings import WAIT_TIME

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    def click_sign_in_button(self):
        sign_in_btn = wait_for_clickable(
            self.driver, 
            (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/div/div/div/div[2]")
        )
        sign_in_btn.click()

    def switch_to_new_tab(self):
        switch_to_new_tab(self.driver)
        # Wait for the new tab to load
        self.wait.until(EC.presence_of_element_located((By.NAME, "loginfmt")))

    def enter_email(self, email):
        # Find email field and enter email
        email_field = wait_for_presence(self.driver, (By.NAME, "loginfmt"))
        email_field.clear()
        email_field.send_keys(email)
        
        # Find and click Next button - using robust approach
        next_btn = wait_for_clickable(self.driver, (By.ID, "idSIButton9"))
        next_btn.click()
        
        # Wait for password field to appear, indicating successful email entry
        wait_for_presence(self.driver, (By.NAME, "passwd"), WAIT_TIME)

    def enter_password(self, password):
        # Find password field and enter password
        password_field = wait_for_presence(self.driver, (By.NAME, "passwd"))
        password_field.clear()
        password_field.send_keys(password)
        
        # Use a fresh reference to the Sign in button and click it
        try:
            sign_in_btn = wait_for_clickable(self.driver, (By.ID, "idSIButton9"))
            sign_in_btn.click()
        except StaleElementReferenceException:
            # If the element becomes stale, try again with a fresh reference
            sign_in_btn = wait_for_clickable(self.driver, (By.ID, "idSIButton9"))
            sign_in_btn.click()

    def handle_stay_signed_in(self):
        try:
            # Wait a moment for the stay signed in prompt to appear
            stay_signed_in = wait_for_clickable(
                self.driver, 
                (By.ID, "idBtn_Back"), 
                timeout=WAIT_TIME
            )
            stay_signed_in.click()
        except (TimeoutException, StaleElementReferenceException):
            # If timeout or stale element, the prompt might not be shown
            pass

    def back_to_main_tab(self):
        switch_to_main_tab(self.driver)
        # Wait for the main application to load after login
        try:
            # Wait for some element that indicates successful login
            self.wait.until(
                EC.url_changes(self.driver.current_url)
            )
        except TimeoutException:
            pass
