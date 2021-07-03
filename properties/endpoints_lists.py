from properties.base_endpoints import BaseEndpoint


class ListsEndpoints(BaseEndpoint):

    def __init__(self):
        super().__init__()
        self._lists_endpoint = self.endpoints['Lists']['listsEndpoint']
        self._list_endpoint = self.endpoints['Lists']['listEndpoint']

    @property
    def lists_endpoint(self):
        return self._lists_endpoint

    @property
    def list_endpoint(self):
        return self._list_endpoint
