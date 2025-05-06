from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    # Updated locators with more specific paths
    textbox_username_xpath = "//input[@placeholder='Username' and @name='username']"
    textbox_password_xpath = "//input[@placeholder='Password' and @name='password']"
    button_login_xpath = "//button[contains(@class,'orangehrm-login-button')]"
    login_page_title = "OrangeHRM"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)  # Increased timeout to 20 seconds

    def set_username(self, username):
        try:
            username_field = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_username_xpath))
            )
            username_field.clear()
            username_field.send_keys(username)
        except Exception as e:
            print(f"Error setting username: {str(e)}")
            raise

    def set_password(self, password):
        try:
            password_field = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_password_xpath))
            )
            password_field.clear()
            password_field.send_keys(password)
        except Exception as e:
            print(f"Error setting password: {str(e)}")
            raise

    def click_login(self):
        try:
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
            )
            login_button.click()
        except Exception as e:
            print(f"Error clicking login button: {str(e)}")
            raise

    def get_login_page_title(self):
        return self.driver.title
    
    def is_login_button_displayed(self):
        try:
            return self.driver.find_element(By.XPATH, self.button_login_xpath).is_displayed()
        except:
            return False
        

    def is_login_page_displayed(self):
        """Verifies if login page is displayed correctly"""
        try:
        # Check for all key elements on login page
            username_field = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_username_xpath)))
            password_field = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_password_xpath)))
            login_button = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
        
            return (username_field.is_displayed() and 
                password_field.is_displayed() and 
                login_button.is_displayed())
        except Exception as e:
            print(f"Login page verification failed: {str(e)}")
            return False