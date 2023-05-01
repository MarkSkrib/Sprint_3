from selenium.webdriver.common.by import By
import module_xpath_constants as constants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from modules import login_module


class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.MAIN_PAGE_LOGIN_BTN)))

        driver.find_element(By.XPATH, constants.MAIN_PAGE_LOGIN_BTN).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        login_module(driver=driver, email="testtestov123@yandex.ru", password="123456")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGGED_IN)))

        assert driver.find_element(By.XPATH,
                                   constants.LOGGED_IN).text == "Оформить заказ", "Не найдена кнопка с текстом \"Оформить заказ\""
        driver.quit()

    def test_login_from_cabinet_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.MAIN_PAGE)))

        driver.find_element(By.XPATH, constants.CABINET_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        login_module(driver=driver, email="testtestov123@yandex.ru", password="123456")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGGED_IN)))

        assert driver.find_element(By.XPATH,
                                   constants.LOGGED_IN).text == "Оформить заказ", "Не найдена кнопка с текстом \"Оформить заказ\""
        driver.quit()

    def test_login_from_registration_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.REGISTER_PAGE)))

        driver.find_element(By.XPATH, constants.LOGIN_LINK_IN_OTHER_PAGE).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        login_module(driver=driver, email="testtestov123@yandex.ru", password="123456")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGGED_IN)))

        assert driver.find_element(By.XPATH,
                                   constants.LOGGED_IN).text == "Оформить заказ", "Не найдена кнопка с текстом \"Оформить заказ\""
        driver.quit()

    def test_login_from_reset_password_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.RESET_PASSWORD_PAGE)))

        driver.find_element(By.XPATH, constants.LOGIN_LINK_IN_OTHER_PAGE).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        login_module(driver=driver, email="testtestov123@yandex.ru", password="123456")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGGED_IN)))

        assert driver.find_element(By.XPATH,
                                   constants.LOGGED_IN).text == "Оформить заказ", "Не найдена кнопка с текстом \"Оформить заказ\""
        driver.quit()
