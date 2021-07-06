from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapped_driver = driver.wrapped_driver
        self.base_url = "https://trello.com/login"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                     message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def wait_for_element_to_be_enabled(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_wrapped_element(self, locator, time=10):
        """fallback to standard WebElement due to self.mouse_over() bug"""
        return WebDriverWait(self.wrapped_driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_element_in_element(self, element, locator: list):
        try:
            return element.find_element(locator[0], locator[1])
        except NoSuchElementException:
            print(f"Element with locator {locator} not found")

    def find_elements_in_element(self, element, locator):
        return element.find_elements(locator[0], locator[1])

    def mouse_over(self, element):
        """Fallback to standard WebDriver due effective defect https://github.com/SeleniumHQ/selenium/issues/6604"""
        ActionChains(self.driver).move_to_element(element).perform()

    def to_site(self):
        return self.driver.get(self.base_url)
