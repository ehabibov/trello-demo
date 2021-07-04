from typing import List
from api.base_api import BaseApi
from api.boards_api import BoardApi
from bindings.cards_bindings import CardResponseBinding
from bindings.lists_bindings import ListRequestBinding, CreatedListResponseBinding


class ListApi(BaseApi):

    def _get_lists_endpoint(self):
        return self.list_endpoints_holder.lists_endpoint

    def _get_list_endpoint(self, list_id):
        return self.list_endpoints_holder.list_endpoint.replace("{id}", list_id)

    def _get_list_cards_endpoint(self, list_id):
        return self.list_endpoints_holder.list_cards_endpoint.replace("{id}", list_id)

    def create_list(self, req: ListRequestBinding):
        return self.post(self._get_lists_endpoint(), req, CreatedListResponseBinding)

    def get_list_cards(self, list_id):
        return self.get(self._get_list_cards_endpoint(list_id), List[CardResponseBinding])

    def get_card_by_list_id_and_card_name(self, list_id, card_name):
        for card in self.get_list_cards(list_id):
            if card.name == card_name:
                return card

    def get_cards_by_board_and_list_name(self, board_name, list_name):
        board_api = BoardApi()
        board = board_api.get_board_by_name(board_name)
        lst = board_api.get_list_from_board_id_by_name(board.id, list_name)
        return self.get_list_cards(lst.id)

    def get_card_by_board_list_card_name(self, board_name, list_name, card_name):
        board_api = BoardApi()
        board = board_api.get_board_by_name(board_name)
        lst = board_api.get_list_from_board_id_by_name(board.id, list_name)
        return self.get_card_by_list_id_and_card_name(lst.id, card_name)
