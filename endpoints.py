import configparser
import definitions


class Endpoints:

    def __init__(self):
        endpoints = configparser.ConfigParser()
        endpoints_path = definitions.ENDPOINTS_CONFIG_PATH
        endpoints.read(endpoints_path)
        self._rootEndpoint = endpoints['Endpoints']['root']
        self._boardsEndpoint = endpoints['Endpoints']['boardsEndpoint']
        self._boardEndpoint = endpoints['Endpoints']['boardEndpoint']

    @property
    def root_endpoint(self):
        return self._rootEndpoint

    @property
    def boards_endpoint(self):
        return self._boardsEndpoint

    @property
    def board_endpoint(self):
        return self._boardEndpoint

