REGISTER_PAGE = "//h2[text()='Регистрация']" # Страница регистрации с заголовком "Регистрация"
NAME_INPUT = "//label[text()='Имя']/following-sibling::input" # Поле ввода имени
EMAIL_INPUT = "//label[text()='Email']/following-sibling::input" # Поле ввода email
PASSWORD_INPUT = "//label[text()='Пароль']/following-sibling::input" # Поле ввода пароля
REGISTER_BUTTON = "//button[text()='Зарегистрироваться']" # Кнопка "Зарегистрироваться" на странице регистрации
LOGIN_PAGE = "//h2[text()='Вход']" # Страница входа с заголовком "Войти"
LOGIN_BUTTON = "//button[text()='Войти']" # Кнопка "Войти" на странице входа
CABINET_LINK = "//a[@href='/account']" # Ссылка на личный кабинет
CABINET_PAGE = "//a[text()='Профиль']" # Ссылка "Профиль" вличном кабинете
CABINET_PAGE_LOGIN_INFO = "//label[text()='Логин']/following-sibling::input" # Поле Email в личном кабинете кабинете
ERROR_MESSAGE_REGISTER = "//p[starts-with(@class,'input__error')]" # Сообщение об ошибке
MAIN_PAGE = "//section/h1[starts-with(text(),'Соберите')]" # Главная страница с заголовком "Соберите бургер"
MAIN_PAGE_LOGIN_BTN = "//button[text()='Войти в аккаунт']" # Кнопка "Войти в аккаунт" на главной странице
LOGGED_IN = "//button[text()='Оформить заказ']" # Кнопка оформить заказ на главной странице
LOGIN_LINK_IN_OTHER_PAGE = "//a[text()='Войти']" # Ссылка "Войти" на страницу входа в других страницах
RESET_PASSWORD_PAGE = "//h2[starts-with(text(),'Восстановление')]" # Страница с заголовком "Восстановление пароля"
CONSTRUCTOR_LINK = "//a[starts-with(@class, 'AppHeader_header__link')]/p[text()='Конструктор']" # Ссылка на главную через "Конструктор"
MAIN_PAGE_MENU_BURGER = "//div[starts-with(@class, 'BurgerIngredients_ingredients__menuContainer')]/h2[1]" # Заголовок "Булки"
LOGO_LINK = "//div[starts-with(@class, 'AppHeader_header__logo')]/a" # Ссылка на лого
LOGOUT_BUTTON = "//button[text()='Выход']" # Кнопка "Выход"
FILLING_TAB = "//div[starts-with(@class, 'tab_tab')]/span[text()='Начинки']" # кнопка "Начинки"
BULKI_TAB = "//div[starts-with(@class, 'tab_tab')]/span[text()='Булки']" # кнопка "Булки"
SAUSAGE_TAB = "//div[starts-with(@class, 'tab_tab')]/span[text()='Соусы']" # кнопка "Соусы"
MAIN_PAGE_MENU_SAUSAGE = "//div[starts-with(@class, 'BurgerIngredients_ingredients__menuContainer')]/h2[2]" # Заголовок "Соусы"
MAIN_PAGE_MENU_FILLING = "//div[starts-with(@class, 'BurgerIngredients_ingredients__menuContainer')]/h2[3]" # Заголовок "Начинки"
