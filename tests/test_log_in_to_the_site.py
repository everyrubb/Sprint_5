from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from const import Const


class TestLogInToTheSite:

    def test_check_button_log_in_main_page(self, driver, page):
        #вход по кнопке «Войти в аккаунт» на главной – полный флоу
        driver.get(Const.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.button_log_in_account))
        driver.find_element(*page.button_log_in_account).click()
        assert Const.LOGIN_PAGE == driver.current_url
        #авторизовываемся
        driver.find_element(*page.input_email).send_keys(Const.EMAIL)
        driver.find_element(*page.input_password).send_keys(Const.PASSWORD)
        driver.find_element(*page.button_log_in).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_set_an_order)))
        assert driver.find_element(*page.button_set_an_order)

    def test_check_personal_account_in_main_page(self, driver, page):
        #вход через кнопку «Личный кабинет»
        driver.get(Const.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_personal_account)))
        driver.find_element(*page.button_personal_account).click()
        assert driver.find_element(*page.header_log_in_page)
        assert Const.LOGIN_PAGE == driver.current_url

    def test_check_log_in_in_registration_page(self, driver, page):
        #вход через кнопку в форме регистрации
        driver.get(Const.REGISTRATION_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.link_log_in)))
        driver.find_element(*page.link_log_in).click()
        assert driver.find_element(*page.header_log_in_page)
        assert Const.LOGIN_PAGE == driver.current_url

    def test_check_log_in_in_recovery_page(self, driver, page):
        #вход через кнопку в форме восстановления пароля
        driver.get(Const.RECOVERY_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.link_log_in)))
        driver.find_element(*page.link_log_in).click()
        assert driver.find_element(*page.header_log_in_page)
        assert Const.LOGIN_PAGE == driver.current_url
