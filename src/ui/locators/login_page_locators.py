from selenium.webdriver.common.by import By


class LoginPageLocators:

    TRELLO_USER_LOGIN_FIELD = (By.CSS_SELECTOR, "input#user")
    TRELLO_HIDDEN_PASSWORD_FIELD = (By.CSS_SELECTOR, "div.show-when-password.hidden")
    TRELLO_LOGIN_BUTTON = (By.CSS_SELECTOR, "input#login")
    ATLASSIAN_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    ATLASSIAN_LOGIN_BUTTON = (By.CSS_SELECTOR, "button#login-submit")
