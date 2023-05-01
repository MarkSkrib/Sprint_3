from selenium.webdriver.common.by import By
import module_xpath_constants as constants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules import login_module


class TestFromCabinetConstructor:

    def test_redirect_to_constructor_from_cabinet(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        login_module(driver=driver, email="testtestov123@yandex.ru", password="123456")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGGED_IN)))

        driver.find_element(By.XPATH, constants.CABINET_LINK).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, constants.CABINET_PAGE)))

        driver.find_element(By.XPATH, constants.CONSTRUCTOR_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.MAIN_PAGE)))

        assert driver.find_element(By.XPATH,
                                   constants.MAIN_PAGE_MENU_BURGER).text == "Булки", "Не найден элемент меню 'Булки'"
        driver.quit()

    def test_redirect_to_constructor_from_cabinet_by_click_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        login_module(driver=driver, email="testtestov123@yandex.ru", password="123456")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGGED_IN)))

        driver.find_element(By.XPATH, constants.CABINET_LINK).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, constants.CABINET_PAGE)))

        driver.find_element(By.XPATH, constants.LOGO_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.MAIN_PAGE)))

        assert driver.find_element(By.XPATH,
                                   constants.MAIN_PAGE_MENU_BURGER).text == "Булки", "Не найден элемент меню 'Булки'"
        driver.quit()