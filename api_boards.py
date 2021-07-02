from typing import List
from api_setup import BaseApi
from bindings.boards import BoardResponseBinding, BoardRequestBinding


class ApiBoards(BaseApi):

    def get_my_boards_endpoint(self):
        return self.endpoints.root_endpoint + self.endpoints.my_boards_endpoint

    def get_board_endpoint(self):
        return self.endpoints.root_endpoint + self.endpoints.boards_endpoint

    def get_boards(self):
        resp_binding = List[BoardResponseBinding]
        endpoint = self.get_my_boards_endpoint()
        boards_obj = self.get(endpoint, resp_binding)
        return boards_obj

    def create_board(self, req: BoardRequestBinding):
        endpoint = self.get_board_endpoint()
        response = self.post(endpoint, req)
        return response
