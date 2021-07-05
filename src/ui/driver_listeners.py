from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class DriverListener(AbstractEventListener):

    def before_click(self, element, driver):
        attributes = f"[tag = {element.tag_name}, text = {element.text}]"
        attributes_js = self.get_attrs_by_js(element, driver)
        print(f"Clicking on: element{attributes} attributes{attributes_js}")

    def before_find(self, by, value, driver):
        print(f"Searching for element with '{by}={value}' on {driver.current_url}")

    def after_find(self, by, value, driver):
        print(f"Found element with '{by}={value}' on {driver.current_url}")

    def after_change_value_of(self, element, driver):
        text = element.get_attribute("value")
        print(f"Sent text: {text}")

    def get_attrs_by_js(self, element, driver):
        script = "let items = {};" + \
                 "for (let index = 0; index < arguments[0].attributes.length; ++index)" + \
                 "{ items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }" + \
                 "return items;"
        return driver.execute_script(script, element)
