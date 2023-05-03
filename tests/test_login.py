from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.MAIN_PAGE_LOGIN_BTN)))
        driver.find_element(*Locators.MAIN_PAGE_LOGIN_BTN).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE)))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("testtestov123@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGGED_IN)))
        assert driver.find_element(
            *Locators.LOGGED_IN).text == "Оформить заказ", "Не найдена кнопка с текстом \"Оформить заказ\""

    def test_login_from_cabinet_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.MAIN_PAGE)))
        driver.find_element(*Locators.CABINET_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE)))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("testtestov123@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGGED_IN)))
        assert driver.find_element(
            *Locators.LOGGED_IN).text == "Оформить заказ", "Не найдена кнопка с текстом \"Оформить заказ\""

    def test_login_from_registration_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.REGISTER_PAGE)))
        driver.find_element(*Locators.LOGIN_LINK_IN_OTHER_PAGE).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE)))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("testtestov123@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGGED_IN)))
        assert driver.find_element(
            *Locators.LOGGED_IN).text == "Оформить заказ", "Не найдена кнопка с текстом \"Оформить заказ\""

    def test_login_from_reset_password_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.RESET_PASSWORD_PAGE)))
        driver.find_element(*Locators.LOGIN_LINK_IN_OTHER_PAGE).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGIN_PAGE)))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("testtestov123@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.LOGGED_IN)))
        assert driver.find_element(
            *Locators.LOGGED_IN).text == "Оформить заказ", "Не найдена кнопка с текстом \"Оформить заказ\""
