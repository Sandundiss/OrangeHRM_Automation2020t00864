import pytest
import time
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage
from Utilities.readProperties import ReadConfig

class Test_002_Leave:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_leave_page(self, setup):
        self.driver = setup
        try:
            self.driver.get(self.base_url)

            # Login first
            self.lp = LoginPage(self.driver)
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(2)

            # Go to Leave page
            self.dp = DashboardPage(self.driver)
            assert self.dp.click_my_leave(), "Failed to click My Leave button"
            time.sleep(2)

            # Verify Leave page
            self.leave_pg = LeavePage(self.driver)
            assert self.leave_pg.is_leave_list_displayed(), "Leave list not displayed"
        finally:
            self.driver.quit()