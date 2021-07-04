from collections import namedtuple
from src.credentials import Credentials
from src.api.properties.endpoints_boards import BoardEndpoints
from src.api.properties.endpoints_cards import CardEndpoints
from src.api.properties.endpoints_lists import ListEndpoints


class Base:

    def __init__(self):
        credentials = Credentials()
        self.board_endpoints_holder = BoardEndpoints()
        self.list_endpoints_holder = ListEndpoints()
        self.card_endpoints_holder = CardEndpoints()
        ApiKeys = namedtuple('ApiKeys', ['apiKey', 'apiToken'])
        self.api_keys_tuple = ApiKeys(credentials.api_key, credentials.api_token)
