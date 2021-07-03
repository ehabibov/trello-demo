import configparser
import definitions


class BaseEndpoint:

    def __init__(self):
        self.endpoints = configparser.ConfigParser()
        self.endpoints_path = definitions.ENDPOINTS_CONFIG_PATH
        self.endpoints.read(self.endpoints_path)
        self._root_endpoint = self.endpoints['Base']['root']

    @property
    def root_endpoint(self):
        return self._root_endpoint
