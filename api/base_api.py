import requests
import shutil
from typing import Type, TypeVar
from databind.json import from_json, to_json
from pprint import pformat as pf
from requests.auth import AuthBase
from base import Base


class BaseApi(Base):

    REQ = TypeVar('REQ')
    RESP = TypeVar('RESP')

    def get(self, endpoint, resp_binding: Type[REQ]) -> REQ:
        response = requests.get(endpoint, auth=TokenAuth(*self.api_keys_tuple))
        self._print_resp(response)
        response_obj: resp_binding = from_json(resp_binding, response.json())
        return response_obj

    def post(self, endpoint, req_binding: Type[REQ], **kwargs) -> RESP:
        resp_binding = kwargs.get("resp_binding")
        if resp_binding is None:
            return self._post_no_resp(endpoint, req_binding)
        else:
            return self._post(endpoint, req_binding, resp_binding)

    def _post_no_resp(self, endpoint, req_binding: Type[REQ]):
        payload = to_json(req_binding)
        response = requests.post(endpoint, data=payload, auth=TokenAuth(*self.api_keys_tuple))
        self._print_resp(response)
        return response

    def _post(self, endpoint, req_binding: Type[REQ], resp_binding: Type[RESP]) -> RESP:
        payload = to_json(req_binding)
        response = requests.post(endpoint, data=payload, auth=TokenAuth(*self.api_keys_tuple))
        self._print_resp(response)
        response_obj: resp_binding = from_json(resp_binding, response.json())
        return response_obj

    def delete(self, endpoint):
        response = requests.delete(endpoint, auth=TokenAuth(*self.api_keys_tuple))
        self._print_resp(response)
        return response

    def _frmt_str(self, string):
        return f'\n{"-" * shutil.get_terminal_size().columns}\n{string}'

    def _print_resp(self, response):
        req_target = f'Request:\n {response.request.method} {response.request.url}\n'
        req_body = f'Request body:\n {response.request.body}\n'
        resp_code = f'Response code:\n {response.status_code} {response.reason}\n'
        resp_body = f'Response body:\n {pf(response.json())}\n'
        formatted = self._frmt_str(f'{req_target}{req_body}{resp_code}{resp_body}')
        print(formatted)


class TokenAuth(AuthBase):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = f'OAuth oauth_consumer_key="{self.key}", oauth_token="{self.token}"'
        return r