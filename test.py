from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Tài khoản
EMAIL = "Theon.test@8cbkg6.onmicrosoft.com"
PASSWORD = "vietnamAI2025*"

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")

# Tự động dùng chromedriver mới nhất
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://172.31.21.225:8443/login")
    time.sleep(2)

    # Click nút "Sign in"
    sign_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/div/div/div/div[2]")))
    sign_in_btn.click()

    # Nếu có tab mới, chuyển qua
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])

    # Nhập email
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "loginfmt")))
    email_input.send_keys(EMAIL)
    wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

    # Nhập mật khẩu
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "passwd")))
    password_input.send_keys(PASSWORD)
    wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

    # Xử lý "Stay signed in?"
    try:
        stay_signed_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='idSIButton9']")))
        stay_signed_in_btn.click()
    except:
        pass
    time.sleep(2)
    
    # Back to the original window
    driver.switch_to.window(driver.window_handles[0])
    
    print("🎉 Đăng nhập thành công!")

except Exception as e:
    print(f"❌ Lỗi đăng nhập: {e}")

finally:
    # driver.quit()
    pass
