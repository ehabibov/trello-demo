from typing import List
from api.base_api import BaseApi
from bindings.boards_bindings import BoardResponseBinding, BoardRequestBinding


class BoardsApi(BaseApi):

    def get_my_boards_endpoint(self):
        return self.boardEndpoints.root_endpoint + self.boardEndpoints.my_boards_endpoint

    def get_boards_endpoint(self):
        return self.boardEndpoints.root_endpoint + self.boardEndpoints.boards_endpoint

    def get_board_endpoint(self, board_id):
        return self.boardEndpoints.root_endpoint + self.boardEndpoints.board_endpoint.replace("{id}", board_id)

    def get_boards(self):
        resp_binding = List[BoardResponseBinding]
        endpoint = self.get_my_boards_endpoint()
        boards_obj = self.get(endpoint, resp_binding)
        return boards_obj

    def create_board(self, req: BoardRequestBinding):
        endpoint = self.get_boards_endpoint()
        response = self.post(endpoint, req)
        return response

    def delete_all_boards(self):
        [self.delete_board(board.id) for board in self.get_boards()]

    def delete_board(self, board_id):
        endpoint = self.get_board_endpoint(board_id)
        return self.delete(endpoint)
