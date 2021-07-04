from src.api.properties.base_endpoints import BaseEndpoint


class BoardEndpoints(BaseEndpoint):

    def __init__(self):
        super().__init__()
        self._my_boards_endpoint = self.endpoints['Boards']['myBoards']
        self._board_endpoint = self.endpoints['Boards']['board']
        self._boards_endpoint = self.endpoints['Boards']['boards']
        self._board_lists_endpoint = self.endpoints['Boards']['boardLists']

    @property
    def my_boards_endpoint(self):
        return self.root_endpoint + self._my_boards_endpoint

    @property
    def board_endpoint(self):
        return self.root_endpoint + self._board_endpoint

    @property
    def boards_endpoint(self):
        return self.root_endpoint + self._boards_endpoint

    @property
    def boards_lists_endpoint(self):
        return self.root_endpoint + self._board_lists_endpoint
