
# Sprint 3

Чек-лист проверок:

**TestRegistration:**

- *test_registration_success* - проверка успешной регистрации. Проверяет совпадает ли созданный email с  email, который находится в личном кабинете.

- *test_registration_error_incorrect_password* - проверка регистрации с невалидными паролями.

**TestLogin:**

- *test_login_from_main_page* - проверка входа на сайт с главной страницы

- *test_login_from_cabinet_button* - проверка входа на сайт через кнопку "Личный кабинет"

- *test_login_from_registration_page* - проверка входа на сайт через страницу регистрации

- *test_login_from_reset_password_page* - проверка входа на сайт через страницу восстановления паролями

**TestCabinet:**

- *test_get_cabinet* - проверка перехода на личный кабинет

**TestFromCabinetConstructor:**

- *test_redirect_to_constructor_from_cabinet* - проверка перехода в конструктор из кабинета

- *test_redirect_to_constructor_from_cabinet_by_click_logo* - проверка перехода в конструктор через логотип

**TestLogout:**

- *test_logout* - проверка выхода из сайта

**TestConstructor:**

- *test_get_burger_section* - проверка перехода на раздел с Булками

- *test_get_sausage_section* - проверка перехода на раздел с соусами

- *test_get_filling_section* - проверка перехода на раздел с начинками