import configparser
import definitions


class Endpoints:

    def __init__(self):
        endpoints = configparser.ConfigParser()
        endpoints_path = definitions.ENDPOINTS_CONFIG_PATH
        endpoints.read(endpoints_path)
        self._root_endpoint = endpoints['Endpoints']['root']
        self._my_boards_endpoint = endpoints['Boards']['myBoardsEndpoint']
        self._board_endpoint = endpoints['Boards']['boardEndpoint']
        self._boards_endpoint = endpoints['Boards']['boardsEndpoint']

    @property
    def root_endpoint(self):
        return self._root_endpoint

    @property
    def my_boards_endpoint(self):
        return self._my_boards_endpoint

    @property
    def board_endpoint(self):
        return self._board_endpoint

    @property
    def boards_endpoint(self):
        return self._boards_endpoint

