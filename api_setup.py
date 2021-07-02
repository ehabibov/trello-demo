from typing import List

import requests
import json
from bindings.boards import BoardResponseBinding
from databind.json import from_json
from pprint import pprint as pp
from main import Main, TokenAuth


class Api(Main):

    def get_boards_endpoint(self):
        root_url = self.endpoints.root_endpoint
        boards_url = self.endpoints.boards_endpoint
        return root_url + boards_url

    def get_boards(self):
        endpoint = self.get_boards_endpoint()
        response = requests.get(endpoint, auth=TokenAuth(self.creds_tuple.apiKey, self.creds_tuple.apiToken))
        boards_raw = json.loads(response.content)
        boards_resp: List[BoardResponseBinding] = from_json(List[BoardResponseBinding], boards_raw)
        return boards_resp

    def make_get(self, endpoint, params, headers):
        return requests.get(endpoint, auth=TokenAuth(self.creds_tuple.apiKey, self.creds_tuple.apiToken))


if __name__ == '__main__':
    a = Api().get_boards()
    pp(a)
