from api.boards_api import BoardApi
from api.cards_api import CardApi
from api.lists_api import ListApi
from bindings.boards_bindings import BoardRequestBinding
from bindings.cards_bindings import CardsRequestBinding
from bindings.lists_bindings import ListRequestBinding


def test_delete_all_boards():
    BoardApi().delete_all_boards()


def test_create_board():
    board = BoardRequestBinding().with_name("BoardOne")
    board_api = BoardApi()
    board_api.create_board(board)
    board_api.get_boards()


def test_create_list():
    board_api = BoardApi()
    list_api = ListApi()
    card_api = CardApi()
    
    board = board_api.get_boards().pop()
    list_req = ListRequestBinding()\
        .with_board_id(board.id).with_name("MyList")
    new_list = list_api.create_list(list_req)

    cards_obj1 = CardsRequestBinding()\
        .with_idlist(new_list.id).with_name("Card1").with_desc("Desc1")
    cards_obj2 = CardsRequestBinding()\
        .with_idlist(new_list.id).with_name("Card2").with_desc("Desc2")
    cards_obj3 = CardsRequestBinding() \
        .with_idlist(new_list.id).with_name("Card3").with_desc("Desc3")

    new_card1 = card_api.create_new_card_in_list(cards_obj1)
    new_card2 = card_api.create_new_card_in_list(cards_obj2)
    new_card3 = card_api.create_new_card_in_list(cards_obj3)

    print(new_card1, new_card2, new_card3)

    cards = list_api.get_list_cards(new_list.id)
    assert len(cards) == 3

    card = list_api.get_card_by_board_list_card_name("BoardOne", "MyList", "Card3")
    card_api.delete_card(card.id)
