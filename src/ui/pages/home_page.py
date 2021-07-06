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

    def get_cards_on_list(self, list_name):
        return self.find_elements(HomePageLocators.cards_in_list_by_name(list_name))

    def get_card_name(self, card_element):
        return self.find_element_in_element(card_element, HomePageLocators.card_name())
