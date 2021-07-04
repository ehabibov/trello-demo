from src.api.properties.base_endpoints import BaseEndpoint


class CardEndpoints(BaseEndpoint):

    def __init__(self):
        super().__init__()
        self._cards_endpoint = self.endpoints['Cards']['cards']
        self._card_endpoint = self.endpoints['Cards']['card']
        self._card_comment_endpoint = self.endpoints['Cards']['cardComment']
        self._card_label_endpoint = self.endpoints['Cards']['cardLabel']
        self._card_actions_endpoint = self.endpoints['Cards']['cardActions']

    @property
    def cards_endpoint(self):
        return self.root_endpoint + self._cards_endpoint

    @property
    def card_endpoint(self):
        return self.root_endpoint + self._card_endpoint

    @property
    def card_comment_endpoint(self):
        return self.root_endpoint + self._card_comment_endpoint

    @property
    def card_label_endpoint(self):
        return self.root_endpoint + self._card_label_endpoint

    @property
    def card_actions_endpoint(self):
        return self.root_endpoint + self._card_actions_endpoint
