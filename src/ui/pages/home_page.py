from src.ui.locators.home_page_locators import HomePageLocators
from src.ui.pages.base_page import BasePage


class HomePage(BasePage):

    def on_page(self):
        return self.find_element(HomePageLocators.home_button())

    def go_to_board(self, board_name):
        loc = HomePageLocators.board(board_name)
        board = self.find_element(loc)
        board.click()
        self.find_element(HomePageLocators.board_header())
