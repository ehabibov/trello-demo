from api.base_api import BaseApi
from bindings.cards_bindings import *


class CardApi(BaseApi):

    def _get_cards_endpoint(self):
        return self.card_endpoints_holder.cards_endpoint

    def _get_card_endpoint(self, card_id):
        return self.card_endpoints_holder.card_endpoint.replace("{id}", card_id)

    def _get_card_comment_endpoint(self, card_id):
        return self.card_endpoints_holder.card_comment_endpoint.replace("{id}", card_id)

    def _get_card_label_endpoint(self, card_id):
        return self.card_endpoints_holder.card_label_endpoint.replace("{id}", card_id)

    def _get_card_actions_endpoint(self, card_id):
        return self.card_endpoints_holder.card_actions_endpoint.replace("{id}", card_id)

    def create_new_card_in_list(self, req: CardsRequestBinding):
        return self.post(self._get_cards_endpoint(), req, CardResponseBinding)

    def add_comment_to_card(self, card_id, req: CardCommentRequestBinding):
        return self.post(self._get_card_comment_endpoint(card_id), req)

    def create_label_on_card(self, card_id, req: CardLabelRequestBinding):
        return self.post(self._get_card_label_endpoint(card_id), req)

    def delete_card(self, card_id):
        return self.delete(self._get_card_endpoint(card_id))

    def get_card_actions(self, card_id):
        return self.get(self._get_card_actions_endpoint(card_id), List[CardActionsResponseBinding])
