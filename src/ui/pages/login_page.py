from src.ui.locators.login_page_locators import LoginPageLocators
from src.ui.pages.base_page import BasePage


class LoginPage(BasePage):

    def login(self, email, password):
        trello_login_field = self.find_element(LoginPageLocators.trello_login_field())
        trello_login_field.send_keys(email)
        self.find_element(LoginPageLocators.trello_hidden_password_field())
        trello_login_button = self.find_element(LoginPageLocators.trello_login_button())
        trello_login_button.click()
        atlassian_password_field = self.find_element(LoginPageLocators.atlassian_password_field())
        atlassian_password_field.send_keys(password)
        atlassian_login_button = self.find_element(LoginPageLocators.atlassian_login_button())
        atlassian_login_button.click()
