from .page.main_page import MainPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "https://www.wildberries.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    #time.sleep(3)

def test_guest_can_go_to_theme_page(browser):
    link = "https://www.wildberries.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_the_theme_page("книги")
    #time.sleep(3)

def test_guest_should_see_login_link(browser):
    link = "https://www.wildberries.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()
    #time.sleep(3)


def test_visibility_of_fast_view(browser):
    link = "https://www.wildberries.ru/"
    page = MainPage(browser, link)
    page.open()
    page.check_the_visibility_of_fast_view()

#не рабочий
def test_visibility_of_add_to_fav(browser):
    link = "https://www.wildberries.ru/"
    page = MainPage(browser, link)
    page.open()
    page.check_the_visibility_of_add_to_fav()

#не рабочий
def test_add_product_to_card(browser):
    link = "https://www.wildberries.ru/"
    page = MainPage(browser, link)
    page.open()
    page.open_product_card()
    #time.sleep(3)

def test_empty_login(browser):
    link = "https://www.wildberries.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(3)
    #проверили, что скрытый блок теперь виден
    page.try_to_log_in()
    time.sleep(2)

