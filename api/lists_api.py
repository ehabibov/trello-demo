from typing import List
from api.base_api import BaseApi
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

    def get_list_cards(self, list_id, resp: List[CardResponseBinding]):
        return self.get(self._get_list_cards_endpoint(list_id), resp)
