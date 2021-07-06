from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://trello.com/login"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                     message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_element_in_element(self, element, locator: list):
        try:
            return element.find_element(locator[0], locator[1])
        except NoSuchElementException:
            print(f"Element with locator {locator} not found")

    def find_elements_in_element(self, element, locator):
        return element.find_elements(locator[0], locator[1])

    def to_site(self):
        return self.driver.get(self.base_url)
