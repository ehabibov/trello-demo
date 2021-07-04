from api.boards_api import BoardApi
from api.lists_api import ListsApi
from bindings.boards_bindings import BoardRequestBinding
from bindings.lists_bindings import ListRequestBinding


def test_delete_all_boards():
    BoardApi().delete_all_boards()


def test_create_board():
    board = BoardRequestBinding()
    board.name = "BoardOne"
    BoardApi().create_board(board)


def test_get_all_boards():
    BoardApi().get_boards()


def test_create_list():
    board = BoardApi().get_boards().pop()
    list_req = ListRequestBinding()
    list_req.idBoard = board.id
    list_req.name = "MyList"
    ListsApi().create_list(list_req)
