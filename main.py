from collections import namedtuple
from credentials import Credentials
from endpoints import Endpoints


class Base:

    def __init__(self):
        credentials = Credentials()
        self.endpoints = Endpoints()
        ApiKeys = namedtuple('ApiKeys', ['apiKey', 'apiToken'])
        self.api_keys_tuple = ApiKeys(credentials.api_key, credentials.api_token)
