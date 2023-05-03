from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import Locators
import random

class TestRegistration:

    def test_registration_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.REGISTER_PAGE)))

        email = f"testtestov9{random.randint(100, 999)}@yandex.ru"

        driver.find_element(*Locators.NAME_INPUT).send_keys("Вася")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE)))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.MAIN_PAGE)))
        driver.find_element(*Locators.CABINET_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.CABINET_PAGE)))
        cabinet_page = driver.find_element(*Locators.CABINET_PAGE)

        assert cabinet_page.text == "Профиль", f"Не найден раздел 'Профиль'."

    @pytest.mark.parametrize("incorrect_password", [' ', '1', '12345'])
    def test_registration_error_incorrect_password(self, driver, incorrect_password):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.REGISTER_PAGE)))

        driver.find_element(*Locators.NAME_INPUT).send_keys("Вася")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("testtestov123@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(incorrect_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        error_message = driver.find_elements(*Locators.ERROR_MESSAGE_REGISTER)

        assert error_message[
                   0].text == "Некорректный пароль" or error_message == [], f'Произведено регистрация с некорректным паролем: {incorrect_password}'
