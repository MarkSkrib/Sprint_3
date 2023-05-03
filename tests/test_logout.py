from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestLogout:

    def test_logout(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE)))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys("testtestov123@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGGED_IN)))
        driver.find_element(*Locators.CABINET_LINK).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Locators.CABINET_PAGE)))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE)))
        driver.find_element(*Locators.CABINET_LINK).click() # Пробуем войти в кабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE)))
        assert driver.find_element(*Locators.LOGIN_PAGE).text == "Вход", "Не найден текст 'Вход', не удалось выйти из аккаунта."
