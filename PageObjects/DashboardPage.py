from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    # Locators
    my_leave_link_xpath = "//button[contains(@title,'My Leave') or contains(@title,'Leave')]"
    user_dropdown_xpath = "//span[@class='oxd-userdropdown-tab']"
    logout_link_xpath = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_my_leave(self):
        """Clicks the My Leave button in the dashboard"""
        try:
            leave_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.my_leave_link_xpath)))
            
            leave_button.click()
            return True
        except Exception as e:
            print(f"Error clicking My Leave button: {str(e)}")
            return False

    def click_user_dropdown(self):
        """Clicks the user profile dropdown"""
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.user_dropdown_xpath))).click()

    def click_logout(self):
        """Clicks the logout link"""
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.logout_link_xpath))).click()