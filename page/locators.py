from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_INPUT = (By.CSS_SELECTOR, "#searchInput")
    PRODUCT_LINK = (By.CSS_SELECTOR, "a.j-open-full-product-card")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_LINK = (By.CSS_SELECTOR, ".navbar-pc__link.j-main-login")
    FAST_VIEW = (By.CSS_SELECTOR, "button.j-open-product-popup")
    FAVOURITES = (By.CSS_SELECTOR, "button.j-add-to-postpone")
    ADD_TO_CARD = (By.CSS_SELECTOR, "button.btn-main")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#requestCode")
    ERROR_BLOCK = (By.CSS_SELECTOR, ".form-block__message--error")