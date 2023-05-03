from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestConstructor:

    def test_get_burger_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.MAIN_PAGE)))
        driver.find_element(*Locators.FILLING_TAB).click()
        driver.find_element(*Locators.BULKI_TAB).click()
        bulki_title = driver.find_element(*Locators.TITLE_BULKI)
        bulki_item = driver.find_element(*Locators.BULKI_ITEM)
        assert bulki_title.text == "Булки" and bulki_item.text == "Флюоресцентная булка R2-D3", "Название раздела должно называться 'Булки' и есть булка: 'Флюоресцентная булка R2-D3'."

    def test_get_sausage_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.MAIN_PAGE)))
        driver.find_element(*Locators.SAUSAGE_TAB).click()
        sausage_title = driver.find_element(*Locators.TITLE_SAUSAGE)
        sausage_item = driver.find_element(*Locators.SAUSAGE_ITEM)
        assert sausage_title.text == "Соусы" and sausage_item.text == "Соус Spicy-X", "Название раздела должно называться 'Соусы' и есть соус: 'Соус Spicy-X'."

    def test_get_filling_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.MAIN_PAGE)))
        driver.find_element(*Locators.FILLING_TAB).click()
        filling_title = driver.find_element(*Locators.TITLE_FILLING)
        filling_item = driver.find_element(*Locators.FILLING_ITEM)
        assert filling_title.text == "Начинки" and filling_item.text == "Говяжий метеорит (отбивная)", "Название раздела должно называться 'Начинки' и есть начинка: 'Говяжий метеорит (отбивная)'."
