import pytest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from src.credentials import Credentials
from src.ui.driver_listeners import DriverListener
from src.ui.pages.home_page import HomePage
from src.ui.pages.login_page import LoginPage


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    ef_driver = EventFiringWebDriver(driver, DriverListener())
    ef_driver.maximize_window()
    ef_driver.implicitly_wait(10)
    yield ef_driver
    ef_driver.quit()


@pytest.fixture
def credentials():
    return {'email': Credentials().email, 'password': Credentials().password}


def test_login(browser, credentials):
    login_page = LoginPage(browser)
    login_page.to_site()
    login_page.login(credentials.get('email'), credentials.get('password'))
    assert HomePage(browser).on_page() is not None
