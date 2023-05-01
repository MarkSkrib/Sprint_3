import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import module_xpath_constants as constants
from module_generators import generate_email

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service("C:/Users/MSkriblovskiy/PycharmProjects/Sprint_3/Drivers/chromedriver.exe"))
    return driver


@pytest.fixture
def registration():
    opts = Options()
    # opts.add_argument("--headless")
    driver = webdriver.Chrome(service=Service("C:/Users/MSkriblovskiy/PycharmProjects/Sprint_3/Drivers/chromedriver.exe"), options=opts)

    driver.get("https://stellarburgers.nomoreparties.site/register")
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.REGISTER_PAGE)))

    email = generate_email()

    name_input = driver.find_element(By.XPATH, constants.NAME_INPUT)
    email_input = driver.find_element(By.XPATH, constants.EMAIL_INPUT)
    password_input = driver.find_element(By.XPATH, constants.PASSWORD_INPUT)
    register_button = driver.find_element(By.XPATH, constants.REGISTER_BUTTON)

    name_input.send_keys("Вася")
    email_input.send_keys(email)
    password_input.send_keys("123456")

    register_button.click()

    driver.quit()

    return {
        "email": email,
        "password": "123456"
    }