from selenium.webdriver.common.by import By
from src.ui.locators.base_locators import BaseLocators


class BoardPageLocators(BaseLocators):

    __LIST = [By.CSS_SELECTOR, "div.list-wrapper"]
    __LIST_NAME = [By.CSS_SELECTOR, "textarea.list-header-name"]
    __CARD = [By.CSS_SELECTOR, "a.list-card"]
    __CARD_NAME = [By.CSS_SELECTOR, "span.list-card-title"]
    __CARD_COMMENT_ICON = [By.CSS_SELECTOR, "span.icon-comment"]
    __LIST_BY_NAME = [By.XPATH, "//textarea[contains(@class, 'list-header-name') and contains(text(), '%s')]"
                                "/ancestor::div[contains(@class, 'list')]"]
    __CARDS_IN_LIST_WITH_NAME = [By.XPATH, "//textarea[contains(@class, 'list-header-name') and contains(text(), '%s')]"
                                           "/ancestor::div[contains(@class, 'list')]//a[contains(@class, 'list-card')]"]
    __CARDS_IN_NAMED_LIST_WITH_NAME = [By.XPATH, "//textarea[contains(@class, 'list-header-name') and contains(text(), '%s')]"
                                                 "/ancestor::div[contains(@class, 'list')]"
                                                 "//span[contains(@class,'list-card-title') and contains(text(), '%s')]"
                                                 "/ancestor::a[contains(@class, 'list-card')]"]
    __CARD_WITH_NAME = [By.XPATH, "//span[contains(@class,'list-card-title') and contains(text(), '%s')]"
                                  "/ancestor::a[contains(@class, 'list_card')]"]

    @classmethod
    def list(cls):
        return cls.__LIST

    @classmethod
    def list_name(cls):
        return cls.__LIST_NAME

    @classmethod
    def card_name(cls):
        return cls.__CARD_NAME

    @classmethod
    def comment_icon(cls):
        return cls.__CARD_COMMENT_ICON

    @classmethod
    def list_by_name(cls, list_name):
        return cls.upd_loc(cls.__LIST_BY_NAME, [list_name])

    @classmethod
    def cards_in_list_by_name(cls, list_name):
        return cls.upd_loc(cls.__CARDS_IN_LIST_WITH_NAME, [list_name])

    @classmethod
    def card_in_list_with_name(cls, list_name, card_name):
        return cls.upd_loc(cls.__CARDS_IN_NAMED_LIST_WITH_NAME, [list_name, card_name])
