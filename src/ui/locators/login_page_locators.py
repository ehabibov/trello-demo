from selenium.webdriver.common.by import By
from src.ui.locators.home_page_locators import BaseLocators


class LoginPageLocators(BaseLocators):

    __TRELLO_USER_LOGIN_FIELD = (By.CSS_SELECTOR, "input#user")
    __TRELLO_HIDDEN_PASSWORD_FIELD = (By.CSS_SELECTOR, "div.show-when-password.hidden")
    __TRELLO_LOGIN_BUTTON = (By.CSS_SELECTOR, "input#login")
    __ATLASSIAN_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    __ATLASSIAN_LOGIN_BUTTON = (By.CSS_SELECTOR, "button#login-submit")

    @classmethod
    def trello_login_field(cls):
        return cls.__TRELLO_USER_LOGIN_FIELD

    @classmethod
    def trello_hidden_password_field(cls):
        return cls.__TRELLO_HIDDEN_PASSWORD_FIELD

    @classmethod
    def trello_login_button(cls):
        return cls.__TRELLO_LOGIN_BUTTON

    @classmethod
    def atlassian_password_field(cls):
        return cls.__ATLASSIAN_PASSWORD_FIELD

    @classmethod
    def atlassian_login_button(cls):
        return cls.__ATLASSIAN_LOGIN_BUTTON
