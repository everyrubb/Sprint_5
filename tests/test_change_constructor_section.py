from selenium.webdriver.common.by import By
from selenium import webdriver

class TestChangeSection:

    def test_change_constructor_section(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, '//span[text()="Соусы"]').click()
        assert driver.find_element(By.XPATH, '//h2[text()="Соусы"]')
        driver.find_element(By.XPATH, '//span[text()="Начинки"]').click()
        assert driver.find_element(By.XPATH, '//h2[text()="Начинки"]')
        driver.find_element(By.XPATH, '//span[text()="Булки"]').click()
        assert driver.find_element(By.XPATH, '//h2[text()="Булки"]')

        driver.quit()