from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    # Alternative locator options
    leave_list_header_xpath = "//h5[contains(.,'Leave')] | //h5[contains(.,'Time Off')] | //h6[contains(.,'Leave')]"
    leave_table_xpath = "//div[contains(@class,'table')] | //table | //div[contains(@class,'card-container')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_leave_list_displayed(self):
        """Verifies if the leave list is displayed"""
        try:
            return self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.leave_list_header_xpath))
            ).is_displayed()
        except:
            return False