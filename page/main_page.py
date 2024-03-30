from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    def go_to_the_theme_page(self, category):
        category_page = self.browser.find_element(
            *MainPageLocators.SEARCH_INPUT)
        category_page.send_keys(category)
        category_page.send_keys(Keys.RETURN)

    def go_to_login_page(self):
        login_link = self.browser.find_element(
            *MainPageLocators.LOGIN_LINK).get_attribute("href")
        # новые вкладки Хром не открывает, так что сделаем это вручную
        self.browser.execute_script(f"window.open('{login_link}');")
        self.browser.switch_to.window(self.browser.window_handles[1])

    def should_be_login_page(self):
        assert "login" in self.browser.current_url, "This is not a login page"

    def check_the_visibility_of_fast_view(self):
        assert self.is_element_present(
            *MainPageLocators.FAST_VIEW), "Element is not presented"

        assert self.browser.find_element(
            *MainPageLocators.FAST_VIEW).is_displayed(), "Button 'fast-view' is not displayed"

    def check_the_visibility_of_add_to_fav(self):
        assert self.is_element_present(
            *MainPageLocators.FAVOURITES), "Element is not presented"

        assert not self.browser.find_element(
            *MainPageLocators.FAVOURITES).is_displayed(), "Button 'add to fav' is displayed, but it's not really visible, and that's the problem."

    def open_product_card(self):
        product_pages = self.browser.find_elements(
            *MainPageLocators.PRODUCT_LINK)

        page1 = product_pages[0].get_attribute('href')
        self.browser.execute_script(f"window.open('{page1}');")
        page2 = product_pages[1].get_attribute('href')
        self.browser.execute_script(f"window.open('{page2}');")

        # страницам нужно время, если я пытаюсь окрыть первую сразу после создания,
        # то напишет, что элемент не найден
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.switch_to.window(self.browser.window_handles[2])

        add_to_card = self.browser.find_element(
            *MainPageLocators.ADD_TO_CARD)
        add_to_card.click()

    def try_to_log_in(self):
        clik_on_button = self.browser.find_element(
            *MainPageLocators.LOGIN_BUTTON)
        clik_on_button.click()
        result = self.browser.find_element(
            *MainPageLocators.ERROR_BLOCK)
        assert result.text == "Введите номер, чтобы получить код" and result.is_displayed()
