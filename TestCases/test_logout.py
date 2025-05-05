import pytest
import time
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from Utilities.readProperties import ReadConfig

class Test_003_Logout:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_logout(self, setup):
        try:
            self.driver = setup
            self.driver.get(self.base_url)

            # Login first
            self.lp = LoginPage(self.driver)
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(2)

            # Logout
            self.dp = DashboardPage(self.driver)
            self.dp.click_user_dropdown()  # First click the user dropdown
            time.sleep(1)
            self.dp.click_logout()  # Then click logout
            time.sleep(2)

            # Verify logout by checking login button is displayed
            assert self.lp.is_login_button_displayed(), "Logout unsuccessful"
        finally:
            self.driver.quit()