import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig

class Test_000_HomePage:
    base_url = ReadConfig.get_application_url()
    
    def test_home_page_title(self, setup):
        """Verify home page title and login page elements"""
        self.driver = setup
        try:
            # Navigate to application
            self.driver.get(self.base_url)
            
            # Initialize LoginPage
            self.lp = LoginPage(self.driver)
            
            # Verify page title
            actual_title = self.driver.title
            expected_title = "OrangeHRM"
            assert actual_title == expected_title, \
                f"Title mismatch. Expected: {expected_title}, Actual: {actual_title}"
            
            # Verify login page elements
            assert self.lp.is_login_page_displayed(), "Login page not displayed correctly"
            
            print("Home page title and login page verification successful")
        except Exception as e:
            pytest.fail(f"Test failed: {str(e)}")
            self.driver.save_screenshot("home_page_verification_error.png")
        finally:
            self.driver.quit()