from api.boards_api import BoardApi
from api.cards_api import CardApi
from api.labels import Label
from api.lists_api import ListApi
from bindings.boards_bindings import BoardRequestBinding
from bindings.cards_bindings import CardsRequestBinding, CardLabelRequestBinding, CardCommentRequestBinding
from bindings.lists_bindings import ListRequestBinding


def test_delete_all_boards():
    BoardApi().delete_all_boards()


def test_create_board():
    board_name = "BoardOne"
    board = BoardRequestBinding().with_name(board_name)
    board_api = BoardApi()
    board_api.create_board(board)
    boards = board_api.get_boards()
    assert len(boards) == 1
    assert boards.pop().name == board_name


def test_create_list():
    board_api = BoardApi()
    list_api = ListApi()
    card_api = CardApi()

    board = board_api.get_boards().pop()
    list_req = ListRequestBinding()\
        .with_board_id(board.id).with_name("MyList")
    new_list = list_api.create_list(list_req)

    cards_obj1 = CardsRequestBinding()\
        .with_list_id(new_list.id).with_name("Card1").with_desc("Desc1")
    cards_obj2 = CardsRequestBinding()\
        .with_list_id(new_list.id).with_name("Card2").with_desc("Desc2")
    cards_obj3 = CardsRequestBinding() \
        .with_list_id(new_list.id).with_name("Card3").with_desc("Desc3")

    new_card1 = card_api.create_new_card_in_list(cards_obj1)
    new_card2 = card_api.create_new_card_in_list(cards_obj2)
    new_card3 = card_api.create_new_card_in_list(cards_obj3)

    cards = list_api.get_list_cards(new_list.id)

    assert len(cards) == 3
    assert new_card1 in cards
    assert new_card2 in cards
    assert new_card3 in cards

    card = list_api.get_card_by_board_list_card_name("BoardOne", "MyList", "Card3")
    card_api.delete_card(card.id)
    cards = list_api.get_list_cards(new_list.id)
    assert len(cards) == 2

    card = list_api.get_card_by_board_list_card_name("BoardOne", "MyList", "Card2")
    label_obj = CardLabelRequestBinding().with_color(Label.GREEN)
    card_api.create_label_on_card(card.id, label_obj)

    card = list_api.get_card_by_board_list_card_name("BoardOne", "MyList", "Card1")
    comment = "Comment for Card 1"
    card_comment_obj = CardCommentRequestBinding().with_comment(comment)
    card_api.add_comment_to_card(card.id, card_comment_obj)

    card_actions = card_api.get_card_actions(card.id)
    card_comment = card_actions.pop().data.text

    assert comment == card_comment
