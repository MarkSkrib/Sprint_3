from selenium.webdriver.common.by import By
import module_xpath_constants as constants


def login_module(driver, email, password):
    email_input = driver.find_element(By.XPATH, constants.EMAIL_INPUT)
    password_input = driver.find_element(By.XPATH, constants.PASSWORD_INPUT)
    email_input.send_keys(email)
    password_input.send_keys(password)

    driver.find_element(By.XPATH, constants.LOGIN_BUTTON).click()

def is_element_visible(driver, section):
    return driver.execute_script("""
        var element = arguments[0];
        var bounding = element.getBoundingClientRect();
        return (
            bounding.top >= 0 &&
            bounding.left >= 0 &&
            bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    """, section)
