from src.ui.locators.login_page_locators import LoginPageLocators
from src.ui.pages.base_page import BasePage


class LoginPage(BasePage):

    def login(self, email, password):
        trello_login_field = self.find_element(LoginPageLocators.TRELLO_USER_LOGIN_FIELD)
        trello_login_field.send_keys(email)
        self.find_element(LoginPageLocators.TRELLO_HIDDEN_PASSWORD_FIELD)
        trello_login_button = self.find_element(LoginPageLocators.TRELLO_LOGIN_BUTTON)
        trello_login_button.click()
        atlassian_password_field = self.find_element(LoginPageLocators.ATLASSIAN_PASSWORD_FIELD)
        atlassian_password_field.send_keys(password)
        atlassian_login_button = self.find_element(LoginPageLocators.ATLASSIAN_LOGIN_BUTTON)
        atlassian_login_button.click()
