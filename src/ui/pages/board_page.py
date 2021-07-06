from src.ui.locators.board_page_locators import BoardPageLocators
from src.ui.pages.base_page import BasePage


class BoardPage(BasePage):

    def get_cards_in_list(self, list_name):
        return self.find_elements(BoardPageLocators.cards_in_list_by_name(list_name))

    def get_card_name(self, card_element):
        return self.find_element_in_element(card_element, BoardPageLocators.card_name())

    def get_card_with_comment(self, card_element):
        return self.find_element_in_element(card_element, BoardPageLocators.comment_icon())
