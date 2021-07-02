import requests
from typing import Type, TypeVar
from databind.json import from_json, to_json
from main import Main, TokenAuth


class BaseApi(Main):

    REQ = TypeVar('REQ')
    RESP = TypeVar('RESP')

    def get(self, endpoint, resp_binding: Type[REQ]) -> REQ:
        response_raw = requests.get(endpoint, auth=TokenAuth(*self.api_credentials_tuple))
        response_obj: resp_binding = from_json(resp_binding, response_raw.json())
        return response_obj

    def post(self, endpoint, req_binding: Type[REQ], **kwargs) -> RESP:
        resp_binding = kwargs.get("resp_binding")
        if resp_binding is None:
            return self._post_no_resp(endpoint, req_binding)
        else:
            return self._post(endpoint, req_binding, resp_binding)

    def _post_no_resp(self, endpoint, req_binding: Type[REQ]):
        payload = to_json(req_binding)
        response = requests.post(endpoint, data=payload, auth=TokenAuth(*self.api_credentials_tuple))
        return response

    def _post(self, endpoint, req_binding: Type[REQ], resp_binding: Type[RESP]) -> RESP:
        payload = to_json(req_binding)
        response_raw = requests.post(endpoint, data=payload, auth=TokenAuth(*self.api_credentials_tuple))
        response_obj: resp_binding = from_json(resp_binding, response_raw.json())
        return response_obj
