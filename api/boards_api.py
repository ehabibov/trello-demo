from typing import List
from api.base_api import BaseApi
from bindings.boards_bindings import BoardResponseBinding, BoardRequestBinding


class BoardApi(BaseApi):

    def _get_my_boards_endpoint(self):
        return self.board_endpoints_holder.my_boards_endpoint

    def _get_boards_endpoint(self):
        return self.board_endpoints_holder.boards_endpoint

    def _get_board_endpoint(self, board_id):
        return self.board_endpoints_holder.board_endpoint.replace("{id}", board_id)

    def get_boards(self):
        return self.get(self._get_my_boards_endpoint(), List[BoardResponseBinding])

    def create_board(self, req: BoardRequestBinding):
        return self.post(self._get_boards_endpoint(), req)

    def delete_all_boards(self):
        [self.delete_board(board.id) for board in self.get_boards()]

    def delete_board(self, board_id):
        return self.delete(self._get_board_endpoint(board_id))
