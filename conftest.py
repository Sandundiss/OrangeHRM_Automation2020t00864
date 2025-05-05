import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--ignore-certificate-errors')
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                            options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()