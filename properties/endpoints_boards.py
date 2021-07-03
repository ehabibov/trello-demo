from properties.base_endpoints import BaseEndpoint


class BoardEndpoints(BaseEndpoint):

    def __init__(self):
        super().__init__()
        self._my_boards_endpoint = self.endpoints['Boards']['myBoardsEndpoint']
        self._board_endpoint = self.endpoints['Boards']['boardEndpoint']
        self._boards_endpoint = self.endpoints['Boards']['boardsEndpoint']

    @property
    def my_boards_endpoint(self):
        return self._my_boards_endpoint

    @property
    def board_endpoint(self):
        return self._board_endpoint

    @property
    def boards_endpoint(self):
        return self._boards_endpoint
