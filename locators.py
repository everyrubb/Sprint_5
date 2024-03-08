from selenium.webdriver.common.by import By

class LocatorsPage:

    @property
    def button_personal_account(self):
        """Кнопка «Личный кабинет» на главной странице"""
        return By.XPATH, "//p[text()='Личный Кабинет']"

    @property
    def button_log_in_account(self):
        """Кнопка «Войти в аккаунт» на главной странице"""
        return By.XPATH, "//button[text()='Войти в аккаунт']"

    @property
    def input_email(self):
        """Инпут Email на странице Входа и на странице регистрации"""
        return By.XPATH, "//label[text()='Email']/../input"

    @property
    def input_password(self):
        """Инпут Пароль на странице Входа и на странице регистрации"""
        return By.XPATH, "//label[text()='Пароль']/../input"

    @property
    def input_login_personal_account(self):
        """Инпут Логин в личном кабинете"""
        return By.XPATH, "//label[text()='Логин']/../input"

    @property
    def input_name(self):
        """Инпут Логин на странице Входа"""
        return By.XPATH, "//label[text()='Имя']/../input"

    @property
    def button_log_in(self):
        """Кнопка «Войти» на странице Входа"""
        return By.XPATH, "//button[text()='Войти']"

    @property
    def button_register(self):
        """Кнопка «Зарегистрироваться» на странице регистрации"""
        return By.XPATH, "//button[text()='Зарегистрироваться']"

    @property
    def error_field_password(self):
        """Нотификция «Некорректный пароль» под инпутом на странице Входа"""
        return By.XPATH, "//form//fieldset[3]//p[text()='Некорректный пароль']"

    @property
    def button_set_an_order(self):
        """Кнопка «Оформитье заказ» на главной странице"""
        return By.XPATH, "//button[text()='Оформить заказ']"

    @property
    def menu_item_log_in(self):
        """Пункт меню «Выход» в личном кабинете"""
        return By.XPATH, "//button[text()='Выход']"

    @property
    def link_log_in(self):
        """Ccылка «Войти» на странице регистрации  и восстановления пароля"""
        return By.XPATH, "//a[text()='Войти']"

    @property
    def header_log_in_page(self):
        """Заголовок «Вход» на странице авторизации"""
        return By.XPATH, "//h2[text()='Вход']"

    @property
    def menu_item_profile(self):
        """Пунт меню «Профиль» в личном кабинете"""
        return By.XPATH, "//a[text()='Профиль']"

    @property
    def main_header_constructor(self):
        """Пункт меню «Конструтор» в шапке сайта"""
        return By.XPATH, "//p[text()='Конструктор']"

    @property
    def header_constructor(self):
        """Заголовок раздела «Конструтор»"""
        return By.XPATH, "//h1[text()='Соберите бургер']"

    @property
    def logo_main_page(self):
        """Логотип сайта"""
        return By.CLASS_NAME, "AppHeader_header__logo__2D0X2"

    @property
    def sauce_constructor(self):
        """Раздел «Соусы» в Конструкторе"""
        return By.XPATH, "//span[text()='Соусы']"

    @property
    def header_sauce_constructor(self):
        """Раздел «Соусы» в Конструкторе"""
        return By.XPATH, "//h2[text()='Соусы']"

    @property
    def filling_constructor(self):
        """Раздел «Начинки» в Конструкторе"""
        return By.XPATH, "//span[text()='Начинки']"

    @property
    def header_filling_constructor(self):
        """Раздел «Начинки» в Конструкторе"""
        return By.XPATH, "//h2[text()='Начинки']"

    @property
    def bread_constructor(self):
        """Раздел «Булки» в Конструкторе"""
        return By.XPATH, "//span[text()='Булки']"

    @property
    def header_bread_constructor(self):
        """Раздел «Булки» в Конструкторе"""
        return By.XPATH, "//h2[text()='Булки']"