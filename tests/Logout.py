from selenium.webdriver.common.by import By
import module_xpath_constants as constants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules import login_module


class TestLogout:

    def test_logout(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        login_module(driver=driver, email="testtestov123@yandex.ru", password="123456")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGGED_IN)))

        driver.find_element(By.XPATH, constants.CABINET_LINK).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, constants.CABINET_PAGE)))

        driver.find_element(By.XPATH, constants.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        driver.find_element(By.XPATH, constants.CABINET_LINK).click() # Пробуем войти в кабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        assert driver.find_element(By.XPATH, constants.LOGIN_PAGE).text == "Вход", "Не найден текст 'Вход', не удалось выйти из аккаунта."