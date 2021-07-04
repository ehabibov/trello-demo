from api.boards_api import BoardApi
from api.cards_api import CardApi
from api.lists_api import ListApi
from bindings.boards_bindings import BoardRequestBinding
from bindings.cards_bindings import CardsRequestBinding
from bindings.lists_bindings import ListRequestBinding


def test_delete_all_boards():
    BoardApi().delete_all_boards()


def test_create_board():
    board = BoardRequestBinding()
    board.name = "BoardOne"
    BoardApi().create_board(board)
    BoardApi().get_boards()


def test_create_list():
    board = BoardApi().get_boards().pop()
    list_req = ListRequestBinding()
    list_req.idBoard = board.id
    list_req.name = "MyList"
    new_list = ListApi().create_list(list_req)
    cards_obj_1 = CardsRequestBinding()
    cards_obj_1.idList = new_list.id
    cards_obj_1.name = "Card1"
    cards_obj_1.desc = "Desc1"

    cards_obj_2 = CardsRequestBinding()
    cards_obj_2.idList = new_list.id
    cards_obj_2.name = "Card2"
    cards_obj_2.desc = "Desc2"

    cards_obj_3 = CardsRequestBinding()
    cards_obj_3.idList = new_list.id
    cards_obj_3.name = "Card3"
    cards_obj_3.desc = "Desc3"

    new_card1 = CardApi().create_new_card_in_list(cards_obj_1)
    new_card2 = CardApi().create_new_card_in_list(cards_obj_2)
    new_card3 = CardApi().create_new_card_in_list(cards_obj_3)

    print(new_card1, new_card2, new_card3)
