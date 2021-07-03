from api_boards import ApiBoards
from bindings.boards import BoardRequestBinding


def test_delete_all_boards():
    boards = ApiBoards()
    boards.delete_all_boards()


def test_create_board():
    board = BoardRequestBinding()
    board.name = "BoardOne"
    api = ApiBoards()
    api.create_board(board)


def test_get_all_boards():
    boards = ApiBoards()
    boards.get_boards()
