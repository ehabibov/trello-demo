from properties.base_endpoints import BaseEndpoint


class CardsEndpoints(BaseEndpoint):

    def __init__(self):
        super().__init__()
        self._cards_endpoint = self.endpoints['Cards']['cardsEndpoint']
        self._card_endpoint = self.endpoints['Cards']['cardEndpoint']
        self._card_comment_endpoint = self.endpoints['Cards']['cardCommentEndpoint']

    @property
    def cards_endpoint(self):
        return self._cards_endpoint

    @property
    def card_endpoint(self):
        return self._card_endpoint

    @property
    def card_comment_endpoint(self):
        return self._card_comment_endpoint
