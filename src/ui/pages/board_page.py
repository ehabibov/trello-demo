from src.ui.locators.board_page_locators import BoardPageLocators
from src.ui.pages.base_page import BasePage


class BoardPage(BasePage):

    def get_cards_in_list(self, list_name):
        return self.find_elements(BoardPageLocators.cards_in_list_by_name(list_name))

    def get_card_name(self, card_element):
        return self.find_element_in_element(card_element, BoardPageLocators.card_name())

    def get_card_with_comment(self, card_element):
        return self.find_element_in_element(card_element, BoardPageLocators.comment_icon())

    def get_list_by_name(self, list_name):
        return self.find_element(BoardPageLocators.list_by_name(list_name))

    def _get_card_from_named_list_by_name(self, list_name, card_name):
        return self.find_element(BoardPageLocators.card_in_list_with_name(list_name, card_name))

    def go_to_card(self, list_name, card_name):
        card = self._get_card_from_named_list_by_name(list_name, card_name)
        card.click()
