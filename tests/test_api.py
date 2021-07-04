import pytest
from src.api.category.boards_api import BoardApi
from src.api.category.cards_api import CardApi
from src.api.category.lists_api import ListApi
from src.api.bindings.boards_bindings import BoardRequestBinding
from src.api.bindings.cards_bindings import CardsRequestBinding, CardLabelRequestBinding, CardCommentRequestBinding
from src.api.bindings.lists_bindings import ListRequestBinding
from src.api.labels import Label


def test_delete_all_boards():
    BoardApi().delete_all_boards()


@pytest.fixture
def get_board_name():
    return "BoardOne"


@pytest.fixture
def get_list_name():
    return "MyList"


@pytest.fixture
def card_names():
    return {'c1': "Card1", 'c2': "Card2", 'c3': "Card3"}


@pytest.fixture
def create_cards(get_list_name, card_names):
    board_api = BoardApi()
    list_api = ListApi()

    board = board_api.get_boards().pop()
    list_req = ListRequestBinding() \
        .with_board_id(board.id).with_name(get_list_name)

    lst = list_api.create_list(list_req)

    cards_obj1 = CardsRequestBinding() \
        .with_list_id(lst.id).with_name(card_names.get('c1')).with_desc("Desc1")
    cards_obj2 = CardsRequestBinding() \
        .with_list_id(lst.id).with_name(card_names.get('c2')).with_desc("Desc2")
    cards_obj3 = CardsRequestBinding() \
        .with_list_id(lst.id).with_name(card_names.get('c3')).with_desc("Desc3")

    return [lst, cards_obj1, cards_obj2, cards_obj3]


def test_create_board(get_board_name):

    board = BoardRequestBinding().with_name(get_board_name)
    board_api = BoardApi()
    board_api.create_board(board)
    boards = board_api.get_boards()
    assert len(boards) == 1
    assert boards.pop().name == get_board_name


def test_create_cards(create_cards):
    card_api = CardApi()
    list_api = ListApi()

    new_card1 = card_api.create_new_card_in_list(create_cards[1])
    new_card2 = card_api.create_new_card_in_list(create_cards[2])
    new_card3 = card_api.create_new_card_in_list(create_cards[3])

    cards = list_api.get_list_cards(create_cards[0].id)

    assert len(cards) == 3
    assert new_card1 in cards
    assert new_card2 in cards
    assert new_card3 in cards


def test_edit_card(get_board_name, get_list_name, card_names):
    list_api = ListApi()
    card_api = CardApi()
    label = Label.GREEN

    card = list_api.get_card_by_board_list_card_name(get_board_name, get_list_name, card_names.get('c2'))
    label_obj = CardLabelRequestBinding().with_color(label)
    card_api.create_label_on_card(card.id, label_obj)

    card = list_api.get_card_by_board_list_card_name(get_board_name, get_list_name, card_names.get('c2'))
    assert card.labels.pop().color == label.value


def test_delete_card(get_board_name, get_list_name, card_names):
    board_api = BoardApi()
    list_api = ListApi()
    card_api = CardApi()

    lst = board_api.get_list_from_board_name_by_name(get_board_name, get_list_name)
    card = list_api.get_card_by_board_list_card_name(get_board_name, get_list_name, card_names.get('c3'))
    card_api.delete_card(card.id)
    cards = list_api.get_list_cards(lst.id)
    assert len(cards) == 2


def test_add_comment_to_card(get_board_name, get_list_name, card_names):
    list_api = ListApi()
    card_api = CardApi()
    comment = "Comment for Card 1"

    card = list_api.get_card_by_board_list_card_name(get_board_name, get_list_name, card_names.get('c1'))
    card_comment_obj = CardCommentRequestBinding().with_comment(comment)
    card_api.add_comment_to_card(card.id, card_comment_obj)

    card_actions = card_api.get_card_actions(card.id)
    card_comment = card_actions.pop().data.text

    assert comment == card_comment
