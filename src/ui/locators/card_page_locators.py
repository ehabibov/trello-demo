from selenium.webdriver.common.by import By

from src.ui.locators.base_locators import BaseLocators


class CardPageLocators(BaseLocators):

    __COMMENT_FIELD = [By.CSS_SELECTOR, "textarea.comment-box-input.js-new-comment-input"]
    __SAVE_COMMENT_BUTTON = [By.CSS_SELECTOR, "input[value='Save']"]
    __COMMENT = [By.XPATH, "//div[contains(@class, 'js-list-actions')]//div[contains(@class, 'current-comment')]/p"]

    @classmethod
    def comment_field(cls):
        return cls.__COMMENT_FIELD

    @classmethod
    def save_comment_button(cls):
        return cls.__SAVE_COMMENT_BUTTON

    @classmethod
    def comment(cls):
        return cls.__COMMENT

