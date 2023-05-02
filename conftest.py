import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service("drivers/chromedriver.exe"))
    yield driver

    driver.quit()