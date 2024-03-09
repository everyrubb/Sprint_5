from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from const import Const
from helpers import generate_random_email


class TestRegistration:

    def test_successful_registration(self, driver, page):
        driver.get(Const.REGISTRATION_PAGE)
        #проходим регистрацию на странице регистрации
        driver.find_element(*page.input_name).send_keys(Const.NAME)
        email = generate_random_email()
        driver.find_element(*page.input_email).send_keys(email)
        driver.find_element(*page.input_password).send_keys("cherenkova")
        driver.find_element(*page.button_register).click()
        # проходим авторизацию на странице «Вход»
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_log_in)))
        driver.find_element(*page.input_email).send_keys(email)
        driver.find_element(*page.input_password).send_keys("cherenkova")
        driver.find_element(*page.button_log_in).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_set_an_order)))
        assert driver.find_element(*page.button_set_an_order)
        # проверяем, что вход прошел успешно, сверяя почты в личном кабинете
        driver.find_element(*page.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.menu_item_profile)))
        profile_email = driver.find_element(*page.input_login_personal_account).get_attribute('value')
        assert email == profile_email

    def test_check_incorrect_password(self, driver, page):
        driver.get(Const.REGISTRATION_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_register)))
        driver.find_element(*page.input_name).send_keys(Const.NAME)
        email = generate_random_email()
        driver.find_element(*page.input_email).send_keys(email)
        driver.find_element(*page.input_password).send_keys("cher")
        driver.find_element(*page.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.error_field_password)))
        assert driver.find_element(*page.error_field_password)
