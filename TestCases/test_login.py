import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
import time

class Test_001_Login:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        try:
            actual_title = self.driver.title
            assert actual_title == "OrangeHRM", f"Title {actual_title} doesn't match expected"
        finally:
            self.driver.close()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        try:
            self.lp = LoginPage(self.driver)
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(3)  # Allow dashboard to load
            actual_title = self.driver.title
            assert actual_title == "OrangeHRM", "Login failed"
        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")
        finally:
            self.driver.close()