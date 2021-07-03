from api.boards_api import BoardsApi
from bindings.boards_bindings import BoardRequestBinding


def test_delete_all_boards():
    boards = BoardsApi()
    boards.delete_all_boards()


def test_create_board():
    board = BoardRequestBinding()
    board.name = "BoardOne"
    api = BoardsApi()
    api.create_board(board)


def test_get_all_boards():
    boards = BoardsApi()
    boards.get_boards()
