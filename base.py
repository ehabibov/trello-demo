from collections import namedtuple
from properties.credentials import Credentials
from properties.endpoints_boards import BoardEndpoints


class Base:

    def __init__(self):
        credentials = Credentials()
        self.boardEndpoints = BoardEndpoints()
        ApiKeys = namedtuple('ApiKeys', ['apiKey', 'apiToken'])
        self.api_keys_tuple = ApiKeys(credentials.api_key, credentials.api_token)
