import requests
import shutil
from typing import Type, TypeVar
from databind.json import from_json, to_json
from pprint import pformat as pf
from requests.auth import AuthBase

from src import log
from src.api.category.base import Base

logger = log.custom_logger(__name__)


class BaseApi(Base):

    REQ = TypeVar('REQ')
    RESP = TypeVar('RESP')

    def get(self, endpoint, resp_binding: Type[RESP]) -> RESP:
        response = requests.get(endpoint, auth=TokenAuth(*self.api_keys_tuple))
        logger.info(self._response_info(response))
        response_obj = from_json(resp_binding, response.json())
        return response_obj

    def post(self, endpoint, req_binding: Type[REQ], resp_binding: Type[RESP] = None) -> RESP:
        if resp_binding is None:
            return self._post_no_resp(endpoint, req_binding)
        else:
            return self._post(endpoint, req_binding, resp_binding)

    def _post_no_resp(self, endpoint, req_binding: Type[REQ]):
        payload = to_json(req_binding)
        response = requests.post(endpoint, data=payload, auth=TokenAuth(*self.api_keys_tuple))
        logger.info(self._response_info(response))
        return response

    def _post(self, endpoint, req_binding: Type[REQ], resp_binding: Type[RESP]) -> RESP:
        payload = to_json(req_binding)
        response = requests.post(endpoint, data=payload, auth=TokenAuth(*self.api_keys_tuple))
        logger.info(self._response_info(response))
        response_obj = from_json(resp_binding, response.json())
        return response_obj

    def delete(self, endpoint):
        response = requests.delete(endpoint, auth=TokenAuth(*self.api_keys_tuple))
        logger.info(self._response_info(response))
        return response

    def _frmt_str(self, string):
        return f'\n{"-" * shutil.get_terminal_size().columns}\n{string}'

    def _response_info(self, response):
        req_target = f'Request:\n {response.request.method} {response.request.url}\n'
        req_body = f'Request body:\n {response.request.body}\n'
        resp_code = f'Response code:\n {response.status_code} {response.reason}\n'
        resp_body = f'Response body:\n {pf(response.json())}\n'
        return self._frmt_str(f'{req_target}{req_body}{resp_code}{resp_body}')


class TokenAuth(AuthBase):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = f'OAuth oauth_consumer_key="{self.key}", oauth_token="{self.token}"'
        return r