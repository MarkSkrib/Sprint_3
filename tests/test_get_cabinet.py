from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestGetCabinet:

    def test_get_cabinet(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE)))

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        email_input.send_keys("testtestov123@yandex.ru")
        password_input.send_keys("123456")

        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.MAIN_PAGE)))

        driver.find_element(*Locators.CABINET_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.CABINET_PAGE)))

        profile_link = driver.find_element(*Locators.CABINET_PAGE)
        assert profile_link.text == 'Профиль', "В личном кабинете должен отображаться раздел 'Профиль'"
