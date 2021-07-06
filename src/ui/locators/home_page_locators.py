from selenium.webdriver.common.by import By
from src.ui.locators.base_locators import BaseLocators


class HomePageLocators(BaseLocators):

    __HOME_BUTTON = [By.CSS_SELECTOR, "span[aria-label='HouseIcon']"]
    __BOARD = [By.CSS_SELECTOR, "div[title='%s'].board-tile-details-name"]
    __BOARD_HEADER = [By.CSS_SELECTOR, "div.board-header"]
    __LIST = [By.CSS_SELECTOR, "div.list-wrapper"]
    __LIST_NAME = [By.CSS_SELECTOR, "textarea.list-header-name"]
    __CARD = [By.CSS_SELECTOR, "a.list-card"]
    __CARD_NAME = [By.CSS_SELECTOR, "span.list-card-title"]
    __CARD_COMMENT_ICON = [By.CSS_SELECTOR, "span.icon-comment"]
    __LIST_BY_NAME = [By.XPATH, "//textarea[contains(@class, 'list-header-name') and contains(text(), '%s')]"
                                "/ancestor::div[contains(@class, 'list')]"]
    __CARDS_IN_LIST_WITH_NAME = [By.XPATH, "//textarea[contains(@class, 'list-header-name') and contains(text(), '%s')]"
                                           "/ancestor::div[contains(@class, 'list')]//a[contains(@class, 'list-card')]"]

    @classmethod
    def home_button(cls):
        return cls.__HOME_BUTTON

    @classmethod
    def board(cls, board_name):
        return cls.upd_loc(cls.__BOARD, board_name)

    @classmethod
    def board_header(cls):
        return cls.__BOARD_HEADER

    @classmethod
    def list(cls):
        return cls.__LIST

    @classmethod
    def list_name(cls):
        return cls.__LIST

    @classmethod
    def card_name(cls):
        return cls.__CARD_NAME

    @classmethod
    def list_by_name(cls, list_name):
        return cls.upd_loc(cls.__LIST_BY_NAME, list_name)

    @classmethod
    def cards_in_list_by_name(cls, list_name):
        return cls.upd_loc(cls.__CARDS_IN_LIST_WITH_NAME, list_name)
