import pytest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from src.credentials import Credentials
from src.ui.driver_listeners import DriverListener
from src.ui.pages.board_page import BoardPage
from src.ui.pages.card_page import CardPage
from src.ui.pages.home_page import HomePage
from src.ui.pages.login_page import LoginPage


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    ef_driver = EventFiringWebDriver(driver, DriverListener())
    ef_driver.maximize_window()
    ef_driver.implicitly_wait(5)
    yield ef_driver
    ef_driver.quit()


@pytest.fixture
def credentials():
    return {'email': Credentials().email, 'password': Credentials().password}


@pytest.fixture
def login(browser, credentials):
    login_page = LoginPage(browser)
    login_page.to_site()
    login_page.login(credentials.get('email'), credentials.get('password'))
    assert HomePage(browser).on_page() is not None


def test_cards_count(login, browser):
    home_page = HomePage(browser)
    home_page.go_to_board("BoardOne")
    board_page = BoardPage(browser)
    cards = board_page.get_cards_in_list("MyList")
    assert len(cards) == 2
    for card in cards:
        assert board_page.get_card_name(card).text in ['Card1', 'Card2']


def test_cards_with_comment(login, browser):
    home_page = HomePage(browser)
    home_page.go_to_board("BoardOne")
    board_page = BoardPage(browser)
    cards = board_page.get_cards_in_list("MyList")

    cards_with_comment = []
    for card in cards:
        tmp = board_page.get_card_with_comment(card)
        if tmp is not None:
            cards_with_comment.append(tmp)
    assert len(cards_with_comment) == 1


def test_comment_on_commented_card(login, browser):
    home_page = HomePage(browser)
    home_page.go_to_board("BoardOne")
    board_page = BoardPage(browser)
    board_page.go_to_card("MyList", "Card1")
    card_page = CardPage(browser)
    card_page.leave_comment("Test comment")
    comments = card_page.get_comments("Test comment")
    assert len(comments) == 1


def test_move_card_to_done(login, browser):
    home_page = HomePage(browser)
    home_page.go_to_board("BoardOne")
    board_page = BoardPage(browser)
    board_page.move_card_to_list("MyList", "Done", "Card1")

    my_list_cards = board_page.get_cards_in_list("MyList")
    done_cards = board_page.get_cards_in_list("Done")
    assert len(my_list_cards) == 1
    assert len(done_cards) == 1
