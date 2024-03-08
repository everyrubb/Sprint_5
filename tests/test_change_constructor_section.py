from const import Const


class TestChangeSection:

    def test_change_constructor_section(self, driver, page):
        #Проверка, что работают переходы к разделам в конструкторе:
        driver.get(Const.MAIN_PAGE)

        driver.find_element(*page.sauce_constructor).click()
        assert driver.find_element(*page.header_sauce_constructor)
        driver.find_element(*page.filling_constructor).click()
        assert driver.find_element(*page.header_filling_constructor)
        driver.find_element(*page.bread_constructor).click()
        assert driver.find_element(*page.header_bread_constructor)