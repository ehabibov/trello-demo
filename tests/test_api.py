from api_boards import ApiBoards
from bindings.boards import BoardRequestBinding


def test_get_all_boards():
    boards = ApiBoards().get_boards()
    print(boards)


def test_board_api():
    board = BoardRequestBinding()
    board.name = "Auto1"
    api = ApiBoards()
    api.create_board(board)
