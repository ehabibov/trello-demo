from src.ui.locators.home_page_locators import HomePageLocators
from src.ui.pages.base_page import BasePage


class HomePage(BasePage):

    def on_page(self):
        return self.find_element(HomePageLocators.home_button())
