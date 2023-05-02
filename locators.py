from selenium.webdriver.common.by import By


class Locators:
    NAME_INPUT = By.XPATH, "//label[text()='Имя']/following-sibling::input"  # Поле ввода имени

    EMAIL_INPUT = By.XPATH, "//label[text()='Email']/following-sibling::input"  # Поле ввода email

    ERROR_MESSAGE_REGISTER = By.XPATH, "//p[starts-with(@class,'input__error')]"  # Сообщение об ошибке

    PASSWORD_INPUT = By.XPATH, "//label[text()='Пароль']/following-sibling::input"  # Поле ввода пароля

    REGISTER_PAGE = By.XPATH, "//h2[text()='Регистрация']"  # Страница регистрации с заголовком "Регистрация"

    REGISTER_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']"  # Кнопка "Зарегистрироваться" на странице регистрации

    LOGIN_PAGE = By.XPATH, "//h2[text()='Вход']"  # Страница входа с заголовком "Войти"

    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"  # Кнопка "Войти" на странице входа

    LOGIN_LINK_IN_OTHER_PAGE = By.XPATH, "//a[text()='Войти']"  # Ссылка "Войти" на страницу входа в других страницах

    LOGGED_IN = By.XPATH, "//button[text()='Оформить заказ']"  # Кнопка оформить заказ на главной странице

    CABINET_LINK = By.XPATH, "//a[@href='/account']"  # Ссылка на личный кабинет

    CABINET_PAGE = By.XPATH, "//a[text()='Профиль']"  # Ссылка "Профиль" в личном кабинете

    CABINET_PAGE_LOGIN_INFO = By.XPATH, "//label[text()='Логин']/following-sibling::input"  # Поле Email в личном кабинете кабинете

    MAIN_PAGE = By.XPATH, "//section/h1[starts-with(text(),'Соберите')]"  # Главная страница с заголовком "Соберите бургер"

    MAIN_PAGE_LOGIN_BTN = By.XPATH, "//button[text()='Войти в аккаунт']"  # Кнопка "Войти в аккаунт" на главной странице

    RESET_PASSWORD_PAGE = By.XPATH, "//h2[starts-with(text(),'Восстановление')]"  # Страница с заголовком "Восстановление пароля"

    CONSTRUCTOR_LINK = By.XPATH, "//a[starts-with(@class, 'AppHeader_header__link')]/p[text()='Конструктор']"  # Ссылка на главную через "Конструктор"

    LOGO_LINK = By.XPATH, "//div[starts-with(@class, 'AppHeader_header__logo')]/a"  # Ссылка на лого

    TITLE_BULKI = By.XPATH, "//h2[starts-with(@class, 'text text_type_main-medium') and text()='Булки']"  # Заголовок "Булки"

    BULKI_ITEM = By.XPATH, "//a/p[text()='Флюоресцентная булка R2-D3']"

    TITLE_SAUSAGE = By.XPATH, "//h2[starts-with(@class, 'text text_type_main-medium') and text()='Соусы']"  # Заголовок "Соусы"

    SAUSAGE_ITEM = By.XPATH, "//a/p[text()='Соус Spicy-X']"

    TITLE_FILLING = By.XPATH, "//h2[starts-with(@class, 'text text_type_main-medium') and text()='Начинки']"  # Заголовок "Начинки"

    FILLING_ITEM = By.XPATH, "//a/p[text()='Говяжий метеорит (отбивная)']"

    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выход']"  # Кнопка "Выход"

    BULKI_TAB = By.XPATH, "//div[starts-with(@class, 'tab_tab')]/span[text()='Булки']"  # кнопка "Булки"

    SAUSAGE_TAB = By.XPATH, "//div[starts-with(@class, 'tab_tab')]/span[text()='Соусы']"  # кнопка "Соусы"

    FILLING_TAB = By.XPATH, "//div[starts-with(@class, 'tab_tab')]/span[text()='Начинки']"  # кнопка "Начинки"

