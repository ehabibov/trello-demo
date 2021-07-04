from src.api.properties.base_endpoints import BaseEndpoint


class ListEndpoints(BaseEndpoint):

    def __init__(self):
        super().__init__()
        self._lists_endpoint = self.endpoints['Lists']['lists']
        self._list_endpoint = self.endpoints['Lists']['list']
        self._list_cards_endpoint = self.endpoints['Lists']['listCards']

    @property
    def lists_endpoint(self):
        return self.root_endpoint + self._lists_endpoint

    @property
    def list_endpoint(self):
        return self.root_endpoint + self._list_endpoint

    @property
    def list_cards_endpoint(self):
        return self.root_endpoint + self._list_cards_endpoint
