from selenium.webdriver.common.by import By
import module_xpath_constants as constants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules import login_module


class TestCabinet:

    def test_get_cabinet(self, driver, registration):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.LOGIN_PAGE)))

        login_module(driver=driver, email=registration["email"], password=registration["password"])

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.MAIN_PAGE)))

        driver.find_element(By.XPATH, constants.CABINET_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, constants.CABINET_PAGE)))

        email_info = driver.find_element(By.XPATH, constants.CABINET_PAGE_LOGIN_INFO)

        assert email_info.get_attribute("value") == registration[
            "email"], f"Не найден элемент ввода c значением {registration['email']}."
        driver.quit()

