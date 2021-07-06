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

    def move_card_to_list(self, from_list_name, to_list_name, card_name):
        card = self.find_wrapped_element(BoardPageLocators.card_in_list_with_name(from_list_name, card_name))
        self.mouse_over(card)
        edit_button = self.find_element(BoardPageLocators.card_in_list_with_name_edit_button(from_list_name, card_name))
        edit_button.click()
        self.__move_focused_card_on_edit_card_menu(to_list_name)

    def __move_focused_card_on_edit_card_menu(self, to_list_name):
        card_menu_move_button = self.find_element(BoardPageLocators.card_menu_move_button())
        card_menu_move_button.click()
        self.wait_for_element_to_be_enabled(BoardPageLocators.card_move_menu_popup())
        card_move_menu_list_dropdown = self.find_element(BoardPageLocators.card_move_menu_list_dropdown())
        card_move_menu_list_dropdown.click()
        option = self.find_element(BoardPageLocators.card_move_to_list_dropdown_option(to_list_name))
        option.click()
        move_button = self.find_element(BoardPageLocators.card_move_menu_popup_move_button())
        move_button.click()
