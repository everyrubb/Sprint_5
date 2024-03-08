from selenium.webdriver.common.by import By
from selenium import webdriver

class TestRegistration:

    def test_successful_registration(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.XPATH, "//label[text()='Имя']/../input").send_keys("Antonina")
        driver.find_element(By.XPATH, "//label[text()='Email']/../input").send_keys("cherenkova_6@yandex.ru")
        driver.find_element(By.XPATH, "//label[text()='Пароль']/../input").send_keys("cherenkova")
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        #driver.find_element(By.XPATH, "//h2[text()='Вход']")

        driver.quit()