from src.ui.locators.card_page_locators import CardPageLocators
from src.ui.pages.base_page import BasePage


class CardPage(BasePage):

    def leave_comment(self, comment):
        comment_field = self.find_element(CardPageLocators.comment_field())
        comment_field.click()
        comment_field.send_keys(comment)
        self.wait_for_element_to_be_enabled(CardPageLocators.save_comment_button())
        save_button = self.find_element(CardPageLocators.save_comment_button())
        save_button.click()

    def get_comments(self, target_comment):
        posted_comments = self.find_elements(CardPageLocators.comment())
        comments = []
        for comment in posted_comments:
            if comment.text == target_comment:
                comments.append(comment)
        return comments
