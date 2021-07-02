from collections import namedtuple
from requests.auth import AuthBase
from credentials import Credentials
from endpoints import Endpoints


class Main:

    def __init__(self):
        credentials = Credentials()
        self.endpoints = Endpoints()
        ApiCredentials = namedtuple('ApiCredentials', ['apiKey', 'apiToken'])
        self.api_credentials_tuple = ApiCredentials(credentials.api_key, credentials.api_token)


class TokenAuth(AuthBase):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = f'OAuth oauth_consumer_key="{self.key}", oauth_token="{self.token}"'
        return r