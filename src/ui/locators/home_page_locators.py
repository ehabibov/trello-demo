from selenium.webdriver.common.by import By
from src.ui.locators.base_locators import BaseLocators


class HomePageLocators(BaseLocators):

    __HOME_BUTTON = [By.CSS_SELECTOR, "span[aria-label='HouseIcon']"]
    __BOARD = [By.CSS_SELECTOR, "div[title='BoardOne'].board-tile-details-name"]

    @classmethod
    def home_button(cls):
        return cls.__HOME_BUTTON

    @classmethod
    def board(cls, board_name):
        return cls.upd_loc(cls.__HOME_BUTTON, board_name)
