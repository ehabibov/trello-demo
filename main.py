from collections import namedtuple
from requests.auth import AuthBase
from credentials import Credentials
from endpoints import Endpoints


class Main:

    def __init__(self):
        self.creds = Credentials()
        self.endpoints = Endpoints()
        Creds = namedtuple('Creds', ['apiKey', 'apiToken'])
        self.creds_tuple = Creds(self.creds.api_key, self.creds.api_token)


if __name__ == '__main__':
    main = Main()
    print(main.creds.api_key)
    print(main.creds.api_token)
    print(main.creds.email)
    print(main.creds.password)
    print(main.endpoints.root_endpoint)
    print(main.endpoints.boards_endpoint)
    print(main.endpoints.board_endpoint)


class TokenAuth(AuthBase):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = f'OAuth oauth_consumer_key="{self.key}", oauth_token="{self.token}"'
        return r