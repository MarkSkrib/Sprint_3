from selenium.webdriver.common.by import By
import module_xpath_constants as constants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules import login_module, is_element_visible

from time import sleep


class TestConstructor:

    def test_get_burger_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        login_module(driver=driver, email="testtestov123@yandex.ru", password="123456")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGGED_IN)))

        driver.find_element(By.XPATH, constants.FILLING_TAB).click()

        sleep(3)
        driver.find_element(By.XPATH, constants.BULKI_TAB).click()
        sleep(3)

        burger_section = driver.find_element(By.XPATH, constants.MAIN_PAGE_MENU_BURGER)
        is_visible = is_element_visible(driver=driver, section=burger_section)

        assert is_visible, "Элемент h2 с текстом 'Бургеры' не прокрутился вниз."
        driver.quit()

    def test_get_sausage_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        login_module(driver=driver, email="testtestov123@yandex.ru", password="123456")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGGED_IN)))

        driver.find_element(By.XPATH, constants.SAUSAGE_TAB).click()

        sleep(3)

        sausage_section = driver.find_element(By.XPATH, constants.MAIN_PAGE_MENU_SAUSAGE)
        is_visible = is_element_visible(driver=driver, section=sausage_section)

        assert is_visible, "Элемент h2 с текстом 'Соусы' не прокрутился на вверх."
        driver.quit()

    def test_get_filling_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        login_module(driver=driver, email="testtestov123@yandex.ru", password="123456")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGGED_IN)))

        driver.find_element(By.XPATH, constants.FILLING_TAB).click()

        sleep(3)

        filling_section = driver.find_element(By.XPATH, constants.MAIN_PAGE_MENU_FILLING)
        is_visible = is_element_visible(driver=driver, section=filling_section)

        assert is_visible, "Элемент h2 с текстом 'Начинки' не прокрутился на вверх."
        driver.quit()