from typing import List
from src.api.category.base_api import BaseApi
from src.api.bindings.boards_bindings import BoardResponseBinding, BoardRequestBinding
from src.api.bindings.lists_bindings import ListResponseBinding


class BoardApi(BaseApi):

    def _get_my_boards_endpoint(self):
        return self.board_endpoints_holder.my_boards_endpoint

    def _get_boards_endpoint(self):
        return self.board_endpoints_holder.boards_endpoint

    def _get_board_endpoint(self, board_id):
        return self.board_endpoints_holder.board_endpoint.replace("{id}", board_id)

    def _get_board_lists_endpoint(self, board_id):
        return self.board_endpoints_holder.boards_lists_endpoint.replace("{id}", board_id)

    def get_boards(self):
        return self.get(self._get_my_boards_endpoint(), List[BoardResponseBinding])

    def get_board_by_name(self, board_name):
        for board in self.get_boards():
            if board.name == board_name:
                return board

    def create_board(self, req: BoardRequestBinding):
        return self.post(self._get_boards_endpoint(), req)

    def delete_all_boards(self):
        [self.delete_board(board.id) for board in self.get_boards()]

    def delete_board(self, board_id):
        return self.delete(self._get_board_endpoint(board_id))

    def get_lists_from_board(self, board_id):
        return self.get(self._get_board_lists_endpoint(board_id), List[ListResponseBinding])

    def get_list_from_board(self, board_id, list_name):
        for lst in self.get_lists_from_board(board_id):
            if lst.name == list_name:
                return lst

    def get_list_from_board_id_by_name(self, board_id, list_name):
        for lst in self.get_lists_from_board(board_id):
            if lst.name == list_name:
                return lst

    def get_list_from_board_name_by_name(self, board_name, list_name):
        board = self.get_board_by_name(board_name)
        for lst in self.get_lists_from_board(board.id):
            if lst.name == list_name:
                return lst