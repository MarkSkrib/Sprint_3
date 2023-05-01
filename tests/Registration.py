from selenium.webdriver.common.by import By
import module_xpath_constants as constants
from module_generators import generate_email
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestRegistration:

    def test_registration_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.REGISTER_PAGE)))

        email = generate_email()

        name_input = driver.find_element(By.XPATH, constants.NAME_INPUT)
        email_input = driver.find_element(By.XPATH, constants.EMAIL_INPUT)
        password_input = driver.find_element(By.XPATH, constants.PASSWORD_INPUT)

        name_input.send_keys("Вася")
        email_input.send_keys(email)
        password_input.send_keys("123456")

        driver.find_element(By.XPATH, constants.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        email_input = driver.find_element(By.XPATH, constants.EMAIL_INPUT)
        password_input = driver.find_element(By.XPATH, constants.PASSWORD_INPUT)
        email_input.send_keys(email)
        password_input.send_keys("123456")
        driver.find_element(By.XPATH, constants.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.MAIN_PAGE)))

        driver.find_element(By.XPATH, constants.CABINET_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.CABINET_PAGE)))

        e = driver.find_element(By.XPATH, constants.CABINET_PAGE_LOGIN_INFO)

        assert e.get_attribute("value") == email, f"Не найден элемент ввода c значением {email}."
        driver.quit()

    @pytest.mark.parametrize("incorrect_password", [' ', '1','12345'])
    def test_registration_error_incorrect_password(self, driver, incorrect_password):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.REGISTER_PAGE)))

        name_input = driver.find_element(By.XPATH, constants.NAME_INPUT)
        email_input = driver.find_element(By.XPATH, constants.EMAIL_INPUT)
        password_input = driver.find_element(By.XPATH, constants.PASSWORD_INPUT)
        register_button = driver.find_element(By.XPATH, constants.REGISTER_BUTTON)

        name_input.send_keys("Вася")
        email_input.send_keys("testuniqueov777@yandex.ru")
        password_input.send_keys(incorrect_password)

        register_button.click()
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.ERROR_MESSAGE_REGISTER)))
        error_message = driver.find_elements(By.XPATH, constants.ERROR_MESSAGE_REGISTER)
        print(error_message)

        assert error_message[0].text == "Некорректный пароль" or error_message == [] , f'Произведено регистрация с некорректным паролем: {incorrect_password}'

        driver.quit()












